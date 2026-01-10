#!/usr/bin/env python3
import argparse
import json
import os
import socket
import subprocess
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path
from urllib.parse import quote


DEFAULT_PORT = 9847
API_PORT_ENV = "NOTEBOOK_VIEWER_API_PORT"


def repo_root() -> Path:
    return Path(__file__).resolve().parent


def context_dir() -> Path:
    d = repo_root() / ".context"
    d.mkdir(parents=True, exist_ok=True)
    return d


def safe_instance_name(name: str) -> str:
    name = name.strip()
    safe = "".join(ch if (ch.isalnum() or ch in "-_") else "_" for ch in name)
    return safe or "default"


def instance_suffix(instance: str) -> str:
    instance = safe_instance_name(instance)
    if instance == "default":
        return ""
    return f".{instance}"


def config_path(instance: str) -> Path:
    return context_dir() / f"notebook-viewer{instance_suffix(instance)}.json"


def log_path(instance: str) -> Path:
    return context_dir() / f"notebook-viewer{instance_suffix(instance)}.log"


def load_config(instance: str) -> dict | None:
    path = config_path(instance)
    if not path.exists():
        return None
    try:
        return json.loads(path.read_text())
    except Exception:
        return None


def save_config(instance: str, cfg: dict):
    config_path(instance).write_text(json.dumps(cfg, indent=2, sort_keys=True) + "\n")


def expected_notebooks_dir() -> Path:
    return (repo_root() / "notebooks").resolve()


def api_base(port: int) -> str:
    return f"http://127.0.0.1:{port}"


def http_json(api: str, method: str, path: str, payload=None, timeout_s: float = 5.0):
    url = f"{api}{path}"
    data = None
    headers = {}
    if payload is not None:
        data = json.dumps(payload).encode("utf-8")
        headers["content-type"] = "application/json"

    req = urllib.request.Request(url, data=data, method=method, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=timeout_s) as resp:
            raw = resp.read()
            if not raw:
                return None
            return json.loads(raw.decode("utf-8"))
    except urllib.error.HTTPError as e:
        raw = e.read()
        try:
            err = json.loads(raw.decode("utf-8"))
        except Exception:
            err = {"ok": False, "error": raw.decode("utf-8", errors="replace")}
        raise RuntimeError(f"HTTP {e.code}: {json.dumps(err)}") from None


def probe_api(port: int) -> tuple[str, dict | None]:
    api = api_base(port)
    try:
        status = http_json(api, "GET", "/status", timeout_s=0.5)
    except (urllib.error.URLError, TimeoutError, ConnectionRefusedError, OSError):
        return ("free", None)
    except Exception:
        return ("other", None)

    if not isinstance(status, dict):
        return ("other", None)
    if status.get("ok") is not True or status.get("app") != "notebook-viewer":
        return ("other", status)

    nb = status.get("notebooks_dir")
    if isinstance(nb, str):
        try:
            if Path(nb).resolve() != expected_notebooks_dir():
                return ("other", status)
        except Exception:
            return ("other", status)

    return ("ours", status)


def pick_free_port() -> int:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("127.0.0.1", 0))
        return int(s.getsockname()[1])


def ensure_built() -> Path:
    repo = Path(__file__).resolve().parent
    src_tauri = repo / "src-tauri"
    bin_path = src_tauri / "target" / "debug" / "notebook-viewer"
    subprocess.run(["cargo", "build"], cwd=src_tauri, check=True)
    if not bin_path.exists():
        raise RuntimeError(f"expected binary at {bin_path}")
    return bin_path


MAX_LOG_SIZE = 1024 * 1024  # 1MB


def resolve_api_port(instance: str, override_port: int | None) -> int | None:
    if override_port is not None:
        return override_port
    cfg = load_config(instance) or {}
    port = cfg.get("api_port")
    return port if isinstance(port, int) else None


def ensure_daemon(args, timeout_s: float = 10.0):
    instance = safe_instance_name(args.instance)
    port = resolve_api_port(instance, args.api_port)

    if port is not None:
        state, _ = probe_api(port)
        if state == "ours":
            return
        if args.api_port is not None and state != "free":
            raise RuntimeError(f"API port {port} is in use")
        if state != "free":
            port = None

    if port is None:
        if instance == "default":
            state, _ = probe_api(DEFAULT_PORT)
            if state == "free":
                port = DEFAULT_PORT
            elif state == "ours":
                save_config(instance, {"api_port": DEFAULT_PORT})
                return
            else:
                port = pick_free_port()
        else:
            port = pick_free_port()

    repo = Path(__file__).resolve().parent
    src_tauri = repo / "src-tauri"
    bin_path = ensure_built()

    log = log_path(instance)

    # Rotate log if too large
    if log.exists() and log.stat().st_size > MAX_LOG_SIZE:
        old_log = log.with_suffix(log.suffix + ".old")
        if old_log.exists():
            old_log.unlink()
        log.rename(old_log)

    env = os.environ.copy()
    env[API_PORT_ENV] = str(port)

    with open(log, "ab") as fp:
        proc = subprocess.Popen(
            [str(bin_path)],
            cwd=src_tauri,
            stdout=fp,
            stderr=fp,
            start_new_session=True,
            env=env,
        )

    save_config(instance, {"api_port": port, "pid": proc.pid})

    started = time.time()
    while time.time() - started < timeout_s:
        state, _ = probe_api(port)
        if state == "ours":
            return
        time.sleep(0.1)

    raise RuntimeError(
        f"viewer did not start within {timeout_s:.1f}s; see log at {log}"
    )


def cmd_start(_args):
    ensure_daemon(_args)
    instance = safe_instance_name(_args.instance)
    port = resolve_api_port(instance, _args.api_port)
    if port is None:
        raise RuntimeError("missing api port after start")
    print(json.dumps(http_json(api_base(port), "GET", "/status"), indent=2))


def cmd_stop(_args):
    instance = safe_instance_name(_args.instance)
    cfg = load_config(instance) or {}
    port = resolve_api_port(instance, _args.api_port)

    if port is None and instance == "default":
        state, _ = probe_api(DEFAULT_PORT)
        if state == "ours":
            port = DEFAULT_PORT

    if port is None:
        return

    try:
        http_json(api_base(port), "POST", "/shutdown", payload={}, timeout_s=2.0)
    except (urllib.error.URLError, TimeoutError, ConnectionRefusedError):
        # Server not running - this is fine
        pass
    except RuntimeError as e:
        print(f"Note: shutdown request failed: {e}", file=sys.stderr)

    pid = cfg.get("pid") if isinstance(cfg.get("pid"), int) else None
    config_path(instance).unlink(missing_ok=True)

    if pid is not None:
        try:
            os.kill(pid, 0)
        except OSError:
            # Process not running
            return
        try:
            os.kill(pid, 15)
        except OSError as e:
            print(f"Note: failed to send SIGTERM to {pid}: {e}", file=sys.stderr)


def cmd_status(_args):
    ensure_daemon(_args)
    instance = safe_instance_name(_args.instance)
    port = resolve_api_port(instance, _args.api_port)
    if port is None:
        raise RuntimeError("missing api port after status")
    print(json.dumps(http_json(api_base(port), "GET", "/status"), indent=2))


def cmd_open(args):
    ensure_daemon(args)
    path = Path(args.path).expanduser().resolve()
    instance = safe_instance_name(args.instance)
    port = resolve_api_port(instance, args.api_port)
    if port is None:
        raise RuntimeError("missing api port after start")
    res = http_json(api_base(port), "POST", "/open", {"path": str(path)}, timeout_s=60.0)
    print(json.dumps(res, indent=2))

    if args.wait:
        idle_res = http_json(
            api_base(port),
            "POST",
            "/wait-idle",
            {"timeout_ms": args.wait_timeout_ms},
            timeout_s=max(5.0, args.wait_timeout_ms / 1000.0 + 1.0),
        )
        print(json.dumps(idle_res, indent=2))


def cmd_show(_args):
    ensure_daemon(_args)
    instance = safe_instance_name(_args.instance)
    port = resolve_api_port(instance, _args.api_port)
    if port is None:
        raise RuntimeError("missing api port after start")
    print(json.dumps(http_json(api_base(port), "POST", "/window/show", {}), indent=2))


def cmd_hide(_args):
    ensure_daemon(_args)
    instance = safe_instance_name(_args.instance)
    port = resolve_api_port(instance, _args.api_port)
    if port is None:
        raise RuntimeError("missing api port after start")
    print(json.dumps(http_json(api_base(port), "POST", "/window/hide", {}), indent=2))


def cmd_reload(_args):
    ensure_daemon(_args)
    instance = safe_instance_name(_args.instance)
    port = resolve_api_port(instance, _args.api_port)
    if port is None:
        raise RuntimeError("missing api port after start")
    print(json.dumps(http_json(api_base(port), "POST", "/reload", {}), indent=2))


def cmd_wait_idle(args):
    ensure_daemon(args)
    instance = safe_instance_name(args.instance)
    port = resolve_api_port(instance, args.api_port)
    if port is None:
        raise RuntimeError("missing api port after start")
    res = http_json(
        api_base(port),
        "POST",
        "/wait-idle",
        {"timeout_ms": args.timeout_ms},
        timeout_s=max(5.0, args.timeout_ms / 1000.0 + 1.0),
    )
    print(json.dumps(res, indent=2))


def cmd_eval(args):
    ensure_daemon(args)
    instance = safe_instance_name(args.instance)
    port = resolve_api_port(instance, args.api_port)
    if port is None:
        raise RuntimeError("missing api port after start")
    res = http_json(
        api_base(port),
        "POST",
        "/eval",
        {"code": args.code, "timeout_ms": args.timeout_ms},
        timeout_s=max(5.0, args.timeout_ms / 1000.0 + 1.0),
    )
    print(json.dumps(res, indent=2))


def cmd_cells(_args):
    ensure_daemon(_args)
    instance = safe_instance_name(_args.instance)
    port = resolve_api_port(instance, _args.api_port)
    if port is None:
        raise RuntimeError("missing api port after start")
    print(json.dumps(http_json(api_base(port), "GET", "/cells"), indent=2))


def cmd_cell(args):
    ensure_daemon(args)
    name = quote(args.name, safe="")
    instance = safe_instance_name(args.instance)
    port = resolve_api_port(instance, args.api_port)
    if port is None:
        raise RuntimeError("missing api port after start")
    print(json.dumps(http_json(api_base(port), "GET", f"/cell/{name}"), indent=2))


def cmd_screenshot(args):
    ensure_daemon(args)
    instance = safe_instance_name(args.instance)
    port = resolve_api_port(instance, args.api_port)
    if port is None:
        raise RuntimeError("missing api port after start")
    if args.selector:
        res = http_json(
            api_base(port),
            "POST",
            "/screenshot/element",
            {"selector": args.selector, "padding": args.padding},
            timeout_s=20.0,
        )
    else:
        res = http_json(api_base(port), "POST", "/screenshot", {}, timeout_s=20.0)
    print(json.dumps(res, indent=2))


def cmd_logs(args):
    ensure_daemon(args)
    instance = safe_instance_name(args.instance)
    port = resolve_api_port(instance, args.api_port)
    if port is None:
        raise RuntimeError("missing api port after start")
    path = f"/logs?clear={str(args.clear).lower()}"
    print(json.dumps(http_json(api_base(port), "GET", path), indent=2))


def cmd_set_input(args):
    ensure_daemon(args)
    # Parse value as JSON if possible, otherwise use as string
    try:
        value = json.loads(args.value)
    except json.JSONDecodeError:
        value = args.value
    instance = safe_instance_name(args.instance)
    port = resolve_api_port(instance, args.api_port)
    if port is None:
        raise RuntimeError("missing api port after start")
    res = http_json(api_base(port), "POST", "/input", {"selector": args.selector, "value": value})
    print(json.dumps(res, indent=2))


def cmd_click(args):
    ensure_daemon(args)
    instance = safe_instance_name(args.instance)
    port = resolve_api_port(instance, args.api_port)
    if port is None:
        raise RuntimeError("missing api port after start")
    res = http_json(api_base(port), "POST", "/click", {"selector": args.selector})
    print(json.dumps(res, indent=2))


def cmd_notebooks(_args):
    ensure_daemon(_args)
    instance = safe_instance_name(_args.instance)
    port = resolve_api_port(instance, _args.api_port)
    if port is None:
        raise RuntimeError("missing api port after start")
    print(json.dumps(http_json(api_base(port), "GET", "/notebooks"), indent=2))


def cmd_page_loads(_args):
    ensure_daemon(_args)
    instance = safe_instance_name(_args.instance)
    port = resolve_api_port(instance, _args.api_port)
    if port is None:
        raise RuntimeError("missing api port after start")
    print(json.dumps(http_json(api_base(port), "GET", "/page-loads"), indent=2))


def cmd_browse(args):
    """Open the notebook catalog and show the window."""
    ensure_daemon(args)
    instance = safe_instance_name(args.instance)
    port = resolve_api_port(instance, args.api_port)
    if port is None:
        raise RuntimeError("missing api port after start")

    # Open the index page (catalog)
    index_path = expected_notebooks_dir() / "src" / "index.md"
    http_json(api_base(port), "POST", "/open", {"path": str(index_path)}, timeout_s=60.0)

    # Wait for it to be ready (best effort - proceed even if it times out)
    try:
        http_json(
            api_base(port),
            "POST",
            "/wait-idle",
            {"timeout_ms": 10000},
            timeout_s=15.0,
        )
    except RuntimeError:
        pass  # Page may still be loading, but show anyway

    # Show the window
    http_json(api_base(port), "POST", "/window/show", {})
    print(json.dumps({"ok": True, "opened": str(index_path)}, indent=2))


def cmd_verify(args):
    ensure_daemon(args)
    instance = safe_instance_name(args.instance)
    port = resolve_api_port(instance, args.api_port)
    if port is None:
        raise RuntimeError("missing api port after start")
    payload = {
        "timeout_ms": args.timeout_ms,
        "screenshot_padding": args.padding,
        "include_controls": args.include_controls,
    }
    # Use a longer HTTP timeout since verify does multiple screenshots
    res = http_json(
        api_base(port),
        "POST",
        "/verify",
        payload,
        timeout_s=max(30.0, args.timeout_ms / 1000.0 + 10.0),
    )
    print(json.dumps(res, indent=2))


def main(argv: list[str]) -> int:
    p = argparse.ArgumentParser(prog="viewer.py")
    p.add_argument("--instance", default="default", help="Viewer instance name (separate process + API port)")
    p.add_argument("--api-port", type=int, help="Override API port for this instance")
    sub = p.add_subparsers(dest="cmd", required=True)

    sub.add_parser("start").set_defaults(fn=cmd_start)
    sub.add_parser("stop").set_defaults(fn=cmd_stop)
    sub.add_parser("status").set_defaults(fn=cmd_status)

    open_p = sub.add_parser("open")
    open_p.add_argument("path")
    open_p.add_argument("--wait", action="store_true", help="Wait for notebook to be idle after opening")
    open_p.add_argument("--wait-timeout-ms", type=int, default=10000, help="Timeout for --wait in milliseconds")
    open_p.set_defaults(fn=cmd_open)

    sub.add_parser("show").set_defaults(fn=cmd_show)
    sub.add_parser("hide").set_defaults(fn=cmd_hide)
    sub.add_parser("reload").set_defaults(fn=cmd_reload)

    w = sub.add_parser("wait-idle")
    w.add_argument("--timeout-ms", type=int, default=5000)
    w.set_defaults(fn=cmd_wait_idle)

    e = sub.add_parser("eval")
    e.add_argument("code")
    e.add_argument("--timeout-ms", type=int, default=5000)
    e.set_defaults(fn=cmd_eval)

    sub.add_parser("cells").set_defaults(fn=cmd_cells)
    c = sub.add_parser("cell")
    c.add_argument("name")
    c.set_defaults(fn=cmd_cell)

    s = sub.add_parser("screenshot")
    s.add_argument("--selector")
    s.add_argument("--padding", type=int, default=16)
    s.set_defaults(fn=cmd_screenshot)

    logs_p = sub.add_parser("logs")
    logs_p.add_argument("--clear", action="store_true", help="Clear logs after retrieving")
    logs_p.set_defaults(fn=cmd_logs)

    input_p = sub.add_parser("set-input")
    input_p.add_argument("selector", help="CSS selector for the input element")
    input_p.add_argument("value", help="Value to set (JSON or string)")
    input_p.set_defaults(fn=cmd_set_input)

    click_p = sub.add_parser("click")
    click_p.add_argument("selector", help="CSS selector for the element to click")
    click_p.set_defaults(fn=cmd_click)

    sub.add_parser("notebooks").set_defaults(fn=cmd_notebooks)
    sub.add_parser("page-loads").set_defaults(fn=cmd_page_loads)
    sub.add_parser("browse", help="Open the notebook catalog and show the window").set_defaults(fn=cmd_browse)

    verify_p = sub.add_parser("verify", help="Verify notebook: discover charts, take screenshots, check errors")
    verify_p.add_argument("--timeout-ms", type=int, default=10000, help="Timeout for waiting for idle")
    verify_p.add_argument("--padding", type=int, default=16, help="Padding around screenshots")
    verify_p.add_argument("--include-controls", action="store_true", help="Also capture UI controls (inputs, sliders)")
    verify_p.set_defaults(fn=cmd_verify)

    args = p.parse_args(argv)
    args.fn(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))

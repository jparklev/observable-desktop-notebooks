#!/usr/bin/env python3
import argparse
import json
import os
import subprocess
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path
from urllib.parse import quote


API = "http://127.0.0.1:9847"
PID_FILE = Path.home() / ".notebook-viewer.pid"


def http_json(method: str, path: str, payload=None, timeout_s: float = 5.0):
    url = f"{API}{path}"
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


def is_running() -> bool:
    try:
        http_json("GET", "/status", timeout_s=0.5)
        return True
    except (urllib.error.URLError, TimeoutError, ConnectionRefusedError):
        return False
    except RuntimeError:
        # HTTP error from server - it's running but returned an error
        return True


def ensure_built() -> Path:
    repo = Path(__file__).resolve().parent
    src_tauri = repo / "src-tauri"
    bin_path = src_tauri / "target" / "debug" / "notebook-viewer"
    subprocess.run(["cargo", "build"], cwd=src_tauri, check=True)
    if not bin_path.exists():
        raise RuntimeError(f"expected binary at {bin_path}")
    return bin_path


MAX_LOG_SIZE = 1024 * 1024  # 1MB


def ensure_daemon(timeout_s: float = 10.0):
    if is_running():
        return

    repo = Path(__file__).resolve().parent
    src_tauri = repo / "src-tauri"
    bin_path = ensure_built()

    log_dir = repo / ".context"
    log_dir.mkdir(parents=True, exist_ok=True)
    log_path = log_dir / "notebook-viewer.log"

    # Rotate log if too large
    if log_path.exists() and log_path.stat().st_size > MAX_LOG_SIZE:
        old_log = log_dir / "notebook-viewer.log.old"
        if old_log.exists():
            old_log.unlink()
        log_path.rename(old_log)

    with open(log_path, "ab") as log:
        proc = subprocess.Popen(
            [str(bin_path)],
            cwd=src_tauri,
            stdout=log,
            stderr=log,
            start_new_session=True,
        )

    PID_FILE.write_text(str(proc.pid))

    started = time.time()
    while time.time() - started < timeout_s:
        if is_running():
            return
        time.sleep(0.1)

    raise RuntimeError(
        f"viewer did not start within {timeout_s:.1f}s; see log at {log_path}"
    )


def cmd_start(_args):
    ensure_daemon()
    print(json.dumps(http_json("GET", "/status"), indent=2))


def cmd_stop(_args):
    try:
        http_json("POST", "/shutdown", payload={}, timeout_s=2.0)
    except (urllib.error.URLError, TimeoutError, ConnectionRefusedError):
        # Server not running - this is fine
        pass
    except RuntimeError as e:
        print(f"Note: shutdown request failed: {e}", file=sys.stderr)

    pid = None
    if PID_FILE.exists():
        try:
            pid = int(PID_FILE.read_text().strip())
        except ValueError as e:
            print(f"Note: invalid PID file: {e}", file=sys.stderr)
            pid = None
        PID_FILE.unlink(missing_ok=True)

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
    ensure_daemon()
    print(json.dumps(http_json("GET", "/status"), indent=2))


def cmd_open(args):
    ensure_daemon()
    path = Path(args.path).expanduser().resolve()
    res = http_json("POST", "/open", {"path": str(path)}, timeout_s=60.0)
    print(json.dumps(res, indent=2))

    if args.wait:
        idle_res = http_json(
            "POST",
            "/wait-idle",
            {"timeout_ms": args.wait_timeout_ms},
            timeout_s=max(5.0, args.wait_timeout_ms / 1000.0 + 1.0),
        )
        print(json.dumps(idle_res, indent=2))


def cmd_show(_args):
    ensure_daemon()
    print(json.dumps(http_json("POST", "/window/show", {}), indent=2))


def cmd_hide(_args):
    ensure_daemon()
    print(json.dumps(http_json("POST", "/window/hide", {}), indent=2))


def cmd_reload(_args):
    ensure_daemon()
    print(json.dumps(http_json("POST", "/reload", {}), indent=2))


def cmd_wait_idle(args):
    ensure_daemon()
    res = http_json(
        "POST",
        "/wait-idle",
        {"timeout_ms": args.timeout_ms},
        timeout_s=max(5.0, args.timeout_ms / 1000.0 + 1.0),
    )
    print(json.dumps(res, indent=2))


def cmd_eval(args):
    ensure_daemon()
    res = http_json(
        "POST",
        "/eval",
        {"code": args.code, "timeout_ms": args.timeout_ms},
        timeout_s=max(5.0, args.timeout_ms / 1000.0 + 1.0),
    )
    print(json.dumps(res, indent=2))


def cmd_cells(_args):
    ensure_daemon()
    print(json.dumps(http_json("GET", "/cells"), indent=2))


def cmd_cell(args):
    ensure_daemon()
    name = quote(args.name, safe="")
    print(json.dumps(http_json("GET", f"/cell/{name}"), indent=2))


def cmd_screenshot(args):
    ensure_daemon()
    if args.selector:
        res = http_json(
            "POST",
            "/screenshot/element",
            {"selector": args.selector, "padding": args.padding},
            timeout_s=20.0,
        )
    else:
        res = http_json("POST", "/screenshot", {}, timeout_s=20.0)
    print(json.dumps(res, indent=2))


def cmd_logs(args):
    ensure_daemon()
    path = f"/logs?clear={str(args.clear).lower()}"
    print(json.dumps(http_json("GET", path), indent=2))


def cmd_set_input(args):
    ensure_daemon()
    # Parse value as JSON if possible, otherwise use as string
    try:
        value = json.loads(args.value)
    except json.JSONDecodeError:
        value = args.value
    res = http_json("POST", "/input", {"selector": args.selector, "value": value})
    print(json.dumps(res, indent=2))


def cmd_click(args):
    ensure_daemon()
    res = http_json("POST", "/click", {"selector": args.selector})
    print(json.dumps(res, indent=2))


def cmd_notebooks(_args):
    ensure_daemon()
    print(json.dumps(http_json("GET", "/notebooks"), indent=2))


def cmd_page_loads(_args):
    ensure_daemon()
    print(json.dumps(http_json("GET", "/page-loads"), indent=2))


def main(argv: list[str]) -> int:
    p = argparse.ArgumentParser(prog="viewer.py")
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

    args = p.parse_args(argv)
    args.fn(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))

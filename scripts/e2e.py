#!/usr/bin/env python3
import json
import shutil
import subprocess
import sys
import time
from pathlib import Path


def run(cmd, *, cwd: Path) -> subprocess.CompletedProcess:
    return subprocess.run(cmd, cwd=cwd, text=True, capture_output=True)


def run_json(cmd, *, cwd: Path):
    proc = run(cmd, cwd=cwd)
    if proc.returncode != 0:
        raise RuntimeError(
            f"command failed: {' '.join(map(str, cmd))}\n"
            f"stdout:\n{proc.stdout}\n"
            f"stderr:\n{proc.stderr}"
        )
    out = proc.stdout.strip()
    return json.loads(out) if out else None


def ensure_notebook_deps(repo: Path) -> None:
    notebooks = repo / "notebooks"
    if (notebooks / "node_modules" / ".bin" / "observable").exists():
        return

    if shutil.which("bun"):
        proc = subprocess.run(["bun", "install"], cwd=notebooks)
        if proc.returncode == 0:
            return

    raise RuntimeError(
        "notebook dependencies missing; run `cd notebooks && bun install`"
    )


def pgrep(pattern: str) -> list[str]:
    proc = subprocess.run(["pgrep", "-fl", pattern], text=True, capture_output=True)
    if proc.returncode == 1:
        return []
    if proc.returncode != 0:
        raise RuntimeError(f"pgrep failed: {proc.stderr.strip()}")
    return [line.strip() for line in proc.stdout.splitlines() if line.strip()]


def main(argv: list[str]) -> int:
    repo = Path(__file__).resolve().parents[1]
    viewer = repo / "viewer.py"

    ensure_notebook_deps(repo)

    try:
        run_json([str(viewer), "start"], cwd=repo)
        run_json([str(viewer), "open", "notebooks/src/index.md"], cwd=repo)
        run_json([str(viewer), "wait-idle", "--timeout-ms", "15000"], cwd=repo)

        exposed = run_json(
            [str(viewer), "eval", "return Object.keys(window.__exposed || {})"],
            cwd=repo,
        )
        if exposed.get("result") != ["n", "noise", "pointCount", "meanY"]:
            raise RuntimeError(f"unexpected window.__exposed keys: {exposed}")

        cells = run_json([str(viewer), "cells"], cwd=repo)
        if set(cells.get("cells", [])) != {"n", "noise", "pointCount", "meanY"}:
            raise RuntimeError(f"unexpected /cells output: {cells}")

        mean = run_json([str(viewer), "cell", "meanY"], cwd=repo)
        if not isinstance(mean.get("value"), (int, float)):
            raise RuntimeError(f"unexpected meanY value: {mean}")

        shot = run_json([str(viewer), "screenshot", "--selector", "#chart-sine"], cwd=repo)
        path = Path(shot.get("path", ""))
        if not path.exists():
            raise RuntimeError(f"screenshot path missing: {shot}")
    finally:
        subprocess.run([str(viewer), "stop"], cwd=repo)

    leftovers = []
    for _ in range(30):
        leftovers = pgrep("observable preview")
        if not leftovers:
            break
        time.sleep(0.1)

    if leftovers:
        raise RuntimeError("leftover preview processes:\n" + "\n".join(leftovers))

    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))

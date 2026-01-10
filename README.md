# Notebook Viewer (Observable Framework + Tauri)

This repo is a clean-room notebook viewer for **Observable Framework** notebooks, controlled via a small HTTP API.

## Quick Start

1. Install notebook dependencies:

```bash
cd notebooks
bun install
```

2. Start the viewer daemon:

```bash
./viewer.py start
```

If you have multiple workspaces running viewers at once, the default instance will use `:9847` when available, otherwise it will pick a free port and persist it in `.context/notebook-viewer.json`.

3. Open the sample notebook:

```bash
./viewer.py open notebooks/src/index.md
```

4. Try the API features (the window stays hidden by default):

```bash
./viewer.py wait-idle
./viewer.py screenshot
./viewer.py screenshot --selector "#calibration"
./viewer.py cells
./viewer.py cell meanY
./viewer.py eval "return window.__exposed.meanY"
```

5. When you want to see the notebook, show the viewer window:

```bash
./viewer.py show
```

## Multiple Notebooks (Multiple Viewer Instances)

One viewer instance can display one notebook at a time. To run multiple notebooks simultaneously, run multiple viewer instances (each is a separate process with its own API port).

```bash
# default instance
./viewer.py start
./viewer.py open notebooks/src/index.md

# second instance (new process + port)
./viewer.py --instance b start
./viewer.py --instance b open notebooks/src/index.md
```

Each instance stores its port/PID in `.context/notebook-viewer.<instance>.json` (default instance uses `.context/notebook-viewer.json`).

## Value Access Convention

Observable Framework pages compile to ES modules; notebook variables are not attached to `window`.

For `/cells` and `/cell/:name`, notebooks should export JSON-serializable values on `window.__exposed`:

```js
window.__exposed = { someValue, anotherValue };
```

## Architecture

- `src-tauri/`: Tauri app + axum HTTP server (`http://127.0.0.1:<api-port>`)
- `notebooks/`: Observable Framework project (served via `observable preview`)
- `viewer.py`: CLI wrapper that spawns the Tauri app and calls the HTTP API

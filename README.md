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

## Value Access Convention

Observable Framework pages compile to ES modules; notebook variables are not attached to `window`.

For `/cells` and `/cell/:name`, notebooks should export JSON-serializable values on `window.__exposed`:

```js
window.__exposed = { someValue, anotherValue };
```

## Architecture

- `src-tauri/`: Tauri app + axum HTTP server (`http://127.0.0.1:9847`)
- `notebooks/`: Observable Framework project (served via `observable preview`)
- `viewer.py`: CLI wrapper that spawns the Tauri app and calls the HTTP API

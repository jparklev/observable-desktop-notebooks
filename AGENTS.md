# Notebook Viewer (Observable Framework + Tauri)

This repo uses **Observable Framework** notebooks (`notebooks/src/*.md`) rendered in a hidden **Tauri** WebView, controlled via a local HTTP API.

## Prerequisites

- **Rust** (for building the Tauri app)
- **Node.js 18+** via one of:
  - `fnm` (Fast Node Manager) - preferred
  - `nvm` or direct install
  - Ensure `npx` is available on PATH
- **bun** (for notebook dependencies)
- **Python 3.10+** (for `viewer.py` CLI)

The framework manager tries node resolution in this order:
1. `fnm exec --using=default npx`
2. Local `./node_modules/.bin/` binaries
3. System `npx`

## Fast Startup

The viewer uses `cargo build` on startup, which is near-instant when no Rust code has changed (just validates the cached binary). Only code changes trigger a full rebuild.

## Jeeves Mode (Silent by Default)

Do not show the viewer window until the user explicitly wants to review it.

### Workflow

```bash
# 1. Install notebook deps
cd notebooks
bun install

# 2. Start viewer daemon (hidden window)
./viewer.py start

# 3. Open a notebook
./viewer.py open notebooks/src/index.md

# 4. Verify silently
./viewer.py wait-idle
./viewer.py screenshot --selector "#chart-sine"

# 5. Present to user
./viewer.py show
```

## Value Access Convention

Observable Framework pages compile to ES modules; variables are not attached to `window`.

For `/cells` and `/cell/:name`, notebooks should expose JSON-serializable values using the `expose()` or `track()` helpers:

```js
import { expose, track } from "./bridge.js";

// Simple exposure (always updates)
expose({ meanY, pointCount });

// Smart tracking (only updates when values change)
track({ meanY, pointCount });
```

Use `track()` in reactive cells that re-run frequently to avoid unnecessary updates.

## CLI Reference

```bash
# Lifecycle
./viewer.py start
./viewer.py stop
./viewer.py status

# Notebooks
./viewer.py open notebooks/src/index.md
./viewer.py open notebooks/src/index.md --wait  # Wait for idle after open
./viewer.py notebooks                           # List notebook history
./viewer.py reload

# Synchronization
./viewer.py wait-idle
./viewer.py page-loads                          # Tracks navigation events (not HMR)

# Screenshots
./viewer.py screenshot
./viewer.py screenshot --selector "#calibration"

# Data access
./viewer.py cells
./viewer.py cell meanY
./viewer.py eval "return window.__exposed.meanY"
./viewer.py logs
./viewer.py logs --clear

# Input manipulation
./viewer.py set-input "input[name=amount]" 100
./viewer.py click "button.submit"

# Window control
./viewer.py hide
./viewer.py show
```


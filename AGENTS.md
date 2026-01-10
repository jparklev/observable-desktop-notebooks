# Notebook Viewer (Observable Framework + Tauri)

This repo uses **Observable Framework** notebooks (`notebooks/src/*.md`) rendered in a hidden **Tauri** WebView, controlled via a local HTTP API.

Note: the Framework preview is configured via `notebooks/observablehq.config.js` (including a small `head` script for reliable rendering in hidden/offscreen WKWebViews).

## Observable Framework Notebook Syntax

**IMPORTANT**: Observable Framework markdown is NOT the same as Observable notebooks. Key differences:

### Frontmatter

Every notebook needs YAML frontmatter. Use `parchment` as the default theme:

```yaml
---
title: My Notebook
theme: parchment
---
```

### Code Blocks

**Simple expressions** (automatic display):
```js
Plot.plot({ marks: [Plot.dot(data, {x: "x", y: "y"})] })
```

**With local variables** (MUST use `display()`):
```js
{
  const processed = data.map(d => d.value * 2);
  display(Plot.plot({ marks: [Plot.line(processed)] }));
}
```

**CRITICAL**: JavaScript block statements `{}` do NOT return values. You MUST call `display()` to render output. Without it, the block produces nothing.

**WRONG** (produces empty output):
```js
{
  const x = 5;
  Plot.plot({...})  // This is lost!
}
```

**CORRECT**:
```js
{
  const x = 5;
  display(Plot.plot({...}));
}
```

### Inputs with `view()`

```js echo
const value = view(Inputs.range([0, 100], {value: 50, label: "Amount"}))
```

- `echo` directive shows the code AND renders the input
- Without `echo`, code executes silently

### No `return` Statements

Code blocks are expressions, not functions. Never use `return` at the block level:

**WRONG**:
```js
{
  const data = [1, 2, 3];
  return Plot.plot({...});  // SyntaxError!
}
```

**CORRECT**:
```js
{
  const data = [1, 2, 3];
  display(Plot.plot({...}));
}
```

Note: `return` IS valid inside nested functions (e.g., `.map(x => { return x * 2; })`).

### Inline Expressions

Use `${...}` for dynamic text:
```markdown
Current value: ${value.toFixed(2)}
```

### LaTeX Math

**IMPORTANT**: Observable Framework does NOT support `$...$` markdown syntax for math. Use `tex` fenced code blocks instead:

**WRONG** (renders as plain text):
```markdown
The formula $R_G \approx R_A - \frac{\sigma^2}{2}$ shows...
```

**CORRECT** (block equation):
````markdown
```tex
R_G \approx R_A - \frac{\sigma^2}{2}
```
````

For inline math variables, use italics as a simple alternative:
```markdown
where *p* is probability and *q* = 1 - *p*
```

Or use the `tex` tagged template literal in JavaScript blocks:
```js
tex`R_G \approx R_A - \frac{\sigma^2}{2}`
```

## Verification

Use the `verify` command to auto-discover and screenshot all visualizations:

```bash
# 1. Open notebook
./viewer.py open notebooks/src/my-notebook.md --wait

# 2. Run verification (discovers charts, takes screenshots, checks errors)
./viewer.py verify
./viewer.py verify --include-controls
```

This returns:
- `page_errors`: Any console errors
- `visualizations`: Array of discovered charts with screenshot paths and context
- `controls`: (Optional) Array of discovered UI controls (Inputs/sliders/buttons) with screenshot paths and context
- `inputs`: Count of interactive inputs
- `exposed_cells`: List of values exposed via `bridge.js`

Each visualization includes:
- `screenshot_path`: Temp file path for sub-agent analysis
- `screenshot_error`: Present when capture fails (so failures are visible without re-running)
- `context_text`: Preceding markdown explaining what the chart should show
- `size`: Width/height in pixels
- `selector`: CSS selector for the element

Screenshots are written under the system temp dir (e.g. `$TMPDIR/notebook-viewer/screenshot-*.png` on macOS).

### Manual Verification

For detailed inspection:

```bash
./viewer.py logs                    # Check for errors
./viewer.py cells                   # List exposed values
./viewer.py screenshot --selector "#chart-id"  # Screenshot specific element
```

## Prerequisites

- **Rust** (for building the Tauri app)
- **Node.js 18+** via one of:
  - `fnm` (Fast Node Manager) - preferred
  - `nvm` or direct install
  - Ensure `npx` is available on PATH
- **bun** (for notebook dependencies)
- **Python 3.10+** (for `viewer.py` CLI)

The framework manager tries node resolution in this order:
1. `fnm exec --using 22 -- ./node_modules/.bin/observable preview`
2. Local `./node_modules/.bin/observable preview`
3. System `npx --yes observable preview`

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
./viewer.py open notebooks/src/index.md --wait --wait-timeout-ms 30000
./viewer.py notebooks                           # List notebook history
./viewer.py reload

# Synchronization
./viewer.py wait-idle
./viewer.py page-loads                          # Tracks navigation events (not HMR)

# Verification (auto-discovers charts, screenshots, checks errors)
./viewer.py verify
./viewer.py verify --timeout-ms 15000           # Longer timeout for heavy notebooks
./viewer.py verify --include-controls           # Also capture UI controls

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

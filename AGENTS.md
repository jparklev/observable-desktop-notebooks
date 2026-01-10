# Notebook Viewer (Observable Framework + Tauri)

This repo uses **Observable Framework** notebooks (`notebooks/src/*.md`) rendered in a hidden **Tauri** WebView, controlled via a local HTTP API (`http://127.0.0.1:<api-port>`).

## Quick Access

**From Desktop** (double-click to open):
```bash
./sync-desktop.py    # Generate/update launchers in ~/Desktop/Notebooks/
```

This creates `.app` launchers for each notebook. Double-click any app to open that notebook in the viewer.

**From CLI**:
```bash
./viewer.py browse   # Opens catalog and shows window
```

## Notebook Organization

**Standalones** - Single `.md` files in `notebooks/src/`:
```
notebooks/src/kelly-criterion.md
notebooks/src/monte-carlo.md
```

**Series** - Folders with multiple parts (auto-paging within folder):
```
notebooks/src/volatility/
  index.md       # Series landing page
  part-1.md
  part-2.md
```

The **catalog** (`notebooks/src/index.md`) is the landing page - add new notebooks there with a brief description.

---

Note: the Framework preview is configured via `notebooks/observablehq.config.js` (including a small `head` script for reliable rendering in hidden/offscreen WKWebViews).

The API port is per viewer instance. Use `./viewer.py status` (or `./viewer.py --instance <name> status`) to discover it; don't hardcode `:9847`.

> **⚠️ Multi-Worktree Warning**: If working in a git worktree while another agent uses a viewer in a different worktree, **always use `--instance <name>`** to avoid conflicts. Example: `./viewer.py --instance myworktree start`. Without isolation, viewers can interfere with each other.

## Documentation References

**Search these folders for patterns and examples when building notebooks:**

- `observable-framework-docs/` - Observable Framework documentation
  - `javascript.md` - JavaScript execution, `display()`, implicit/explicit display
  - `reactivity.md` - Reactive variables, generators, inputs, invalidation
  - `markdown.md` - Grids, cards, HTML, frontmatter
  - `inputs/` - Input component reference (range, select, radio, etc.)
  - `lib/` - Library documentation (plot, d3, tex, duckdb, etc.)

- `observable-plot-docs/` - Observable Plot documentation
  - `marks/` - 30 mark types (dot, line, bar, area, cell, text, geo, etc.)
  - `transforms/` - Data transforms (bin, group, stack, normalize, etc.)
  - `features/` - Scales, facets, legends, projections, interactions
  - `examples/` - **233 example notebooks** - use these as templates!

## Notebook Creation Workflow

Claude orchestrates notebook creation, using Gemini for research and visual review.

### Phase 1: Research & Spec

**1. Topic research (Gemini Flash)**

For notebooks that require domain knowledge, use Gemini Flash for web research:

```bash
gemini -m gemini-3-flash-preview \
  "Research [TOPIC] for a data visualization notebook. Find:
   - Key concepts to explain
   - Common datasets or data sources
   - Interesting angles or insights to highlight
   - Any formulas or calculations needed"
```

Gemini Flash can search the web to gather background information, find public datasets, and understand the domain.

**2. Data sourcing**

Identify where data will come from:
- **Public APIs** - Gemini can search for relevant APIs
- **Static datasets** - Download CSVs, JSON files
- **Generated data** - Synthetic data for teaching concepts
- **Data loaders** - Scripts that fetch/process data at build time

For real data, create a data loader or download to `notebooks/src/`.

**3. Example patterns (Gemini Flash)**

Scan the 233 examples for relevant visualization patterns:

```bash
ls observable-plot-docs/examples/ | gemini -m gemini-3-flash-preview \
  "User wants a notebook about [TOPIC]. Which examples are most relevant?
   Return 5-10 with brief reasons. You may read any example files for more context."
```

Gemini can open and read example files if descriptions would help. Many examples include explanatory comments.

**4. Claude decides approach**

Claude reviews Gemini's research and suggestions but has final authority. If no examples are helpful, Claude can use basic patterns (line charts, bar charts, etc.) without copying from examples.

**5. Draft spec**

Claude writes a brief spec:
- Teaching goal (what should reader understand?)
- Data sources (static file, data loader, inline?)
- Narrative arc (hook → build → insight → conclusion)
- Key visualizations (list with brief description)
- Interactive elements (which parameters are adjustable?)

**4. Spec review (Gemini Pro)**

```bash
cat spec.md | gemini -m gemini-3-pro-preview \
  "Review this notebook spec. Identify:
   - Missing pieces or gaps in the narrative
   - Better visualization approaches
   - Opportunities for interactivity
   - Potential teaching clarity issues"
```

Claude incorporates feedback and finalizes the spec.

### Phase 2: Build

Two approaches - choose based on notebook complexity:

**Option A: Sequential (simpler notebooks)**

Write one section → verify → get feedback → repeat.

```bash
# After each section
./viewer.py open notebooks/src/notebook.md --wait
./viewer.py verify
# Review screenshots, fix issues, continue
```

**Option B: Parallel (complex notebooks)**

Write all sections at once, then batch verify:

```bash
# Write complete notebook first
./viewer.py open notebooks/src/notebook.md --wait
./viewer.py verify  # Returns all screenshots
```

Then send all screenshots to Gemini for batch visual review.

### Phase 3: Visual Review (Gemini Pro)

After `verify`, screenshots are saved to temp files. Send to Gemini for multimodal analysis:

```bash
# Copy screenshot to workspace (required for Gemini)
cp /tmp/screenshot-viz-001.png ./screenshot.png

gemini -m gemini-3-pro-preview \
  "Review this data visualization from an Observable notebook.
   Context: [describe what this chart should show]

   Evaluate:
   - Is the visualization clear and readable?
   - Are axis labels, legends, and titles effective?
   - Is the color scheme appropriate?
   - Any visual issues (clipping, overlap, sizing)?
   - Does it effectively teach the concept?"

rm ./screenshot.png  # Clean up
```

For batch review, send multiple screenshots with context for each.

### Phase 4: Iterate

Based on Gemini's visual feedback:
1. Fix identified issues
2. Re-verify affected sections
3. Get Gemini's opinion on improvements
4. Repeat until polished

Claude and Gemini can collaborate on:
- Visualization refinements
- Color and styling choices
- Interactive element design
- Narrative flow

### Phase 5: Present & Catalog

Once functional and beautiful:

```bash
./viewer.py show  # Display to user
```

Collect user feedback and iterate if needed.

**Add to catalog** - Update `notebooks/src/index.md` with a link and description.

**Sync desktop launchers** - Run `./sync-desktop.py` to update `~/Desktop/Notebooks/`.

### Workflow Summary

```
┌─────────────────────────────────────────────────────────────┐
│  RESEARCH         Gemini Flash: topic research (web search) │
│                   Gemini Flash: data source discovery       │
│                   Gemini Flash: scan examples               │
│                   Claude decides approach                   │
├─────────────────────────────────────────────────────────────┤
│  SPEC             Claude drafts spec                        │
│                   Gemini Pro reviews                        │
│                   Claude finalizes                          │
├─────────────────────────────────────────────────────────────┤
│  BUILD            Claude writes notebook                    │
│                   ./viewer.py verify → screenshots          │
├─────────────────────────────────────────────────────────────┤
│  REVIEW           Gemini Pro reviews screenshots            │
│                   (multimodal visual analysis)              │
├─────────────────────────────────────────────────────────────┤
│  ITERATE          Claude fixes issues                       │
│                   Gemini provides feedback                  │
│                   Repeat until polished                     │
├─────────────────────────────────────────────────────────────┤
│  PRESENT          ./viewer.py show                          │
│                   User review                               │
│                   Add to index.md, run ./sync-desktop.py    │
└─────────────────────────────────────────────────────────────┘
```

### Gemini Usage Tips

**Gemini Flash** (fast research, scanning):
- Use **focused prompts** with constrained output format
- Can get stuck in research loops if prompts are too open-ended
- Best for: topic research, example scanning, quick questions
- Example: "List 5-10 relevant examples with brief reasons" (not "explore everything")

**Gemini Pro** (deep review, prose, visual analysis):
- Can handle more open-ended prompts
- Best for: spec review, visual/multimodal analysis, nuanced feedback
- **Educational prose**: Use Gemini Pro to write multi-paragraph explanations, historical context, references with superscripts, and conceptual deep-dives. It excels at making technical topics accessible.
- Give context about what you're building and what to look for

**Screenshot handoff pattern** (for visual review):
```bash
# 1. Copy screenshot to workspace (Gemini can't read /tmp directly)
cp /tmp/screenshot-viz-001.png ./screenshot.png

# 2. Send to Gemini with context
gemini -m gemini-3-pro-preview \
  "Review this [chart type] showing [what it should show].
   Check for: readability, labeling, visual issues, teaching clarity."

# 3. Clean up
rm ./screenshot.png
```

For batch review, copy multiple screenshots and describe each.

## Philosophy: Exploratory & Educational Notebooks

Observable Plot and Framework are designed for **exploratory data visualization** - finding insights quickly. Our notebooks should teach and reveal, not just display.

### Core Principles

1. **Optimize for "time to first chart"** - Start with the simplest valid expression using Plot's defaults. Let the user see the data's shape before adding complexity.

2. **Iterate, don't dump** - Present solutions in stages:
   - Raw view: The data as-is
   - Refined view: Add encodings (color, size) or facets to reveal patterns
   - Polished view: Add labels, sorted domains, tooltips

3. **Leverage reactivity** - Write code that utilizes topological execution:
   - Define variables at the top level so they can be inspected anywhere
   - Bind UI inputs directly to variables that feed into charts
   - The chart should "breathe" - when inputs change, charts update automatically

4. **Transform data declaratively** - Use Plot's built-in transforms (`Plot.group`, `Plot.bin`, `Plot.window`) inside mark definitions rather than opaque pre-processing

5. **Code is for reading** - Use clear column names as accessor strings (`y: "close"`) rather than arrow functions unless necessary

### Progressive Refinement

Start simple, then progressively add detail:

```js
// Step 1: One-liner with defaults
Plot.dot(data, {x: "x", y: "y"}).plot()

// Step 2: Add encoding
Plot.dot(data, {x: "x", y: "y", stroke: "category"}).plot()

// Step 3: Add refinements
Plot.plot({
  grid: true,
  color: {legend: true},
  marks: [Plot.dot(data, {x: "x", y: "y", stroke: "category"})]
})
```

### Reactivity for Teaching

Notebooks should be **live and interconnected** - like a spreadsheet. When a reader changes an input, they immediately see how it affects the output. This builds intuition.

```js
const threshold = view(Inputs.range([0, 100], {label: "Threshold"}))
```

```js
// This chart updates whenever threshold changes
Plot.dot(data.filter(d => d.value > threshold), {x: "x", y: "y"})
```

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

### Code Block Types

**Expression blocks** (no semicolon) - implicitly display the result:
```js
Plot.plot({ marks: [Plot.dot(data, {x: "x", y: "y"})] })
```

**Program blocks** (with semicolons) - must call `display()` explicitly:
```js
const processed = data.map(d => d.value * 2);
display(Plot.plot({ marks: [Plot.line(processed)] }));
```

**CRITICAL**: Block statements `{}` do NOT return values. You MUST call `display()`:

```js
// WRONG (produces empty output)
{
  const x = 5;
  Plot.plot({...})  // This is lost!
}

// CORRECT
{
  const x = 5;
  display(Plot.plot({...}));
}
```

### Variable Scope

**Top-level variables are shared across the page:**
```js
// Block 1
const x = 10;

// Block 2 (can reference x)
display(x * 2)  // Works - sees x from Block 1
```

**Block-scoped variables are local:**
```js
// Block 1 - z is hidden
{
  const z = 3;
}

// Block 2 - cannot see z
display(z)  // ERROR: z is not defined
```

**Avoid unnecessary curly braces** - they hide variables from other cells.

### No `return` Statements

Code blocks are expressions, not functions. Never use `return` at the block level:

```js
// WRONG - SyntaxError!
{
  const data = [1, 2, 3];
  return Plot.plot({...});
}

// CORRECT
{
  const data = [1, 2, 3];
  display(Plot.plot({...}));
}
```

Note: `return` IS valid inside nested functions (e.g., `.map(x => { return x * 2; })`).

### Inputs with `view()`

```js echo
const value = view(Inputs.range([0, 100], {value: 50, label: "Amount"}))
```

- `echo` directive shows the code AND renders the input
- Without `echo`, code executes silently
- The variable is reactive - blocks referencing it re-run when it changes

### Inline Expressions

Use `${...}` for dynamic text:
```markdown
Current value: ${value.toFixed(2)}
```

### LaTeX Math

**IMPORTANT**: Observable Framework does NOT support `$...$` markdown syntax. Use `tex` fenced code blocks:

```tex
R_G \approx R_A - \frac{\sigma^2}{2}
```

Or the `tex` tagged template literal in JavaScript:
```js
tex`R_G \approx R_A - \frac{\sigma^2}{2}`
```

For inline math, use italics as a simple alternative: *p* = probability.

## Observable Plot Patterns

### Available by Default

**Libraries** (no import needed):
- `Plot` - Observable Plot
- `d3` - D3.js (scales, shapes, arrays, time, formatting)
- `Inputs` - Observable Inputs (range, select, checkbox, etc.)
- `html` - Hypertext Literal for DOM creation
- `tex` - LaTeX rendering
- `Generators` - Async generator utilities

**Reactive Variables** (built-in, always updating):
- `now` - Current timestamp (for animation)
- `width` - Page width (for responsive charts)
- `dark` - Boolean for dark mode detection

**Additional Libraries** (see `observable-framework-docs/lib/`):
- DuckDB, SQLite - SQL databases
- Arquero, Arrow - Columnar data
- Leaflet, Mapbox, Deck.gl - Maps
- Mermaid, DOT - Diagrams
- Vega-Lite, ECharts - Alternative chart libraries

### Mark Composition (Layering)

Build complex charts by layering marks. Order matters (later marks draw on top):

```js
Plot.plot({
  marks: [
    Plot.ruleY([0]),                           // Base reference line
    Plot.areaY(data, {x: "date", y: "value"}), // Fill area
    Plot.lineY(data, {x: "date", y: "value"})  // Line on top
  ]
})
```

**Common patterns:**
- Financial charts: `ruleX` (range) + `ruleX` (body, thicker stroke)
- Heatmaps: `cell` (fill) + `text` (labels with contrast color)
- Annotated charts: data marks + `text` annotations

### Key Marks Reference

| Mark | Use Case |
|------|----------|
| `dot` | Scatter plots, point clouds |
| `line`/`lineY` | Time series, trends |
| `area`/`areaY` | Filled time series, stacked areas |
| `bar`/`barX`/`barY` | Bar charts, histograms |
| `cell` | Heatmaps, calendars, matrices |
| `rect`/`rectY` | Histograms, binned distributions |
| `rule`/`ruleX`/`ruleY` | Reference lines, ranges |
| `text` | Labels, annotations |
| `tip` | Tooltips on hover |
| `bollinger`/`bollingerY` | Financial bands |

### Transforms

Use transforms to reshape data within the plot:

```js
// Bin continuous data
Plot.rectY(data, Plot.binX({y: "count"}, {x: "value"}))

// Group categorical data
Plot.barY(data, Plot.groupX({y: "count"}, {x: "category"}))

// Normalize to percentages
Plot.tickX(data, Plot.normalizeX("sum", {x: "value", y: "category", z: "state"}))

// Stack bars
Plot.barX(data, Plot.stackX({x: "value", fill: "category"}))
```

### Scale Configuration

```js
Plot.plot({
  color: {
    scheme: "rdylbu",      // Diverging color scheme
    pivot: 0,              // Center point for diverging
    legend: true           // Show legend
  },
  x: {
    grid: true,
    label: "Value →",
    tickFormat: "%"        // Format as percentage
  },
  y: {
    domain: [0, 100],      // Fixed domain
    reverse: true          // Flip axis direction
  }
})
```

### Responsive Charts

Use the reactive `width` variable or `resize()` helper:

```js
// Using width variable
Plot.barX(data).plot({width})

// Using resize for containers
resize((width, height) => Plot.barX(data).plot({width, height}))
```

### Faceting (Small Multiples)

Facets partition data and repeat a plot for each partition - powerful for teaching and comparison:

```js
// Vertical facets by species
Plot.dot(penguins, {
  x: "culmen_length_mm",
  y: "culmen_depth_mm",
  fy: "species"  // Facet by species
}).plot()

// Two-dimensional faceting
Plot.plot({
  marks: [
    Plot.frame(),
    Plot.dot(penguins, {
      x: "culmen_length_mm",
      y: "culmen_depth_mm",
      fx: "sex",       // Horizontal facets
      fy: "species"    // Vertical facets
    })
  ]
})
```

**Teaching pattern**: Show context by mixing faceted and non-faceted marks:
```js
Plot.plot({
  marks: [
    // Background: all data in gray (non-faceted)
    Plot.dot(penguins, {x: "x", y: "y", fill: "#aaa", r: 1}),
    // Foreground: faceted subset
    Plot.dot(penguins, {x: "x", y: "y", fy: "species"})
  ]
})
```

### Tooltips and Crosshairs

Add interactivity for exploration:

```js
// Simple tooltip on hover
Plot.dot(data, {x: "x", y: "y", tip: true})

// Tooltip with extra channels
Plot.dot(data, {
  x: "weight",
  y: "height",
  channels: {name: "name", sport: "sport"},
  tip: true
})

// Crosshair for precise reading
Plot.plot({
  marks: [
    Plot.dot(data, {x: "x", y: "y"}),
    Plot.crosshair(data, {x: "x", y: "y"})
  ]
})
```

## Advanced Reactivity

### Mutables for Shared State

When multiple cells need to read AND write the same value, use `Mutable`:

```js
import {Mutable} from "observablehq:stdlib";

const count = Mutable(0)
```

```js
// Read the value
display(count.value)
```

```js
// Write from another cell (e.g., button click)
html`<button onclick=${() => count.value++}>Increment</button>`
```

This is useful for:
- Counters and state machines
- Coordinating multiple visualizations
- Complex multi-cell interactions

### FileAttachment

Load static files alongside your notebooks:

```js
const data = FileAttachment("data.csv").csv({typed: true})
```

Supported formats:
- `.csv`, `.tsv` - Tabular data
- `.json` - JSON objects/arrays
- `.parquet`, `.arrow` - Columnar formats
- `.xlsx` - Excel workbooks
- `.zip` - Archives (extract individual files)
- Images, video, audio

**Note**: Path must be a static string literal (no template strings).

### Data Loaders

For dynamic data at build time, use data loaders (`*.csv.js`, `*.json.py`, etc.):

```js
// quakes.json.sh - shell script data loader
curl -f https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson
```

Then reference the output:
```js
const quakes = FileAttachment("quakes.json").json()
```

Data loaders can be Python, JavaScript, R, or any executable.

### Environment Variables & Secrets

Secrets (API keys, database credentials) should **never** reach the browser. Use data loaders + dotenv:

**Setup:**
```bash
cd notebooks && bun add dotenv
```

**Create `.env`** (already in `.gitignore`):
```
API_KEY=sk-xxxxx
DATABASE_URL=postgres://...
```

**Data loader** (`src/api-data.json.js`):
```javascript
import "dotenv/config";

const res = await fetch("https://api.example.com/data", {
  headers: { Authorization: `Bearer ${process.env.API_KEY}` }
});

process.stdout.write(JSON.stringify(await res.json()));
```

**Notebook** (`src/my-notebook.md`):
```js
const data = await FileAttachment("api-data.json").json()
```

The secret stays on the server; only the fetched data reaches the browser.

**See:** `notebooks/src/env-test.md` for a working example.

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

### Troubleshooting

**`verify` returns empty visualizations after edits:**
HMR (Hot Module Replacement) can sometimes fail to properly reload. Solution:
```bash
./viewer.py stop
./viewer.py start
./viewer.py open notebooks/src/notebook.md --wait
./viewer.py verify
```

**Screenshots show "Not found" or wrong notebook:**
Another viewer instance (possibly in a different worktree) may be interfering. Use instance isolation:
```bash
./viewer.py --instance myname stop
./viewer.py --instance myname start
./viewer.py --instance myname open notebooks/src/notebook.md --wait
```

**Viewer hangs or times out:**
- Check `./viewer.py logs` for JavaScript errors
- Notebooks with infinite generators (animation loops) may prevent idle state
- Try `./viewer.py verify --timeout-ms 15000` for longer timeout

## Prerequisites

- **Rust** (for building the Tauri app)
- **Node.js 18+** via one of:
  - `fnm` (Fast Node Manager) - preferred
  - `nvm` or direct install
  - Ensure `npx` is available on PATH
- **bun** (for notebook dependencies)
- **Python 3.10+** (for `viewer.py` CLI)

The framework manager tries to run `observable preview` in this order:
1. `fnm exec --using 22 -- ./node_modules/.bin/observable preview ...` (preferred)
2. `./node_modules/.bin/observable preview ...`
3. `npx --yes observable preview ...`

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

**Limitation**: `track()` uses JSON serialization for change detection. Avoid exposing very large datasets directly - expose summaries instead.

## Multiple Viewer Instances

One viewer instance controls one Tauri WebView (one notebook at a time). Use `--instance <name>` to run another isolated instance (separate process + API port):

```bash
./viewer.py --instance b start
./viewer.py --instance b open notebooks/src/index.md
```

The default instance uses `:9847` when available; otherwise it picks a free port. Use `--api-port <port>` to force a specific port if needed.

Instance state/logs are stored in `.context/notebook-viewer.<instance>.json` and `.context/notebook-viewer.<instance>.log` (default instance uses `.context/notebook-viewer.json` and `.context/notebook-viewer.log`).

## CLI Reference

```bash
# Lifecycle
./viewer.py start
./viewer.py stop
./viewer.py status
./viewer.py browse                              # Open catalog and show window

# Notebooks
./viewer.py open notebooks/src/index.md
./viewer.py open notebooks/src/index.md --wait  # Wait for idle after open
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

## Common Mistakes to Avoid

### 1. The "Return" Trap
```js
// WRONG - LLMs often write this
{
  const data = fetchData();
  return Plot.plot({...})  // Renders nothing!
}

// CORRECT
{
  const data = fetchData();
  display(Plot.plot({...}));
}
```

### 2. Semicolon Suppresses Output
```js
Plot.plot({...});  // With semicolon = Program block = no implicit display
Plot.plot({...})   // No semicolon = Expression block = displays automatically
```

### 3. Over-Using Block Scope
```js
// WRONG - x is hidden
{ const x = 10; }
display(x);  // ERROR: x is not defined

// CORRECT - x is shared
const x = 10;
display(x);  // Works
```

### 4. Forgetting `display()` in Loops
```js
// WRONG - only last value shows
for (const item of data) {
  Plot.dot([item])  // Lost on each iteration
}

// CORRECT
for (const item of data) {
  display(Plot.dot([item]));
}
```

### 5. Assuming Libraries Need Import
```js
// WRONG - Plot is already available
import * as Plot from "@observablehq/plot";

// CORRECT - just use it
Plot.dot(data, {x: "x", y: "y"})
```

### 6. Animation/Generator Loops
If your notebook has infinite generators (for animation), `verify` may timeout:
```js
// This runs forever - be aware when verifying
const i = (function* () {
  for (let i = 0; true; ++i) yield i;
})();
```

### 7. Code Examples Get Executed
Only ` ```js ` blocks are executed. Use ` ```javascript ` for non-executable examples:
````markdown
**This runs in the browser:**
```js
const x = 10;  // Creates variable x
```

**This is just syntax-highlighted text:**
```javascript
const x = 10;  // Display only, not executed
```
````
This matters when showing Node.js code (like data loaders) that uses `process.env` - if you use ` ```js `, it will error because `process` doesn't exist in browsers.

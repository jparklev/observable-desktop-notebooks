# Observable Desktop Integration for Claude Code

This project enables Claude Code to programmatically edit and view Observable Desktop notebooks.

## Jeeves Mode: Work Silently, Present Results

**Philosophy**: Like Wodehouse's Jeeves (impeccably portrayed by Stephen Fry), the agent should handle everything behind the scenes with quiet competence. The user rings for a data analysis; Jeeves materializes with the finished notebook, a brief summary of findings, and perhaps a raised eyebrow at any anomalies in the data. They shouldn't see the sausage being made—no flashing windows, no interrupted focus, just results.

> "I endeavoured to give satisfaction, sir."

### How It Works

1. **Edit HTML directly** - Notebooks are just HTML files. Edit them with standard file operations without opening Observable Desktop at all.

2. **Iterate silently** - Use `capture-cell` to verify charts look correct. **Iterate as many times as needed.** Refine the visualization until it genuinely illuminates the data. Bostock's principle: "Test forms against actual data."

3. **Present when polished** - Open the notebook for the user with context and analysis.

### On Iteration

**Do not hesitate to iterate.** Capture a cell, examine it, adjust the code, capture again. Good visualization often requires multiple passes:
- First pass: Does the data show up at all?
- Second pass: Is the form appropriate? (Bar vs line vs scatter?)
- Third pass: Are scales, colors, labels right?
- Fourth pass: Does it communicate insight?

Use `capture-cell` liberally—it's completely silent.

### On Notebook Prose

Notebooks are not just code—they're literate documents. **Include prose, thoughts, and analysis**:
- Explain what the visualization reveals
- Note ambiguities or uncertainties in the data
- Document decisions ("I chose a log scale because...")
- Surface questions that emerged during analysis
- Add markdown cells with context, caveats, methodology

When the user asks for analysis, the notebook should read like a report with embedded visualizations, not just a collection of charts.

**Every analytical choice needs justification:**
- Why this time period? (market regimes, data availability, sample size requirements)
- Why these metrics? (Sharpe vs Sortino, daily vs weekly returns)
- What are the limitations? (survivorship bias, single period, simplifications)

**Include forward-looking content:**
- "Future Analysis Directions" section with concrete next steps
- Tier by effort: near-term (easy), medium-term (more work), longer-term (research questions)
- This signals the analysis is a starting point, not a final answer

### Notebook Structure Convention

Notebooks should follow this structure:

1. **Title & Introduction** - Markdown cell with title and context
2. **Main Content** - ONLY section headers (markdown) and visualization cells
3. **Appendix** - ALL data and computation cells at the bottom

**Main body should contain ONLY:**
- Markdown cells (titles, section headers, prose, insights)
- Visualization cells (Plot.plot, charts, tables rendered with `md`)

**Appendix should contain ALL:**
- Raw data arrays
- Data transformations (`bars = rawBars.map(...)`)
- Derived computations (`dailyReturns`, `stats`, `normalizedData`)
- Helper functions and configuration (`colors`, `symbols`)

```html
<!-- MAIN BODY: Only markdown and visualizations -->
<script type="text/markdown">
# Title
</script>

<script type="text/markdown">
## Section Header
</script>

<script type="application/vnd.observable.javascript">
// Visualization only - references variables defined in Appendix
Plot.plot({marks: [Plot.line(processedData, {x: "date", y: "value"})]})
</script>

<!-- APPENDIX: All data and computations -->
<script type="text/markdown">
---

## Appendix
</script>

<script type="application/vnd.observable.javascript" hidden>
colors = ({AAPL: "#555", MSFT: "#00a4ef"})
</script>

<script type="application/vnd.observable.javascript" hidden>
processedData = rawData.map(d => ({date: new Date(d.t), value: d.c}))
</script>

<script type="application/vnd.observable.javascript">
rawData = [...]
</script>
```

Observable's reactive evaluation means cell order doesn't affect execution - cells run based on dependencies regardless of position. This lets us put all "plumbing" at the bottom while keeping the narrative clean.

### Cell Display Best Practices

**Hiding intermediate computations:**
- The `hidden` attribute hides cell OUTPUT but code may still appear in some views
- For cleaner notebooks, prefer computing derived values inside visualization cells using block syntax:

```javascript
// Instead of separate cell: `bars = rawBars.map(...)`
// Compute inline in the visualization:
{
  const bars = rawBars.map(d => ({date: new Date(d.t), close: d.c}));
  return Plot.plot({marks: [Plot.line(bars, {x: "date", y: "close"})]});
}
```

**Volume/bar charts with many data points:**
- Daily data over 6+ months creates unreadable x-axis labels
- Use weekly binning: `Plot.rectY(data, Plot.binX({y: "sum"}, {x: "date", y: "volume", interval: "week"}))`
- Set explicit ticks: `x: {type: "time", ticks: "month"}`
- This aggregates daily bars into weekly summaries with readable month labels

### Example Workflow

```bash
# 1. Create notebook
./observable.py new notebooks/report.html --title "Q4 Analysis"

# 2. Add and edit cells (HTML editing - no Observable needed)

# 3. Iterate on visualizations silently
./observable.py capture-cell notebooks/report.html 5  # Check chart
# Hmm, the bars are too thin. Adjust code...
./observable.py capture-cell notebooks/report.html 5  # Better.

# 4. When polished, open for the user
./observable.py open notebooks/report.html
```

**When presenting**: "Your Q4 analysis is ready, sir. Revenue shows a 12% uptick in the Eastern region, though I note some irregularity in the November figures that may warrant investigation. The notebook is open for your review."

### Verifying Output: Use `capture-cell` Only

When you need to verify a cell's output before presenting:

```bash
# Capture a specific cell by index (completely silent!)
# Moves cell to top temporarily, captures, restores order
./observable.py capture-cell notebooks/report.html 6    # Capture cell at index 6
./observable.py capture-cell notebooks/report.html 10   # Capture cell at index 10

# List cells to find the index you want
./observable.py list notebooks/report.html
```

**`capture-cell` is the ONLY method to use** for verification screenshots:
- Completely silent (no window focus changes)
- Works for any cell regardless of position
- Temporarily reorders cells, captures, then restores

**DO NOT use `render` for verification** - it closes/disrupts the notebook and may prevent `open` from working correctly afterward.

### Commands for Jeeves Mode

| Command | Purpose | User Visible? |
|---------|---------|---------------|
| `new`, `add`, `edit`, `delete` | Edit notebook HTML | No |
| `capture-cell <idx>` | **Capture any cell silently** | No |
| `list` | Show cell indices | No |
| `open` | **Open final notebook for user** | Yes (the deliverable!) |

**During development**: Edit HTML directly, use `capture-cell` to verify specific outputs.

**When complete**: **ALWAYS use `open` to present the finished notebook to the user.** This is the deliverable—don't skip it!

## Notebooks Directory

All notebooks live in `notebooks/`. **Before creating a new notebook**, always search existing notebooks to check if the user wants to edit/refactor an existing one:

```bash
# List existing notebooks
ls notebooks/

# Search notebook contents
grep -l "keyword" notebooks/*.html
```

## Version Control

This project uses **jj** (Jujutsu) colocated with git. Use all jj features freely (rebase, squash, split, etc).

## Quick Start for Agents

```bash
cd ~/src/tries/2025-12-20-observable-desktop-hack

# Edit a cell and see result (background mode - won't steal focus)
./observable.py edit-and-view notebooks/reactivity-demo.html 1 "Math.PI * 2"
# Returns: Screenshot: /tmp/xxx.png
# Then read the screenshot to see the result

# List cells
./observable.py list notebooks/reactivity-demo.html --json

# Add a cell
./observable.py add notebooks/reactivity-demo.html "Plot.plot({marks: [Plot.dot([1,2,3])]})"

# Take screenshot without stealing focus
./observable.py screenshot

# Create new notebook (in notebooks/ folder)
./observable.py new notebooks/my-notebook.html --title "My Notebook"
```

## Key Discoveries

### Architecture
- **Observable Desktop is a Tauri app** (Rust + WKWebView), NOT Electron
- Notebooks are stored in the **cloud** (api.observablehq.com), not locally by default
- However, the app can **open local HTML files** directly
- No public REST API exists for notebook management

### Notebook Format
Notebooks use HTML with a `<notebook>` root element containing `<script>` cells:

```html
<!doctype html>
<notebook theme="air">
  <title>My Notebook</title>
  <script type="text/markdown">
# Markdown cell
  </script>
  <script type="application/vnd.observable.javascript" pinned>
// Observable JavaScript cell - supports viewof, mutable, reactivity
myValue = 42
  </script>
  <script type="application/vnd.observable.javascript" pinned>
// Reactive - updates when myValue changes
doubled = myValue * 2
  </script>
  <script type="text/markdown">
The value is **${myValue}**, doubled is **${doubled}**.
  </script>
</notebook>
```

### Cell Types
- `application/vnd.observable.javascript` - **Observable JavaScript (RECOMMENDED)** - supports `viewof`, `mutable`, reactivity
- `module` or `type="module"` - Standard ES modules (no Observable features)
- `text/markdown` - Markdown (supports `${variable}` interpolation)
- `text/html` - HTML
- `text/x-typescript` - TypeScript
- `application/sql` - SQL

**IMPORTANT**: Use `application/vnd.observable.javascript` for reactive notebooks, NOT `module`. Standard JS modules don't support `viewof`, `mutable`, or Observable's reactive variable syntax.

### Cell Attributes
- `pinned` - Show source code
- `hidden` - Hide output
- `id="..."` - Stable identifier for editing

### Available Themes
Light: `air`, `cotton`, `glacier`, `parchment`, `stark`, `sun-faded`
Dark: `coffee`, `deep-space`, `ink`, `midnight`, `near-midnight`, `ocean-floor`, `slate`

## CLI Tools

### observable.py - Main CLI
```bash
# Create new notebook
./observable.py new my-notebook.html --title "My Notebook" --theme air

# List cells
./observable.py list notebook.html
./observable.py list notebook.html --json  # JSON output

# Add a cell
./observable.py add notebook.html "Plot.plot({marks: [Plot.barY([1,2,3])]})"
./observable.py add notebook.html "# Title" --type text/markdown
./observable.py add notebook.html "code" --index 0  # Insert at position

# Edit a cell (by index or ID)
./observable.py edit notebook.html 0 "// New content"
./observable.py edit notebook.html cell-1 "// New content"

# Get cell content
./observable.py get notebook.html 0

# Delete a cell
./observable.py delete notebook.html 2

# Open in Observable Desktop
./observable.py open notebook.html

# Reload from disk (close + reopen)
./observable.py reload notebook.html

# Take screenshot of Observable Desktop
./observable.py screenshot
./observable.py screenshot -o /tmp/shot.png

# Edit and get visual feedback (use sparingly - causes window flash)
./observable.py edit-and-view notebook.html 1 "2 + 2"
# Returns path to screenshot showing result

# Capture specific cell silently (RECOMMENDED for verification)
./observable.py capture-cell notebook.html 5   # Capture cell at index 5

# Watch for changes and auto-reload (for interactive development)
./observable.py watch notebook.html

# DEPRECATED: render command - disrupts notebook state, avoid using
# ./observable.py render notebook.html  # DON'T USE - closes notebook
```

### obs-sync - Two-way Sync
```bash
./obs-sync notebook.html
# Watches for both:
# - CLI edits -> reloads Observable
# - Observable saves -> logs/notifies
```

## Workflow for Claude Code Agents

### Jeeves Mode (Recommended)

Work silently, present the finished notebook:

```bash
# 1. Create notebook (doesn't open Observable)
./observable.py new notebooks/analysis.html --title "My Analysis"

# 2. Edit cells by modifying HTML directly (use Edit tool)
# No need to open Observable at all during development

# 3. When ready, open for the user
./observable.py open notebooks/analysis.html

# 4. Present with context: "Your analysis is ready. Key findings..."
```

### With Verification (Recommended)

If you need to verify output before presenting:

```bash
# List cells to find indices
./observable.py list notebooks/analysis.html

# Capture specific cells to verify (completely silent)
./observable.py capture-cell notebooks/analysis.html 3   # Check main chart
./observable.py capture-cell notebooks/analysis.html 7   # Check stats table

# Review the screenshots to verify everything looks correct
# Then ALWAYS open for user at the end
./observable.py open notebooks/analysis.html
```

### Legacy: Visual Edit Loop

Use sparingly - causes window flashing:
```bash
# Edit a cell and see the result (flashes window)
SCREENSHOT=$(./observable.py edit-and-view notebook.html 1 "Math.PI * 2")
```

## Python API

```python
from observable import Notebook, take_screenshot, reload_notebook, edit_and_view

# Load notebook
nb = Notebook('notebook.html')

# List cells
for cell in nb.cells:
    print(f"{cell.index}: {cell.type} - {cell.content[:50]}")

# Add cell
nb.add_cell("Plot.plot({marks: [Plot.dot([1,2,3])]})", cell_type="module", pinned=True)
nb.save()

# Edit cell
nb.edit_cell(0, "// Updated content")
nb.save()

# Delete cell
nb.delete_cell(2)
nb.save()

# Reload in Observable Desktop
reload_notebook('notebook.html')

# Take screenshot
screenshot_path = take_screenshot()

# Edit and get visual feedback (best for agents)
screenshot_path = edit_and_view('notebook.html', 1, "new code")
```

## Important Notes

### Reloading
- `View > Reload` in Observable Desktop does NOT reload from disk
- Must close and reopen the file to see disk changes
- Use `./observable.py reload` or the watch command

### File Watching
- Uses `fswatch` for efficient change detection
- Falls back to polling if fswatch unavailable

### Screenshots
- **Use `capture-cell` for verification** - moves cell to top, captures, restores order (completely silent)
- The generic `screenshot` command brings Observable Desktop to front (avoid for Jeeves mode)
- Returns path to PNG file

### Two-way Sync
- Observable Desktop saves changes back to the HTML file when you Cmd+S
- The `obs-sync` tool detects both directions of changes

## Data Locations

| Location | Purpose |
|----------|---------|
| `~/Library/Application Support/com.observablehq.notebook-desktop/store.json` | API keys, settings |
| `~/Library/WebKit/com.observablehq.notebook-desktop/` | WebKit cache (empty) |
| `/Applications/Observable Desktop.app/` | Application bundle |

## Limitations

1. **No cloud API** - Cannot programmatically access cloud notebooks
2. **Must close/reopen** - View > Reload doesn't read from disk
3. **Tauri, not Electron** - Cannot use Electron debugging tools
4. **Safari Web Inspector** - Not exposed in release builds
5. **Brief focus steal** - Scroll commands briefly activate Observable (wait time reduced). Reloads are now backgrounded and do not steal focus.

## Scrolling (Deprecated)

**Prefer `capture-cell` instead** - it's completely silent and works for any cell position.

Scroll commands exist but steal focus and are no longer recommended:

```bash
# DEPRECATED - use capture-cell instead
./observable.py scroll --top      # Scroll to top
./observable.py scroll --bottom   # Scroll to bottom
./observable.py scroll --down 3   # Scroll down 3 pages
```

Scrolling requires briefly activating Observable (steals focus). Use `capture-cell` for silent operation.

## Background Mode

Screenshots can be taken without stealing focus from the current app:

```bash
# Background screenshot (default) - uses window ID capture
./observable.py screenshot

# Foreground screenshot (brings Observable to front)
./observable.py screenshot --foreground
```

The `edit-and-view` command:
- Saves your current active app
- Reloads Observable in the background (no focus change)
- Activates Observable briefly ONLY if scrolling is needed
- Restores focus to your previous app
- Takes screenshot in background

## Future Improvements

1. **Cell diffing** - Show what changed between versions
2. **Error detection** - Parse cell output for errors
3. **Better screenshot timing** - Wait for cells to finish rendering
4. **Full-page screenshot** - Scroll and stitch for complete notebook capture
5. **MCP server** - Expose as Model Context Protocol server for other agents
6. **JavaScript injection** - If devtools could be enabled, inject scroll commands

---

# Observable Notebook Reference

This section contains comprehensive documentation for writing Observable notebook cells.

## Complete Notebook File Format

A notebook HTML file consists of:
- A `<notebook>` root element
- An optional `<title>` element
- One `<script>` element per cell

### Indentation & Escaping

Cell source uses **four spaces of indentation** for each line; these leading spaces are trimmed when parsing.

**Escaping rules:**
- `</script>` must be escaped as `<\/script>`
- Backslashes need doubling: `\\` becomes `\`

### Notebook Attributes

```html
<notebook theme="air" readonly>
```

- **theme**: One of 13 themes (see Available Themes above)
- **readonly**: Disallows editing when present

## All Cell Types

| Type Attribute | Language | Description |
|----------------|----------|-------------|
| `module` | JavaScript | Default, reactive JS |
| `text/x-typescript` | TypeScript | TypeScript support |
| `text/markdown` | Markdown | Rich text formatting |
| `text/html` | HTML | Custom HTML markup |
| `application/sql` | SQL | Database queries |
| `application/x-tex` | LaTeX | Mathematical notation |
| `text/vnd.graphviz` | DOT | Graphviz diagrams |
| `application/vnd.observable.javascript` | Observable JS | Legacy Observable syntax |
| `application/vnd.node.javascript` | Node.js | Data loader |
| `text/x-python` | Python | Data loader |
| `text/x-r` | R | Data loader |

### Cell Attributes Reference

| Attribute | Purpose |
|-----------|---------|
| `type` | Cell language/mode |
| `pinned` | Show source code when present |
| `hidden` | Suppress implicit display output |
| `output` | Expose values for non-JS cells |
| `database` | Which database to query (SQL cells) |
| `format` | Output format for data loaders |
| `id` | Stable identifier (positive integer) |

## JavaScript Cells

### Cell Structures

**Expression** - Simple value:
```javascript
3 * 3 * 3
// Displays: 27
```

**Variable Definition** - Named, referenceable:
```javascript
myValue = 42
```

**Code Block** - Complex logic:
```javascript
{
  let sum = 0;
  for (let i = 0; i < 10; i++) sum += i;
  return sum;
}
```

### Object Literals

Wrap in parentheses to distinguish from code blocks:
```javascript
({name: "Alice", age: 30})
```

### Reactivity

Cells run in **topological order** based on dependencies, not sequential position. A cell referencing other cells re-evaluates automatically when dependencies change.

```javascript
// Cell 1
x = 5

// Cell 2 - updates whenever x changes
y = x * 2
```

### Async/Await

```javascript
data = await fetch("https://api.example.com/data").then(r => r.json())
```

### Generators

```javascript
// Counts up every second
{
  let i = 0;
  while (true) {
    yield i++;
    await Promises.delay(1000);
  }
}
```

## Markdown Cells

### Text Formatting

```markdown
*Italics* or _italics_
**Bold** or __bold__
~~Strikethrough~~
`inline code`
```

### Headings

```markdown
# Heading 1
## Heading 2
### Heading 3
#### Heading 4
##### Heading 5
```

### Lists

```markdown
- Unordered item
  - Nested item

1. Ordered item
   1. Nested ordered
```

### Links & Images

```markdown
[Link text](https://example.com)
![Alt text](${await FileAttachment("image.png").url()})
```

### Code Blocks

````markdown
```javascript
const x = 42;
```
````

### Tables

```markdown
Column 1 | Column 2 | Column 3
:------- | :------: | -------:
Left     | Center   | Right
```

### Embedded JavaScript

Use template literals for dynamic content:
```markdown
The value is ${myVariable}.
Today is ${new Date().toLocaleDateString()}.
```

## HTML Cells

```html
<div id="container">
  <p>Static HTML content</p>
  <p>Dynamic value: ${myVariable}</p>
</div>

<style>
#container p { color: blue; }
</style>
```

### Hypertext Literal (htl)

For dynamic HTML generation:
```javascript
htl.html`<ul>${data.map(d => htl.html`<li>${d.name}</li>`)}</ul>`
```

## SQL Cells

### Basic Query

```sql
SELECT * FROM customers WHERE country = 'USA'
```

### Parameterized Queries

```sql
SELECT * FROM products WHERE price < ${maxPrice}
```

### Database Attribute

```html
<script type="application/sql" database="mydb">
SELECT * FROM users
</script>
```

Results return as an **array of JavaScript objects**.

## TeX/LaTeX Cells

```latex
E = mc^2

\frac{-b \pm \sqrt{b^2 - 4ac}}{2a}

\sum_{i=1}^{n} x_i = x_1 + x_2 + \cdots + x_n
```

Uses KaTeX for rendering. See https://katex.org/ for syntax reference.

## Observable Plot

Plot is a JavaScript library for exploratory data visualization using composable marks.

### Basic Plot Structure

```javascript
Plot.plot({
  marks: [
    Plot.dot(data, {x: "column1", y: "column2"})
  ]
})
```

### Common Options

```javascript
Plot.plot({
  width: 800,
  height: 400,
  marginLeft: 60,
  marginBottom: 40,
  grid: true,
  x: {label: "X Axis Label"},
  y: {label: "Y Axis Label"},
  color: {legend: true},
  marks: [/* ... */]
})
```

### Mark Types

**Basic Marks:**
- `Plot.dot(data, options)` - Scatter plots, points
- `Plot.line(data, options)` - Line charts
- `Plot.areaY(data, options)` - Area charts
- `Plot.barY(data, options)` - Vertical bars
- `Plot.barX(data, options)` - Horizontal bars
- `Plot.cell(data, options)` - Heatmap cells
- `Plot.rect(data, options)` - Rectangles
- `Plot.text(data, options)` - Text labels
- `Plot.rule(data, options)` - Reference lines
- `Plot.tickX/tickY(data, options)` - Tick marks

**Statistical Marks:**
- `Plot.boxY(data, options)` - Box plots
- `Plot.density(data, options)` - Density estimation
- `Plot.contour(data, options)` - Contour lines
- `Plot.hexbin(data, options)` - Hexagonal binning
- `Plot.linearRegressionY(data, options)` - Regression lines

**Specialized Marks:**
- `Plot.link(data, options)` - Connections between points
- `Plot.arrow(data, options)` - Directional arrows
- `Plot.vector(data, options)` - Vector fields
- `Plot.geo(data, options)` - Geographic features
- `Plot.image(data, options)` - Raster images
- `Plot.tree(data, options)` - Tree structures
- `Plot.frame()` - Plot border

**Interactive:**
- `Plot.tip(data, options)` - Tooltips

### Channel Options

Channels vary per data element:
```javascript
Plot.dot(data, {
  x: "date",           // Column name
  y: d => d.value * 2, // Function
  fill: "category",    // Color by category
  r: "size",           // Radius by value
  title: "name"        // Tooltip text
})
```

### Constant Options

Apply uniformly:
```javascript
Plot.dot(data, {
  x: "date",
  y: "value",
  fill: "steelblue",   // All dots blue
  r: 5,                // All radius 5
  opacity: 0.7         // All 70% opacity
})
```

### Transforms

```javascript
// Binning
Plot.rectY(data, Plot.binX({y: "count"}, {x: "value"}))

// Grouping
Plot.barY(data, Plot.groupX({y: "sum"}, {x: "category", y: "value"}))

// Stacking
Plot.areaY(data, Plot.stackY({x: "date", y: "value", fill: "category"}))

// Sorting
Plot.barY(data, Plot.sort({x: "y"}, {x: "name", y: "value"}))
```

### Faceting

```javascript
Plot.plot({
  facet: {data, x: "region"},  // Split by region horizontally
  marks: [
    Plot.dot(data, {x: "date", y: "value"})
  ]
})
```

### Common Patterns

**Scatter plot:**
```javascript
Plot.dot(data, {x: "x", y: "y", fill: "category"}).plot()
```

**Line chart:**
```javascript
Plot.line(data, {x: "date", y: "value", stroke: "series"}).plot()
```

**Bar chart:**
```javascript
Plot.barY(data, {x: "category", y: "value", fill: "steelblue"}).plot()
```

**Histogram:**
```javascript
Plot.rectY(data, Plot.binX({y: "count"}, {x: "value"})).plot()
```

**Heatmap:**
```javascript
Plot.cell(data, {x: "col", y: "row", fill: "value"}).plot()
```

## Input Widgets

### viewof Syntax

```javascript
viewof myValue = Inputs.range([0, 100], {value: 50, step: 1, label: "Value"})
```

Reference the value in other cells:
```javascript
result = myValue * 2  // Reactive - updates when input changes
```

### Available Inputs

**Single Value:**
```javascript
Inputs.button("Click me")
Inputs.toggle({label: "Enable", value: true})
Inputs.range([min, max], {value, step, label})
Inputs.number([min, max], {value, step, label})
Inputs.text({label: "Name", placeholder: "Enter name"})
Inputs.textarea({label: "Description", rows: 5})
Inputs.date({label: "Date", value: new Date()})
Inputs.datetime({label: "DateTime"})
Inputs.color({label: "Color", value: "#ff0000"})
```

**Selection:**
```javascript
Inputs.radio(["A", "B", "C"], {label: "Choose one"})
Inputs.select(["A", "B", "C"], {label: "Select", multiple: false})
Inputs.checkbox(["A", "B", "C"], {label: "Select multiple"})
```

**File:**
```javascript
Inputs.file({label: "Upload", accept: ".csv,.json"})
```

**Tabular:**
```javascript
Inputs.search(data, {label: "Search"})
Inputs.table(data)
```

## File Attachments

### FileAttachment API

```javascript
// Text files
text = await FileAttachment("data.txt").text()

// JSON
data = await FileAttachment("data.json").json()

// CSV (with type inference)
data = await FileAttachment("data.csv").csv({typed: true})

// TSV
data = await FileAttachment("data.tsv").tsv({typed: true})

// Excel
workbook = await FileAttachment("data.xlsx").xlsx()
sheet = workbook.sheet("Sheet1", {headers: true})

// SQLite
db = await FileAttachment("database.db").sqlite()
results = await db.query("SELECT * FROM table")

// Images
img = await FileAttachment("image.png").image({width: 400})

// URL (for embedding)
url = await FileAttachment("file.pdf").url()

// Binary
buffer = await FileAttachment("data.bin").arrayBuffer()

// ZIP archives
archive = await FileAttachment("files.zip").zip()
file = await archive.file("inner.txt").text()
```

## Database Connections

### Supported Databases
- Amazon Redshift
- BigQuery
- Databricks
- MongoDB (SQL)
- MySQL
- Oracle
- PostgreSQL
- Snowflake
- SQL Server

### SQL Cell with Database

```html
<script type="application/sql" database="myConnection">
SELECT * FROM users WHERE active = true
</script>
```

## Imports

### Import from Other Notebooks

```javascript
import {chart} from "@username/notebook"
import {chart as myChart} from "@username/notebook"
import {chart} with {myData as data} from "@username/notebook"
```

### Import Libraries

```javascript
d3 = require("d3@7")
_ = require("lodash@4")
```

## Standard Library

### Built-in Variables

```javascript
now      // Current timestamp, reactive
width    // Page width, reactive
```

### Promises

```javascript
await Promises.delay(1000)           // Wait 1 second
await Promises.tick(1000)            // Wait until next second boundary
await Promises.when(new Date(...))   // Wait until specific time
```

### Generators

```javascript
// React to input changes
Generators.input(inputElement)

// Adapt push-based to pull-based
Generators.observe(notify => {
  // setup
  return () => { /* cleanup */ }
})
```

### DOM Utilities

```javascript
// Canvas context with proper DPI
ctx = DOM.context2d(width, height)

// Unique IDs for SVG
id = DOM.uid("gradient")
// Use: id.id, id.href
```

### Template Literals

```javascript
html`<div>HTML content</div>`
svg`<circle r="10"/>`
md`**Markdown** content`
tex`E = mc^2`
dot`digraph { A -> B }`
```

## Data Table Features

### Filtering
- String: `is`, `is not`, `contains`
- Numeric: `<`, `>`, `<=`, `>=`, `is not null`

### Derived Columns
```javascript
// In derived column expression:
row.price * row.quantity
```

### Convert to Code
Data tables can be converted to SQL queries or JavaScript code preserving filters, sorts, and slices.

## Tips for Writing Cells

1. **Name cells** you want to reference: `myData = [1, 2, 3]`
2. **Pin cells** to show code: add `pinned` attribute
3. **Use await** for async operations
4. **Return values** from blocks with `return`
5. **Object literals** need parentheses: `({key: value})`
6. **Reactivity is automatic** - cells update when dependencies change
7. **Order doesn't matter** - cells run in dependency order, not document order

---

# Mike Bostock's Visualization Philosophy

Mike Bostock (creator of D3.js and Observable) on the purpose of visualization:

> "I like the human-centric nature of visualization: you're creating something whose only goal is to help people understand or communicate."

> Per Ben Shneiderman: "The purpose of visualization is insight, not pictures." Visualization is a means to an end. A means to insight.

## The Ladder of Abstraction

Bostock envisions "a ladder of abstraction":
- **Lowest rung**: Low-level code (WebGL shaders, raw Canvas)
- **Middle rungs**: D3.js - efficient document manipulation based on data
- **Higher rungs**: Observable Plot - composable marks and transforms
- **Highest rung**: Visual interfaces with overview, zoom, filter, details-on-demand

Observable is building this ladder from the bottom up: JavaScript → Canvas/SVG → D3 → Plot.

## 10 Principles from 10 Years of Open-Source Visualization

1. **Teaching drives impact** - Documentation, tutorials, examples are central. Examples inspire, demonstrate techniques, and serve as building blocks.

2. **Support fuels research** - User questions reveal gaps and inform improvements.

3. **Technical features have hidden costs** - Interaction and animation risk obscuring insight. Static visualizations should be the foundation; flourishes should serve exploration, not replace clarity.

4. **Visualization exists on a spectrum** - Exploratory graphics prioritize speed for personal insight; explanatory graphics must communicate clearly.

5. **Data work dominates** - Data preparation is 80% of the effort. Tools like d3-array matter more than flashy rendering.

6. **Test forms against actual data** - Low-friction experimentation enables trying multiple approaches quickly.

7. **Interaction code is buggy** - Simpler interaction patterns reduce maintenance burden.

8. **Build community** - Find collaborators who provide validation, feedback, support, mentorship.

9. **Sustain through enjoyment** - Work you enjoy is more sustainable.

10. **D3's core contribution is a "kernel"** - Not a framework, but efficient manipulation of documents based on data.

## On Learning D3

> "Do I think people should learn D3? It shouldn't be your top priority. It's something you learn progressively when it's useful. We're optimizing what we spend our time on. Because D3 is so low-level, I worry about effort expended on technical aspects that don't directly contribute to understanding."

---

# Observable Plot: Advanced Reference

Plot's philosophy: **No chart types, only layered geometric marks.** Combine fundamental primitives to construct custom visualizations.

## Complete Mark Reference

### Core Marks
| Mark | Purpose |
|------|---------|
| `dot` | Points, scatter plots |
| `line` | Connect points with lines |
| `area` | Fill between curves |
| `bar` | Rectangular bars |
| `cell` | Grid cells (ordinal x ordinal) |
| `rect` | Rectangles (quantitative x quantitative) |
| `rule` | Reference lines |
| `text` | Labels |
| `tick` | Tick marks |
| `link` | Connections between points |
| `arrow` | Directional arrows |
| `frame` | Plot border |

### Statistical Marks
| Mark | Purpose |
|------|---------|
| `boxY` / `boxX` | Box plots showing distribution |
| `density` | Kernel density estimation |
| `linearRegressionY` | Fitted trend lines |

### Spatial Marks
| Mark | Purpose |
|------|---------|
| `contour` | Isolines for continuous data |
| `raster` | Pixel-based rendering, interpolation |
| `image` | Embed raster images |
| `geo` | Geographic/map features |

### Topological Marks (Delaunay/Voronoi)
| Mark | Purpose |
|------|---------|
| `voronoi` | Voronoi tessellation cells |
| `voronoiMesh` | Cell boundary mesh |
| `delaunayLink` | Triangulation edges |
| `delaunayMesh` | Triangulation mesh |
| `hull` | Convex hull |

### Hierarchical Marks
| Mark | Purpose |
|------|---------|
| `tree` | Tree/hierarchy layouts |
| `vector` | Vector fields |
| `waffle` | Square grid charts |

### Interactive
| Mark | Purpose |
|------|---------|
| `tip` | Tooltips on hover |
| `auto` | Automatically selects mark type |

## Advanced Mark Examples

### Voronoi Tessellation
```javascript
// Color regions by nearest point's category
Plot.plot({
  marks: [
    Plot.voronoi(data, {x: "x", y: "y", fill: "category", fillOpacity: 0.3}),
    Plot.voronoiMesh(data, {x: "x", y: "y", stroke: "gray"}),
    Plot.dot(data, {x: "x", y: "y", fill: "category"})
  ]
})
```

### Delaunay Triangulation
```javascript
// Show triangulation with convex hull
Plot.plot({
  marks: [
    Plot.delaunayMesh(data, {x: "x", y: "y", stroke: "#ccc"}),
    Plot.hull(data, {x: "x", y: "y", stroke: "red", strokeWidth: 2}),
    Plot.dot(data, {x: "x", y: "y"})
  ]
})
```

### Hexbin Heatmap
```javascript
// Hexagonal binning with count encoding
Plot.plot({
  color: {legend: true},
  marks: [
    Plot.hexgrid(),  // Show empty hexagons
    Plot.dot(data, Plot.hexbin({fill: "count"}, {
      x: "weight",
      y: "height",
      binWidth: 20
    }))
  ]
})
```

### Hexbin with Size Encoding
```javascript
// Bubble hexbin: size = count, color = mean value
Plot.plot({
  r: {range: [0, 14]},
  marks: [
    Plot.dot(data, Plot.hexbin(
      {r: "count", fill: "mean"},  // Bivariate encoding
      {x: "x", y: "y", fill: "value", binWidth: 30}
    ))
  ]
})
```

### Contour Density
```javascript
// Density contours from point cloud
Plot.plot({
  marks: [
    Plot.contour(data, {x: "x", y: "y", fill: "density", bandwidth: 20}),
    Plot.dot(data, {x: "x", y: "y", r: 1, fill: "white"})
  ]
})
```

### Raster with Barycentric Interpolation
```javascript
// Smooth interpolation from scattered samples
Plot.plot({
  color: {scheme: "viridis"},
  marks: [
    Plot.raster(data, {
      x: "longitude",
      y: "latitude",
      fill: "temperature",
      interpolate: "barycentric"  // Delaunay-based smooth interpolation
    })
  ]
})
```

### Function-Based Raster (Mandelbrot-style)
```javascript
// Evaluate function at each pixel
Plot.plot({
  marks: [
    Plot.raster({
      fill: (x, y) => Math.sin(x) * Math.cos(y),
      x1: -Math.PI, x2: Math.PI,
      y1: -Math.PI, y2: Math.PI
    })
  ]
})
```

## Complete Transform Reference

| Transform | Purpose |
|-----------|---------|
| `bin` | Group quantitative/temporal data into bins |
| `group` | Group ordinal/nominal data |
| `stack` | Stack values (for stacked charts) |
| `normalize` | Scale to [0,1] for proportions |
| `window` | Rolling/sliding window operations |
| `map` | Transform series values (normalize, cumsum) |
| `select` | Filter to specific points (first, last, min, max) |
| `hexbin` | Hexagonal binning |
| `centroid` | Compute centroids |
| `dodge` | Offset overlapping marks |
| `filter` | Filter data points |
| `sort` | Sort data |
| `reverse` | Reverse order |
| `shuffle` | Randomize order |
| `tree` | Compute tree layout |
| `interval` | Expand points to intervals |

### Transform Composition
Transforms are composable - chain them:
```javascript
Plot.barY(data,
  Plot.groupX(
    {y: "sum"},
    Plot.filter(d => d.value > 0, {x: "category", y: "value"})
  )
)
```

### Bin Transform
```javascript
// Histogram
Plot.rectY(data, Plot.binX({y: "count"}, {x: "value"}))

// 2D heatmap
Plot.rect(data, Plot.bin({fill: "count"}, {x: "a", y: "b"}))
```

### Group Transform
```javascript
// Bar chart with aggregation
Plot.barY(data, Plot.groupX({y: "sum"}, {x: "category", y: "amount"}))

// Multiple reducers
Plot.barY(data, Plot.groupX(
  {y: "mean", title: d => `n=${d.length}`},
  {x: "category", y: "value"}
))
```

### Stack Transform
```javascript
// Stacked area
Plot.areaY(data, Plot.stackY({x: "date", y: "value", fill: "category"}))

// Normalized (100%) stack
Plot.areaY(data, Plot.stackY({
  offset: "normalize",
  x: "date", y: "value", fill: "category"
}))
```

### Window Transform
```javascript
// Rolling average
Plot.line(data, Plot.windowY({k: 30, reduce: "mean"}, {x: "date", y: "value"}))

// Bollinger bands
Plot.bollinger(data, {x: "date", y: "close", n: 20, k: 2})
```

### Select Transform
```javascript
// Label only extremes
Plot.text(data, Plot.selectMaxY({x: "date", y: "value", text: "label"}))
```

## Reducers for Transforms

| Reducer | Output |
|---------|--------|
| `count` | Number of elements |
| `sum` | Sum of values |
| `mean` | Arithmetic mean |
| `median` | Median value |
| `min` / `max` | Extremes |
| `deviation` | Standard deviation |
| `variance` | Variance |
| `mode` | Most common value |
| `first` / `last` | First/last value |
| `proportion` | Fraction of total |
| `distinct` | Unique values count |
| Custom function | `(values, index) => result` |

## Scales & Axes

```javascript
Plot.plot({
  x: {
    type: "log",          // linear, log, sqrt, symlog, pow, time, utc, ordinal, band, point
    domain: [1, 1000],    // Data extent
    range: [0, width],    // Pixel extent
    label: "Value (log)", // Axis label
    tickFormat: "s",      // D3 format specifier
    grid: true            // Show gridlines
  },
  y: {
    nice: true,           // Round domain to nice values
    zero: true,           // Include zero
    reverse: true         // Flip direction
  },
  color: {
    type: "categorical",  // categorical, sequential, diverging, ordinal
    scheme: "tableau10",  // Color scheme name
    legend: true          // Show legend
  },
  r: {
    range: [1, 20]        // Radius range for size encoding
  }
})
```

## Color Schemes

**Sequential**: `blues`, `greens`, `greys`, `oranges`, `purples`, `reds`, `viridis`, `magma`, `inferno`, `plasma`, `warm`, `cool`, `turbo`

**Diverging**: `brbg`, `prgn`, `piyg`, `puor`, `rdbu`, `rdgy`, `rdylbu`, `rdylgn`, `spectral`

**Categorical**: `tableau10`, `category10`, `accent`, `dark2`, `paired`, `set1`, `set2`, `set3`

## Projections (for geo marks)

```javascript
Plot.plot({
  projection: "albers-usa",  // Or: mercator, equirectangular, orthographic, etc.
  marks: [
    Plot.geo(geoData, {fill: "value"})
  ]
})
```

## Sources

- [Observable Plot Documentation](https://observablehq.com/plot/)
- [Mike Bostock's 10 Years of Open-Source Visualization](https://observablehq.com/@mbostock/10-years-of-open-source-visualization)
- [Delaunay Marks](https://observablehq.com/plot/marks/delaunay)
- [Hexbin Transform](https://observablehq.com/plot/transforms/hexbin)
- [Raster Mark](https://observablehq.com/plot/marks/raster)
- [Transforms Overview](https://observablehq.com/plot/features/transforms)

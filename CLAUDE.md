# Observable Desktop Integration for Claude Code

This project enables Claude Code to programmatically edit and view Observable Desktop notebooks.

## Notebooks Directory

All notebooks live in `notebooks/`. **Before creating a new notebook**, always search existing notebooks to check if the user wants to edit/refactor an existing one:

```bash
# List existing notebooks
ls notebooks/

# Search notebook contents
grep -l "keyword" notebooks/*.html
```

Current notebooks:
- `reactivity-demo.html` - Demonstrates reactive variables, mutable state, viewof inputs
- `mutable-demo.html` - Mutable variable examples
- `ai-demo.html`, `ai-test.html` - AI-related experiments
- `hello.html` - Basic hello world

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

# Edit and get visual feedback (RECOMMENDED FOR AGENTS)
./observable.py edit-and-view notebook.html 1 "2 + 2"
# Returns path to screenshot showing result

# Watch for changes and auto-reload
./observable.py watch notebook.html
```

### obs-sync - Two-way Sync
```bash
./obs-sync notebook.html
# Watches for both:
# - CLI edits -> reloads Observable
# - Observable saves -> logs/notifies
```

## Workflow for Claude Code Agents

### Visual Edit Loop (Recommended)
```bash
# 1. Edit a cell and see the result
SCREENSHOT=$(./observable.py edit-and-view notebook.html 1 "Math.PI * 2")

# 2. View the screenshot to verify
# The screenshot shows the rendered notebook with your changes
```

### Manual Workflow
```bash
# 1. Start the watcher in a background terminal
./observable.py watch notebook.html &

# 2. Edit the HTML file directly
# (Claude Code edits the file)

# 3. Watcher auto-reloads Observable Desktop

# 4. Take screenshot to see result
./observable.py screenshot -o /tmp/result.png
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
- Uses macOS `screencapture` command
- Brings Observable Desktop to front before capture
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

## Scrolling

For cells in the bottom portion of the notebook, the tool scrolls to show them:

```bash
# Scroll commands
./observable.py scroll --top      # Scroll to top
./observable.py scroll --bottom   # Scroll to bottom
./observable.py scroll --down 3   # Scroll down 3 pages
```

The `edit-and-view` command automatically scrolls to show edited cells:
- Cells in the top 60% of notebook: scrolls from top using Page Downs
- Cells in the bottom 40%: scrolls to bottom, then up slightly to show output

**Note**: Scrolling requires briefly activating Observable (for keyboard events), but focus is restored to your previous app afterward. Delays have been optimized for better ergonomics.

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

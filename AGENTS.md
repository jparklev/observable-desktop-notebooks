# Observable Desktop Integration for Claude Code

> **CRITICAL: Always Use Gemini for Ideation and Review**
>
> Before building a notebook, use **Gemini CLI (`gemini-3-pro-preview`)** to:
> 1. **Ideate** — Outline the narrative arc, sections, and key visualizations
> 2. **Review** — After building, pipe the notebook to Gemini for critical review of mathematical accuracy, conceptual clarity, and missing nuances
>
> Gemini excels at catching errors (like confusing 1.5x Kelly for ruin when the threshold is actually 2x) and suggesting improvements. Always have Gemini in the loop.
>
> ```bash
> # Ideation
> gemini -m gemini-3-pro-preview "Design a notebook on [topic]. Outline sections, visualizations, key formulas..."
>
> # Review
> cat notebooks/my-notebook.html | gemini -m gemini-3-pro-preview "Review this notebook for mathematical accuracy, conceptual clarity, and missing nuances. Be critical."
> ```

> **CRITICAL: Silent Operation Required**
>
> When verifying notebook output, **ONLY use `capture-cell`**. This command moves the target cell to the top of the HTML, reloads in background, captures a screenshot silently, then restores the original order.
>
> The user should not see Observable Desktop until you call `open` to present the finished notebook.

## Jeeves Mode: Work Silently, Present Results

**Philosophy**: Like Wodehouse's Jeeves, handle everything behind the scenes with quiet competence. The user shouldn't see the sausage being made—no flashing windows, no interrupted focus, just results.

### Workflow

```bash
# 1. Create notebook
./observable.py new notebooks/analysis.html --title "My Analysis"

# 2. Edit cells directly in HTML (use Edit tool, no Observable needed)

# 3. Verify visualizations silently (iterate as needed)
./observable.py list notebooks/analysis.html              # Find cell indices
./observable.py capture-cell notebooks/analysis.html 3    # Check chart
# Adjust code, capture again until it looks right

# 4. Present the finished notebook
./observable.py open notebooks/analysis.html
```

**When presenting**: "Your analysis is ready, sir. Key findings: [summary]. The notebook is open for your review."

### Commands

| Command | Purpose | User Visible? |
|---------|---------|---------------|
| `new`, `add`, `edit`, `delete`, `get` | Edit notebook HTML | No |
| `list` | Show cell indices | No |
| `capture-cell <idx>` | Verify cell output silently | No |
| `open` | Present finished notebook | Yes |

## Writing Good Notebooks

### Prose and Analysis

Notebooks are literate documents. Include:
- What the visualization reveals
- Ambiguities or uncertainties in the data
- Decisions ("I chose a log scale because...")
- Questions that emerged during analysis
- A "Future Analysis Directions" section

**Every analytical choice needs justification:** Why this time period? Why these metrics? What are the limitations?

### Keep Notebooks Self-Contained

**Never hardcode computed values.** All data, fetches, calculations, attachments, and computations should live inside the notebook:

```javascript
// BAD: Magic numbers
sharpeRatio = 1.47

// GOOD: Computed from data
sharpeRatio = (d3.mean(returns) / d3.deviation(returns)) * Math.sqrt(252)
```

### Structure Convention

1. **Title & Introduction** - Markdown with context
2. **Main Content** - Section headers (markdown) + visualization cells only
3. **Appendix** - All data and computation cells at the bottom

Observable's reactive evaluation means cell order doesn't affect execution—cells run based on dependencies. Put plumbing at the bottom, keep the narrative clean.

### Cell Display Tips

Compute derived values inline to avoid clutter:

```javascript
{
  const bars = rawBars.map(d => ({date: new Date(d.t), close: d.c}));
  return Plot.plot({marks: [Plot.line(bars, {x: "date", y: "close"})]});
}
```

For time series with many points, use weekly binning and month ticks:
```javascript
Plot.rectY(data, Plot.binX({y: "sum"}, {x: "date", y: "volume", interval: "week"}))
// with: x: {type: "time", ticks: "month"}
```

## CLI Reference

```bash
# Notebook management
./observable.py new notebook.html --title "Title" --theme air
./observable.py list notebook.html [--json]
./observable.py add notebook.html "code" [--type text/markdown] [--index 0]
./observable.py edit notebook.html <idx|id> "new content"
./observable.py get notebook.html <idx>
./observable.py delete notebook.html <idx>

# Verification (SILENT)
./observable.py capture-cell notebook.html <idx>

# Presentation (USER-FACING)
./observable.py open notebook.html
```

## Notebook Format

Notebooks are HTML with a `<notebook>` root containing `<script>` cells:

```html
<!doctype html>
<notebook theme="air">
  <title>My Notebook</title>
  <script type="text/markdown">
# Markdown cell
  </script>
  <script type="application/vnd.observable.javascript" pinned>
myValue = 42
  </script>
</notebook>
```

### Cell Types

| Type | Use For |
|------|---------|
| `application/vnd.observable.javascript` | **Reactive JS (recommended)** - supports `viewof`, `mutable` |
| `text/markdown` | Prose, headers (supports `${variable}` interpolation) |
| `module` | Standard ES modules (no Observable features) |
| `application/sql` | Database queries |

**Use `application/vnd.observable.javascript`** for reactive notebooks, NOT `module`.

### Cell Attributes

- `pinned` - Show source code in rendered notebook
- `hidden` - Hide cell output (cell still runs)
- `id="..."` - Stable identifier for editing

### When to Pin Cells (Show Code)

Use judgment about what the user might want to inspect or modify:

**Pin these** (user likely wants to see/edit):
- Interactive inputs with `viewof` — users may want to tweak ranges, labels, options
- Key model parameters or assumptions they might want to adjust
- Novel or educational code patterns worth studying
- Data transformations the user might want to customize

**Don't pin these** (implementation detail, clutter):
- Standard Plot boilerplate — the chart speaks for itself
- Routine data loading (`fetch`, `FileAttachment`)
- Helper computations that aren't the focus
- Markdown cells (never need pinning)

**Example heuristic**: If the cell's *output* tells the whole story, don't pin. If the *code itself* is interesting or editable, pin it.

```html
<!-- PIN: User might adjust the elasticity range -->
<script type="application/vnd.observable.javascript" pinned>
viewof elasticity = Inputs.range([0.1, 2.0], {value: 1.0, step: 0.1, label: "Elasticity (σ)"})
</script>

<!-- DON'T PIN: Standard chart, output is what matters -->
<script type="application/vnd.observable.javascript">
Plot.plot({marks: [Plot.line(data, {x: "date", y: "value"})]})
</script>

<!-- PIN: Core model logic user might want to understand/modify -->
<script type="application/vnd.observable.javascript" pinned>
capitalShare = {
  const Kterm = alpha * Math.pow(K, rho);
  const Lterm = (1 - alpha) * Math.pow(L, rho);
  return Kterm / (Kterm + Lterm);
}
</script>
```

### Themes

Light: `air`, `cotton`, `glacier`, `parchment`, `stark`, `sun-faded`
Dark: `coffee`, `deep-space`, `ink`, `midnight`, `near-midnight`, `ocean-floor`, `slate`

---

# Observable Desktop Runtime

> **Important**: Observable Desktop is different from Observable Framework. Desktop runs standalone HTML notebooks with a reactive runtime. Framework is a static site generator with build-time features. Many Framework docs don't apply to Desktop.

## What Works in Observable Desktop

### Built-in Globals (No Import Needed)

These are available automatically in `application/vnd.observable.javascript` cells:

| Global | Description |
|--------|-------------|
| `Plot` | Observable Plot for visualization |
| `d3` | D3.js for data manipulation |
| `Inputs` | Interactive input widgets |
| `htl` / `html` | HTML template literals |
| `view` | Display element + return value generator |
| `Generators` | Async generators (`.observe`, `.input`) |
| `Mutable` | Mutable state containers |
| `FileAttachment` | Load local data files |
| `DuckDBClient` | In-browser SQL database |

### What Does NOT Work

| Feature | Status | Alternative |
|---------|--------|-------------|
| `npm:` imports | ❌ SyntaxError | Use built-in globals only |
| JSX / React | ❌ Framework-only | Use `htl.html` templates |
| Data loaders | ❌ Build-time feature | Use runtime `fetch()` |
| Global `sql` tag | ❌ Not defined | Use `db.sql` or `db.query()` instead |

## SQL with DuckDB

DuckDB runs entirely in-browser via WASM. Define a database, then query it.

### Setup Pattern

```javascript
// 1. Create database with inline data
db = DuckDBClient.of({
  sales: [
    {product: "Widget", revenue: 100, quarter: "Q1"},
    {product: "Gadget", revenue: 200, quarter: "Q1"}
  ]
})

// 2. Query with db.query() (string)
results = db.query("SELECT product, SUM(revenue) as total FROM sales GROUP BY product")

// 3. Or use db.sql tagged template (supports interpolation)
results = db.sql`SELECT * FROM sales WHERE revenue > ${minRevenue}`
```

### Loading External Data

```javascript
// Load CSV/Parquet into DuckDB
db = DuckDBClient.of({
  earthquakes: FileAttachment("quakes.csv")
})

// Or load from URL
db = DuckDBClient.of({
  earthquakes: "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.csv"
})
```

### SQL Cells

SQL cells (`application/sql`) work but need a `db` defined first:

```html
<!-- First, define db in a JS cell -->
<script type="application/vnd.observable.javascript">
db = DuckDBClient.of({mydata: [...]})
</script>

<!-- Then SQL cell can query it -->
<script type="application/sql">
SELECT * FROM mydata WHERE value > 100
</script>
```

### Reactive Queries

```javascript
// Input controls query parameters
viewof minRevenue = Inputs.range([0, 500], {value: 100, label: "Min Revenue"})

// Query re-runs when minRevenue changes
filtered = db.query(`SELECT * FROM sales WHERE revenue >= ${minRevenue}`)

// Display result
Inputs.table(filtered)
```

### Plotting SQL Results

```javascript
// DuckDB returns Arrow tables - Plot handles them directly
Plot.plot({
  marks: [
    Plot.barY(await db.query("SELECT product, SUM(revenue) as total FROM sales GROUP BY product"),
      {x: "product", y: "total"})
  ]
})
```

## Reactivity Model

Observable runs like a spreadsheet: cells re-run automatically when referenced variables change.

### Key Concepts

1. **Cells run in dependency order**, not document order
2. **Top-level assignments create reactive variables**: `x = 42`
3. **References automatically track dependencies**: a cell using `x` re-runs when `x` changes
4. **Promises are implicitly awaited** across cells
5. **Generators are implicitly iterated** across cells

### Reactive Patterns

```javascript
// Named cell (reactive variable)
data = [1, 2, 3, 4, 5]

// Dependent cell (auto-updates when data changes)
sum = d3.sum(data)

// Input with viewof (two-way binding)
viewof threshold = Inputs.range([0, 100], {value: 50, label: "Threshold"})

// Reactive computation using input
filtered = data.filter(d => d > threshold)

// Mutable state (when you need to mutate from multiple places)
mutableCounter = Mutable(0)
// Increment: ++mutableCounter.value
// Read in other cells: mutableCounter (just the value)
```

### Block Expressions

Use blocks to compute intermediate values without polluting the namespace:

```javascript
{
  const processed = rawData.map(d => transform(d));
  const filtered = processed.filter(d => d.value > 0);
  return Plot.plot({marks: [Plot.dot(filtered, {x: "x", y: "y"})]});
}
```

### Async Data Loading

```javascript
// Fetch from API (reactive - runs once, cached)
earthquakes = {
  const response = await fetch("https://earthquake.usgs.gov/...");
  return response.json();
}

// Reference in other cells (implicitly awaited)
Plot.dot(earthquakes.features, {...})
```

## Observable Inputs Reference

All inputs use the `viewof` pattern for reactivity:

```javascript
// Slider
viewof value = Inputs.range([min, max], {value: 50, step: 1, label: "Label"})

// Dropdown
viewof choice = Inputs.select(["A", "B", "C"], {label: "Choose", value: "A"})

// Radio buttons
viewof option = Inputs.radio(["X", "Y", "Z"], {label: "Pick one", value: "X"})

// Checkboxes (multiple selection)
viewof selected = Inputs.checkbox(["A", "B", "C"], {label: "Select", value: ["A"]})

// Text input
viewof query = Inputs.text({label: "Search", placeholder: "Type..."})

// Toggle (boolean)
viewof enabled = Inputs.toggle({label: "Enable", value: true})

// Button (triggers action)
viewof clicks = Inputs.button("Click me", {reduce: (n) => n + 1, value: 0})

// Data table (with selection)
viewof selected = Inputs.table(data, {columns: ["name", "value"], multiple: true})

// Search (filter data)
viewof results = Inputs.search(data, {placeholder: "Search..."})
```

### Input Options

Common options across input types:
- `label` - Label text
- `value` - Initial value
- `disabled` - Disable input
- `format` - Format displayed value: `format: x => x.toFixed(2)`

### Formatting Examples

```javascript
// Percentage slider
viewof rate = Inputs.range([0, 1], {
  value: 0.08,
  step: 0.01,
  label: "Rate",
  format: x => (x * 100).toFixed(0) + "%"
})

// Currency display
viewof price = Inputs.range([0, 1000], {
  value: 100,
  format: x => "$" + x.toFixed(2)
})
```

### Slider Value Display Issue

The number input boxes next to sliders can appear blank in Observable Desktop, making it hard for users to see the current value. **Always pair sliders with a markdown cell that displays the current value reactively.**

```html
<!-- Slider input -->
<script type="application/vnd.observable.javascript" pinned>
viewof rate = Inputs.range([0, 0.30], {value: 0.10, step: 0.01, label: "Return Rate"})
</script>

<!-- Display current value below -->
<script type="text/markdown">
**Current settings:** Return = ${(rate * 100).toFixed(0)}%
</script>
```

This ensures users can always see the exact slider values, especially when inputs are pinned and the code is visible but the rendered value isn't.

## Generators for Dynamic Values

```javascript
// Track pointer position
pointer = Generators.observe((notify) => {
  const handler = (e) => notify([e.clientX, e.clientY]);
  addEventListener("pointermove", handler);
  notify([0, 0]); // Initial value
  return () => removeEventListener("pointermove", handler); // Cleanup
})

// Animation frame counter
frame = {
  let i = 0;
  while (true) {
    yield i++;
    await new Promise(r => requestAnimationFrame(r));
  }
}
```

## HTML Templates with htl

```javascript
// Simple HTML
htl.html`<div style="color: red;">Hello</div>`

// With reactive interpolation
htl.html`<div>Value: ${someReactiveVariable}</div>`

// Complex layouts
htl.html`<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px;">
  ${items.map(item => htl.html`<div class="card">${item.name}</div>`)}
</div>`
```

## Markdown Interpolation

In `text/markdown` cells, use `${expression}` for reactive values:

```markdown
The current value is **${value}** and the sum is **${d3.sum(data)}**.
```

---

# Observable Plot Reference

Plot uses composable marks, not chart types. Combine primitives to build visualizations.

## Basic Structure

```javascript
Plot.plot({
  width: 800,
  height: 400,
  grid: true,
  x: {label: "X Axis"},
  y: {label: "Y Axis"},
  color: {legend: true},
  marks: [
    Plot.dot(data, {x: "col1", y: "col2", fill: "category"})
  ]
})
```

## Common Marks

| Mark | Purpose |
|------|---------|
| `dot` | Scatter plots |
| `line` | Line charts |
| `areaY` | Area charts |
| `barY` / `barX` | Bar charts |
| `cell` | Heatmaps |
| `text` | Labels |
| `rule` | Reference lines |
| `tip` | Tooltips |

## Transforms

```javascript
// Histogram
Plot.rectY(data, Plot.binX({y: "count"}, {x: "value"}))

// Grouped bars
Plot.barY(data, Plot.groupX({y: "sum"}, {x: "category", y: "amount"}))

// Stacked area
Plot.areaY(data, Plot.stackY({x: "date", y: "value", fill: "series"}))

// Rolling average
Plot.line(data, Plot.windowY({k: 30, reduce: "mean"}, {x: "date", y: "value"}))
```

## Scales

```javascript
x: {type: "log", domain: [1, 1000], label: "Value", grid: true}
y: {nice: true, zero: true}
color: {scheme: "tableau10", legend: true}
```

**Color schemes:**
- Sequential: `blues`, `viridis`, `turbo`
- Diverging: `rdbu`, `spectral`
- Categorical: `tableau10`, `category10`

## Input Widgets

```javascript
viewof myValue = Inputs.range([0, 100], {value: 50, label: "Value"})
viewof selection = Inputs.select(["A", "B", "C"], {label: "Choose"})
```

Reference the value reactively: `result = myValue * 2`

## File Attachments

```javascript
data = await FileAttachment("data.csv").csv({typed: true})
data = await FileAttachment("data.json").json()
img = await FileAttachment("image.png").image({width: 400})
```

---

# Mike Bostock's Visualization Philosophy

> "The purpose of visualization is insight, not pictures."

Key principles:
1. **Data work dominates** - Preparation is 80% of the effort
2. **Test forms against actual data** - Low-friction experimentation
3. **Technical features have hidden costs** - Static visualizations first; flourishes should serve exploration, not replace clarity
4. **Teaching drives impact** - Examples inspire and demonstrate

> "D3 is something you learn progressively when it's useful. Because it's so low-level, I worry about effort expended on technical aspects that don't directly contribute to understanding."

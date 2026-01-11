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

Claude orchestrates notebook creation, using Gemini for research, educational prose, and visual review.

### Phase 1: Research & Spec

**1. Topic research (Gemini Flash)**

For notebooks that require domain knowledge, use Gemini Flash for web research. Go beyond basic searches — find **curriculum-grade material**:

```bash
gemini -m gemini-3-flash-preview \
  "Research [TOPIC] for an educational data visualization notebook. Find:
   - University syllabi or course materials (MIT OCW, Stanford, etc.)
   - Key concepts to explain with mathematical precision
   - Common misconceptions students have about this topic
   - Ground truth values for verification (e.g., 'Black-Scholes call with S=100, K=100, T=1, r=0.05, σ=0.2 should be ~10.45')
   - Problem sets or exercises from textbooks
   - Real datasets or APIs for demonstration"
```

**2. Ground Truth Extraction**

For quantitative topics, **extract specific numeric values** that can be verified:

> *Example for Kelly Criterion:*
> - If p=0.6, b=1 (even money), Kelly bet = 0.20 (20%)
> - If p=0.55, b=2 (2:1 payoff), Kelly bet = 0.325 (32.5%)
> - A 50% loss requires a 100% gain to recover (not 50%)

These values become test cases during the Build phase.

**3. Data sourcing**

Identify where data will come from:
- **Public APIs** - Gemini can search for relevant APIs
- **Static datasets** - Download CSVs, JSON files
- **Generated data** - Synthetic data for teaching concepts
- **Data loaders** - Scripts that fetch/process data at build time

For real data, create a data loader or download to `notebooks/src/`.

**4. Example patterns (Gemini Flash)**

Scan the 233 examples for relevant visualization patterns:

```bash
ls observable-plot-docs/examples/ | gemini -m gemini-3-flash-preview \
  "User wants a notebook about [TOPIC]. Which 5-10 examples are most relevant?
   Return a numbered list with brief reasons. Keep response under 500 words."
```

**5. Claude decides approach**

Claude reviews Gemini's research and suggestions but has final authority. If no examples are helpful, Claude can use basic patterns (line charts, bar charts, etc.) without copying from examples.

**6. Draft spec with Test Plan**

Claude writes a spec that includes a **Test Plan** for calculation verification:

```markdown
## Spec: [Notebook Title]

### Teaching Goal
What should the reader understand after completing this notebook?

### Data Sources
- Static file, data loader, or inline?
- APIs with rate limits or authentication?

### Narrative Arc
1. Hook - Why should the reader care?
2. Build - Introduce concepts progressively
3. Insight - The "aha" moment
4. Conclusion - Practical takeaways

### Key Visualizations
- Chart 1: [description]
- Chart 2: [description]

### Interactive Elements
- Which parameters should be adjustable?
- What intuition should parameter exploration build?

### Test Plan (REQUIRED for quantitative notebooks)
Ground truth values that MUST be correct:
1. `kellyBet(0.6, 1)` should equal `0.20`
2. `recoveryGain(0.5)` should equal `1.0` (100% gain needed after 50% loss)
3. [Add specific test cases from research]

Common misconceptions to address:
- [Misconception 1]
- [Misconception 2]
```

**7. Spec review (Gemini Pro)**

```bash
cat spec.md | gemini -m gemini-3-pro-preview \
  "Review this notebook spec for a quantitative educational notebook. Check:
   - Are the ground truth test cases correct and sufficient?
   - Are there gaps in the narrative arc?
   - What common misconceptions are missing?
   - Are there opportunities for 'predict before reveal' exercises?
   - Is the math rigorous enough for an educated reader?"
```

Claude incorporates feedback and finalizes the spec.

### Phase 2: Build with Verification

**1. Import testing utilities**

For quantitative notebooks, import the testing helpers at the top:

```js
import { createSuite } from "./testing.js";
import { Quiz } from "./quiz.js";
```

**2. Write calculations with inline tests**

Place calculation logic in testable functions, then verify them immediately:

```js
// Define the calculation
function kellyBet(p, b) {
  const q = 1 - p;
  return (b * p - q) / b;
}

// Create a test suite (results exposed to bridge for verification)
const { test, view, stats } = createSuite("Kelly");

test("Even money, 60% win rate", (expect) => {
  expect(kellyBet(0.6, 1)).toBeCloseTo(0.20, 2);
});

test("2:1 odds, 55% win rate", (expect) => {
  expect(kellyBet(0.55, 2)).toBeCloseTo(0.325, 2);
});

// Display test results (must use display() since view() returns a DOM element)
display(view());
```

The `testing.js` library exposes results to the bridge, so `./viewer.py verify` can check for test failures.

**Important**: The `view()` function returns a DOM element. In the same code block where you run tests, call `display(view())` to render results. If you try to call `view()` from a separate code block, the variable won't be in scope.

**3. Build incrementally with verification**

Two approaches - choose based on notebook complexity:

**Option A: Sequential (simpler notebooks)**

Write one section → verify → get feedback → repeat.

```bash
# After each section
./viewer.py open notebooks/src/notebook.md --wait
./viewer.py verify
# Check for: page_errors, test failures in exposed_cells, visual issues
```

**Option B: Parallel (complex notebooks)**

Write all sections at once, then batch verify:

```bash
# Write complete notebook first
./viewer.py open notebooks/src/notebook.md --wait
./viewer.py verify  # Returns all screenshots + test results
```

**4. Check test results before visual review**

After `verify`, check the exposed cells for test suite results:

```bash
./viewer.py cells  # Look for test_suite_* entries
```

If any test suite shows `failed > 0`, **STOP and fix the bug before continuing**. Do not proceed to visual review with failing tests.

### Phase 3: Logic & Visual Review

Review happens in two stages: **logic verification** (catch calculation bugs) then **visual review** (catch presentation issues).

**Stage A: Logic Verification**

Before visual review, verify the math and logic are correct:

```bash
# Check test results
./viewer.py cells | grep test_suite

# If tests pass, proceed. If tests fail, fix bugs first.
```

**Stage B: Visual Review (Gemini Pro)**

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
   - Is the color scheme appropriate (FT Paper palette for parchment)?
   - Any visual issues (clipping, overlap, sizing)?
   - Does it effectively teach the concept?"

rm ./screenshot.png  # Clean up
```

**Stage C: Red-Teaming (Gemini Pro)**

For quantitative notebooks, run a **skeptical student** pass:

```bash
cat notebooks/src/notebook.md | gemini -m gemini-3-pro-preview \
  "You are a skeptical graduate student reviewing this educational notebook.

   Your job is to FIND BUGS, not praise the work. Look for:
   1. Mathematical errors or incorrect formulas
   2. Claims in the text that contradict what the charts show
   3. Missing edge cases (what happens at 0? at infinity? at negative values?)
   4. Logical leaps that aren't explained
   5. Incorrect intuitions being built by the interactive elements
   6. Quiz questions with wrong answers or misleading explanations

   Be specific. Quote the problematic text and explain what's wrong."
```

This catches bugs that visual review misses. The option hedging notebook bug (mentioned in project history) would have been caught by this step.

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

**Data Sources Appendix** - When a notebook fetches external data, add an appendix at the bottom showing:

1. **API/data source links** with documentation references
2. **Fetch code** displayed (not executed) using ` ```javascript ` blocks
3. **Data transformation code** showing how raw data becomes chart-ready
4. **Data notes** explaining units, refresh behavior, calculations

Example structure:

```markdown
## Appendix: Data Sources

### API Endpoint

**Source:** [API Documentation Link](https://example.com/docs)

Description of what the endpoint returns.

` ` `javascript
// Fetch code shown but NOT executed (use javascript, not js)
const data = await fetch("https://api.example.com/data").then(r => r.json())
` ` `

### Data Transformation

` ` `javascript
// Transformation code shown but NOT executed
const processed = data.map(d => ({ ... }))
` ` `

### Data Notes

- Note about data freshness
- Note about calculations
```

This appendix serves as documentation and helps readers understand what data powers the notebook.

### Workflow Summary

```
┌─────────────────────────────────────────────────────────────┐
│  RESEARCH         Gemini Flash: curriculum-grade research   │
│                   Extract ground truth test values          │
│                   Gemini Flash: data source discovery       │
│                   Gemini Flash: scan 233 examples           │
│                   Claude decides approach                   │
├─────────────────────────────────────────────────────────────┤
│  SPEC             Claude drafts spec + TEST PLAN            │
│                   Gemini Pro reviews (check math rigor)     │
│                   Claude finalizes                          │
├─────────────────────────────────────────────────────────────┤
│  BUILD            Import testing.js, quiz.js                │
│                   Claude writes notebook with inline tests  │
│                   Add interactive educational patterns      │
│                   ./viewer.py verify → test results + shots │
├─────────────────────────────────────────────────────────────┤
│  VERIFY           Check test_suite_* for failures           │
│                   ⚠️ STOP if tests fail — fix bugs first    │
├─────────────────────────────────────────────────────────────┤
│  REVIEW           Gemini Pro: visual review (screenshots)   │
│                   Gemini Pro: RED-TEAM (skeptical student)  │
│                   Find logic bugs, misconceptions, gaps     │
├─────────────────────────────────────────────────────────────┤
│  ITERATE          Claude fixes issues                       │
│                   Re-run tests and red-team                 │
│                   Repeat until robust                       │
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
- **Always constrain**: "List 5-10 items" (not "explore everything")
- **Always limit**: "Keep response under 500 words"

**Gemini Pro** (deep review, prose, visual analysis):
- Can handle more open-ended prompts
- Best for: spec review, visual/multimodal analysis, nuanced feedback, red-teaming
- **Educational prose**: Gemini Pro excels at writing multi-paragraph explanations, historical context, and conceptual deep-dives. Use it liberally for the prose portions of notebooks.
- Give context about what you're building and what to look for

**Educational Prose Generation (Gemini Pro)**

When you need rigorous explanatory prose, have Gemini write it:

```bash
gemini -m gemini-3-pro-preview \
  "Write a 3-paragraph introduction to [CONCEPT] for a data visualization notebook.

   Audience: Educated non-experts (curious engineers, finance professionals)
   Tone: Authoritative but accessible, like the Financial Times
   Include: Historical context, why it matters, one surprising insight
   Avoid: Jargon without explanation, hand-waving, oversimplification

   The introduction should hook the reader and set up the interactive exploration that follows."
```

**Bug-Finding Prompts (Gemini Pro)**

For quantitative notebooks, use Gemini Pro to find calculation errors:

```bash
cat notebooks/src/notebook.md | gemini -m gemini-3-pro-preview \
  "Find mathematical errors in this notebook. Check:
   1. Are formulas implemented correctly?
   2. Do examples use correct numeric values?
   3. Are edge cases handled (divide by zero, negative inputs)?
   4. Do charts match the math they claim to show?

   Quote problematic code and explain the bug."
```

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

### Interactive Educational Patterns

Beyond basic parameter sliders, use these patterns to deepen understanding:

**1. Prediction Exercises ("Guess Before Reveal")**

Force readers to commit to a mental model before seeing the answer:

```js
const userGuess = view(Inputs.range([0, 100], {
  label: "If an asset falls 50%, what % gain is needed to recover?",
  value: 50
}));
const reveal = view(Inputs.button("Check My Answer"));
```

```js
{
  if (reveal) {
    const correct = 100;  // 50% loss needs 100% gain
    const isClose = Math.abs(userGuess - correct) < 5;

    display(html`<div class="card" style="border-left: 4px solid ${isClose ? "#2d724f" : "#b3312c"};">
      <strong>${isClose ? "Correct!" : "Not quite."}</strong>
      A 50% loss reduces $100 to $50. To recover, you need +$50 on a $50 base = <strong>100% gain</strong>.
    </div>`);

    // Show the visual proof
    display(Plot.plot({
      title: "The Recovery Trap",
      marks: [
        Plot.line(d3.range(0, 90, 1).map(loss => ({
          loss,
          recovery: (1 / (1 - loss/100) - 1) * 100
        })), {x: "loss", y: "recovery", stroke: "#b3312c"}),
        Plot.dot([{loss: 50, recovery: 100}], {x: "loss", y: "recovery", r: 6, fill: "#0f5499"})
      ]
    }));
  }
}
```

**2. Goal-Seeking Exploration**

Instead of passive slider exploration, give a specific target:

```js
display(md`### Challenge: Find the Optimal Leverage
Adjust the slider until you maximize the **Growth Rate**. The curve turns red in the ruin zone.`);

const leverage = view(Inputs.range([0, 2], {label: "Leverage", step: 0.05, value: 0.5}));
```

```js
{
  const p = 0.6, b = 1;
  const optimalF = p - (1 - p);  // 0.20
  const growth = p * Math.log(1 + b * leverage) + (1 - p) * Math.log(1 - Math.min(leverage, 0.99));
  const efficiency = growth / (p * Math.log(1 + b * optimalF) + (1 - p) * Math.log(1 - optimalF)) * 100;
  const color = leverage > 2 * optimalF ? "#b3312c" : "#0f5499";

  display(html`<div style="font-size: 1.5rem; color: ${color};">
    Efficiency: <strong>${efficiency.toFixed(0)}%</strong>
    ${leverage > 2 * optimalF ? " — RUIN ZONE" : ""}
  </div>`);
}
```

**3. Knowledge Check Quizzes**

Use the `quiz.js` helper for multiple-choice questions:

```js
import { Quiz } from "./quiz.js";

display(Quiz({
  question: "If volatility doubles, what happens to the option price?",
  options: ["It doubles", "It increases (but less than 2x)", "It stays the same", "It decreases"],
  correctIndex: 1,
  explanation: "Option prices increase with volatility, but the relationship is not linear. The vega (volatility sensitivity) depends on time to expiration and moneyness."
}));
```

**4. Worked Examples with Missing Variables**

Show a complete calculation but leave one step for the reader:

```js
display(md`**Exercise:** A trading system has a **55% win rate** (p=0.55) and **2:1 payoff** (b=2).
Using the Kelly formula f* = (bp - q) / b, calculate the optimal bet size.`);

const userCalc = view(Inputs.number({label: "Your answer (decimal, e.g., 0.25)", step: 0.01}));
```

```js
{
  if (userCalc !== null) {
    const correct = (2 * 0.55 - 0.45) / 2;  // 0.325
    const error = Math.abs(userCalc - correct);

    if (error < 0.01) {
      display(md`✅ **Correct!** f* = (2 × 0.55 - 0.45) / 2 = 0.325 or **32.5%**`);
    } else {
      display(md`❌ **Try again.** Hint: q = 1 - 0.55 = 0.45. The numerator is (2 × 0.55) - 0.45 = 0.65.`);
    }
  }
}
```

**5. Counter-Example Simulations**

Address misconceptions by simulating them to failure:

```js
display(md`### The Martingale Fallacy
"Just double your bet after every loss." Let's see what happens.`);

const maxDoubles = view(Inputs.range([3, 10], {label: "Max consecutive losses before bust", step: 1, value: 5}));
```

Then simulate 1000 traders using Martingale and show how they all eventually hit the losing streak that wipes them out.

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

### Color Palette for Parchment Theme

The parchment theme has a warm peachy background (`#f9f0ea`) and brown text (`#4a413a`). Avoid bright "digital" colors that clash with the paper aesthetic. Use the "FT Paper" palette inspired by the Financial Times' data visualization on their pink background:

**Recommended Palette (FT Paper):**

| Role | Hex | Name | Use For |
|------|-----|------|---------|
| **Primary** | `#0f5499` | FT Dark Blue | Main data, volume bars, primary metrics |
| **Secondary** | `#a0616a` | Dusty Rose | Secondary data, contrast, highlights |
| **Positive** | `#2d724f` | Muted Green | Gains, upward trends, success states |
| **Negative** | `#b3312c` | Brick Red | Losses, downward trends, error states |
| **Neutral** | `#7a8b8a` | Gray-Green | "Other" categories, muted elements |
| **Accent** | `#c78c39` | Warm Amber | Tertiary data, count metrics |

**Why These Colors Work:**

1. **Editorial sophistication** - Inspired by FT's proven palette on warm backgrounds
2. **Ink-on-paper feel** - Slightly desaturated, feels printed rather than digital
3. **Clear semantic meaning** - Green/red for positive/negative are muted but distinct

**What to Avoid:**

- Bright saturated colors (too "digital" for parchment)
- Pure yellows - get lost on cream/parchment backgrounds
- Solarized colors - designed for code editors, too saturated for print aesthetic

**Resources:**

- [Datawrapper: Colors in Data Vis Style Guides](https://www.datawrapper.de/blog/colors-for-data-vis-style-guides/)
- [FT Visual Vocabulary](https://github.com/Financial-Times/chart-doctor/tree/main/visual-vocabulary)
- Observable Plot schemes: `rdylbu`, `warm`, `cool` work well with parchment

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
1. **Check the path** - Must be `notebooks/src/notebook.md` (not `src/notebook.md` or doubled paths)
2. **Verify the URL** in `./viewer.py open` output - should show `/notebook-name` not `/path/to/notebook-name`
3. **Instance conflict** - Another viewer instance may be interfering. Use instance isolation:
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

### 8. Semicolons on `view()` Break Cross-Cell Access
This is subtle but critical. When defining reactive inputs, the semicolon determines variable scope:

```js
// WRONG - revealAnswer is NOT exported to page scope
const revealAnswer = view(Inputs.button("Check"));  // semicolon!
```

```js
// In another cell:
if (revealAnswer) { ... }  // ReferenceError: Can't find variable: revealAnswer
```

```js
// CORRECT - no semicolon exports the variable
const revealAnswer = view(Inputs.button("Check"))
```

```js
// Now this works!
if (revealAnswer) { ... }
```

**Rule**: When using `view()` to create a reactive variable that other cells need, **never end with a semicolon**.

### 9. htl.html Doesn't Support Reactive Expressions
The `html` tagged template literal does NOT support reactive arrow functions:

```js
// WRONG - renders the function text, not its result
html`<div>${() => someReactiveValue}</div>`
// Output: "<div>() => someReactiveValue</div>"

// CORRECT - use DOM manipulation for dynamic content
const div = document.createElement("div");
div.textContent = someReactiveValue;
```

For complex interactive components, use imperative DOM manipulation (see `quiz.js` for an example).

### 10. SQL Code Blocks Have Table Registration Issues
The ` ```sql ` syntax can fail if tables aren't properly registered:

```js
// WRONG - may fail with "table not found"
```sql id=stats
SELECT * FROM myData GROUP BY category
```

```js
// CORRECT - use db.query() for reliability
const db = await DuckDBClient.of({ myData });
const stats = await db.query(`SELECT * FROM myData GROUP BY category`);
```

### 11. Helper Modules Should Use Plain JS State
When creating reusable modules (like `testing.js`), avoid Observable-specific constructs:

```js
// WRONG - Mutable may not work in helper modules
import { Mutable } from "observablehq:stdlib";
const state = Mutable([]);  // "change is not a function" error

// CORRECT - plain JS works everywhere
const state = [];
function addItem(item) { state.push(item); }
```

Observable's `Mutable` is designed for cross-cell reactivity in notebooks, not for internal module state.

### 12. Verify Viewer Path After Restart
After restarting the viewer, always confirm the notebook loaded correctly:

```bash
./viewer.py open notebooks/src/notebook.md --wait
./viewer.py verify
# Check the URL in output - should NOT show "Not found"
```

Common path mistakes:
- `src/notebook.md` (missing `notebooks/` prefix)
- `notebooks/notebooks/src/notebook.md` (doubled prefix)
- `notebook` (missing `.md` extension)

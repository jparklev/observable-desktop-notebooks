---
url: "https://observablehq.com/framework/convert"
title: "Converting notebooks | Observable Framework"
---

01. [JavaScript syntax](https://observablehq.com/framework/convert#java-script-syntax)
02. [Imports](https://observablehq.com/framework/convert#imports)
03. [Generators](https://observablehq.com/framework/convert#generators)
04. [Views](https://observablehq.com/framework/convert#views)
05. [Mutables](https://observablehq.com/framework/convert#mutables)
06. [Standard library](https://observablehq.com/framework/convert#standard-library)
07. [File attachments](https://observablehq.com/framework/convert#file-attachments)
08. [Recommended libraries](https://observablehq.com/framework/convert#recommended-libraries)
09. [Sample datasets](https://observablehq.com/framework/convert#sample-datasets)
10. [Cell modes](https://observablehq.com/framework/convert#cell-modes)
11. [Databases](https://observablehq.com/framework/convert#databases)
12. [Secrets](https://observablehq.com/framework/convert#secrets)

# [Converting notebooks](https://observablehq.com/framework/convert\#converting-notebooks)

Framework’s built-in `convert` command helps you convert an [Observable notebook](https://observablehq.com/documentation/notebooks/) to standard [Markdown](https://observablehq.com/framework/markdown) for use with Observable Framework. To convert a notebook, you need its URL; pass it to the `convert` command like so:

```sh
npm run observable convert <notebook-url>
```

The above command assumes you’re running `convert` within an existing project. Outside of a project, you can use npx:

```sh
npx @observablehq/framework@latest convert <notebook-url>
```

You can convert multiple notebooks by passing multiple URLs:

```sh
npm run observable convert <url1> <url2> <url3>
```

The `convert` command currently only supports public notebooks. To convert a private notebook, you can (temporarily) make the notebook public unlisted by clicking **Share…** on the notebook and choosing **Can view (unlisted)** under **Public** access. Please upvote [#1578](https://github.com/observablehq/framework/issues/1578) if you are interested in support for converting private notebooks.

For example, to convert D3’s [_Zoomable sunburst_](https://observablehq.com/@d3/zoomable-sunburst):

```sh
npm run observable convert https://observablehq.com/@d3/zoomable-sunburst
```

This will output something like:

```
┌   observable convert
│
◇  Downloaded zoomable-sunburst.md in 443ms
│
◇  Downloaded flare-2.json in 288ms
│
└  1 notebook converted; 2 files written
```

The `convert` command generates files in the source root of the current project by default (typically `src`); you can change the output directory using the `--output` command-line flag. The command above generates two files: `zoomable-sunburst.md`, a Markdown file representing the converted notebook; and `flare-2.json`, an attached JSON file.

Due to differences between Observable Framework and Observable notebooks, the `convert` command typically won’t produce a working Markdown page out of the box; you’ll often need to make further edits to the generated Markdown. We describe these differences below, along with examples of manual conversion.

The `convert` command has minimal “magic” so that its behavior is easier to understand and because converting notebook code into standard Markdown and JavaScript requires human interpretation. Still, we’re considering making `convert` smarter; let us know if you’re interested.

## [JavaScript syntax](https://observablehq.com/framework/convert\#java-script-syntax)

Framework uses vanilla [JavaScript syntax](https://observablehq.com/framework/javascript) while notebooks use a nonstandard dialect called [Observable JavaScript](https://observablehq.com/documentation/cells/observable-javascript). A JavaScript cell in a notebook is technically not a JavaScript program ( _i.e._, a sequence of statements) but rather a _cell declaration_; it can be either an _expression cell_ consisting of a single JavaScript expression (such as `1 + 2`) or a _block cell_ consisting of any number of JavaScript statements (such as `console.log("hello");`) surrounded by curly braces. These two forms of cell require slightly different treatment. The `convert` command converts both into JavaScript [fenced code blocks](https://observablehq.com/framework/javascript#fenced-code-blocks).

### [Expression cells](https://observablehq.com/framework/convert\#expression-cells)

Named expression cells in notebooks can be converted into standard variable declarations, typically using `const`. So this:

```js
foo = 42
```

Becomes this:

```js
const foo = 42;
```

Variable declarations in Framework don’t implicitly display. To inspect the value of a variable (such as `foo` above), call `display` explicitly.

Framework allows multiple variable declarations in the same code block, so you can coalesce multiple JavaScript cells from a notebook into a single JavaScript code block in Framework. Though note that there’s no [implicit `await`](https://observablehq.com/framework/reactivity#promises) when referring to a variable declared in the same code block, so beware of promises.

Anonymous expression cells become expression code blocks in Framework, which work the same, so you shouldn’t have to make any changes.

3

```js
1 + 2
```

While a notebook is limited to a linear sequence of cells, Framework allows you to interpolate dynamic values anywhere on the page: consider using an [inline expression](https://observablehq.com/framework/javascript#inline-expressions) instead of a fenced code block.

### [Block cells](https://observablehq.com/framework/convert\#block-cells)

Block cells are used in notebooks for more elaborate definitions. They are characterized by curly braces (`{…}`) and a return statement to indicate the cell’s value. Here is an abridged typical example adapted from D3’s [_Bar chart_](https://observablehq.com/@d3/bar-chart/2):

```js
chart = {
  const width = 960;
  const height = 500;

  const svg = d3.create("svg")
      .attr("width", width)
      .attr("height", height);

  return svg.node();
}
```

To convert a named block cell to vanilla JavaScript: delete the cell name (`chart`), assignment operator (`=`), and surrounding curly braces (`{` and `}`); then replace the return statement with a variable declaration and a call to [`display`](https://observablehq.com/framework/javascript#explicit-display) as desired.

```js
const width = 960;
const height = 500;

const svg = d3.create("svg")
    .attr("width", width)
    .attr("height", height);

const chart = display(svg.node());
```

For an anonymous block cell, omit the variable declaration. To hide the display, omit the call to `display`; you can use an [inline expression](https://observablehq.com/framework/javascript#inline-expressions) ( _e.g._, `${chart}`) to display the chart elsewhere.

If you prefer, you can instead convert a block cell into a function such as:

```js
function chart() {
  const width = 960;
  const height = 500;

  const svg = d3.create("svg")
      .attr("width", width)
      .attr("height", height);

  return svg.node();
}
```

Then call the function from an inline expression ( _e.g._, `${chart()}`) to display its output anywhere on the page. This technique is also useful for importing a chart definition into multiple pages.

## [Imports](https://observablehq.com/framework/convert\#imports)

Notebooks often import other notebooks from Observable or open-source libraries from npm. Imports require additional manual conversion.

If the converted notebook [imports other notebooks](https://observablehq.com/documentation/notebooks/imports), you should convert the imported notebooks, too. Extract the desired JavaScript code from the imported notebooks into standard [JavaScript modules](https://observablehq.com/framework/imports#local-imports) which you can then import in Framework.

In Framework, reactivity only applies to [top-level variables](https://observablehq.com/framework/reactivity#top-level-variables) declared in fenced code blocks. If the imported code depends on reactivity or uses [`import-with`](https://observablehq.com/documentation/notebooks/imports#import-with), you will likely need to do some additional refactoring, say converting JavaScript cells into functions that take options.

Some notebooks use [`require`](https://observablehq.com/documentation/cells/require) to load libraries from npm. Framework discourages the use of `require` and does not include built-in support for it because the asynchronous module definition (AMD) convention has been superseded by standard [JavaScript modules](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules). Also, Framework preloads transitive dependencies using static analysis to improve performance, and self-hosts imports to eliminate a runtime dependency on external servers to improve security and give you control over library versioning. So this:

```js
regl = require("regl")
```

Should be converted to a static [npm import](https://observablehq.com/framework/imports#npm-imports):

```js
import regl from "npm:regl";
```

The code above imports the default export from [regl](https://github.com/regl-project/regl). For other libraries, such as D3, you should use a namespace import instead:

```js
import * as d3 from "npm:d3";
```

You can import [d3-require](https://github.com/d3/d3-require) if you really want to a `require` implementation; we just don’t recommend it.

Likewise, instead of `resolve` or `require.resolve`, use [`import.meta.resolve`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/import.meta/resolve). So this:

```js
require.resolve("regl")
```

Should be converted to:

```js
import.meta.resolve("npm:regl")
```

Some notebooks use [dynamic import](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/import) to load libraries from npm-backed CDNs such as [jsDelivr](https://www.jsdelivr.com/esm) and [esm.sh](https://esm.sh/). While you can use dynamic imports in Framework, for security and performance, we recommend converting these into static imports. So this:

```js
isoformat = import("https://esm.sh/isoformat")
```

Should be converted to:

```js
import * as isoformat from "npm:isoformat";
```

If you do not want to self-host an import, say because you want the latest version of the library to update without having to rebuild your app, you can load it from an external server by providing an absolute URL:

```js
import * as isoformat from "https://esm.sh/isoformat";
```

## [Generators](https://observablehq.com/framework/convert\#generators)

In notebooks, the `yield` operator turns any cell [into a generator](https://observablehq.com/documentation/cells/observable-javascript#cells-implicitly-iterate-over-generators). In vanilla JavaScript, the `yield` operator is only allowed within generator functions. Therefore in Framework you’ll need to wrap a generator cell declaration with an immediately-invoked generator function expression (IIGFE). So this:

```js
foo = {
  for (let i = 0; i < 10; ++i) {
    yield i;
  }
}
```

Can be converted to:

```js
const foo = (function* () {
  for (let i = 0; i < 10; ++i) {
    yield i;
  }
})();
```

Since variables are evaluated lazily, the generator `foo` above will only run if it is referenced by another code block. If you want to perform asynchronous side effects, consider using an animation loop and the [invalidation promise](https://observablehq.com/framework/reactivity#invalidation) instead of a generator.

If you need to use `await` with the generator, too, then use `async function*` to declare an async generator function instead.

## [Views](https://observablehq.com/framework/convert\#views)

In notebooks, the nonstandard [`viewof` operator](https://observablehq.com/@observablehq/views) is used to declare a reactive value that is controlled by a user interface element such as a range input. In Framework, the [`view` function](https://observablehq.com/framework/reactivity#inputs) performs the equivalent task with vanilla syntax. So this:

```js
viewof gain = Inputs.range([0, 11], {value: 5, step: 0.1, label: "Gain"})
```

Can be converted to:

```js
const gain = view(Inputs.range([0, 11], {value: 5, step: 0.1, label: "Gain"}));
```

In other words: replace `viewof` with `const`, and then wrap the input declaration with a call to `view`. The `view` function both displays the given input and returns the corresponding value generator so you can define a top-level reactive value.

## [Mutables](https://observablehq.com/framework/convert\#mutables)

In notebooks, the nonstandard [`mutable` operator](https://observablehq.com/@observablehq/mutable) is used to declare a reactive value that can be assigned from another cell. In Framework, the [`Mutable` function](https://observablehq.com/framework/reactivity#mutables) performs the equivalent task with vanilla syntax. So this:

```js
mutable foo = 42
```

Can be converted to:

```js
const foo = Mutable(42);
const setFoo = (x) => (foo.value = x);
```

Then replace any assignments to `mutable foo` with calls to `setFoo`. Note that `setFoo` must be declared in the same code block as `foo`, and that outside of that block, `foo` represents the value; any code that depends on `foo` will update reactively after `setFoo` is invoked.

## [Standard library](https://observablehq.com/framework/convert\#standard-library)

As part of our modernization efforts with Framework, we’ve pruned deprecated methods from the standard library used in notebooks. The following notebook built-ins are not available in Framework:

- [`DOM`](https://github.com/observablehq/stdlib/blob/493bf210f5fcd9360cf87a961403aa963ba08c96/src/dom/index.js)
- [`Files`](https://github.com/observablehq/stdlib/blob/493bf210f5fcd9360cf87a961403aa963ba08c96/src/files/index.js)
- [`Generators.disposable`](https://github.com/observablehq/stdlib/blob/493bf210f5fcd9360cf87a961403aa963ba08c96/src/generators/disposable.js)
- [`Generators.filter`](https://github.com/observablehq/stdlib/blob/493bf210f5fcd9360cf87a961403aa963ba08c96/src/generators/filter.js)
- [`Generators.map`](https://github.com/observablehq/stdlib/blob/493bf210f5fcd9360cf87a961403aa963ba08c96/src/generators/map.js)
- [`Generators.range`](https://github.com/observablehq/stdlib/blob/493bf210f5fcd9360cf87a961403aa963ba08c96/src/generators/range.js)
- [`Generators.valueAt`](https://github.com/observablehq/stdlib/blob/493bf210f5fcd9360cf87a961403aa963ba08c96/src/generators/valueAt.js)
- [`Generators.worker`](https://github.com/observablehq/stdlib/blob/493bf210f5fcd9360cf87a961403aa963ba08c96/src/generators/worker.js)
- [`Promises`](https://github.com/observablehq/stdlib/blob/493bf210f5fcd9360cf87a961403aa963ba08c96/src/promises/index.js)
- [`md`](https://github.com/observablehq/stdlib/blob/493bf210f5fcd9360cf87a961403aa963ba08c96/src/md.js)
- [`require`](https://github.com/observablehq/stdlib/blob/493bf210f5fcd9360cf87a961403aa963ba08c96/src/require.js)
- [`resolve`](https://github.com/observablehq/stdlib/blob/493bf210f5fcd9360cf87a961403aa963ba08c96/src/require.js)

For convenience, we’ve linked to the implementations above so that you can see how they work, and if desired, copy the code into your own Framework app as vanilla JavaScript. For example, for a [2D canvas](https://developer.mozilla.org/en-US/docs/Web/API/CanvasRenderingContext2D), you can replace `DOM.context2d` with:

```js
function context2d(width, height, dpi = devicePixelRatio) {
  const canvas = document.createElement("canvas");
  canvas.width = width * dpi;
  canvas.height = height * dpi;
  canvas.style = `width: ${width}px;`;
  const context = canvas.getContext("2d");
  context.scale(dpi, dpi);
  return context;
}
```

For `md`, we recommend writing literal Markdown. To parse dynamic Markdown, you can also import your preferred parser such as [markdown-it](https://github.com/markdown-it/markdown-it) from npm.

In addition to the above removals, a few of the built-in methods have changed:

- `FileAttachment` (see [below](https://observablehq.com/framework/convert#file-attachments))
- `Generators.input` is now an async generator
- `Generators.observe` is now an async generator
- `Generators.queue` is now an async generator
- `Mutable` (see [above](https://observablehq.com/framework/convert#mutables))
- `width` uses [`ResizeObserver`](https://developer.mozilla.org/en-US/docs/Web/API/ResizeObserver) instead of window _resize_ events

The Framework standard library also includes several new methods that are not available in notebooks. These are covered elsewhere: [`Generators.dark`](https://observablehq.com/framework/lib/generators#dark) and [`dark`](https://observablehq.com/framework/lib/generators#dark); [`Generators.now`](https://observablehq.com/framework/lib/generators#now); [`Generators.width`](https://observablehq.com/framework/lib/generators#width-element) and [`resize`](https://observablehq.com/framework/javascript#resize-render); [`display`](https://observablehq.com/framework/javascript#display-value); and [`sql`](https://observablehq.com/framework/sql#sql-literals).

## [File attachments](https://observablehq.com/framework/convert\#file-attachments)

Framework’s [`FileAttachment`](https://observablehq.com/framework/files) includes a few new features:

- `file.href`
- `file.size`
- `file.lastModified`
- `file.mimeType` is always defined
- `file.text` now supports an `encoding` option
- [`file.arquero`](https://observablehq.com/framework/lib/arquero)
- [`file.parquet`](https://observablehq.com/framework/lib/arrow#apache-parquet)

And two removals:

- `file.csv` _etc._ treats the `typed: "auto"` option as `typed: true`
- `file.arrow` doesn’t take a `version` option

For the latter, `file.arrow` now imports `npm:apache-arrow` internally, and thus uses the same version of Arrow as if you imported Arrow directly.

## [Recommended libraries](https://observablehq.com/framework/convert\#recommended-libraries)

In Framework, implicit imports of recommended libraries are normal [npm imports](https://observablehq.com/framework/imports#npm-imports), and thus are self-hosted, giving you control over versioning. If a requested library is not in your [npm cache](https://observablehq.com/framework/imports#self-hosting-of-npm-imports), then by default the latest version will be downloaded. You can request a more specific version either by seeding the npm cache or by including a semver range in the import specifier ( _e.g._, `import * as d3 from "npm:d3@6"`).

Because Framework defaults to the latest version of recommended libraries, you will typically get a more recent version than what is available in notebooks. As of August 2024, here is a comparison of recommended library versions between notebooks and Framework:

- [`@duckdb/duckdb-wasm`](https://observablehq.com/framework/lib/duckdb) from 1.24.0 to 1.28.0
- [`apache-arrow`](https://observablehq.com/framework/lib/arrow) from 4.0.1 to 17.0.0
- [`arquero`](https://observablehq.com/framework/lib/arquero) from 4.8.8 to 6.0.1
- [`dot`](https://observablehq.com/framework/lib/dot) from `viz.js` 2.0.0 to `@viz-js/viz` at 3.7.0
- [`exceljs`](https://observablehq.com/framework/lib/xlsx) from 4.3.0 to 4.4.0
- [`katex`](https://observablehq.com/framework/lib/tex) from 0.11.0 to 0.16.11
- [`leaflet`](https://observablehq.com/framework/lib/leaflet) from 1.9.3 to 1.9.4
- [`mermaid`](https://observablehq.com/framework/lib/mermaid) from 9.2.2 to 10.9.1
- [`vega`](https://observablehq.com/framework/lib/vega-lite) from 5.22.1 to 5.30.0
- [`vega-lite`](https://observablehq.com/framework/lib/vega-lite) from 5.6.0 to 5.20.1
- [`vega-lite-api`](https://observablehq.com/framework/lib/vega-lite) from 5.0.0 to 5.6.0

In Framework, the [`html`](https://observablehq.com/framework/lib/htl) and [`svg`](https://observablehq.com/framework/lib/htl) built-in template literals are implemented with [Hypertext Literal](https://observablehq.com/framework/lib/htl) which automatically escapes interpolated values. The [`dot`](https://observablehq.com/framework/lib/dot) template literal implements responsive dark mode & better styling. And Framework has several additional recommended libraries that are not available in notebooks: [`ReactDOM`](https://observablehq.com/framework/jsx), [`React`](https://observablehq.com/framework/jsx), [`duckdb`](https://observablehq.com/framework/lib/duckdb), [`echarts`](https://observablehq.com/framework/lib/echarts), [`mapboxgl`](https://observablehq.com/framework/lib/mapbox-gl), and [`vg`](https://observablehq.com/framework/lib/mosaic).

## [Sample datasets](https://observablehq.com/framework/convert\#sample-datasets)

Like recommended libraries, Framework’s built-in sample datasets ( _e.g._, `aapl` and `penguins`) are backed by npm imports that are self-hosted.

## [Cell modes](https://observablehq.com/framework/convert\#cell-modes)

The `convert` command only supports code cell modes: Markdown, JavaScript, HTML, TeX, and SQL. It does not support non-code cell modes: data table and chart. You can use the “Convert to SQL” or “Convert to JavaScript” feature to convert data table cells and chart cells to their code equivalents prior to conversion. Alternatively, you can manually replace data table cells with `Inputs.table` (see [#23](https://github.com/observablehq/framework/issues/23) for future enhancements), and chart cells with Observable Plot’s [auto mark](https://observablehq.com/plot/marks/auto).

## [Databases](https://observablehq.com/framework/convert\#databases)

Database connectors can be replaced by [data loaders](https://observablehq.com/framework/data-loaders).

## [Secrets](https://observablehq.com/framework/convert\#secrets)

We recommend using a `.env` file with [dotenv](https://github.com/motdotla/dotenv) to store your secrets (such as database passwords and API keys) in a central place outside of your checked-in code; see our [Google Analytics dashboard](https://github.com/observablehq/framework/tree/main/examples/google-analytics/) example.

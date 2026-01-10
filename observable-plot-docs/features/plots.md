---
url: "https://observablehq.com/plot/features/plots"
title: "Plots | Plot"
---

# Plots [​](https://observablehq.com/plot/features/plots\#plots)

To render a **plot** in Observable Plot, call [plot](https://observablehq.com/plot/features/plots#plot) (typically as `Plot.plot`), passing in the desired _options_. This function returns an SVG or HTML figure element.

Hello, world! [Fork](https://observablehq.com/@observablehq/plot-hello-world "Open on Observable")

js

```
Plot.plot({
  marks: [\
    Plot.frame(),\
    Plot.text(["Hello, world!"], {frameAnchor: "middle"})\
  ]
})
```

TIP

The returned plot element is detached; it must be inserted into the page to be visible. For help, see the [getting started guide](https://observablehq.com/plot/getting-started).

## Marks option [​](https://observablehq.com/plot/features/plots\#marks-option)

The **marks** option specifies an array of [marks](https://observablehq.com/plot/features/marks) to render. Above, there are two marks: a [frame](https://observablehq.com/plot/marks/frame) to draw the outline of the plot frame, and a [text](https://observablehq.com/plot/marks/text) to say hello. 👋

Each mark supplies its own tabular data. For example, the table below shows the first five rows of a daily dataset of Apple stock price (`aapl`).

| Date | Open | High | Low | Close | Volume |
| --- | --- | --- | --- | --- | --- |
| 2013-05-13 | 64.501427 | 65.414284 | 64.500000 | 64.962860 | 79237200 |
| 2013-05-14 | 64.835716 | 65.028572 | 63.164288 | 63.408573 | 111779500 |
| 2013-05-15 | 62.737144 | 63.000000 | 60.337143 | 61.264286 | 185403400 |
| 2013-05-16 | 60.462856 | 62.549999 | 59.842857 | 62.082859 | 150801000 |
| 2013-05-17 | 62.721428 | 62.869999 | 61.572857 | 61.894287 | 106976100 |

In JavaScript, we can represent tabular data as an array of objects. Each object records a daily observation, with properties _Date_, _Open_, _High_, and so on. This is known as a “row-based” format since each object corresponds to a row in the table.

js

```
aapl = [\
  {Date: new Date("2013-05-13"), Open: 64.501427, High: 65.414284, Low: 64.500000, Close: 64.962860, Volume: 79237200},\
  {Date: new Date("2013-05-14"), Open: 64.835716, High: 65.028572, Low: 63.164288, Close: 63.408573, Volume: 111779500},\
  {Date: new Date("2013-05-15"), Open: 62.737144, High: 63.000000, Low: 60.337143, Close: 61.264286, Volume: 185403400},\
  {Date: new Date("2013-05-16"), Open: 60.462856, High: 62.549999, Low: 59.842857, Close: 62.082859, Volume: 150801000},\
  {Date: new Date("2013-05-17"), Open: 62.721428, High: 62.869999, Low: 61.572857, Close: 61.894287, Volume: 106976100}\
]
```

TIP

Rather than baking data into JavaScript, use [JSON](https://en.wikipedia.org/wiki/JSON) or [CSV](https://en.wikipedia.org/wiki/Comma-separated_values) files to store data. You can use [d3.json](https://d3js.org/d3-fetch#json), [d3.csv](https://d3js.org/d3-fetch#csv), or [fetch](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API) to load a file. On Observable, you can also use a [file attachment](https://observablehq.com/@observablehq/file-attachments) or [SQL cell](https://observablehq.com/@observablehq/sql-cell).

To use data with Plot, pass the data as the first argument to the mark constructor. We can then assign columns of data such as _Date_ and _Close_ to visual properties of the mark (or “channels”) such as horizontal↔︎ position **x** and vertical↕︎ position **y**.

60708090100110120130140150160170180190↑ Close20142015201620172018 [Fork](https://observablehq.com/@observablehq/plot-first-line-chart "Open on Observable")

js

```
Plot.plot({
  marks: [\
    Plot.lineY(aapl, {x: "Date", y: "Close"})\
  ]
})
```

A plot can have multiple marks, and each mark has its own data. For example, say we had a similar table `goog` representing the daily price of Google stock for the same period. Below, the red line represents Google stock, while the blue line represents Apple stock.

01002003004005006007008009001,0001,100↑ Close20142015201620172018 [Fork](https://observablehq.com/@observablehq/plot-layered-marks "Open on Observable")

js

```
Plot.plot({
  marks: [\
    Plot.ruleY([0]),\
    Plot.lineY(goog, {x: "Date", y: "Close", stroke: "red"}),\
    Plot.lineY(aapl, {x: "Date", y: "Close", stroke: "blue"})\
  ]
})
```

TIP

When comparing the performance of different stocks, we typically want to normalize the return relative to a purchase price. See the [normalize transform](https://observablehq.com/plot/transforms/normalize) for an example.

Alternatively, the tables can be combined, say with a _Symbol_ column to distinguish AAPL from GOOG. This allows the use of a categorical _color_ scale and legend.

AAPLGOOG

01002003004005006007008009001,0001,100↑ Close20142015201620172018 [Fork](https://observablehq.com/@observablehq/plot-stocks-multiline-chart "Open on Observable")

js

```
Plot.plot({
  color: {legend: true},
  marks: [\
    Plot.ruleY([0]),\
    Plot.lineY(stocks, {x: "Date", y: "Close", stroke: "Symbol"})\
  ]
})
```

Each mark has its own options, and different mark types support different options. See the respective mark type (such as [bar](https://observablehq.com/plot/marks/bar) or [dot](https://observablehq.com/plot/marks/dot)) for details.

Marks are drawn in the given order, with the last mark drawn on top. For example, below green bars are drawn on top of black bars.

0.000.010.020.030.040.050.060.070.080.090.100.110.12↑ frequencyABCDEFGHIJKLMNOPQRSTUVWXYZletter [Fork](https://observablehq.com/@observablehq/plot-marks-z-order "Open on Observable")

js

```
Plot.plot({
  x: {padding: 0.4},
  marks: [\
    Plot.barY(alphabet, {x: "letter", y: "frequency", dx: 2, dy: 2}),\
    Plot.barY(alphabet, {x: "letter", y: "frequency", fill: "green", dx: -2, dy: -2})\
  ]
})
```

## Layout options [​](https://observablehq.com/plot/features/plots\#layout-options)

The layout options determine the overall size of the plot; all are specified as numbers in pixels:

- **marginTop** \- the top margin
- **marginRight** \- the right margin
- **marginBottom** \- the bottom margin
- **marginLeft** \- the left margin
- **margin** \- shorthand for the four margins
- **width** \- the outer width of the plot (including margins)
- **height** \- the outer height of the plot (including margins)

Experiment with the margins by adjusting the sliders below. Note that because the _x_ scale is a _band_ scale, the **round** option defaults to true, so the bars may jump when you adjust the horizontal margins to snap to crisp edges.

marginTop:20marginRight:20marginBottom:30marginLeft:40

0.000.010.020.030.040.050.060.070.080.090.100.110.12↑ frequencyABCDEFGHIJKLMNOPQRSTUVWXYZletter

js

```
Plot.plot({
  marginTop,
  marginRight,
  marginBottom,
  marginLeft,
  grid: true,
  marks: [\
    Plot.frame({\
      stroke: "var(--vp-c-text-2)",\
      strokeOpacity: 0.5,\
      insetTop: -marginTop,\
      insetRight: -marginRight,\
      insetBottom: -marginBottom,\
      insetLeft: -marginLeft,\
    }),\
    Plot.barY(alphabet, {x: "letter", y: "frequency", fill: "green"}),\
    Plot.frame()\
  ]
})
```

js

```
Plot.plot({
  marginTop: 20,
  marginRight: 20,
  marginBottom: 30,
  marginLeft: 40,
  grid: true,
  marks: [\
    Plot.barY(alphabet, {x: "letter", y: "frequency", fill: "green"}),\
    Plot.frame()\
  ]
})
```

INFO

To assist the explanation, the plot above is drawn with a light gray border.

The default **width** is 640. On Observable, the width can be set to the [standard width](https://github.com/observablehq/stdlib/blob/main/README.md#width) to make responsive plots. The default **height** is chosen automatically based on the plot’s associated scales; for example, if _y_ is linear and there is no _fy_ scale, it might be 396. The default margins depend on the maximum margins of the plot’s constituent [marks](https://observablehq.com/plot/features/plots#marks-option). While most marks default to zero margins (because they are drawn inside the chart area), Plot’s [axis mark](https://observablehq.com/plot/marks/axis) has non-zero default margins.

TIP

Plot does not adjust margins automatically to make room for long tick labels. If your _y_ axis labels are too long, you can increase the **marginLeft** to make more room. Also consider using a different **tickFormat** for short labels ( _e.g._, `s` for SI prefix notation), or a scale **transform** (say to convert units to millions or billions).

The **aspectRatio** option [Permalink to "aspectRatio"](https://observablehq.com/plot/features/plots#aspectRatio) [^0.6.4](https://github.com/observablehq/plot/releases/tag/v0.6.4 "added in v0.6.4"), if not null, computes a default **height** such that a variation of one unit in the _x_ dimension is represented by the corresponding number of pixels as a variation in the _y_ dimension of one unit. The **aspectRatio** option is recommended only when _x_ and _y_ domains share the same units, such as millimeters. When a position scale is [ordinal](https://observablehq.com/plot/features/scales#discrete-scales) ( _point_ or _band_), consecutive domain values are treated as one unit length apart; for example, if both _x_ and _y_ are ordinal, then an aspect ratio of one produces a square grid.

Use fixed aspect ratio:

AdelieChinstrapGentoo

14161820↑ culmen\_depth\_mm3540455055culmen\_length\_mm → [Fork](https://observablehq.com/@observablehq/plot-intro-to-aspectratio "Open on Observable")

js

```
Plot.plot({
  grid: true,
  inset: 10,
  aspectRatio: fixed ? 1 : undefined,
  color: {legend: true},
  marks: [\
    Plot.frame(),\
    Plot.dot(penguins, {x: "culmen_length_mm", y: "culmen_depth_mm", stroke: "species"})\
  ]
})
```

TIP

When using facets, set the _fx_ and _fy_ scales’ **round** option to false if you need an exact aspect ratio.

## Other options [​](https://observablehq.com/plot/features/plots\#other-options)

By default, [plot](https://observablehq.com/plot/features/plots#plot) returns an SVG element; however, if the plot includes a title, subtitle, [legend](https://observablehq.com/plot/features/legends), or caption, plot wraps the SVG element with an HTML figure element. You can also force Plot to generate a figure element by setting the **figure** option [^0.6.10](https://github.com/observablehq/plot/releases/tag/v0.6.10 "added in v0.6.10") to true.

The **title** & **subtitle** options [^0.6.10](https://github.com/observablehq/plot/releases/tag/v0.6.10 "added in v0.6.10") and the **caption** option accept either a string or an HTML element. If given an HTML element, say using the [`html` tagged template literal](http://github.com/observablehq/htl), the title and subtitle are used as-is while the caption is wrapped in a figcaption element; otherwise, the specified text will be escaped and wrapped in an h2, h3, or figcaption, respectively.

## For charts, an informative title

### Subtitle to follow with additional context

Titles, subtitles, captions, and annotations assist inter­-pretation by telling the reader what’s interesting. Don’t makethe reader work to find what you already know.Figure 1. A chart with a title, subtitle, and caption. [Fork](https://observablehq.com/@observablehq/plot-caption "Open on Observable")

js

```
Plot.plot({
  title: "For charts, an informative title",
  subtitle: "Subtitle to follow with additional context",
  caption: "Figure 1. A chart with a title, subtitle, and caption.",
  marks: [\
    Plot.frame(),\
    Plot.text(["Titles, subtitles, captions, and annotations assist inter­pretation by telling the reader what’s interesting. Don’t make the reader work to find what you already know."], {lineWidth: 30, frameAnchor: "middle"})\
  ]
})
```

The **style** option allows custom styles to override Plot’s defaults. It may be specified either as a string of inline styles ( _e.g._, `"color: red;"`, in the same fashion as assigning [_element_.style](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/style)) or an object of properties ( _e.g._, `{color: "red"}`, in the same fashion as assigning [_element_.style properties](https://developer.mozilla.org/en-US/docs/Web/API/CSSStyleDeclaration)). By default, the returned plot has a max-width of 100%, and the system-ui font. Plot’s marks and axes default to [currentColor](https://developer.mozilla.org/en-US/docs/Web/CSS/color_value#currentcolor_keyword), meaning that they will inherit the surrounding content’s color.

CAUTION

Unitless numbers ( [quirky lengths](https://www.w3.org/TR/css-values-4/#deprecated-quirky-length)) such as `{padding: 20}` are not supported by some browsers; you should instead specify a string with units such as `{padding: "20px"}`.

The generated SVG element has a class name which applies a default stylesheet. Use the top-level **className** option to specify that class name.

The **clip** option [^0.6.10](https://github.com/observablehq/plot/releases/tag/v0.6.10 "added in v0.6.10") determines the default clipping behavior if the [mark **clip** option](https://observablehq.com/plot/features/marks#mark-options) is not specified; set it to true to enable clipping. This option does not affect [axis](https://observablehq.com/plot/marks/axis), [grid](https://observablehq.com/plot/marks/grid), and [frame](https://observablehq.com/plot/marks/frame) marks, whose **clip** option defaults to false.

The **document** option specifies the [document](https://developer.mozilla.org/en-US/docs/Web/API/Document) used to create plot elements. It defaults to window.document, but can be changed to another document, say when using a virtual DOM implementation for server-side rendering in Node.

## plot( _options_) [​](https://observablehq.com/plot/features/plots\#plot)

js

```
Plot.plot({
  height: 200,
  marks: [\
    Plot.barY(alphabet, {x: "letter", y: "frequency"})\
  ]
})
```

Renders a new plot with the specified _options_, returning a SVG or HTML figure element. This element can then be inserted into the page as described in the [getting started guide](https://observablehq.com/plot/getting-started).

## _mark_.plot( _options_) [​](https://observablehq.com/plot/features/plots\#mark_plot)

js

```
Plot.barY(alphabet, {x: "letter", y: "frequency"}).plot({height: 200})
```

Given a [_mark_](https://observablehq.com/plot/features/marks), this is a convenience shorthand for calling [plot](https://observablehq.com/plot/features/plots#plot) where the **marks** option includes this _mark_. Any additional **marks** in _options_ are drawn on top of this _mark_.

## _plot_.scale( _name_) [​](https://observablehq.com/plot/features/plots\#plot_scale)

js

```
const plot = Plot.plot(options); // render a plot
const color = plot.scale("color"); // get the color scale
console.log(color.range); // inspect the scale’s range
```

Returns the [scale object](https://observablehq.com/plot/features/scales#scale-options) for the scale with the specified _name_ (such as _x_ or _color_) on the given _plot_, where _plot_ is a rendered plot element returned by [plot](https://observablehq.com/plot/features/plots#plot). If the associated _plot_ has no scale with the given _name_, returns undefined.

## _plot_.legend( _name_, _options_) [​](https://observablehq.com/plot/features/plots\#plot_legend)

js

```
const plot = Plot.plot(options); // render a plot
const legend = plot.legend("color"); // render a color legend
```

Renders a standalone legend for the scale with the specified _name_ (such as _x_ or _color_) on the given _plot_, where _plot_ is a rendered plot element returned by [plot](https://observablehq.com/plot/features/plots#plot), returning a SVG or HTML figure element. This element can then be inserted into the page as described in the [getting started guide](https://observablehq.com/plot/getting-started). If the associated _plot_ has no scale with the given _name_, returns undefined. Legends are currently only supported for _color_, _opacity_, and _symbol_ scales.

Pager

[Previous pageGetting started](https://observablehq.com/plot/getting-started)

[Next pageMarks](https://observablehq.com/plot/features/marks)

[Home](https://observablehq.com/ "Home")

Resources

- [Forum](https://talk.observablehq.com/)
- [Slack](https://observablehq.com/slack/join)
- [Releases](https://github.com/observablehq/plot/releases)

Observable

- [Product](https://observablehq.com/product)
- [Plot](https://observablehq.com/plot)
- [Integrations](https://observablehq.com/data-integrations)
- [Pricing](https://observablehq.com/pricing)

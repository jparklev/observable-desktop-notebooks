---
url: "https://observablehq.com/plot/marks/axis"
title: "Axis mark | Plot"
---

# Axis mark [^0.6.3](https://github.com/observablehq/plot/releases/tag/v0.6.3 "added in v0.6.3") [​](https://observablehq.com/plot/marks/axis\#axis-mark)

The **axis mark** conveys the meaning of a position [scale](https://observablehq.com/plot/features/scales): _x_ or _y_, and _fx_ or _fy_ when [faceting](https://observablehq.com/plot/features/facets). Plot automatically adds default axis marks as needed, but you can customize the appearance of axes either through scale options or by explicitly declaring an axis mark.

For example, the **axis** scale option specifies the side of the frame to draw the axis. Setting it to _both_ will repeat the axis on both sides.

ABCDEFGHIJKLMNOPQRSTUVWXYZletter024681012frequency (%) →024681012 [Fork](https://observablehq.com/@observablehq/plot-axis-both "Open on Observable")

js

```
Plot.plot({
  x: {percent: true, grid: true, axis: "both"},
  marks: [\
    Plot.barX(alphabet, {x: "frequency", y: "letter"}),\
    Plot.ruleX([0])\
  ]
})
```

The above is equivalent to declaring two explicit axis marks, one with the _top_ **anchor** and the other with the _bottom_ **anchor**, and one explicit [grid mark](https://observablehq.com/plot/marks/grid). A benefit of declaring explicit axes is that you can draw them atop other marks.

ABCDEFGHIJKLMNOPQRSTUVWXYZletter024681012frequency (%) →024681012 [Fork](https://observablehq.com/@observablehq/plot-axis-both "Open on Observable")

js

```
Plot.plot({
  x: {percent: true},
  marks: [\
    Plot.axisX({anchor: "top"}),\
    Plot.axisX({anchor: "bottom", label: null}),\
    Plot.barX(alphabet, {x: "frequency", y: "letter"}),\
    Plot.gridX({interval: 1, stroke: "white", strokeOpacity: 0.5}),\
    Plot.ruleX([0])\
  ]
})
```

INFO

The **interval** option above instructs the grid lines to be drawn at unit intervals, _i.e._ whole percentages. As an alternative, you can use the **ticks** option to specify the desired number of ticks or the **tickSpacing** option to specify the desired separation between adjacent ticks in pixels.

If you don’t declare an axis mark for a position scale, Plot will implicitly add one for you below (before) all other marks. To disable an implicit axis, set the _scale_. **axis** option to null for the corresponding scale; or, set the top-level **axis** option to null to disable all implicit axes.

Plot’s axis mark is a composite mark comprised of:

- a [vector](https://observablehq.com/plot/marks/vector) for ticks
- a [text](https://observablehq.com/plot/marks/text) for tick labels
- a [text](https://observablehq.com/plot/marks/text) for an axis label

As such, you can take advantage of the full capabilities of these marks. For example, you can use the text mark’s **lineWidth** option to wrap long tick labels (and even soft hyphens). Note this option is expressed in ems, not pixels, and you may have to reserve additional **marginBottom** to make room for multiple lines.

Committed 671birthdays tomemoryDiscovered howto “like” thingsmentallyEx is doing toowellFamily in feudwith Zucker­-bergsHigh schoolfriends all deadnowNot enoughpolitics02468101214161820222426↑ Responses (%) [Fork](https://observablehq.com/@observablehq/plot-wrap-tick-labels "Open on Observable")

js

```
Plot.plot({
  y: {percent: true},
  marks: [\
    Plot.axisX({label: null, lineWidth: 8, marginBottom: 40}),\
    Plot.axisY({label: "Responses (%)"}),\
    Plot.barY(responses, {x: "name", y: "value"}),\
    Plot.ruleY([0])\
  ]
})
```

Or, you can use the **textAnchor** option to extend the _y_-axis tick labels to the right and into the frame, and the **fill** option to specify the color of the text.

010203040Yield (kg) →🍌 banana🍎 apple🍐 pear [Fork](https://observablehq.com/@observablehq/plot-anchor-tick-labels "Open on Observable")

js

```
Plot.plot({
  marginTop: 0,
  marginLeft: 4,
  x: {ticks: 4, label: "Yield (kg)"},
  marks: [\
    Plot.barX([42, 17, 32], {y: ["🍌 banana", "🍎 apple", "🍐 pear"]}),\
    Plot.axisY({textAnchor: "start", fill: "white", dx: 14})\
  ]
})
```

Layering several marks makes it possible to create [ggplot2-style axes](https://ggplot2.tidyverse.org/reference/guide_axis.html) with a filled [frame](https://observablehq.com/plot/marks/frame) and white grid lines.

6080100120140160180↑ Close20142015201620172018 [Fork](https://observablehq.com/@observablehq/plot-ggplot2-style-axes "Open on Observable")

js

```
Plot.plot({
  inset: 10,
  marks: [\
    Plot.frame({fill: "#eaeaea"}),\
    Plot.gridY({stroke: "white", strokeOpacity: 1}),\
    Plot.gridX({stroke: "white", strokeOpacity: 1}),\
    Plot.line(aapl, {x: "Date", y: "Close", stroke: "black"})\
  ]
})
```

Or you could emulate the style of _The New York Times_, with tick labels above dashed grid lines, and a custom tick format to show units (here dollars) on the first tick.

20142015201620172018020406080100120140160$180↑ Close [Fork](https://observablehq.com/@observablehq/plot-nyt-style-axes "Open on Observable")

js

```
Plot.plot({
  round: true,
  marginLeft: 0, // don’t need left-margin since labels are inset
  x: {label: null, insetLeft: 36}, // reserve space for inset labels
  marks: [\
    Plot.gridY({\
      strokeDasharray: "0.75,2", // dashed\
      strokeOpacity: 1 // opaque\
    }),\
    Plot.axisY({\
      tickSize: 0, // don’t draw ticks\
      dx: 38, // offset right\
      dy: -6, // offset up\
      lineAnchor: "bottom", // draw labels above grid lines\
      tickFormat: (d, i, _) => (i === _.length - 1 ? `$${d}` : d)\
    }),\
    Plot.ruleY([0]),\
    Plot.line(aapl, {x: "Date", y: "Close", markerEnd: "dot"})\
  ]
})
```

Time axes default to a consistent multi-line tick format [^0.6.9](https://github.com/observablehq/plot/releases/tag/v0.6.9 "added in v0.6.9"), [à la Datawrapper](https://blog.datawrapper.de/new-axis-ticks/), for example showing the first month of each quarter, and the year:

020406080100120140160180↑ CloseJul2013OctJan2014AprJulOctJan2015AprJulOctJan2016AprJulOctJan2017AprJulOctJan2018Apr [Fork](https://observablehq.com/@observablehq/plot-datawrapper-style-date-axis "Open on Observable")

js

```
Plot.plot({
  marks: [\
    Plot.ruleY([0]),\
    Plot.axisX({ticks: "3 months"}),\
    Plot.gridX(),\
    Plot.line(aapl, {x: "Date", y: "Close"})\
  ]
})
```

The format is inferred from the tick interval, and consists of two fields ( _e.g._, month and year, day and month, minutes and hours); when a tick has the same second field value as the previous tick ( _e.g._, “19 Jan” after “17 Jan”), only the first field (“19”) is shown for brevity. Alternatively, you can specify multiple explicit axes with options for hierarchical time intervals, here showing weeks, months, and years.

120125130135140145150155160165170175180↑ Close 2017 2018 Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec Jan Feb Mar Apr [Fork](https://observablehq.com/@observablehq/plot-multiscale-date-axis "Open on Observable")

js

```
Plot.plot({
  x: {round: true, nice: d3.utcWeek},
  y: {inset: 6},
  marks: [\
    Plot.frame({fill: "currentColor", fillOpacity: 0.1}),\
    Plot.frame({anchor: "bottom"}),\
    Plot.axisX({ticks: "year", tickSize: 28, tickPadding: -11, tickFormat: "  %Y", textAnchor: "start"}),\
    Plot.axisX({ticks: "month", tickSize: 16, tickPadding: -11, tickFormat: "  %b", textAnchor: "start"}),\
    Plot.gridX({ticks: "week", stroke: "white", strokeOpacity: 1, insetBottom: -0.5}),\
    Plot.line(aapl.slice(-340, -10), {x: "Date", y: "Close", curve: "step"})\
  ]
})
```

You can even style an axis dynamically based on data! The data associated with an axis or grid mark are the tick values sampled from the associated scale’s domain. If you don’t specify the data explicitly, the ticks will be chosen through a combination of the **ticks**, **tickSpacing**, and **interval** options.

20142015201620172018020406080100120140160180↑ Close [Fork](https://observablehq.com/@observablehq/plot-data-based-axis "Open on Observable")

js

```
Plot.plot({
  marginRight: 0,
  marks: [\
    Plot.ruleY([0]),\
    Plot.line(aapl, {x: "Date", y: "Close"}),\
    Plot.gridY({x: (y) => aapl.find((d) => d.Close >= y)?.Date, insetLeft: -6}),\
    Plot.axisY({x: (y) => aapl.find((d) => d.Close >= y)?.Date, insetLeft: -6, textStroke: "white"})\
  ]
})
```

The color of an axis can be controlled with the **color**, **stroke**, and **fill** options, which affect the axis’ component marks differently. The **stroke** option affects the tick vector; the **fill** option affects the label texts. The **color** option is shorthand for setting both **fill** and **stroke**. While these options are typically set to constant colors (such as _red_ or the default _currentColor_), they can be specified as channels to assign colors dynamically based on the associated tick value.

0.00.10.20.30.40.50.60.70.80.91.0 [Fork](https://observablehq.com/@observablehq/plot-axes-with-color "Open on Observable")

js

```
Plot.axisX(d3.ticks(0, 1, 10), {color: "red"}).plot() // text fill and tick stroke
```

0.00.10.20.30.40.50.60.70.80.91.0 [Fork](https://observablehq.com/@observablehq/plot-axes-with-color "Open on Observable")

js

```
Plot.axisX(d3.ticks(0, 1, 10), {stroke: Plot.identity, strokeWidth: 3, tickSize: 10}).plot() // tick stroke
```

0.00.10.20.30.40.50.60.70.80.91.0 [Fork](https://observablehq.com/@observablehq/plot-axes-with-color "Open on Observable")

js

```
Plot.axisX(d3.ticks(0, 1, 10), {fill: "red"}).plot() // text fill
```

To draw an outline around the tick labels, say to improve legibility when drawing an axes atop other marks, use the **textStroke** (default _none_), **textStrokeWidth** (default 3), and **textStrokeOpacity** (default 1) options.

0102030405060708090100 [Fork](https://observablehq.com/@observablehq/plot-axes-with-color "Open on Observable")

js

```
Plot.plot({
  height: 40,
  style: "background: #777;",
  x: {domain: [0, 100]},
  marks: [\
    Plot.axisX({\
      fill: "black",\
      stroke: "white",\
      textStroke: "white",\
      textStrokeWidth: 3,\
      textStrokeOpacity: 0.6\
    })\
  ]
})
```

When faceting, the _x_\- and _y_-axes are typically repeated across facets. A _bottom_-anchored _x_-axis is by default drawn on any facet _with empty space below it_; conversely, a _top_-anchored _x_-axis is drawn on any facet _with empty space above it_. Similarly, a _left_-anchored _y_-axis is drawn on facets with empty space to the left, and a _right_-anchored _y_-axis is drawn on facets with empty space to the right.

If the default behavior isn’t what you want, use the _mark_. **facetAnchor** option to control which facets show an axis. (This option applies not just to Plot’s axis and grid mark, but any mark; for example, you can use it to place a text mark at the bottom of each facet column.) The supported values for this option are:

- _top_ \- show only on the top facets
- _right_ \- show only on the right facets
- _bottom_ \- show only on the bottom facets
- _left_ \- show only on the left facets
- _top-empty_ \- show on any facet with space above (a superset of _top_)
- _right-empty_ \- show on any facet with space to the right (a superset of _right_)
- _bottom-empty_ \- show on any facet with space to below (a superset of _below_)
- _left-empty_ \- show on any facet with space to the left (a superset of _left_)
- null - show on every facet

The interactive chart below shows the different possibilities. Note that we place the facet _fx_-axis (in blue) opposite the _x_-axis (in red).

anchor: bottomtop facetAnchor: autobottom-emptybottomtop-emptytopnull

AdelieChinstrapGentoospecies141618201416182014161820↑ culmen\_depth\_mm4050405040504050culmen\_length\_mm →FEMALEMALEsex [Fork](https://observablehq.com/@observablehq/plot-facetanchor "Open on Observable")

js

```
Plot.plot({
  facet: {marginRight: 80},
  grid: true,
  marks: [\
    Plot.frame(),\
    Plot.dot(penguins, {x: "culmen_length_mm", y: "culmen_depth_mm", fx: "sex", fy: "species"}),\
    Plot.axisX({color: "red", anchor, facetAnchor: facetAnchor === "auto" ? undefined : facetAnchor === "null" ? null : facetAnchor}),\
    Plot.axisFx({color: "blue", anchor: anchor === "top" ? "bottom" : "top"}) // place fx axis opposite x\
  ]
})
```

The **labelAnchor** option controls the position of the axis label. For the _x_ or _fx_ axis, the label anchor may be _left_, _center_, or _right_. It defaults to _center_ for ordinal scales and _right_ for quantitative scales.

0.00.10.20.30.40.50.60.70.80.91.0top-left →top-center →top-right →0.00.10.20.30.40.50.60.70.80.91.0bottom-left →bottom-center →bottom-right → [Fork](https://observablehq.com/@observablehq/plot-labelanchor "Open on Observable")

js

```
Plot.plot({
  height: 80,
  grid: true,
  x: {type: "linear"},
  marks: [\
    Plot.axisX({anchor: "top", label: "top-left", labelAnchor: "left"}),\
    Plot.axisX({anchor: "top", label: "top-center", labelAnchor: "center", ticks: []}),\
    Plot.axisX({anchor: "top", label: "top-right", labelAnchor: "right", ticks: []}),\
    Plot.axisX({anchor: "bottom", label: "bottom-left", labelAnchor: "left"}),\
    Plot.axisX({anchor: "bottom", label: "bottom-center", labelAnchor: "center", ticks: []}),\
    Plot.axisX({anchor: "bottom", label: "bottom-right", labelAnchor: "right", ticks: []})\
  ]
})
```

For the _y_ and _fy_ axis, the label anchor may be _top_, _center_, or _bottom_. It defaults to _center_ for ordinal scales and _top_ for quantitative scales. When the label anchor is _center_, the label is rotated by 90° to fit, though you may need to adjust the margins to avoid overlap between the tick labels and the axis label.

0.00.10.20.30.40.50.60.70.80.91.0↑ left-topleft-center →↑ left-bottom0.00.10.20.30.40.50.60.70.80.91.0right-top ↑right-center →right-bottom ↑ [Fork](https://observablehq.com/@observablehq/plot-labelanchor "Open on Observable")

js

```
Plot.plot({
  grid: true,
  y: {type: "linear"},
  marks: [\
    Plot.axisY({anchor: "left", label: "left-top", labelAnchor: "top"}),\
    Plot.axisY({anchor: "left", label: "left-center", labelAnchor: "center", ticks: []}),\
    Plot.axisY({anchor: "left", label: "left-bottom", labelAnchor: "bottom", ticks: []}),\
    Plot.axisY({anchor: "right", label: "right-top", labelAnchor: "top"}),\
    Plot.axisY({anchor: "right", label: "right-center", labelAnchor: "center", ticks: []}),\
    Plot.axisY({anchor: "right", label: "right-bottom", labelAnchor: "bottom", ticks: []})\
  ]
})
```

## Axis options [​](https://observablehq.com/plot/marks/axis\#axis-options)

By default, the _data_ for an axis mark are tick values sampled from the associated scale’s domain. If desired, you can specify the _data_ explicitly ( _e.g._ as an array of numbers), or use one of the following options:

- **ticks** \- the approximate number of ticks to generate, or interval, or array of values
- **tickSpacing** \- the approximate number of pixels between ticks (if **ticks** is not specified)
- **interval** \- an interval or time interval

Note that when an axis mark is declared explicitly (via the [**marks** plot option](https://observablehq.com/plot/features/plots#marks-option), as opposed to an implicit axis), the corresponding scale’s _scale_.ticks and _scale_.tickSpacing options are not automatically inherited by the axis mark; however, the _scale_.interval option _is_ inherited, as is the _scale_.label option. You can declare multiple axis marks for the same scale with different ticks, and styles, as desired.

In addition to the [standard mark options](https://observablehq.com/plot/features/marks), the axis mark supports the following options:

- **anchor** \- the axis orientation: _top_ or _bottom_ for _x_ or _fx_; _left_ or _right_ for _y_ or _fy_
- **tickSize** \- the length of the tick vector (in pixels; default 6 for _x_ or _y_, or 0 for _fx_ or _fy_)
- **tickPadding** \- the separation between the tick vector and its label (in pixels; default 3)
- **tickFormat** \- either a function or specifier string to format tick values; see [Formats](https://observablehq.com/plot/features/formats)
- **tickRotate** \- whether to rotate tick labels (an angle in degrees clockwise; default 0)
- **fontVariant** \- the ticks’ font-variant; defaults to _tabular-nums_ for quantitative axes
- **label** \- a string to label the axis; defaults to the scale’s label, perhaps with an arrow
- **labelAnchor** \- the label anchor: _top_, _right_, _bottom_, _left_, or _center_
- **labelArrow** \- the label arrow: _auto_ (default), _up_, _right_, _down_, _left_, _none_, or true [^0.6.7](https://github.com/observablehq/plot/releases/tag/v0.6.7 "added in v0.6.7")
- **labelOffset** \- the label position offset (in pixels; default depends on margins and orientation)
- **color** \- the color of the ticks and labels (defaults to _currentColor_)
- **textStroke** \- the color of the stroke around tick labels (defaults to _none_)
- **textStrokeOpacity** \- the opacity of the stroke around tick labels
- **textStrokeWidth** \- the thickness of the stroke around tick labels (in pixels)

The **labelArrow** option controls the arrow (↑, →, ↓, or ←) added to the axis label indicating the direction of ascending value; for example, horizontal position _x_ typically increases in value going right→, while vertical position _y_ typically increases in value going up↑. If _auto_ (the default), the arrow will be added only if the scale is quantitative or temporal; if true, the arrow will also apply to ordinal scales, provided the domain is consistently ordered.

As a composite mark, the **stroke** option affects the color of the tick vector, while the **fill** option affects the color the text labels; both default to the **color** option, which defaults to _currentColor_. The **x** and **y** channels, if specified, position the ticks; if not specified, the tick positions depend on the axis **anchor**. The orientation of the tick labels likewise depends on the **anchor**. See the [text mark](https://observablehq.com/plot/marks/text) for details on available options for the tick and axis labels.

The axis mark’s [**facetAnchor**](https://observablehq.com/plot/features/facets) option defaults to _top-empty_ if anchor is _top_, _right-empty_ if anchor is _right_, _bottom-empty_ if anchor is _bottom_, and _left-empty_ if anchor is _left_. This ensures the proper positioning of the axes with respect to empty facets.

The axis mark’s default margins depend on its orientation ( **anchor**) as follows, in order of **marginTop**, **marginRight**, **marginBottom**, and **marginLeft**, in pixels:

- _top_ \- 30, 20, 0, 20
- _right_ \- 20, 40, 20, 0
- _bottom_ \- 0, 20, 30, 20
- _left_ \- 20, 0, 20, 40

For simplicity’s sake and for consistent layout across plots, axis margins are not automatically sized to make room for tick labels; instead, shorten your tick labels (for example using the _k_ SI-prefix tick format, or setting a _scale_.transform to show thousands or millions, or setting the **textOverflow** option to _ellipsis_ and the **lineWidth** option to clip long labels) or increase the margins as needed.

## axisX( _data_, _options_) [​](https://observablehq.com/plot/marks/axis\#axisX)

js

```
Plot.axisX({anchor: "bottom", tickSpacing: 80})
```

Returns a new _x_ axis with the given _options_.

## axisY( _data_, _options_) [​](https://observablehq.com/plot/marks/axis\#axisY)

js

```
Plot.axisY({anchor: "left", tickSpacing: 35})
```

Returns a new _y_ axis with the given _options_.

## axisFx( _data_, _options_) [​](https://observablehq.com/plot/marks/axis\#axisFx)

js

```
Plot.axisFx({anchor: "top", label: null})
```

Returns a new _fx_ axis with the given _options_.

## axisFy( _data_, _options_) [​](https://observablehq.com/plot/marks/axis\#axisFy)

js

```
Plot.axisFy({anchor: "right", label: null})
```

Returns a new _fy_ axis with the given _options_.

Pager

[Previous pageAuto](https://observablehq.com/plot/marks/auto)

[Next pageBar](https://observablehq.com/plot/marks/bar)

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

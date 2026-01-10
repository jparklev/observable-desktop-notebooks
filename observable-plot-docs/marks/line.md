---
url: "https://observablehq.com/plot/marks/line"
title: "Line mark | Plot"
---

# Line mark [​](https://observablehq.com/plot/marks/line\#line-mark)

The **line mark** draws two-dimensional lines as in a line chart. Because the line mark interpolates between adjacent data points, typically both the _x_ and _y_ scales are quantitative or temporal. For example, below is a line chart of the closing price of Apple stock.

60708090100110120130140150160170180190↑ Close20142015201620172018 [Fork](https://observablehq.com/@observablehq/plot-simple-line-chart "Open on Observable")

js

```
Plot.line(aapl, {x: "Date", y: "Close"}).plot({y: {grid: true}})
```

If the **x** and **y** options are not defined, the line mark assumes that the data is an iterable of points \[\[ _x₁_, _y₁_\], \[ _x₂_, _y₂_\], …\], allowing for [shorthand](https://observablehq.com/plot/features/shorthand).

6070809010011012013014015016017018019020142015201620172018 [Fork](https://observablehq.com/@observablehq/plot-shorthand-line-chart "Open on Observable")

js

```
Plot.line(aapl.map((d) => [d.Date, d.Close])).plot()
```

TIP

This shorthand loses the automatic _x_\- and _y_-axis labels, reducing legibility. Use the **label** [scale option](https://observablehq.com/plot/features/scales) to restore them.

The [lineY constructor](https://observablehq.com/plot/marks/line#lineY) provides default channel definitions of **x** = index and **y** = [identity](https://observablehq.com/plot/features/transforms#identity), letting you pass an array of numbers as data. The [lineX constructor](https://observablehq.com/plot/marks/line#lineX) similarly provides **x** = identity and **y** = index defaults for lines that go up↑ instead of to the right→. Below, a random walk is made using [d3.cumsum](https://observablehq.com/@d3/d3-cumsum?collection=@d3/d3-array) and [d3.randomNormal](https://observablehq.com/@d3/d3-random?collection=@d3/d3-random).

−8−6−4−2024681012141618200100200300400500 [Fork](https://observablehq.com/@observablehq/plot-shorthand-liney "Open on Observable")

js

```
Plot.lineY(d3.cumsum({length: 600}, d3.randomNormal())).plot()
```

As with [areas](https://observablehq.com/plot/marks/area), points in lines are connected in input order: the first point is connected to the second point, the second is connected to the third, and so on. Line data is typically in chronological order. Unsorted data may produce gibberish.

60708090100110120130140150160170180190↑ Close20142015201620172018 [Fork](https://observablehq.com/@observablehq/plot-line-sort "Open on Observable")

js

```
Plot.lineY(d3.shuffle(aapl.slice()), {x: "Date", y: "Close"}).plot() // 🌶️
```

If your data isn’t sorted, use the [sort transform](https://observablehq.com/plot/transforms/sort).

60708090100110120130140150160170180190↑ Close20142015201620172018 [Fork](https://observablehq.com/@observablehq/plot-line-sort "Open on Observable")

js

```
Plot.lineY(d3.shuffle(aapl.slice()), {x: "Date", y: "Close", sort: "Date"}).plot()
```

While the _x_ scale of a line chart often represents time, this is not required. For example, we can plot the elevation profile of a Tour de France stage — and imagine how tiring it must be to start a climb after riding 160km! ⛰🚴💦

01002003004005006007008009001,0001,1001,200↑ Elevation (m)020406080100120140160180Distance from stage start (km) → [Fork](https://observablehq.com/@observablehq/plot-tour-de-france-elevation-profile "Open on Observable")

js

```
Plot.plot({
  x: {
    label: "Distance from stage start (km)"
  },
  y: {
    label: "Elevation (m)",
    grid: true
  },
  marks: [\
    Plot.ruleY([0]),\
    Plot.line(tdf, {x: "distance", y: "elevation"})\
  ]
})
```

There is no requirement that **y** be dependent on **x**; lines can be used in connected scatterplots to show two independent (but often correlated) variables. (See also [phase plots](https://en.wikipedia.org/wiki/Phase_portrait).) The chart below recreates Hannah Fairfield’s [“Driving Shifts Into Reverse”](http://www.nytimes.com/imagepages/2010/05/02/business/02metrics.html) from 2009.

1.41.61.82.02.22.42.62.83.03.2↑ Cost of gasoline ($ per gallon)4,0005,0006,0007,0008,0009,00010,000Miles driven (per person-year) →19601965197019751980198519901995200020052010 [Fork](https://observablehq.com/@observablehq/plot-connected-scatterplot "Open on Observable")

js

```
Plot.plot({
  inset: 10,
  grid: true,
  x: {label: "Miles driven (per person-year)"},
  y: {label: "Cost of gasoline ($ per gallon)"},
  marks: [\
    Plot.line(driving, {x: "miles", y: "gas", curve: "catmull-rom", marker: true}),\
    Plot.text(driving, {filter: (d) => d.year % 5 === 0, x: "miles", y: "gas", text: (d) => `${d.year}`, dy: -8})\
  ]
})
```

To draw multiple lines, use the **z** channel to group [tidy data](https://r4ds.had.co.nz/tidy-data.html) into series. For example, the chart below shows unemployment rates of various metro areas from the Bureau of Labor Statistics; the **z** value is the metro division name.

0246810121416↑ Unemployment (%)2000200220042006200820102012 [Fork](https://observablehq.com/@observablehq/plot-multiple-line-chart "Open on Observable")

js

```
Plot.plot({
  y: {
    grid: true,
    label: "Unemployment (%)"
  },
  marks: [\
    Plot.ruleY([0]),\
    Plot.line(bls, {x: "date", y: "unemployment", z: "division"})\
  ]
})
```

TIP

If your data is not tidy, you can use [_array_.flatMap](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/flatMap) to pivot.

If a **stroke** (or **fill**) channel is specified, the **z** option defaults to the same, automatically grouping series. For this reason, both **stroke** and **z** are typically ordinal or categorical.

−40−30−20−10+0+100+200+300+400+500↑ Change in price (%)20142015201620172018AAPLAMZNGOOGIBM [Fork](https://observablehq.com/@observablehq/plot-index-chart "Open on Observable")

js

```
Plot.plot({
  y: {
    type: "log",
    grid: true,
    label: "Change in price (%)",
    tickFormat: ((f) => (x) => f((x - 1) * 100))(d3.format("+d"))
  },
  marks: [\
    Plot.ruleY([1]),\
    Plot.line(stocks, Plot.normalizeY({\
      x: "Date",\
      y: "Close",\
      stroke: "Symbol"\
    })),\
    Plot.text(stocks, Plot.selectLast(Plot.normalizeY({\
      x: "Date",\
      y: "Close",\
      z: "Symbol",\
      text: "Symbol",\
      textAnchor: "start",\
      dx: 3\
    })))\
  ]
})
```

INFO

Here the [normalize transform](https://observablehq.com/plot/transforms/normalize) normalizes each time series ( **z**) relative to its initial value, while the [select transform](https://observablehq.com/plot/transforms/select) extracts the last point for labeling. A custom tick format converts multiples to percentage change ( _e.g._, 1.6× = +60%).

Varying-color lines are supported. If the **stroke** value varies within series, the line will be segmented by color. (The same behavior applies to other channels, such as **strokeWidth** and **title**.) Specifying the **z** channel (say to null for a single series) is recommended.

0246810121416↑ Unemployment (%)2000200220042006200820102012 [Fork](https://observablehq.com/@observablehq/plot-varying-stroke-line "Open on Observable")

js

```
Plot.plot({
  x: {
    label: null
  },
  y: {
    grid: true,
    label: "Unemployment (%)"
  },
  marks: [\
    Plot.ruleY([0]),\
    Plot.line(bls, {\
      x: "date",\
      y: "unemployment",\
      z: "division",\
      stroke: "unemployment"\
    })\
  ]
})
```

Color encodings can also be used to highlight specific series, such as here to emphasize high unemployment in Michigan.

0246810121416↑ Unemployment (%)2000200220042006200820102012 [Fork](https://observablehq.com/@observablehq/plot-multiple-line-highlight "Open on Observable")

js

```
Plot.plot({
  y: {
    grid: true,
    label: "Unemployment (%)"
  },
  color: {
    domain: [false, true],
    range: ["#ccc", "red"]
  },
  marks: [\
    Plot.ruleY([0]),\
    Plot.line(bls, {\
      x: "date",\
      y: "unemployment",\
      z: "division",\
      stroke: (d) => /, MI /.test(d.division),\
      sort: {channel: "stroke"}\
    })\
  ]
})
```

When using **z**, lines are drawn in input order. The [sort transform](https://observablehq.com/plot/transforms/sort) above places the red lines on top of the gray ones to improve readability.

As an alternative to **z**, you can render multiple lines using multiple marks. While more verbose, this allows you to choose different options for each line. For example, below we plot the a 14-day moving average of the daily highs and lows in temperate San Francisco using the [window transform](https://observablehq.com/plot/transforms/window).

35404550556065↑ Temperature (°F)Oct2010Jan2011AprJulOctJan2012AprJulOct [Fork](https://observablehq.com/@observablehq/plot-moving-average-line "Open on Observable")

js

```
Plot.plot({
  y: {
    grid: true,
    label: "Temperature (°F)"
  },
  marks: [\
    Plot.line(sftemp, Plot.windowY(14, {x: "date", y: "low", stroke: "#4e79a7"})),\
    Plot.line(sftemp, Plot.windowY(14, {x: "date", y: "high", stroke: "#e15759"})),\
    Plot.ruleY([32]) // freezing\
  ]
})
```

If some channel values are undefined (or null or NaN), gaps will appear between adjacent points. To demonstrate, below we set the **y** value to NaN for the first three months of each year.

6070809010011012013014015016017018019020142015201620172018 [Fork](https://observablehq.com/@observablehq/plot-line-chart-with-gaps "Open on Observable")

js

```
Plot.plot({
  y: {
    grid: true
  },
  marks: [\
    Plot.lineY(aapl, {x: "Date", y: (d) => d.Date.getUTCMonth() < 3 ? NaN : d.Close})\
  ]
})
```

Supplying undefined values is not the same as filtering the data: the latter will interpolate between the data points. Observe the conspicuous straight lines below!

60708090100110120130140150160170180190↑ Close20142015201620172018 [Fork](https://observablehq.com/@observablehq/plot-line-chart-with-gaps "Open on Observable")

js

```
Plot.plot({
  y: {
    grid: true
  },
  marks: [\
    Plot.lineY(aapl, {filter: (d) => d.Date.getUTCMonth() >= 3, x: "Date", y: "Close", strokeOpacity: 0.3}),\
    Plot.lineY(aapl, {x: "Date", y: (d) => d.Date.getUTCMonth() < 3 ? NaN : d.Close})\
  ]
})
```

While uncommon, you can draw a line with ordinal position values. For example below, each line represents a U.S. state; **x** represents an (ordinal) age group while **y** represents the proportion of the state’s population in that age group. This chart emphasizes the overall age distribution of the United States, while giving a hint to variation across states.

02468101214161820↑ Population (%)<1010-1920-2930-3940-4950-5960-6970-79≥80Age range (years) → [Fork](https://observablehq.com/@observablehq/plot-ordinal-line "Open on Observable")

js

```
Plot.plot({
  x: {
    domain: stateage.ages, // in age order
    label: "Age range (years)",
    labelAnchor: "right",
    labelArrow: true
  },
  y: {
    label: "Population (%)",
    percent: true,
    grid: true
  },
  marks: [\
    Plot.ruleY([0]),\
    Plot.line(stateage, Plot.normalizeY("sum", {x: "age", y: "population", z: "state", strokeWidth: 1}))\
  ]
})
```

With a [spherical projection](https://observablehq.com/plot/features/projections), line segments become [geodesics](https://en.wikipedia.org/wiki/Great-circle_distance), taking the shortest path between two points on the sphere and wrapping around the antimeridian at 180° longitude. The line below shows Charles Darwin’s voyage on HMS _Beagle_. (Data via [Benjamin Schmidt](https://observablehq.com/@bmschmidt/data-driven-projections-darwins-world).)

[Fork](https://observablehq.com/@observablehq/plot-spherical-line "Open on Observable")

js

```
Plot.plot({
  projection: "equirectangular",
  marks: [\
    Plot.geo(land), // MultiPolygon\
    Plot.line(beagle, {stroke: "red"}), // [[lon, lat], …]\
    Plot.geo({type: "Point", coordinates: [-0.13, 51.5]}, {fill: "red"}) // London\
  ]
})
```

TIP

Disable spherical interpolation by setting the **curve** option to _linear_ instead of the default _auto_.

A projected line can use varying color, too. Below, color reveals the westward direction of the Beagle’s journey around the world, starting and ending in London.

[Fork](https://observablehq.com/@observablehq/plot-spherical-line-with-a-varying-stroke "Open on Observable")

js

```
Plot.plot({
  projection: "equirectangular",
  marks: [\
    Plot.geo(land),\
    Plot.line(beagle, {stroke: (d, i) => i, z: null})\
  ]
})
```

INFO

Setting **z** to null forces a single line; we want the **stroke** to vary within the line instead of producing a separate line for each color.

Interpolation is controlled by the [**curve** option](https://observablehq.com/plot/features/curves). The default curve is _linear_, which draws straight line segments between pairs of adjacent points. A _step_ curve is nice for emphasizing when the value changes, while _basis_ and _catmull–rom_ are nice for smoothing.

## Line options [​](https://observablehq.com/plot/marks/line\#line-options)

The following channels are required:

- **x** \- the horizontal position; bound to the _x_ scale
- **y** \- the vertical position; bound to the _y_ scale

In addition to the [standard mark options](https://observablehq.com/plot/features/marks#mark-options), the following optional channels are supported:

- **z** \- a categorical value to group data into series

By default, the data is assumed to represent a single series (a single value that varies over time, _e.g._). If the **z** channel is specified, data is grouped by **z** to form separate series. Typically **z** is a categorical value such as a series name. If **z** is not specified, it defaults to **stroke** if a channel, or **fill** if a channel.

The **fill** defaults to _none_. The **stroke** defaults to _currentColor_ if the fill is _none_, and to _none_ otherwise. If the stroke is defined as a channel, the line will be broken into contiguous overlapping segments when the stroke color changes; the stroke color will apply to the interval spanning the current data point and the following data point. This behavior also applies to the **fill**, **fillOpacity**, **strokeOpacity**, **strokeWidth**, **opacity**, **href**, **title**, and **ariaLabel** channels. When any of these channels are used, setting an explicit **z** channel (possibly to null) is strongly recommended. The **strokeWidth** defaults to 1.5, the **strokeLinecap** and **strokeLinejoin** default to _round_, and the **strokeMiterlimit** defaults to 1.

Points along the line are connected in input order. Likewise, if there are multiple series via the **z**, **fill**, or **stroke** channel, the series are drawn in input order such that the last series is drawn on top. Typically, the data is already in sorted order, such as chronological for time series; if sorting is needed, consider a [sort transform](https://observablehq.com/plot/transforms/sort).

The line mark supports [curve options](https://observablehq.com/plot/features/curves) to control interpolation between points, and [marker options](https://observablehq.com/plot/features/markers) to add a marker (such as a dot or an arrowhead) on each of the control points. The default curve is _auto_, which is equivalent to _linear_ if there is no [projection](https://observablehq.com/plot/features/projections), and otherwise uses the associated projection. If any of the **x** or **y** values are invalid (undefined, null, or NaN), the line will be interrupted, resulting in a break that divides the line shape into multiple segments. (See [d3-shape’s _line_.defined](https://d3js.org/d3-shape/line#line_defined) for more.) If a line segment consists of only a single point, it may appear invisible unless rendered with rounded or square line caps. In addition, some curves such as _cardinal-open_ only render a visible segment if it contains multiple points.

## line( _data_, _options_) [​](https://observablehq.com/plot/marks/line\#line)

js

```
Plot.line(aapl, {x: "Date", y: "Close"})
```

Returns a new line with the given _data_ and _options_. If neither the **x** nor **y** options are specified, _data_ is assumed to be an array of pairs \[\[ _x₀_, _y₀_\], \[ _x₁_, _y₁_\], \[ _x₂_, _y₂_\], …\] such that **x** = \[ _x₀_, _x₁_, _x₂_, …\] and **y** = \[ _y₀_, _y₁_, _y₂_, …\].

## lineX( _data_, _options_) [​](https://observablehq.com/plot/marks/line\#lineX)

js

```
Plot.lineX(aapl.map((d) => d.Close))
```

Similar to [line](https://observablehq.com/plot/marks/line#line) except that if the **x** option is not specified, it defaults to the identity function and assumes that _data_ = \[ _x₀_, _x₁_, _x₂_, …\]. If the **y** option is not specified, it defaults to \[0, 1, 2, …\].

If the **interval** option is specified, the [binY transform](https://observablehq.com/plot/transforms/bin) is implicitly applied to the specified _options_. The reducer of the output _x_ channel may be specified via the **reduce** option, which defaults to _first_. To default to zero instead of showing gaps in data, as when the observed value represents a quantity, use the _sum_ reducer.

js

```
Plot.lineX(observations, {y: "date", x: "temperature", interval: "day"})
```

The **interval** option is recommended to “regularize” sampled data; for example, if your data represents timestamped temperature measurements and you expect one sample per day, use "day" as the interval.

## lineY( _data_, _options_) [​](https://observablehq.com/plot/marks/line\#lineY)

js

```
Plot.lineY(aapl.map((d) => d.Close))
```

Similar to [line](https://observablehq.com/plot/marks/line#line) except that if the **y** option is not specified, it defaults to the identity function and assumes that _data_ = \[ _y₀_, _y₁_, _y₂_, …\]. If the **x** option is not specified, it defaults to \[0, 1, 2, …\].

If the **interval** option is specified, the [binX transform](https://observablehq.com/plot/transforms/bin) is implicitly applied to the specified _options_. The reducer of the output _y_ channel may be specified via the **reduce** option, which defaults to _first_. To default to zero instead of showing gaps in data, as when the observed value represents a quantity, use the _sum_ reducer.

js

```
Plot.lineY(observations, {x: "date", y: "temperature", interval: "day"})
```

The **interval** option is recommended to “regularize” sampled data; for example, if your data represents timestamped temperature measurements and you expect one sample per day, use "day" as the interval.

Pager

[Previous pageImage](https://observablehq.com/plot/marks/image)

[Next pageLinear regression](https://observablehq.com/plot/marks/linear-regression)

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

---
url: "https://observablehq.com/plot/marks/area"
title: "Area mark | Plot"
---

# Area mark [​](https://observablehq.com/plot/marks/area\#area-mark)

The **area mark** draws the region between a baseline ( **x1**, **y1**) and a topline ( **x2**, **y2**) as in an area chart. Often the baseline represents _y_ = 0, and because the area mark interpolates between adjacent data points, typically both the _x_ and _y_ scales are quantitative or temporal.

020406080100120140160180↑ Close20142015201620172018 [Fork](https://observablehq.com/@observablehq/plot-area-simple "Open on Observable")

js

```
Plot.areaY(aapl, {x: "Date", y: "Close"}).plot()
```

The area mark has three constructors: [areaY](https://observablehq.com/plot/marks/area#areaY) for when the baseline and topline share _x_ values, as in a time-series area chart where time goes right→ (or ←left); [areaX](https://observablehq.com/plot/marks/area#areaX) for when the baseline and topline share _y_ values, as in a time-series area chart where time goes up↑ (or down↓); and lastly the rarely-used [area](https://observablehq.com/plot/marks/area#area) where the baseline and topline share neither _x_ nor _y_ values.

The area mark is often paired with a [line](https://observablehq.com/plot/marks/line) and [rule](https://observablehq.com/plot/marks/rule) mark to accentuate the topline and baseline.

020406080100120140160180↑ Close20142015201620172018 [Fork](https://observablehq.com/@observablehq/plot-area-and-line "Open on Observable")

js

```
Plot.plot({
  y: {
    grid: true
  },
  marks: [\
    Plot.areaY(aapl, {x: "Date", y: "Close", fillOpacity: 0.3}),\
    Plot.lineY(aapl, {x: "Date", y: "Close"}),\
    Plot.ruleY([0])\
  ]
})
```

With the default definitions of **x** = index and **y** = [identity](https://observablehq.com/plot/features/transforms#identity), you can pass an array of numbers as data. Below, a random walk is constructed with [d3.cumsum](https://observablehq.com/@d3/d3-cumsum?collection=@d3/d3-array) and [d3.randomNormal](https://observablehq.com/@d3/d3-random?collection=@d3/d3-random).

−8−6−4−2024681012141618200100200300400500 [Fork](https://observablehq.com/@observablehq/plot-random-walk-area "Open on Observable")

js

```
Plot.areaY(d3.cumsum({length: 600}, d3.randomNormal())).plot()
```

As with [lines](https://observablehq.com/plot/marks/line), points in areas are connected in input order: the first point is connected to the second point, the second is connected to the third, and so on. Area data is typically in chronological order. Unsorted data may produce gibberish.

020406080100120140160180↑ Close20142015201620172018 [Fork](https://observablehq.com/@observablehq/plot-area-sort "Open on Observable")

js

```
Plot.areaY(d3.shuffle(aapl.slice()), {x: "Date", y: "Close"}).plot() // 🌶️
```

If your data isn’t sorted, use the [sort transform](https://observablehq.com/plot/transforms/sort).

020406080100120140160180↑ Close20142015201620172018 [Fork](https://observablehq.com/@observablehq/plot-area-sort "Open on Observable")

js

```
Plot.areaY(d3.shuffle(aapl.slice()), {x: "Date", y: "Close", sort: "Date"}).plot()
```

When the baseline is not _y_ = 0 but instead represents another dimension of data as in a band chart, specify **y1** and **y2** instead of **y**.

404550556065707580↑ Temperature (°F)Oct2010Jan2011AprJulOctJan2012AprJulOct [Fork](https://observablehq.com/@observablehq/plot-temperature-band "Open on Observable")

js

```
Plot.plot({
  y: {
    label: "Temperature (°F)",
    grid: true
  },
  marks: [\
    Plot.areaY(sftemp, {x: "date", y1: "low", y2: "high"})\
  ]
})
```

TIP

Since **y1** and **y2** refer to different fields here, a _y_-scale label is specified to improve readability. Also, the band above is spiky; you can smooth it by applying a [window transform](https://observablehq.com/plot/transforms/window).

While charts typically put _y_ = 0 on the bottom edge, such that the area grows up↑, this is not required; reversing the _y_ scale will produce a “hanging” area that grows down↓.

180160140120100806040200↓ Close20142015201620172018 [Fork](https://observablehq.com/@observablehq/plot-top-down-area-chart "Open on Observable")

js

```
Plot.plot({
  x: {
    label: null
  },
  y: {
    grid: true,
    reverse: true
  },
  marks: [\
    Plot.areaY(aapl, {x: "Date", y: "Close", fillOpacity: 0.3}),\
    Plot.lineY(aapl, {x: "Date", y: "Close"}),\
    Plot.ruleY([0])\
  ]
})
```

For a vertically-oriented baseline and topline, such as when time goes up↑ instead of right→, use [areaX](https://observablehq.com/plot/marks/area#areaX) instead of [areaY](https://observablehq.com/plot/marks/area#areaY) and swap **x** and **y**.

20142015201620172018020406080100120140160180Close → [Fork](https://observablehq.com/@observablehq/plot-vertical-area-chart "Open on Observable")

js

```
Plot.plot({
  x: {
    grid: true
  },
  marks: [\
    Plot.areaX(aapl, {y: "Date", x: "Close", fillOpacity: 0.3}),\
    Plot.lineX(aapl, {y: "Date", x: "Close"}),\
    Plot.ruleX([0])\
  ]
})
```

If some channel values are undefined (or null or NaN), gaps will appear between adjacent points. To demonstrate, below we set the **y** value to NaN for the first three months of each year.

02040608010012014016018020142015201620172018 [Fork](https://observablehq.com/@observablehq/plot-area-chart-with-missing-data "Open on Observable")

js

```
Plot.plot({
  y: {
    grid: true
  },
  marks: [\
    Plot.areaY(aapl, {x: "Date", y: (d) => d.Date.getUTCMonth() < 3 ? NaN : d.Close, fillOpacity: 0.3}),\
    Plot.lineY(aapl, {x: "Date", y: (d) => d.Date.getUTCMonth() < 3 ? NaN : d.Close}),\
    Plot.ruleY([0])\
  ]
})
```

Supplying undefined values is not the same as filtering the data: the latter will interpolate between the data points. Observe the conspicuous straight lines below!

020406080100120140160180↑ Close20142015201620172018

js

```
Plot.plot({
  y: {
    grid: true
  },
  marks: [\
    Plot.areaY(aapl, {filter: (d) => d.Date.getUTCMonth() >= 3, x: "Date", y: "Close", fillOpacity: 0.3}),\
    Plot.lineY(aapl, {x: "Date", y: (d) => d.Date.getUTCMonth() < 3 ? NaN : d.Close}),\
    Plot.ruleY([0])\
  ]
})
```

If a **fill** channel is specified, it is assumed to be ordinal or nominal; data is grouped into series and then implicitly [stacked](https://observablehq.com/plot/transforms/stack).

02468101214↑ Unemployed (thousands)20002001200220032004200520062007200820092010 [Fork](https://observablehq.com/@observablehq/plot-stacked-areas "Open on Observable")

js

```
Plot.plot({
  y: {
    transform: (d) => d / 1000,
    label: "Unemployed (thousands)"
  },
  marks: [\
    Plot.areaY(industries, {x: "date", y: "unemployed", fill: "industry"}),\
    Plot.ruleY([0])\
  ]
})
```

CAUTION

This area chart uses color but does not include a [legend](https://observablehq.com/plot/features/legends). This should usually be avoided because color cannot be interpreted without a legend, titles, or labels.

Or, as a streamgraph with the **offset** stack transform option:

02468101214↑ Unemployed (thousands)20002001200220032004200520062007200820092010 [Fork](https://observablehq.com/@observablehq/plot-centered-streamgraph "Open on Observable")

js

```
Plot.plot({
  y: {
    transform: (d) => d / 1000,
    label: "Unemployed (thousands)"
  },
  marks: [\
    Plot.areaY(industries, {x: "date", y: "unemployed", fill: "industry", offset: "wiggle"}),\
  ]
})
```

The **z** channel determines how data is grouped: if the **z** channel is not specified, but a varying **fill** channel is, the **fill** channel is used for **z**; the **z** channel will further fallback to a varying **stroke** channel if needed.

The **z** channel (either implicitly or explicitly) is typically used with the [stack transform](https://observablehq.com/plot/transforms/stack) for a stacked area chart or streamgraph. You can disable the implicit stack transform and produce overlapping areas by setting **y2** instead of **y**.

02004006008001,0001,2001,4001,6001,8002,0002,2002,400↑ unemployed20002001200220032004200520062007200820092010 [Fork](https://observablehq.com/@observablehq/plot-overlapping-areas "Open on Observable")

js

```
Plot.plot({
  marks: [\
    Plot.areaY(industries, {x: "date", y2: "unemployed", z: "industry", fillOpacity: 0.1}),\
    Plot.lineY(industries, {x: "date", y: "unemployed", z: "industry", strokeWidth: 1})\
  ]
})
```

To vary **fill** within a single series, set the **z** option to null.

20M30M100M200MVolume020406080100120140160180↑ Close20142015201620172018 [Fork](https://observablehq.com/@observablehq/plot-variable-fill-area "Open on Observable")

js

```
Plot.plot({
  color: {
    type: "log",
    legend: true
  },
  marks: [\
    Plot.areaY(aapl, {x: "Date", y: "Close", fill: "Volume", z: null}),\
    Plot.ruleY([0])\
  ]
})
```

As an alternative to overlapping or stacking, [faceting](https://observablehq.com/plot/features/facets) will produce small multiples, here arranged vertically with a shared _x_-axis.

AgricultureBusiness servicesConstructionEducation and HealthFinanceGovernmentInformationLeisure and hospitalityManufacturingMining and ExtractionOtherSelf-employedTransportation and UtilitiesWholesale and Retail Trade [Fork](https://observablehq.com/@observablehq/plot-faceted-areas "Open on Observable")

js

```
Plot.plot({
  height: 720,
  axis: null,
  marks: [\
    Plot.areaY(industries, {x: "date", y: "unemployed", fy: "industry"}),\
    Plot.text(industries, Plot.selectFirst({text: "industry", fy: "industry", frameAnchor: "top-left", dx: 6, dy: 6})),\
    Plot.frame()\
  ]
})
```

TIP

Above, smaller industries such as agriculture and mining & extraction are dwarfed by larger industries such as wholesale & retail trade. To emphasize each industry’s trend, instead of comparing absolute numbers across industries, you could use the [normalize transform](https://observablehq.com/plot/transforms/normalize).

Or, as a [horizon chart](https://observablehq.com/@observablehq/plot-horizon), where the area is repeated at different scales with different colors, showing both small-scale variation in position and large-scale variation in color:

AgricultureBusiness servicesConstructionEducation and HealthFinanceGovernmentInformationLeisure and hospitalityManufacturingMining and ExtractionOtherSelf-employedTransportation and UtilitiesWholesale and Retail Trade [Fork](https://observablehq.com/@observablehq/plot-unemployment-horizon-chart "Open on Observable")

js

```
Plot.plot((() => {
  const bands = 7;
  const step = d3.max(industries, (d) => d.unemployed) / bands;
  return {
    height: 720,
    axis: null,
    y: {domain: [0, step]},
    color: {scheme: "YlGnBu"},
    facet: {data: industries, y: "industry"},
    marks: [\
      d3.range(bands).map((i) => Plot.areaY(industries, {x: "date", y: (d) => d.unemployed - i * step, fill: i, clip: true})),\
      Plot.text(industries, Plot.selectFirst({text: "industry", frameAnchor: "top-left", dx: 6, dy: 6})),\
      Plot.frame()\
    ]
  };
})())
```

See also the [ridgeline chart](https://observablehq.com/@observablehq/plot-ridgeline) example.

Interpolation is controlled by the [**curve** option](https://observablehq.com/plot/features/curves). The default curve is _linear_, which draws straight line segments between pairs of adjacent points. A _step_ curve is nice for emphasizing when the value changes, while _basis_ and _catmull–rom_ are nice for smoothing.

## Area options [​](https://observablehq.com/plot/marks/area\#area-options)

The following channels are required:

- **x1** \- the horizontal position of the baseline; bound to the _x_ scale
- **y1** \- the vertical position of the baseline; bound to the _y_ scale

In addition to the [standard mark options](https://observablehq.com/plot/features/marks#mark-options), the following optional channels are supported:

- **x2** \- the horizontal position of the topline; bound to the _x_ scale
- **y2** \- the vertical position of the topline; bound to the _y_ scale
- **z** \- a categorical value to group data into series

If **x2** is not specified, it defaults to **x1**. If **y2** is not specified, it defaults to **y1**. These defaults facilitate sharing _x_ or _y_ coordinates between the baseline and topline. See also the implicit stack transform and shorthand **x** and **y** options supported by [areaY](https://observablehq.com/plot/marks/area#areaY) and [areaX](https://observablehq.com/plot/marks/area#areaX).

By default, the data is assumed to represent a single series ( _i.e._, a single value that varies over time). If the **z** channel is specified, data is grouped by **z** to form separate series. Typically **z** is a categorical value such as a series name. If **z** is not specified, it defaults to **fill** if a channel, or **stroke** if a channel.

The **stroke** defaults to _none_. The **fill** defaults to _currentColor_ if the stroke is _none_, and to _none_ otherwise. If the fill is defined as a channel, the area will be broken into contiguous overlapping segments when the fill color changes; the fill color will apply to the interval spanning the current data point and the following data point. This behavior also applies to the **fillOpacity**, **stroke**, **strokeOpacity**, **strokeWidth**, **opacity**, **href**, **title**, and **ariaLabel** channels. When any of these channels are used, setting an explicit **z** channel (possibly to null) is strongly recommended. The **strokeLinecap** and **strokeLinejoin** default to _round_, and the **strokeMiterlimit** defaults to 1.

Points along the baseline and topline are connected in input order. Likewise, if there are multiple series via the **z**, **fill**, or **stroke** channel, the series are drawn in input order such that the last series is drawn on top. Typically, the data is already in sorted order, such as chronological for time series; if sorting is needed, consider a [sort transform](https://observablehq.com/plot/transforms/sort).

The area mark supports [curve options](https://observablehq.com/plot/features/curves) to control interpolation between points. If any of the **x1**, **y1**, **x2**, or **y2** values are invalid (undefined, null, or NaN), the baseline and topline will be interrupted, resulting in a break that divides the area shape into multiple segments. (See [d3-shape’s _area_.defined](https://d3js.org/d3-shape/area#area_defined) for more.) If an area segment consists of only a single point, it may appear invisible unless rendered with rounded or square line caps. In addition, some curves such as _cardinal-open_ only render a visible segment if it contains multiple points.

## areaY( _data_, _options_) [​](https://observablehq.com/plot/marks/area\#areaY)

js

```
Plot.areaY(aapl, {x: "Date", y: "Close"})
```

Returns a new area with the given _data_ and _options_. This constructor is used when the baseline and topline share _x_ values, as in a time-series area chart where time goes right→. If neither the **y1** nor **y2** option is specified, the **y** option may be specified as shorthand to apply an implicit [stackY transform](https://observablehq.com/plot/transforms/stack); this is the typical configuration for an area chart with a baseline at _y_ = 0\. If the **y** option is not specified, it defaults to the identity function. The **x** option specifies the **x1** channel; and the **x1** and **x2** options are ignored.

If the **interval** option is specified, the [binX transform](https://observablehq.com/plot/transforms/bin) is implicitly applied to the specified _options_. The reducer of the output _y_ channel may be specified via the **reduce** option, which defaults to _first_. To default to zero instead of showing gaps in data, as when the observed value represents a quantity, use the _sum_ reducer.

js

```
Plot.areaY(observations, {x: "date", y: "temperature", interval: "day"})
```

The **interval** option is recommended to “regularize” sampled data; for example, if your data represents timestamped temperature measurements and you expect one sample per day, use "day" as the interval.

The **areaY** mark draws the region between a baseline ( _y1_) and a topline ( _y2_) as in an area chart. When the baseline is _y_ = 0, the _y_ channel can be specified instead of _y1_ and _y2_.

## areaX( _data_, _options_) [​](https://observablehq.com/plot/marks/area\#areaX)

js

```
Plot.areaX(aapl, {y: "Date", x: "Close"})
```

Returns a new area with the given _data_ and _options_. This constructor is used when the baseline and topline share _y_ values, as in a time-series area chart where time goes up↑. If neither the **x1** nor **x2** option is specified, the **x** option may be specified as shorthand to apply an implicit [stackX transform](https://observablehq.com/plot/transforms/stack); this is the typical configuration for an area chart with a baseline at _x_ = 0\. If the **x** option is not specified, it defaults to the identity function. The **y** option specifies the **y1** channel; and the **y1** and **y2** options are ignored.

If the **interval** option is specified, the [binY transform](https://observablehq.com/plot/transforms/bin) is implicitly applied to the specified _options_. The reducer of the output _x_ channel may be specified via the **reduce** option, which defaults to _first_. To default to zero instead of showing gaps in data, as when the observed value represents a quantity, use the _sum_ reducer.

js

```
Plot.areaX(observations, {y: "date", x: "temperature", interval: "day"})
```

The **interval** option is recommended to “regularize” sampled data; for example, if your data represents timestamped temperature measurements and you expect one sample per day, use "day" as the interval.

## area( _data_, _options_) [​](https://observablehq.com/plot/marks/area\#area)

js

```
Plot.area(aapl, {x1: "Date", y1: 0, y2: "Close"})
```

Returns a new area with the given _data_ and _options_. This method is rarely used directly; it is only needed when the baseline and topline have neither common **x** nor **y** values. [areaY](https://observablehq.com/plot/marks/area#areaY) is used in the common horizontal orientation where the baseline and topline share **x** values, while [areaX](https://observablehq.com/plot/marks/area#areaX) is used in the vertical orientation where the baseline and topline share **y** values.

Pager

[Previous pageAccessibility](https://observablehq.com/plot/features/accessibility)

[Next pageArrow](https://observablehq.com/plot/marks/arrow)

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

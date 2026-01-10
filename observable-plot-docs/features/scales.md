---
url: "https://observablehq.com/plot/features/scales"
title: "Scales | Plot"
---

# Scales [​](https://observablehq.com/plot/features/scales\#scales)

**Scales** convert an abstract value such as time or temperature to a visual value such as _x_ → or _y_ ↑ position or color. For example, say we have a dataset (`gistemp`) containing monthly observations of [global average surface temperature](https://data.giss.nasa.gov/gistemp/) from 1880 to 2016, represented as the “anomaly” (or difference) relative to the 1951–1980 average. The first few rows are:

| Date | Anomaly |
| --- | --- |
| 1880-01-01 | -0.3 |
| 1880-02-01 | -0.21 |
| 1880-03-01 | -0.18 |
| 1880-04-01 | -0.27 |
| 1880-05-01 | -0.14 |
| 1880-06-01 | -0.29 |

When visualizing this data with a [line](https://observablehq.com/plot/marks/line), the _x_ scale is responsible for mapping dates to horizontal↔︎ positions. For example, 1880-01-01 might be mapped to _x_ = 40 (on the left) and 2016-12-01 might be mapped to _x_ = 620 (on the right). Likewise, the _y_ scale maps temperature anomalies to vertical↕︎ positions.

−0.6−0.4−0.20.00.20.40.60.81.01.2↑ Anomaly1880190019201940196019802000 [Fork](https://observablehq.com/@observablehq/plot-scales-intro "Open on Observable")

js

```
Plot.lineY(gistemp, {x: "Date", y: "Anomaly"}).plot()
```

In Plot, the [mark](https://observablehq.com/plot/features/marks) binds channels to scales; for example, the line’s **x** channel is bound to the _x_ scale. The channel name and the scale name are often the same, but not always; for example, an area’s **y1** and **y2** channels are both bound to the _y_ scale. (You can opt-out of a scale for a particular channel using [scale overrides](https://observablehq.com/plot/features/marks#mark-options) if needed.)

Think of a scale as a function that takes an abstract value and returns the corresponding visual value. For the _y_ scale above, that might look like this:

js

```
function y(anomaly) {
  const t = (anomaly - minAnomaly) / (maxAnomaly - minAnomaly); // t in [0, 1]
  return height - marginBottom - t * (height - marginTop - marginBottom);
}
```

The function `y` depends on a few additional details: the chart’s size and margins, and the minimum and maximum temperatures in the data:

js

```
const marginTop = 20;
const marginBottom = 30;
const height = 400;
const minAnomaly = d3.min(gistemp, (d) => d.Anomaly);
const maxAnomaly = d3.max(gistemp, (d) => d.Anomaly);
```

Scales aren’t limited to horizontal and vertical position. They can also output to color, radius, length, opacity, and more. For example if we switch to a [rule](https://observablehq.com/plot/marks/rule) and use the **stroke** channel instead of **y**, we get a one-dimensional heatmap:

1880190019201940196019802000 [Fork](https://observablehq.com/@observablehq/plot-scales-intro "Open on Observable")

js

```
Plot.ruleX(gistemp, {x: "Date", stroke: "Anomaly"}).plot()
```

While the resulting chart looks different, the _color_ scale here behaves similarly to the `y` function above — the only difference is that it interpolates colors (using [d3.interpolateTurbo](https://d3js.org/d3-scale-chromatic/sequential#interpolateTurbo)) instead of numbers (the top and bottom sides of the plot frame):

js

```
function color(anomaly) {
  const t = (anomaly - minAnomaly) / (maxAnomaly - minAnomaly); // t in [0, 1]
  return d3.interpolateTurbo(t);
}
```

Within a given [plot](https://observablehq.com/plot/features/plots), marks share scales. For example, if a plot has two line marks, such as the lines below visualizing the daily closing price of Google and Apple stock, both share the same _x_ and _y_ scales for a consistent encoding.

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

When comparing the performance of different stocks, we typically want to normalize the return relative to a purchase price; see the [normalize transform](https://observablehq.com/plot/transforms/normalize) for an example. Also, not that we recommend them, but if you are interested in dual-axis charts, please upvote [#147](https://github.com/observablehq/plot/issues/147).

Plot has many different scales; we categorize them by their _input_ ( **domain**) and _output_ ( **range**).

The **domain** is the abstract values that the scale expects as input. For quantitative or temporal data, it is typically expressed as an extent such as \[ _start_, _end_\], \[ _cold_, _hot_\], or \[ _min_, _max_\]. For ordinal or nominal data, it is an array of values such as names or categories. The type of input values corresponds to the **type** scale option ( _e.g._, _linear_ or _ordinal_).

The **range** is the visual values that the scale generates as output. For position scales, it is typically an extent such as \[ _left_, _right_\] or \[ _bottom_, _top_\]; for color scales, it might be a continuous extent \[ _blue_, _red_\] or an array of discrete colors. The type of values that a scale outputs corresponds to the _name_ of the scale ( _e.g._, _x_ or _color_).

Let’s look at some examples to make this less abstract.

## Continuous scales [​](https://observablehq.com/plot/features/scales\#continuous-scales)

The domain of a quantitative scale is a continuous extent \[ _min_, _max_\] where _min_ and _max_ are numbers, such as temperatures. Below, the first domain value ( _x_ = 0) corresponds to the left side of the plot while the second ( _x_ = 100) corresponds to the right side.

0102030405060708090100 [Fork](https://observablehq.com/@observablehq/plot-continuous-scales "Open on Observable")

js

```
Plot.plot({x: {domain: [0, 100], grid: true}})
```

Flipping the domain reverses the scale so that + _x_ points ←left instead of right→.

1009080706050403020100 [Fork](https://observablehq.com/@observablehq/plot-continuous-scales "Open on Observable")

js

```
Plot.plot({x: {domain: [100, 0], grid: true}})
```

Alternatively, use the **reverse** option; this is convenient when the domain is implied from data rather than specified explicitly.

1009080706050403020100 [Fork](https://observablehq.com/@observablehq/plot-continuous-scales "Open on Observable")

js

```
Plot.plot({x: {domain: [0, 100], reverse: true, grid: true}})
```

If the domain is dates, Plot will default to a UTC scale. This is a linear scale with ticks based on the Gregorian calendar.

Jan2021FebMarAprMayJunJulAugSepOctNovDecJan2022 [Fork](https://observablehq.com/@observablehq/plot-continuous-scales "Open on Observable")

js

```
Plot.plot({x: {domain: [new Date("2021-01-01"), new Date("2022-01-01")], grid: true}})
```

To force a UTC scale, say when the data is milliseconds since UNIX epoch rather than Date instances, pass _utc_ as the **type** option. Though we recommend coercing strings and numbers to more specific types when you load data, rather than relying on scales to do it.

Jan2021FebMarAprMayJunJulAugSepOctNovDecJan2022 [Fork](https://observablehq.com/@observablehq/plot-continuous-scales "Open on Observable")

js

```
Plot.plot({x: {type: "utc", domain: [1609459200000, 1640995200000], grid: true}})
```

If the scale **type** is _time_, the ticks will be in local time — as with the dates below — rather than UTC.

Jan2021FebMarAprMayJunJulAugSepOctNovDecJan2022 [Fork](https://observablehq.com/@observablehq/plot-continuous-scales "Open on Observable")

js

```
Plot.plot({x: {type: "time", domain: [new Date(2021, 0, 1), new Date(2022, 0, 1)], grid: true}})
```

When plotting values that vary widely, such as the luminosity of stars in an [HR diagram](https://observablehq.com/@mbostock/hertzsprung-russell-diagram), a _log_ scale may improve readability. Log scales default to base-10 ticks with SI-prefix notation.

1101001k10k100k [Fork](https://observablehq.com/@observablehq/plot-continuous-scales "Open on Observable")

js

```
Plot.plot({x: {type: "log", domain: [1e0, 1e5], grid: true}})
```

If you prefer conventional notation, you can specify the **tickFormat** option to change the behavior of the axis. The **tickFormat** option can either be a [d3.format](https://d3js.org/d3-format) string or a function that takes a tick value and returns the corresponding string. Note, however, that this may result in overlapping text.

1101001,00010,000100,000 [Fork](https://observablehq.com/@observablehq/plot-continuous-scales "Open on Observable")

js

```
Plot.plot({x: {type: "log", domain: [1e0, 1e5], tickFormat: ",", grid: true}})
```

Log scales also support a **base** option, say for powers of two. This does not affect the scale’s encoding, but it does change where ticks are shown.

12481632641282565121,0242,0484,0968,192 [Fork](https://observablehq.com/@observablehq/plot-continuous-scales "Open on Observable")

js

```
Plot.plot({x: {type: "log", base: 2, domain: [1e0, 1e4], ticks: 20, grid: true}})
```

The domain of a log scale cannot include (or cross) zero; for this, consider a [bi-symmetric log](https://d3js.org/d3-scale/symlog) scale instead.

−10−8−6−4−20246810 [Fork](https://observablehq.com/@observablehq/plot-continuous-scales "Open on Observable")

js

```
Plot.plot({x: {type: "symlog", domain: [-10, 10], grid: true}})
```

Power scales and square-root scales are also supported. The _pow_ scale supports the **exponent** option, which defaults to 1 (for a linear scale). The _sqrt_ scale is shorthand for a _pow_ scale with exponent 0.5.

0102030405060708090100 [Fork](https://observablehq.com/@observablehq/plot-continuous-scales "Open on Observable")

js

```
Plot.plot({x: {type: "sqrt", domain: [0, 100], grid: true}})
```

0102030405060708090100 [Fork](https://observablehq.com/@observablehq/plot-continuous-scales "Open on Observable")

js

```
Plot.plot({x: {type: "pow", exponent: 1 / 3, domain: [0, 100], grid: true}})
```

Continuous scales also support a **clamp** option which, if true, clamps input values to the scale’s domain before scaling. This is useful for preventing marks from escaping the chart area.

Continuous scales support an **interpolate** option specified either as a function that takes a single argument _t_ in \[0, 1\] and returns the corresponding value from the **range**, or as a two-argument function that takes a pair of values \[ _start_, _end_\] from the range and returns the corresponding interpolator from \[0, 1\], typically mapping 0 to _start_, and 1 to _end_.

Continuous scales support a piecewise **domain** specified as an array of _n_ domain values (with _n_ greater than or equal to two), with a corresponding **range** having the same number of values; each segment of the domain is mapped to the matching segment of the range using the scale’s interpolator. When the domain has _n_ > 2 elements and the range has two elements (for example, when using the default range on a _x_ or _y_ scale), the latter is automatically split into _n_ − 1 segments of equal size. Note that in addition to the domain, you must specify the scale’s continuous **type** since a scale specified with a domain having more than two elements otherwise defaults to an ordinal scale. (You will often have to specify the **ticks** manually, too.) For an example, see the [Polylinear axis](https://observablehq.com/@observablehq/polylinear-axis) notebook.

## Discrete scales [​](https://observablehq.com/plot/features/scales\#discrete-scales)

Sadly, not all data is continuous: some data is merely ordinal, such as t-shirt sizes; and some categorical ( _a.k.a._ nominal), such as brands of clothing. To encode such data as position, a _point_ or _band_ scale is required.

A _point_ scale divides space into uniformly-spaced discrete values. It is commonly used for scatterplots (a [dot mark](https://observablehq.com/plot/marks/dot)) of ordinal data. It is the default scale type for ordinal data on the _x_ and _y_ scale.

ABCDEFGHIJ [Fork](https://observablehq.com/@observablehq/plot-discrete-scales "Open on Observable")

js

```
Plot.plot({x: {type: "point", domain: "ABCDEFGHIJ", grid: true}})
```

A band scale divides space into uniformly-spaced and -sized discrete intervals. It is commonly used for bar charts (bar marks). To show the bands below, we use a [cell](https://observablehq.com/plot/marks/cell) instead of a [grid](https://observablehq.com/plot/marks/grid).

ABCDEFGHIJ [Fork](https://observablehq.com/@observablehq/plot-discrete-scales "Open on Observable")

js

```
Plot
  .cell("ABCDEFGHIJ", {x: Plot.identity, stroke: "currentColor", strokeOpacity: 0.1})
  .plot({x: {type: "band", domain: "ABCDEFGHIJ"}})
```

While _point_ and _band_ scales appear visually similar when only the grid is visible, the two are not identical — they differ respective to padding. Play with the options below to get a sense of their effect on the scale’s behavior.

Padding:0.10Align:0.50

ABCDEFGHIJ

js

```
Plot.plot({
  grid: true,
  marginTop: 0.5,
  x: {
    padding,
    align,
    round: false
  },
  marks: [\
    Plot.frame({strokeOpacity: 0.3}),\
    Plot.tickX("ABCDEFGHIJ", {x: Plot.identity, stroke: "currentColor"})\
  ]
})
```

ABCDEFGHIJ

js

```
Plot.plot({
  grid: true,
  marginTop: 0.5,
  x: {
    padding,
    align,
    round: false
  },
  marks: [\
    Plot.frame({strokeOpacity: 0.3}),\
    Plot.cell("ABCDEFGHIJ", {x: Plot.identity, stroke: "currentColor"})\
  ]
})
```

Position scales also have a **round** option which forces the scale to snap to integer pixels. This defaults to true for point and band scales, and false for quantitative scales. Use caution with high-cardinality ordinal domains ( _i.e._, a point or band scale used to encode many different values), as rounding can lead to “wasted” space or even zero-width bands.

## Color scales [​](https://observablehq.com/plot/features/scales\#color-scales)

While position is the most salient (and important) encoding, color matters too! The default quantitative color scale **type** is _linear_, and the default **scheme** is [_turbo_](https://ai.googleblog.com/2019/08/turbo-improved-rainbow-colormap-for.html). A wide variety of sequential, diverging, and cyclical schemes are supported, including ColorBrewer and [_viridis_](http://bids.github.io/colormap/).

Color scheme: BluesGreensGreysPurplesRedsOrangesTurboViridisMagmaInfernoPlasmaCividisCubehelixWarmCoolBuGnBuPuGnBuOrRdPuBuGnPuBuPuRdRdPuYlGnBuYlGnYlOrBrYlOrRdRainbowSinebow

js

```
Plot.plot({
  axis: null,
  padding: 0,
  color: {
    scheme: schemeq
  },
  marks: [\
    Plot.cell(d3.range(40), {x: Plot.identity, fill: Plot.identity, inset: -0.5})\
  ]
})
```

You can implement a custom color scheme by specifying the scale’s **range**, or by passing an **interpolate** function that takes a parameter _t_ in \[0, 1\]. The **interpolate** option can specify a color space such as _rgb_, or a two-argument function that takes a pair of values from the range.

Color interpolate: rgblabhclhsld3.interpolateRgb.gamma(2)(t) => \`hsl(${t \* 360},100%,50%)\`

js

```
Plot.plot({
  axis: null,
  padding: 0,
  color: {
    type: "linear",
    ...interpolateq === "angry-rainbow"
      ? {interpolate: (t) => `hsl(${t * 360},100%,50%)`}
      : interpolateq === "rgb-gamma"
      ? {range: ["steelblue", "orange"], interpolate: d3.interpolateRgb.gamma(2)}
      : {range: ["steelblue", "orange"], interpolate: interpolateq}
  },
  marks: [\
    Plot.cell(d3.range(40), {x: Plot.identity, fill: Plot.identity, inset: -0.5})\
  ]
})
```

And like position scales, you can apply a _sqrt_, _pow_, _log_, or _symlog_ transform; these are often useful when working with non-uniformly distributed data.

Diverging color scales are intended to show positive and negative values, or more generally values above or below some **pivot** value. Diverging color scales default to the _RdBu_ (red–blue) color scheme. The pivot defaults to zero, but you can change it with the **pivot** option, which should ideally be a value near the middle of the domain.

Color scheme: BrBGPRGnPiYGPuOrRdBuRdGyRdYlBuRdYlGnSpectralBuRdBuYlRd

js

```
Plot.plot({
  axis: null,
  padding: 0,
  color: {
    type: "linear",
    scheme: schemed
  },
  marks: [\
    Plot.cell(d3.range(40), {x: Plot.identity, fill: Plot.identity, inset: -0.5})\
  ]
})
```

Below we again show observed global surface temperatures. The reversed _BuRd_ color scheme is used since blue and red are semantically associated with cold and hot, respectively.

−0.6−0.4−0.20.00.20.40.60.81.01.2↑ Anomaly1880190019201940196019802000 [Fork](https://observablehq.com/@observablehq/plot-diverging-color-scatterplot "Open on Observable")

js

```
Plot.plot({
  grid: true,
  color: {
    type: "diverging",
    scheme: "BuRd"
  },
  marks: [\
    Plot.ruleY([0]),\
    Plot.dot(gistemp, {x: "Date", y: "Anomaly", stroke: "Anomaly"})\
  ]
})
```

Plot also provides color schemes for discrete data. Use the _categorical_ type for categorical (nominal) unordered data, and the _ordinal_ type for ordered data.

Color scheme: AccentCategory10Dark2Observable10PairedPastel1Pastel2Set1Set2Set3Tableau10BluesGreensGreysPurplesRedsOrangesTurboViridisMagmaInfernoPlasmaCividisCubehelixWarmCoolBuGnBuPuGnBuOrRdPuBuGnPuBuPuRdRdPuYlGnBuYlGnYlOrBrYlOrRdRainbowSinebow

ABCDEFGHIJ

js

```
Plot.plot({
  color: {
    type: "ordinal",
    scheme: schemeo
  },
  marks: [\
    Plot.cell("ABCDEFGHIJ", {x: Plot.identity, fill: Plot.identity})\
  ]
})
```

CAUTION

Discrete color schemes are intended for data that has only a few unique values. If the size of the categorical domain exceeds the number of colors in the scheme, colors will be reused; combining values into an “other” category is recommended.

## Other scales [​](https://observablehq.com/plot/features/scales\#other-scales)

But wait, there’s more! 😅 Plot has _opacity_, _r_, _symbol_, and _length_ scales, too. For example, the _r_ scale **type** defaults to _sqrt_ such that when used with the [dot mark](https://observablehq.com/plot/marks/dot), the resulting area is proportional to the **r** channel value. You can adjust the effective dot size by specifying an explicit **range**, as below.

Radius: 8.0

12345678910 [Fork](https://observablehq.com/@observablehq/plot-radius-scale-range "Open on Observable")

js

```
Plot.plot({
  r: {range: [0, radius]},
  marks: [\
    Plot.dot(d3.range(1, 11), {x: Plot.identity, r: Plot.identity, fill: "currentColor"})\
  ]
})
```

The default **range** for the associated _r_ scale is constructed such that a zero value maps to zero for an accurate areal encoding, while the first quartile of values is mapped to a radius of three pixels; this tends to be more stable with varying data.

## Type inference [​](https://observablehq.com/plot/features/scales\#type-inference)

Plot strives to be concise: rather than you laboriously specifying everything, Plot can guess by inspecting the data so you don’t have to set the **type**, **domain**, and **range** (and for color, **scheme**) of scales explicitly. But for Plot’s guesses to be accurate, your data must match Plot’s expectations. Here they are.

A scale’s **type** is most often inferred from associated marks’ channel values: strings and booleans imply an _ordinal_ scale; dates imply a _utc_ scale; anything else is _linear_. Plot assumes that your data is consistently typed, so inference is based solely on the first non-null, non-undefined value. We recommend typed CSV (passing `{typed: true}` to Observable’s FileAttachment csv method) or explicitly coercing types when loading data ( _e.g._, d3.autoType).

If a scale’s **domain** is specified explicitly, the scale’s **type** is inferred from the **domain** values rather than channels as described above. However, if the **domain** or **range** has more than two elements, the _ordinal_ type (or _point_ for position scales) is used.

Finally, some marks declare the scale **type** for associated channels. For example, [barX](https://observablehq.com/plot/marks/bar) requires _y_ to be a _band_ scale. Further, the facet scales _fx_ and _fy_ are always _band_ scales, and the _r_ (radius) scale is implicitly a _sqrt_ scale.

If you don’t specify a quantitative scale’s **domain**, it is the extent (minimum and maximum) of associated channel values, except for the _r_ (radius) scale where it goes from zero to the maximum. A quantitative domain can be extended to “nice” human-readable values with the **nice** option. For an ordinal scale, the domain defaults to the sorted union (all distinct values in natural order) of associated values; see the [**sort** mark option](https://observablehq.com/plot/features/scales#sort-mark-option) to change the order.

All position scales ( _x_, _y_, _fx_, and _fy_) have implicit automatic ranges based on the chart dimensions. The _x_ scale ranges from the left to right edge, while the _y_ scale ranges from the bottom to top edge, accounting for margins.

## Scale transforms [​](https://observablehq.com/plot/features/scales\#scale-transforms)

The **transform** scale option allows you to apply a function to all values before they are passed through the scale. This is convenient for transforming a scale’s data, say to convert to thousands or between temperature units.

02468101214161820↑ Temperature (°C)Oct2010Jan2011AprJulOctJan2012AprJulOct [Fork](https://observablehq.com/@observablehq/plot-fahrenheit-to-celsius-scale-transform "Open on Observable")

js

```
Plot.plot({
  y: {
    grid: true,
    label: "Temperature (°C)",
    transform: (f) => (f - 32) * (5 / 9) // convert Fahrenheit to Celsius
  },
  marks: [\
    Plot.ruleY([32]), // 32°F\
    Plot.lineY(sftemp, Plot.windowY(7, {x: "date", y: "high"}))\
  ]
})
```

The **percent** scale option is shorthand for a **transform** that multiplies values by 100; it also adds a percent symbol (%) to the default label.

01234567891011121314↑ Frequency (%)−0.8−0.6−0.4−0.20.00.20.40.60.81.01.21.4Anomaly → [Fork](https://observablehq.com/@observablehq/plot-percent-scale-transform "Open on Observable")

js

```
Plot.plot({
  y: {percent: true}, // convert proportion [0, 1] to percent [0, 100]
  color: {scheme: "BuRd"},
  marks: [\
    Plot.rectY(gistemp, Plot.binX({y: "proportion", fill: "x"}, {x: "Anomaly", fill: "Anomaly"})),\
    Plot.ruleY([0])\
  ]
})
```

CAUTION

[Mark transforms](https://observablehq.com/plot/features/transforms) typically consume values _before_ they are passed through scales ( _e.g._, when binning). In this case the mark transforms will see the values prior to the scale transform as input, and the scale transform will apply to the _output_ of the mark transform.

The **interval** scale option [Permalink to "interval"](https://observablehq.com/plot/features/scales#interval) [^0.5.1](https://github.com/observablehq/plot/releases/tag/v0.5.1 "added in v0.5.1") sets an ordinal scale’s **domain** to the start of every interval within the extent of the data. In addition, it implicitly sets the **transform** of the scale to _interval_.floor, rounding values down to the start of each interval. For example, below we generate a time-series bar chart; when an **interval** is specified, missing days are visible.

Use interval:

05101520253035404550556065↑ Daily trade volume (millions)18Mar251Apr81522296May [Fork](https://observablehq.com/@observablehq/plot-band-scale-interval "Open on Observable")

js

```
Plot.plot({
  marginBottom: 80,
  x: {
    tickRotate: -90,
    interval: intervaled ? "day" : null,
    label: null
  },
  y: {
    transform: (d) => d / 1e6,
    label: "Daily trade volume (millions)"
  },
  marks: [\
    Plot.barY(aapl.slice(-40), {x: "Date", y: "Volume"}),\
    Plot.ruleY([0])\
  ]
})
```

TIP

As an added bonus, the **fontVariant** and **type** options are no longer needed because Plot now understands that the _x_ scale, despite being _ordinal_, represents daily observations.

While the example above relies on the **interval** being promoted to the scale’s **transform**, the [stack](https://observablehq.com/plot/transforms/stack), [bin](https://observablehq.com/plot/transforms/bin), and [group](https://observablehq.com/plot/transforms/group) transforms are also interval-aware: they apply the scale’s **interval**, if any, _before_ grouping values. (This results in the interval being applied twice, both before and after the mark transform, but the second application has no effect since interval application is idempotent.)

The **interval** option can also be used for quantitative and temporal scales. This enforces uniformity, say rounding timed observations down to the nearest hour, which may be helpful for the [stack transform](https://observablehq.com/plot/transforms/stack) among other uses.

## Scale options [​](https://observablehq.com/plot/features/scales\#scale-options)

Each scale’s options are specified as a nested options object with the corresponding scale name within the top-level [plot options](https://observablehq.com/plot/features/plots):

- **x** \- horizontal position
- **y** \- vertical position
- **r** \- radius (size)
- **color** \- fill or stroke
- **opacity** \- fill or stroke opacity
- **length** \- linear length (for [vectors](https://observablehq.com/plot/marks/vector))
- **symbol** \- categorical symbol (for [dots](https://observablehq.com/plot/marks/dot))

For example, to set the domain for the _x_ scale:

1880190019201940196019802000

js

```
Plot.plot({x: {domain: [new Date("1880-01-01"), new Date("2016-11-01")]}})
```

Plot supports many scale types. Some scale types are for quantitative data: values that can be added or subtracted, such as temperature or time. Other scale types are for ordinal or categorical data: unquantifiable values that can only be ordered, such as t-shirt sizes, or values with no inherent order that can only be tested for equality, such as types of fruit. Some scale types are further intended for specific visual encodings: for example, as position or color.

You can set the scale type explicitly via the **type** scale option, though typically the scale type is inferred automatically. Some marks mandate a particular scale type: for example, [barY](https://observablehq.com/plot/marks/bar) requires that the _x_ scale is a _band_ scale. Some scales have a default type: for example, the _r_ (radius) scale defaults to _sqrt_ and the _opacity_ scale defaults to _linear_. Most often, the scale type is inferred from associated data, pulled either from the domain (if specified) or from associated channels. Strings and booleans imply an ordinal scale; dates imply a UTC scale; and anything else is linear. Unless they represent text, we recommend explicitly converting strings to more specific types when loading data ( _e.g._, with d3.autoType or Observable’s FileAttachment). For simplicity’s sake, Plot assumes that data is consistently typed; type inference is based solely on the first non-null, non-undefined value.

For quantitative data ( _i.e._ numbers), a mathematical transform may be applied to the data by changing the scale type:

- _linear_ (default) - linear transform (translate and scale)
- _pow_ \- power (exponential) transform
- _sqrt_ \- square-root transform ( _pow_ transform with exponent = 0.5)
- _log_ \- logarithmic transform
- _symlog_ \- bi-symmetric logarithmic transform per [Webber _et al._](https://www.researchgate.net/publication/233967063_A_bi-symmetric_log_transformation_for_wide-range_data)

The appropriate transform depends on the data’s distribution and what you wish to know. A _sqrt_ transform exaggerates differences between small values at the expense of large values; it is a special case of the _pow_ transform which has a configurable _scale_. **exponent** (0.5 for _sqrt_). A _log_ transform is suitable for comparing orders of magnitude and can only be used when the domain does not include zero. The base defaults to 10 and can be specified with the _scale_. **base** option; note that this only affects the axis ticks and not the scale’s behavior. A _symlog_ transform is more elaborate, but works well with wide-range values that include zero; it can be configured with the _scale_. **constant** option (default 1).

For temporal data ( _i.e._ dates), two variants of a _linear_ scale are also supported:

- _utc_ (default, recommended) - UTC time
- _time_ \- local time

UTC is recommended over local time as charts in UTC time are guaranteed to appear consistently to all viewers whereas charts in local time will depend on the viewer’s time zone. Due to limitations in JavaScript’s Date class, Plot does not yet support an explicit time zone other than UTC.

For ordinal data ( _e.g._, strings), use the _ordinal_ scale type or the _point_ or _band_ position scale types. The _categorical_ scale type is also supported; it is equivalent to _ordinal_ except as a color scale, where it provides a different default color scheme. (Since position is inherently ordinal or even quantitative, categorical data must be assigned an effective order when represented as position, and hence _categorical_ and _ordinal_ may be considered synonymous in context.)

You can opt-out of a scale using the _identity_ scale type. This is useful if you wish to specify literal colors or pixel positions within a mark channel rather than relying on the scale to convert abstract values into visual values. For position scales ( _x_ and _y_), an _identity_ scale is still quantitative and may produce an axis, yet unlike a _linear_ scale the domain and range are fixed based on the plot layout.

TIP

To opt-out of a scale for a single channel, you can specify the channel values as a `{value, scale}` object; see [mark options](https://observablehq.com/plot/features/marks#mark-options).

Quantitative scales, as well as identity position scales, coerce channel values to numbers; both null and undefined are coerced to NaN. Similarly, time scales coerce channel values to dates; numbers are assumed to be milliseconds since UNIX epoch, while strings are assumed to be in [ISO 8601 format](https://github.com/mbostock/isoformat/blob/main/README.md#parsedate-fallback).

A scale’s domain (the extent of its inputs, abstract values) and range (the extent of its outputs, visual values) are typically inferred automatically. You can set them explicitly using these options:

- **domain** \- typically \[ _min_, _max_\], or an array of ordinal or categorical values
- **range** \- typically \[ _min_, _max_\], or an array of ordinal or categorical values
- **unknown** \- the desired output value (defaults to undefined) for invalid input values
- **reverse** \- reverses the domain (or the range), say to flip the chart along _x_ or _y_
- **interval** \- an interval or time interval (for interval data; see below)

For most quantitative scales, the default domain is the \[ _min_, _max_\] of all values associated with the scale. For the _radius_ and _opacity_ scales, the default domain is \[0, _max_\] to ensure a meaningful value encoding. For ordinal scales, the default domain is the set of all distinct values associated with the scale in natural ascending order; for a different order, set the domain explicitly or add a [**sort** option](https://observablehq.com/plot/features/scales#sort-mark-option) to an associated mark. For threshold scales, the default domain is \[0\] to separate negative and non-negative values. For quantile scales, the default domain is the set of all defined values associated with the scale. If a scale is reversed, it is equivalent to setting the domain as \[ _max_, _min_\] instead of \[ _min_, _max_\].

The default range depends on the scale: for position scales ( _x_, _y_, _fx_, and _fy_), the default range depends on the [plot’s size and margins](https://observablehq.com/plot/features/plots). For color scales, there are default color schemes for quantitative, ordinal, and categorical data. For opacity, the default range is \[0, 1\]. And for radius, the default range is designed to produce dots of “reasonable” size assuming a _sqrt_ scale type for accurate area representation: zero maps to zero, the first quartile maps to a radius of three pixels, and other values are extrapolated. This convention for radius ensures that if the scale’s data values are all equal, dots have the default constant radius of three pixels, while if the data varies, dots will tend to be larger.

The behavior of the **unknown** scale option depends on the scale type. For quantitative and temporal scales, the unknown value is used whenever the input value is undefined, null, or NaN. For ordinal or categorical scales, the unknown value is returned for any input value outside the domain. For band or point scales, the unknown option has no effect; it is effectively always equal to undefined. If the unknown option is set to undefined (the default), or null or NaN, then the affected input values will be considered undefined and filtered from the output.

For data at regular intervals, such as integer values or daily samples, the [**interval** option](https://observablehq.com/plot/features/scales#scale-transforms) can be used to enforce uniformity. The specified _interval_ — such as d3.utcMonth — must expose an _interval_.floor( _value_), _interval_.offset( _value_), and _interval_.range( _start_, _stop_) functions. The option can also be specified as a number, in which case it will be promoted to a numeric interval with the given step. The option can alternatively be specified as a string ( _second_, _minute_, _hour_, _day_, _week_, _month_, _quarter_, _half_, _year_, _monday_, _tuesday_, _wednesday_, _thursday_, _friday_, _saturday_, _sunday_) [^0.6.2](https://github.com/observablehq/plot/releases/tag/v0.6.2 "added in v0.6.2") naming the corresponding time interval, or a skip interval consisting of a number followed by the interval name (possibly pluralized), such as _3 months_ or _10 years_. This option sets the default _scale_.transform to the given interval’s _interval_.floor function. In addition, the default _scale_.domain is an array of uniformly-spaced values spanning the extent of the values associated with the scale.

Quantitative scales can be further customized with additional options:

- **clamp** \- if true, clamp input values to the scale’s domain
- **nice** \- if true (or a tick count), extend the domain to nice round values
- **zero** \- if true, extend the domain to include zero if needed
- **percent** \- if true, transform proportions in \[0, 1\] to percentages in \[0, 100\]

Clamping is typically used in conjunction with setting an explicit domain since if the domain is inferred, no values will be outside the domain. Clamping is useful for focusing on a subset of the data while ensuring that extreme values remain visible, but use caution: clamped values may need an annotation to avoid misinterpretation. Top-level **clamp**, **nice**, and **zero** options are supported as shorthand for setting the respective option on all scales.

The **transform** option allows you to apply a function to all values before they are passed through the scale. This is convenient for transforming a scale’s data, say to convert to thousands or between temperature units.

js

```
Plot.plot({
  y: {
    label: "Temperature (°F)",
    transform: (f) => f * 9 / 5 + 32 // convert Celsius to Fahrenheit
  },
  marks: …
})
```

### Color scale options [​](https://observablehq.com/plot/features/scales\#color-scale-options)

The normal scale types — _linear_, _sqrt_, _pow_, _log_, _symlog_, and _ordinal_ — can be used to encode color. In addition, Plot supports special scale types for color:

- _categorical_ \- like _ordinal_, but defaults to _observable10_
- _sequential_ \- like _linear_
- _cyclical_ \- like _linear_, but defaults to _rainbow_
- _threshold_ \- discretizes using thresholds given as the **domain**; defaults to _rdylbu_
- _quantile_ \- discretizes by computing quantile thresholds; defaults to _rdylbu_
- _quantize_ \- discretizes by computing uniform thresholds; defaults to _rdylbu_ [^0.4.3](https://github.com/observablehq/plot/releases/tag/v0.4.3 "added in v0.4.3")
- _diverging_ \- like _linear_, but with a pivot; defaults to _rdbu_
- _diverging-log_ \- like _log_, but with a pivot that defaults to 1; defaults to _rdbu_
- _diverging-pow_ \- like _pow_, but with a pivot; defaults to _rdbu_
- _diverging-sqrt_ \- like _sqrt_, but with a pivot; defaults to _rdbu_
- _diverging-symlog_ \- like _symlog_, but with a pivot; defaults to _rdbu_

For a _threshold_ scale, the **domain** represents _n_ (typically numeric) thresholds which will produce a **range** of _n_ \+ 1 output colors; the _i_ th color of the **range** applies to values that are smaller than the _i_ th element of the domain and larger or equal to the _i_ \- 1th element of the domain. For a _quantile_ scale, the **domain** represents all input values to the scale, and the **n** option specifies how many quantiles to compute from the **domain**; **n** quantiles will produce **n** \- 1 thresholds, and an output range of **n** colors. For a _quantize_ scale, the domain will be transformed into approximately **n** quantized values, where **n** is an option that defaults to 5.

By default, all diverging color scales are symmetric around the pivot; set **symmetric** to false if you want to cover the whole extent on both sides.

Color scales support two additional options:

- **scheme** \- a named color scheme in lieu of a range, such as _reds_
- **interpolate** \- in conjunction with a range, how to interpolate colors

For quantile and quantize color scales, the **scheme** option is used in conjunction with **n**, which determines how many quantiles or quantized values to compute, and thus the number of elements in the scale’s range; it defaults to 5 (for quintiles in the case of a quantile scale).

The following sequential scale schemes are supported for both quantitative and ordinal data:

BluesBuGnBuPuCividisCoolCubehelixGnBuGreensGreysInfernoMagmaOrRdOrangesPlasmaPuBuPuBuGnPuRdPurplesRdPuRedsTurboViridisWarmYlGnYlGnBuYlOrBrYlOrRd

js

```
Plot.plot({
  width: 322,
  height: 25 * 27,
  margin: 0,
  marginRight: 70,
  padding: 0,
  x: {axis: null},
  y: {axis: "right", tickSize: 0},
  color: {type: "identity"},
  marks: [\
    Plot.cell([\
      ["Blues", d3.interpolateBlues],\
      ["Greens", d3.interpolateGreens],\
      ["Greys", d3.interpolateGreys],\
      ["Purples", d3.interpolatePurples],\
      ["Reds", d3.interpolateReds],\
      ["Oranges", d3.interpolateOranges],\
      ["Turbo", d3.interpolateTurbo],\
      ["Viridis", d3.interpolateViridis],\
      ["Magma", d3.interpolateMagma],\
      ["Inferno", d3.interpolateInferno],\
      ["Plasma", d3.interpolatePlasma],\
      ["Cividis", d3.interpolateCividis],\
      ["Cubehelix", d3.interpolateCubehelixDefault],\
      ["Warm", d3.interpolateWarm],\
      ["Cool", d3.interpolateCool],\
      ["BuGn", d3.interpolateBuGn],\
      ["BuPu", d3.interpolateBuPu],\
      ["GnBu", d3.interpolateGnBu],\
      ["OrRd", d3.interpolateOrRd],\
      ["PuBuGn", d3.interpolatePuBuGn],\
      ["PuBu", d3.interpolatePuBu],\
      ["PuRd", d3.interpolatePuRd],\
      ["RdPu", d3.interpolateRdPu],\
      ["YlGnBu", d3.interpolateYlGnBu],\
      ["YlGn", d3.interpolateYlGn],\
      ["YlOrBr", d3.interpolateYlOrBr],\
      ["YlOrRd", d3.interpolateYlOrRd],\
    ].flatMap(([name, i]) => d3.ticks(0, 1, 20).map((t) => [t, name, String(i(t))])), {fill: "2", insetTop: 0.5, insetBottom: 0.5})\
  ]
})
```

The default color scheme, _turbo_, was chosen primarily to ensure high-contrast visibility. Color schemes such as _blues_ make low-value marks difficult to see against a white background, for better or for worse. To use a subset of a continuous color scheme (or any single-argument _interpolate_ function), set the _scale_.range property to the corresponding subset of \[0, 1\]; for example, to use the first half of the _rainbow_ color scheme, use a range of \[0, 0.5\]. By default, the full range \[0, 1\] is used. If you wish to encode a quantitative value without hue, consider using _opacity_ rather than _color_ (e.g., use Plot.dot’s _strokeOpacity_ instead of _stroke_).

The following diverging scale schemes are supported:

BrBGBuRdBuYlRdPRGnPiYGPuOrRdBuRdGyRdYlBuRdYlGnSpectral

js

```
Plot.plot({
  width: 322,
  height: 25 * 11,
  margin: 0,
  marginRight: 70,
  padding: 0,
  x: {axis: null},
  y: {axis: "right", tickSize: 0},
  color: {type: "identity"},
  marks: [\
    Plot.cell([\
      ["BrBG", d3.interpolateBrBG],\
      ["PRGn", d3.interpolatePRGn],\
      ["PiYG", d3.interpolatePiYG],\
      ["PuOr", d3.interpolatePuOr],\
      ["RdBu", d3.interpolateRdBu],\
      ["RdGy", d3.interpolateRdGy],\
      ["RdYlBu", d3.interpolateRdYlBu],\
      ["RdYlGn", d3.interpolateRdYlGn],\
      ["Spectral", d3.interpolateSpectral],\
      ["BuRd", (t) => d3.interpolateRdBu(1 - t)],\
      ["BuYlRd", (t) => d3.interpolateRdYlBu(1 - t)],\
    ].flatMap(([name, i]) => d3.ticks(0, 1, 30).map((t) => [t, name, String(i(t))])), {fill: "2", insetTop: 0.5, insetBottom: 0.5})\
  ]
})
```

Picking a diverging color scheme name defaults the scale type to _diverging_; set the scale type to _linear_ to treat the color scheme as sequential instead. Diverging color scales support a _scale_. **pivot** option, which defaults to zero. Values below the pivot will use the lower half of the color scheme ( _e.g._, reds for the _rdgy_ scheme), while values above the pivot will use the upper half (grays for _rdgy_).

The following cylical color schemes are supported:

rainbowsinebow

js

```
Plot.plot({
  width: 322,
  height: 25 * 2,
  margin: 0,
  marginRight: 70,
  padding: 0,
  x: {axis: null},
  y: {axis: "right", tickSize: 0},
  color: {type: "identity"},
  marks: [\
    Plot.cell([\
      ["rainbow", d3.interpolateRainbow],\
      ["sinebow", d3.interpolateSinebow],\
    ].flatMap(([name, i]) => d3.ticks(0, 1, 30).map((t) => [t, name, String(i(t))])), {fill: "2", insetTop: 0.5, insetBottom: 0.5})\
  ]
})
```

The following categorical color schemes are supported:

AccentCategory10Dark2Observable10PairedPastel1Pastel2Set1Set2Set3Tableau10

js

```
Plot.plot({
  width: 322,
  height: 25 * 10,
  margin: 0,
  marginRight: 70,
  padding: 0,
  x: {axis: null},
  y: {axis: "right", tickSize: 0},
  color: {type: "identity"},
  marks: [\
    Plot.cell([\
      ["Accent", d3.schemeAccent],\
      ["Category10", d3.schemeCategory10],\
      ["Dark2", d3.schemeDark2],\
      ["Observable10", Plot.scale({color: {type: "categorical"}}).range],\
      ["Paired", d3.schemePaired],\
      ["Pastel1", d3.schemePastel1],\
      ["Pastel2", d3.schemePastel2],\
      ["Set1", d3.schemeSet1],\
      ["Set2", d3.schemeSet2],\
      ["Set3", d3.schemeSet3],\
      ["Tableau10", d3.schemeTableau10],\
    ].flatMap(([name, scheme]) => scheme.map((s, i) => [i, name, s])), {fill: "2", inset: 0.5})\
  ]
})
```

The following color interpolators are supported:

- _rgb_ \- RGB (red, green, blue)
- _hsl_ \- HSL (hue, saturation, lightness)
- _lab_ \- CIELAB ( _a.k.a._ “Lab”)
- _hcl_ \- CIELChab ( _a.k.a._ “LCh” or “HCL”)

### Position scale options [​](https://observablehq.com/plot/features/scales\#position-scale-options)

The position scales ( _x_, _y_, _fx_, and _fy_) support additional options:

- **inset** \- inset the default range by the specified amount in pixels
- **round** \- round the output value to the nearest integer (whole pixel)

The _x_ and _fx_ scales support asymmetric insets for more precision. Replace inset by:

- **insetLeft** \- insets the start of the default range by the specified number of pixels
- **insetRight** \- insets the end of the default range by the specified number of pixels

Similarly, the _y_ and _fy_ scales support asymmetric insets with:

- **insetTop** \- insets the top of the default range by the specified number of pixels
- **insetBottom** \- insets the bottom of the default range by the specified number of pixels

The inset scale options can provide “breathing room” to separate marks from axes or the plot’s edge. For example, in a scatterplot with a Plot.dot with the default 3-pixel radius and 1.5-pixel stroke width, an inset of 5 pixels prevents dots from overlapping with the axes. The _scale_.round option is useful for crisp edges by rounding to the nearest pixel boundary.

In addition to the generic _ordinal_ scale type, which requires an explicit output range value for each input domain value, Plot supports special _point_ and _band_ scale types for encoding ordinal data as position. These scale types accept a \[ _min_, _max_\] range similar to quantitative scales, and divide this continuous interval into discrete points or bands based on the number of distinct values in the domain ( _i.e._, the domain’s cardinality). If the associated marks have no effective width along the ordinal dimension — such as a dot, rule, or tick — then use a _point_ scale; otherwise, say for a bar, use a _band_ scale.

Ordinal position scales support additional options, all specified as proportions in \[0, 1\]:

- **padding** \- how much of the range to reserve to inset first and last point or band
- **align** \- where to distribute points or bands (0 = at start, 0.5 = at middle, 1 = at end)

For a _band_ scale, you can further fine-tune padding:

- **paddingInner** \- how much of the range to reserve to separate adjacent bands
- **paddingOuter** \- how much of the range to reserve to inset first and last band

Align defaults to 0.5 (centered). Band scale padding defaults to 0.1 (10% of available space reserved for separating bands), while point scale padding defaults to 0.5 (the gap between the first point and the edge is half the distance of the gap between points, and likewise for the gap between the last point and the opposite edge). Note that rounding and mark insets (e.g., for bars and rects) also affect separation between adjacent marks.

Plot implicitly generates an [axis mark](https://observablehq.com/plot/marks/axis) for position scales if one is not explicitly declared. (For more control, declare the axis mark explicitly.) The following [axis mark options](https://observablehq.com/plot/marks/axis#axis-options) are also available as scale options, applying to the implicit axis:

- **axis** \- the axis **anchor**: _top_, _bottom_ ( _x_ or _fx_); _left_, _right_ ( _y_ or _fy_); _both_; null to suppress
- **ticks** \- the approximate number of ticks to generate, or interval, or array of values
- **tickSpacing** \- the approximate number of pixels between ticks (if **ticks** is not specified)
- **tickSize** \- the length of each tick (in pixels; default 6 for _x_ and _y_, or 0 for _fx_ and _fy_)
- **tickPadding** \- the separation between the tick and its label (in pixels; default 3)
- **tickFormat** \- either a function or specifier string to format tick values; see [Formats](https://observablehq.com/plot/features/formats)
- **tickRotate** \- whether to rotate tick labels (an angle in degrees clockwise; default 0)
- **fontVariant** \- the font-variant attribute; defaults to _tabular-nums_ if quantitative
- **label** \- a string to label the axis
- **labelAnchor** \- the label anchor: _top_, _right_, _bottom_, _left_, or _center_
- **labelArrow** \- the label arrow: _auto_ (default), _up_, _right_, _down_, _left_, _none_, or true [^0.6.7](https://github.com/observablehq/plot/releases/tag/v0.6.7 "added in v0.6.7")
- **labelOffset** \- the label position offset (in pixels; default depends on margins and orientation)
- **ariaLabel** \- a short label representing the axis in the accessibility tree
- **ariaDescription** \- a textual description for the axis

For an implicit [grid mark](https://observablehq.com/plot/marks/grid), use the **grid** option. For an implicit [frame mark](https://observablehq.com/plot/marks/frame) along one edge of the frame, use the **line** option.

- **grid** \- whether to draw grid lines across the plot for each tick
- **line** \- if true, draw the axis line (only for _x_ and _y_)

Top-level options are also supported as shorthand: **grid** (for _x_ and _y_ only; see [facets](https://observablehq.com/plot/features/facets)), **label**, **axis**, **inset**, **round**, **align**, and **padding**. If the **grid** option is true, show a grid using _currentColor_; if specified as a string, show a grid with the specified color; if an approximate number of ticks, an interval, or an array of tick values, show corresponding grid lines.

## Sort mark option [^0.2.0](https://github.com/observablehq/plot/releases/tag/v0.2.0 "added in v0.2.0") [​](https://observablehq.com/plot/features/scales\#sort-mark-option)

If an ordinal scale’s domain is not set, it defaults to natural ascending order; to order the domain by associated values in another dimension, either compute the domain manually (consider [d3.groupSort](https://d3js.org/d3-array/group#groupSort)) or use an associated mark’s **sort** option. For example, to sort bars by ascending frequency rather than alphabetically by letter:

js

```
Plot.barY(alphabet, {x: "letter", y: "frequency", sort: {x: "y"}})
```

The sort option is an object whose keys are ordinal scale names, such as _x_ or _fx_, and whose values are mark channel names, such as **y**, **y1**, or **y2**. By specifying an existing channel rather than a new value, you avoid repeating the order definition and can refer to channels derived by [transforms](https://observablehq.com/plot/features/transforms) (such as [stack](https://observablehq.com/plot/transforms/stack) or [bin](https://observablehq.com/plot/transforms/bin)). When sorting the _x_ domain, if no **x** channel is defined, **x2** will be used instead if available, and similarly for _y_ and **y2**; this is useful for marks that implicitly stack such as [area](https://observablehq.com/plot/marks/area), [bar](https://observablehq.com/plot/marks/bar), and [rect](https://observablehq.com/plot/marks/rect). A sort value may also be specified as _width_ or _height_ [^0.4.2](https://github.com/observablehq/plot/releases/tag/v0.4.2 "added in v0.4.2"), representing derived channels \| _x2_ \- _x1_ \| and \| _y2_ \- _y1_ \| respectively.

Note that there may be multiple associated values in the secondary dimension for a given value in the primary ordinal dimension. The secondary values are therefore grouped for each associated primary value, and each group is then aggregated by applying a reducer. The default reducer is _max_, but may be changed by specifying the **reduce** option. Lastly the primary values are by default sorted based on the associated reduced value in natural ascending order to produce the domain. The above code is shorthand for:

js

```
Plot.barY(alphabet, {x: "letter", y: "frequency", sort: {x: "y", reduce: "max", order: "ascending"}})
```

Generally speaking, a reducer only needs to be specified when there are multiple secondary values for a given primary value. See the [group transform](https://observablehq.com/plot/transforms/group) for the list of supported reducers.

For descending rather than ascending order, set the **order** option to _descending_:

js

```
Plot.barY(alphabet, {x: "letter", y: "frequency", sort: {x: "y", order: "descending"}})
```

Alternatively, the _-channel_ shorthand option, which changes the default **order** to _descending_:

js

```
Plot.barY(alphabet, {x: "letter", y: "frequency", sort: {x: "-y"}})
```

Setting **order** to null will disable sorting, preserving the order of the data. (When an aggregating transform is used, such as [group](https://observablehq.com/plot/transforms/group) or [bin](https://observablehq.com/plot/transforms/bin), note that the data may already have been sorted and thus the order may differ from the input data.)

Alternatively, set the **reverse** option to true. This produces a different result than descending order for null or unorderable values: descending order puts nulls last, whereas reversed ascending order puts nulls first.

js

```
Plot.barY(alphabet, {x: "letter", y: "frequency", sort: {x: "y", reverse: true}})
```

An additional **limit** option truncates the domain to the first _n_ values after ordering. If **limit** is negative, the last _n_ values are used instead. Hence, a positive **limit** with **reverse** = true will return the top _n_ values in descending order. If **limit** is an array \[ _lo_, _hi_\], the _i_ th values with _lo_ ≤ _i_ < _hi_ will be selected. (Note that like the [basic filter transform](https://observablehq.com/plot/transforms/filter), limiting the _x_ domain here does not affect the computation of the _y_ domain, which is computed independently without respect to filtering.)

js

```
Plot.barY(alphabet, {x: "letter", y: "frequency", sort: {x: "y", limit: 5}})
```

If different sort options are needed for different ordinal scales, the channel name can be replaced with a _value_ object with additional per-scale options.

js

```
Plot.barY(alphabet, {x: "letter", y: "frequency", sort: {x: {value: "y", order: "descending"}}})
```

If the input channel is _data_, then the reducer is passed groups of the mark’s data; this is typically used in conjunction with a custom reducer function, as when the built-in single-channel reducers are insufficient.

Note: when the value of the sort option is a string or a function, it is interpreted as a mark [sort transform](https://observablehq.com/plot/transforms/sort). To use both sort options and a mark sort transform, use [Plot.sort](https://observablehq.com/plot/transforms/sort#sort).

## scale( _options_) [^0.4.0](https://github.com/observablehq/plot/releases/tag/v0.4.0 "added in v0.4.0") [​](https://observablehq.com/plot/features/scales\#scale)

You can also create a standalone scale with Plot. **scale**( _options_). The _options_ object must define at least one scale; see [Scale options](https://observablehq.com/plot/features/scales#scale-options) for how to define a scale. For example, here is a categorical color scale with the _Tableau10_ color scheme and a domain of fruits:

js

```
const color = Plot.scale({color: {scheme: "Tableau10", domain: ["apple", "orange", "pear"]}});
```

Both [_plot_.scale](https://observablehq.com/plot/features/plots#plot_scale) and [Plot.scale](https://observablehq.com/plot/features/scales#scale) return scale objects. These objects represent the actual (or “materialized”) scale options used by Plot, including the domain, range, interpolate function, _etc._ The scale’s label, if any, is also returned; however, note that other axis properties are not currently exposed. Point and band scales also expose their materialized bandwidth and step.

js

```
color.domain // ["apple", "orange", "pear"]
```

For convenience, scale objects expose a _scale_. **apply**( _input_) method which returns the scale’s output for the given _input_ value. When applicable, scale objects also expose a _scale_. **invert**( _output_) method which returns the corresponding input value from the scale’s domain for the given _output_ value.

js

```
color.apply("apple") // "#4e79a7"
```

To apply a standalone scale object to a plot, pass it to Plot.plot as the corresponding scale options, such as **color**:

01234

js

```
Plot.cellX(["apple", "apple", "orange", "pear", "orange"]).plot({color})
```

As another example, below are two plots with different options where the second plot uses the _color_ scale from the first plot:

js

```
const plot1 = Plot.plot({...options1});
const plot2 = Plot.plot({...options2, color: plot1.scale("color")});
```

Pager

[Previous pageMarks](https://observablehq.com/plot/features/marks)

[Next pageProjections](https://observablehq.com/plot/features/projections)

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

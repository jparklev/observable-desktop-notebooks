---
url: "https://observablehq.com/plot/transforms/bin"
title: "Bin transform | Plot"
---

# Bin transform [​](https://observablehq.com/plot/transforms/bin\#bin-transform)

TIP

The bin transform is for aggregating quantitative or temporal data. For ordinal or nominal data, use the [group transform](https://observablehq.com/plot/transforms/group). See also the [hexbin transform](https://observablehq.com/plot/transforms/hexbin).

The **bin transform** groups quantitative or temporal data — continuous measurements such as heights, weights, or temperatures — into discrete bins. You can then compute summary statistics for each bin, such as a count, sum, or proportion. The bin transform is most often used to make histograms or heatmaps with the [rect mark](https://observablehq.com/plot/marks/rect).

For example, here is a histogram showing the distribution of weights of Olympic athletes.

050100150200250300350400450500550600↑ Frequency406080100120140160weight → [Fork](https://observablehq.com/@observablehq/plot-a-simple-histogram "Open on Observable")

js

```
Plot.plot({
  y: {grid: true},
  marks: [\
    Plot.rectY(olympians, Plot.binX({y: "count"}, {x: "weight"})),\
    Plot.ruleY([0])\
  ]
})
```

The binX transform takes **x** as input and outputs **x1** and **x2** representing the extent of each bin in _x_. The _outputs_ argument (here `{y: "count"}`) declares additional output channels ( **y**) and the associated reducer ( _count_). Hence the height of each rect above represents the number of athletes in the corresponding bin, _i.e._, the number of athletes with a similar weight.

While the binX transform is often used to generate **y**, it can output any channel. Below, the **fill** channel represents count per bin, resulting in a one-dimensional heatmap.

406080100120140160weight → [Fork](https://observablehq.com/@observablehq/plot-color-bins "Open on Observable")

js

```
Plot
  .rect(olympians, Plot.binX({fill: "count"}, {x: "weight"}))
  .plot({color: {scheme: "YlGnBu"}})
```

You can partition bins using **z**. If **z** is undefined, it defaults to **fill** or **stroke**, if any. In conjunction with the rectY mark’s implicit [stackY transform](https://observablehq.com/plot/transforms/stack), this will produce a stacked histogram.

femalemale

050100150200250300350400450500550600↑ Frequency406080100120140160weight → [Fork](https://observablehq.com/@observablehq/plot-vertical-histogram "Open on Observable")

js

```
Plot.plot({
  y: {grid: true},
  color: {legend: true},
  marks: [\
    Plot.rectY(olympians, Plot.binX({y: "count"}, {x: "weight", fill: "sex"})),\
    Plot.ruleY([0])\
  ]
})
```

TIP

You can invoke the stack transform explicitly as `Plot.stackY(Plot.binX({y: "count"}, {x: "weight", fill: "sex"}))` to produce an identical chart.

You can opt-out of the implicit stackY transform by having binX generate **y1** or **y2** instead of **y** (and similarly **x1** or **x2** for stackX and binY). When overlapping marks, use either opacity or blending to make the overlap visible.

050100150200250300350400↑ Frequency406080100120140160weight → [Fork](https://observablehq.com/@observablehq/plot-overlapping-histogram "Open on Observable")

js

```
Plot.plot({
  y: {grid: true},
  marks: [\
    Plot.rectY(olympians, Plot.binX({y2: "count"}, {x: "weight", fill: "sex", mixBlendMode: "multiply"})),\
    Plot.ruleY([0])\
  ]
})
```

CAUTION

While the **mixBlendMode** option is useful for mitigating occlusion, it can be slow to render if there are many elements. More than two overlapping histograms may also be hard to read.

The bin transform comes in three orientations:

- [binX](https://observablehq.com/plot/transforms/bin#binX) bins on **x**, and often outputs **y** as in a histogram with vertical↑ rects;
- [binY](https://observablehq.com/plot/transforms/bin#binY) bins on **y**, and often outputs **x** as in a histogram with horizontal→ rects; and
- [bin](https://observablehq.com/plot/transforms/bin#bin) bins on both **x** and **y**, and often outputs to **fill** or **r** as in a heatmap.

As you might guess, the binY transform with the rectX mark produces a histogram with horizontal→ rects.

406080100120140160↑ weight0100200300400500600Frequency → [Fork](https://observablehq.com/@observablehq/plot-horizontal-histogram "Open on Observable")

js

```
Plot.plot({
  x: {grid: true},
  marks: [\
    Plot.rectX(olympians, Plot.binY({x: "count"}, {y: "weight"})),\
    Plot.ruleX([0])\
  ]
})
```

You can produce a two-dimensional heatmap with bin transform and a rect mark by generating a **fill** output channel. Below, color encodes the number of athletes in each bin (of similar height and weight).

1.21.31.41.51.61.71.81.92.02.12.2↑ height406080100120140160weight → [Fork](https://observablehq.com/@observablehq/plot-olympians-heatmap "Open on Observable")

js

```
Plot
  .rect(olympians, Plot.bin({fill: "count"}, {x: "weight", y: "height"}))
  .plot({color: {scheme: "YlGnBu"}})
```

The bin transform also outputs **x** and **y** channels representing bin centers. These can be used to place a [dot mark](https://observablehq.com/plot/marks/dot) whose size again represents the number of athletes in each bin.

1.31.41.51.61.71.81.92.02.12.2↑ height406080100120140160weight → [Fork](https://observablehq.com/@observablehq/plot-dot-heatmap "Open on Observable")

js

```
Plot.plot({
  r: {range: [0, 6]}, // generate slightly smaller dots
  marks: [\
    Plot.dot(olympians, Plot.bin({r: "count"}, {x: "weight", y: "height"}))\
  ]
})
```

We can add the **stroke** channel to show overlapping distributions by sex.

1.31.41.51.61.71.81.92.02.12.2↑ height406080100120140160weight → [Fork](https://observablehq.com/@observablehq/plot-dot-heatmap "Open on Observable")

js

```
Plot.plot({
  r: {range: [0, 6]},
  marks: [\
    Plot.dot(olympians, Plot.bin({r: "count"}, {x: "weight", y: "height", stroke: "sex"}))\
  ]
})
```

Similarly the binX and binY transforms generate respective **x** and **y** channels for one-dimensional binning.

406080100120140160weight → [Fork](https://observablehq.com/@observablehq/plot-dot-bins "Open on Observable")

js

```
Plot.plot({
  r: {range: [0, 14]},
  marks: [\
    Plot.dot(olympians, Plot.binX({r: "count"}, {x: "weight"}))\
  ]
})
```

In addition to rect and dot, you can even use continuous marks such as [area](https://observablehq.com/plot/marks/area) and [line](https://observablehq.com/plot/marks/line). In this case you should set the bin transform’s **filter** option to null so that empty bins are included in the output; otherwise, the area or line would mislead by interpolating over missing bins.

050100150200250300350400450500550600↑ Frequency406080100120140160weight → [Fork](https://observablehq.com/@observablehq/plot-density-estimation "Open on Observable")

js

```
Plot.plot({
  y: {grid: true},
  marks: [\
    Plot.areaY(olympians, Plot.binX({y: "count", filter: null}, {x: "weight", fillOpacity: 0.2})),\
    Plot.lineY(olympians, Plot.binX({y: "count", filter: null}, {x: "weight"})),\
    Plot.ruleY([0])\
  ]
})
```

The **cumulative** option produces a cumulative distribution. Below, each bin represents the number of athletes with the given weight _or less_. To have each bin represent the number of athletes with the given weight _or more_, set **cumulative** to −1.

Cumulative:  -1 (reverse) +1 (true)

01,0002,0003,0004,0005,0006,0007,0008,0009,00010,000↑ Frequency406080100120140160weight →

js

```
Plot.plot({
  marginLeft: 60,
  y: {grid: true},
  marks: [\
    Plot.rectY(olympians, Plot.binX({y: "count"}, {x: "weight", cumulative})),\
    Plot.ruleY([0])\
  ]
})
```

The bin transform works with Plot’s [faceting system](https://observablehq.com/plot/features/facets), partitioning bins by facet. Below, we compare the weight distributions of athletes within each sport using the _proportion-facet_ reducer. Sports are sorted by median weight: gymnasts tend to be the lightest, and basketball players the heaviest.

gymnasticstriathlonathleticstable tennismodern pentathloncyclingtaekwondobadmintonequestrianfootballhockeyweightliftingaquaticsgolfsailingfencingtennisjudoshootingarcherywrestlingrowingrugby sevenscanoevolleyballhandballbasketballsport406080100120140160weight →

js

```
Plot.plot({
  marginLeft: 100,
  padding: 0,
  x: {grid: true},
  fy: {domain: d3.groupSort(olympians.filter((d) => d.weight), (g) => d3.median(g, (d) => d.weight), (d) => d.sport)},
  color: {scheme: "YlGnBu"},
  marks: [Plot.rect(olympians, Plot.binX({fill: "proportion-facet"}, {x: "weight", fy: "sport", inset: 0.5}))]
})
```

The bin transform sets default insets for a one-pixel gap between rects. You can set explicit insets if you prefer, say if you want the rects to touch. In this case we recommend rounding on the _x_ scale to avoid antialiasing artifacts between rects.

050100150200250300350400450500550600↑ Frequency406080100120140160weight →

js

```
Plot.plot({
  x: {round: true},
  y: {grid: true},
  marks: [\
    Plot.rectY(olympians, Plot.binX({y: "count"}, {x: "weight", inset: 0})),\
    Plot.ruleY([0])\
  ]
})
```

## Bin options [​](https://observablehq.com/plot/transforms/bin\#bin-options)

Given input _data_ = \[ _d₀_, _d₁_, _d₂_, …\], by default the resulting binned data is an array of arrays where each inner array is a subset of the input data \[\[ _d₁_, _d₂_, …\], \[ _d₀_, …\], …\]. Each inner array is in input order. The outer array is in ascending order according to the associated dimension ( _x_ then _y_).

By specifying a reducer for the **data** output, as described below, you can change how the binned data is computed. The outputs may also include **filter** and **sort** options specified as reducers, and a **reverse** option to reverse the order of generated bins. By default, empty bins are omitted, and non-empty bins are generated in ascending threshold order.

In addition to data, the following channels are automatically output:

- **x1** \- the starting horizontal position of the bin
- **x2** \- the ending horizontal position of the bin
- **x** \- the horizontal center of the bin
- **y1** \- the starting vertical position of the bin
- **y2** \- the ending vertical position of the bin
- **y** \- the vertical center of the bin
- **z** \- the first value of the _z_ channel, if any
- **fill** \- the first value of the _fill_ channel, if any
- **stroke** \- the first value of the _stroke_ channel, if any

The **x1**, **x2**, and **x** output channels are only computed by the binX and bin transform; similarly the **y1**, **y2**, and **y** output channels are only computed by the binY and bin transform. The **x** and **y** output channels are lazy: they are only computed if needed by a downstream mark or transform. Conversely, the **x1** and **x2** outputs default to undefined if **x** is explicitly defined; and the **y1** and **y2** outputs default to undefined if **y** is explicitly defined.

You can declare additional output channels by specifying the channel name and desired reducer in the _outputs_ object which is the first argument to the transform. For example, to use binX to generate a **y** channel of bin counts as in a frequency histogram:

js

```
Plot.binX({y: "count"}, {x: "culmen_length_mm"})
```

The following named reducers are supported:

- _first_ \- the first value, in input order
- _last_ \- the last value, in input order
- _count_ \- the number of elements (frequency)
- _distinct_ \- the number of distinct values
- _sum_ \- the sum of values
- _proportion_ \- the sum proportional to the overall total (weighted frequency)
- _proportion-facet_ \- the sum proportional to the facet total
- _min_ \- the minimum value
- _min-index_ \- the zero-based index of the minimum value
- _max_ \- the maximum value
- _max-index_ \- the zero-based index of the maximum value
- _mean_ \- the mean value (average)
- _median_ \- the median value
- _mode_ \- the value with the most occurrences
- _pXX_ \- the percentile value, where XX is a number in \[00,99\]
- _deviation_ \- the standard deviation
- _variance_ \- the variance per [Welford’s algorithm](https://en.wikipedia.org/wiki/Algorithms_for_calculating_variance#Welford's_online_algorithm)
- _identity_ \- the array of values
- _x_ \- the middle of the bin’s _x_ extent (when binning on _x_)
- _x1_ \- the lower bound of the bin’s _x_ extent (when binning on _x_)
- _x2_ \- the upper bound of the bin’s _x_ extent (when binning on _x_)
- _y_ \- the middle of the bin’s _y_ extent (when binning on _y_)
- _y1_ \- the lower bound of the bin’s _y_ extent (when binning on _y_)
- _y2_ \- the upper bound of the bin’s _y_ extent (when binning on _y_)
- _z_ [^0.6.14](https://github.com/observablehq/plot/releases/tag/v0.6.14 "added in v0.6.14") \- the bin’s _z_ value ( _z_, _fill_, or _stroke_)

In addition, a reducer may be specified as:

- a function to be passed the array of values for each bin and the extent of the bin
- an object with a **reduceIndex** method, and optionally a **scope**

In the last case, the **reduceIndex** method is repeatedly passed three arguments: the index for each bin (an array of integers), the input channel’s array of values, and the extent of the bin (an object {data, x1, x2, y1, y2}); it must then return the corresponding aggregate value for the bin.

If the reducer object’s **scope** is _data_, then the **reduceIndex** method is first invoked for the full data; the return value of the **reduceIndex** method is then made available as a third argument (making the extent the fourth argument). Similarly if the **scope** is _facet_, then the **reduceIndex** method is invoked for each facet, and the resulting reduce value is made available while reducing the facet’s bins. (This optional **scope** is used by the _proportion_ and _proportion-facet_ reducers.)

Most reducers require binding the output channel to an input channel; for example, if you want the **y** output channel to be a _sum_ (not merely a count), there should be a corresponding **y** input channel specifying which values to sum. If there is not, _sum_ will be equivalent to _count_.

js

```
Plot.binX({y: "sum"}, {x: "culmen_length_mm", y: "body_mass_g"})
```

You can control whether a channel is computed before or after binning. If a channel is declared only in _options_ (and it is not a special group-eligible channel such as **x**, **y**, **z**, **fill**, or **stroke**), it will be computed after binning and be passed the binned data: each datum is the array of input data corresponding to the current bin.

js

```
Plot.binX({y: "count"}, {x: "economy (mpg)", title: (data) => data.map((d) => d.name).join("\n")})
```

This is equivalent to declaring the channel only in _outputs_.

js

```
Plot.binX({y: "count", title: (data) => data.map((d) => d.name).join("\n")}, {x: "economy (mpg)"})
```

However, if a channel is declared in both _outputs_ and _options_, then the channel in _options_ is computed before binning and can then be aggregated using any built-in reducer (or a custom reducer function) during the bin transform.

js

```
Plot.binX({y: "count", title: (names) => names.join("\n")}, {x: "economy (mpg)", title: "name"})
```

To control how the quantitative dimensions _x_ and _y_ are divided into bins, the following options are supported:

- **thresholds** \- the threshold values; see below
- **interval** \- an alternative method of specifying thresholds
- **domain** \- values outside the domain will be omitted
- **cumulative** \- if positive, each bin will contain all lesser bins

These options may be specified either on the _options_ or _outputs_ object. If the **domain** option is not specified, it defaults to the minimum and maximum of the corresponding dimension ( _x_ or _y_), possibly niced to match the threshold interval to ensure that the first and last bin have the same width as other bins. If **cumulative** is negative (-1 by convention), each bin will contain all _greater_ bins rather than all _lesser_ bins, representing the [complementary cumulative distribution](https://en.wikipedia.org/wiki/Cumulative_distribution_function#Complementary_cumulative_distribution_function_.28tail_distribution.29).

To pass separate binning options for **x** and **y**, use an object with the options above and a **value** option to specify the input channel values.

js

```
Plot.binX({y: "count"}, {x: {thresholds: 20, value: "culmen_length_mm"}})
```

The **thresholds** option may be specified as a named method or a variety of other ways:

- _auto_ (default) - Scott’s rule, capped at 200
- _freedman-diaconis_ \- the [Freedman–Diaconis rule](https://en.wikipedia.org/wiki/Freedman%E2%80%93Diaconis_rule)
- _scott_ \- [Scott’s normal reference rule](https://en.wikipedia.org/wiki/Histogram#Scott.27s_normal_reference_rule)
- _sturges_ \- [Sturges’ formula](https://en.wikipedia.org/wiki/Histogram#Sturges.27_formula)
- a count (hint) representing the desired number of bins
- an array of _n_ threshold values for _n_ \- 1 bins
- an interval or time interval (for temporal binning; see below)
- a function that returns an array, count, or time interval

If the **thresholds** option is specified as a function, it is passed three arguments: the array of input values, the domain minimum, and the domain maximum. If a number, [d3.ticks](https://d3js.org/d3-array/ticks) or [d3.utcTicks](https://d3js.org/d3-time#utcTicks) is used to choose suitable nice thresholds. If an interval, it must expose an _interval_.floor( _value_), _interval_.ceil( _value_), _interval_.offset( _value_), and _interval_.range( _start_, _stop_) methods. If the interval is a time interval such as "day" (equivalently, d3.utcDay), or if the thresholds are specified as an array of dates, then the binned values are implicitly coerced to dates. Time intervals are intervals that are also functions that return a Date instance when called with no arguments.

If the **interval** option is used instead of **thresholds**, it may be either an interval, a time interval, or a number. If a number _n_, threshold values are consecutive multiples of _n_ that span the domain; otherwise, the **interval** option is equivalent to the **thresholds** option. When the thresholds are specified as an interval, and the default **domain** is used, the domain will automatically be extended to start and end to align with the interval.

The bin transform supports grouping in addition to binning: you can subdivide bins by up to two additional ordinal or categorical dimensions (not including faceting). If any of **z**, **fill**, or **stroke** is a channel, the first of these channels will be used to subdivide bins. Similarly, binX will group on **y** if **y** is not an output channel, and binY will group on **x** if **x** is not an output channel. For example, for a stacked histogram:

js

```
Plot.binX({y: "count"}, {x: "body_mass_g", fill: "species"})
```

Lastly, the bin transform changes the default [mark insets](https://observablehq.com/plot/features/marks#mark-options): binX changes the defaults for **insetLeft** and **insetRight**; binY changes the defaults for **insetTop** and **insetBottom**; bin changes all four.

## bin( _outputs_, _options_) [​](https://observablehq.com/plot/transforms/bin\#bin)

js

```
Plot.rect(olympians, Plot.bin({fill: "count"}, {x: "weight", y: "height"}))
```

Bins on **x** and **y**. Also groups on the first channel of **z**, **fill**, or **stroke**, if any.

## binX( _outputs_, _options_) [​](https://observablehq.com/plot/transforms/bin\#binX)

js

```
Plot.rectY(olympians, Plot.binX({y: "count"}, {x: "weight"}))
```

Bins on **x**. Also groups on **y** and the first channel of **z**, **fill**, or **stroke**, if any.

## binY( _outputs_, _options_) [​](https://observablehq.com/plot/transforms/bin\#binY)

js

```
Plot.rectX(olympians, Plot.binY({x: "count"}, {y: "weight"}))
```

Bins on **y**. Also groups on **x** and first channel of **z**, **fill**, or **stroke**, if any.

Pager

[Previous pageWaffle](https://observablehq.com/plot/marks/waffle)

[Next pageCentroid](https://observablehq.com/plot/transforms/centroid)

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

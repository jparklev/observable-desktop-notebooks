---
url: "https://observablehq.com/plot/transforms/window"
title: "Window transform | Plot"
---

# Window transform [​](https://observablehq.com/plot/transforms/window\#window-transform)

The **window transform** is a specialized [map transform](https://observablehq.com/plot/transforms/map) that computes a moving window and then derives summary statistics from the current window, say to compute rolling averages, rolling minimums, or rolling maximums.

For example, the band chart below shows the daily high and low temperature in San Francisco. The red line represents the 7-day average high, and the blue line the 7-day average low.

Window size (k):7

404550556065707580↑ Temperature (°F)Oct2010Jan2011AprJulOctJan2012AprJulOct [Fork](https://observablehq.com/@observablehq/plot-window-line-area "Open on Observable")

js

```
Plot.plot({
  y: {
    grid: true,
    label: "Temperature (°F)"
  },
  marks: [\
    Plot.areaY(sftemp, {x: "date", y1: "low", y2: "high", fillOpacity: 0.3}),\
    Plot.lineY(sftemp, Plot.windowY(k, {x: "date", y: "low", stroke: "blue"})),\
    Plot.lineY(sftemp, Plot.windowY(k, {x: "date", y: "high", stroke: "red"}))\
  ]
})
```

The **k** option specifies the window size: the number of consecutive elements in the rolling window. A larger window for the rolling mean above produces a smoother curve.

The **anchor** specifies how to align the rolling window with the data. If _middle_ (the default), the window is centered around the current data point; for time-series data, this means the window will incorporate values from the future as well as the past. Setting **anchor** to _end_ will compute a trailing moving average.

Anchor:  start  middle  end

4550556065707580↑ Temperature (°F)Oct2010Jan2011AprJulOctJan2012AprJulOct [Fork](https://observablehq.com/@observablehq/plot-window-anchor "Open on Observable")

js

```
Plot.plot({
  y: {
    grid: true,
    label: "Temperature (°F)"
  },
  marks: [\
    Plot.lineY(sftemp, {x: "date", y: "high", strokeOpacity: 0.3}),\
    Plot.lineY(sftemp, Plot.windowY({k: 28, anchor}, {x: "date", y: "high"}))\
  ]
})
```

The window transform uses input order, not natural order by value, to determine the meaning of _start_ and _end_. When the data is in reverse chronological order, the meaning of _start_ and _end_ is effectively reversed because the first data point is the most recent. Use a [sort transform](https://observablehq.com/plot/transforms/sort) to change the order as needed.

If **strict** is false (the default), the window size is effectively reduced at the start or end of each series or both, depending on the **anchor**. Values computed with a truncated window may be noisy; if you would prefer to not show this data instead, set the **strict** option to true. [^0.6.0](https://github.com/observablehq/plot/releases/tag/v0.6.0 "added in v0.6.0") The **strict** option can also have a dramatic effect if some data is missing: when strict, the reducer will be skipped if any of the values in the current window are null, undefined, or NaN.

Strict:

38404244464850525456586062↑ Temperature (°F)Oct2010Jan2011AprJulOctJan2012AprJulOct [Fork](https://observablehq.com/@observablehq/plot-window-anchor "Open on Observable")

js

```
Plot.plot({
  y: {
    grid: true,
    label: "Temperature (°F)"
  },
  marks: [\
    Plot.lineY(sftemp, {x: "date", y: "low", strokeOpacity: 0.3}),\
    Plot.lineY(sftemp, Plot.windowY({k: 28, anchor: "end", strict}, {x: "date", y: "low"}))\
  ]
})
```

The **reduce** option specifies how to compute the output value for the current window. It defaults to _mean_ for a rolling average. Below, the rolling minimum, maximum, and median are shown. The window transform supports most of the same reducers as [bin](https://observablehq.com/plot/transforms/bin) and [group](https://observablehq.com/plot/transforms/group), and you can implement a custom reducer as a function if needed.

38404244464850525456586062↑ Temperature (°F)Oct2010Jan2011AprJulOctJan2012AprJulOct [Fork](https://observablehq.com/@observablehq/plot-window-reduce "Open on Observable")

js

```
Plot.plot({
  y: {
    grid: true,
    label: "Temperature (°F)"
  },
marks: [\
    Plot.lineY(sftemp, {x: "date", y: "low", strokeOpacity: 0.3}),\
    Plot.lineY(sftemp, Plot.windowY({k: 28, reduce: "min"}, {x: "date", y: "low", stroke: "blue"})),\
    Plot.lineY(sftemp, Plot.windowY({k: 28, reduce: "max"}, {x: "date", y: "low", stroke: "red"})),\
    Plot.lineY(sftemp, Plot.windowY({k: 28, reduce: "median"}, {x: "date", y: "low"}))\
  ]
})
```

While the windowY transform derives **y** (and **y1** and **y2**), and the windowX transform likewise derives **x**, **x1**, and **x2**, you can use the [map transform](https://observablehq.com/plot/transforms/map) directly for other channels. For example, the chart below uses a variable **stroke** to encode slope: the monthly change in unemployment rate for each metropolitan division. The slope is computed with a window of size 2 and the _difference_ reducer.

0246810121416↑ unemployment2000200220042006200820102012 [Fork](https://observablehq.com/@observablehq/plot-window-and-map "Open on Observable")

js

```
Plot.plot({
  y: {grid: true},
  color: {scheme: "BuYlRd", domain: [-0.5, 0.5]},
  marks: [\
    Plot.ruleY([0]),\
    Plot.lineY(\
      bls,\
      Plot.map(\
        {stroke: Plot.window({k: 2, reduce: "difference"})},\
        {x: "date", y: "unemployment", z: "division", stroke: "unemployment"}\
      )\
    ),\
  ]
})
```

As shown above, the window transform also understands the **z** channel: each metropolitan division is treated as a separate series.

## Window options [​](https://observablehq.com/plot/transforms/window\#window-options)

The window transform supports the following options:

- **k** \- the window size (the number of elements in the window)
- **anchor** \- how to align the window: _start_, _middle_ (default), or _end_
- **reduce** \- the window reducer; defaults to _mean_
- **strict** \- if true, output undefined if any window value is undefined; defaults to false

If the **strict** option is false (the default), the window will be automatically truncated as needed, and undefined input values are ignored. For example, if **k** is 24 and **anchor** is _middle_, then the initial 11 values have effective window sizes of 13, 14, 15, … 23, and likewise the last 12 values have effective window sizes of 23, 22, 21, … 12. Values computed with a truncated window may be noisy; if you would prefer to not show this data, set the **strict** option to true.

If the **strict** option is true, the output start values or end values or both (depending on the **anchor**) of each series may be undefined since there are not enough elements to create a window of size **k**; output values may also be undefined if some of the input values in the corresponding window are undefined.

The following named reducers are supported:

- _min_ \- the minimum
- _max_ \- the maximum
- _mean_ \- the mean (average)
- _median_ \- the median
- _mode_ \- the mode (most common occurrence)
- _pXX_ \- the percentile value, where XX is a number in \[00,99\]
- _sum_ \- the sum of values
- _deviation_ \- the standard deviation
- _variance_ \- the variance per [Welford’s algorithm](https://en.wikipedia.org/wiki/Algorithms_for_calculating_variance#Welford's_online_algorithm)
- _difference_ \- the difference between the last and first window value
- _ratio_ \- the ratio of the last and first window value
- _first_ \- the first value
- _last_ \- the last value

A reducer may also be specified as a function to be passed an index of size **k** and the corresponding input channel array; or if the function only takes one argument, an array of **k** values.

## window( _k_) [^0.2.3](https://github.com/observablehq/plot/releases/tag/v0.2.3 "added in v0.2.3") [​](https://observablehq.com/plot/transforms/window\#window)

js

```
Plot.map({y: Plot.window(24)}, {x: "Date", y: "Close", stroke: "Symbol"})
```

Returns a window map method for the given window size _k_, suitable for use with Plot.map. For additional options to the window transform, replace the number _k_ with an object with properties **k**, **anchor**, **reduce**, or **strict**.

## windowX( _k_, _options_) [​](https://observablehq.com/plot/transforms/window\#windowX)

js

```
Plot.windowX(24, {y: "Date", x: "Anomaly"})
```

Like [mapX](https://observablehq.com/plot/transforms/map#mapX), but applies the window map method with the given window size _k_. For additional options to the window transform, replace the number _k_ with an object with properties **k**, **anchor**, or **reduce**.

## windowY( _k_, _options_) [​](https://observablehq.com/plot/transforms/window\#windowY)

js

```
Plot.windowY(24, {x: "Date", y: "Anomaly"})
```

Like [mapY](https://observablehq.com/plot/transforms/map#mapY), but applies the window map method with the given window size _k_. For additional options to the window transform, replace the number _k_ with an object with properties **k**, **anchor**, or **reduce**.

Pager

[Previous pageTree](https://observablehq.com/plot/transforms/tree)

[Next pageCrosshair](https://observablehq.com/plot/interactions/crosshair)

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

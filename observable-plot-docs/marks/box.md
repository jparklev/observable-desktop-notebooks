---
url: "https://observablehq.com/plot/marks/box"
title: "Box mark | Plot"
---

# Box mark [^0.4.2](https://github.com/observablehq/plot/releases/tag/v0.4.2 "added in v0.4.2") [​](https://observablehq.com/plot/marks/box\#box-mark)

The **box mark** summarizes one-dimensional distributions as boxplots. It is a [composite mark](https://observablehq.com/plot/features/marks#marks) consisting of a [rule](https://observablehq.com/plot/marks/rule) to represent the extreme values (not including outliers), a [bar](https://observablehq.com/plot/marks/bar) to represent the interquartile range (trimmed to the data), a [tick](https://observablehq.com/plot/marks/tick) to represent the median value, and a [dot](https://observablehq.com/plot/marks/dot) to represent any outliers. The [group transform](https://observablehq.com/plot/transforms/group) is used to group and aggregate data.

For example, the boxplot below shows [A.A. Michelson’s experimental measurements](https://stat.ethz.ch/R-manual/R-devel/library/datasets/html/morley.html) of the speed of light. (Speed is in km/sec minus 299,000.)

6507007508008509009501,0001,050↑ Speed12345Expt [Fork](https://observablehq.com/@observablehq/plot-vertical-box-plot "Open on Observable")

js

```
Plot.plot({
  y: {
    grid: true,
    inset: 6
  },
  marks: [\
    Plot.boxY(morley, {x: "Expt", y: "Speed"})\
  ]
})
```

[boxY](https://observablehq.com/plot/marks/box#boxY) produces vertical boxplots; for horizontal boxplots, use [boxX](https://observablehq.com/plot/marks/box#boxX) and swap **x** and **y**.

12345Expt6507007508008509009501,0001,050Speed → [Fork](https://observablehq.com/@observablehq/plot-horizontal-box-plot "Open on Observable")

js

```
Plot.plot({
  x: {
    grid: true,
    inset: 6
  },
  marks: [\
    Plot.boxX(morley, {x: "Speed", y: "Expt"})\
  ]
})
```

As [shorthand](https://observablehq.com/plot/features/shorthand), you can pass an array of numbers for a single boxplot.

01234567 [Fork](https://observablehq.com/@observablehq/plot-shorthand-box-plot "Open on Observable")

js

```
Plot.boxX([0, 3, 4.4, 4.5, 4.6, 5, 7]).plot()
```

Since the box mark uses the [group transform](https://observablehq.com/plot/transforms/group), the secondary dimension must be ordinal. To group quantitative values, bin manually, say with [Math.floor](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/floor); see [#1330](https://github.com/observablehq/plot/issues/1330).

02,0004,0006,0008,00010,00012,00014,00016,00018,000↑ Price0.00.51.01.52.02.53.03.54.04.55.0Carats → [Fork](https://observablehq.com/@observablehq/plot-binned-box-plot "Open on Observable")

js

```
Plot.plot({
  marginLeft: 60,
  y: {
    grid: true,
    label: "Price"
  },
  x: {
    interval: 0.5,
    label: "Carats",
    labelAnchor: "right",
    tickFormat: (x) => x.toFixed(1)
  },
  marks: [\
    Plot.ruleY([0]),\
    Plot.boxY(diamonds, {x: (d) => Math.floor(d.carat * 2) / 2, y: "price"})\
  ]
})
```

This chart is slightly easier to construct with [faceting](https://observablehq.com/plot/features/facets) using the [**interval** scale option](https://observablehq.com/plot/features/scales#scale-transforms) on the _fx_ scale. (This technique cannot be used with the _x_ scale above because the scale interval transform is applied _after_ the box mark applies the group transform.)

0.00.51.01.52.02.53.03.54.04.55.0Carats →02,0004,0006,0008,00010,00012,00014,00016,00018,000↑ Price [Fork](https://observablehq.com/@observablehq/plot-binned-box-plot "Open on Observable")

js

```
Plot.plot({
  marginLeft: 60,
  y: {
    grid: true,
    label: "Price"
  },
  fx: {
    interval: 0.5,
    label: "Carats",
    labelAnchor: "right",
    tickFormat: (x) => x.toFixed(1)
  },
  marks: [\
    Plot.ruleY([0]),\
    Plot.boxY(diamonds, {fx: "carat", y: "price"})\
  ]
})
```

## Box options [​](https://observablehq.com/plot/marks/box\#box-options)

The box mark is a [composite mark](https://observablehq.com/plot/features/marks#marks) consisting of four marks:

- a [rule](https://observablehq.com/plot/marks/rule) representing the extreme values (not including outliers)
- a [bar](https://observablehq.com/plot/marks/bar) representing the interquartile range (trimmed to the data)
- a [tick](https://observablehq.com/plot/marks/tick) representing the median value, and
- a [dot](https://observablehq.com/plot/marks/dot) representing outliers, if any

The given _options_ are passed through to these underlying marks, with the exception of the following options:

- **fill** \- the fill color of the bar; defaults to #ccc
- **fillOpacity** \- the fill opacity of the bar; defaults to 1
- **stroke** \- the stroke color of the rule, tick, and dot; defaults to _currentColor_
- **strokeOpacity** \- the stroke opacity of the rule, tick, and dot; defaults to 1
- **strokeWidth** \- the stroke width of the tick; defaults to 1
- **r** \- the radius of the dot; defaults to 3

## boxX( _data_, _options_) [​](https://observablehq.com/plot/marks/box\#boxX)

js

```
Plot.boxX(simpsons.map((d) => d.imdb_rating))
```

Returns a horizontal box mark. If the **x** option is not specified, it defaults to the identity function, as when _data_ is an array of numbers. If the **y** option is not specified, it defaults to null; if the **y** option is specified, it should represent an ordinal (discrete) value.

## boxY( _data_, _options_) [​](https://observablehq.com/plot/marks/box\#boxY)

js

```
Plot.boxY(simpsons.map((d) => d.imdb_rating))
```

Returns a vertical box mark. If the **y** option is not specified, it defaults to the identity function, as when _data_ is an array of numbers. If the **x** option is not specified, it defaults to null; if the **x** option is specified, it should represent an ordinal (discrete) value.

Pager

[Previous pageBollinger](https://observablehq.com/plot/marks/bollinger)

[Next pageCell](https://observablehq.com/plot/marks/cell)

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

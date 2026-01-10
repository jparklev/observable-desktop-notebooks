---
url: "https://observablehq.com/plot/transforms/normalize"
title: "Normalize transform | Plot"
---

# Normalize transform [​](https://observablehq.com/plot/transforms/normalize\#normalize-transform)

The **normalize transform** is a specialized [map transform](https://observablehq.com/plot/transforms/map) that normalizes series values relative to some basis, say to convert absolute values into relative values. For example, here is an index chart — a type of multi-series line chart — showing the return of several stocks relative to their closing price on a particular date.

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

TIP

The [select transform](https://observablehq.com/plot/transforms/select) is used to label the endpoints of each line.

INFO

This example uses an [immediately-invoked function expression (IIFE)](https://developer.mozilla.org/en-US/docs/Glossary/IIFE) for the **tickFormat** option so that the [d3.format](https://d3js.org/d3-format) only needs to be constructed once.

The normalize transform converts absolute values into relative ones. So, if **y** is \[ _y₀_, _y₁_, _y₂_, …\] and the _first_ basis is used with [normalizeY](https://observablehq.com/plot/transforms/normalize#normalizeY), the resulting output **y** channel is \[ _y₀_ / _y₀_, _y₁_ / _y₀_, _y₂_ / _y₀_, …\]. But it’s a bit more complicated than this in practice since **y** is first grouped by **z**, **fill**, or **stroke** into separate series.

As another example, the normalize transform can be used to compute proportional demographics from absolute populations. The plot below compares the demographics of U.S. states: color represents age group, **y** represents the state, and **x** represents the proportion of the state’s population in that age group.

<1010-1920-2930-3940-4950-5960-6970-79≥80

02468101214161820Population (%) →<10<10<10<10<10<10<10<10<10<10<10<10<10<10<10<10<10<10<10<10<10<10<10<10<10<10<10<10<10<10<10<10<10<10<10<10<10<10<10<10<10<10<10<10<10<10<10<10<10<10<10<1010-1910-1910-1910-1910-1910-1910-1910-1910-1910-1910-1910-1910-1910-1910-1910-1910-1910-1910-1910-1910-1910-1910-1910-1910-1910-1910-1910-1910-1910-1910-1910-1910-1910-1910-1910-1910-1910-1910-1910-1910-1910-1910-1910-1910-1910-1910-1910-1910-1910-1910-1910-1920-2920-2920-2920-2920-2920-2920-2920-2920-2920-2920-2920-2920-2920-2920-2920-2920-2920-2920-2920-2920-2920-2920-2920-2920-2920-2920-2920-2920-2920-2920-2920-2920-2920-2920-2920-2920-2920-2920-2920-2920-2920-2920-2920-2920-2920-2920-2920-2920-2920-2920-2920-2930-3930-3930-3930-3930-3930-3930-3930-3930-3930-3930-3930-3930-3930-3930-3930-3930-3930-3930-3930-3930-3930-3930-3930-3930-3930-3930-3930-3930-3930-3930-3930-3930-3930-3930-3930-3930-3930-3930-3930-3930-3930-3930-3930-3930-3930-3930-3930-3930-3930-3930-3930-3940-4940-4940-4940-4940-4940-4940-4940-4940-4940-4940-4940-4940-4940-4940-4940-4940-4940-4940-4940-4940-4940-4940-4940-4940-4940-4940-4940-4940-4940-4940-4940-4940-4940-4940-4940-4940-4940-4940-4940-4940-4940-4940-4940-4940-4940-4940-4940-4940-4940-4940-4940-4950-5950-5950-5950-5950-5950-5950-5950-5950-5950-5950-5950-5950-5950-5950-5950-5950-5950-5950-5950-5950-5950-5950-5950-5950-5950-5950-5950-5950-5950-5950-5950-5950-5950-5950-5950-5950-5950-5950-5950-5950-5950-5950-5950-5950-5950-5950-5950-5950-5950-5950-5950-5960-6960-6960-6960-6960-6960-6960-6960-6960-6960-6960-6960-6960-6960-6960-6960-6960-6960-6960-6960-6960-6960-6960-6960-6960-6960-6960-6960-6960-6960-6960-6960-6960-6960-6960-6960-6960-6960-6960-6960-6960-6960-6960-6960-6960-6960-6960-6960-6960-6960-6960-6960-6970-7970-7970-7970-7970-7970-7970-7970-7970-7970-7970-7970-7970-7970-7970-7970-7970-7970-7970-7970-7970-7970-7970-7970-7970-7970-7970-7970-7970-7970-7970-7970-7970-7970-7970-7970-7970-7970-7970-7970-7970-7970-7970-7970-7970-7970-7970-7970-7970-7970-7970-7970-79≥80≥80≥80≥80≥80≥80≥80≥80≥80≥80≥80≥80≥80≥80≥80≥80≥80≥80≥80≥80≥80≥80≥80≥80≥80≥80≥80≥80≥80≥80≥80≥80≥80≥80≥80≥80≥80≥80≥80≥80≥80≥80≥80≥80≥80≥80≥80≥80≥80≥80≥80≥80ALAKAZARCACOCTDEDCFLGAHIIDILINIAKSKYLAMEMDMAMIMNMSMOMTNENVNHNJNMNYNCNDOHOKORPARISCSDTNTXUTVTVAWAWVWIWYPR [Fork](https://observablehq.com/@observablehq/plot-dot-plot "Open on Observable")

js

```
Plot.plot({
  height: 660,
  axis: null,
  grid: true,
  x: {
    axis: "top",
    label: "Population (%)",
    percent: true
  },
  color: {
    scheme: "spectral",
    domain: stateage.ages, // in age order
    legend: true
  },
  marks: [\
    Plot.ruleX([0]),\
    Plot.ruleY(stateage, Plot.groupY({x1: "min", x2: "max"}, {...xy, sort: {y: "x1"}})),\
    Plot.dot(stateage, {...xy, fill: "age", title: "age"}),\
    Plot.text(stateage, Plot.selectMinX({...xy, textAnchor: "end", dx: -6, text: "state"}))\
  ]
})
```

js

```
xy = Plot.normalizeX("sum", {z: "state", x: "population", y: "state"})
```

TIP

To reduce code duplication, pull shared options out into an object (here `xy`) and then merge them into each mark’s options using the spread operator (`...`).

## Normalize options [​](https://observablehq.com/plot/transforms/normalize\#normalize-options)

The **basis** option specifies how to normalize the series values; it is one of:

- _first_ \- the first value, as in an index chart; the default
- _last_ \- the last value
- _min_ \- the minimum value
- _max_ \- the maximum value
- _mean_ \- the mean value (average)
- _median_ \- the median value
- _pXX_ \- the percentile value, where XX is a number in \[00,99\]
- _sum_ \- the sum of values
- _extent_ \- the minimum is mapped to zero, and the maximum to one
- _deviation_ \- subtract the mean, then divide by the standard deviation
- a function to be passed an array of values, returning the desired basis
- a function to be passed an index and channel value array, returning the desired basis

## normalize( _basis_) [^0.2.3](https://github.com/observablehq/plot/releases/tag/v0.2.3 "added in v0.2.3") [​](https://observablehq.com/plot/transforms/normalize\#normalize)

js

```
Plot.map({y: Plot.normalize("first")}, {x: "Date", y: "Close", stroke: "Symbol"})
```

Returns a normalize map method for the given _basis_, suitable for use with the [map transform](https://observablehq.com/plot/transforms/map).

## normalizeX( _basis_, _options_) [​](https://observablehq.com/plot/transforms/normalize\#normalizeX)

js

```
Plot.normalizeX("first", {y: "Date", x: "Close", stroke: "Symbol"})
```

Like [mapX](https://observablehq.com/plot/transforms/map#mapX), but applies the normalize map method with the given _basis_. The **basis** option can also be mixed into the specified _options_ like so:

js

```
Plot.normalizeX({basis: "first", y: "Date", x: "Close", stroke: "Symbol"})
```

If not specified, the _basis_ defaults to _first_.

## normalizeY( _basis_, _options_) [​](https://observablehq.com/plot/transforms/normalize\#normalizeY)

js

```
Plot.normalizeY("first", {x: "Date", y: "Close", stroke: "Symbol"})
```

Like [mapY](https://observablehq.com/plot/transforms/map#mapY), but applies the normalize map method with the given _basis_. The **basis** option can also be mixed into the specified _options_ like so:

js

```
Plot.normalizeY({basis: "first", x: "Date", y: "Close", stroke: "Symbol"})
```

If not specified, the _basis_ defaults to _first_.

Pager

[Previous pageMap](https://observablehq.com/plot/transforms/map)

[Next pageSelect](https://observablehq.com/plot/transforms/select)

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

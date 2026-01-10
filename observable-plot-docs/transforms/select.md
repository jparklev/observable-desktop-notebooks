---
url: "https://observablehq.com/plot/transforms/select"
title: "Select transform | Plot"
---

# Select transform [^0.4.0](https://github.com/observablehq/plot/releases/tag/v0.4.0 "added in v0.4.0") [​](https://observablehq.com/plot/transforms/select\#select-transform)

The **select transform** filters a mark’s index to show a subset of the data. It is a specialized [filter transform](https://observablehq.com/plot/transforms/filter) that pulls a single value or a sample subset out of each series. For example, below selectLast is used to label the last value in a line chart.

020406080100120140160180↑ Close20142015201620172018188.59 [Fork](https://observablehq.com/@observablehq/plot-value-labeled-line-chart "Open on Observable")

js

```
Plot.plot({
  y: {grid: true},
  marks: [\
    Plot.ruleY([0]),\
    Plot.line(aapl, {x: "Date", y: "Close"}),\
    Plot.text(aapl, Plot.selectLast({x: "Date", y: "Close", text: "Close", frameAnchor: "bottom", dy: -6}))\
  ]
})
```

The select transform uses input order, not natural order by value, to determine the meaning of _first_ and _last_. Since this dataset is in reverse chronological order, the first element is the most recent.

Using selectMinY and selectMaxY, you can label the extreme values.

020406080100120140160180↑ Close2014201520162017201856.254190.04 [Fork](https://observablehq.com/@observablehq/plot-value-labeled-line-chart "Open on Observable")

js

```
Plot.plot({
  y: {grid: true},
  marks: [\
    Plot.ruleY([0]),\
    Plot.line(aapl, {x: "Date", y: "Close"}),\
    Plot.text(aapl, Plot.selectMinY({x: "Date", y: "Close", text: "Close", frameAnchor: "top", dy: 6})),\
    Plot.text(aapl, Plot.selectMaxY({x: "Date", y: "Close", text: "Close", frameAnchor: "bottom", dy: -6}))\
  ]
})
```

The select transform groups data into series using the **z**, **fill**, or **stroke** channel in the same fashion as the [area](https://observablehq.com/plot/marks/area) and [line](https://observablehq.com/plot/marks/line) marks. Below, the select transform is used to label the last point in each series of a multi-series line chart.

02004006008001,0001,2001,4001,600↑ Close20142015201620172018AAPLAMZNGOOGIBM [Fork](https://observablehq.com/@observablehq/plot-labeled-multi-line-chart "Open on Observable")

js

```
Plot.plot({
  y: {grid: true},
  marks: [\
    Plot.ruleY([0]),\
    Plot.line(stocks, {x: "Date", y: "Close", stroke: "Symbol"}),\
    Plot.text(stocks, Plot.selectLast({x: "Date", y: "Close", z: "Symbol", text: "Symbol", textAnchor: "start", dx: 3}))\
  ]
})
```

## select( _selector_, _options_) [​](https://observablehq.com/plot/transforms/select\#select)

js

```
Plot.select("first", {x: "Date", y: "Close"}) // selectFirst
```

js

```
Plot.select({y: "min"}, {x: "Date", y: "Close"}) // selectMinY
```

Selects the points in each series determined by the given _selector_, which is one of:

- a named selector, either _first_ or _last_,
- a function which receives as input the series index, or
- a { _name_: _value_} object (with exactly one _name_).

In the last case, _name_ is the name of a channel and _value_ is a value selector, which is one of:

- a named selector, either _min_ or _max_, or
- a function which receives as input the series index and the channel values.

For example, to select the point in each city with the highest temperature (“selectMaxFill”):

js

```
Plot.select({fill: "max"}, {x: "date", y: "city", z: "city", fill: "temperature"})
```

A selector function must return the selected index: a subset of the passed-in series index. For example, selectFirst and selectMinY can be implemented using functions like so:

js

```
Plot.select((I) => [I[0]], {x: "Date", y: "Close"}) // selectFirst
```

js

```
Plot.select({y: (I, Y) => [d3.least(I, (i) => Y[i])]}, {x: "Date", y: "Close"}) // selectMinY
```

Or, to select the point within each series that is the closest to the median of **y**:

js

```
Plot.select({y: selectorMedian}, {x: "year", y: "revenue", fill: "format"})
```

js

```
function selectorMedian(I, V) {
  const median = d3.median(I, (i) => V[i]);
  const i = d3.least(I, (i) => Math.abs(V[i] - median));
  return [i];
}
```

The following selects a sample of 10% of the data:

js

```
Plot.select({y: selectorSample}, {x: "Date", y: "Close"})
```

js

```
function selectorSample(I) {
  return I.filter((i, j) => j % 10 === 0);
}
```

## selectFirst( _options_) [​](https://observablehq.com/plot/transforms/select\#selectFirst)

js

```
Plot.selectFirst({x: "Date", y: "Close"})
```

Selects the first point of each series according to input order.

## selectLast( _options_) [​](https://observablehq.com/plot/transforms/select\#selectLast)

js

```
Plot.selectLast({x: "Date", y: "Close"})
```

Selects the last point of each series according to input order.

## selectMinX( _options_) [​](https://observablehq.com/plot/transforms/select\#selectMinX)

js

```
Plot.selectMinX({x: "Date", y: "Close"})
```

Selects the leftmost point of each series.

## selectMinY( _options_) [​](https://observablehq.com/plot/transforms/select\#selectMinY)

js

```
Plot.selectMinY({x: "Date", y: "Close"})
```

Selects the lowest point of each series.

## selectMaxX( _options_) [​](https://observablehq.com/plot/transforms/select\#selectMaxX)

js

```
Plot.selectMaxX({x: "Date", y: "Close"})
```

Selects the rightmost point of each series.

## selectMaxY( _options_) [​](https://observablehq.com/plot/transforms/select\#selectMaxY)

js

```
Plot.selectMaxY({x: "Date", y: "Close"})
```

Selects the highest point of each series.

Pager

[Previous pageNormalize](https://observablehq.com/plot/transforms/normalize)

[Next pageShift](https://observablehq.com/plot/transforms/shift)

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

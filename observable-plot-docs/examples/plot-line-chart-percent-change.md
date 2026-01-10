---
url: "https://observablehq.com/@observablehq/plot-line-chart-percent-change"
title: "Line chart, percent change"
---

# Line chart, percent change

The variant of a [line chart](/@observablehq/plot-simple-line-chart) shows the change in price of Apple stock relative to ${basis.toFixed(2) === aapl[0].Close.toFixed(2) ? `its ${aapl[0].Date.toLocaleString("en-US", { year: "numeric", month: "long", day: "numeric", })}`: "the"} price of $${basis.toFixed(2)}. The vertical [log scale](https://observablehq.com/plot/features/scales#continuous-scales) allows [accurate comparison](/@mbostock/methods-of-comparison-compared); the [normalize transform](/plot/transforms/normalize) uses a custom basis, for interaction. Data: [Yahoo Finance](https://finance.yahoo.com/lookup)

```js
viewof basis = Inputs.range(d3.extent(aapl, d => d.Close), {label: "Basis", value: aapl[0].Close, step: 0.01, format: x => x.toFixed(2)})
```

```js
Plot.plot({
  width: 928,
  marginLeft: 45,
  y: {type: "log", tickFormat: d => `${d > 1 ? "+" : ""}${Math.round(100 * (d - 1))}%`, grid: true, ticks: 12},
  marks: [
    Plot.ruleY([1]),
    Plot.line(aapl, Plot.normalizeY(() => basis, {x: "Date", y: "Close", stroke: "steelblue"}))
  ]
})
```

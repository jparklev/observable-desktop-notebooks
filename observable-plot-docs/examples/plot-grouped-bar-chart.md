---
url: "https://observablehq.com/@observablehq/plot-grouped-bar-chart"
title: "Grouped bar chart"
---

# Grouped bar chart

[Facets](https://observablehq.com/plot/features/facets) group the bars by State; the *fx* domain, representing States, is [sorted](https://observablehq.com/plot/features/scales#sort-mark-option) by the sum total of the heights of the bars (in other words, by total population). Each facet is a simple bar chart, with the ordinal *x* position ordered by age (*keys*).

```js
Plot.plot({
  x: {axis: null},
  y: {tickFormat: "s", grid: true},
  color: {scheme: "spectral", legend: true},
  marks: [
    Plot.barY(data, {
      x: "key",
      y: "population",
      fill: "key",
      fx: "state",
      sort: {x: null, color: null, fx: {value: "-y", reduce: "sum"}}
    }),
    Plot.ruleY([0])
  ]
})
```

```js
data = FileAttachment("population-state-age.csv").csv({typed: true})
```

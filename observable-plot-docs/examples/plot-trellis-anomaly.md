---
url: "https://observablehq.com/@observablehq/plot-trellis-anomaly"
title: "Barley Trellis plot with arrows"
---

# Barley Trellis plot with arrows

See the [Trellis display](https://observablehq.com/@observablehq/plot-barley-trellis) notebook for more context. Here the variation is shown as an [arrow](https://observablehq.com/plot/marks/arrow) and is used to sort the [facets](https://observablehq.com/plot/features/facets), strongly emphasizing the direction of the change in yield.

```js
Plot.plot({
  height: 800,
  marginLeft: 110,
  grid: true,
  x: {nice: true},
  y: {inset: 5},
  color: {scheme: "spectral", label: "Change in yield", tickFormat: "+f", legend: true},
  facet: {marginRight: 90},
  marks: [
    Plot.frame(),
    Plot.arrow(barley, Plot.groupY({
      x1: "first",
      x2: "last",
      stroke: ([x1, x2]) => x2 - x1 // year-over-year difference
    }, {
      x: "yield",
      y: "variety",
      fy: "site",
      stroke: "yield",
      strokeWidth: 2,
      sort: {y: "x1", fy: "x1", reduce: "median", reverse: true}
    }))
  ]
})
```

```js
barley = FileAttachment("barley.csv").csv({typed: true})
```

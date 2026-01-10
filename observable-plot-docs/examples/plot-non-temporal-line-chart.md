---
url: "https://observablehq.com/@observablehq/plot-non-temporal-line-chart"
title: "Non-temporal line chart"
---

# Non-temporal line chart

In this [line](https://observablehq.com/plot/marks/line) chart drawing the elevation profile of a Tour de France stage, the *x* scale represents distance, not time.

```js
Plot.plot({
  x: {
    label: "Distance from stage start (km) →"
  },
  y: {
    label: "↑ Elevation (m)",
    grid: true
  },
  marks: [
    Plot.ruleY([0]),
    Plot.lineY(tdf, {x: "distance", y: "elevation"})
  ]
})
```

```js
tdf = FileAttachment("tdf-stage-8-2017.csv").csv({typed: true})
```

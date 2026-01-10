---
url: "https://observablehq.com/@observablehq/plot-line-with-moving-average"
title: "Line with moving average"
---

# Line with moving average

The [window](https://observablehq.com/plot/transforms/window) transform can be used to draw a moving average atop points — here, global temperature readings. Source: [NASA Goddard Institute for Space Studies](https://data.giss.nasa.gov/gistemp/)

```js
Plot.plot({
  color: {scheme: "BuRd"},
  marks: [
    Plot.ruleY([0]),
    Plot.dot(gistemp, {x: "Date", y: "Anomaly", stroke: "Anomaly"}),
    Plot.lineY(gistemp, Plot.windowY(12, {x: "Date", y: "Anomaly"}))
  ]
})
```

```js
gistemp = FileAttachment("gistemp.csv").csv({typed: true})
```

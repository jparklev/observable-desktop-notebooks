---
url: "https://observablehq.com/@observablehq/plot-continuous-dimensions-heatmap"
title: "Quantitative dimensions heatmap"
---

# Quantitative dimensions heatmap

Given two quantitative dimensions for *x* and *y*, use the [bin](https://observablehq.com/plot/transforms/bin) transform to create a heatmap.

```js
Plot.plot({
  height: 640,
  marginLeft: 44,
  color: {
    scheme: "bupu",
    type: "symlog"
  },
  marks: [
    Plot.rect(
      diamonds,
      Plot.bin({ fill: "count" }, { x: "carat", y: "price", thresholds: 100 })
    )
  ]
})
```

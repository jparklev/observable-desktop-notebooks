---
url: "https://observablehq.com/@observablehq/plot-multi-series-line-chart-interactive-tips"
title: "Multi-series line chart, interactive tips"
---

# Multi-series line chart, interactive tips

The [pointerX transform](https://observablehq.com/plot/interactions/pointer) respects the dominant dimension (time) by finding the closest point on *x*, but disambiguates between series by also considering the *y* dimension to breaks ties.

```js
Plot.plot({
  marks: [
    Plot.ruleY([0]),
    Plot.lineY(industries, {x: "date", y: "unemployed", stroke: "industry", tip: "x"})
  ]
})
```

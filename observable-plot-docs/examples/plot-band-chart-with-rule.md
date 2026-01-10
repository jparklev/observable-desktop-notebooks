---
url: "https://observablehq.com/@observablehq/plot-band-chart-with-rule"
title: "Band chart with rule"
---

# Band chart with rule

A [ruleX](https://observablehq.com/plot/marks/rule) encodes a vertical extent at a given horizontal position.

```js
Plot.plot({
  y: {grid: true, label: "↑ Temperature (°C)"},
  color: {scheme: "BuRd"},
  marks: [
    Plot.ruleY([0]),
    Plot.ruleX(seattle, {x: "date", y1: "temp_min", y2: "temp_max", stroke: "temp_min"})
  ]
})
```

```js
seattle = FileAttachment("seattle-weather.csv").csv({typed: true})
```

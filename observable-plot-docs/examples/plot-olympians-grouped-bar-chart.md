---
url: "https://observablehq.com/@observablehq/plot-olympians-grouped-bar-chart"
title: "Olympians grouped bar chart"
---

# Olympians grouped bar chart

The *color* scale, which also represents _sex_, is redundant with *x*, allowing us to suppress the *x* axis and instead rely on the color [legend](https://observablehq.com/plot/features/legends) to help the reader understand the chart’s encodings. The [facets](https://observablehq.com/plot/features/facets) (representing _sports_) are separated by making the *x* [scale](https://observablehq.com/plot/features/scales)’s paddingOuter option a bit larger than the default.

```js
Plot.plot({
  marginBottom: 100,
  fx: {padding: 0, label: null, tickRotate: 90, tickSize: 6},
  x: {axis: null, paddingOuter: 0.2},
  y: {grid: true},
  color: {legend: true},
  marks: [
    Plot.barY(olympians, Plot.groupX({y2: "count"}, {x: "sex", fx: "sport", fill: "sex"})),
    Plot.ruleY([0])
  ]
})
```

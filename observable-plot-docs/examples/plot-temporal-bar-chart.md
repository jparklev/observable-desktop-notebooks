---
url: "https://observablehq.com/@observablehq/plot-temporal-bar-chart"
title: "Temporal bar chart"
---

# Temporal bar chart

Use the [interval transform](https://observablehq.com/plot/transforms/interval) —here, expressed as the [rect](https://observablehq.com/plot/marks/rect) mark’s **interval** option— to convert a single time value in *x* into an extent ⟨*x₁*, *x₂*⟩.

```js
Plot.plot({
  marks: [
    Plot.rectY(weather.slice(-42), {x: "date", y: "wind", interval: "day"}),
    Plot.ruleY([0])
  ]
})
```

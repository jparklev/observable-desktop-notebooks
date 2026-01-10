---
url: "https://observablehq.com/@observablehq/plot-vertical-histogram"
title: "Stacked histogram"
---

# Stacked histogram

Olympic athletes [binned](https://observablehq.com/plot/transforms/bin) by weight, separately for each category (*sex*). The [rectY](https://observablehq.com/plot/marks/rect) mark showing the counts is implicitly [stacked](https://observablehq.com/plot/transforms/stack), avoiding occlusion. For an alternative, see [overlapping histogram](https://observablehq.com/@observablehq/plot-overlapping-histogram).

```js
Plot.plot({
  y: {grid: true},
  color: {legend: true},
  marks: [
    Plot.rectY(olympians, Plot.binX({y: "count"}, {x: "weight", fill: "sex"})),
    Plot.ruleY([0])
  ]
})
```

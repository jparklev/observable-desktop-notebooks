---
url: "https://observablehq.com/@observablehq/plot-density-estimation"
title: "Continuous histogram"
---

# Continuous histogram

This approximates a density estimation by [binning](https://observablehq.com/plot/transforms/bin) the data. If you are interested in a better evaluation of density, please upvote issue [#1469](https://github.com/observablehq/plot/issues/1469).

```js
Plot.plot({
  y: {grid: true},
  marks: [
    Plot.areaY(olympians, Plot.binX({y: "count", filter: null}, {x: "weight", fillOpacity: 0.2})),
    Plot.lineY(olympians, Plot.binX({y: "count", filter: null}, {x: "weight"})),
    Plot.ruleY([0])
  ]
})
```

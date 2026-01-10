---
url: "https://observablehq.com/@observablehq/plot-cumulative-histogram"
title: "Cumulative histogram"
---

# Cumulative histogram

If _cumulative_ is −1, each [bin](https://observablehq.com/plot/transforms/bin) represents the number of athletes above a given weight; if +1, below a given weight.

```js
viewof cumulative = Inputs.radio(new Map([["−1", -1], ["+1", 1]]), {label: "cumulative", value: 1})
```

```js
Plot.plot({
  marginLeft: 60,
  y: {grid: true},
  marks: [
    Plot.rectY(olympians, Plot.binX({y: "count"}, {x: "weight", cumulative})),
    Plot.ruleY([0])
  ]
})
```

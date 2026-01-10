---
url: "https://observablehq.com/@observablehq/plot-horizontal-bar-chart"
title: "Horizontal bar chart"
---

# Horizontal bar chart

The ordinal dimension (letters) is, in this case, explicitly [sorted](https://observablehq.com/plot/features/scales#sort-mark-option) according to the *x* dimension, *i.e.* the size of each bar, instead of following the natural order (alphabetical) of its domain.

```js
Plot.plot({
  x: {
    axis: "top",
    grid: true,
    percent: true
  },
  marks: [
    Plot.ruleX([0]),
    Plot.barX(alphabet, {x: "frequency", y: "letter", sort: {y: "x", reverse: true}})
  ]
})
```

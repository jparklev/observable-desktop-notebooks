---
url: "https://observablehq.com/@observablehq/plot-vertical-bar-chart"
title: "Vertical bar chart"
---

# Vertical bar chart

The ordinal dimension (letters) is, in this case, explicitly [sorted](https://observablehq.com/plot/features/scales#sort-mark-option) according to the *y* dimension, *i.e.* the size of each bar, instead of following the natural order (alphabetical) of its domain.

```js
Plot.plot({
  y: {
    grid: true,
    percent: true
  },
  marks: [
    Plot.ruleY([0]),
    Plot.barY(alphabet, {x: "letter", y: "frequency", sort: {x: "y", reverse: true}})
  ]
})
```

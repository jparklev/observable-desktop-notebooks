---
url: "https://observablehq.com/@observablehq/plot-dot-heatmap"
title: "Dot heatmap"
---

# Dot heatmap

The [bin](https://observablehq.com/plot/transforms/bin) transform aggregates data along two quantitative axes *x* and *y*. The result can be displayed by a [dot](https://observablehq.com/plot/marks/dot) mark with a *radius* encoding the number of elements in each bin.

```js
Plot.plot({
  r: {range: [0, 6]}, // generate slightly smaller dots
  marks: [
    Plot.dot(olympians, Plot.bin({r: "count"}, {x: "weight", y: "height"}))
  ]
})
```

Each bin can be further grouped by category (here, by _sex_):

```js
Plot.plot({
  r: {range: [0, 6]},
  marks: [
    Plot.dot(olympians, Plot.bin({r: "count"}, {x: "weight", y: "height", stroke: "sex"}))
  ]
})
```

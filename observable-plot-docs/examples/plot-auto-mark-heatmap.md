---
url: "https://observablehq.com/@observablehq/plot-auto-mark-heatmap"
title: "Auto mark, heatmap"
---

# Auto mark, heatmap

Given two quantitative dimensions for *x* and *y*, the [auto](https://observablehq.com/plot/marks/auto) mark will create a heatmap from the [binned](https://observablehq.com/plot/transforms/bin) values.

```js
Plot.auto(olympians, {x: "weight", y: "height", color: "count"}).plot()
```

This auto mark is equivalent to a rect & bin combination:

```js
Plot.rect(olympians, Plot.bin({fill: "count"}, {x: "weight", y: "height"})).plot()
```

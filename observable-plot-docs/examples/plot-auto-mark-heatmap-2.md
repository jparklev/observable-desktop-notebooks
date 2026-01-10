---
url: "https://observablehq.com/@observablehq/plot-auto-mark-heatmap-2"
title: "Auto mark, heatmap 2"
---

# Auto mark, heatmap 2

Given a quantitative dimension for *x* and an ordinal dimension for *y*, the [auto](https://observablehq.com/plot/marks/auto) mark will create a heatmap from the [binned](https://observablehq.com/plot/transforms/bin) *x* values, grouped by *y*.

```js
Plot.auto(olympians, {x: "weight", y: "sex", color: "count"}).plot()
```

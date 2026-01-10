---
url: "https://observablehq.com/@observablehq/plot-stacked-bars"
title: "Stacked bars"
---

# Stacked bars

Group and count data sharing the same *x* base (here, the island where penguins were counted) and *fill* color (their species). The [bar](https://observablehq.com/plot/marks/bar) mark implicitly [stacks](https://observablehq.com/plot/transforms/stack) values, avoiding occlusion between bars and allowing to a part-to-whole comparison on a given *x*.

```js
Plot.barY(
  penguins,
  Plot.groupX({ y: "count" }, { x: "island", fill: "species" })
).plot({ color: { legend: true } })
```

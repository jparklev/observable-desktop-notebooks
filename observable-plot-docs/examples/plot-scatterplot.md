---
url: "https://observablehq.com/@observablehq/plot-scatterplot/2"
title: "Scatterplot"
---

# Scatterplot

Given a dataset with two quantitative dimensions, the [dot](https://observablehq.com/plot/marks/dot) mark creates a scatterplot.

```js
Plot.dot(penguins, {x: "culmen_length_mm", y: "culmen_depth_mm"}).plot()
```

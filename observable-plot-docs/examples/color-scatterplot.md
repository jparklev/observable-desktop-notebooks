---
url: "https://observablehq.com/@observablehq/color-scatterplot"
title: "Scatterplot with color"
---

# Scatterplot with color

Two quantitative dimensions encoded to the *x* and *y* dimensions (see [scales](https://observablehq.com/plot/features/scales)), and a categorical dimension encoded to *stroke* (color), drawn with the [dot](https://observablehq.com/plot/marks/dot) mark.

```js
Plot.dot(penguins, {x: "culmen_length_mm", y: "culmen_depth_mm", stroke: "species"}).plot()
```

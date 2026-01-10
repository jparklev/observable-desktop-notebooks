---
url: "https://observablehq.com/@observablehq/plot-scatterplot-with-ordinal-dimension"
title: "Scatterplot with ordinal dimension"
---

# Scatterplot with ordinal dimension

A [dot](https://observablehq.com/plot/marks/dot) mark encoding three dimensions with various [scales](https://observablehq.com/plot/features/scales): *x* is quantitative, *y* and *stroke* (color) are nominal.

```js
Plot.plot({
  marginLeft: 60,
  x: {inset: 10},
  y: {label: null},
  marks: [
    Plot.dot(penguins, {x: "body_mass_g", y: "species", stroke: "sex"})
  ]
})
```

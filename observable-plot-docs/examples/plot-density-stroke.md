---
url: "https://observablehq.com/@observablehq/plot-density-stroke"
title: "Density stroke"
---

# Density stroke

The [density](https://observablehq.com/plot/marks/density) contours can be colored based on their value.

```js
Plot.plot({
  inset: 10,
  grid: true,
  x: {type: "log"},
  y: {type: "log"},
  marks: [
    Plot.density(diamonds, {x: "carat", y: "price", stroke: "density"})
  ]
})
```

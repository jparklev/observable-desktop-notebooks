---
url: "https://observablehq.com/@observablehq/plot-one-dimensional-crosshair"
title: "One-dimensional crosshair"
---

# One-dimensional crosshair

If either **x** or **y** is not specified, the [crosshair](https://observablehq.com/plot/interactions/crosshair) is one-dimensional.

```js
Plot.plot({
  marks: [
    Plot.tickX(penguins, {x: "body_mass_g"}),
    Plot.crosshairX(penguins, {x: "body_mass_g", color: "red", opacity: 1})
  ]
})
```

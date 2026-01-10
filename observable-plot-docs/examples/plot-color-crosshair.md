---
url: "https://observablehq.com/@observablehq/plot-color-crosshair"
title: "Color crosshair"
---

# Color crosshair

The **color** option of the [crosshair](https://observablehq.com/plot/interactions/crosshair) mark sets the fill color of the text and the stroke color of the rule. This option can be specified as a channel to reinforce a color encoding.

```js
Plot.plot({
  marks: [
    Plot.dot(penguins, {x: "culmen_length_mm", y: "culmen_depth_mm", stroke: "sex"}),
    Plot.crosshair(penguins, {x: "culmen_length_mm", y: "culmen_depth_mm", color: "sex", opacity: 0.5})
  ]
})
```

---
url: "https://observablehq.com/@observablehq/plot-symbol-channel"
title: "Symbol channel"
---

# Symbol channel

When an ordinal _color_ scale is used redundantly with a [_symbol_](https://observablehq.com/plot/marks/dot.html) scale, the _symbol_ [legend](https://observablehq.com/plot/features/legend.html) will incorporate the color encoding. This is more accessible than using color alone, particularly for readers with color vision deficiency.

```js
Plot.plot({
  grid: true,
  x: {label: "Body mass (g) →"},
  y: {label: "↑ Flipper length (mm)"},
  symbol: {legend: true},
  marks: [
    Plot.dot(penguins, {x: "body_mass_g", y: "flipper_length_mm", stroke: "species", symbol: "species"})
  ]
})
```

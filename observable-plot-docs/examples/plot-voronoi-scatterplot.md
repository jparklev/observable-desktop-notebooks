---
url: "https://observablehq.com/@observablehq/plot-voronoi-scatterplot"
title: "Voronoi scatterplot"
---

# Voronoi scatterplot

The [voronoi](https://observablehq.com/plot/marks/voronoi) mark computes the region closest to each point.

```js
Plot.plot({
  color: {legend: true},
  marks: [
    Plot.voronoi(penguins, {x: "culmen_depth_mm", y: "culmen_length_mm", fill: "species", fillOpacity: 0.2, stroke: "var(--vp-c-bg)"}),
    Plot.frame(),
    Plot.dot(penguins, {x: "culmen_depth_mm", y: "culmen_length_mm", fill: "species"})
  ]
})
```

---
url: "https://observablehq.com/@observablehq/plot-faceted-areas"
title: "Faceted areas"
---

# Faceted areas

Small multiples, rendering different [facets](https://observablehq.com/plot/features/facets) (subsets of the complete dataset), facilitate comparison between modalities. Here, the evolution of the number of unemployed workers across industries.

```js
Plot.plot({
  height: 720,
  axis: null,
  marks: [
    Plot.areaY(industries, {x: "date", y: "unemployed", fy: "industry"}),
    Plot.text(industries, Plot.selectFirst({text: "industry", fy: "industry", frameAnchor: "top-left", dx: 6, dy: 6})),
    Plot.frame()
  ]
})
```

---
url: "https://observablehq.com/@observablehq/plot-filled-contours"
title: "Filled contours"
---

# Filled contours

[Contours](https://observablehq.com/plot/marks/contour) can be filled with a color based on their value.

```js
Plot.plot({
  aspectRatio: 1,
  color: {
    legend: true,
    label: "Elevation (m)"
  },
  marks: [
    Plot.contour(volcano.values, {
      width: volcano.width,
      height: volcano.height,
      fill: Plot.identity,
      stroke: "black"
    })
  ]
})
```

```js
volcano = FileAttachment("volcano.json").json()
```

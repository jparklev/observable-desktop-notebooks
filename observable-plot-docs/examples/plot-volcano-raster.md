---
url: "https://observablehq.com/@observablehq/plot-volcano-raster"
title: "Volcano raster"
---

# Volcano raster

A [raster](https://observablehq.com/plot/marks/raster) mark directly reading an array of elevation values.

```js
Plot.plot({
  aspectRatio: 1,
  color: {label: "Elevation (m)", legend: true},
  marks: [
    Plot.raster(volcano.values, {width: volcano.width, height: volcano.height})
  ]
})
```

```js
volcano = FileAttachment("volcano.json").json()
```

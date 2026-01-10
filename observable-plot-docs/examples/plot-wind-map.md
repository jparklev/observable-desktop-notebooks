---
url: "https://observablehq.com/@observablehq/plot-wind-map"
title: "Wind map"
---

# Wind map

[Vectors](https://observablehq.com/plot/marks/vector) on a grid can show both direction and intensity—in this case, the speed of winds.

```js
Plot.plot({
  inset: 10,
  aspectRatio: 1,
  color: {
    label: "Speed (m/s)",
    zero: true,
    legend: true
  },
  marks: [
    Plot.vector(wind, {
      x: "longitude",
      y: "latitude",
      rotate: ({u, v}) => Math.atan2(u, v) * 180 / Math.PI,
      length: ({u, v}) => Math.hypot(u, v),
      stroke: ({u, v}) => Math.hypot(u, v)
    })
  ]
})
```

```js
wind = FileAttachment("wind.csv").csv({typed: true})
```

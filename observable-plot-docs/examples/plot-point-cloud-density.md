---
url: "https://observablehq.com/@observablehq/plot-point-cloud-density"
title: "Point cloud density"
---

# Point cloud density

The [density](https://observablehq.com/plot/marks/density) mark shows the estimated density of two-dimensional point clouds.

```js
Plot.plot({
  inset: 10,
  marks: [
    Plot.density(faithful, {x: "waiting", y: "eruptions", stroke: "steelblue", strokeWidth: 0.25}),
    Plot.density(faithful, {x: "waiting", y: "eruptions", stroke: "steelblue", thresholds: 4}),
    Plot.dot(faithful, {x: "waiting", y: "eruptions", fill: "currentColor", r: 1.5})
  ]
})
```

```js
faithful = FileAttachment("faithful.tsv").tsv({typed: true})
```

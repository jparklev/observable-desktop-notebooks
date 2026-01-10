---
url: "https://observablehq.com/@observablehq/plot-spherical-line-with-a-varying-stroke"
title: "Spherical line with a varying stroke"
---

# Spherical line with a varying stroke

Set the **z** option to null for [line](https://observablehq.com/plot/marks/line) charts that represent a single series of data with a varying color. This also works with the geodesic [curve](https://observablehq.com/plot/features/curves) used for map [projections](https://observablehq.com/plot/features/projections)!

```js
Plot.plot({
  projection: "equirectangular",
  marks: [
    Plot.geo(land),
    Plot.line(beagle, {stroke: (d, i) => i, z: null})
  ]
})
```

```js
beagle = FileAttachment("beagle.csv").csv({array: true, typed: true})
```

```js
world = FileAttachment("countries-110m.json").json()
```

```js
land = topojson.feature(world, world.objects.land)
```

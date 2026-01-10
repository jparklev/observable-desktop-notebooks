---
url: "https://observablehq.com/@observablehq/plot-world-projections"
title: "World projections"
---

# World projections

No single [projection](https://observablehq.com/plot/features/projections) is best at everything. It is impossible, for example, for a projection to be both conformal (preserving angles) and equal-area (preserving relative surface areas).

```js
viewof projection = Inputs.select(
  [
    /* "albers", */
    "azimuthal-equal-area",
    "azimuthal-equidistant",
    /* "conic-conformal", */
    "conic-equal-area",
    "conic-equidistant",
    "equal-earth",
    "equirectangular",
    "gnomonic",
    /* "identity", */
    /* "reflect-y", */
    "mercator",
    "orthographic",
    "stereographic",
    "transverse-mercator"
  ],
  { label: "projection", value: "equirectangular" }
)
```

```js
Plot.plot({
  projection,
  marks: [
    Plot.graticule(),
    Plot.geo(land, {fill: "currentColor"}),
    Plot.sphere()
  ]
})
```

```js
world = FileAttachment("countries-110m.json").json()
```

```js
land = topojson.feature(world, world.objects.land)
```

---
url: "https://observablehq.com/@observablehq/plot-polar-projection"
title: "Polar projection"
---

# Polar projection

To demonstrate the extensibility of Plot’s [projection system](https://observablehq.com/plot/features/projections), this example explicitly defines an azimuthal equidistant projection that fits a designated rectangle.

```js
Plot.plot({
  width: 688,
  height: 688,
  projection: ({width, height}) => d3.geoAzimuthalEquidistant()
    .rotate([0, 90])
    .translate([width / 2, height / 2])
    .scale(width)
    .clipAngle(40),
  marks: [
    Plot.graticule(),
    Plot.geo(land, {fill: "currentColor"}),
    Plot.frame()
  ]
})
```

```js
world = FileAttachment("countries-110m.json").json()
```

```js
land = topojson.feature(world, world.objects.land)
```

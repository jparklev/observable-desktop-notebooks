---
url: "https://observablehq.com/@observablehq/plot-earthquake-globe"
title: "Earthquake globe"
---

# Earthquake globe

[Projections](https://observablehq.com/plot/features/projections) and live data!

```js
viewof longitude = Inputs.range([-180, 180], {label: "longitude", step: 1, value: 90})
```

```js
Plot.plot({
  projection: {type: "orthographic", rotate: [-longitude, -30]},
  r: {transform: (d) => Math.pow(10, d)}, // convert Richter to amplitude
  style: "overflow: visible;", // allow dots to escape
  marks: [
    Plot.geo(land, {fill: "currentColor", fillOpacity: 0.2}),
    Plot.sphere(),
    Plot.dot(earthquakes, {x: "longitude", y: "latitude", r: "magnitude", stroke: "red", fill: "red", fillOpacity: 0.2})
  ]
})
```

```js
world = FileAttachment("countries-110m.json").json()
```

```js
land = topojson.feature(world, world.objects.land)
```

```js
earthquakes = d3.json("https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_week.geojson").then(d => d.features.map(f => {
  const c = d3.geoCentroid(f);
  return {magnitude: f.properties.mag, longitude: c[0], latitude: c[1]};
}))
```

---
url: "https://observablehq.com/@observablehq/plot-walmart-voronoi"
title: "Walmart Voronoi"
---

# Walmart Voronoi

The [Voronoi](https://observablehq.com/plot/marks/delaunay) diagram of the Walmart stores in the contiguous U.S. shows the catchment area of each point.

```js
Plot.plot({
  projection: "albers",
  marks: [
    Plot.geo(nation),
    Plot.dot(walmarts, {x: "longitude", y: "latitude", fill: "currentColor", r: 1}),
    Plot.voronoiMesh(walmarts, {x: "longitude", y: "latitude"})
  ]
})
```

```js
us = FileAttachment("us-counties-10m.json").json()
```

```js
nation = topojson.feature(us, us.objects.nation)
```

```js
walmarts = FileAttachment("walmarts.tsv").tsv({typed: true})
```

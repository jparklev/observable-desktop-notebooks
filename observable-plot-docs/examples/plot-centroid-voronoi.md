---
url: "https://observablehq.com/@observablehq/plot-centroid-voronoi"
title: "Centroid Voronoi"
---

# Centroid Voronoi

A classic of creative mapping: take the [centroids](https://observablehq.com/plot/transforms/centroid) of geographic features, and compute their [voronoi](https://observablehq.com/plot/marks/delaunay) diagram.

```js
Plot.voronoi(counties, Plot.centroid()).plot({projection: "albers"})
```

```js
us = FileAttachment("us-counties-10m.json").json()
```

```js
counties = topojson.feature(us, us.objects.counties).features
```

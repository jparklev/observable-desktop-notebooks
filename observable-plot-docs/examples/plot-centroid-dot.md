---
url: "https://observablehq.com/@observablehq/plot-centroid-dot"
title: "Centroid dot"
---

# Centroid dot

The [centroid](https://observablehq.com/plot/transforms/centroid) and geoCentroid transforms work slightly differently—they allow to compute a single location for each geographic feature, which can be used, for example, to display a [dot](https://observablehq.com/plot/marks/dot).

```js
Plot.dot(counties, Plot.centroid()).plot({projection: "albers-usa"})
```

```js
Plot.dot(counties, Plot.geoCentroid()).plot({projection: "albers-usa"})
```

--- The difference between the centroid initializer and the geoCentroid transform is almost imperceptible. In the map below, which layers both approaches, only one dot near the bottom-left of the frame is noticeably different:

```js
Plot.plot({
  projection: "albers-usa",
  marks: [
    Plot.dot(counties, Plot.geoCentroid({stroke: "red"})),
    Plot.dot(counties, Plot.centroid({fill: "currentColor", r: 2}))
  ]
})
```

```js
us = FileAttachment("us-counties-10m.json").json()
```

```js
counties = topojson.feature(us, us.objects.counties).features
```

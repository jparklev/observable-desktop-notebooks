---
url: "https://observablehq.com/@observablehq/plot-map-small-multiples"
title: "Map small multiples"
---

# Map small multiples

Plot’s [projection](https://observablehq.com/plot/features/projections) system is compatible with its [faceting](https://observablehq.com/plot/features/facets) system. Below, a comic strip of sorts shows the locations of Walmart store openings in past decades.

```js
Plot.plot({
  marginLeft: 0,
  marginRight: 0,
  projection: "albers",
  fx: {
    interval: d3.utcYear.every(10),
    tickFormat: (d) => `${d.getUTCFullYear()}’s`,
    label: null
  },
  marks: [
    Plot.geo(statemesh, {strokeOpacity: 0.1}),
    Plot.geo(nation),
    Plot.dot(walmarts, {fx: "date", x: "longitude", y: "latitude", r: 1, fill: "currentColor"})
  ]
})
```

```js
walmarts = FileAttachment("walmarts.tsv").tsv({typed: true})
```

```js
us = FileAttachment("us-counties-10m.json").json()
```

```js
statemesh = topojson.mesh(us, us.objects.states)
```

```js
nation = topojson.feature(us, us.objects.nation)
```

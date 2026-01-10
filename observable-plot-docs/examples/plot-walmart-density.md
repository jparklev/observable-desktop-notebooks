---
url: "https://observablehq.com/@observablehq/plot-walmart-density"
title: "Walmart density"
---

# Walmart density

The [density](https://observablehq.com/plot/marks/density) mark supports projected data. For more accurate results, prefer an equal-area [projection](https://observablehq.com/plot/features/projections).

```js
Plot.plot({
  projection: "albers",
  color: {scheme: "YlGnBu"},
  style: "overflow: visible;",
  marks: [
    Plot.density(walmarts, {x: "longitude", y: "latitude", bandwidth: 10, fill: "density"}),
    Plot.geo(statemesh, {strokeOpacity: 0.3}),
    Plot.geo(nation),
    Plot.dot(walmarts, {x: "longitude", y: "latitude", r: 1, fill: "currentColor"})
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
statemesh = topojson.mesh(us, us.objects.states)
```

```js
walmarts = FileAttachment("walmarts.tsv").tsv({typed: true})
```

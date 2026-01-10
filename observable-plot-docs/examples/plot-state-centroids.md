---
url: "https://observablehq.com/@observablehq/plot-state-centroids"
title: "State centroids"
---

# State centroids

Mark the [centroid](https://observablehq.com/plot/transforms/centroid) of each U.S. state with a [dot](https://observablehq.com/plot/marks/dot) and an interactive [tip](https://observablehq.com/plot/marks/tip).

```js
Plot.plot({
  projection: "albers-usa",
  marks: [
    Plot.geo(states, {strokeOpacity: 0.1, tip: true, title: "name"}),
    Plot.geo(nation),
    Plot.dot(states, Plot.centroid({fill: "red", stroke: "white"}))
  ]
})
```

```js
nation = topojson.feature(us, us.objects.nation)
```

```js
states = topojson.feature(us, us.objects.states).features
```

```js
us = FileAttachment("us-counties-10m.json").json()
```

---
url: "https://observablehq.com/@observablehq/plot-maps-tips"
title: "Map and tips"
---

# Map and tips

The [centroid transform](https://observablehq.com/plot/transforms/centroid) can derive **x** and **y** channels from [geometries](https://observablehq.com/plot/marks/geo), thus allowing the placement of [tips](https://observablehq.com/plot/marks/tip).

```js
Plot.plot({
  projection: "albers-usa",
  marks: [
    Plot.geo(states),
    Plot.tip(states, Plot.geoCentroid({title: (d) => d.properties.name, anchor: "bottom", textPadding: 3}))
  ]
})
```

For interactive tips, just combine the [pointer](https://observablehq.com/plot/interactions/pointer) and [centroid](https://observablehq.com/plot/transforms/centroid) transforms:

```js
Plot.plot({
  projection: "albers-usa",
  marks: [
    Plot.geo(states),
    Plot.tip(states, Plot.pointer(Plot.geoCentroid({title: (d) => d.properties.name})))
  ]
})
```

```js
us = FileAttachment("us-counties-10m@1.json").json()
```

```js
states = topojson.feature(us, us.objects.states).features
```

---
url: "https://observablehq.com/@observablehq/plot-albers-usa-projection"
title: "Albers-USA projection"
---

# Albers-USA projection

Use the *albers-usa* projection for U.S.-centric maps. This projection is equal-area for the continental United States and Hawaii. Note however that the scale for Alaska is diminished: it is projected at 0.35× its true relative area.

```js
Plot.plot({
  projection: "albers-usa",
  marks: [
    Plot.geo(nation),
    Plot.geo(statemesh, {strokeOpacity: 0.2})
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

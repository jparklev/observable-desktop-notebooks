---
url: "https://observablehq.com/@observablehq/plot-state-labels"
title: "State labels"
---

# State labels

Add a label to U.S. states with a [text mark](https://observablehq.com/plot/marks/text) and a [centroid](https://observablehq.com/plot/transforms/centroid) transform.

```js
Plot.plot({
  projection: "albers-usa",
  marks: [
    Plot.geo(statemesh),
    Plot.text(states, Plot.centroid({text: (d) => d.properties.name, fill: "currentColor", stroke: "white"}))
  ]
})
```

```js
states = topojson.feature(us, us.objects.states).features
```

```js
statemesh = topojson.mesh(us, us.objects.states)
```

```js
us = FileAttachment("us-counties-10m.json").json()
```

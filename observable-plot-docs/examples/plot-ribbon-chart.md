---
url: "https://observablehq.com/@observablehq/plot-ribbon-chart"
title: "Ribbon chart"
---

# Ribbon chart

Ordering [stacks](https://observablehq.com/plot/transforms/stack) by *value* results in criss-crossing ribbons with the largest value on top. (Use **reverse** to put the smallest values on top.)

```js
Plot.plot({
  y: {
    grid: true,
    label: "↑ Annual revenue (billions, adj.)",
    transform: (d) => d / 1000 // convert millions to billions
  },
  marks: [
    Plot.areaY(riaa, {x: "year", y: "revenue", z: "format", fill: "group", order: "value"}),
    Plot.ruleY([0])
  ]
})
```

```js
riaa = FileAttachment("riaa-us-revenue.csv").csv({typed: true})
```

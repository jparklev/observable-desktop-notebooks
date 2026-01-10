---
url: "https://observablehq.com/@observablehq/plot-one-dimensional-density"
title: "One-dimensional density"
---

# One-dimensional density

Although it is inherently two-dimensional, the [density](https://observablehq.com/plot/marks/density) mark is compatible with one-dimensional data. For a more accurate estimation of one-dimensional densities, please upvote issue [#1469](https://github.com/observablehq/plot/issues/1469).

```js
Plot.plot({
  height: 100,
  inset: 10,
  marks: [
    Plot.density(faithful, {x: "waiting", stroke: "steelblue", strokeWidth: 0.25, bandwidth: 10}),
    Plot.density(faithful, {x: "waiting", stroke: "steelblue", thresholds: 4, bandwidth: 10}),
    Plot.dot(faithful, {x: "waiting", fill: "currentColor", r: 1.5})
  ]
})
```

```js
faithful = FileAttachment("faithful.tsv").tsv({typed: true})
```

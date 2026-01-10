---
url: "https://observablehq.com/@observablehq/plot-vertical-bars-rotated-labels"
title: "Vertical bars, rotated labels"
---

# Vertical bars, rotated labels

The [tickRotate](https://observablehq.com/plot/marks/axis#axis-options) axis option rotates the tick labels.

```js
Plot.plot({
  marginBottom: 60,
  x: {
    tickRotate: -30,
  },
  y: {
    transform: (d) => d / 1000,
    label: "↑ Market value (US dollars, billions)",
    grid: 5
  },
  marks: [
    Plot.ruleY([0]),
    
    Plot.barY(brands, {
      x: "name",
      y: "value",
      sort: { x: "y", reverse: true, limit: 20 },
      fill: "steelblue"
    }),
  ]
})
```

Data: Interbrand. Market value of 100 top global brands in 2018, millions of dollars.

```js
brands = FileAttachment("brands-2018.csv").csv({typed: true})
```

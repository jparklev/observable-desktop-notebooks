---
url: "https://observablehq.com/@observablehq/plot-arrow-variation-chart"
title: "Arrow variation chart"
---

# Arrow variation chart

An [arrow](https://observablehq.com/plot/marks/arrow) connects the positions in 1980 and 2015 of each city on this population × inequality chart. Color [encodes](https://observablehq.com/plot/features/scales) variation.

```js
Plot.plot({
  grid: true,
  inset: 10,
  x: {
    type: "log",
    label: "Population →"
  },
  y: {
    label: "↑ Inequality",
    ticks: 4
  },
  color: {
    scheme: "BuRd",
    label: "Change in inequality from 1980 to 2015",
    legend: true,
    tickFormat: "+f"
  },
  marks: [
    Plot.arrow(metros, {
      x1: "POP_1980",
      y1: "R90_10_1980",
      x2: "POP_2015",
      y2: "R90_10_2015",
      bend: true,
      stroke: (d) => d.R90_10_2015 - d.R90_10_1980
    }),
    Plot.text(metros, {
      x: "POP_2015",
      y: "R90_10_2015",
      filter: "highlight",
      text: "nyt_display",
      fill: "currentColor",
      stroke: "white",
      dy: -6
    })
  ]
})
```

```js
metros = FileAttachment("metros.csv").csv({typed: true})
```

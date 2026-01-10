---
url: "https://observablehq.com/@observablehq/plot-civilizations-timeline"
title: "Civilizations timeline"
---

# Civilizations timeline

A [bar](https://observablehq.com/plot/marks/bar) mark with explicit *x1* and *x2* channels, marking the start and end of civilizations.

```js
Plot.plot({
  marginLeft: 130,
  axis: null,
  x: {
    axis: "top",
    grid: true,
    tickFormat: (x) => x < 0 ? `${-x} BC` : `${x} AD`
  },
  marks: [
    Plot.barX(civilizations, {
      x1: "start",
      x2: "end",
      y: "civilization",
      sort: {y: "x1"}
    }),
    Plot.text(civilizations, {
      x: "start",
      y: "civilization",
      text: "civilization",
      textAnchor: "end",
      dx: -3
    })
  ]
})
```

```js
civilizations = FileAttachment("civilizations.csv").csv({typed: true})
```

---
url: "https://observablehq.com/@observablehq/plot-variable-fill-area"
title: "Variable fill area"
---

# Variable fill area

Set the **z** option to null for [area](https://observablehq.com/plot/marks/area) (or [line](https://observablehq.com/@observablehq/plot-window-and-map)) charts that represent a single series of data with a varying color.

```js
Plot.plot({
  color: {
    type: "log",
    legend: true
  },
  marks: [
    Plot.areaY(aapl, {x: "Date", y: "Close", fill: "Volume", z: null}),
    Plot.ruleY([0])
  ]
})
```

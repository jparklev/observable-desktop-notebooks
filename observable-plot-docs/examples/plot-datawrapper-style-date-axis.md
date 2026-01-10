---
url: "https://observablehq.com/@observablehq/plot-datawrapper-style-date-axis"
title: "Datawrapper-style date axis"
---

# Datawrapper-style date axis

Plot’s time [axes](https://observablehq.com/plot/marks/axis) display month and year on two separate lines, [à la Datawrapper](https://academy.datawrapper.de/article/199-custom-date-formats-that-you-can-display-in-datawrapper).

```js
Plot.plot({
  marks: [
    Plot.ruleY([0]),
    Plot.axisX({ticks: "3 months"}),
    Plot.gridX(),
    Plot.line(aapl, {x: "Date", y: "Close"})
  ]
})
```

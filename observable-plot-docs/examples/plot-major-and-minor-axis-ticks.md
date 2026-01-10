---
url: "https://observablehq.com/@observablehq/plot-major-and-minor-axis-ticks"
title: "Major and minor axis ticks"
---

# Major and minor axis ticks

The [axis](https://observablehq.com/plot/marks/axis) mark can be called several times with different options.

```js
Plot.plot({
  x: {nice: true},
  y: {grid: true},
  marks: [
    Plot.line(aapl, {x: "Date", y: "Close"}),
    Plot.axisX({ticks: "month", text: null, tickSize: 3}),
    Plot.axisX(),
    Plot.axisY({ticks: 50, tickSize: 3, text: null}),
    Plot.axisY()
  ]
})
```

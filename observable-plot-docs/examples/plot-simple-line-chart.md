---
url: "https://observablehq.com/@observablehq/plot-simple-line-chart"
title: "Simple line chart"
---

# Simple line chart

The [line](https://observablehq.com/plot/marks/line) mark draws two-dimensional lines.

```js
Plot.lineY(aapl, {x: "Date", y: "Close"}).plot({y: {grid: true}})
```

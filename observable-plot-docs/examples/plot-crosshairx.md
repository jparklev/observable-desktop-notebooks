---
url: "https://observablehq.com/@observablehq/plot-crosshairx"
title: "CrosshairX"
---

# CrosshairX

For charts which have a “dominant” dimension, such as time in a time-series chart, use the [crosshairX](https://observablehq.com/plot/interactions/crosshair) mark for the [pointerX](https://observablehq.com/plot/interactions/pointer#pointerx-options) transform.

```js
Plot.plot({
  style: "overflow: visible;",
  marks: [
    Plot.lineY(aapl, {x: "Date", y: "Close"}),
    Plot.crosshairX(aapl, {x: "Date", y: "Close"})
  ]
})
```

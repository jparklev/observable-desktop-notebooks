---
url: "https://observablehq.com/@observablehq/plot-dot-bins"
title: "Dot histogram"
---

# Dot histogram

A [dot](https://observablehq.com/plot/marks/dot) mark with a radius [encoding](https://observablehq.com/plot/features/scales) representing the count of Olympic athletes, [binned](https://observablehq.com/plot/transforms/bin) by weight.

```js
Plot.plot({
  r: {range: [0, 14]},
  marks: [
    Plot.dot(olympians, Plot.binX({r: "count"}, {x: "weight"}))
  ]
})
```

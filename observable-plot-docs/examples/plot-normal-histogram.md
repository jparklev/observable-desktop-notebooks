---
url: "https://observablehq.com/@observablehq/plot-normal-histogram"
title: "Normal histogram"
---

# Normal histogram

For a histogram, use the [binX](https://observablehq.com/plot/transforms/bin) transform with the [rectY](https://observablehq.com/plot/marks/rect) mark. Here we bin 10,000 random samples, generated on-the-fly into the *x* channel from a [normal distribution](https://observablehq.com/@d3/d3-random#normal).

```js
Plot.rectY({length: 10000}, Plot.binX({y: "count"}, {x: d3.randomNormal()})).plot()
```

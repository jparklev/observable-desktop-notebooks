---
url: "https://observablehq.com/@observablehq/plot-hexbin-text"
title: "Hexbin text"
---

# Hexbin text

Olympic athletes are placed on this [heatmap](https://observablehq.com/@observablehq/plot-olympians-hexbin) according to their weight and height, [scaled](https://observablehq.com/plot/features/scales) by *x* and *y*. _Then_ their positions (in pixels) are grouped into [hexagonal bins](https://observablehq.com/plot/transforms/hexbin), which are represented by a [text](https://observablehq.com/plot/marks/text) mark showing the count.

```js
Plot
  .text(olympians, Plot.hexbin({text: "count"}, {x: "weight", y: "height"}))
  .plot()
```

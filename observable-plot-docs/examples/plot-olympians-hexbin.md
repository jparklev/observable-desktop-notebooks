---
url: "https://observablehq.com/@observablehq/plot-olympians-hexbin"
title: "Hexbin heatmap"
---

# Hexbin heatmap

Olympic athletes are placed on this heatmap according to their weight and height, [scaled](https://observablehq.com/plot/features/scales) by *x* and *y*. _Then_ their positions (in pixels) are binned into [hexagons](https://observablehq.com/plot/transforms/hexbin), which are filled with a *color* that encodes frequency.

```js
Plot
  .hexagon(olympians, Plot.hexbin({fill: "count"}, {x: "weight", y: "height", symbol: "square"}))
  .plot({color: {scheme: "YlGnBu"}})
```

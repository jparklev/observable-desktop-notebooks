---
url: "https://observablehq.com/@observablehq/plot-ggplot2-style-axes"
title: "ggplot2-style axes"
---

# ggplot2-style axes

The [frame](https://observablehq.com/plot/marks/frame) and [grid](https://observablehq.com/plot/marks/grid) marks allow for a full customization of the chart’s background, à la [ggplot2](https://ggplot2.tidyverse.org/).

```js
Plot.plot({
  inset: 10,
  marks: [
    Plot.frame({fill: "#eaeaea"}),
    Plot.gridY({stroke: "white", strokeOpacity: 1}),
    Plot.gridX({stroke: "white", strokeOpacity: 1}),
    Plot.line(aapl, {x: "Date", y: "Close", stroke: "black"})
  ]
})
```

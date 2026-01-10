---
url: "https://observablehq.com/@observablehq/plot-prebinned-histogram"
title: "Pre-binned histogram"
---

# Pre-binned histogram

This is for demonstration only; you wouldn’t normally bin “by hand” as shown here, but rather use the [bin](https://observablehq.com/plot/transforms/bin) transform.

```js
Plot.rectY(bins, {x1: "x0", x2: "x1", y2: "length"}).plot()
```

```js
bins = d3.bin().thresholds(80).value((d) => d.weight)(olympians)
```

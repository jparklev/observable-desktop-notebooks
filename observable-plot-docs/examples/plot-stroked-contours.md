---
url: "https://observablehq.com/@observablehq/plot-stroked-contours"
title: "Stroked contours"
---

# Stroked contours

[Contours](https://observablehq.com/plot/marks/contour) default to a stroked outline of the region that contains values above each threshold.

```js
Plot.contour(volcano.values, {width: volcano.width, height: volcano.height}).plot({aspectRatio: 1})
```

```js
volcano = FileAttachment("volcano.json").json()
```

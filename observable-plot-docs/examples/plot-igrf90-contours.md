---
url: "https://observablehq.com/@observablehq/plot-igrf90-contours"
title: "IGRF90 contours"
---

# IGRF90 contours

The [contour](https://observablehq.com/plot/marks/contour) mark can derive contours from non-gridded data samples.

```js
Plot.contour(ca55, {x: "LONGITUDE", y: "LATITUDE", fill: "MAG_IGRF90"}).plot({color: {type: "diverging"}})
```

```js
ca55 = FileAttachment("ca55-south.csv").csv({typed: true})
```

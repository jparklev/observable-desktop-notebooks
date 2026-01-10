---
url: "https://observablehq.com/@observablehq/plot-blurred-contours"
title: "Blurred contours"
---

# Blurred contours

Use the contour mark’s [blur](https://observablehq.com/plot/marks/contour) option for smoother isolines.

```js
Plot.contour(ca55, {x: "LONGITUDE", y: "LATITUDE", fill: "MAG_IGRF90", blur: 4}).plot({color: {type: "diverging"}})
```

```js
ca55 = FileAttachment("ca55-south.csv").csv({typed: true})
```

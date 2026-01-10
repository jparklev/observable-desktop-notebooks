---
url: "https://observablehq.com/@observablehq/plot-geotiff-contours"
title: "GeoTIFF contours"
---

# GeoTIFF contours

```js
Plot.plot({
  width,
  projection: "equal-earth",
  color: { scheme: "Magma" },
  marks: [
    Plot.contour(values, {
      x: (_, i) => i % n / 2,
      y: (_, i) => 90 - Math.floor(i / n) / 2,
      fill: values,
      thresholds: 30,
      stroke: "#000",
      strokeWidth: 0.25,
      clip: "sphere"
    }),
    Plot.sphere()
  ]
})
```

```js
GeoTIFF = import("https://esm.sh/geotiff@2")
```

```js
tiff = FileAttachment("sfctmp.tiff").arrayBuffer().then(GeoTIFF.fromArrayBuffer)
```

```js
image = tiff.getImage()
```

```js
n = image.getWidth()
```

```js
values = (await image.readRasters())[0]
```

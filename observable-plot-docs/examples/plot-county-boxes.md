---
url: "https://observablehq.com/@observablehq/plot-county-boxes"
title: "County boxes"
---

# County boxes

Geographic bounding boxes of U.S. counties, rendered as [rects](https://observablehq.com/plot/marks/rect) with the four coordinates *x₁*, *y₁*, *x₂* and *y₂*.

```js
Plot.plot({
  projection: "albers-usa",
  marks: [
    Plot.rect(countyboxes, {
      x1: "0", // or ([x1]) => x1
      y1: "1", // or ([, y1]) => y1
      x2: "2", // or ([,, x2]) => x2
      y2: "3", // or ([,,, y2]) => y2
      stroke: "currentColor"
    })
  ]
})
```

```js
countyboxes = {
  const counties = topojson.feature(us, us.objects.counties).features;
  return counties.map((d) => d3.geoBounds(d).flat());
}
```

```js
us = FileAttachment("us-counties-10m.json").json()
```

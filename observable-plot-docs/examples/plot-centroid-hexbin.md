---
url: "https://observablehq.com/@observablehq/plot-centroid-hexbin"
title: "Centroid hexbin"
---

# Centroid hexbin

Combine the [geoCentroid](https://observablehq.com/plot/transforms/centroid) and [hexbin](https://observablehq.com/plot/transforms/hexbin) transforms to measure the density of U.S. counties.

```js
Plot.dot(counties, Plot.hexbin({r:"count"}, Plot.geoCentroid())).plot({projection: "albers"})
```

```js
us = FileAttachment("us-counties-10m.json").json()
```

```js
counties = topojson.feature(us, us.objects.counties).features
```

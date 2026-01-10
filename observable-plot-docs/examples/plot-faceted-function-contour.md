---
url: "https://observablehq.com/@observablehq/plot-faceted-function-contour"
title: "Faceted function contour"
---

# Faceted function contour

The [facets](https://observablehq.com/plot/features/facets) are passed as the third argument to the function of *x* and *y* for which we draw [contours](https://observablehq.com/plot/marks/contour). To draw a single function, see the simpler [Function contour](/@observablehq/plot-function-contour) notebook. Note that all the facets share the same thresholds.

```js
Plot.plot({
  height: 580,
  color: { type: "diverging", scheme: "PuOr" },
  fx: { tickFormat: (f) => f?.name },
  fy: { tickFormat: (f) => f?.name },
  marks: [
    Plot.contour({
      fill: (x, y, { fx, fy }) => fx(x) * fy(y),
      fx: [sin, sin, lin, lin],
      fy: [cos, lin, lin, cos],
      x1: 0,
      y1: 0,
      x2: fourPi,
      y2: fourPi,
      interval: 0.2
    }),
    Plot.frame()
  ]
})
```

```js
function lin(x) { return x / fourPi; }
```

```js
sin = Math.sin
```

```js
cos = Math.cos
```

```js
fourPi = 4 * Math.PI
```

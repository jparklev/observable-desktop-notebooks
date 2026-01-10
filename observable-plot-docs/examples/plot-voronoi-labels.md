---
url: "https://observablehq.com/@fil/plot-voronoi-labels"
title: "Voronoi labels"
---

# Voronoi labels

Using the [Voronoi diagram](https://github.com/d3/d3-delaunay) to limit label occlusion. See also [D3: Voronoi labels](https://observablehq.com/@d3/voronoi-labels), [occlusion](https://observablehq.com/@fil/occlusion), and [Plot issue #27](https://github.com/observablehq/plot/issues/27).

```js
viewof showVoronoi = Inputs.toggle({ label: "show voronoi", value: true })
```

```js
viewof activate = Inputs.toggle({ label: "move to centroids", value: true })
```

```js
viewof useProjection = Inputs.toggle({
  label: "mercator",
  value: false
})
```

```js
Plot.plot({
  width,
  height: useProjection ? width : width * 0.7,
  inset: useProjection ? 0 : 20,
  projection: useProjection ? { type: "mercator" } : undefined,
  marks: [
    useProjection ? Plot.sphere() : Plot.frame(),
    showVoronoi
      ? Plot.voronoiMesh(airports, { x: "longitude", y: "latitude" })
      : null,
    Plot.arrow(
      airports,
      maybeVoronoiCentroids({
        x1: "longitude",
        y1: "latitude",
        x2: "longitude",
        y2: "latitude",
        stroke: "black",
        strokeWidth: 0.7,
        bend: true,
        headLength: 0
      })
    ),
    Plot.dot(airports, {
      x: "longitude",
      y: "latitude",
      r: 1.5,
      fill: "black"
    }),
    Plot.text(
      airports,
      maybeVoronoiCentroids({
        x: "longitude",
        y: "latitude",
        text: (d) => d.name.split(/ /)[0],
        stroke: "white",
        strokeWidth: 7,
        fill: "black"
      })
    )
  ]
})
```

The custom **voronoiCentroids** options transform (code below) modifies the ﹤x, y﹥ position channels (for the text mark)—and ﹤x2, y2﹥, for the link mark— to reflect the cendroid of the associated polygon in the Voronoi diagram created by the data. This allows to position text labels where there is more space, thus limiting occlusion. If you pass a link or arrow mark, that has ﹤x1, y1, x2, y2﹥ positions, the ﹤x1, y1﹥ channels are left intact as the starting point, with ﹤x2, y2﹥ being the end point.

```js
voronoiCentroids = (options) =>
  Plot.initializer(
    options,
    function (
      data,
      facets,
      { x: X0, y: Y0, x2: X = X0, y2: Y = Y0 },
      { x, y },
      { width, height, marginLeft, marginRight, marginTop, marginBottom },
      { projection }
    ) {
      const n = X.value.length;
      const P = new Float64Array(2 * n).fill(NaN);
      let i;
      if (projection) {
        const stream = projection.stream({
          point(x, y) {
            P[2 * i] = x;
            P[2 * i + 1] = y;
          }
        });
        for (i = 0; i < n; ++i) stream.point(X.value[i], Y.value[i]);
      } else {
        for (i = 0; i < n; ++i) P[2 * i] = x ? x(X.value[i]) : X.value[i];
        for (i = 0; i < n; ++i) P[2 * i + 1] = y ? y(Y.value[i]) : Y.value[i];
      }

      for (const I of facets) {
        const v = new d3.Delaunay(P).voronoi([
          marginLeft,
          marginTop,
          width - marginRight,
          height - marginBottom
        ]);
        for (const [i, k] of I.entries())
          [X.value[i], Y.value[i]] = d3.polygonCentroid(v.cellPolygon(k) ?? []);
      }
      delete X.scale;
      delete Y.scale;
      return { data, facets };
    }
  )
```

```js
maybeVoronoiCentroids = activate ? voronoiCentroids : (options) => options
```

--- _data_

```js
airports = FileAttachment("airports.csv")
  .csv({ typed: true })
  .then((data) => data.filter((d, i) => i % 20 === 0))
```

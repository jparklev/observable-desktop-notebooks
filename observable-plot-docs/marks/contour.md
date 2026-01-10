---
url: "https://observablehq.com/plot/marks/contour"
title: "Contour mark | Plot"
---

# Contour mark [^0.6.2](https://github.com/observablehq/plot/releases/tag/v0.6.2 "added in v0.6.2") [​](https://observablehq.com/plot/marks/contour\#contour-mark)

TIP

To produce a heatmap instead of contours, see the [raster mark](https://observablehq.com/plot/marks/raster). For contours of estimated point density, see the [density mark](https://observablehq.com/plot/marks/density).

The **contour mark** draws [isolines](https://en.wikipedia.org/wiki/Contour_line) to delineate regions above and below a particular continuous value. These contours are computed by applying the [marching squares algorithm](https://en.wikipedia.org/wiki/Marching_squares) to a discrete grid. Like the [raster mark](https://observablehq.com/plot/marks/raster), the grid can be constructed either by [interpolating spatial samples](https://observablehq.com/plot/marks/raster#spatial-interpolators) (arbitrary points in **x** and **y**) or by sampling a continuous function _f_( _x_, _y_) along the grid.

For example, the contours below show the topography of the [Maungawhau volcano](https://en.wikipedia.org/wiki/Maungawhau), produced from a 87×61 grid of elevation samples.

05101520253035404550556001020304050607080 [Fork](https://observablehq.com/@observablehq/plot-stroked-contours "Open on Observable")

js

```
Plot.contour(volcano.values, {width: volcano.width, height: volcano.height}).plot()
```

Whereas the **value** option produces isolines suitable for stroking, the **fill** option produces filled contours. Setting the **fill** to [identity](https://observablehq.com/plot/features/transforms#identity) will apply a color encoding to the contour values, allowing the contour values to be read via a _color_ legend.

100120140160180Elevation (m)05101520253035404550556001020304050607080 [Fork](https://observablehq.com/@observablehq/plot-filled-contours "Open on Observable")

js

```
Plot.plot({
  color: {
    legend: true,
    label: "Elevation (m)"
  },
  marks: [\
    Plot.contour(volcano.values, {\
      width: volcano.width,\
      height: volcano.height,\
      fill: Plot.identity,\
      stroke: "black"\
    })\
  ]
})
```

INFO

Contours are drawn in ascending value order, with the highest value on top; hence, filled contour polygons overlap! If you are interested in isobands, please upvote [#1420](https://github.com/observablehq/plot/issues/1420).

The grid (`volcano.values` above) is a list of numbers `[103, 104, 104, …]`. The first number `103` is the elevation of the bottom-left corner. This grid is in [row-major order](https://en.wikipedia.org/wiki/Row-_and_column-major_order), meaning that the elevations of the first row are followed by the second row, then the third, and so on. Here’s a smaller grid to demonstrate the concept.

js

```
grid = ({
  "width": 10,
  "height": 10,
  "values": [\
     0,  0,  0,  0,  0,  0,  0,  0,  0,  0,\
     0,  1,  2,  3,  4,  5,  6,  7,  8,  9,\
     0,  2,  4,  6,  8, 10, 12, 14, 16, 18,\
     0,  3,  6,  9, 12, 15, 18, 21, 24, 27,\
     0,  4,  8, 12, 16, 20, 24, 28, 32, 36,\
     0,  5, 10, 15, 20, 25, 30, 35, 40, 45,\
     0,  6, 12, 18, 24, 30, 36, 42, 48, 54,\
     0,  7, 14, 21, 28, 35, 42, 49, 56, 63,\
     0,  8, 16, 24, 32, 40, 48, 56, 64, 72,\
     0,  9, 18, 27, 36, 45, 54, 63, 72, 81\
  ]
})
```

We can visualize this small grid directly with a [text mark](https://observablehq.com/plot/marks/text) using the same color encoding. Notice that the image below is flipped vertically relative to the data: the first row of the data is the _bottom_ of the image because below _y_ points up↑.

012345678910↑ row012345678910column →00000000000123456789024681012141618036912151821242704812162024283236051015202530354045061218243036424854071421283542495663081624324048566472091827364554637281 [Fork](https://observablehq.com/@observablehq/plot-small-grid-contours "Open on Observable")

js

```
Plot.plot({
  grid: true,
  x: {domain: [0, grid.width], label: "column"},
  y: {domain: [0, grid.height], label: "row"},
  marks: [\
    Plot.text(grid.values, {\
      text: Plot.identity,\
      fill: Plot.identity,\
      x: (d, i) => i % grid.width + 0.5,\
      y: (d, i) => Math.floor(i / grid.width) + 0.5\
    })\
  ]
})
```

Also notice that the grid points are offset by 0.5: they represent the _middle_ of each pixel rather than the corner. Below, the contour mark is laid under the text mark to show filled contours.

01234567891001234567891000000000000123456789024681012141618036912151821242704812162024283236051015202530354045061218243036424854071421283542495663081624324048566472091827364554637281 [Fork](https://observablehq.com/@observablehq/plot-small-grid-contours "Open on Observable")

js

```
Plot.plot({
  marks: [\
    Plot.contour(grid.values, {\
      width: grid.width,\
      height: grid.height,\
      fill: Plot.identity,\
      interval: 5\
    }),\
    Plot.text(grid.values, {\
      text: Plot.identity,\
      fill: "white",\
      x: (d, i) => i % grid.width + 0.5,\
      y: (d, i) => Math.floor(i / grid.width) + 0.5\
    })\
  ]
})
```

Similar to the [bin transform](https://observablehq.com/plot/transforms/bin), contour levels can be specified either with the **interval** option (above, a contour at each multiple of 5) or with the **thresholds** option (either a count of thresholds or an explicit array of values).

While the contour mark provides convenient shorthand for strictly gridded data, as above, it _also_ works with samples in arbitrary positions and arbitrary order. For example, in 1955 the [Great Britain aeromagnetic survey](https://www.bgs.ac.uk/datasets/gb-aeromagnetic-survey/) measured the Earth’s magnetic field by plane. Each sample recorded the longitude and latitude alongside the strength of the [IGRF](https://www.ncei.noaa.gov/products/international-geomagnetic-reference-field) in [nanoteslas](https://en.wikipedia.org/wiki/Tesla_(unit)).

```
LONGITUDE,LATITUDE,MAG_IGRF90
-2.36216,51.70945,7
-2.36195,51.71727,6
-2.36089,51.72404,9
-2.35893,51.73758,12
-2.35715,51.7532,18
-2.35737,51.76636,24
```

Using a [dot mark](https://observablehq.com/plot/marks/dot), we can make a quick scatterplot to see the irregular grid. We’ll use a _diverging_ color scale to distinguish positive and negative values.

51.751.851.952.052.152.252.352.452.552.6↑ LATITUDE−2.4−2.2−2.0−1.8−1.6−1.4−1.2−1.0−0.8−0.6LONGITUDE → [Fork](https://observablehq.com/@observablehq/plot-igrf90-dots "Open on Observable")

js

```
Plot.dot(ca55, {x: "LONGITUDE", y: "LATITUDE", fill: "MAG_IGRF90"}).plot({color: {type: "diverging"}})
```

Pass the same arguments to the contour mark for continuous contours.

51.751.851.952.052.152.252.352.452.552.6↑ LATITUDE−2.4−2.2−2.0−1.8−1.6−1.4−1.2−1.0−0.8−0.6LONGITUDE → [Fork](https://observablehq.com/@observablehq/plot-igrf90-contours "Open on Observable")

js

```
Plot.contour(ca55, {x: "LONGITUDE", y: "LATITUDE", fill: "MAG_IGRF90"}).plot({color: {type: "diverging"}})
```

As with the raster mark, the **blur** option applies a Gaussian blur to the underlying raster grid, resulting in smoother contours.

51.751.851.952.052.152.252.352.452.552.6↑ LATITUDE−2.4−2.2−2.0−1.8−1.6−1.4−1.2−1.0−0.8−0.6LONGITUDE → [Fork](https://observablehq.com/@observablehq/plot-blurred-contours "Open on Observable")

js

```
Plot.contour(ca55, {x: "LONGITUDE", y: "LATITUDE", fill: "MAG_IGRF90", blur: 4}).plot({color: {type: "diverging"}})
```

TIP

The contour mark also supports the **interpolate** option for control over [spatial interpolation](https://observablehq.com/plot/marks/raster#spatial-interpolators).

The contour mark supports Plot’s [projection system](https://observablehq.com/plot/features/projections). The chart below shows global atmospheric water vapor measurements from [NASA Earth Observations](https://neo.gsfc.nasa.gov/view.php?datasetId=MYDAL2_M_SKY_WV).

0246Water vapor (cm) [Fork](https://observablehq.com/@observablehq/plot-contours-projection "Open on Observable")

js

```
Plot.plot({
  projection: "equal-earth",
  color: {
    scheme: "BuPu",
    domain: [0, 6],
    legend: true,
    label: "Water vapor (cm)"
  },
  marks: [\
    Plot.contour(vapor, {\
      fill: Plot.identity,\
      width: 360,\
      height: 180,\
      x1: -180,\
      y1: 90,\
      x2: 180,\
      y2: -90,\
      blur: 1,\
      stroke: "black",\
      strokeWidth: 0.5,\
      clip: "sphere"\
    }),\
    Plot.sphere({stroke: "black"})\
  ]
})
```

As an alternative to interpolating discrete samples, you can supply values as a continuous function _f_( _x_, _y_); the contour mark will invoke this function for the midpoint of each pixel in the raster grid, similar to a WebGL fragment shader. For example, below we visualize the trigonometric function sin( _x_) cos( _y_), producing a checkerboard-like pattern.

−1.0−0.50.00.51.0sin(x) cos(y)024681012↑ y024681012141618x → [Fork](https://observablehq.com/@observablehq/plot-function-contour-2 "Open on Observable")

js

```
Plot.plot({
  aspectRatio: 1,
  x: {tickSpacing: 80, label: "x"},
  y: {tickSpacing: 80, label: "y"},
  color: {type: "diverging", legend: true, label: "sin(x) cos(y)"},
  marks: [\
    Plot.contour({\
      fill: (x, y) => Math.sin(x) * Math.cos(y),\
      x1: 0,\
      y1: 0,\
      x2: 6 * Math.PI,\
      y2: 4 * Math.PI\
    })\
  ]
})
```

TIP

When faceting, the sample function _f_( _x_, _y_) is passed a third argument of the facet values { _fx_, _fy_}.

## Contour options [​](https://observablehq.com/plot/marks/contour\#contour-options)

If _data_ is provided, it represents discrete samples in abstract coordinates **x** and **y**; the **value** channel specifies further abstract quantitative values ( _e.g._, height in a topographic map) to be [spatially interpolated](https://observablehq.com/plot/marks/raster#spatial-interpolators) to produce the underlying raster grid.

js

```
Plot.contour(volcano.values, {width: volcano.width, height: volcano.height, value: Plot.identity})
```

The **value** channel may alternatively be specified as a continuous function _f_( _x_, _y_) to be evaluated at each pixel centroid of the raster grid (without interpolation).

js

```
Plot.contour({x1: 0, y1: 0, x2: 4, y2: 4, value: (x, y) => Math.sin(x) * Math.cos(y)})
```

The resolution of the raster grid may be specified with the following options:

- **width** \- the number of pixels on each horizontal line
- **height** \- the number of lines; a positive integer

Alternatively, the raster dimensions may be imputed from the extent of _x_ and _y_ and a pixel size:

- **x1** \- the starting horizontal position; bound to the _x_ scale
- **x2** \- the ending horizontal position; bound to the _x_ scale
- **y1** \- the starting vertical position; bound to the _y_ scale
- **y2** \- the ending vertical position; bound to the _y_ scale
- **pixelSize** \- the screen size of a raster pixel; defaults to 1

If **width** is specified, **x1** defaults to 0 and **x2** defaults to **width**; likewise, if **height** is specified, **y1** defaults to 0 and **y2** defaults to **height**. Otherwise, if **data** is specified, **x1**, **y1**, **x2**, and **y2** respectively default to the frame’s left, top, right, and bottom coordinates. Lastly, if **data** is not specified (as when **value** is a function of _x_ and _y_), you must specify all of **x1**, **x2**, **y1**, and **y2** to define the raster domain (see below).

The contour mark shares many options with the [raster mark](https://observablehq.com/plot/marks/raster). The **interpolate** option is ignored when the **value** channel is a continuous function of _x_ and _y_, and otherwise defaults to _nearest_. For smoother contours, the **blur** option (default 0) specifies a non-negative pixel radius for smoothing prior to applying marching squares. The **smooth** option (default true) specifies whether to apply linear interpolation after marching squares when computing contour polygons. The **thresholds** and **interval** options specify the contour thresholds; see the [bin transform](https://observablehq.com/plot/transforms/bin) for details.

With the exception of the **x**, **y**, **x1**, **y1**, **x2**, **y2**, and **value** channels, the contour mark’s channels are not evaluated on the initial _data_ but rather on the contour multipolygons generated in the initializer. For example, to generate filled contours where the color corresponds to the contour threshold value:

js

```
Plot.contour(volcano.values, {width: volcano.width, height: volcano.height, value: Plot.identity, fill: "value"})
```

As shorthand, a single channel may be specified, in which case it is promoted to the _value_ channel.

js

```
Plot.contour(volcano.values, {width: volcano.width, height: volcano.height, fill: Plot.identity})
```

## contour( _data_, _options_) [​](https://observablehq.com/plot/marks/contour\#contour)

js

```
Plot.contour(volcano.values, {width: volcano.width, height: volcano.height, fill: Plot.identity})
```

Returns a new contour mark with the given (optional) _data_ and _options_.

Pager

[Previous pageCell](https://observablehq.com/plot/marks/cell)

[Next pageDelaunay](https://observablehq.com/plot/marks/delaunay)

[Home](https://observablehq.com/ "Home")

Resources

- [Forum](https://talk.observablehq.com/)
- [Slack](https://observablehq.com/slack/join)
- [Releases](https://github.com/observablehq/plot/releases)

Observable

- [Product](https://observablehq.com/product)
- [Plot](https://observablehq.com/plot)
- [Integrations](https://observablehq.com/data-integrations)
- [Pricing](https://observablehq.com/pricing)

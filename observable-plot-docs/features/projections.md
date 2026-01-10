---
url: "https://observablehq.com/plot/features/projections"
title: "Projections | Plot"
---

# Projections [^0.6.1](https://github.com/observablehq/plot/releases/tag/v0.6.1 "added in v0.6.1") [​](https://observablehq.com/plot/features/projections\#projections)

A **projection** maps abstract coordinates in _x_ and _y_ to pixel positions on screen. Most often, abstract coordinates are spherical (degrees longitude and latitude), as when rendering a geographic map. For example, below we show earthquakes in the last seven days with a magnitude of 2.5 or higher as reported by the [USGS](https://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php). Use the slider to adjust the _orthographic_ projection’s center of longitude.

Longitude: 90°

[Fork](https://observablehq.com/@observablehq/plot-earthquake-globe "Open on Observable")

js

```
Plot.plot({
  projection: {type: "orthographic", rotate: [-longitude, -30]},
  r: {transform: (d) => Math.pow(10, d)}, // convert Richter to amplitude
  marks: [\
    Plot.geo(land, {fill: "currentColor", fillOpacity: 0.2}),\
    Plot.sphere(),\
    Plot.dot(earthquakes, {x: "longitude", y: "latitude", r: "magnitude", stroke: "red", fill: "red", fillOpacity: 0.2})\
  ]
})
```

Above, a [geo mark](https://observablehq.com/plot/marks/geo) draws polygons representing land and a [sphere mark](https://observablehq.com/plot/marks/geo#sphere) draws the outline of the globe. A [dot mark](https://observablehq.com/plot/marks/dot) draws earthquakes as circles sized by magnitude.

The geo mark is “projection aware” so that it can handle all the nuances of projecting spherical polygons to the screen — leaning on [d3-geo](https://d3js.org/d3-geo) to provide [adaptive sampling](https://observablehq.com/@d3/adaptive-sampling) with configurable precision, [antimeridian cutting](https://observablehq.com/@d3/antimeridian-cutting), and clipping. The dot mark is not; instead, Plot applies the projection in place of the _x_ and _y_ scales. Hence, projections work with any mark that consumes continuous **x** and **y** channels — as well as marks that use **x1** & **y1** and **x2** & **y2**. Each mark implementation decides whether to handle projections specially or to treat the projection as any other position scale. (For example, the [line mark](https://observablehq.com/plot/marks/line) is projection-aware to draw geodesics.)

INFO

Marks that require _band_ scales (bars, cells, and ticks) cannot be used with projections. Likewise one-dimensional marks such as rules cannot be used, though see [#1164](https://github.com/observablehq/plot/issues/1164).

Plot provides a variety of built-in projections. And as above, all world projections can be rotated to show a different aspect.

Projection: azimuthal-equal-areaazimuthal-equidistantconic-equal-areaconic-equidistantequal-earthequirectangulargnomonicmercatororthographicstereographictransverse-mercator

[Fork](https://observablehq.com/@observablehq/plot-world-projections "Open on Observable")

js

```
Plot.plot({
  projection: "equirectangular",
  marks: [\
    Plot.graticule(),\
    Plot.geo(land, {fill: "currentColor"}),\
    Plot.sphere()\
  ]
})
```

Why so many? Each projection has its strengths and weaknesses:

- _conformal_ projections preserve angles and local shape,
- _equal-area_ projections preserve area (use these for choropleths),
- _equidistant_ projections preserve distance from one (or two) points,
- _azimuthal_ projections expand radially from a central feature,
- _cylindrical_ projections have symmetry around the axis of rotation,
- the _stereographic_ projection preserves circles, and
- the _gnomonic_ projection displays all great circles as straight lines!

No single projection is best at everything. It is impossible, for example, for a projection to be both conformal and equal-area.

In addition to world projections, Plot provides the U.S.-centric _albers-usa_ conic equal-area projection with an inset of Alaska and Hawaii. (Note that the scale for Alaska is diminished: it is projected at 0.35× its true relative area.)

[Fork](https://observablehq.com/@observablehq/plot-albers-usa-projection "Open on Observable")

js

```
Plot.plot({
  projection: "albers-usa",
  marks: [\
    Plot.geo(nation),\
    Plot.geo(statemesh, {strokeOpacity: 0.2})\
  ]
})
```

TIP

Use the _albers-usa_ projection for U.S.-centric choropleth maps.

For maps that focus on a specific region, use the **domain** option to zoom in. This object should be a GeoJSON object. For example, you can use [d3.geoCircle](https://d3js.org/d3-geo/shape#geoCircle) to generate a circle of a given radius centered at a given longitude and latitude. You can also use the **inset** options for a bit of padding around the **domain**.

Radius: 30.0°

[Fork](https://observablehq.com/@observablehq/plot-projection-domain "Open on Observable")

js

```
Plot.plot({
  projection: {
    type: "azimuthal-equidistant",
    rotate: [-9, -34],
    domain: circle,
    inset: 10
  },
  marks: [\
    Plot.graticule(),\
    Plot.geo(land, {fill: "currentColor", fillOpacity: 0.3}),\
    Plot.geo(circle, {stroke: "red", strokeWidth: 2}),\
    Plot.frame()\
  ]
})
```

js

```
circle = d3.geoCircle().center([9, 34]).radius(radius)()
```

If none of Plot’s built-in projections meet your needs, you can use any of [D3’s extended projections](https://github.com/d3/d3-geo-projection) by specifying the **projection** option as a function that returns a D3 projection. Below, a map of Antarctica in a polar aspect of the _azimuthal-equidistant_ projection.

[Fork](https://observablehq.com/@observablehq/plot-polar-projection "Open on Observable")

js

```
Plot.plot({
  width: 688,
  height: 688,
  projection: ({width, height}) => d3.geoAzimuthalEquidistant()
    .rotate([0, 90])
    .translate([width / 2, height / 2])
    .scale(width)
    .clipAngle(40),
  marks: [\
    Plot.graticule(),\
    Plot.geo(land, {fill: "currentColor"}),\
    Plot.frame()\
  ]
})
```

While this notebook mostly details spherical projections, you can use the _identity_ projection to display planar geometry. For example, below we draw a schematic of the second floor of the [Westport House](https://en.wikipedia.org/wiki/Westport_House) in Dundee, Ireland.

[Fork](https://observablehq.com/@observablehq/plot-floor-plan "Open on Observable")

js

```
Plot.geo(westport).plot({projection: {type: "identity", domain: westport}})
```

TIP

There’s also a _reflect-y_ projection in case _y_ points up↑, which is often the case with [projected reference systems](https://en.wikipedia.org/wiki/Projected_coordinate_system).

Naturally, Plot’s projection system is compatible with its [faceting system](https://observablehq.com/plot/features/facets). Below, a comic strip of sorts shows the locations of Walmart store openings in past decades.

1960’s1970’s1980’s1990’s2000’s [Fork](https://observablehq.com/@observablehq/plot-map-small-multiples "Open on Observable")

js

```
Plot.plot({
  marginLeft: 0,
  marginRight: 0,
  projection: "albers",
  fx: {
    interval: "10 years",
    tickFormat: (d) => `${d.getUTCFullYear()}’s`,
    label: null
  },
  marks: [\
    Plot.geo(statemesh, {strokeOpacity: 0.1}),\
    Plot.geo(nation),\
    Plot.dot(walmarts, {fx: "date", x: "longitude", y: "latitude", r: 1, fill: "currentColor"})\
  ]
})
```

INFO

This uses the [**interval** scale option](https://observablehq.com/plot/features/scales#scale-transforms) to bin temporal data into facets by decade.

To learn more about mapping with Plot, see our hands-on tutorials:

- [Build your first map with Observable Plot](https://observablehq.com/@observablehq/build-your-first-map-with-observable-plot)
- [Build your first choropleth map with Observable Plot](https://observablehq.com/@observablehq/build-your-first-choropleth-map-with-observable-plot)

## Projection options [​](https://observablehq.com/plot/features/projections\#projection-options)

The **projection** [plot option](https://observablehq.com/plot/features/plots) applies a two-dimensional (often geographic) projection in place of **x** and **y** scales. It is typically used in conjunction with a [geo mark](https://observablehq.com/plot/marks/geo) to produce a map, but can be used with any mark that supports **x** and **y** channels, such as [dot](https://observablehq.com/plot/marks/dot), [text](https://observablehq.com/plot/marks/text), [arrow](https://observablehq.com/plot/marks/arrow), and [rect](https://observablehq.com/plot/marks/rect). For marks that use **x1**, **y1**, **x2**, and **y2** channels, the two projected points are ⟨ _x1_, _y1_⟩ and ⟨ _x2_, _y2_⟩; otherwise, the projected point is ⟨ _x_, _y_⟩.

The following built-in named projections are supported:

- _equirectangular_ \- the equirectangular, or _plate carrée_, projection
- _orthographic_ \- the orthographic projection
- _stereographic_ \- the stereographic projection
- _mercator_ \- the Mercator projection
- _equal-earth_ \- the [Equal Earth projection](https://en.wikipedia.org/wiki/Equal_Earth_projection) by Šavrič _et al._
- _azimuthal-equal-area_ \- the azimuthal equal-area projection
- _azimuthal-equidistant_ \- the azimuthal equidistant projection
- _conic-conformal_ \- the conic conformal projection
- _conic-equal-area_ \- the conic equal-area projection
- _conic-equidistant_ \- the conic equidistant projection
- _gnomonic_ \- the gnomonic projection
- _transverse-mercator_ \- the transverse Mercator projection
- _albers_ \- the Albers’ conic equal-area projection
- _albers-usa_ \- a composite Albers conic equal-area projection suitable for the United States
- _identity_ \- the identity projection for planar geometry
- _reflect-y_ \- like the identity projection, but _y_ points up
- null (default) - the null projection for pre-projected geometry in screen coordinates

In addition to these named projections, the **projection** option may be specified as a [D3 projection](https://d3js.org/d3-geo/projection), or any custom projection that implements [_projection_.stream](https://d3js.org/d3-geo/stream), or a function that receives a configuration object ({ _width_, _height_, ... _options_}) and returns such a projection. In the last case, the width and height represent the frame dimensions minus any insets.

If the **projection** option is specified as an object, the following additional projection options are supported:

- **type** \- one of the projection names above
- **parallels** \- the [standard parallels](https://d3js.org/d3-geo/conic#conic_parallels) (for conic projections only)
- **precision** \- the [sampling threshold](https://d3js.org/d3-geo/projection#projection_precision)
- **rotate** \- a two- or three- element array of Euler angles to rotate the sphere
- **domain** \- a GeoJSON object to fit in the center of the (inset) frame
- **inset** \- inset by the given amount in pixels when fitting to the frame (default zero)
- **insetLeft** \- inset from the left edge of the frame (defaults to inset)
- **insetRight** \- inset from the right edge of the frame (defaults to inset)
- **insetTop** \- inset from the top edge of the frame (defaults to inset)
- **insetBottom** \- inset from the bottom edge of the frame (defaults to inset)
- **clip** \- the projection clipping method

The following projection clipping methods are supported for **clip**:

- _frame_ or true (default) - clip to the extent of the frame (including margins but not insets)
- a number - clip to a great circle of the given radius in degrees centered around the origin
- null or false - do not clip

Whereas the **clip** [mark option](https://observablehq.com/plot/features/marks#mark-options) is implemented using SVG clipping, the **clip** projection option affects the generated geometry and typically produces smaller SVG output.

Pager

[Previous pageScales](https://observablehq.com/plot/features/scales)

[Next pageTransforms](https://observablehq.com/plot/features/transforms)

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

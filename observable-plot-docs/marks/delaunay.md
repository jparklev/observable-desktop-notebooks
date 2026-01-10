---
url: "https://observablehq.com/plot/marks/delaunay"
title: "Delaunay marks | Plot"
---

# Delaunay marks [^0.5.1](https://github.com/observablehq/plot/releases/tag/v0.5.1 "added in v0.5.1") [​](https://observablehq.com/plot/marks/delaunay\#delaunay-marks)

Given set of points in **x** and **y**, the **Delaunay marks** compute the [Delaunay triangulation](https://en.wikipedia.org/wiki/Delaunay_triangulation), its dual the [Voronoi tessellation](https://en.wikipedia.org/wiki/Voronoi_diagram), and the [convex hull](https://en.wikipedia.org/wiki/Convex_hull).

The [voronoi mark](https://observablehq.com/plot/marks/delaunay#voronoi) computes the region closest to each point (its _Voronoi cell_). The cell can be empty if another point shares the exact same coordinates. Together, the cells cover the entire plot. Voronoi diagrams can group related points with color, for example.

AdelieChinstrapGentoo

34363840424446485052545658↑ culmen\_length\_mm1415161718192021culmen\_depth\_mm → [Fork](https://observablehq.com/@observablehq/plot-voronoi-scatterplot "Open on Observable")

js

```
Plot.plot({
  color: {legend: true},
  marks: [\
    Plot.voronoi(penguins, {x: "culmen_depth_mm", y: "culmen_length_mm", fill: "species", fillOpacity: 0.2, stroke: "white"}),\
    Plot.frame(),\
    Plot.dot(penguins, {x: "culmen_depth_mm", y: "culmen_length_mm", fill: "species"})\
  ]
})
```

Each cell is associated with a particular data point, and channels such as **stroke**, **fill**, **fillOpacity**, **strokeOpacity**, **href**, _etc._, work as they do on other marks, such as [dots](https://observablehq.com/plot/marks/dot).

To show the local density of a scatterplot, one can draw the whole boundary at once with [voronoiMesh](https://observablehq.com/plot/marks/delaunay#voronoiMesh). Whereas the [voronoi mark](https://observablehq.com/plot/marks/delaunay#voronoi) will draw shared cell boundaries twice, the mesh will draw them only once.

34363840424446485052545658↑ culmen\_length\_mm1415161718192021culmen\_depth\_mm → [Fork](https://observablehq.com/@observablehq/plot-voronoi-mesh "Open on Observable")

js

```
Plot.plot({
  marks: [\
    Plot.voronoiMesh(penguins, {x: "culmen_depth_mm", y: "culmen_length_mm"}),\
    Plot.dot(penguins, {x: "culmen_depth_mm", y: "culmen_length_mm", fill: "species"})\
  ]
})
```

The boundary between two neighboring Voronoi cells is a line segment defined by equal distance from their two respective points. The construction of the Voronoi diagram involves the computation of the Delaunay graph, which defines these neighbors. Use [delaunayMesh](https://observablehq.com/plot/marks/delaunay#delaunayMesh) to draw the graph.

34363840424446485052545658↑ culmen\_length\_mm1415161718192021culmen\_depth\_mm → [Fork](https://observablehq.com/@observablehq/plot-delaunay-mesh "Open on Observable")

js

```
Plot.plot({
  marks: [\
    Plot.delaunayMesh(penguins, {x: "culmen_depth_mm", y: "culmen_length_mm", z: "species", stroke: "species", strokeOpacity: 0.5}),\
    Plot.dot(penguins, {x: "culmen_depth_mm", y: "culmen_length_mm", fill: "species"})\
  ]
})
```

As shown above, the Delaunay graph is computed separately for each color; specifying **z**, **stroke**, or **fill** creates independent series.

Another derivative of the Delaunay graph is the convex hull of a set of points: the polygon with the minimum perimeter that contains all the points. The [hull mark](https://observablehq.com/plot/marks/delaunay#hull) will draw this hull.

34363840424446485052545658↑ culmen\_length\_mm1415161718192021culmen\_depth\_mm → [Fork](https://observablehq.com/@observablehq/plot-convex-hull "Open on Observable")

js

```
Plot.plot({
  marks: [\
    Plot.hull(penguins, {x: "culmen_depth_mm", y: "culmen_length_mm", fill: "species", fillOpacity: 0.2}),\
    Plot.dot(penguins, {x: "culmen_depth_mm", y: "culmen_length_mm", stroke: "species"})\
  ]
})
```

Using independent series is not recommended in the case of the voronoi and voronoiMesh marks as it will result in an unreadable chart due to overlapping Voronoi diagrams, but it can be useful to color the links of the Delaunay graph based on some property of data, such as the body mass of penguins below.

3,0004,0005,0006,000body\_mass\_g34363840424446485052545658↑ culmen\_length\_mm1415161718192021culmen\_depth\_mm → [Fork](https://observablehq.com/@observablehq/plot-delaunay-links "Open on Observable")

js

```
Plot.plot({
  color: {legend: true},
  marks: [\
    Plot.delaunayLink(penguins, {x: "culmen_depth_mm", y: "culmen_length_mm", stroke: "body_mass_g", strokeWidth: 1.5})\
  ]
})
```

CAUTION

The link color is driven by one arbitrary extremity of each edge; this might change in the future.

The Delaunay marks can be one-dimensional, too.

3,0003,5004,0004,5005,0005,5006,000body\_mass\_g → [Fork](https://observablehq.com/@observablehq/plot-one-dimensional-voronoi "Open on Observable")

js

```
Plot.plot({
  marks: [\
    Plot.voronoi(penguins, {x: "body_mass_g", fill: "species"}),\
    Plot.voronoiMesh(penguins, {x: "body_mass_g", stroke: "white", strokeOpacity: 1})\
  ]
})
```

The [Delaunay marks](https://observablehq.com/plot/marks/delaunay) also work with Plot’s [projection system](https://observablehq.com/plot/features/projections), as in this Voronoi diagram showing the distribution of Walmart stores in the contiguous United States.

[Fork](https://observablehq.com/@observablehq/plot-walmart-voronoi "Open on Observable")

js

```
Plot.plot({
  projection: "albers",
  marks: [\
    Plot.geo(nation),\
    Plot.dot(walmarts, {x: "longitude", y: "latitude", fill: "currentColor", r: 1}),\
    Plot.voronoiMesh(walmarts, {x: "longitude", y: "latitude"})\
  ]
})
```

CAUTION

Distances between projected points are not exactly proportional to the corresponding distances on the sphere. This [creates a discrepancy](https://observablehq.com/@observablehq/planar-vs-spherical-voronoi) between the planar Voronoi diagram and its spherical counterpart. For greater accuracy, use [d3-geo-voronoi](https://github.com/Fil/d3-geo-voronoi) with the [geo mark](https://observablehq.com/plot/marks/geo).

## delaunayLink( _data_, _options_) [​](https://observablehq.com/plot/marks/delaunay\#delaunayLink)

js

```
Plot.delaunayLink(penguins, {x: "culmen_depth_mm", y: "culmen_length_mm"})
```

Draws links for each edge of the Delaunay triangulation of the points given by the **x** and **y** channels. Supports the same options as the [link mark](https://observablehq.com/plot/marks/link), except that **x1**, **y1**, **x2**, and **y2** are derived automatically from **x** and **y**. When an aesthetic channel is specified (such as **stroke** or **strokeWidth**), the link inherits the corresponding channel value from one of its two endpoints arbitrarily.

If a **z** channel is specified, the input points are grouped by _z_, and separate Delaunay triangulations are constructed for each group.

## delaunayMesh( _data_, _options_) [​](https://observablehq.com/plot/marks/delaunay\#delaunayMesh)

js

```
Plot.delaunayMesh(penguins, {x: "culmen_depth_mm", y: "culmen_length_mm"})
```

Draws a mesh of the Delaunay triangulation of the points given by the **x** and **y** channels. The **stroke** option defaults to _currentColor_, and the **strokeOpacity** defaults to 0.2. The **fill** option is not supported. When an aesthetic channel is specified (such as **stroke** or **strokeWidth**), the mesh inherits the corresponding channel value from one of its constituent points arbitrarily.

If a **z** channel is specified, the input points are grouped by _z_, and separate Delaunay triangulations are constructed for each group.

## hull( _data_, _options_) [​](https://observablehq.com/plot/marks/delaunay\#hull)

js

```
Plot.hull(penguins, {x: "culmen_depth_mm", y: "culmen_length_mm"})
```

Draws a convex hull around the points given by the **x** and **y** channels. The **stroke** option defaults to _currentColor_ and the **fill** option defaults to _none_. When an aesthetic channel is specified (such as **stroke** or **strokeWidth**), the hull inherits the corresponding channel value from one of its constituent points arbitrarily.

If a **z** channel is specified, the input points are grouped by _z_, and separate convex hulls are constructed for each group. If the **z** channel is not specified, it defaults to either the **fill** channel, if any, or the **stroke** channel, if any.

## voronoi( _data_, _options_) [​](https://observablehq.com/plot/marks/delaunay\#voronoi)

js

```
Plot.voronoi(penguins, {x: "culmen_depth_mm", y: "culmen_length_mm"})
```

Draws polygons for each cell of the Voronoi tessellation of the points given by the **x** and **y** channels.

If a **z** channel is specified, the input points are grouped by _z_, and separate Voronoi tessellations are constructed for each group.

## voronoiMesh( _data_, _options_) [​](https://observablehq.com/plot/marks/delaunay\#voronoiMesh)

js

```
Plot.voronoiMesh(penguins, {x: "culmen_depth_mm", y: "culmen_length_mm"})
```

Draws a mesh for the cell boundaries of the Voronoi tessellation of the points given by the **x** and **y** channels. The **stroke** option defaults to _currentColor_, and the **strokeOpacity** defaults to 0.2. The **fill** option is not supported. When an aesthetic channel is specified (such as **stroke** or **strokeWidth**), the mesh inherits the corresponding channel value from one of its constituent points arbitrarily.

If a **z** channel is specified, the input points are grouped by _z_, and separate Voronoi tessellations are constructed for each group.

Pager

[Previous pageContour](https://observablehq.com/plot/marks/contour)

[Next pageDensity](https://observablehq.com/plot/marks/density)

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

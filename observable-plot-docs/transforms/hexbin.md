---
url: "https://observablehq.com/plot/transforms/hexbin"
title: "Hexbin transform | Plot"
---

# Hexbin transform [^0.5.0](https://github.com/observablehq/plot/releases/tag/v0.5.0 "added in v0.5.0") [​](https://observablehq.com/plot/transforms/hexbin\#hexbin-transform)

The **hexbin transform** groups two-dimensional quantitative or temporal data — continuous measurements such as heights, weights, or temperatures — into discrete hexagonal bins. You can then compute summary statistics for each bin, such as a count, sum, or proportion. The hexbin transform is most often used to make heatmaps with the [dot mark](https://observablehq.com/plot/marks/dot).

For example, the heatmap below shows the weights and heights of Olympic athletes. The color of each hexagon represents the number ( _count_) of athletes with similar weight and height.

1.31.41.51.61.71.81.92.02.12.2↑ height406080100120140160weight → [Fork](https://observablehq.com/@observablehq/plot-olympians-hexbin "Open on Observable")

js

```
Plot
  .dot(olympians, Plot.hexbin({fill: "count"}, {x: "weight", y: "height"}))
  .plot({color: {scheme: "YlGnBu"}})
```

Whereas the [bin transform](https://observablehq.com/plot/transforms/bin) produces rectangular bins and operates on abstract data, the hexbin transform produces hexagonal bins and operates in “screen space” ( _i.e._, pixel coordinates) after the _x_ and _y_ scales have been applied to the data. And whereas the bin transform produces **x1**, **y1**, **x2**, **y2** representing rectangular extents, the hexbin transform produces **x** and **y** representing hexagon centers.

To produce an areal encoding as in a bubble map, output **r**. In this case, the default range of the _r_ scale is set such that the hexagons do not overlap. The **binWidth** option, which defaults to 20, specifies the distance between centers of neighboring hexagons in pixels.

Bin width: 20.0

1.31.41.51.61.71.81.92.02.12.2↑ height406080100120140160weight → [Fork](https://observablehq.com/@observablehq/plot-hexbin-binwidth "Open on Observable")

js

```
Plot
  .dot(olympians, Plot.hexbin({r: "count"}, {x: "weight", y: "height", binWidth}))
  .plot()
```

If desired, you can output both **fill** and **r** for a redundant encoding.

1.31.41.51.61.71.81.92.02.12.2↑ height406080100120140160weight → [Fork](https://observablehq.com/@observablehq/plot-hexbin-redundant "Open on Observable")

js

```
Plot
  .dot(olympians, Plot.hexbin({fill: "count", r: "count"}, {x: "weight", y: "height", stroke: "currentColor"}))
  .plot({color: {scheme: "YlGnBu"}})
```

TIP

Setting a **stroke** ensures that the smallest hexagons are visible.

Alternatively, the **fill** and **r** channels can encode independent (or “bivariate”) dimensions of data. Below, the **r** channel uses _count_ as before, while the **fill** channel uses _mode_ to show the most frequent sex of athletes in each hexagon. The larger athletes are more likely to be male, while the smaller athletes are more likely to be female.

1.31.41.51.61.71.81.92.02.12.2↑ height406080100120140160weight → [Fork](https://observablehq.com/@observablehq/plot-bivariate-hexbin "Open on Observable")

js

```
Plot
  .dot(olympians, Plot.hexbin({fill: "mode", r: "count"}, {x: "weight", y: "height", fill: "sex"}))
  .plot()
```

Using **z**, the hexbin transform will partition hexagons by ordinal value. If **z** is not specified, it defaults to **fill** (if there is no **fill** output channel) or **stroke** (if there is no **stroke** output channel). Setting **z** to _sex_ in the chart above, and switching to **stroke** instead of **fill**, produces separate overlapping hexagons for each sex.

1.31.41.51.61.71.81.92.02.12.2↑ height406080100120140160weight → [Fork](https://observablehq.com/@observablehq/plot-overlapping-hexbin "Open on Observable")

js

```
Plot
  .dot(olympians, Plot.hexbin({stroke: "mode", r: "count"}, {x: "weight", y: "height", z: "sex", stroke: "sex"}))
  .plot()
```

The hexbin transform can be paired with any mark that supports **x** and **y** channels (which is almost all of them). The [text mark](https://observablehq.com/plot/marks/text) is useful for labelling. By setting the **text** output channel, you can derive the text from the binned contents.

1.31.41.51.61.71.81.92.02.12.2↑ height406080100120140160weight →3893792726336138776124923721635823611602351925020313435677572370902291352016673079042114924710491336724834166374411114918312812471043659110106112286352315602547438135410936472215534346264821958104096501127891921781064428201351578172044158861741319174158316116331711217251347106181611363224941377411445134552126324321251312116116111172231111212111421111116121141111212111111111212121111111111111111 [Fork](https://observablehq.com/@observablehq/plot-hexbin-text "Open on Observable")

js

```
Plot
  .text(olympians, Plot.hexbin({text: "count"}, {x: "weight", y: "height"}))
  .plot()
```

The hexbin transform also works with Plot’s [projection system](https://observablehq.com/plot/features/projections). Below, hexagon size represents the number of nearby Walmart stores, while color represents the date the first nearby Walmart store opened. (The first Walmart opened in Rogers, Arkansas.)

1970198019902000First year opened [Fork](https://observablehq.com/@observablehq/plot-hexbin-map "Open on Observable")

js

```
Plot.plot({
  projection: "albers",
  r: {range: [0, 16]},
  color: {scheme: "spectral", label: "First year opened", legend: true},
  marks: [\
    Plot.geo(statemesh, {strokeOpacity: 0.5}),\
    Plot.geo(nation),\
    Plot.dot(walmarts, Plot.hexbin({r: "count", fill: "min"}, {x: "longitude", y: "latitude", fill: "date"}))\
  ]
})
```

CAUTION

Beware the [modifiable areal unit problem](https://en.wikipedia.org/wiki/Modifiable_areal_unit_problem). On a small scale map, this is compounded by the Earth’s curvature, which makes it impossible to create an accurate and regular grid. Use an equal-area projection when binning.

The [hexgrid mark](https://observablehq.com/plot/marks/hexgrid) draws the base hexagonal grid as a mesh. This is useful for showing the empty hexagons, since the hexbin transform does not output empty bins (and unlike the bin transform, the hexbin transform does not currently support the **filter** option).

1.31.41.51.61.71.81.92.02.12.2↑ height406080100120140160weight → [Fork](https://observablehq.com/@observablehq/plot-hexgrid-demo "Open on Observable")

js

```
Plot.plot({
  marks: [\
    Plot.hexgrid(),\
    Plot.dot(olympians, Plot.hexbin({r: "count"}, {x: "weight", y: "height", fill: "currentColor"}))\
  ]
})
```

The hexbin transform defaults the **symbol** option to _hexagon_, but you can override it. The [circle constructor](https://observablehq.com/plot/marks/dot#circle) changes it to _circle_.

1.31.41.51.61.71.81.92.02.12.2↑ height406080100120140160weight → [Fork](https://observablehq.com/@observablehq/plot-hexbin-circle "Open on Observable")

js

```
Plot.circle(olympians, Plot.hexbin({r: "count"}, {x: "weight", y: "height"})).plot()
```

Hexbins work best when there is an interesting density of dots in the center of the chart, but sometimes hexagons “escape” the edge of the frame and cover the axes. To prevent this, you can use the **inset** [scale option](https://observablehq.com/plot/features/scales) to reserve space on the edges of the frame.

1.31.41.51.61.71.81.92.02.12.2↑ height406080100120140160weight → [Fork](https://observablehq.com/@observablehq/plot-hexbin-inset "Open on Observable")

js

```
Plot
  .dot(olympians, Plot.hexbin({fill: "count"}, {x: "weight", y: "height"}))
  .plot({inset: 10, color: {scheme: "YlGnBu"}})
```

TIP

You can also set the dot’s **clip** option to true to prevent the hexagons from escaping.

Alternatively, use the [axis mark](https://observablehq.com/plot/marks/axis) to draw axes on top of the hexagons.

406080100120140160weight →1.31.41.51.61.71.81.92.02.12.2↑ height [Fork](https://observablehq.com/@observablehq/plot-hexbin-and-axes "Open on Observable")

js

```
Plot.plot({
  color: {scheme: "YlGnBu"},
  marks: [\
    Plot.dot(olympians, Plot.hexbin({fill: "count"}, {x: "weight", y: "height"})),\
    Plot.axisX(),\
    Plot.axisY()\
  ]
})
```

## Hexbin options [​](https://observablehq.com/plot/transforms/hexbin\#hexbin-options)

The _options_ must specify the **x** and **y** channels. The **binWidth** option (default 20) defines the distance between centers of neighboring hexagons in pixels. If any of **z**, **fill**, or **stroke** is a channel, the first of these channels will be used to subdivide bins.

The _outputs_ options are similar to the [bin transform](https://observablehq.com/plot/transforms/bin); for each hexagon, an output channel value is derived by reducing the corresponding binned input channel values. The _outputs_ object specifies the reducer for each output channel.

The following named reducers are supported:

- _first_ \- the first value, in input order
- _last_ \- the last value, in input order
- _count_ \- the number of elements (frequency)
- _distinct_ \- the number of distinct values
- _sum_ \- the sum of values
- _proportion_ \- the sum proportional to the overall total (weighted frequency)
- _proportion-facet_ \- the sum proportional to the facet total
- _min_ \- the minimum value
- _min-index_ \- the zero-based index of the minimum value
- _max_ \- the maximum value
- _max-index_ \- the zero-based index of the maximum value
- _mean_ \- the mean value (average)
- _median_ \- the median value
- _deviation_ \- the [standard deviation](https://d3js.org/d3-array/summarize#deviation)
- _variance_ \- the variance per [Welford’s algorithm](https://en.wikipedia.org/wiki/Algorithms_for_calculating_variance#Welford's_online_algorithm)
- _mode_ \- the value with the most occurrences
- _identity_ \- the array of values
- _x_ [^0.6.12](https://github.com/observablehq/plot/releases/tag/v0.6.12 "added in v0.6.12") \- the hexagon’s _x_ center
- _y_ [^0.6.12](https://github.com/observablehq/plot/releases/tag/v0.6.12 "added in v0.6.12") \- the hexagon’s _y_ center

In addition, a reducer may be specified as:

- a function to be passed the array of values for each bin and the center of the bin
- an object with a _reduceIndex_ method

In the last case, the **reduceIndex** method is repeatedly passed three arguments: the index for each bin (an array of integers), the input channel’s array of values, and the center of the bin (an object {data, x, y}); it must then return the corresponding aggregate value for the bin.

Most reducers require binding the output channel to an input channel; for example, if you want the **y** output channel to be a _sum_ (not merely a count), there should be a corresponding **y** input channel specifying which values to sum. If there is not, _sum_ will be equivalent to _count_.

## hexbin( _outputs_, _options_) [​](https://observablehq.com/plot/transforms/hexbin\#hexbin)

js

```
Plot.dot(olympians, Plot.hexbin({fill: "count"}, {x: "weight", y: "height"}))
```

Bins hexagonally on **x** and **y**. Also groups on the first channel of **z**, **fill**, or **stroke**, if any.

Pager

[Previous pageGroup](https://observablehq.com/plot/transforms/group)

[Next pageInterval](https://observablehq.com/plot/transforms/interval)

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

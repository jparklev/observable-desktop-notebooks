---
url: "https://observablehq.com/plot/what-is-plot"
title: "What is Plot? | Plot"
---

# What is Plot? [​](https://observablehq.com/plot/what-is-plot\#what-is-plot)

**Observable Plot** is a free, open-source, JavaScript library for visualizing tabular data, focused on accelerating exploratory data analysis. It has a concise, memorable, yet expressive interface, featuring [scales](https://observablehq.com/plot/features/scales) and [layered marks](https://observablehq.com/plot/features/marks) in the _grammar of graphics_ style popularized by [Leland Wilkinson](https://en.wikipedia.org/wiki/Leland_Wilkinson) and [Hadley Wickham](https://en.wikipedia.org/wiki/Hadley_Wickham) and inspired by the earlier ideas of [Jacques Bertin](https://en.wikipedia.org/wiki/Jacques_Bertin). And there are [plenty of examples](https://observablehq.com/@observablehq/plot-gallery) to learn from and copy-paste.

In the spirit of _show don’t tell_, here’s a scatterplot of body measurements of athletes from the [2016 Summer Olympics](https://flother.is/2017/olympic-games-data/).

femalemale

1.31.41.51.61.71.81.92.02.12.2↑ height406080100120140160weight → [Fork](https://observablehq.com/@observablehq/plot-olympians-scatterplot "Open on Observable")

js

```
Plot
  .dot(olympians, {x: "weight", y: "height", stroke: "sex"})
  .plot({color: {legend: true}})
```

A plot specification assigns columns of data ( _weight_, _height_, and _sex_) to visual properties of marks ( **x**, **y**, and **stroke**). Plot does the rest! You can configure much more, if needed, but Plot’s goal is to help you get a meaningful visualization quickly to accelerate analysis.

This scatterplot suffers from overplotting: many dots are drawn in the same spot, so it’s hard to perceive density. We can fix this by applying a [bin transform](https://observablehq.com/plot/transforms/bin) to group athletes of similar height and weight (and sex), and then use opacity to encode the number of athletes in the bin.

1.21.31.41.51.61.71.81.92.02.12.2↑ height406080100120140160weight → [Fork](https://observablehq.com/@observablehq/plot-olympians-bins "Open on Observable")

js

```
Plot.rect(olympians, Plot.bin({fillOpacity: "count"}, {x: "weight", y: "height", fill: "sex", inset: 0})).plot()
```

Or we could try the [density mark](https://observablehq.com/plot/marks/density).

1.31.41.51.61.71.81.92.02.12.2↑ height406080100120140160weight → [Fork](https://observablehq.com/@observablehq/plot-olympians-density "Open on Observable")

js

```
Plot.density(olympians, {x: "weight", y: "height", stroke: "sex"}).plot()
```

A simpler take on this data is to focus on one dimension: weight. We can use the bin transform again to make a histogram with weight on the _x_-axis and frequency on the _y_-axis. This plot uses a [rect mark](https://observablehq.com/plot/marks/rect) and an implicit [stack transform](https://observablehq.com/plot/transforms/stack).

050100150200250300350400450500550600↑ Frequency406080100120140160weight → [Fork](https://observablehq.com/@observablehq/plot-vertical-histogram "Open on Observable")

js

```
Plot.rectY(olympians, Plot.binX({y: "count"}, {x: "weight", fill: "sex"})).plot()
```

Or if we’d prefer to show the two distributions separately as small multiples, we can [facet](https://observablehq.com/plot/features/facets) the data along _y_ (keeping the _fill_ encoding for consistency, and adding grid lines and a rule at _y_ = 0 to improve readability).

femalemalesex01002003004000100200300400↑ Frequency406080100120140160weight → [Fork](https://observablehq.com/@observablehq/plot-faceted-histogram "Open on Observable")

js

```
Plot.plot({
  grid: true,
  marks: [\
    Plot.rectY(olympians, Plot.binX({y: "count"}, {x: "weight", fill: "sex", fy: "sex"})),\
    Plot.ruleY([0])\
  ]
})
```

## What can Plot do? [​](https://observablehq.com/plot/what-is-plot\#what-can-plot-do)

Because marks are composable, and because you can extend Plot with custom marks, you can make almost anything with it — much more than the charts above! The following [tree diagram](https://observablehq.com/plot/marks/tree) of the documentation gives a sense of what’s ”in the box” with Plot. Peruse our [gallery of examples](https://observablehq.com/@observablehq/plot-gallery) for more inspiration.

/Plot/Plot/Introduction/Plot/Features/Plot/Marks/Plot/Transforms/Plot/Interactions [/Plot/API index](https://observablehq.com/plot/api) [/Plot/Introduction/What is Plot?](https://observablehq.com/plot/what-is-plot) [/Plot/Introduction/Why Plot?](https://observablehq.com/plot/why-plot) [/Plot/Introduction/Getting started](https://observablehq.com/plot/getting-started) [/Plot/Introduction/Examples](https://observablehq.com/plot/.https://observablehq.com/@observablehq/plot-gallery) [/Plot/Features/Plots](https://observablehq.com/plot/features/plots) [/Plot/Features/Marks](https://observablehq.com/plot/features/marks) [/Plot/Features/Scales](https://observablehq.com/plot/features/scales) [/Plot/Features/Projections](https://observablehq.com/plot/features/projections) [/Plot/Features/Transforms](https://observablehq.com/plot/features/transforms) [/Plot/Features/Interactions](https://observablehq.com/plot/features/interactions) [/Plot/Features/Facets](https://observablehq.com/plot/features/facets) [/Plot/Features/Legends](https://observablehq.com/plot/features/legends) [/Plot/Features/Curves](https://observablehq.com/plot/features/curves) [/Plot/Features/Formats](https://observablehq.com/plot/features/formats) [/Plot/Features/Intervals](https://observablehq.com/plot/features/intervals) [/Plot/Features/Markers](https://observablehq.com/plot/features/markers) [/Plot/Features/Shorthand](https://observablehq.com/plot/features/shorthand) [/Plot/Features/Accessibility](https://observablehq.com/plot/features/accessibility) [/Plot/Marks/Area](https://observablehq.com/plot/marks/area) [/Plot/Marks/Arrow](https://observablehq.com/plot/marks/arrow) [/Plot/Marks/Auto](https://observablehq.com/plot/marks/auto) [/Plot/Marks/Axis](https://observablehq.com/plot/marks/axis) [/Plot/Marks/Bar](https://observablehq.com/plot/marks/bar) [/Plot/Marks/Bollinger](https://observablehq.com/plot/marks/bollinger) [/Plot/Marks/Box](https://observablehq.com/plot/marks/box) [/Plot/Marks/Cell](https://observablehq.com/plot/marks/cell) [/Plot/Marks/Contour](https://observablehq.com/plot/marks/contour) [/Plot/Marks/Delaunay](https://observablehq.com/plot/marks/delaunay) [/Plot/Marks/Density](https://observablehq.com/plot/marks/density) [/Plot/Marks/Difference](https://observablehq.com/plot/marks/difference) [/Plot/Marks/Dot](https://observablehq.com/plot/marks/dot) [/Plot/Marks/Frame](https://observablehq.com/plot/marks/frame) [/Plot/Marks/Geo](https://observablehq.com/plot/marks/geo) [/Plot/Marks/Grid](https://observablehq.com/plot/marks/grid) [/Plot/Marks/Hexgrid](https://observablehq.com/plot/marks/hexgrid) [/Plot/Marks/Image](https://observablehq.com/plot/marks/image) [/Plot/Marks/Line](https://observablehq.com/plot/marks/line) [/Plot/Marks/Linear regression](https://observablehq.com/plot/marks/linear-regression) [/Plot/Marks/Link](https://observablehq.com/plot/marks/link) [/Plot/Marks/Raster](https://observablehq.com/plot/marks/raster) [/Plot/Marks/Rect](https://observablehq.com/plot/marks/rect) [/Plot/Marks/Rule](https://observablehq.com/plot/marks/rule) [/Plot/Marks/Text](https://observablehq.com/plot/marks/text) [/Plot/Marks/Tick](https://observablehq.com/plot/marks/tick) [/Plot/Marks/Tip](https://observablehq.com/plot/marks/tip) [/Plot/Marks/Tree](https://observablehq.com/plot/marks/tree) [/Plot/Marks/Vector](https://observablehq.com/plot/marks/vector) [/Plot/Marks/Waffle](https://observablehq.com/plot/marks/waffle) [/Plot/Transforms/Bin](https://observablehq.com/plot/transforms/bin) [/Plot/Transforms/Centroid](https://observablehq.com/plot/transforms/centroid) [/Plot/Transforms/Dodge](https://observablehq.com/plot/transforms/dodge) [/Plot/Transforms/Filter](https://observablehq.com/plot/transforms/filter) [/Plot/Transforms/Group](https://observablehq.com/plot/transforms/group) [/Plot/Transforms/Hexbin](https://observablehq.com/plot/transforms/hexbin) [/Plot/Transforms/Interval](https://observablehq.com/plot/transforms/interval) [/Plot/Transforms/Map](https://observablehq.com/plot/transforms/map) [/Plot/Transforms/Normalize](https://observablehq.com/plot/transforms/normalize) [/Plot/Transforms/Select](https://observablehq.com/plot/transforms/select) [/Plot/Transforms/Shift](https://observablehq.com/plot/transforms/shift) [/Plot/Transforms/Sort](https://observablehq.com/plot/transforms/sort) [/Plot/Transforms/Stack](https://observablehq.com/plot/transforms/stack) [/Plot/Transforms/Tree](https://observablehq.com/plot/transforms/tree) [/Plot/Transforms/Window](https://observablehq.com/plot/transforms/window) [/Plot/Interactions/Crosshair](https://observablehq.com/plot/interactions/crosshair) [/Plot/Interactions/Pointer](https://observablehq.com/plot/interactions/pointer)[API index/Plot/API index](https://observablehq.com/plot/api) [What is Plot?/Plot/Introduction/What is Plot?](https://observablehq.com/plot/what-is-plot) [Why Plot?/Plot/Introduction/Why Plot?](https://observablehq.com/plot/why-plot) [Getting started/Plot/Introduction/Getting started](https://observablehq.com/plot/getting-started) [Examples/Plot/Introduction/Examples](https://observablehq.com/plot/.https://observablehq.com/@observablehq/plot-gallery) [Plots/Plot/Features/Plots](https://observablehq.com/plot/features/plots) [Marks/Plot/Features/Marks](https://observablehq.com/plot/features/marks) [Scales/Plot/Features/Scales](https://observablehq.com/plot/features/scales) [Projections/Plot/Features/Projections](https://observablehq.com/plot/features/projections) [Transforms/Plot/Features/Transforms](https://observablehq.com/plot/features/transforms) [Interactions/Plot/Features/Interactions](https://observablehq.com/plot/features/interactions) [Facets/Plot/Features/Facets](https://observablehq.com/plot/features/facets) [Legends/Plot/Features/Legends](https://observablehq.com/plot/features/legends) [Curves/Plot/Features/Curves](https://observablehq.com/plot/features/curves) [Formats/Plot/Features/Formats](https://observablehq.com/plot/features/formats) [Intervals/Plot/Features/Intervals](https://observablehq.com/plot/features/intervals) [Markers/Plot/Features/Markers](https://observablehq.com/plot/features/markers) [Shorthand/Plot/Features/Shorthand](https://observablehq.com/plot/features/shorthand) [Accessibility/Plot/Features/Accessibility](https://observablehq.com/plot/features/accessibility) [Area/Plot/Marks/Area](https://observablehq.com/plot/marks/area) [Arrow/Plot/Marks/Arrow](https://observablehq.com/plot/marks/arrow) [Auto/Plot/Marks/Auto](https://observablehq.com/plot/marks/auto) [Axis/Plot/Marks/Axis](https://observablehq.com/plot/marks/axis) [Bar/Plot/Marks/Bar](https://observablehq.com/plot/marks/bar) [Bollinger/Plot/Marks/Bollinger](https://observablehq.com/plot/marks/bollinger) [Box/Plot/Marks/Box](https://observablehq.com/plot/marks/box) [Cell/Plot/Marks/Cell](https://observablehq.com/plot/marks/cell) [Contour/Plot/Marks/Contour](https://observablehq.com/plot/marks/contour) [Delaunay/Plot/Marks/Delaunay](https://observablehq.com/plot/marks/delaunay) [Density/Plot/Marks/Density](https://observablehq.com/plot/marks/density) [Difference/Plot/Marks/Difference](https://observablehq.com/plot/marks/difference) [Dot/Plot/Marks/Dot](https://observablehq.com/plot/marks/dot) [Frame/Plot/Marks/Frame](https://observablehq.com/plot/marks/frame) [Geo/Plot/Marks/Geo](https://observablehq.com/plot/marks/geo) [Grid/Plot/Marks/Grid](https://observablehq.com/plot/marks/grid) [Hexgrid/Plot/Marks/Hexgrid](https://observablehq.com/plot/marks/hexgrid) [Image/Plot/Marks/Image](https://observablehq.com/plot/marks/image) [Line/Plot/Marks/Line](https://observablehq.com/plot/marks/line) [Linear regression/Plot/Marks/Linear regression](https://observablehq.com/plot/marks/linear-regression) [Link/Plot/Marks/Link](https://observablehq.com/plot/marks/link) [Raster/Plot/Marks/Raster](https://observablehq.com/plot/marks/raster) [Rect/Plot/Marks/Rect](https://observablehq.com/plot/marks/rect) [Rule/Plot/Marks/Rule](https://observablehq.com/plot/marks/rule) [Text/Plot/Marks/Text](https://observablehq.com/plot/marks/text) [Tick/Plot/Marks/Tick](https://observablehq.com/plot/marks/tick) [Tip/Plot/Marks/Tip](https://observablehq.com/plot/marks/tip) [Tree/Plot/Marks/Tree](https://observablehq.com/plot/marks/tree) [Vector/Plot/Marks/Vector](https://observablehq.com/plot/marks/vector) [Waffle/Plot/Marks/Waffle](https://observablehq.com/plot/marks/waffle) [Bin/Plot/Transforms/Bin](https://observablehq.com/plot/transforms/bin) [Centroid/Plot/Transforms/Centroid](https://observablehq.com/plot/transforms/centroid) [Dodge/Plot/Transforms/Dodge](https://observablehq.com/plot/transforms/dodge) [Filter/Plot/Transforms/Filter](https://observablehq.com/plot/transforms/filter) [Group/Plot/Transforms/Group](https://observablehq.com/plot/transforms/group) [Hexbin/Plot/Transforms/Hexbin](https://observablehq.com/plot/transforms/hexbin) [Interval/Plot/Transforms/Interval](https://observablehq.com/plot/transforms/interval) [Map/Plot/Transforms/Map](https://observablehq.com/plot/transforms/map) [Normalize/Plot/Transforms/Normalize](https://observablehq.com/plot/transforms/normalize) [Select/Plot/Transforms/Select](https://observablehq.com/plot/transforms/select) [Shift/Plot/Transforms/Shift](https://observablehq.com/plot/transforms/shift) [Sort/Plot/Transforms/Sort](https://observablehq.com/plot/transforms/sort) [Stack/Plot/Transforms/Stack](https://observablehq.com/plot/transforms/stack) [Tree/Plot/Transforms/Tree](https://observablehq.com/plot/transforms/tree) [Window/Plot/Transforms/Window](https://observablehq.com/plot/transforms/window) [Crosshair/Plot/Interactions/Crosshair](https://observablehq.com/plot/interactions/crosshair) [Pointer/Plot/Interactions/Pointer](https://observablehq.com/plot/interactions/pointer)Plot/PlotIntroduction/Plot/IntroductionFeatures/Plot/FeaturesMarks/Plot/MarksTransforms/Plot/TransformsInteractions/Plot/Interactions

Pager

[Next pageWhy Plot?](https://observablehq.com/plot/why-plot)

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

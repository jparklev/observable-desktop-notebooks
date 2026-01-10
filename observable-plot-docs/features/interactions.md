---
url: "https://observablehq.com/plot/features/interactions"
title: "Interactions | Plot"
---

# Interactions [​](https://observablehq.com/plot/features/interactions\#interactions)

Interaction allows reading values out of a plot (details on demand), or fluidly changing a view of data without editing code (zoom and filter). There are a variety of ways to achieve interaction with Plot, including built-in interaction features and development techniques with frameworks such as Observable and React.

## Pointing [​](https://observablehq.com/plot/features/interactions\#pointing)

When looking at a scatterplot, the reader may wonder, _what abstract values does this dot represent?_

The [pointer transform](https://observablehq.com/plot/interactions/pointer) can provide an answer: it dynamically [filters](https://observablehq.com/plot/transforms/filter) a mark such that only the data closest to the pointer (such as the mouse) is rendered. The pointer transform is often paired with the [tip mark](https://observablehq.com/plot/marks/tip) for interactive tooltips, revealing exact values as the pointer moves over the plot. The tip can show additional fields not otherwise visible, such as the _name_ and _sport_ of Olympic athletes below.

1.31.41.51.61.71.81.92.02.12.2↑ height406080100120140160weight → [Fork](https://observablehq.com/@observablehq/scatterplot-with-interactive-tips "Open on Observable")

js

```
Plot.dot(olympians, {
  x: "weight",
  y: "height",
  stroke: "sex",
  channels: {name: "name", sport: "sport"},
  tip: true
}).plot()
```

The [crosshair mark](https://observablehq.com/plot/interactions/crosshair) uses the pointer transform internally to display a [rule](https://observablehq.com/plot/marks/rule) and a [text](https://observablehq.com/plot/marks/text) showing the **x** (horizontal↔︎ position) and **y** (vertical↕︎ position) value of the nearest data.

1.31.41.51.61.71.81.92.02.12.2↑ height406080100120140160weight → [Fork](https://observablehq.com/@observablehq/plot-crosshair "Open on Observable")

js

```
Plot.plot({
  marks: [\
    Plot.dot(olympians, {x: "weight", y: "height", stroke: "sex"}),\
    Plot.crosshair(olympians, {x: "weight", y: "height"})\
  ]
})
```

These values are displayed atop the axes on the edge of the frame; unlike the tip mark, the crosshair mark will not obscure other marks in the plot.

## Selecting [​](https://observablehq.com/plot/features/interactions\#selecting)

Support for selecting points within a plot through direct manipulation is under development. If you are interested in this feature, please upvote [#5](https://github.com/observablehq/plot/issues/5). See [#721](https://github.com/observablehq/plot/pull/721) for some early work on brushing.

## Zooming [​](https://observablehq.com/plot/features/interactions\#zooming)

Support for interactive panning and zooming is planned for a future release. If you are interested in this feature, please upvote [#1590](https://github.com/observablehq/plot/issues/1590).

## Animation [​](https://observablehq.com/plot/features/interactions\#animation)

Support for declarative animation is planned for a future release. If you are interested in this feature, please upvote [#166](https://github.com/observablehq/plot/issues/166). See [#995](https://github.com/observablehq/plot/pull/995) for some early work on a **time** channel.

## Custom reactivity [​](https://observablehq.com/plot/features/interactions\#custom-reactivity)

With the exception of render transforms (see the [pointer transform](https://github.com/observablehq/plot/blob/main/src/interactions/pointer.js) implementation), Plot does not currently provide incremental re-rendering (partial updates to previously-rendered plots) or animated transitions between views.

That said, you can simply throw away an old plot and replace it with a new one! This allows plotting of dynamic data: data which can change in real-time as it streams in, or because it is derived in response to external inputs such as range sliders and search boxes.

On Observable, you can use [viewof](https://observablehq.com/@observablehq/views) in conjunction with [Observable Inputs](https://observablehq.com/@observablehq/inputs) (or other plots!) for interactivity. If your cell references another cell, it will automatically re-run whenever the upstream cell’s value changes. For example, try dragging the slider in this [hexbin example](https://observablehq.com/@observablehq/plot-hexbin-binwidth). In React, use [useEffect](https://react.dev/reference/react/useEffect) and [useRef](https://react.dev/reference/react/useRef) to re-render the plot when data changes. In Vue, use [ref](https://vuejs.org/api/reactivity-core.html#ref). For more, see our [getting started guide](https://observablehq.com/plot/getting-started).

You can also manipulate the SVG that Plot creates, if you are comfortable using lower-level APIs; see examples by [Mike Freeman](https://observablehq.com/@mkfreeman/plot-animation) and [Philippe Rivière](https://observablehq.com/@fil/plot-animate-a-bar-chart).

Pager

[Previous pageTransforms](https://observablehq.com/plot/features/transforms)

[Next pageFacets](https://observablehq.com/plot/features/facets)

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

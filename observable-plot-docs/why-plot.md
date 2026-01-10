---
url: "https://observablehq.com/plot/why-plot"
title: "Why Plot? | Plot"
---

# Why Plot? [​](https://observablehq.com/plot/why-plot\#why-plot)

**Observable Plot** is for exploratory data visualization. It’s for finding insights quickly. Its API, while expressive and configurable, optimizes for conciseness and memorability. We want the time to first chart to be as fast as possible.

And the speed doesn’t stop there: Plot helps you quickly pivot and refine your views of data. Our hope with Plot is that you’ll spend less time reading the docs, searching for code to copy-paste, and debugging — and more time asking questions of data.

Compared to other visualization tools, including low-level tools such as D3 and less expressive high-level tools such as chart templates, we think you’ll be more productive exploring data with Plot. You’ll spend more time “using vision to think” and less time wrangling the machinery of programming.

Or put more simply: **with Plot, you’ll see more charts.**

## Plot is concise [​](https://observablehq.com/plot/why-plot\#plot-is-concise)

You can make a meaningful chart in Plot with as little as one line of code.

1415161718192021↑ culmen\_depth\_mm3540455055culmen\_length\_mm → [Fork](https://observablehq.com/@observablehq/color-scatterplot "Open on Observable")

js

```
Plot.dot(penguins, {x: "culmen_length_mm", y: "culmen_depth_mm", stroke: "species"}).plot()
```

What makes Plot concise? In a word: _defaults_. If you specify the semantics — your data and the desired encodings — Plot will figure out the rest.

The beauty of defaults is that you can override them as needed. This is ideal for exploring: you invest minimally in the initial chart, and as you start to see something interesting, you progressively customize to improve the display. Perhaps the plot above would be easier to read with an aspect ratio proportional to the data, a grid, and a legend?

AdelieChinstrapGentoo

1520↑ Culmen depth (mm)3540455055Culmen length (mm) → [Fork](https://observablehq.com/@observablehq/plot-refined-color-scatterplot "Open on Observable")

js

```
Plot.plot({
  grid: true,
  aspectRatio: 1,
  inset: 10,
  x: {tickSpacing: 80, label: "Culmen length (mm)"},
  y: {tickSpacing: 80, label: "Culmen depth (mm)"},
  color: {legend: true},
  marks: [\
    Plot.frame(),\
    Plot.dot(penguins, {x: "culmen_length_mm", y: "culmen_depth_mm", stroke: "species"})\
  ]
})
```

## Plot transforms data [​](https://observablehq.com/plot/why-plot\#plot-transforms-data)

Munging data, not visualizing it, is often most of the work of data analysis. Plot’s [transforms](https://observablehq.com/plot/features/transforms) let you aggregate and derive data _within_ your plot specification, reducing the time spent preparing data. For example, if you have a dataset of penguins, you can quickly count their frequency by _species_ with the [group transform](https://observablehq.com/plot/transforms/group).

AdelieChinstrapGentoospecies020406080100120140Frequency → [Fork](https://observablehq.com/@observablehq/plot-groupy-transform "Open on Observable")

js

```
Plot.plot({
  marginLeft: 80,
  marginRight: 80,
  marks: [\
    Plot.barX(penguins, Plot.groupY({x: "count"}, {y: "species"})),\
    Plot.ruleX([0])\
  ]
})
```

Because transforms are integrated into Plot, they work automatically with other Plot features such as [faceting](https://observablehq.com/plot/features/facets). For example, to breakdown the chart above by _island_, we just add the **fy** (vertical facet) option.

BiscoeDreamTorgersenislandAdelieChinstrapGentooAdelieChinstrapGentooAdelieChinstrapGentoospecies020406080100120Frequency → [Fork](https://observablehq.com/@observablehq/plot-groupy-transform/2 "Open on Observable")

js

```
Plot.plot({
  marginLeft: 80,
  marginRight: 80,
  marks: [\
    Plot.barX(penguins, Plot.groupY({x: "count"}, {fy: "island", y: "species"})),\
    Plot.ruleX([0])\
  ]
})
```

And to color by _sex_, too? Add **fill**; the [bar mark](https://observablehq.com/plot/marks/bar) then applies an implicit [stack transform](https://observablehq.com/plot/transforms/stack).

FEMALEMALEnull

BiscoeDreamTorgersenislandAdelieChinstrapGentooAdelieChinstrapGentooAdelieChinstrapGentoospecies020406080100120Frequency → [Fork](https://observablehq.com/@observablehq/plot-groupy-transform/3 "Open on Observable")

js

```
Plot.plot({
  marginLeft: 80,
  marginRight: 80,
  color: {legend: true},
  marks: [\
    Plot.barX(penguins, Plot.groupY({x: "count"}, {fy: "island", y: "species", fill: "sex"})),\
    Plot.ruleX([0])\
  ]
})
```

Plot’s transforms can do powerful things, including [normalizing series](https://observablehq.com/plot/transforms/normalize), computing [moving averages](https://observablehq.com/plot/transforms/window), laying out [trees](https://observablehq.com/plot/marks/tree), [dodging](https://observablehq.com/plot/transforms/dodge), and [hexagonal binning](https://observablehq.com/plot/transforms/hexbin).

## Plot is composable [​](https://observablehq.com/plot/why-plot\#plot-is-composable)

Simple components gain power through composition, such as layering multiple [marks](https://observablehq.com/plot/features/marks) into a single plot. Plot makes it easy to define custom composite marks, such as this one comprising a rule, area, and line:

js

```
function arealineY(data, {color, fillOpacity = 0.1, ...options} = {}) {
  return Plot.marks(
    Plot.ruleY([0]),
    Plot.areaY(data, {fill: color, fillOpacity, ...options}),
    Plot.lineY(data, {stroke: color, ...options})
  );
}
```

You can use this composite mark like any built-in mark:

020406080100120140160180↑ Close20142015201620172018 [Fork](https://observablehq.com/@observablehq/plot-arealiney-custom-mark "Open on Observable")

js

```
arealineY(aapl, {x: "Date", y: "Close", color: "blue"}).plot()
```

Plot uses this technique internally: the [axis mark](https://observablehq.com/plot/marks/axis) and [box mark](https://observablehq.com/plot/marks/box) are both composite marks.

AdelieChinstrapGentoo3,0003,5004,0004,5005,0005,5006,000body\_mass\_g → [Fork](https://observablehq.com/@observablehq/plot-penguins-horizontal-box-plot "Open on Observable")

js

```
Plot.boxX(penguins, {x: "body_mass_g", y: "species"}).plot({marginLeft: 60, y: {label: null}})
```

Plot’s [transforms](https://observablehq.com/plot/features/transforms) are composable, too: to apply multiple transforms, you simply pass the _options_ from one transform to the next. Some marks even apply implicit transforms, say for [stacking](https://observablehq.com/plot/transforms/stack) or [binning](https://observablehq.com/plot/transforms/bin) as shown [above](https://observablehq.com/plot/why-plot#plot-transforms-data). Mark options are plain JavaScript objects, so you can also share options across marks and inspect them to debug.

## Plot is extensible [​](https://observablehq.com/plot/why-plot\#plot-is-extensible)

Plot isn’t a new language; it’s “just” vanilla JavaScript. Plot embraces JavaScript, letting you plug in your own functions for accessors, reducers, transforms… even custom marks! And Plot generates SVG, so you can style it with CSS and manipulate it just like you do with D3. (See [Mike Freeman’s tooltip plugin](https://observablehq.com/@mkfreeman/plot-tooltip) for a great example of extending Plot this way.)

## Plot builds on D3 [​](https://observablehq.com/plot/why-plot\#plot-builds-on-d3)

Plot is informed by our more than [ten years’ experience](https://observablehq.com/@mbostock/10-years-of-open-source-visualization) developing [D3](https://d3js.org/), the web’s most popular library for data visualization.

Plot uses D3 to implement a wide variety of features:

- scales (ticks, color schemes, number formatting)
- shapes (areas, lines, curves, symbols, stacks)
- planar geometry (Delaunay, Voronoi, contours, density estimation)
- spherical geometry (geographic projections)
- data manipulation (group, rollup, bin, statistics)
- tree diagrams
- … and more!

If you already know some D3, you’ll find many parts of Plot familiar.

We’ve long said that _D3 makes things possible, not necessarily easy._ And that’s true regardless of the task at hand. D3 makes hard and amazing things _possible_, yes, but even simple things that should be easy are often not. To paraphrase Amanda Cox: “Use D3 if you think it’s perfectly normal to write a hundred lines of code for a bar chart.”

**Plot’s goal is to make the easy things easy, and fast, and then some.**

TIP

Whether or not Plot succeeds at this goal is up to you — so we’d love [your feedback](https://github.com/observablehq/plot/discussions/new/choose) on what you find easy or hard to do with Plot. And we encourage you to [ask for help](https://github.com/observablehq/plot/discussions/categories/q-a) when you get stuck. We learn a lot from helping!

Since Plot and D3 have different goals, they make different trade-offs. Plot is more efficient: you can make charts quickly. But it is also necessarily less expressive: bespoke visualizations with extensive animation and interaction, advanced techniques like force-directed graph layout, or even developing your own charting library, are better done with D3’s low-level API.

We recommend D3 for _bespoke_ data visualizations, if you decide the extra expressiveness of D3 is worth the time and effort. D3 makes sense for media organizations such as _The New York Times_ or _The Pudding_, where a single graphic may be seen by a million readers, and where a team of editors can work together to advance the state of the art in visual communication; but is it the best tool for building your team’s private dashboard, or a one-off analysis? You may be surprised how far you can get with Plot.

Pager

[Previous pageWhat is Plot?](https://observablehq.com/plot/what-is-plot)

[Next pageGetting started](https://observablehq.com/plot/getting-started)

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

---
url: "https://observablehq.com/plot/marks/link"
title: "Link mark | Plot"
---

# Link mark [​](https://observablehq.com/plot/marks/link\#link-mark)

The **link mark** draws straight lines between two points \[ **x1**, **y1**\] and \[ **x2**, **y2**\] in quantitative dimensions. It is similar to the [arrow mark](https://observablehq.com/plot/marks/arrow), except it draws a straight line — or geodesic when used with a [spherical projection](https://observablehq.com/plot/features/projections).

For example, the chart below shows the rising inequality (and population) in various U.S. cities from 1980 to 2015. Each link represents two observations of a city: the city’s population ( **x**) and inequality ( **y**) in 1980, and the same in 2015. The link’s **stroke** redundantly encodes the change in inequality: red indicates rising inequality, while blue (there are only four) indicates declining inequality.

−2+0+2Change in inequality from 1980 to 201545678↑ Inequality200k300k400k1M2M3M4M10M20MPopulation →New YorkChicagoHoustonWashington, D.C.San FranciscoSan JoseFairfield, Conn.Binghamton, N.Y. [Fork](https://observablehq.com/@observablehq/plot-link-variation-chart "Open on Observable")

js

```
Plot.plot({
  grid: true,
  inset: 10,
  x: {
    type: "log",
    label: "Population"
  },
  y: {
    label: "Inequality",
    ticks: 4
  },
  color: {
    scheme: "BuRd",
    label: "Change in inequality from 1980 to 2015",
    legend: true,
    tickFormat: "+f"
  },
  marks: [\
    Plot.link(metros, {\
      x1: "POP_1980",\
      y1: "R90_10_1980",\
      x2: "POP_2015",\
      y2: "R90_10_2015",\
      stroke: (d) => d.R90_10_2015 - d.R90_10_1980,\
      markerEnd: "arrow"\
    }),\
    Plot.text(metros, {\
      x: "POP_2015",\
      y: "R90_10_2015",\
      filter: "highlight",\
      text: "nyt_display",\
      fill: "currentColor",\
      stroke: "white",\
      dy: -8\
    })\
  ]
})
```

The link mark is used by the composite [tree mark](https://observablehq.com/plot/marks/tree) to render a link from parent to child in a hierarchy. The [treeLink transform](https://observablehq.com/plot/transforms/tree) sets the default [curve option](https://observablehq.com/plot/features/curves) to _bump-x_.

ChaosErosErebusTartarusGaiaMountainsPontusUranus [Fork](https://observablehq.com/@observablehq/plot-tree-and-link "Open on Observable")

js

```
Plot.plot({
  axis: null,
  height: 120,
  inset: 20,
  insetRight: 120,
  marks: [\
    Plot.link(gods, Plot.treeLink({stroke: "node:internal"})),\
    Plot.dot(gods, Plot.treeNode({fill: "node:internal"})),\
    Plot.text(gods, Plot.treeNode({text: "node:name", stroke: "white", fill: "currentColor", dx: 6}))\
  ]
})
```

In this example, `gods` is an array of slash-separated paths representing the ancestry of mythological Greek gods.

js

```
gods = [\
  "Chaos/Gaia/Mountains",\
  "Chaos/Gaia/Pontus",\
  "Chaos/Gaia/Uranus",\
  "Chaos/Eros",\
  "Chaos/Erebus",\
  "Chaos/Tartarus"\
]
```

With a [spherical projection](https://observablehq.com/plot/features/projections) and the default [_auto_ curve](https://observablehq.com/plot/features/curves), the link mark will render a geodesic: the shortest path between two points on the surface of the sphere. Setting the **curve** to _linear_ will instead draw a straight line between the projected points. For example, below we draw two links from San Francisco to Paris.

[Fork](https://observablehq.com/@observablehq/plot-projected-link "Open on Observable")

js

```
Plot.plot({
  projection: "equal-earth",
  marks: [\
    Plot.sphere(),\
    Plot.geo(land, {fill: "currentColor", fillOpacity: 0.3}),\
    Plot.link({length: 1}, {curve: "linear", stroke: "red", ...xy}),\
    Plot.link({length: 1}, {markerStart: "dot", markerEnd: "arrow", strokeWidth: 1.5, ...xy})\
  ]
})
```

js

```
xy = ({x1: -122.4194, y1: 37.7749, x2: 2.3522, y2: 48.8566})
```

Like a [rule](https://observablehq.com/plot/marks/rule), a link can also serve as annotation. Whereas a rule is strictly horizontal or vertical, however, a link can generate [diagonal lines](http://kelsocartography.com/blog/?p=2074). The following chart depicts the gender gap in wages, segmented by education and age, in the U.S. A regular grid would make the gender disparity much less clear, even with the domains explicitly set to be equal.

0102030405060708090100↑ Median annual income (women, thousands)0102030405060708090100Median annual income (men, thousands) →−40%−30%−20%−10%Equal [Fork](https://observablehq.com/@observablehq/plot-gender-income-inequality "Open on Observable")

js

```
Plot.plot({
  aspectRatio: 1,
  marginRight: 40,
  x: {
    label: "Median annual income (men, thousands)",
    transform: (d) => d / 1000,
    tickSpacing: 60
  },
  y: {
    label: "Median annual income (women, thousands)",
    transform: (d) => d / 1000,
    tickSpacing: 60
  },
  marks: [\
    Plot.link([0.6, 0.7, 0.8, 0.9, 1], {\
      x1: 0,\
      y1: 0,\
      x2: 102000,\
      y2: (k) => 102000 * k,\
      strokeOpacity: (k) => k === 1 ? 1 : 0.2\
    }),\
    Plot.text([0.6, 0.7, 0.8, 0.9, 1], {\
      x: 102000,\
      y: (k) => 102000 * k,\
      text: ((f) => (k) => k === 1 ? "Equal" : f(k - 1))(d3.format("+.0%")),\
      textAnchor: "start",\
      dx: 6\
    }),\
    Plot.dot(income, {x: "m", y: "f"})\
  ]
})
```

## Link options [​](https://observablehq.com/plot/marks/link\#link-options)

The following channels are required:

- **x1** \- the starting horizontal position; bound to the _x_ scale
- **y1** \- the starting vertical position; bound to the _y_ scale
- **x2** \- the ending horizontal position; bound to the _x_ scale
- **y2** \- the ending vertical position; bound to the _y_ scale

For vertical or horizontal links, the **x** option can be specified as shorthand for **x1** and **x2**, and the **y** option can be specified as shorthand for **y1** and **y2**, respectively.

The link mark supports the [standard mark options](https://observablehq.com/plot/features/marks). The **stroke** defaults to currentColor. The **fill** defaults to none. The **strokeWidth** and **strokeMiterlimit** default to one.

The link mark supports [curve options](https://observablehq.com/plot/features/curves) to control interpolation between points, and [marker options](https://observablehq.com/plot/features/markers) to add a marker (such as a dot or an arrowhead) on each of the control points. Since a link always has two points by definition, only the following curves (or a custom curve) are recommended: _linear_, _step_, _step-after_, _step-before_, _bump-x_, or _bump-y_. Note that the _linear_ curve is incapable of showing a fill since a straight line has zero area. For a curved link, you can use a bent [arrow](https://observablehq.com/plot/marks/arrow) (with no arrowhead, if desired).

## link( _data_, _options_) [​](https://observablehq.com/plot/marks/link\#link)

js

```
Plot.link(inequality, {x1: "POP_1980", y1: "R90_10_1980", x2: "POP_2015", y2: "R90_10_2015"})
```

Returns a new link with the given _data_ and _options_.

Pager

[Previous pageLinear regression](https://observablehq.com/plot/marks/linear-regression)

[Next pageRaster](https://observablehq.com/plot/marks/raster)

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

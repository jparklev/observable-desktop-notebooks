---
url: "https://observablehq.com/plot/marks/tick"
title: "Tick mark | Plot"
---

# Tick mark [​](https://observablehq.com/plot/marks/tick\#tick-mark)

TIP

The tick mark is one of two marks in Plot for drawing horizontal or vertical lines; it should be used when the secondary position dimension, if any, is ordinal. When it is quantitative, use a [rule](https://observablehq.com/plot/marks/rule).

The **tick mark** comes in two orientations: [tickY](https://observablehq.com/plot/marks/tick#tickY) draws a horizontal↔︎ line with a given _y_ value, while [tickX](https://observablehq.com/plot/marks/tick#tickX) draws a vertical↕︎ line with a given _x_ value. Ticks have an optional secondary position dimension ( **x** for tickY and **y** for tickX); this second dimension is ordinal, unlike a [rule](https://observablehq.com/plot/marks/rule), and requires a corresponding [band scale](https://observablehq.com/plot/features/scales).

Ticks are often used to show one-dimensional distributions, as in the “barcode” plot below showing the proportion of the population in each age bracket across U.S. states.

≥8070-7960-6950-5940-4930-3920-2910-19<10Age (years)02468101214161820Population (%) → [Fork](https://observablehq.com/@observablehq/plot-barcode "Open on Observable")

js

```
Plot.plot({
  x: {
    grid: true,
    label: "Population (%)",
    percent: true
  },
  y: {
    domain: stateage.ages, // in age order
    reverse: true,
    label: "Age (years)",
    labelAnchor: "top"
  },
  marks: [\
    Plot.ruleX([0]),\
    Plot.tickX(stateage, Plot.normalizeX("sum", {z: "state", x: "population", y: "age"}))\
  ]
})
```

Both ticks and [bars](https://observablehq.com/plot/marks/bar) have an ordinal secondary position dimension; a tick is therefore convenient for stroking the upper bound of a bar for emphasis, as in the bar chart below. A separate [rule](https://observablehq.com/plot/marks/rule) is also used to denote _y_ = 0.

0123456789101112↑ frequency (%)ABCDEFGHIJKLMNOPQRSTUVWXYZ [Fork](https://observablehq.com/@observablehq/plot-bar-and-tick "Open on Observable")

js

```
Plot.plot({
  x: {label: null},
  y: {percent: true},
  marks: [\
    Plot.barY(alphabet, {x: "letter", y: "frequency", fillOpacity: 0.2}),\
    Plot.tickY(alphabet, {x: "letter", y: "frequency"}),\
    Plot.ruleY([0])\
  ]
})
```

When there is no secondary position dimension, a tick behaves identically to a [rule](https://observablehq.com/plot/marks/rule). While a one-dimensional rule and tick are equivalent, a one-dimensional rule is generally preferred, if only because the name “rule” is more descriptive. But as an example below, a random normal distribution is plotted below with ticks.

−4−3−2−101234 [Fork](https://observablehq.com/@observablehq/plot-random-ticks "Open on Observable")

js

```
Plot.plot({
  x: {domain: [-4, 4]},
  marks: [\
    Plot.tickX({length: 500}, {x: d3.randomNormal(), strokeOpacity: 0.2})\
  ]
})
```

TIP

Reducing opacity allows better perception of density when ticks overlap.

Ticks are also used by the [box mark](https://observablehq.com/plot/marks/box) to denote the median value for each group.

## Tick options [​](https://observablehq.com/plot/marks/tick\#tick-options)

For the required channels, see [tickX](https://observablehq.com/plot/marks/tick#tickX) and [tickY](https://observablehq.com/plot/marks/tick#tickY). The tick mark supports the [standard mark options](https://observablehq.com/plot/features/marks#mark-options), including insets, and [marker options](https://observablehq.com/plot/features/markers) to add a marker (such as a dot or an arrowhead) to the start or end of the rule. The **stroke** defaults to _currentColor_.

## tickX( _data_, _options_) [​](https://observablehq.com/plot/marks/tick\#tickX)

js

```
Plot.tickX(stateage, {x: "population", y: "age"})
```

Returns a new vertical↕︎ tick with the given _data_ and _options_. The following channels are required:

- **x** \- the horizontal position; bound to the _x_ scale

The following optional channels are supported:

- **y** \- the vertical position; bound to the _y_ scale, which must be _band_

If the **y** channel is not specified, the tick will span the full vertical extent of the frame.

## tickY( _data_, _options_) [​](https://observablehq.com/plot/marks/tick\#tickY)

js

```
Plot.tickY(stateage, {y: "population", x: "age"})
```

Returns a new horizontal↔︎ tick with the given _data_ and _options_. The following channels are required:

- **y** \- the vertical position; bound to the _y_ scale

The following optional channels are supported:

- **x** \- the horizontal position; bound to the _x_ scale, which must be _band_

If the **x** channel is not specified, the tick will span the full vertical extent of the frame.

Pager

[Previous pageText](https://observablehq.com/plot/marks/text)

[Next pageTip](https://observablehq.com/plot/marks/tip)

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

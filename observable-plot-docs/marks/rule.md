---
url: "https://observablehq.com/plot/marks/rule"
title: "Rule mark | Plot"
---

# Rule mark [​](https://observablehq.com/plot/marks/rule\#rule-mark)

TIP

The rule mark is one of two marks in Plot for drawing horizontal or vertical lines; it should be used when the secondary position dimension, if any, is quantitative. When it is ordinal, use a [tick](https://observablehq.com/plot/marks/tick).

The **rule mark** comes in two orientations: [ruleY](https://observablehq.com/plot/marks/rule#ruleY) draws a horizontal↔︎ line with a given _y_ value, while [ruleX](https://observablehq.com/plot/marks/rule#ruleX) draws a vertical↕︎ line with a given _x_ value. Rules are often used as annotations, say to mark the _y_ = 0 baseline (in red below for emphasis) in a line chart.

020406080100120140160180↑ Close20142015201620172018 [Fork](https://observablehq.com/@observablehq/plot-rule-zero "Open on Observable")

js

```
Plot.plot({
  y: {
    grid: true
  },
  marks: [\
    Plot.ruleY([0], {stroke: "red"}),\
    Plot.line(aapl, {x: "Date", y: "Close"})\
  ]
})
```

As annotations, rules often have a hard-coded array of literal values as data. This [shorthand](https://observablehq.com/plot/features/shorthand) utilizes the default [identity](https://observablehq.com/plot/features/transforms#identity) definition of the rule’s position ( **y** for ruleY and **x** for ruleX).

+0+20+40+60+80+100+120+140+160+180↑ Change in price (%)20142015201620172018 [Fork](https://observablehq.com/@observablehq/plot-rule-one "Open on Observable")

js

```
Plot.plot({
  y: {
    type: "log",
    grid: true,
    label: "Change in price (%)",
    tickFormat: ((f) => (d) => f((d - 1) * 100))(d3.format("+d"))
  },
  marks: [\
    Plot.ruleY([1], {stroke: "red"}),\
    Plot.line(aapl, Plot.normalizeY("first", {x: "Date", y: "Close"}))\
  ]
})
```

Yet rules can also be used to visualize data. Below, a random normal distribution is plotted with rules, looking a bit like the [emission spectrum of Hydrogen](https://en.wikipedia.org/wiki/Hydrogen_spectral_series).

−4−3−2−101234 [Fork](https://observablehq.com/@observablehq/plot-rule-random "Open on Observable")

js

```
Plot.plot({
  x: {domain: [-4, 4]},
  marks: [\
    Plot.ruleX({length: 500}, {x: d3.randomNormal(), strokeOpacity: 0.2})\
  ]
})
```

TIP

Reducing opacity allows better perception of density when rules overlap.

Rules can also serve as an alternative to an [area mark](https://observablehq.com/plot/marks/area) as in a band chart, provided the data is sufficiently dense: you can limit the extent of a rule along the secondary dimension ( **y1** and **y2** channels for ruleX, and **x1** and **x2** channels for ruleY) rather than having it span the frame. And rules support a **stroke** color encoding. The rules below plot the daily minimum and maximum temperature for Seattle.

−505101520253035↑ Temperature (°C)2012201320142015

js

```
Plot.plot({
  y: {grid: true, label: "Temperature (°C)"},
  color: {scheme: "BuRd"},
  marks: [\
    Plot.ruleY([0]),\
    Plot.ruleX(seattle, {x: "date", y1: "temp_min", y2: "temp_max", stroke: "temp_min"})\
  ]
})
```

In the dense [candlestick chart](https://observablehq.com/@observablehq/observable-plot-candlestick) below, three rules are drawn for each trading day: a gray rule spans the chart, showing gaps for weekends and holidays; a black rule spans the day’s low and high; and a green or red rule spans the day’s open and close.

60708090100110120130140150160170180190↑ Stock price ($)20142015201620172018 [Fork](https://observablehq.com/@observablehq/plot-candlestick-chart "Open on Observable")

js

```
Plot.plot({
  inset: 6,
  label: null,
  y: {grid: true, label: "Stock price ($)"},
  color: {type: "threshold", range: ["red", "green"]},
  marks: [\
    Plot.ruleX(aapl, {x: "Date", y1: "Low", y2: "High"}),\
    Plot.ruleX(aapl, {x: "Date", y1: "Open", y2: "Close", stroke: (d) => d.Close - d.Open, strokeWidth: 4})\
  ]
})
```

Rules can be used to connect graphical elements, such as in the [dot plot](https://observablehq.com/plot/marks/dot) below showing the decline of _The Simpsons_. The rules indicate the extent (minimum and maximum) for each season, computed via the [group transform](https://observablehq.com/plot/transforms/group), while a red line shows the median rating trend.

4.55.05.56.06.57.07.58.08.59.0↑ imdb\_rating510152025season → [Fork](https://observablehq.com/@observablehq/plot-simpsons-decline "Open on Observable")

js

```
Plot.plot({
  marks: [\
    Plot.ruleX(simpsons, Plot.groupX({y1: "min", y2: "max"}, {x: "season", y: "imdb_rating"})),\
    Plot.dot(simpsons, {x: "season", y: "imdb_rating", fill: "currentColor", stroke: "white"}),\
    Plot.lineY(simpsons, Plot.groupX({y: "median"}, {x: "season", y: "imdb_rating", stroke: "red"}))\
  ]
})
```

Rules can indicate uncertainty or error by setting the [**marker** option](https://observablehq.com/plot/features/markers) to _tick_; this draws a small perpendicular line at the start and end of the rule. For example, to simulate ±10% error:

012345678910111213↑ frequency (%)ABCDEFGHIJKLMNOPQRSTUVWXYZ

js

```
Plot.plot({
  x: {label: null},
  y: {percent: true},
  marks: [\
    Plot.barY(alphabet, {x: "letter", y: "frequency", fill: "blue"}),\
    Plot.ruleX(alphabet, {x: "letter", y1: (d) => d.frequency * 0.9, y2: (d) => d.frequency * 1.1, marker: "tick"}),\
    Plot.ruleY([0])\
  ]
})
```

Rules can also be a stylistic choice, as in the lollipop 🍭 chart below, serving the role of a skinny [bar](https://observablehq.com/plot/marks/bar) topped with a [_dot_ marker](https://observablehq.com/plot/features/markers).

0123456789101112↑ frequency (%)ABCDEFGHIJKLMNOPQRSTUVWXYZ [Fork](https://observablehq.com/@observablehq/plot-lollipop "Open on Observable")

js

```
Plot.plot({
  x: {label: null, tickPadding: 6, tickSize: 0},
  y: {percent: true},
  marks: [\
    Plot.ruleX(alphabet, {x: "letter", y: "frequency", strokeWidth: 2, markerEnd: "dot"})\
  ]
})
```

Rules are also used by the [grid mark](https://observablehq.com/plot/marks/grid) to draw grid lines.

## Rule options [​](https://observablehq.com/plot/marks/rule\#rule-options)

For the required channels, see [ruleX](https://observablehq.com/plot/marks/rule#ruleX) and [ruleY](https://observablehq.com/plot/marks/rule#ruleY). The rule mark supports the [standard mark options](https://observablehq.com/plot/features/marks#mark-options), including insets along its secondary dimension, and [marker options](https://observablehq.com/plot/features/markers) to add a marker (such as a dot or an arrowhead) to the start or end of the rule. The **stroke** defaults to _currentColor_.

## ruleX( _data_, _options_) [​](https://observablehq.com/plot/marks/rule\#ruleX)

js

```
Plot.ruleX([0]) // as annotation
```

js

```
Plot.ruleX(alphabet, {x: "letter", y: "frequency"}) // like barY
```

Returns a new vertical↕︎ rule with the given _data_ and _options_. The following channels are optional:

- **x** \- the horizontal position; bound to the _x_ scale
- **y1** \- the starting vertical position; bound to the _y_ scale
- **y2** \- the ending vertical position; bound to the _y_ scale

If **x** is not specified, it defaults to [identity](https://observablehq.com/plot/features/transforms#identity) and assumes that _data_ = \[ _x₀_, _x₁_, _x₂_, …\]. If **x** is null, the rule will be centered horizontally in the plot frame.

If **y** is specified, it is shorthand for **y2** with **y1** equal to zero; this is the typical configuration for a vertical lollipop chart with rules aligned at _y_ = 0\. If **y1** is not specified, the rule will start at the top of the plot (or facet). If **y2** is not specified, the rule will end at the bottom of the plot (or facet).

If an **interval** is specified, such as d3.utcDay, **y1** and **y2** can be derived from **y**: _interval_.floor( _y_) is invoked for each _y_ to produce _y1_, and _interval_.offset( _y1_) is invoked for each _y1_ to produce _y2_. If the interval is specified as a number _n_, _y1_ and _y2_ are taken as the two consecutive multiples of _n_ that bracket _y_. Named UTC intervals such as _day_ are also supported; see [scale options](https://observablehq.com/plot/features/scales#scale-options).

## ruleY( _data_, _options_) [​](https://observablehq.com/plot/marks/rule\#ruleY)

js

```
Plot.ruleY([0]) // as annotation
```

js

```
Plot.ruleY(alphabet, {y: "letter", x: "frequency"}) // like barX
```

Returns a new horizontal↔︎ rule with the given _data_ and _options_. The following channels are optional:

- **y** \- the vertical position; bound to the _y_ scale
- **x1** \- the starting horizontal position; bound to the _x_ scale
- **x2** \- the ending horizontal position; bound to the _x_ scale

If **y** is not specified, it defaults to [identity](https://observablehq.com/plot/features/transforms#identity) and assumes that _data_ = \[ _y₀_, _y₁_, _y₂_, …\]. If **y** is null, the rule will be centered vertically in the plot frame.

If **x** is specified, it is shorthand for **x2** with **x1** equal to zero; this is the typical configuration for a horizontal lollipop chart with rules aligned at _x_ = 0\. If **x1** is not specified, the rule will start at the left edge of the plot (or facet). If **x2** is not specified, the rule will end at the right edge of the plot (or facet).

If an **interval** is specified, such as d3.utcDay, **x1** and **x2** can be derived from **x**: _interval_.floor( _x_) is invoked for each _x_ to produce _x1_, and _interval_.offset( _x1_) is invoked for each _x1_ to produce _x2_. If the interval is specified as a number _n_, _x1_ and _x2_ are taken as the two consecutive multiples of _n_ that bracket _x_. Named UTC intervals such as _day_ are also supported; see [scale options](https://observablehq.com/plot/features/scales#scale-options).

Pager

[Previous pageRect](https://observablehq.com/plot/marks/rect)

[Next pageText](https://observablehq.com/plot/marks/text)

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

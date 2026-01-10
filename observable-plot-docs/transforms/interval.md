---
url: "https://observablehq.com/plot/transforms/interval"
title: "Interval transform | Plot"
---

# Interval transform [​](https://observablehq.com/plot/transforms/interval\#interval-transform)

TIP

There’s also an [**interval** scale option](https://observablehq.com/plot/features/scales#scale-transforms) for quantizing continuous data.

The **interval transform** turns a quantitative or temporal _value_ into a continuous extent \[ _start_, _stop_\]. For example, if _value_ is an instant in time, the interval transform could return a _start_ of UTC midnight and a _stop_ of the UTC midnight the following day.

The interval transform is often used for time-series bar charts. For example, consider the chart below of the daily trade volume of Apple stock. Because of the [barY mark](https://observablehq.com/plot/marks/bar), the _x_ scale is ordinal ( _band_). And because the regularity of the data is not specified ( _i.e._, because Plot has no way of knowing that this is daily data), every distinct value must have its own label, leading to crowding. If a day were missing data, it would be difficult to spot! 👓

05101520253035404550556065↑ Daily trade volume (millions)16Mar1920212223262728292Apr345691011121316171819202324252627301May2347891011 [Fork](https://observablehq.com/@observablehq/plot-band-scale-interval "Open on Observable")

js

```
Plot.plot({
  marginBottom: 80,
  x: {type: "band"}, // ⚠️ not utc
  y: {
    transform: (d) => d / 1e6,
    label: "Daily trade volume (millions)"
  },
  marks: [\
    Plot.barY(aapl.slice(-40), {x: "Date", y: "Volume"}),\
    Plot.ruleY([0])\
  ]
})
```

In contrast, a [rectY mark](https://observablehq.com/plot/marks/rect) with the **interval** option and the _day_ interval produces a temporal ( _utc_) _x_ scale. This allows Plot to compute ticks at meaningful intervals: here weekly boundaries, UTC midnight on Sundays. Furthermore, we can see that this isn’t truly daily data — it’s missing weekends and holidays when the stock market was closed.

05101520253035404550556065↑ Daily trade volume (millions)18Mar251Apr81522296May [Fork](https://observablehq.com/@observablehq/plot-temporal-interval-option "Open on Observable")

js

```
Plot.plot({
  y: {
    grid: true,
    transform: (d) => d / 1e6,
    label: "Daily trade volume (millions)"
  },
  marks: [\
    Plot.rectY(aapl.slice(-40), {x: "Date", interval: "day", y: "Volume"}),\
    Plot.ruleY([0])\
  ]
})
```

INFO

The interval transform is not a standalone transform, but an option on marks and scales.

The meaning of the **interval** mark option depends on the associated mark, such as line, bar, rect, or dot. For example, for the [barY mark](https://observablehq.com/plot/marks/bar), the **interval** option affects converts a singular _y_ value into an interval \[ _y1_, _y2_\]. In the contrived example below, notice that the vertical↕︎ extent of each bar spans an interval of 5 million, rather than extending to _y_ = 0.

0510152025303540455055606570↑ Daily trade volume (millions)16Mar1920212223262728292Apr345691011121316171819202324252627301May2347891011 [Fork](https://observablehq.com/@observablehq/plot-interval-bars "Open on Observable")

js

```
Plot.plot({
  marginBottom: 80,
  x: {type: "band"}, // ⚠️ not utc
  y: {
    grid: true,
    transform: (d) => d / 1e6,
    label: "Daily trade volume (millions)"
  },
  marks: [\
    Plot.barY(aapl.slice(-40), {x: "Date", y: "Volume", interval: 5e6}),\
    Plot.ruleY([0])\
  ]
})
```

While the **interval** option is most commonly specified as a named time interval or a number, it can also be specified as a [D3 time interval](https://d3js.org/d3-time#_interval) or any object that implements _interval_.floor and _interval_.offset.

Pager

[Previous pageHexbin](https://observablehq.com/plot/transforms/hexbin)

[Next pageMap](https://observablehq.com/plot/transforms/map)

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

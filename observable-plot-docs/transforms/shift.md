---
url: "https://observablehq.com/plot/transforms/shift"
title: "Shift transform | Plot"
---

# Shift transform [^0.6.12](https://github.com/observablehq/plot/releases/tag/v0.6.12 "added in v0.6.12") [​](https://observablehq.com/plot/transforms/shift\#shift-transform)

The **shift transform** is a specialized [map transform](https://observablehq.com/plot/transforms/map) that derives an output **x1** channel by shifting the **x** channel; it can be used with the [difference mark](https://observablehq.com/plot/marks/difference) to show change over time. For example, the chart below shows the price of Apple stock. The green region shows when the price went up over the given interval, while the blue region shows when the price went down.

Shift (days):365

60708090100110120130140150160170180190↑ Close2015201620172018

js

```
Plot.differenceY(aapl, Plot.shiftX(`${shift} days`, {x: "Date", y: "Close"})).plot({y: {grid: true}})
```

js

```
Plot.differenceY(aapl, Plot.shiftX("365 days", {x: "Date", y: "Close"})).plot({y: {grid: true}})
```

When looking at year-over-year growth, the chart is mostly green, implying that you would make a profit by holding Apple stock for a year. However, if you bought in 2015 and sold in 2016, you would likely have lost money. Try adjusting the slider to a shorter or longer interval: how does that affect the typical return?

## shiftX( _interval_, _options_) [​](https://observablehq.com/plot/transforms/shift\#shiftX)

js

```
Plot.shiftX("7 days", {x: "Date", y: "Close"})
```

Derives an **x1** channel from the input **x** channel by shifting values by the given [_interval_](https://observablehq.com/plot/features/intervals). The _interval_ may be specified as: a name ( _second_, _minute_, _hour_, _day_, _week_, _month_, _quarter_, _half_, _year_, _monday_, _tuesday_, _wednesday_, _thursday_, _friday_, _saturday_, _sunday_) with an optional number and sign ( _e.g._, _+3 days_ or _-1 year_); or as a number; or as an implementation — such as d3.utcMonth — with _interval_.floor( _value_), _interval_.offset( _value_), and _interval_.range( _start_, _stop_) methods.

The shiftX transform also aliases the **x** channel to **x2** and applies a domain hint to the **x2** channel such that by default the plot shows only the intersection of **x1** and **x2**. For example, if the interval is _+1 year_, the first year of the data is not shown.

## shiftY( _interval_, _options_) [^0.6.16](https://github.com/observablehq/plot/releases/tag/v0.6.16 "added in v0.6.16") [​](https://observablehq.com/plot/transforms/shift\#shiftY)

js

```
Plot.shiftY("7 days", {y: "Date", x: "Close"})
```

Derives a **y1** channel from the input **y** channel by shifting values by the given [_interval_](https://observablehq.com/plot/features/intervals). See [shiftX](https://observablehq.com/plot/transforms/shift#shiftX) for more.

The shiftY transform also aliases the **y** channel to **y2** and applies a domain hint to the **y2** channel such that by default the plot shows only the intersection of **y1** and **y2**. For example, if the interval is _+1 year_, the first year of the data is not shown.

Pager

[Previous pageSelect](https://observablehq.com/plot/transforms/select)

[Next pageSort](https://observablehq.com/plot/transforms/sort)

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

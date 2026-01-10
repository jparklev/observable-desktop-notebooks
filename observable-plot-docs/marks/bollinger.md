---
url: "https://observablehq.com/plot/marks/bollinger"
title: "Bollinger mark | Plot"
---

# Bollinger mark [^0.6.10](https://github.com/observablehq/plot/releases/tag/v0.6.10 "added in v0.6.10") [​](https://observablehq.com/plot/marks/bollinger\#bollinger-mark)

The **bollinger mark** is a [composite mark](https://observablehq.com/plot/features/marks#marks) consisting of a [line](https://observablehq.com/plot/marks/line) representing a moving average and an [area](https://observablehq.com/plot/marks/area) representing volatility as a band; the band thickness is proportional to the deviation of nearby values. The bollinger mark is often used to [analyze the price](https://en.wikipedia.org/wiki/Bollinger_Bands) of financial instruments such as stocks.

For example, the chart below shows the price of Apple stock from 2013 to 2018, with a window size _n_ of 20 days and radius _k_ of 2 standard deviations.

Window size (n):20Radius (k):2

60708090100110120130140150160170180190↑ Close20142015201620172018

js

```
Plot.bollingerY(aapl, {x: "Date", y: "Close", n, k}).plot()
```

js

```
Plot.bollingerY(aapl, {x: "Date", y: "Close", n: 20, k: 2}).plot()
```

For more control, you can also use the [bollinger map method](https://observablehq.com/plot/marks/bollinger#bollinger) directly with the [map transform](https://observablehq.com/plot/transforms/map).

60708090100110120130140150160170180190↑ Close20142015201620172018

js

```
Plot.plot({
  marks: [\
    Plot.lineY(aapl, Plot.mapY(Plot.bollinger({n: 20, k: -2}), {x: "Date", y: "Close", stroke: "red"})),\
    Plot.lineY(aapl, Plot.mapY(Plot.bollinger({n: 20, k: 2}), {x: "Date", y: "Close", stroke: "green"})),\
    Plot.lineY(aapl, {x: "Date", y: "Close"})\
  ]
})
```

Below a candlestick chart is constructed from two [rule marks](https://observablehq.com/plot/marks/rule), with a bollinger mark underneath to emphasize the days when the stock was more volatile.

68707274767880828486889092Jan2014FebMarAprMayJun

js

```
Plot.plot({
  x: {domain: [new Date("2014-01-01"), new Date("2014-06-01")]},
  y: {domain: [68, 92], grid: true},
  color: {domain: [-1, 0, 1], range: ["red", "black", "green"]},
  marks: [\
    Plot.bollingerY(aapl, {x: "Date", y: "Close", stroke: "none", clip: true}),\
    Plot.ruleX(aapl, {x: "Date", y1: "Low", y2: "High", strokeWidth: 1, clip: true}),\
    Plot.ruleX(aapl, {x: "Date", y1: "Open", y2: "Close", strokeWidth: 3, stroke: (d) => Math.sign(d.Close - d.Open), clip: true})\
  ]
})
```

The bollinger mark has two constructors: the common [bollingerY](https://observablehq.com/plot/marks/bollinger#bollingerY) for when time goes right→ (or ←left); and the rare [bollingerX](https://observablehq.com/plot/marks/bollinger#bollingerX) for when time goes up↑ (or down↓).

201420152016201720186080100120140160180Close →

js

```
Plot.bollingerX(aapl, {y: "Date", x: "Close"}).plot()
```

As [shorthand](https://observablehq.com/plot/features/shorthand), you can pass an array of numbers as data. Below, the _x_ axis represents the zero-based index into the data ( _i.e._, trading days since May 13, 2013).

6070809010011012013014015016017018019002004006008001,0001,200

js

```
Plot.bollingerY(aapl.map((d) => d.Close)).plot()
```

## Bollinger options [​](https://observablehq.com/plot/marks/bollinger\#bollinger-options)

The bollinger mark is a [composite mark](https://observablehq.com/plot/features/marks#marks) consisting of two marks:

- an [area](https://observablehq.com/plot/marks/area) representing volatility as a band, and
- a [line](https://observablehq.com/plot/marks/line) representing a moving average

The bollinger mark supports the following special options:

- **n** \- the window size (the window transform’s **k** option), an integer; defaults to 20
- **k** \- the band radius, a number representing a multiple of standard deviations; defaults to 2
- **color** \- the fill color of the area, and the stroke color of the line; defaults to _currentColor_
- **opacity** \- the fill opacity of the area; defaults to 0.2
- **fill** \- the fill color of the area; defaults to **color**
- **fillOpacity** \- the fill opacity of the area; defaults to **opacity**
- **stroke** \- the stroke color of the line; defaults to **color**
- **strokeOpacity** \- the stroke opacity of the line; defaults to 1
- **strokeWidth** \- the stroke width of the line in pixels; defaults to 1.5

Any additional options are passed through to the underlying [line mark](https://observablehq.com/plot/marks/line), [area mark](https://observablehq.com/plot/marks/area), and [window transform](https://observablehq.com/plot/transforms/window). Unlike the window transform, the **strict** option defaults to true, and the **anchor** option defaults to _end_ (which assumes that the data is in chronological order).

## bollingerX( _data_, _options_) [​](https://observablehq.com/plot/marks/bollinger\#bollingerX)

js

```
Plot.bollingerX(aapl, {y: "Date", x: "Close"})
```

Returns a bollinger mark for when time goes up↑ (or down↓). If the **x** option is not specified, it defaults to the identity function, as when _data_ is an array of numbers \[ _x₀_, _x₁_, _x₂_, …\]. If the **y** option is not specified, it defaults to \[0, 1, 2, …\].

## bollingerY( _data_, _options_) [​](https://observablehq.com/plot/marks/bollinger\#bollingerY)

js

```
Plot.bollingerY(aapl, {x: "Date", y: "Close"})
```

Returns a bollinger mark for when time goes right→ (or ←left). If the **y** option is not specified, it defaults to the identity function, as when _data_ is an array of numbers \[ _y₀_, _y₁_, _y₂_, …\]. If the **x** option is not specified, it defaults to \[0, 1, 2, …\].

## bollinger( _options_) [​](https://observablehq.com/plot/marks/bollinger\#bollinger)

js

```
Plot.lineY(data, Plot.map({y: Plot.bollinger({n: 20})}, {x: "Date", y: "Close"}))
```

Returns a bollinger map method for use with the [map transform](https://observablehq.com/plot/transforms/map). The **k** option here defaults to zero instead of two.

Pager

[Previous pageBar](https://observablehq.com/plot/marks/bar)

[Next pageBox](https://observablehq.com/plot/marks/box)

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

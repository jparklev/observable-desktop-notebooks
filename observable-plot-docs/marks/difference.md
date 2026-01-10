---
url: "https://observablehq.com/plot/marks/difference"
title: "Difference mark | Plot"
---

# Difference mark [^0.6.12](https://github.com/observablehq/plot/releases/tag/v0.6.12 "added in v0.6.12") [​](https://observablehq.com/plot/marks/difference\#difference-mark)

The **difference mark** puts a metric in context by comparing it. Like the [area mark](https://observablehq.com/plot/marks/area), the region between two lines is filled; unlike the area mark, alternating color shows when the metric is above or below the comparison value.

In the simplest case, the difference mark compares a metric to a constant. For example, the plot below shows the [global surface temperature anomaly](https://data.giss.nasa.gov/gistemp/) from 1880–2016; 0° represents the 1951–1980 average; above-average temperatures are in red, while below-average temperatures are in blue. (It’s getting hotter.)

−0.6−0.4−0.20.00.20.40.60.81.01.2↑ Anomaly1880190019201940196019802000

js

```
Plot.differenceY(gistemp, {
  x: "Date",
  y: "Anomaly",
  positiveFill: "red",
  negativeFill: "blue",
  tip: true
}).plot({y: {grid: true}})
```

A 24-month [moving average](https://observablehq.com/plot/transforms/window) improves readability by smoothing out the noise.

−0.4−0.20.00.20.40.60.81.0↑ Anomaly1880190019201940196019802000

js

```
Plot.differenceY(
  gistemp,
  Plot.windowY(12 * 2, {
    x: "Date",
    y: "Anomaly",
    positiveFill: "red",
    negativeFill: "blue",
    tip: true
  })
).plot({y: {grid: true}})
```

More powerfully, the difference mark compares two metrics. For example, the plot below shows the number of travelers per day through TSA checkpoints in 2020 compared to 2019. (This in effect compares a metric against itself, but as the data represents each year as a separate column, it is equivalent to two metrics.) In the first two months of 2020, there were on average more travelers per day than 2019; yet when COVID-19 hit, there were many fewer travelers per day, dropping almost to zero.

JanFebMarAprMayJunJulAugSepOctNovDec02004006008001,0001,2001,4001,6001,8002,0002,2002,4002,6002,800↑ Travelers per day (thousands, 2020 vs. 2019)

js

```
Plot.plot({
  x: {tickFormat: "%b"},
  y: {grid: true, label: "Travelers"},
  marks: [\
    Plot.axisY({label: "Travelers per day (thousands, 2020 vs. 2019)", tickFormat: (d) => d / 1000}),\
    Plot.ruleY([0]),\
    Plot.differenceY(tsa, {x: "Date", y1: "2019", y2: "2020", tip: {format: {x: "%B %-d"}}})\
  ]
})
```

If the data is “tall” rather than “wide” — that is, if the two metrics we wish to compare are represented by separate _rows_ rather than separate _columns_ — we can use the [group transform](https://observablehq.com/plot/transforms/group) with the [find reducer](https://observablehq.com/plot/transforms/group#find): group the rows by **x** (date), then find the desired **y1** and **y2** for each group. The plot below shows daily minimum temperature for San Francisco compared to San Jose. Notice how the insulating fog keeps San Francisco warmer in winter and cooler in summer, reducing seasonal variation.

35404550556065↑ tminJanFebMarAprMayJunJulAugSepOctNovDec

js

```
Plot.plot({
  x: {tickFormat: "%b"},
  y: {grid: true},
  marks: [\
    Plot.ruleY([32]),\
    Plot.differenceY(\
      temperature,\
      Plot.windowY(\
        14,\
        Plot.groupX(\
          {\
            y1: Plot.find((d) => d.station === "SJ"),\
            y2: Plot.find((d) => d.station === "SF")\
          },\
          {\
            x: "date",\
            y: "tmin",\
            tip: true\
          }\
        )\
      )\
    )\
  ]
})
```

The difference mark can also be used to compare a metric to itself using the [shift transform](https://observablehq.com/plot/transforms/shift). The chart below shows year-over-year growth in the price of Apple stock.

60708090100110120130140150160170180190↑ Close2015201620172018

js

```
Plot.differenceY(aapl, Plot.shiftX("+1 year", {x: "Date", y: "Close"})).plot({y: {grid: true}})
```

For most of the covered time period, you would have made a profit by holding Apple stock for a year; however, if you bought in 2015 and sold in 2016, you would likely have lost money.

## Difference options [​](https://observablehq.com/plot/marks/difference\#difference-options)

The following channels are required:

- **x2** \- the horizontal position of the metric; bound to the _x_ scale
- **y2** \- the vertical position of the metric; bound to the _y_ scale

In addition to the [standard mark options](https://observablehq.com/plot/features/marks#mark-options), the following optional channels are supported:

- **x1** \- the horizontal position of the comparison; bound to the _x_ scale
- **y1** \- the vertical position of the comparison; bound to the _y_ scale

If **x1** is not specified, it defaults to **x2**. If **y1** is not specified, it defaults to 0 if **x1** and **x2** are equal, and to **y2** otherwise. These defaults facilitate sharing _x_ or _y_ coordinates between the metric and its comparison.

The standard **fill** option is ignored; instead, there are separate channels based on the sign of the difference:

- **positiveFill** \- the color for when the metric is greater, defaults to green
- **negativeFill** \- the color for when the comparison is greater, defaults to blue
- **fillOpacity** \- the areas’ opacity, defaults to 1
- **positiveFillOpacity** \- the positive area’s opacity, defaults to _opacity_
- **negativeFillOpacity** \- the negative area’s opacity, defaults to _opacity_
- **stroke** \- the metric line’s stroke color, defaults to currentColor
- **strokeOpacity** \- the metric line’s opacity, defaults to 1

These options are passed to the underlying area and line marks; in particular, when they are defined as a channel, the underlying marks are broken into contiguous overlapping segments when the values change. When any of these channels are used, setting an explicit **z** channel (possibly to null) is strongly recommended.

## differenceY( _data_, _options_) [​](https://observablehq.com/plot/marks/difference\#differenceY)

js

```
Plot.differenceY(gistemp, {x: "Date", y: "Anomaly"})
```

Returns a new vertical difference with the given _data_ and _options_. The mark is a composite of a positive area, negative area, and line. The positive area extends from the bottom of the frame to the line, and is clipped by the area extending from the comparison to the top of the frame. The negative area conversely extends from the top of the frame to the line, and is clipped by the area extending from the comparison to the bottom of the frame.

## differenceX( _data_, _options_) [^0.6.16](https://github.com/observablehq/plot/releases/tag/v0.6.16 "added in v0.6.16") [​](https://observablehq.com/plot/marks/difference\#differenceX)

js

```
Plot.differenceX(gistemp, {y: "Date", x: "Anomaly"})
```

Returns a new horizontal difference with the given _data_ and _options_. See [differenceY](https://observablehq.com/plot/marks/difference#differenceY) for more.

Pager

[Previous pageDensity](https://observablehq.com/plot/marks/density)

[Next pageDot](https://observablehq.com/plot/marks/dot)

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

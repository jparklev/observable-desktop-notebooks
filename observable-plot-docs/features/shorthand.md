---
url: "https://observablehq.com/plot/features/shorthand"
title: "Shorthand | Plot"
---

# Shorthand [^0.4.2](https://github.com/observablehq/plot/releases/tag/v0.4.2 "added in v0.4.2") [​](https://observablehq.com/plot/features/shorthand\#shorthand)

The most concise form of Plot is its **shorthand** syntax where no options are specified — only data. To use this shorthand, the data must have a specific structure: either a one-dimensional array of values \[ _v₀_, _v₁_, _v₂_, …\] or a two-dimensional array of tuples \[\[ _x₀_, _y₀_\], \[ _x₁_, _y₁_\], \[ _x₂_, _y₂_\], …\].

While none of these charts are particularly groundbreaking, we hope you find this shorthand convenient the next time you want a quick look at some data. And if the shorthand view is useful, you can then enhance it by adding options!

## One dimension [​](https://observablehq.com/plot/features/shorthand\#one-dimension)

Let’s start with the one-dimensional form: an array of numbers.

js

```
numbers = [\
  170.16, 172.53, 172.54, 173.44, 174.35, 174.55, 173.16, 174.59, 176.18, 177.90,\
  176.15, 179.37, 178.61, 177.30, 177.30, 177.25, 174.51, 172.00, 170.16, 165.53,\
  166.87, 167.17, 166.00, 159.10, 154.83, 163.09, 160.29, 157.07, 158.50, 161.95,\
  163.04, 169.79, 172.36, 172.05, 172.83, 171.80, 173.67, 176.35, 179.10, 179.26\
]
```

These numbers represent the daily opening price of Apple stock starting on January 1, 2018. For a simple line chart, we can pass the data to [Plot.lineY](https://observablehq.com/plot/marks/line) to construct a line mark, and then call _line_.plot.

15615816016216416616817017217417617805101520253035 [Fork](https://observablehq.com/@observablehq/plot-shorthand-one-dimensional-line "Open on Observable")

js

```
Plot.lineY(numbers).plot()
```

The _y_-axis above represents price in U.S. dollars. The _x_-axis represents the index of the data: the first value 170.16 is shown at _x_ = 0, the second value 172.53 at _x_ = 1, and so on. In other words, _x_ represents the number of (trading) days since January 1, 2018. It’d be nicer to have an _x_-axis that shows dates here, but it’s still convenient to see the trend in stock price quickly.

If we pass the numbers to [Plot.areaY](https://observablehq.com/plot/marks/area) instead, we’ll get a simple area chart with a baseline implicitly at _y_ = 0.

02040608010012014016005101520253035 [Fork](https://observablehq.com/@observablehq/plot-shorthand-one-dimensional-area "Open on Observable")

js

```
Plot.areaY(numbers).plot()
```

Similarly if we use [Plot.rectY](https://observablehq.com/plot/marks/rect), we’ll get a series of vertical bars. This implicitly uses the [interval transform](https://observablehq.com/plot/transforms/interval) such that the first rect spans from _x_ = 0 to _x_ = 1, the second from _x_ = 1 to _x_ = 2, and so on, with a horizontal inset to separate adjacent rects.

0204060801001201401600510152025303540 [Fork](https://observablehq.com/@observablehq/plot-shorthand-one-dimensional-rect "Open on Observable")

js

```
Plot.rectY(numbers).plot()
```

[Plot.barY](https://observablehq.com/plot/marks/bar) produces a visually similar result but with different semantics: _x_ is now ordinal (a _band_ scale) rather than quantitative ( _linear_). An ordinal axis labels every tick, which appear at the middle of each bar rather than between rects.

0204060801001201401600123456789101112131415161718192021222324252627282930313233343536373839 [Fork](https://observablehq.com/@observablehq/plot-shorthand-one-dimensional-bar "Open on Observable")

js

```
Plot.barY(numbers).plot()
```

Like Plot.barY, [Plot.cellX](https://observablehq.com/plot/marks/cell) implies that _x_ is ordinal. But now instead of a _y_ channel the numeric value is encoded as the _fill_ color. The default quantitative color scheme is _turbo_; higher values are reddish, and lower values blueish.

0123456789101112131415161718192021222324252627282930313233343536373839 [Fork](https://observablehq.com/@observablehq/plot-shorthand-one-dimensional-cell "Open on Observable")

js

```
Plot.cellX(numbers).plot()
```

If we don’t care about the order of our data and we instead just want to look at the one-dimensional distribution of values, we can use [Plot.dotX](https://observablehq.com/plot/marks/dot).

156158160162164166168170172174176178 [Fork](https://observablehq.com/@observablehq/plot-shorthand-one-dimensional-dot "Open on Observable")

js

```
Plot.dotX(numbers).plot()
```

Alternatively, we can use [Plot.ruleX](https://observablehq.com/plot/marks/rule) to draw a vertical rule at each value. In this case, Plot.ruleX behaves identically to [Plot.tickX](https://observablehq.com/plot/marks/tick). (If there _were_ a _y_ channel, then Plot.tickX would imply that _y_ is ordinal whereas Plot.ruleX would imply that _y_ is quantitative.) It is common to use the rule shorthand to annotate special _x_ or _y_ values in plots, such as _y_ = 0, in conjunction with other marks.

156158160162164166168170172174176178 [Fork](https://observablehq.com/@observablehq/plot-shorthand-one-dimensional-rule "Open on Observable")

js

```
Plot.ruleX(numbers).plot()
```

156158160162164166168170172174176178 [Fork](https://observablehq.com/@observablehq/plot-shorthand-one-dimensional-tick "Open on Observable")

js

```
Plot.tickX(numbers).plot()
```

We could even use [Plot.vectorX](https://observablehq.com/plot/marks/vector) here to draw little up-pointing arrows. (Typically the vector mark is used in conjunction with the **rotate** and **length** options to control the direction and magnitude of each vector.)

156158160162164166168170172174176178 [Fork](https://observablehq.com/@observablehq/plot-shorthand-one-dimensional-vector "Open on Observable")

js

```
Plot.vectorX(numbers).plot()
```

While not particularly readable due to occlusion, we can use [Plot.textX](https://observablehq.com/plot/marks/text) to draw a label at each value, too.

156158160162164166168170172174176178170.16172.53172.54173.44174.35174.55173.16174.59176.18177.9176.15179.37178.61177.3177.3177.25174.51172170.16165.53166.87167.17166159.1154.83163.09160.29157.07158.5161.95163.04169.79172.36172.05172.83171.8173.67176.35179.1179.26 [Fork](https://observablehq.com/@observablehq/plot-shorthand-one-dimensional-text "Open on Observable")

js

```
Plot.textX(numbers).plot()
```

For a more formal method of summarizing a one-dimensional distribution, we can use [Plot.boxX](https://observablehq.com/plot/marks/box) to create a horizontal boxplot. The gray band represents the interquartile range; the black whiskers show the extrema (not including outliers); and the thick black stroke represents the median; any outliers (none in this dataset) are drawn as dots.

156158160162164166168170172174176178 [Fork](https://observablehq.com/@observablehq/plot-shorthand-box "Open on Observable")

js

```
Plot.boxX(numbers).plot()
```

Some of Plot’s transforms support shorthand syntax, too. For example, we can use Plot.rectY with [Plot.binX](https://observablehq.com/plot/transforms/bin) to generate a histogram — another common way to visualize a one-dimensional distribution.

0246810121416↑ Frequency150155160165170175180 [Fork](https://observablehq.com/@observablehq/plot-shorthand-histogram "Open on Observable")

js

```
Plot.rectY(numbers, Plot.binX()).plot()
```

Similarly [Plot.groupX](https://observablehq.com/plot/transforms/group) can be used to group and count ordinal data, such as the frequency of bases in a random DNA sequence.

js

```
gene = "AAAAGAGTGAAGATGCTGGAGACGAGTGAAGCATTCACTTTAGGGAAAGCGAGGCAAGAGCGTTTCAGAAGACGAAACCTGGTAGGTGCACTCACCACAG"
```

05101520253035↑ FrequencyACGT [Fork](https://observablehq.com/@observablehq/plot-shorthand-group "Open on Observable")

js

```
Plot.barY(gene, Plot.groupX()).plot()
```

And here’s the [dodge transform](https://observablehq.com/plot/transforms/dodge) for a beeswarm plot:

156158160162164166168170172174176178 [Fork](https://observablehq.com/@observablehq/plot-shorthand-dodge "Open on Observable")

js

```
Plot.dotX(numbers, Plot.dodgeY()).plot()
```

## Two dimensions [​](https://observablehq.com/plot/features/shorthand\#two-dimensions)

Now let’s switch to a two-dimensional array of tuples \[\[ _x₀_, _y₀_\], \[ _x₁_, _y₁_\], \[ _x₂_, _y₂_\], …\]. The _x_-values here are times (Date instances at UTC midnight); the _y_-values again are the daily opening price of Apple stock.

js

```
timeSeries = [\
  [new Date("2018-01-02"), 170.160004],\
  [new Date("2018-01-03"), 172.529999],\
  [new Date("2018-01-04"), 172.539993],\
  [new Date("2018-01-05"), 173.440002],\
  [new Date("2018-01-08"), 174.350006],\
  [new Date("2018-01-09"), 174.550003],\
  [new Date("2018-01-10"), 173.160004],\
  [new Date("2018-01-11"), 174.589996],\
  [new Date("2018-01-12"), 176.179993],\
  [new Date("2018-01-16"), 177.899994],\
  [new Date("2018-01-17"), 176.149994],\
  [new Date("2018-01-18"), 179.369995],\
  [new Date("2018-01-19"), 178.610001],\
  [new Date("2018-01-22"), 177.300003],\
  [new Date("2018-01-23"), 177.300003],\
  [new Date("2018-01-24"), 177.250000],\
  [new Date("2018-01-25"), 174.509995],\
  [new Date("2018-01-26"), 172.000000],\
  [new Date("2018-01-29"), 170.160004],\
  [new Date("2018-01-30"), 165.529999],\
  [new Date("2018-01-31"), 166.869995],\
  [new Date("2018-02-01"), 167.169998],\
  [new Date("2018-02-02"), 166.000000],\
  [new Date("2018-02-05"), 159.100006],\
  [new Date("2018-02-06"), 154.830002],\
  [new Date("2018-02-07"), 163.089996],\
  [new Date("2018-02-08"), 160.289993],\
  [new Date("2018-02-09"), 157.070007],\
  [new Date("2018-02-12"), 158.500000],\
  [new Date("2018-02-13"), 161.949997],\
  [new Date("2018-02-14"), 163.039993],\
  [new Date("2018-02-15"), 169.789993],\
  [new Date("2018-02-16"), 172.360001],\
  [new Date("2018-02-20"), 172.050003],\
  [new Date("2018-02-21"), 172.830002],\
  [new Date("2018-02-22"), 171.800003],\
  [new Date("2018-02-23"), 173.669998],\
  [new Date("2018-02-26"), 176.350006],\
  [new Date("2018-02-27"), 179.100006],\
  [new Date("2018-02-28"), 179.259995]\
]
```

If we pass this to Plot.line ( _not_ Plot.lineY as before), we’ll get another line chart, but now the _x_-axis shows the date rather than the zero-based index. Also, the _x_-values are no longer uniformly spaced, as there are gaps on the weekends and holidays when the markets are closed.

1561581601621641661681701721741761787Jan1421284Feb111825 [Fork](https://observablehq.com/@observablehq/plot-shorthand-temporal-line "Open on Observable")

js

```
Plot.line(timeSeries).plot()
```

Similarly Plot.area will produce the equivalent area chart, again with an implicit baseline at _y_ = 0.

0204060801001201401607Jan1421284Feb111825 [Fork](https://observablehq.com/@observablehq/plot-shorthand-temporal-area "Open on Observable")

js

```
Plot.area(timeSeries).plot()
```

There’s currently no two-dimensional shorthand for rect or bar, though you can use these marks to display time series data with options.

Plot.dot will produce a scatterplot…

1561581601621641661681701721741761787Jan1421284Feb111825 [Fork](https://observablehq.com/@observablehq/plot-shorthand-temporal-dot "Open on Observable")

js

```
Plot.dot(timeSeries).plot()
```

As will Plot.vector…

1561581601621641661681701721741761787Jan1421284Feb111825 [Fork](https://observablehq.com/@observablehq/plot-shorthand-temporal-vector "Open on Observable")

js

```
Plot.vector(timeSeries).plot()
```

Plot.text also produces a scatterplot with labels showing the zero-based index of the data. Perhaps not very useful, but it at least shows the data’s order.

1561581601621641661681701721741761787Jan1421284Feb1118250123456789101112131415161718192021222324252627282930313233343536373839 [Fork](https://observablehq.com/@observablehq/plot-shorthand-temporal-text "Open on Observable")

js

```
Plot.text(timeSeries).plot()
```

Plot.cell also supports two-dimensional shorthand. As we saw above, Plot.cell implies that _x_ and _y_ are ordinal, so we shouldn’t pass temporal (dates) and quantitative (numbers) data; here’s a matrix diagram that shows which pairs exist in the dataset. You might use this, for example, to visualize who reviewed whose code.

js

```
matrix = [\
  ["Jacob", "Olivia"],\
  ["Mia", "Noah"],\
  ["Noah", "Ava"],\
  ["Ava", "Mason"],\
  ["Olivia", "Noah"],\
  ["Jacob", "Emma"],\
  ["Ava", "Noah"],\
  ["Noah", "Jacob"],\
  ["Olivia", "Ava"],\
  ["Mason", "Emma"],\
  ["Jacob", "Mia"],\
  ["Mia", "Jacob"],\
  ["Emma", "Jacob"]\
]
```

AvaEmmaJacobMasonMiaNoahOliviaAvaEmmaJacobMasonMiaNoahOlivia [Fork](https://observablehq.com/@observablehq/plot-shorthand-cell "Open on Observable")

js

```
Plot.cell(matrix).plot()
```

## Caveats [​](https://observablehq.com/plot/features/shorthand\#caveats)

Plot has a few marks that don’t currently provide meaningful shorthand. The [arrow](https://observablehq.com/plot/marks/arrow) and [link](https://observablehq.com/plot/marks/link) marks both require a start ( _x1_, _y1_) and end ( _x2_, _y2_) point; and the [image](https://observablehq.com/plot/marks/image) mark requires a source URL ( _src_).

Pager

[Previous pageMarkers](https://observablehq.com/plot/features/markers)

[Next pageAccessibility](https://observablehq.com/plot/features/accessibility)

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

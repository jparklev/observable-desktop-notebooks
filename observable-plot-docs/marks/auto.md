---
url: "https://observablehq.com/plot/marks/auto"
title: "Auto mark | Plot"
---

# Auto mark [^0.6.3](https://github.com/observablehq/plot/releases/tag/v0.6.3 "added in v0.6.3") [​](https://observablehq.com/plot/marks/auto\#auto-mark)

The magic ✨ **auto mark** automatically selects a mark type that best represents the given dimensions of the data according to some simple heuristics. The auto mark — which powers [Observable’s chart cell](https://observablehq.com/@observablehq/chart-cell) — is intended to support fast exploratory analysis where the goal is to get a useful plot as quickly as possible. For example, two quantitative dimensions make a scatterplot:

175180185190195200205210215220225230↑ flipper\_length\_mm3,0003,5004,0004,5005,0005,5006,000body\_mass\_g → [Fork](https://observablehq.com/@observablehq/plot-auto-mark-scatterplot "Open on Observable")

js

```
Plot.auto(penguins, {x: "body_mass_g", y: "flipper_length_mm"}).plot()
```

TIP

The auto mark is supposed to be fast and fluid, so don’t overthink it. If you need precise control, use explicit marks instead.

CAUTION

While the auto mark will respect the options you provide, you shouldn’t rely on its behavior being stable over time. The auto mark may get smarter and take advantage of new features. Because its heuristics are likely to evolve, they are not explicitly documented; see the [source code](https://github.com/observablehq/plot/blob/main/src/marks/auto.js) for details.

A monotonically increasing dimension (here _Date_, as the data is ordered chronologically), paired with a numeric column ( _Close_), makes a line chart:

60708090100110120130140150160170180190↑ Close20142015201620172018 [Fork](https://observablehq.com/@observablehq/plot-auto-mark-line-chart "Open on Observable")

js

```
Plot.auto(aapl, {x: "Date", y: "Close"}).plot()
```

Given only one dimension of data, it makes a histogram:

050100150200250300350400450500550600↑ Frequency406080100120140160weight → [Fork](https://observablehq.com/@observablehq/plot-auto-mark-quantitative-histogram "Open on Observable")

js

```
Plot.auto(olympians, {x: "weight"}).plot()
```

020406080100120140160↑ FrequencyBiscoeDreamTorgersenisland [Fork](https://observablehq.com/@observablehq/plot-auto-mark-ordinal-histogram "Open on Observable")

js

```
Plot.auto(penguins, {x: "island"}).plot()
```

This is easier than deciding whether to use bin and rect, or group and bar: the auto mark chooses the right one based on whether the data is quantitative or ordinal.

If you’d like to explicitly avoid grouping the data, you can opt out of the reducer, and get a one-dimensional plot:

3,0003,5004,0004,5005,0005,5006,000body\_mass\_g → [Fork](https://observablehq.com/@observablehq/plot-auto-mark-barcode "Open on Observable")

js

```
Plot.auto(penguins, {x: "body_mass_g", y: {reduce: null}}).plot()
```

As you can see from that **reduce** property, the auto mark has some special syntax that lets you specify a reducer without explicitly specifying a transform. For example, the scatterplot above can be made into a heatmap by adding a color reducer. You can pass the name of a reducer to that property, or pass a shorthand string:

1.21.31.41.51.61.71.81.92.02.12.2↑ height406080100120140160weight → [Fork](https://observablehq.com/@observablehq/plot-auto-mark-heatmap "Open on Observable")

js

```
Plot.auto(olympians, {x: "weight", y: "height", color: "count"}).plot()
```

That’s equivalent to this:

js

```
Plot.rect(olympians, Plot.bin({fill: "count"}, {x: "weight", y: "height"})).plot()
```

Notice that the code above makes you think about nested functions and two different options objects, which the auto mark flattens. The auto mark infers that it should use a [rect](https://observablehq.com/plot/marks/rect); that it should [bin](https://observablehq.com/plot/transforms/bin) on **x** and **y**; that the kind of color should be a **fill**; and that **fill** is an “output” of the reducer, whereas **x** and **y** are “inputs”.

This saves you a little bit of typing, but, more importantly, it means that switching from showing one dimension to another only involves changing _one thing_. In the code above, if you change **y** from _weight_ to _sex_, it’ll break, because _sex_ is ordinal instead of quantitative. (You’d also have to change [rect](https://observablehq.com/plot/marks/rect) to [barX](https://observablehq.com/plot/marks/bar#barX), and [bin](https://observablehq.com/plot/transforms/bin#bin) to [binX](https://observablehq.com/plot/transforms/bin#binX).) With the auto mark, it just works:

femalemalesex406080100120140160weight → [Fork](https://observablehq.com/@observablehq/plot-auto-mark-heatmap-2 "Open on Observable")

js

```
Plot.auto(olympians, {x: "weight", y: "sex", color: "count"}).plot()
```

Similarly, with explicit marks and transforms, changing a vertical histogram to a horizontal histogram involves switching [rectY](https://observablehq.com/plot/marks/rect#rectY) to [rectX](https://observablehq.com/plot/marks/rect#rectX), [binX](https://observablehq.com/plot/transforms/bin#binX) to [binY](https://observablehq.com/plot/transforms/bin#binY), **x** to **y**, and **y** to **x**. With the auto mark, just specify **y** instead of **x**:

BiscoeDreamTorgersenisland020406080100120140160Frequency → [Fork](https://observablehq.com/@observablehq/plot-auto-mark-horizontal-histogram "Open on Observable")

js

```
Plot.auto(penguins, {y: "island"}).plot()
```

For the sake of seamless switching, the auto mark has just one color channel, which it assigns to either **fill** or **stroke** depending on the mark. We can see that clearly by overriding a line chart with the **mark** option to make an area chart:

2004006008001,0001,2001,4001,6001,8002,0002,2002,400↑ unemployed20002001200220032004200520062007200820092010 [Fork](https://observablehq.com/@observablehq/plot-auto-mark-color-channel "Open on Observable")

js

```
Plot.auto(industries, {x: "date", y: "unemployed", color: "industry"}).plot()
```

02,0004,0006,0008,00010,00012,00014,000↑ unemployed20002001200220032004200520062007200820092010

js

```
Plot.auto(industries, {x: "date", y: "unemployed", color: "industry", mark: "area"}).plot()
```

The **mark** override option supports [dot](https://observablehq.com/plot/marks/dot), [line](https://observablehq.com/plot/marks/line), [area](https://observablehq.com/plot/marks/area), [rule](https://observablehq.com/plot/marks/rule), and [bar](https://observablehq.com/plot/marks/bar) (which automatically chooses among barX, barY, rectX, rectY, rect, and cell).

You can get a more elaborate aggregated chart by passing an object with both a **value** (the input dimension) and a **reduce** (the reducer). For example, here’s the average heights of Olympians over time by sex:

femalemale

1.601.651.701.751.801.851.90↑ height1955196019651970197519801985199019952000date\_of\_birth → [Fork](https://observablehq.com/@observablehq/plot-auto-mark-with-value-and-reduce "Open on Observable")

js

```
Plot
  .auto(olympians, {x: "date_of_birth", y: {value: "height", reduce: "mean"}, color: "sex", mark: "line"})
  .plot({color: {legend: true}})
```

You can similarly pass a **zero** option to indicate that zero is meaningful for either **x** or **y**. This adds a corresponding rule to the returned mark.

02004006008001,0001,2001,4001,6001,8002,0002,2002,400↑ unemployed20002001200220032004200520062007200820092010 [Fork](https://observablehq.com/@observablehq/plot-auto-mark-zero-option "Open on Observable")

js

```
Plot.auto(industries, {x: "date", y: {value: "unemployed", zero: true}, color: "industry"}).plot()
```

The auto mark has a **size** channel, which (currently) always results in a dot. For now, it’s an alias for the dot’s **r** channel; in the future it will also represent a vector’s **length** channel.

60708090100110120130140150160170180190↑ Close20142015201620172018 [Fork](https://observablehq.com/@observablehq/plot-auto-mark-size-channel "Open on Observable")

js

```
Plot.auto(aapl, {x: "Date", y: "Close", size: "Volume"}).plot()
```

Like with any other mark, you can also use **fx** or **fy**, and pass additional global options in the plot method.

AdelieChinstrapGentoospeciesBiscoeDreamTorgersenisland354045505535404550553540455055↑ culmen\_length\_mm3,0004,0005,0006,0003,0004,0005,0006,0003,0004,0005,0006,0003,0004,0005,0006,000body\_mass\_g → [Fork](https://observablehq.com/@observablehq/plot-auto-mark-faceted "Open on Observable")

js

```
Plot.auto(penguins, {
  x: "body_mass_g",
  y: "culmen_length_mm",
  fx: "island",
  fy: "species"
}).plot({
  grid: true,
  x: {ticks: 5},
  marginRight: 70
})
```

Caution

You can combine the auto mark with other marks, but the combination may be brittle because the auto mark may pick encodings that don’t play well with others.

## Auto options [​](https://observablehq.com/plot/marks/auto\#auto-options)

The auto mark currently supports only a subset of the standard [mark options](https://observablehq.com/plot/features/marks#mark-options). You must provide at least one position channel:

- **x** \- horizontal position
- **y** \- vertical position

You may also provide one or more visual encoding channels:

- **color** \- corresponds to **stroke** or **fill** (depending on the chosen mark type)
- **size** \- corresponds to **r** (and in future, possibly **length**)

And you may specify the standard mark-level facet channels:

- **fx** \- horizontal facet position (column)
- **fy** \- vertical facet position (row)

In addition to channel values, the **x**, **y**, **color**, and **size** options may specify reducers. Setting a reducer on **x** implicitly groups or bins on **y**, and likewise setting a reducer on **y** implicitly groups or bins on **x**. Setting a reducer on **color** or **size** groups or bins in both **x** and **y**. Setting a reducer on both **x** and **y** throws an error. To specify a reducer, simply pass the reducer name to the corresponding option. For example:

js

```
Plot.auto(penguins, {x: "body_mass_g", y: "count"})
```

To pass both a value and a reducer, or to disambiguate whether the given string represents a field name or a reducer name, the **x**, **y**, **color**, and **size** options can also be specified as an object with separate **value** and **reduce** properties. For example, to compute the total weight of the penguins in each bin:

js

```
Plot.auto(penguins, {x: "body_mass_g", y: {value: "body_mass_g", reduce: "sum"}})
```

If the **color** channel is specified as a string that is also a valid CSS color, it is interpreted as a constant color. For example, for red bars:

js

```
Plot.auto(penguins, {x: "body_mass_g", color: "red"})
```

This is shorthand for:

js

```
Plot.auto(penguins, {x: "body_mass_g", color: {color: "red"}})
```

To reference a field name instead as a variable color encoding, specify the **color** option as an object with a **value** property:

js

```
Plot.auto(penguins, {x: "body_mass_g", color: {value: "red"}})
```

Alternatively, you can specify a function of data or an array of values, as with a standard mark channel.

The auto mark chooses the mark type automatically based on several simple heuristics. For more control, you can specify the desired mark type using the **mark** option, which supports the following names:

- _area_ \- areaY or areaX (or sometimes area)
- _bar_ \- barY or barX; or rectY, rectX, or rect; or cell
- _dot_ \- dot
- _line_ \- lineY or lineX (or sometimes line)
- _rule_ \- ruleY or ruleX

The chosen mark type depends both on the options you provide ( _e.g._, whether you specified **x** or **y** or both) and the inferred type of the corresponding data values (whether the associated dimension of data is quantitative, categorical, monotonic, _etc._).

## auto( _data_, _options_) [​](https://observablehq.com/plot/marks/auto\#auto)

js

```
Plot.auto(olympians, {x: "weight", y: "height", color: "count"}) // equivalent to rect + bin, say
```

Returns an automatically-chosen mark with the given _data_ and _options_, suitable for a quick view of the data.

## autoSpec( _data_, _options_) [^0.6.4](https://github.com/observablehq/plot/releases/tag/v0.6.4 "added in v0.6.4") [​](https://observablehq.com/plot/marks/auto\#autoSpec)

js

```
Plot.autoSpec(olympians, {x: "weight", y: "height", color: "count"})
```

Returns an auto mark _options_ object with no option undefined; the mark type, reducers, and other options are all populated.

Pager

[Previous pageArrow](https://observablehq.com/plot/marks/arrow)

[Next pageAxis](https://observablehq.com/plot/marks/axis)

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

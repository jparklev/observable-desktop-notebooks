---
url: "https://observablehq.com/plot/features/marks"
title: "Marks | Plot"
---

# Marks [​](https://observablehq.com/plot/features/marks\#Marks)

TIP

If you aren’t yet up and running with Plot, please read our [getting started guide](https://observablehq.com/plot/getting-started) first. Tinkering with the code below will give a better sense of how Plot works.

Plot doesn’t have chart types; instead, you construct charts by layering **marks**.

## Marks are geometric shapes [​](https://observablehq.com/plot/features/marks\#marks-are-geometric-shapes)

Plot provides a variety of mark types. Think of marks as the “visual vocabulary” — the painter’s palette 🎨, but of shapes instead of colors — that you pull from when composing a chart. Each mark type produces a certain type of geometric shape.

For example, the [dot mark](https://observablehq.com/plot/marks/dot) draws stroked circles (by default).

−0.6−0.4−0.20.00.20.40.60.81.01.2↑ Anomaly1880190019201940196019802000 [Fork](https://observablehq.com/@observablehq/plot-temporal-scatterplot "Open on Observable")

js

```
Plot.dot(gistemp, {x: "Date", y: "Anomaly"}).plot()
```

The [line mark](https://observablehq.com/plot/marks/line) draws connected line segments (also known as a _polyline_ or _polygonal chain_).

−0.6−0.4−0.20.00.20.40.60.81.01.2↑ Anomaly1880190019201940196019802000 [Fork](https://observablehq.com/@observablehq/plot-temporal-line-chart "Open on Observable")

js

```
Plot.lineY(gistemp, {x: "Date", y: "Anomaly"}).plot()
```

And the [bar mark](https://observablehq.com/plot/marks/bar) draws rectangular bars in either a horizontal (barX→) or vertical (barY↑) orientation.

ABCDEFGHIJKLMNOPQRSTUVWXYZletter0.000.020.040.060.080.100.12frequency → [Fork](https://observablehq.com/@observablehq/plot-alphabet-bar-chart "Open on Observable")

js

```
Plot.barX(alphabet, {x: "frequency", y: "letter"}).plot()
```

So instead of looking for a chart type, consider the shape of the primary graphical elements in your chart, and look for the corresponding mark type. If a chart has only a single mark, the mark type _is_ effectively the chart type: the bar mark is used to make a bar chart, the area mark is used to make an area chart, and so on.

## Marks are layered [​](https://observablehq.com/plot/features/marks\#marks-are-layered)

The big advantage of mark types over chart types is that you can compose multiple marks of different types into a single [plot](https://observablehq.com/plot/features/plots). For example, below an [area](https://observablehq.com/plot/marks/area) and [line](https://observablehq.com/plot/marks/line) are used to plot the same sequence of values, while a [rule](https://observablehq.com/plot/marks/rule) emphasizes _y_ = 0.

020406080100120140160180↑ Close20142015201620172018 [Fork](https://observablehq.com/@observablehq/plot-layered-marks-2 "Open on Observable")

js

```
Plot.plot({
  marks: [\
    Plot.ruleY([0]),\
    Plot.areaY(aapl, {x: "Date", y: "Close", fillOpacity: 0.2}),\
    Plot.lineY(aapl, {x: "Date", y: "Close"})\
  ]
})
```

Each mark supplies its own data; a quick way to combine multiple datasets into a chart is to declare a separate mark for each. You can even use [_array_.map](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/map) to create multiple marks from nested data.

1002003004005006007008009001,0001,100↑ Close20142015201620172018 [Fork](https://observablehq.com/@observablehq/plot-layered-marks-2 "Open on Observable")

js

```
Plot.plot({
  marks: [\
    [goog, aapl].map((stock) => Plot.lineY(stock, {x: "Date", y: "Close"}))\
  ]
})
```

Marks may also be a function which returns an [SVG element](https://developer.mozilla.org/en-US/docs/Web/SVG/Element), if you wish to insert arbitrary content. (Here we use [Hypertext Literal](https://github.com/observablehq/htl) to generate an SVG gradient.)

0.000.010.020.030.040.050.060.070.080.090.100.110.12↑ frequencyABCDEFGHIJKLMNOPQRSTUVWXYZletter[Fork](https://observablehq.com/@observablehq/plot-gradient-bars "Open on Observable")

js

```
Plot.plot({
  marks: [\
    () => htl.svg`<defs>\
      <linearGradient id="gradient" gradientTransform="rotate(90)">\
        <stop offset="15%" stop-color="purple" />\
        <stop offset="75%" stop-color="red" />\
        <stop offset="100%" stop-color="gold" />\
      </linearGradient>\
    </defs>`,\
    Plot.barY(alphabet, {x: "letter", y: "frequency", fill: "url(#gradient)"}),\
    Plot.ruleY([0])\
  ]
})
```

And marks may be null or undefined, which produce no output; this is useful for showing marks conditionally ( _e.g._, when a box is checked).

Show area:

020406080100120140160180↑ Close20142015201620172018 [Fork](https://observablehq.com/@observablehq/plot-optional-marks "Open on Observable")

js

```
Plot.plot({
  marks: [\
    Plot.ruleY([0]),\
    area ? Plot.areaY(aapl, {x: "Date", y: "Close", fillOpacity: 0.2}) : null,\
    Plot.lineY(aapl, {x: "Date", y: "Close"})\
  ]
})
```

## Marks use scales [​](https://observablehq.com/plot/features/marks\#marks-use-scales)

Marks are (typically) not positioned in literal pixels, or colored in literal colors, as in a conventional graphics system. Instead you provide abstract values such as time and temperature — marks are drawn “in data space” — and [scales](https://observablehq.com/plot/features/scales) encode these into visual values such as position and color. And best of all, Plot automatically creates [axes](https://observablehq.com/plot/marks/axis) and [legends](https://observablehq.com/plot/features/legends) to document the scales’ encodings.

Data is passed through scales automatically during rendering; the mark controls which scales are used. The **x** and **y** options are typically bound to the _x_ and _y_ scales, respectively, while the **fill** and **stroke** options are typically bound to the _color_ scale. Changing a scale’s definition, say by overriding its **domain** (the extent of abstract input values) or **type**, affects the appearance of all marks that use the scale.

30405060708090100200300↑ Close20142015201620172018 [Fork](https://observablehq.com/@observablehq/plot-aapl-log-scale "Open on Observable")

js

```
Plot.plot({
  y: {
    type: "log",
    domain: [30, 300],
    grid: true
  },
  marks: [\
    Plot.lineY(aapl, {x: "Date", y: "Close"})\
  ]
})
```

## Marks have tidy data [​](https://observablehq.com/plot/features/marks\#marks-have-tidy-data)

A single mark can draw multiple shapes. A mark generally produces a shape — such as a rectangle or circle — for each element in the data.

60708090100110120130140150160170180190↑ Close20142015201620172018 [Fork](https://observablehq.com/@observablehq/plot-tidy-data "Open on Observable")

js

```
Plot.dot(aapl, {x: "Date", y: "Close"}).plot()
```

It’s more complicated than that, though, since some marks produce shapes that incorporate _multiple_ data points. Pass the same data to a [line](https://observablehq.com/plot/marks/line) and you’ll get a single polyline.

60708090100110120130140150160170180190↑ Close20142015201620172018 [Fork](https://observablehq.com/@observablehq/plot-tidy-data "Open on Observable")

js

```
Plot.lineY(aapl, {x: "Date", y: "Close"}).plot()
```

And a line mark isn’t even guaranteed to produce a single polyline — there can be multiple polylines, as in a line chart with multiple series (using **z**).

46810121416↑ unemployment2000200220042006200820102012 [Fork](https://observablehq.com/@observablehq/plot-multiple-series-line-chart "Open on Observable")

js

```
Plot.lineY(bls, {x: "date", y: "unemployment", z: "division"}).plot()
```

Plot favors [tidy data](http://vita.had.co.nz/papers/tidy-data.html) structured as an array of objects, where each object represents an observation (a row), and each object property represents an observed value; all objects in the array should have the same property names (the columns).

For example, say we have hourly readings from two sensors _A_ and _B_. You can represent the sensor log as an array of objects like so:

js

```
linedata = [\
  {hour: 0, value: 8, sensor: "A"},\
  {hour: 0, value: 6, sensor: "B"},\
  {hour: 1, value: 7, sensor: "A"},\
  {hour: 1, value: 5, sensor: "B"},\
  {hour: 2, value: 3, sensor: "A"},\
  {hour: 2, value: 0, sensor: "B"},\
  {hour: 3, value: 9, sensor: "A"},\
  {hour: 3, value: 2, sensor: "B"}\
]
```

TIP

For larger datasets, you can more efficiently pass data using an [Apache Arrow](https://arrow.apache.org/docs/js/) table as a columnar data representation. [^0.6.16](https://github.com/observablehq/plot/releases/tag/v0.6.16 "added in v0.6.16")

Then you can pass the data to the line mark, and extract named columns from the data for the desired options:

0123456789↑ value0.00.51.01.52.02.53.0hour → [Fork](https://observablehq.com/@observablehq/plot-accessors "Open on Observable")

js

```
Plot.lineY(linedata, {x: "hour", y: "value", stroke: "sensor"}).plot()
```

Another common way to extract a column from tabular data is an accessor function. This function is invoked for each element in the data (each row), and returns the corresponding observed value, as with [_array_.map](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/map).

01234567890.00.51.01.52.02.53.0 [Fork](https://observablehq.com/@observablehq/plot-accessors "Open on Observable")

js

```
Plot.lineY(linedata, {
  x: (d) => d.hour,
  y: (d) => d.value,
  stroke: (d) => d.sensor
}).plot()
```

For greater efficiency, Plot also supports columnar data: you can use an [Apache Arrow](https://arrow.apache.org/docs/js/) table as data instead of an array of objects. [^0.6.16](https://github.com/observablehq/plot/releases/tag/v0.6.16 "added in v0.6.16") You can even pass parallel arrays of values, or Apache Arrow vectors, to each channel.

js

```
Plot.lineY({length: linedata.length}, {
  x: linedata.map((d) => d.hour),
  y: linedata.map((d) => d.value),
  stroke: linedata.map((d) => d.sensor)
}).plot()
```

TIP

Note that when accessor functions or parallel arrays are used instead of field names, automatic axis labels ( _hour_ and _value_) are lost. These can be restored using the **label** option on the _x_ and _y_ scales.

## Marks imply data types [​](https://observablehq.com/plot/features/marks\#marks-imply-data-types)

Data comes in different types: quantitative (or temporal) values can be subtracted, ordinal values can be ordered, and nominal (or categorical) values can only be the same or different.

INFO

Because nominal values often need some arbitrary order for display purposes — often alphabetical — Plot uses the term _ordinal_ to refer to both ordinal and nominal data.

Some marks work with any type of data, while other marks have certain requirements or assumptions of data. For example, a line should only be used when both _x_ and _y_ are quantitative or temporal, and when the data is in a meaningful order (such as chronological). This is because the line mark will interpolate between adjacent points to draw line segments. If _x_ or _y_ is nominal — say the names of countries — it doesn’t make sense to use a line because there is no half-way point between two nominal values.

dodon’tpleasethis0.00.51.01.52.02.53.0 [Fork](https://observablehq.com/@observablehq/plot-dont-do-this "Open on Observable")

js

```
Plot.lineY(["please", "don’t", "do", "this"]).plot() // 🌶️
```

WARNING

While Plot aspires to give good defaults and helpful warnings, Plot won’t prevent you from creating a meaningless chart. _Only you_ can prevent bogus charts!

In particular, beware the simple “bar”! A bar mark is used for a bar chart, but a rect mark is needed for a histogram. Plot has four different mark types for drawing rectangles:

- use [rect](https://observablehq.com/plot/marks/rect) when both _x_ and _y_ are quantitative
- use [barX](https://observablehq.com/plot/marks/bar) when _x_ is quantitative and _y_ is ordinal
- use [barY](https://observablehq.com/plot/marks/bar) when _x_ is ordinal and _y_ is quantitative
- use [cell](https://observablehq.com/plot/marks/cell) when both _x_ and _y_ are ordinal

Plot encourages you to think about data types as you visualize because data types often imply semantics. For example, do you notice anything strange about the bar chart below?

01,0002,0003,0004,0005,0006,0007,000↑ population201420152016201720192020year [Fork](https://observablehq.com/@observablehq/plot-the-missing-bar "Open on Observable")

js

```
Plot
  .barY(timeseries, {x: "year", y: "population"}) // 🌶️
  .plot({x: {tickFormat: ""}})
```

Here’s the underlying data:

js

```
timeseries = [\
  {year: 2014, population: 7295.290765},\
  {year: 2015, population: 7379.797139},\
  {year: 2016, population: 7464.022049},\
  {year: 2017, population: 7547.858925},\
  {year: 2019, population: 7713.468100},\
  {year: 2020, population: 7794.798739}\
]
```

The data is missing the population for the year 2018! Because the barY mark implies an ordinal _x_ scale, the gap is hidden. Switching to the rectY mark (with the **interval** option to indicate that these are annual observations) reveals the missing data.

01,0002,0003,0004,0005,0006,0007,000↑ population20142015201620172018201920202021year → [Fork](https://observablehq.com/@observablehq/plot-the-missing-bar "Open on Observable")

js

```
Plot
  .rectY(timeseries, {x: "year", y: "population", interval: 1})
  .plot({x: {tickFormat: ""}})
```

Alternatively, you can keep the barY mark and apply the **interval** option to the _x_ scale.

01,0002,0003,0004,0005,0006,0007,000↑ population2014201520162017201820192020year → [Fork](https://observablehq.com/@observablehq/plot-the-missing-bar "Open on Observable")

js

```
Plot
  .barY(timeseries, {x: "year", y: "population"})
  .plot({x: {tickFormat: "", interval: 1}})
```

## Marks have options [​](https://observablehq.com/plot/features/marks\#marks-have-options)

When constructing a mark, you can specify options to change the mark’s appearance. These options are passed as a second argument to the mark constructor. (The first argument is the required data.) For example, if you want filled dots instead of stroked ones, pass the desired color to the **fill** option:

−0.6−0.4−0.20.00.20.40.60.81.01.2↑ Anomaly1880190019201940196019802000 [Fork](https://observablehq.com/@observablehq/plot-marks-have-options "Open on Observable")

js

```
Plot.dot(gistemp, {x: "Date", y: "Anomaly", fill: "red"}).plot()
```

As the name suggests, options are generally optional; Plot tries to provide good defaults for whatever you don’t specify. Plot even has [shorthand](https://observablehq.com/plot/features/shorthand) for various common forms of data. Below, we extract an array of numbers from the `gistemp` dataset, and use the line mark shorthand to set _x_ = index and _y_ = identity.

−0.6−0.4−0.20.00.20.40.60.81.01.202004006008001,0001,2001,4001,600 [Fork](https://observablehq.com/@observablehq/plot-marks-have-options "Open on Observable")

js

```
Plot.lineY(gistemp.map((d) => d.Anomaly)).plot()
```

Some marks even provide default [transforms](https://observablehq.com/plot/features/transforms), say for [stacking](https://observablehq.com/plot/transforms/stack)!

TIP

Because Plot strives to be concise, there are many default behaviors, some of which can be subtle. If Plot isn’t doing what you expect, try disabling the defaults by specifying options explicitly.

In addition to the standard options such as **fill** and **stroke** that are supported by all mark types, each mark type can support options unique to that type. For example, the dot mark takes a **symbol** option so you can draw things other than circles. See the documentation for each mark type to see what it supports.

## Marks have channels [​](https://observablehq.com/plot/features/marks\#marks-have-channels)

Channels are mark options that can be used to encode data. These options allow the value to vary with the data, such as a different position or color for each dot. To use a channel, supply it with a column of data, typically as:

- a field (column) name,
- an accessor function, or
- an array of values of the same length and order as the data.

Not all mark options can be expressed as channels. For example, **stroke** can be a channel but **strokeDasharray** cannot. This is mostly a pragmatic limitation — it would be harder to implement Plot if every option were expressible as a channel — but it also serves to guide you towards options that are intended for encoding data.

TIP

To vary the definition of a constant option with data, create multiple marks with your different constant options, and then filter the data for each mark to achieve the desired result.

Some options can be either a channel or a constant depending on the provided value. For example, if you set the **fill** option to _purple_, Plot interprets it as a literal color.

20142015201620172019202001,0002,0003,0004,0005,0006,0007,000population → [Fork](https://observablehq.com/@observablehq/plot-marks-have-channels "Open on Observable")

js

```
Plot
  .barX(timeseries, {x: "population", y: "year", fill: "purple"})
  .plot({y: {label: null, tickFormat: ""}})
```

Whereas if the **fill** option is a string but _not_ a valid CSS color, Plot assumes you mean the corresponding column of the data and interprets it as a channel.

20142015201620172019202001,0002,0003,0004,0005,0006,0007,000population → [Fork](https://observablehq.com/@observablehq/plot-marks-have-channels "Open on Observable")

js

```
Plot
  .barX(timeseries, {x: "population", y: "year", fill: "year"})
  .plot({y: {label: null, tickFormat: ""}})
```

If the **fill** option is a function, it is interpreted as a channel.

20142015201620172019202001,0002,0003,0004,0005,0006,0007,000population → [Fork](https://observablehq.com/@observablehq/plot-marks-have-channels "Open on Observable")

js

```
Plot
  .barX(timeseries, {x: "population", y: "year", fill: (d) => d.year})
  .plot({y: {label: null, tickFormat: ""}})
```

Lastly, note that while channels are normally bound to a [scale](https://observablehq.com/plot/features/marks#marks-use-scales), you can bypass the _color_ scale here by supplying literal color values to the **fill** channel.

20142015201620172019202001,0002,0003,0004,0005,0006,0007,000population → [Fork](https://observablehq.com/@observablehq/plot-marks-have-channels "Open on Observable")

js

```
Plot
  .barX(timeseries, {x: "population", y: "year", fill: (d) => d.year & 1 ? "red" : "currentColor"})
  .plot({y: {label: null, tickFormat: ""}})
```

But rather than supplying literal values, it is more semantic to provide abstract values and use scales. In addition to centralizing the encoding definition (if used by multiple marks), it allows Plot to generate a legend.

evenodd

20142015201620172019202001,0002,0003,0004,0005,0006,0007,000population → [Fork](https://observablehq.com/@observablehq/plot-marks-have-channels "Open on Observable")

js

```
Plot
  .barX(timeseries, {x: "population", y: "year", fill: (d) => d.year & 1 ? "odd" : "even"})
  .plot({y: {label: null, tickFormat: ""}, color: {legend: true}})
```

You can then specify the _color_ scale’s **domain** and **range** to control the encoding.

## Mark options [​](https://observablehq.com/plot/features/marks\#mark-options)

Mark constructors take two arguments: **data** and **options**. Together these describe a tabular dataset and how to visualize it. Option values that must be the same for all of a mark’s generated shapes are known as _constants_, whereas option values that may vary across a mark’s generated shapes are known as _channels_. Channels are typically bound to [scales](https://observablehq.com/plot/features/scales) and encode abstract data values, such as time or temperature, as visual values, such as position or color. (Channels can also be used to order ordinal domains; see the [**sort** option](https://observablehq.com/plot/features/scales#sort-mark-option).)

A mark’s data is most commonly an array of objects representing a tabular dataset, such as the result of loading a CSV file, while a mark’s options bind channels (such as _x_ and _y_) to columns in the data (such as _units_ and _fruit_).

js

```
sales = [\
  {units: 10, fruit: "peach"},\
  {units: 20, fruit: "pear"},\
  {units: 40, fruit: "plum"},\
  {units: 30, fruit: "plum"}\
]
```

js

```
Plot.dot(sales, {x: "units", y: "fruit"})
```

While a column name such as `"units"` is the most concise way of specifying channel values, values can also be specified as functions for greater flexibility, say to transform data or derive a new column on the fly. Channel functions are invoked for each datum ( _d_) in the data and return the corresponding channel value. (This is similar to how D3’s [_selection_.attr](https://d3js.org/d3-selection/modifying#selection_attr) accepts functions, though note that Plot channel functions should return abstract values, not visual values.)

js

```
Plot.dot(sales, {x: (d) => d.units * 1000, y: (d) => d.fruit})
```

Plot also supports columnar data for greater efficiency with bigger datasets; for example, data can be specified as any array of the appropriate length (or any iterable or value compatible with [Array.from](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/from)), and then separate arrays of values can be passed as _options_.

js

```
index = [0, 1, 2, 3]
```

js

```
units = [10, 20, 40, 30]
```

js

```
fruits = ["peach", "pear", "plum", "plum"]
```

js

```
Plot.dot(index, {x: units, y: fruits})
```

Channel values can also be specified as numbers for constant values, say for a fixed baseline with an [area](https://observablehq.com/plot/marks/area).

js

```
Plot.area(aapl, {x1: "Date", y1: 0, y2: "Close"})
```

Missing and invalid data are handled specifically for each mark type and channel. In most cases, if the provided channel value for a given datum is null, undefined, or (strictly) NaN, the mark will implicitly filter the datum and not generate a corresponding output. In some cases, such as the radius ( _r_) of a dot, the channel value must additionally be positive. Plot.line and Plot.area will stop the path before any invalid point and start again at the next valid point, thus creating interruptions rather than interpolating between valid points. Titles will only be added if they are non-empty.

All marks support the following style options:

- **fill** \- fill color
- **fillOpacity** \- fill opacity (a number between 0 and 1)
- **stroke** \- stroke color
- **strokeWidth** \- stroke width (in pixels)
- **strokeOpacity** \- stroke opacity (a number between 0 and 1)
- **strokeLinejoin** \- how to join lines ( _bevel_, _miter_, _miter-clip_, or _round_)
- **strokeLinecap** \- how to cap lines ( _butt_, _round_, or _square_)
- **strokeMiterlimit** \- to limit the length of _miter_ joins
- **strokeDasharray** \- a comma-separated list of dash lengths (typically in pixels)
- **strokeDashoffset** \- the [stroke dash offset](https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/stroke-dashoffset) (typically in pixels)
- **opacity** \- object opacity (a number between 0 and 1)
- **mixBlendMode** \- the [blend mode](https://developer.mozilla.org/en-US/docs/Web/CSS/mix-blend-mode) ( _e.g._, _multiply_)
- **imageFilter** \- a CSS [filter](https://developer.mozilla.org/en-US/docs/Web/CSS/filter) ( _e.g._, _blur(5px)_) [^0.6.7](https://github.com/observablehq/plot/releases/tag/v0.6.7 "added in v0.6.7")
- **shapeRendering** \- the [shape-rendering mode](https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/shape-rendering) ( _e.g._, _crispEdges_)
- **paintOrder** \- the [paint order](https://developer.mozilla.org/en-US/docs/Web/CSS/paint-order) ( _e.g._, _stroke_)
- **dx** \- horizontal offset (in pixels; defaults to 0)
- **dy** \- vertical offset (in pixels; defaults to 0)
- **target** \- link target (e.g., “\_blank” for a new window); for use with the **href** channel
- **className** \- the [class attribute](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/class), if any (defaults to null) [^0.6.16](https://github.com/observablehq/plot/releases/tag/v0.6.16 "added in v0.6.16")
- **ariaDescription** \- a textual description of the mark’s contents
- **ariaHidden** \- if true, hide this content from the accessibility tree
- **pointerEvents** \- the [pointer events](https://developer.mozilla.org/en-US/docs/Web/CSS/pointer-events) ( _e.g._, _none_)
- **clip** \- whether and how to clip the mark
- **tip** \- whether to generate an implicit [pointer](https://observablehq.com/plot/interactions/pointer) [tip](https://observablehq.com/plot/marks/tip) [^0.6.7](https://github.com/observablehq/plot/releases/tag/v0.6.7 "added in v0.6.7")

If the **clip** option [Permalink to "clip"](https://observablehq.com/plot/features/marks#clip) is _frame_ (or equivalently true), the mark is clipped to the frame’s dimensions. If the **clip** option is null (or equivalently false), the mark is not clipped. If the **clip** option is _sphere_, the mark will be clipped to the projected sphere ( _e.g._, the front hemisphere when using the orthographic projection); a [geographic projection](https://observablehq.com/plot/features/projections) is required in this case. Lastly if the **clip** option is a GeoJSON object [^0.6.17](https://github.com/observablehq/plot/releases/tag/v0.6.17 "added in v0.6.17"), the mark will be clipped to the projected geometry.

If the **tip** option is true, a [tip mark](https://observablehq.com/plot/marks/tip) with the [pointer transform](https://observablehq.com/plot/interactions/pointer) will be derived from this mark and placed atop all other marks, offering details on demand. If the **tip** option is set to an options object, these options will be passed to the derived tip mark. If the **tip** option (or, if an object, its **pointer** option) is set to _x_, _y_, or _xy_, [pointerX](https://observablehq.com/plot/interactions/pointer#pointerX), [pointerY](https://observablehq.com/plot/interactions/pointer#pointerY), or [pointer](https://observablehq.com/plot/interactions/pointer#pointer) will be used, respectively; otherwise the pointing mode will be chosen automatically. (If the **tip** mark option is truthy, the **title** channel is no longer applied using an SVG title element as this would conflict with the tip mark.)

For all marks except [text](https://observablehq.com/plot/marks/text), the **dx** and **dy** options are rendered as a transform property, possibly including a 0.5px offset on low-density screens.

All marks support the following optional channels:

- **fill** \- a fill color; bound to the _color_ scale
- **fillOpacity** \- a fill opacity; bound to the _opacity_ scale
- **stroke** \- a stroke color; bound to the _color_ scale
- **strokeOpacity** \- a stroke opacity; bound to the _opacity_ scale
- **strokeWidth** \- a stroke width (in pixels)
- **opacity** \- an object opacity; bound to the _opacity_ scale
- **title** \- an accessible, short-text description (a string of text, possibly with newlines)
- **href** \- a URL to link to
- **ariaLabel** \- a short label representing the value in the accessibility tree

The **fill**, **fillOpacity**, **stroke**, **strokeWidth**, **strokeOpacity**, and **opacity** options can be specified as either channels or constants. When the fill or stroke is specified as a function or array, it is interpreted as a channel; when the fill or stroke is specified as a string, it is interpreted as a constant if a valid CSS color and otherwise it is interpreted as a column name for a channel. Similarly when the fill opacity, stroke opacity, object opacity, stroke width, or radius is specified as a number, it is interpreted as a constant; otherwise it is interpreted as a channel.

The scale associated with any channel can be overridden by specifying the channel as an object with a _value_ property specifying the channel values and a _scale_ property specifying the desired scale name or null for an unscaled channel. For example, to force the **stroke** channel to be unscaled, interpreting the associated values as literal color strings:

js

```
Plot.dot(data, {stroke: {value: "fieldName", scale: null}})
```

To instead force the **stroke** channel to be bound to the _color_ scale regardless of the provided values, say:

js

```
Plot.dot(data, {stroke: {value: "fieldName", scale: "color"}})
```

The color channels ( **fill** and **stroke**) are bound to the _color_ scale by default, unless the provided values are all valid CSS color strings or nullish, in which case the values are interpreted literally and unscaled.

In addition to functions of data, arrays, and column names, channel values can be specified as an object with a _transform_ method; this transform method is passed the mark’s array of data and must return the corresponding array of channel values. (Whereas a channel value specified as a function is invoked repeatedly for each element in the mark’s data, similar to _array_.map, the transform method is invoked only once being passed the entire array of data.) For example, to pass the mark’s data directly to the **x** channel, equivalent to [Plot.identity](https://observablehq.com/plot/features/transforms#identity):

js

```
Plot.dot(numbers, {x: {transform: (data) => data}})
```

The **title**, **href**, and **ariaLabel** options can _only_ be specified as channels. When these options are specified as a string, the string refers to the name of a column in the mark’s associated data. If you’d like every instance of a particular mark to have the same value, specify the option as a function that returns the desired value, _e.g._`() => "Hello, world!"`.

For marks that support the **frameAnchor** option, it may be specified as one of the four sides ( _top_, _right_, _bottom_, _left_), one of the four corners ( _top-left_, _top-right_, _bottom-right_, _bottom-left_), or the _middle_ of the frame.

All marks support the following [transform](https://observablehq.com/plot/features/transforms) options:

- **filter** \- apply the [filter transform](https://observablehq.com/plot/transforms/filter)
- **sort** \- apply the [sort transform](https://observablehq.com/plot/transforms/sort)
- **reverse** \- apply the [reverse transform](https://observablehq.com/plot/transforms/sort#reverse)
- **transform** \- apply a [custom transform](https://observablehq.com/plot/features/transforms#custom-transforms)
- **initializer** \- apply a [custom initializer](https://observablehq.com/plot/features/transforms#custom-initializers)

The **sort** option, when not specified as a channel value (such as a field name or an accessor function), can also be used to [impute ordinal scale domains](https://observablehq.com/plot/features/scales#sort-mark-option).

### Insets [​](https://observablehq.com/plot/features/marks\#insets)

Rect-like marks support insets: a positive inset moves the respective side in (towards the opposing side), whereas a negative inset moves the respective side out (away from the opposing side). Insets are specified in pixels using the following options:

- **inset** \- shorthand for all four insets
- **insetTop** \- inset the top edge
- **insetRight** \- inset the right edge
- **insetBottom** \- inset the bottom edge
- **insetLeft** \- inset the left edge

Insets default to zero. Insets are commonly used to create a one-pixel gap between adjacent bars in histograms; the [bin transform](https://observablehq.com/plot/transforms/bin) provides default insets. (Note that the [band scale padding](https://observablehq.com/plot/features/scales#position-scale-options) defaults to 0.1 as an alternative to insets.)

### Rounded corners [​](https://observablehq.com/plot/features/marks\#rounded-corners)

Rect-like marks support rounded corners. Each corner (or side) is individually addressable [^0.6.16](https://github.com/observablehq/plot/releases/tag/v0.6.16 "added in v0.6.16") using the following options:

- **r** \- the radius for all four corners
- **rx1** \- the radius for the **x1**- **y1** and **x1**- **y2** corners
- **rx2** \- the radius for the **x2**- **y1** and **x2**- **y2** corners
- **ry1** \- the radius for the **x1**- **y1** and **x2**- **y1** corners
- **ry2** \- the radius for the **x1**- **y2** and **x2**- **y2** corners
- **rx1y1** \- the radius for the **x1**- **y1** corner
- **rx1y2** \- the radius for the **x1**- **y2** corner
- **rx2y1** \- the radius for the **x2**- **y1** corner
- **rx2y2** \- the radius for the **x2**- **y2** corner
- **rx** \- the [_x_-radius](https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/rx) for elliptical corners
- **ry** \- the [_y_-radius](https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/ry) for elliptical corners

Corner radii are specified in either pixels or, for **rx** and **ry**, as percentages (strings) or the keyword _auto_. If the corner radii are too big, they are reduced proportionally.

## marks(... _marks_) [^0.2.0](https://github.com/observablehq/plot/releases/tag/v0.2.0 "added in v0.2.0") [​](https://observablehq.com/plot/features/marks\#marks)

js

```
Plot.marks(
  Plot.ruleY([0]),
  Plot.areaY(data, {fill: color, fillOpacity, ...options}),
  Plot.lineY(data, {stroke: color, ...options})
)
```

A convenience method for composing a mark from a series of other marks. Returns an array of marks that implements the _mark_.plot function. See the [box mark](https://observablehq.com/plot/marks/box) implementation for an example.

Pager

[Previous pagePlots](https://observablehq.com/plot/features/plots)

[Next pageScales](https://observablehq.com/plot/features/scales)

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

---
url: "https://observablehq.com/plot/marks/waffle"
title: "Waffle mark | Plot"
---

# Waffle mark [^0.6.16](https://github.com/observablehq/plot/releases/tag/v0.6.16 "added in v0.6.16") [​](https://observablehq.com/plot/marks/waffle\#waffle-mark)

The **waffle mark** is similar to the [bar mark](https://observablehq.com/plot/marks/bar) in that it displays a quantity (or quantitative extent) for a given category; but unlike a bar, a waffle is subdivided into square cells that allow easier counting. Waffles are useful for reading exact quantities. How quickly can you count the pears 🍐 below? How many more apples 🍎 are there than bananas 🍌?

020406080100120140160180200220240260280300applesbananasorangespears [Fork](https://observablehq.com/@observablehq/plot-simple-waffle "Open on Observable")

js

```
Plot.waffleY([212, 207, 315, 11], {x: ["apples", "bananas", "oranges", "pears"]}).plot({height: 420})
```

The waffle mark is often used with the [group transform](https://observablehq.com/plot/transforms/group) to compute counts. The chart below compares the number of female and male athletes in the 2012 Olympics.

05001,0001,5002,0002,5003,0003,5004,0004,5005,0005,5006,000↑ Frequencyfemalemale [Fork](https://observablehq.com/@observablehq/plot-waffle-group "Open on Observable")

js

```
Plot.waffleY(olympians, Plot.groupX({y: "count"}, {x: "sex"})).plot({x: {label: null}})
```

INFO

Waffles are rendered using SVG patterns, making them more performant than alternatives such as the [dot mark](https://observablehq.com/plot/marks/dot) for rendering many points.

The **unit** option determines the quantity each waffle cell represents; it defaults to one. The unit may be set to a value greater than one for large quantities, or less than one (but greater than zero) for small fractional quantities. Try changing the unit below to see its effect.

Unit:  1 2 5 10 25 50 100

1950195519601965197019751980198519901995200005001,0001,5002,0002,5003,0003,5004,0004,500↑ Frequency [Fork](https://observablehq.com/@observablehq/plot-waffle-unit "Open on Observable")

js

```
Plot.waffleY(olympians, Plot.groupZ({y: "count"}, {fx: "date_of_birth", unit})).plot({fx: {interval: "5 years", label: null}})
```

TIP

Use [faceting](https://observablehq.com/plot/features/facets) as an alternative to supplying an ordinal channel ( _i.e._, _fx_ instead of _x_ for a vertical waffleY). The facet scale’s **interval** option then allows grouping by a quantitative or temporal variable, such as the athlete’s year of birth in the chart below.

While waffles typically represent integer quantities, say to count people or days, they can also encode fractional values with a partial first or last cell. Set the **round** option to true to disable partial cells, or to Math.ceil or Math.floor to round up or down.

Like bars, waffles can be [stacked](https://observablehq.com/plot/transforms/stack), and implicitly apply the stack transform when only a single quantitative channel is supplied.

femalemale

30405060708090100110120130140150160170weight →02004006008001,0001,2001,4001,6001,8002,0002,2002,4002,6002,800↑ Frequency [Fork](https://observablehq.com/@observablehq/plot-stacked-waffles "Open on Observable")

js

```
Plot.waffleY(olympians, Plot.groupZ({y: "count"}, {fill: "sex", sort: "sex", fx: "weight", unit: 10})).plot({fx: {interval: 10}, color: {legend: true}})
```

Waffles can also be used to highlight a proportion of the whole. The chart below recreates a graphic of survey responses from [“Teens in Syria”](https://www.economist.com/graphic-detail/2015/08/19/teens-in-syria) by _The Economist_ (August 19, 2015); positive responses are in orange, while negative responses are in gray. The **rx** option is used to produce circles instead of squares.

## Subdued

### Of 120 surveyed Syrian teenagers:

do no activitiesother than schooldon’t go out afterdarkengage in politicaldiscussion andsocial movements,including onlinewould like to doactivities but areprevented by safetyconcerns74%80%8%61% [Fork](https://observablehq.com/@observablehq/plot-survey-waffle "Open on Observable")

js

```
Plot.plot({
  axis: null,
  label: null,
  height: 260,
  marginTop: 20,
  marginBottom: 70,
  title: "Subdued",
  subtitle: "Of 120 surveyed Syrian teenagers:",
  marks: [\
    Plot.axisFx({lineWidth: 10, anchor: "bottom", dy: 20}),\
    Plot.waffleY({length: 1}, {y: 120, fillOpacity: 0.4, rx: "100%"}),\
    Plot.waffleY(survey, {fx: "question", y: "yes", rx: "100%", fill: "orange"}),\
    Plot.text(survey, {fx: "question", text: (d) => (d.yes / 120).toLocaleString("en-US", {style: "percent"}), frameAnchor: "bottom", lineAnchor: "top", dy: 6, fill: "orange", fontSize: 24, fontWeight: "bold"})\
  ]
})
```

The waffle mark comes in two orientations: waffleY extends vertically↑, while waffleX extends horizontally→. The waffle mark automatically determines the appropriate number of cells per row or per column (depending on orientation) such that the cells are square, don’t overlap, and are consistent with position scales.

Apples:512

apples050100150200250300350400450500

js

```
Plot.waffleX([apples], {y: ["apples"]}).plot({height: 240})
```

INFO

The number of rows in the waffle above is guaranteed to be an integer, but it might not be a multiple or factor of the _x_-axis tick interval. For example, the waffle might have 15 rows while the _x_-axis shows ticks every 100 units.

TIP

To set the number of rows (or columns) directly, use the **multiple** option, though note that manually setting the multiple may result in non-square cells if there isn’t enough room. Alternatively, you can bias the automatic multiple while preserving square cells by setting the **padding** option on the corresponding band scale: padding defaults to 0.1; a higher value may produce more rows, while a lower (or zero) value may produce fewer rows.

## Waffle options [​](https://observablehq.com/plot/marks/waffle\#waffle-options)

For required channels, see the [bar mark](https://observablehq.com/plot/marks/bar). The waffle mark supports the [standard mark options](https://observablehq.com/plot/features/marks), including [insets](https://observablehq.com/plot/features/marks#insets) and [rounded corners](https://observablehq.com/plot/features/marks#rounded-corners). The **stroke** defaults to _none_. The **fill** defaults to _currentColor_ if the stroke is _none_, and to _none_ otherwise.

The waffle mark supports a few additional options to control the rendering of cells:

- **unit** \- the quantity each cell represents; defaults to 1
- **multiple** \- the number of cells per row (or column); defaults to undefined
- **gap** \- the separation between adjacent cells, in pixels; defaults to 1
- **round** \- whether to round values to avoid partial cells; defaults to false

If **multiple** is undefined (the default), the waffle mark will use as many cells per row (or column) that fits within the available bandwidth while ensuring that the cells are square, or one cell per row if square cells are not possible. You can change the rounding behavior by specifying **round** as a function, such as Math.floor or Math.ceil; true is equivalent to Math.round.

## waffleX( _data_, _options_) [​](https://observablehq.com/plot/marks/waffle\#waffleX)

js

```
Plot.waffleX(olympians, Plot.groupY({x: "count"}, {y: "sport"}))
```

Returns a new horizontal→ waffle with the given _data_ and _options_. The following channels are required:

- **x1** \- the starting horizontal position; bound to the _x_ scale
- **x2** \- the ending horizontal position; bound to the _x_ scale

The following optional channels are supported:

- **y** \- the vertical position; bound to the _y_ scale, which must be _band_

If neither the **x1** nor **x2** option is specified, the **x** option may be specified as shorthand to apply an implicit [stackX transform](https://observablehq.com/plot/transforms/stack); this is the typical configuration for a horizontal waffle chart with columns aligned at _x_ = 0\. If the **x** option is not specified, it defaults to [identity](https://observablehq.com/plot/features/transforms#identity). If _options_ is undefined, then it defaults to **x2** as identity and **y** as the zero-based index \[0, 1, 2, …\]; this allows an array of numbers to be passed to waffleX to make a quick sequential waffle chart. If the **y** channel is not specified, the column will span the full vertical extent of the plot (or facet).

If an **interval** is specified, such as d3.utcDay, **x1** and **x2** can be derived from **x**: _interval_.floor( _x_) is invoked for each _x_ to produce _x1_, and _interval_.offset( _x1_) is invoked for each _x1_ to produce _x2_. If the interval is specified as a number _n_, _x1_ and _x2_ are taken as the two consecutive multiples of _n_ that bracket _x_. Named UTC intervals such as _day_ are also supported; see [scale options](https://observablehq.com/plot/features/scales#scale-options).

## waffleY( _data_, _options_) [​](https://observablehq.com/plot/marks/waffle\#waffleY)

js

```
Plot.waffleY(olympians, Plot.groupX({y: "count"}, {x: "sport"}))
```

Returns a new vertical↑ waffle with the given _data_ and _options_. The following channels are required:

- **y1** \- the starting vertical position; bound to the _y_ scale
- **y2** \- the ending vertical position; bound to the _y_ scale

The following optional channels are supported:

- **x** \- the horizontal position; bound to the _x_ scale, which must be _band_

If neither the **y1** nor **y2** option is specified, the **y** option may be specified as shorthand to apply an implicit [stackY transform](https://observablehq.com/plot/transforms/stack); this is the typical configuration for a vertical waffle chart with columns aligned at _y_ = 0\. If the **y** option is not specified, it defaults to [identity](https://observablehq.com/plot/features/transforms#identity). If _options_ is undefined, then it defaults to **y2** as identity and **x** as the zero-based index \[0, 1, 2, …\]; this allows an array of numbers to be passed to waffleY to make a quick sequential waffle chart. If the **x** channel is not specified, the column will span the full horizontal extent of the plot (or facet).

If an **interval** is specified, such as d3.utcDay, **y1** and **y2** can be derived from **y**: _interval_.floor( _y_) is invoked for each _y_ to produce _y1_, and _interval_.offset( _y1_) is invoked for each _y1_ to produce _y2_. If the interval is specified as a number _n_, _y1_ and _y2_ are taken as the two consecutive multiples of _n_ that bracket _y_. Named UTC intervals such as _day_ are also supported; see [scale options](https://observablehq.com/plot/features/scales#scale-options).

Pager

[Previous pageVector](https://observablehq.com/plot/marks/vector)

[Next pageBin](https://observablehq.com/plot/transforms/bin)

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

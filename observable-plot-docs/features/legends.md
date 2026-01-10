---
url: "https://observablehq.com/plot/features/legends"
title: "Legends | Plot"
---

# Legends [^0.3.0](https://github.com/observablehq/plot/releases/tag/v0.3.0 "added in v0.3.0") [​](https://observablehq.com/plot/features/legends\#legends)

Plot can generate **legends** for _color_, _opacity_, and _symbol_ [scales](https://observablehq.com/plot/features/scales). For example, the scatterplot below of body measurements of Olympic athletes includes a legend for its _color_ scale, allowing the meaning of color to be interpreted by the reader. (The axes similarly document the meaning of the _x_ and _y_ position scales.)

femalemale

1.31.41.51.61.71.81.92.02.12.2↑ height406080100120140160weight → [Fork](https://observablehq.com/@observablehq/plot-olympians-scatterplot "Open on Observable")

js

```
Plot.plot({
  color: {legend: true},
  marks: [\
    Plot.dot(olympians, {x: "weight", y: "height", stroke: "sex"})\
  ]
})
```

The legend above is a _swatches_ legend because the _color_ scale is _ordinal_ (with a _categorical_ scheme). When the _color_ scale is continuous, a _ramp_ legend with a smooth gradient is generated instead. The plot below of global average surface temperature ( [GISTEMP](https://data.giss.nasa.gov/gistemp/)) uses a _diverging_ _color_ scale to indicate the deviation from the 1951–1980 average in degrees Celsius.

−101Anomaly−0.6−0.4−0.20.00.20.40.60.81.01.2↑ Anomaly1880190019201940196019802000 [Fork](https://observablehq.com/@observablehq/plot-diverging-color-scatterplot "Open on Observable")

js

```
Plot.plot({
  color: {
    scheme: "BuRd",
    legend: true
  },
  marks: [\
    Plot.ruleY([0]),\
    Plot.dot(gistemp, {x: "Date", y: "Anomaly", stroke: "Anomaly"})\
  ]
})
```

When an ordinal _color_ scale is used redundantly with a _symbol_ scale, the _symbol_ legend will incorporate the color encoding. This is more accessible than using color alone, particularly for readers with color vision deficiency.

AdelieChinstrapGentoo

175180185190195200205210215220225230↑ Flipper length (mm)3,0003,5004,0004,5005,0005,5006,000Body mass (g) → [Fork](https://observablehq.com/@observablehq/plot-symbol-channel "Open on Observable")

js

```
Plot.plot({
  grid: true,
  x: {label: "Body mass (g)"},
  y: {label: "Flipper length (mm)"},
  symbol: {legend: true},
  marks: [\
    Plot.dot(penguins, {x: "body_mass_g", y: "flipper_length_mm", stroke: "species", symbol: "species"})\
  ]
})
```

Plot does not yet generate legends for the _r_ (radius) scale or the _length_ scale. If you are interested in this feature, please upvote [#236](https://github.com/observablehq/plot/issues/236). In the meantime, you can implement a legend using marks as demonstrated in the [spike map](https://observablehq.com/@observablehq/plot-spike) example.

## Legend options [​](https://observablehq.com/plot/features/legends\#legend-options)

If the **legend** [scale option](https://observablehq.com/plot/features/scales#scale-options) is true, the default legend will be produced for the scale; otherwise, the meaning of the **legend** option depends on the scale: for quantitative color scales, it defaults to _ramp_ but may be set to _swatches_ for a discrete scale (most commonly for _threshold_ color scales); for _ordinal_ _color_ scales and _symbol_ scales, only the _swatches_ value is supported. If the \* _legend_ scale option is undefined, it will be inherited from the top-level **legend** plot option. [prerelease](https://github.com/observablehq/plot/pull/2249 "added in #2249")

Categorical and ordinal color legends are rendered as swatches, unless the **legend** option is set to _ramp_. The swatches can be configured with the following options:

- **tickFormat** \- a format function for the labels
- **swatchSize** \- the size of the swatch (if square)
- **swatchWidth** \- the swatches’ width
- **swatchHeight** \- the swatches’ height
- **columns** \- the number of swatches per row
- **marginLeft** \- the legend’s left margin
- **className** \- a class name, that defaults to a randomly generated string scoping the styles
- **opacity** \- the swatch fill opacity [^0.6.5](https://github.com/observablehq/plot/releases/tag/v0.6.5 "added in v0.6.5")
- **width** \- the legend’s width (in pixels)

Symbol legends are rendered as swatches and support the options above in addition to the following options:

- **fill** \- the symbol fill color
- **fillOpacity** \- the symbol fill opacity; defaults to 1
- **stroke** \- the symbol stroke color
- **strokeOpacity** \- the symbol stroke opacity; defaults to 1
- **strokeWidth** \- the symbol stroke width; defaults to 1.5
- **r** \- the symbol radius; defaults to 4.5 pixels

The **fill** and **stroke** symbol legend options can be specified as “color” to apply the color scale when the symbol scale is a redundant encoding. The **fill** defaults to none. The **stroke** defaults to currentColor if the fill is none, and to none otherwise. The **fill** and **stroke** options may also be inherited from the corresponding options on an associated dot mark.

Continuous color legends are rendered as a ramp, and can be configured with the following options:

- **label** \- the scale’s label
- **ticks** \- the desired number of ticks, or an array of tick values
- **tickFormat** \- a format function for the legend’s ticks
- **tickSize** \- the tick size
- **round** \- if true (default), round tick positions to pixels
- **width** \- the legend’s width
- **height** \- the legend’s height
- **marginTop** \- the legend’s top margin
- **marginRight** \- the legend’s right margin
- **marginBottom** \- the legend’s bottom margin
- **marginLeft** \- the legend’s left margin
- **opacity** \- the ramp’s fill opacity

The **style** legend option allows custom styles to override Plot’s defaults; it has the same behavior as in Plot’s top-level [plot options](https://observablehq.com/plot/features/plots). The **className** option is suffixed with _-ramp_ or _-swatches_, reflecting the **legend** type.

## legend( _options_) [​](https://observablehq.com/plot/features/legends\#legend)

Renders a standalone legend for the scale defined by the given _options_ object, returning a SVG or HTML figure element. This element can then be inserted into the page as described in the [getting started guide](https://observablehq.com/plot/getting-started). The _options_ object must define at least one scale; see [scale options](https://observablehq.com/plot/features/scales) for how to define a scale.

For example, here is a _ramp_ legend of a _linear_ _color_ scale with the default domain of \[0, 1\] and default scheme _turbo_:

0.00.20.40.60.81.0

js

```
Plot.legend({color: {type: "linear"}})
```

The _options_ object may also include any additional legend options described in the previous section. For example, to make the above legend slightly wider:

0.00.20.40.60.81.0

js

```
Plot.legend({width: 320, color: {type: "linear"}})
```

Pager

[Previous pageFacets](https://observablehq.com/plot/features/facets)

[Next pageCurves](https://observablehq.com/plot/features/curves)

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

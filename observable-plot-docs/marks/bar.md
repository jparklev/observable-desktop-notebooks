---
url: "https://observablehq.com/plot/marks/bar"
title: "Bar mark | Plot"
---

# Bar mark [​](https://observablehq.com/plot/marks/bar\#bar-mark)

TIP

The bar mark is a variant of the [rect mark](https://observablehq.com/plot/marks/rect) for use when one dimension is ordinal and the other is quantitative. See also the [cell mark](https://observablehq.com/plot/marks/cell).

The **bar mark** comes in two orientations: [barY](https://observablehq.com/plot/marks/bar#barY) extends vertically↑ as in a vertical bar chart or column chart, while [barX](https://observablehq.com/plot/marks/bar#barX) extends horizontally→. For example, the bar chart below shows the frequency of letters in the English language.

0.000.010.020.030.040.050.060.070.080.090.100.110.12↑ frequencyABCDEFGHIJKLMNOPQRSTUVWXYZletter [Fork](https://observablehq.com/@observablehq/plot-vertical-bars "Open on Observable")

js

```
Plot.barY(alphabet, {x: "letter", y: "frequency"}).plot()
```

Ordinal domains are sorted naturally (alphabetically) by default. Either set the [scale **domain**](https://observablehq.com/plot/features/scales) explicitly to change the order, or use the mark [**sort** option](https://observablehq.com/plot/features/scales#sort-mark-option) to derive the scale domain from a channel. For example, to sort **x** by descending **y**:

0.000.010.020.030.040.050.060.070.080.090.100.110.12↑ frequencyETAOINSHRDLCUMWFGYPBVKJXQZletter [Fork](https://observablehq.com/@observablehq/plot-vertical-bars "Open on Observable")

js

```
Plot.barY(alphabet, {x: "letter", y: "frequency", sort: {x: "-y"}}).plot()
```

There is typically one ordinal value associated with each bar, such as a name (or above, letter), and two quantitative values defining a lower and upper bound; the lower bound is often not specified (as above) because it defaults to zero. For barY, **x** is ordinal and **y1** & **y2** are quantitative, whereas for barX, **y** is ordinal and **x1** & **x2** are quantitative.

Above, since **y** was specified instead of **y1** and **y2**, the bar spans from zero to the given _y_ value: if you only specify a single quantitative value, barY applies an implicit [stackY transform](https://observablehq.com/plot/transforms/stack) and likewise barX implicitly applies stackX. The stacked horizontal bar chart below draws one bar (of unit width in **x**) per penguin, colored and sorted by the penguin’s body mass, and grouped by species along **y**.

3,0004,0005,0006,000body\_mass\_gAdelieChinstrapGentoo020406080100120140Frequency → [Fork](https://observablehq.com/@observablehq/plot-stacked-unit-chart "Open on Observable")

js

```
Plot.plot({
  marginLeft: 60,
  x: {label: "Frequency"},
  y: {label: null},
  color: {legend: true},
  marks: [\
    Plot.barX(penguins, {y: "species", x: 1, inset: 0.5, fill: "body_mass_g", sort: "body_mass_g"}),\
    Plot.ruleX([0])\
  ]
})
```

TIP

The [group transform](https://observablehq.com/plot/transforms/group) with the _count_ reducer could be used to produce one bar per species.

You can opt-out of the implicit stack transform by specifying the bar’s extent with two quantitative values: **x1** and **x2** for barX, or **y1** and **y2** for barY. For example, here is a historical timeline of civilizations, where each has a beginning and an end.

3000 BC2000 BC1000 BC0 AD1000 AD2000 ADAegean civilizationAge of pre-colonial civilization (Christian, Islamic, and traditional kingdoms)Age of Turkic empiresAge of united CaliphateAncient Andean regionAncient ChinaAncient Steppe empiresBritish IndiaClassic age of MesoamericaColonial AfricaColonial United StatesEarly Islamic periodEarly modern ChinaEarly modern EuropeEarly Nubian civilizationEgyptian civilizationFirst Persian EmpireFormative age of MesoamericaFormative Japan (age of Yamato rule)Formative USFractured Islamic worldGreat power USGreek ageHeian ageImperial JapanIndian kingdom ageIndus civilizationInter-Persian periodKushMedieval Andean regionMedieval ChinaMedieval EuropeMesopotamian civilizationModern AfricaModern EuropeModern IndiaModern JapanMongol EmpireMughal EmpirePeak of AksumPeople's Republic of ChinaPostclassic age of MesoamericaPtolemaic EgyptRepublic of ChinaRoman > Byzantine EgyptRoman EmpireRoman RepublicSecond Persian EmpireShogunateSuperpower USVedic age [Fork](https://observablehq.com/@observablehq/plot-civilizations-timeline "Open on Observable")

js

```
Plot.plot({
  marginLeft: 130,
  axis: null,
  x: {
    axis: "top",
    grid: true,
    tickFormat: (x) => x < 0 ? `${-x} BC` : `${x} AD`
  },
  marks: [\
    Plot.barX(civilizations, {\
      x1: "start",\
      x2: "end",\
      y: "civilization",\
      sort: {y: "x1"}\
    }),\
    Plot.text(civilizations, {\
      x: "start",\
      y: "civilization",\
      text: "civilization",\
      textAnchor: "end",\
      dx: -3\
    })\
  ]
})
```

TIP

This uses a [text mark](https://observablehq.com/plot/marks/text) to label the bars directly instead of a _y_ axis. It also uses a custom tick format for the _x_ axis to show the calendar era.

For a diverging bar chart, simply specify a negative value. The chart below shows change in population from 2010 to 2019. States whose population increased are green, while states whose population decreased are pink. (Puerto Rico’s population declined sharply after hurricanes Maria and Irma.)

−10−5+0+5+10+15← decrease · Change in population, 2010–2019 (%) · increase →Puerto RicoWest VirginiaIllinoisVermontConnecticutMississippiNew YorkRhode IslandPennsylvaniaNew JerseyMichiganMaineOhioNew MexicoKansasWisconsinMissouriLouisianaAlabamaWyomingKentuckyAlaskaNew HampshireArkansasIowaIndianaHawaiiMarylandOklahomaNebraskaCaliforniaMassachusettsMinnesotaVirginiaTennesseeMontanaDelawareSouth DakotaGeorgiaNorth CarolinaOregonSouth CarolinaWashingtonNorth DakotaArizonaIdahoNevadaFloridaColoradoTexasUtahDistrict of Columbia [Fork](https://observablehq.com/@observablehq/plot-state-population-change "Open on Observable")

js

```
Plot.plot({
  label: null,
  x: {
    axis: "top",
    label: "← decrease · Change in population, 2010–2019 (%) · increase →",
    labelAnchor: "center",
    tickFormat: "+",
    percent: true
  },
  color: {
    scheme: "PiYg",
    type: "ordinal"
  },
  marks: [\
    Plot.barX(statepop, {y: "State", x: (d) => (d[2019] - d[2010]) / d[2010], fill: (d) => Math.sign(d[2019] - d[2010]), sort: {y: "x"}}),\
    Plot.gridX({stroke: "white", strokeOpacity: 0.5}),\
    Plot.axisY({x: 0}),\
    Plot.ruleX([0])\
  ]
})
```

TIP

The **percent** scale option is useful for showing percentages; it applies a [scale transform](https://observablehq.com/plot/features/scales#scale-transforms) that multiplies associated channel values by 100.

When ordinal data is regular, such as the yearly observations of the time-series bar chart of world population below, use the **interval** option to enforce uniformity and show gaps for missing data. It can be set to a named interval such as _hour_ or _day_, a number for numeric intervals, a [d3-time interval](https://d3js.org/d3-time#_interval), or a custom implementation.

Use interval:

01,0002,0003,0004,0005,0006,0007,000↑ population2014201520162017201820192020year → [Fork](https://observablehq.com/@observablehq/plot-ordinal-scale-interval "Open on Observable")

js

```
Plot
  .barY(timeseries, {x: "year", y: "population"})
  .plot({x: {tickFormat: "", interval: checked ? 1 : undefined}})
```

TIP

You can also make a time-series bar chart with a [rect mark](https://observablehq.com/plot/marks/rect), possibly with the [bin transform](https://observablehq.com/plot/transforms/bin) to bin observations at regular intervals.

A bar’s ordinal dimension is optional; if missing, the bar spans the chart along this dimension. Such bars typically also have a color encoding. For example, here are [warming stripes](https://showyourstripes.info/) showing the increase in average temperature globally over the last 172 years.

186018801900192019401960198020002020year → [Fork](https://observablehq.com/@observablehq/plot-warming-stripes-2 "Open on Observable")

js

```
Plot.plot({
  x: {round: true, tickFormat: "d"},
  color: {scheme: "BuRd"},
  marks: [\
    Plot.barX(hadcrut, {\
      x: "year",\
      fill: "anomaly",\
      interval: 1, // annual observations\
      inset: 0 // no gaps\
    })\
  ]
})
```

With the [stack transform](https://observablehq.com/plot/transforms/stack), a one-dimensional bar can show the proportions of each value relative to the whole, as a compact alternative to a pie or donut chart.

0102030405060708090100frequency (%) →ETAOINSHRDLCUMWFGYPBVKJXQZ [Fork](https://observablehq.com/@observablehq/plot-stacked-percentages "Open on Observable")

js

```
Plot.plot({
  x: {percent: true},
  marks: [\
    Plot.barX(alphabet, Plot.stackX({x: "frequency", fillOpacity: 0.3, inset: 0.5})),\
    Plot.textX(alphabet, Plot.stackX({x: "frequency", text: "letter", inset: 0.5})),\
    Plot.ruleX([0, 1])\
  ]
})
```

TIP

Although barX applies an implicit stackX transform, [textX](https://observablehq.com/plot/marks/text) does not; this example uses an explicit stackX transform in both cases for clarity.

For a grouped bar chart, use [faceting](https://observablehq.com/plot/features/facets). The chart below uses **fy** to partition the bar chart of penguins by island.

BiscoeDreamTorgersenFEMALEMALEFEMALEMALEFEMALEMALE01020304050607080Frequency → [Fork](https://observablehq.com/@observablehq/plot-grouped-unit-chart "Open on Observable")

js

```
Plot.plot({
  marginLeft: 60,
  marginRight: 60,
  label: null,
  x: {label: "Frequency"},
  y: {padding: 0},
  marks: [\
    Plot.barX(penguins, {fy: "island", y: "sex", x: 1, inset: 0.5}),\
    Plot.ruleX([0])\
  ]
})
```

## Bar options [​](https://observablehq.com/plot/marks/bar\#bar-options)

For required channels, see [barX](https://observablehq.com/plot/marks/bar#barX) and [barY](https://observablehq.com/plot/marks/bar#barY). The bar mark supports the [standard mark options](https://observablehq.com/plot/features/marks), including [insets](https://observablehq.com/plot/features/marks#insets) and [rounded corners](https://observablehq.com/plot/features/marks#rounded-corners). The **stroke** defaults to _none_. The **fill** defaults to _currentColor_ if the stroke is _none_, and to _none_ otherwise.

## barX( _data_, _options_) [​](https://observablehq.com/plot/marks/bar\#barX)

js

```
Plot.barX(alphabet, {y: "letter", x: "frequency"})
```

Returns a new horizontal→ bar with the given _data_ and _options_. The following channels are required:

- **x1** \- the starting horizontal position; bound to the _x_ scale
- **x2** \- the ending horizontal position; bound to the _x_ scale

The following optional channels are supported:

- **y** \- the vertical position; bound to the _y_ scale, which must be _band_

If neither the **x1** nor **x2** option is specified, the **x** option may be specified as shorthand to apply an implicit [stackX transform](https://observablehq.com/plot/transforms/stack); this is the typical configuration for a horizontal bar chart with bars aligned at _x_ = 0\. If the **x** option is not specified, it defaults to [identity](https://observablehq.com/plot/features/transforms#identity). If _options_ is undefined, then it defaults to **x2** as identity and **y** as the zero-based index \[0, 1, 2, …\]; this allows an array of numbers to be passed to barX to make a quick sequential bar chart. If the **y** channel is not specified, the bar will span the full vertical extent of the plot (or facet).

If an **interval** is specified, such as d3.utcDay, **x1** and **x2** can be derived from **x**: _interval_.floor( _x_) is invoked for each _x_ to produce _x1_, and _interval_.offset( _x1_) is invoked for each _x1_ to produce _x2_. If the interval is specified as a number _n_, _x1_ and _x2_ are taken as the two consecutive multiples of _n_ that bracket _x_. Named UTC intervals such as _day_ are also supported; see [scale options](https://observablehq.com/plot/features/scales#scale-options).

## barY( _data_, _options_) [​](https://observablehq.com/plot/marks/bar\#barY)

js

```
Plot.barY(alphabet, {x: "letter", y: "frequency"})
```

Returns a new vertical↑ bar with the given _data_ and _options_. The following channels are required:

- **y1** \- the starting vertical position; bound to the _y_ scale
- **y2** \- the ending vertical position; bound to the _y_ scale

The following optional channels are supported:

- **x** \- the horizontal position; bound to the _x_ scale, which must be _band_

If neither the **y1** nor **y2** option is specified, the **y** option may be specified as shorthand to apply an implicit [stackY transform](https://observablehq.com/plot/transforms/stack); this is the typical configuration for a vertical bar chart with bars aligned at _y_ = 0\. If the **y** option is not specified, it defaults to [identity](https://observablehq.com/plot/features/transforms#identity). If _options_ is undefined, then it defaults to **y2** as identity and **x** as the zero-based index \[0, 1, 2, …\]; this allows an array of numbers to be passed to barY to make a quick sequential bar chart. If the **x** channel is not specified, the bar will span the full horizontal extent of the plot (or facet).

If an **interval** is specified, such as d3.utcDay, **y1** and **y2** can be derived from **y**: _interval_.floor( _y_) is invoked for each _y_ to produce _y1_, and _interval_.offset( _y1_) is invoked for each _y1_ to produce _y2_. If the interval is specified as a number _n_, _y1_ and _y2_ are taken as the two consecutive multiples of _n_ that bracket _y_. Named UTC intervals such as _day_ are also supported; see [scale options](https://observablehq.com/plot/features/scales#scale-options).

Pager

[Previous pageAxis](https://observablehq.com/plot/marks/axis)

[Next pageBollinger](https://observablehq.com/plot/marks/bollinger)

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

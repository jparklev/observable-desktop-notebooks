---
url: "https://observablehq.com/plot/marks/rect"
title: "Rect mark | Plot"
---

# Rect mark [​](https://observablehq.com/plot/marks/rect\#rect-mark)

The **rect mark** draws axis-aligned rectangles defined by **x1**, **y1**, **x2**, and **y2**. For example, here we display geographic bounding boxes of U.S. counties represented as \[ _x1_, _y1_, _x2_, _y2_\] tuples, where _x1_ & _x2_ are degrees longitude and _y1_ & _y2_ are degrees latitude.

[Fork](https://observablehq.com/@observablehq/plot-county-boxes "Open on Observable")

js

```
Plot.plot({
  projection: "albers-usa",
  marks: [\
    Plot.rect(countyboxes, {\
      x1: "0", // or ([x1]) => x1\
      y1: "1", // or ([, y1]) => y1\
      x2: "2", // or ([,, x2]) => x2\
      y2: "3", // or ([,,, y2]) => y2\
      stroke: "currentColor"\
    })\
  ]
})
```

The rect mark is often used to produce histograms or heatmaps of quantitative data. For example, given some binned observations computed by [d3.bin](https://d3js.org/d3-array/bin), we can produce a basic histogram with [rectY](https://observablehq.com/plot/marks/rect#rectY) as follows:

020406080100120140160180200↑ length−4−3−2−10123 [Fork](https://observablehq.com/@observablehq/plot-rects-and-bins "Open on Observable")

js

```
Plot.rectY(bins, {x1: "x0", x2: "x1", y: "length"}).plot({round: true})
```

js

```
bins = d3.bin()(d3.range(1000).map(d3.randomNormal()))
```

INFO

d3.bin uses _x0_ and _x1_ to represent the lower and upper bound of each bin, whereas the rect mark uses **x1** and **x2**. The _length_ field is the count of values in each bin, which is encoded as **y**.

More commonly, the rect mark is paired with the [bin transform](https://observablehq.com/plot/transforms/bin) to bin quantitative values automatically. As an added bonus, this sets default [inset options](https://observablehq.com/plot/features/marks#mark-options) for a 1px gap separating adjacent rects, improving readability.

020406080100120140160180200↑ Frequency−4−3−2−10123 [Fork](https://observablehq.com/@observablehq/plot-rects-and-bins "Open on Observable")

js

```
Plot.rectY(d3.range(1000).map(d3.randomNormal()), Plot.binX()).plot()
```

Like the [bar mark](https://observablehq.com/plot/marks/bar), the rect mark has two convenience constructors for common orientations: [rectX](https://observablehq.com/plot/marks/rect#rectX) is for horizontal→ rects with an implicit [stackX transform](https://observablehq.com/plot/transforms/stack#stackX), while [rectY](https://observablehq.com/plot/marks/rect#rectY) is for vertical↑ rects with an implicit [stackY transform](https://observablehq.com/plot/transforms/stack#stackY).

femalemale

050100150200250300350400450500550600↑ Frequency406080100120140160weight → [Fork](https://observablehq.com/@observablehq/plot-vertical-histogram "Open on Observable")

js

```
Plot.plot({
  color: {legend: true},
  marks: [\
    Plot.rectY(olympians, Plot.binX({y: "count"}, {x: "weight", fill: "sex"})),\
    Plot.ruleY([0])\
  ]
})
```

For overlapping rects, you can opt-out of the implicit stack transform by specifying either **x1** or **x2** for rectX, and likewise either **y1** or **y2** for rectY.

femalemale

050100150200250300350400↑ Frequency406080100120140160weight → [Fork](https://observablehq.com/@observablehq/plot-overlapping-histogram "Open on Observable")

js

```
Plot.plot({
  round: true,
  color: {legend: true},
  marks: [\
    Plot.rectY(olympians, Plot.binX({y2: "count"}, {x: "weight", fill: "sex", mixBlendMode: "multiply"})),\
    Plot.ruleY([0])\
  ]
})
```

CAUTION

While the **mixBlendMode** option is useful for mitigating occlusion, it can be slow to render if there are many elements. More than two overlapping histograms may also be hard to read.

The rect mark and bin transform naturally support [faceting](https://observablehq.com/plot/features/facets), too.

femalemalesex01002003004000100200300400↑ Frequency406080100120140160weight → [Fork](https://observablehq.com/@observablehq/plot-overlapping-histogram "Open on Observable")

js

```
Plot.plot({
  marks: [\
    Plot.rectY(olympians, Plot.binX({y: "count"}, {x: "weight", fy: "sex"})),\
    Plot.ruleY([0])\
  ]
})
```

The [rect constructor](https://observablehq.com/plot/marks/rect#rect), again with the [bin transform](https://observablehq.com/plot/transforms/bin), can produce two-dimensional histograms (heatmaps) where density is represented by the **fill** color encoding.

1,0002,0003,0004,0005,0006,0007,0008,0009,00010,00011,00012,00013,00014,00015,00016,00017,00018,00019,000↑ price0.51.01.52.02.53.03.54.04.55.0carat → [Fork](https://observablehq.com/@observablehq/plot-continuous-dimensions-heatmap "Open on Observable")

js

```
Plot.plot({
  height: 640,
  marginLeft: 60,
  color: {
    scheme: "YlGnBu",
    type: "symlog"
  },
  marks: [\
    Plot.rect(diamonds, Plot.bin({fill: "count"}, {x: "carat", y: "price", thresholds: 100}))\
  ]
})
```

TIP

A similar plot can be made with the [dot mark](https://observablehq.com/plot/marks/dot), if you’d prefer a size encoding.

Below we recreate an uncommon [chart by Max Roser](https://ourworldindata.org/poverty-minimum-growth-needed) that visualizes global poverty. Each rect represents a country: _x_ encodes the country’s population, while _y_ encodes the proportion of that population living in poverty; hence area represents the number of people living in poverty. Rects are [stacked](https://observablehq.com/plot/transforms/stack) along _x_ in order of descending _y_.

0102030405060708090100↑ Proportion living on less than $30 per day (%)01,0002,0003,0004,0005,0006,0007,000Population (millions) →Guinea-Bissau
100.0%Mali
100.0%Madagascar
100.0%Somalia
100.0%Niger
100.0%Burundi
100.0%Congo, Democratic Republic of
100.0%Timor-Leste
100.0%South Sudan
100.0%Liberia
100.0%Sierra Leone
100.0%Nigeria
100.0%Togo
99.9%Guinea
99.9%Burkina Faso
99.9%Ethiopia
99.9%Yemen, Republic of
99.9%Malawi
99.9%Papua New Guinea
99.9%Benin
99.9%Tanzania
99.9%Senegal
99.9%Chad
99.9%Uzbekistan
99.8%Bangladesh
99.8%Solomon Islands
99.8%Kenya
99.8%Uganda
99.8%Cote d'Ivoire
99.8%Iraq
99.8%Nepal
99.8%Mauritania
99.8%Rwanda
99.7%Central African Republic
99.7%Kosovo
99.7%Sudan
99.7%India
99.7%Kyrgyz Republic
99.6%Vanuatu
99.6%Pakistan
99.6%Lao People's Democratic Republic
99.6%Angola
99.6%Micronesia, Federated States of
99.6%Gambia, The
99.6%Haiti
99.6%Kiribati
99.6%Zambia
99.5%Syrian Arab Republic
99.5%Lesotho
99.5%Congo, Republic of
99.5%Mozambique
99.4%Tajikistan
99.4%Egypt, Arab Republic of
99.4%Myanmar
99.4%Zimbabwe
99.3%Sao Tome and Principe
99.2%Cameroon
99.2%Albania
99.2%Djibouti
99.2%Philippines
99.1%Moldova
99.1%Algeria
99.1%Ghana
98.9%Comoros
98.9%Georgia
98.9%Indonesia
98.8%Armenia
98.6%Vietnam
98.2%Ukraine
98.2%Kazakhstan
98.1%North Macedonia
98.1%Tuvalu
98.0%Eswatini
98.0%Sri Lanka
98.0%Mongolia
97.9%Gabon
97.6%West Bank and Gaza
97.6%Turkmenistan
97.6%Nauru
97.5%Tunisia
97.3%Fiji
97.2%Romania
97.2%Cabo Verde
97.0%Guatemala
96.9%Samoa
96.8%Honduras
96.8%Tonga
96.7%El Salvador
96.7%Bhutan
96.5%Serbia
96.4%Botswana
96.3%Jordan
96.1%China
96.1%Morocco
96.0%Nicaragua
95.1%Guyana
94.9%Belize
94.9%Mauritius
94.4%Jamaica
94.1%Peru
93.5%Mexico
93.5%Montenegro
93.3%Maldives
93.0%Namibia
92.6%Bolivia
91.9%Ecuador
91.5%Thailand
91.5%Iran, Islamic Republic of
91.2%Colombia
90.8%South Africa
90.8%Dominican Republic
90.4%Poland
89.8%Belarus
89.8%Bulgaria
88.8%St. Lucia
88.5%Paraguay
87.5%Turkey
86.5%Croatia
86.3%Azerbaijan
86.0%Seychelles
85.9%Russian Federation
84.0%Brazil
83.9%Hungary
83.0%Chile
81.4%Bosnia and Herzegovina
81.1%Slovak Republic
80.9%Greece
80.3%Costa Rica
79.1%Panama
78.9%Lebanon
77.9%Latvia
77.3%Lithuania
74.4%Malaysia
71.6%Trinidad and Tobago
71.4%Portugal
69.9%Uruguay
69.9%Czech Republic
65.2%Estonia
61.1%Israel
52.4%Spain
48.6%Slovenia
47.2%Cyprus
43.9%Italy
40.2%Korea, Republic of
36.0%Taiwan, China
35.2%United Kingdom
34.6%Malta
34.3%Ireland
30.9%Japan
30.5%United States
24.2%France
22.5%Germany
22.2%Belgium
22.0%Canada
20.7%Australia
19.7%Austria
19.6%Finland
19.1%Netherlands
17.9%Sweden
16.5%Iceland
15.8%United Arab Emirates
14.9%Luxembourg
14.0%Denmark
13.9%Switzerland
11.9%Norway
6.9% [Fork](https://observablehq.com/@observablehq/plot-cumulative-distribution-of-poverty "Open on Observable")

js

```
Plot.plot({
  x: {label: "Population (millions)"},
  y: {percent: true, label: "Proportion living on less than $30 per day (%)"},
  marks: [\
    Plot.rectY(povcalnet, Plot.stackX({\
      filter: (d) => ["N", "A"].includes(d.CoverageType),\
      x: "ReqYearPopulation",\
      order: "HeadCount",\
      reverse: true,\
      y2: "HeadCount", // y2 to avoid stacking by y\
      title: (d) => `${d.CountryName}\n${(d.HeadCount * 100).toFixed(1)}%`,\
      insetLeft: 0.2,\
      insetRight: 0.2\
    })),\
    Plot.ruleY([0])\
  ]
})
```

The [interval transform](https://observablehq.com/plot/transforms/interval) may be used to convert a single value in **x** or **y** (or both) into an extent. (Unlike the bin transform, the interval transform will produce overlapping rects if multiple points have the same position.) The chart below shows the observed daily maximum temperature in Seattle for the year 2015. The day-in-month and month-in-year numbers are expanded to unit intervals by setting the **interval** option to 1.

JFMAMJJASONDJ51015202530 [Fork](https://observablehq.com/@observablehq/plot-seattle-heatmap-quantitative "Open on Observable")

js

```
Plot.plot({
  aspectRatio: 1,
  y: {ticks: 12, tickFormat: Plot.formatMonth("en", "narrow")},
  marks: [\
    Plot.rect(seattle.filter((d) => d.date.getUTCFullYear() === 2015), {\
      x: (d) => d.date.getUTCDate(),\
      y: (d) => d.date.getUTCMonth(),\
      interval: 1,\
      fill: "temp_max",\
      inset: 0.5\
    })\
  ]
})
```

TIP

A similar chart could be made with the [cell mark](https://observablehq.com/plot/marks/cell) using ordinal _x_ and _y_ scales instead, or with the [dot mark](https://observablehq.com/plot/marks/dot) as a scatterplot.

To round corners, use the **r** option. If the combined corner radii exceed the width or height of the rect, the radii are proportionally reduced to produce a pill shape with circular caps. Try increasing the radii below.

r:4

02004006008001,0001,2001,4001,6001,8002,0002,2002,4002,6002,800↑ Frequency406080100120140160180weight →

js

```
Plot.plot({
  marks: [\
    Plot.rectY(olympians, Plot.binX({y: "count"}, {x: "weight", r, thresholds: 10})),\
    Plot.ruleY([0])\
  ]
})
```

js

```
Plot.plot({
  marks: [\
    Plot.rectY(olympians, Plot.binX({y: "count"}, {x: "weight", r: 4, thresholds: 10})),\
    Plot.ruleY([0])\
  ]
})
```

To round corners on a specific side, use the **rx1**, **ry1**, **rx2**, or **ry2** options. When stacking rounded rects vertically, use a positive **ry2** and a corresponding negative **ry1**; likewise for stacking rounded rects horizontally, use a positive **rx2** and a negative **rx1**. Use the **clip** option to hide the “wings” below zero.

femalemale

050100150200250300350400450500550600↑ Frequency406080100120140160weight → [Fork](https://observablehq.com/@observablehq/plot-rounded-rects "Open on Observable")

js

```
Plot.plot({
  color: {legend: true},
  marks: [\
    Plot.rectY(olympians, Plot.binX({y: "count"}, {x: "weight", fill: "sex", ry2: 4, ry1: -4, clip: "frame"})),\
    Plot.ruleY([0])\
  ]
})
```

You can even round specific corners using the **rx1y1**, **rx2y1**, **rx2y2**, and **rx1y2** options.

femalemale

050100150200250300350400450500550600↑ Frequency406080100120140160weight → [Fork](https://observablehq.com/@observablehq/plot-rounded-rects "Open on Observable")

js

```
Plot.plot({
  color: {legend: true},
  marks: [\
    Plot.rectY(olympians, Plot.binX({y: "count"}, {x: "weight", fill: "sex", rx1y2: 10, rx1y1: -10, clip: "frame"})),\
    Plot.ruleY([0])\
  ]
})
```

## Rect options [​](https://observablehq.com/plot/marks/rect\#rect-options)

The following channels are optional:

- **x1** \- the starting horizontal position; bound to the _x_ scale
- **y1** \- the starting vertical position; bound to the _y_ scale
- **x2** \- the ending horizontal position; bound to the _x_ scale
- **y2** \- the ending vertical position; bound to the _y_ scale

If **x1** is specified but **x2** is not specified, then _x_ must be a _band_ scale; if **y1** is specified but **y2** is not specified, then _y_ must be a _band_ scale.

If an **interval** is specified, such as d3.utcDay, **x1** and **x2** can be derived from **x**: _interval_.floor( _x_) is invoked for each **x** to produce **x1**, and _interval_.offset( _x1_) is invoked for each **x1** to produce **x2**. The same is true for **y**, **y1**, and **y2**, respectively. If the interval is specified as a number _n_, **x1** and **x2** are taken as the two consecutive multiples of _n_ that bracket **x**. Named UTC intervals such as _day_ are also supported; see [scale options](https://observablehq.com/plot/features/scales#scale-options).

The rect mark supports the [standard mark options](https://observablehq.com/plot/features/marks#mark-options), including [insets](https://observablehq.com/plot/features/marks#insets) and [rounded corners](https://observablehq.com/plot/features/marks#rounded-corners). The **stroke** defaults to _none_. The **fill** defaults to _currentColor_ if the stroke is _none_, and to _none_ otherwise.

## rect( _data_, _options_) [​](https://observablehq.com/plot/marks/rect\#rect)

js

```
Plot.rect(olympians, Plot.bin({fill: "count"}, {x: "weight", y: "height"}))
```

Returns a new rect with the given _data_ and _options_.

## rectX( _data_, _options_) [​](https://observablehq.com/plot/marks/rect\#rectX)

js

```
Plot.rectX(olympians, Plot.binY({x: "count"}, {y: "weight"}))
```

Equivalent to [rect](https://observablehq.com/plot/marks/rect#rect), except that if neither the **x1** nor **x2** option is specified, the **x** option may be specified as shorthand to apply an implicit [stackX transform](https://observablehq.com/plot/transforms/stack); this is the typical configuration for a histogram with horizontal→ rects aligned at _x_ = 0\. If the **x** option is not specified, it defaults to the identity function.

## rectY( _data_, _options_) [​](https://observablehq.com/plot/marks/rect\#rectY)

js

```
Plot.rectY(olympians, Plot.binX({y: "count"}, {x: "weight"}))
```

Equivalent to [rect](https://observablehq.com/plot/marks/rect#rect), except that if neither the **y1** nor **y2** option is specified, the **y** option may be specified as shorthand to apply an implicit [stackY transform](https://observablehq.com/plot/transforms/stack); this is the typical configuration for a histogram with vertical↑ rects aligned at _y_ = 0\. If the **y** option is not specified, it defaults to the identity function.

Pager

[Previous pageRaster](https://observablehq.com/plot/marks/raster)

[Next pageRule](https://observablehq.com/plot/marks/rule)

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

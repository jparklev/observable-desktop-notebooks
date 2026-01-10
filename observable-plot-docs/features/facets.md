---
url: "https://observablehq.com/plot/features/facets"
title: "Facets | Plot"
---

# Facets [​](https://observablehq.com/plot/features/facets\#facets)

Faceting partitions data by ordinal or categorical value and then repeats a plot for each partition (each **facet**), producing [small multiples](https://en.wikipedia.org/wiki/Small_multiple) for comparison. Faceting is typically enabled by declaring the horizontal↔︎ facet channel **fx**, the vertical↕︎ facet channel **fy**, or both for two-dimensional faceting.

For example, below we recreate the Trellis display (“reminiscent of garden trelliswork”) of [Becker _et al._](https://hci.stanford.edu/courses/cs448b/papers/becker-trellis-jcgs.pdf) using the dot’s **fy** channel to declare vertical↕︎ facets, showing the yields of several varieties of barley across several sites for the years 1931 and 1932.

WasecaCrookstonMorrisUniversity FarmDuluthGrand RapidssiteTrebiWisconsin No. 38No. 457GlabronPeatlandVelvetNo. 475ManchuriaNo. 462SvansotaTrebiWisconsin No. 38No. 457GlabronPeatlandVelvetNo. 475ManchuriaNo. 462SvansotaTrebiWisconsin No. 38No. 457GlabronPeatlandVelvetNo. 475ManchuriaNo. 462SvansotaTrebiWisconsin No. 38No. 457GlabronPeatlandVelvetNo. 475ManchuriaNo. 462SvansotaTrebiWisconsin No. 38No. 457GlabronPeatlandVelvetNo. 475ManchuriaNo. 462SvansotaTrebiWisconsin No. 38No. 457GlabronPeatlandVelvetNo. 475ManchuriaNo. 462Svansotavariety10203040506070yield → [Fork](https://observablehq.com/@observablehq/plot-trellis "Open on Observable")

js

```
Plot.plot({
  height: 800,
  marginRight: 90,
  marginLeft: 110,
  grid: true,
  x: {nice: true},
  y: {inset: 5},
  color: {type: "categorical"},
  marks: [\
    Plot.frame(),\
    Plot.dot(barley, {\
      x: "yield",\
      y: "variety",\
      fy: "site",\
      stroke: "year",\
      sort: {y: "-x", fy: "-x", reduce: "median"}\
    })\
  ]
})
```

TIP

This plot uses the [**sort** mark option](https://observablehq.com/plot/features/scales#sort-mark-option) to order the _y_ and _fy_ scale domains by descending median yield (the associated _x_ values). Without this option, the domains would be sorted alphabetically.

TIP

Use the [frame mark](https://observablehq.com/plot/marks/frame) for stronger visual separation of facets.

The chart above reveals a likely data collection error: the years appear to be reversed for the Morris site as it is the only site where the yields in 1932 were higher than in 1931. The anomaly in Morris is more obvious if we use directed arrows to show the year-over-year change. The [group transform](https://observablehq.com/plot/transforms/group) groups the observations by site and variety to compute the change.

−20−10+0+10+20Change in yieldWasecaCrookstonUniversity FarmDuluthGrand RapidsMorrissiteTrebiNo. 457Wisconsin No. 38GlabronPeatlandNo. 462VelvetSvansotaManchuriaNo. 475TrebiNo. 457Wisconsin No. 38GlabronPeatlandNo. 462VelvetSvansotaManchuriaNo. 475TrebiNo. 457Wisconsin No. 38GlabronPeatlandNo. 462VelvetSvansotaManchuriaNo. 475TrebiNo. 457Wisconsin No. 38GlabronPeatlandNo. 462VelvetSvansotaManchuriaNo. 475TrebiNo. 457Wisconsin No. 38GlabronPeatlandNo. 462VelvetSvansotaManchuriaNo. 475TrebiNo. 457Wisconsin No. 38GlabronPeatlandNo. 462VelvetSvansotaManchuriaNo. 475variety10203040506070yield → [Fork](https://observablehq.com/@observablehq/plot-trellis-anomaly "Open on Observable")

js

```
Plot.plot({
  height: 800,
  marginLeft: 110,
  grid: true,
  x: {nice: true},
  y: {inset: 5},
  color: {scheme: "spectral", label: "Change in yield", tickFormat: "+f", legend: true},
  facet: {marginRight: 90},
  marks: [\
    Plot.frame(),\
    Plot.arrow(barley, Plot.groupY({\
      x1: "first",\
      x2: "last",\
      stroke: ([x1, x2]) => x2 - x1 // year-over-year difference\
    }, {\
      x: "yield",\
      y: "variety",\
      fy: "site",\
      stroke: "yield",\
      strokeWidth: 2,\
      sort: {y: "-x1", fy: "-x1", reduce: "median"}\
    }))\
  ]
})
```

INFO

Here the sort order has changed slightly: the _y_ and _fy_ domains are sorted by the median **x1** values, which are the yields for 1931.

Faceting requires ordinal or categorical data because there are a discrete number of facets; the associated _fx_ and _fy_ scales are [band scales](https://observablehq.com/plot/features/scales#discrete-scales). Quantitative or temporal data can be made ordinal by binning, say using [Math.floor](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/floor). Or, use the [**interval** scale option](https://observablehq.com/plot/features/scales#scale-transforms) on the _fx_ or _fy_ scale. Below, we produce a [box plot](https://observablehq.com/plot/marks/box) of the weights (in kilograms) of Olympic athletes, faceted by height binned at a 10cm (0.1 meter) interval.

2.22.01.81.61.41.2height →406080100120140160weight → [Fork](https://observablehq.com/@observablehq/plot-olympians-box-plot "Open on Observable")

js

```
Plot.plot({
  fy: {
    grid: true,
    tickFormat: ".1f",
    interval: 0.1, // 10cm
    reverse: true
  },
  marks: [\
    Plot.boxX(olympians.filter((d) => d.height), {x: "weight", fy: "height"})\
  ]
})
```

TIP

If you are interested in automatic faceting for quantitative data, please upvote [#14](https://github.com/observablehq/plot/issues/14).

When both **fx** and **fy** channels are specified, two-dimensional faceting results, as in the faceted scatterplot of penguin culmen measurements below. The horizontal↔︎ facet shows sex (with the rightmost column representing penguins whose _sex_ field is null, indicating missing data), while the vertical↕︎ facet shows species.

AdelieChinstrapGentooFEMALEMALE141618201416182014161820↑ culmen\_depth\_mm4050405040504050culmen\_length\_mm → [Fork](https://observablehq.com/@observablehq/plot-two-dimensional-faceting "Open on Observable")

js

```
Plot.plot({
  grid: true,
  marginRight: 60,
  facet: {label: null},
  marks: [\
    Plot.frame(),\
    Plot.dot(penguins, {\
      x: "culmen_length_mm",\
      y: "culmen_depth_mm",\
      fx: "sex",\
      fy: "species"\
    })\
  ]
})
```

You can mix-and-match faceted and non-faceted marks within the same plot. The non-faceted marks will be repeated across all facets. This is useful for decoration marks, such as a [frame](https://observablehq.com/plot/marks/frame), and also for context: below, the entire population of penguins is repeated in each facet as small gray dots, making it easier to see how each facet compares to the whole.

AdelieChinstrapGentooFEMALEMALE141618201416182014161820↑ culmen\_depth\_mm4050405040504050culmen\_length\_mm → [Fork](https://observablehq.com/@observablehq/plot-non-faceted-marks "Open on Observable")

js

```
Plot.plot({
  grid: true,
  marginRight: 60,
  facet: {label: null},
  marks: [\
    Plot.frame(),\
    Plot.dot(penguins, {\
      x: "culmen_length_mm",\
      y: "culmen_depth_mm",\
      fill: "#aaa",\
      r: 1\
    }),\
    Plot.dot(penguins, {\
      x: "culmen_length_mm",\
      y: "culmen_depth_mm",\
      fx: "sex",\
      fy: "species"\
    })\
  ]
})
```

TIP

Set the [**facet** mark option](https://observablehq.com/plot/features/facets#mark-facet-options) to _exclude_ to draw only the dots _not_ in the current facet.

When there are many facets, facets may be small and hard to read; you may need to increase the plot’s **width** or **height**. Alternatively, you can wrap facets by computing a row and column number as **fy** and **fx**. Below, small multiples of varying unemployment counts across industries are shown in a three-column display.

Wholesale and Retail TradeBusiness servicesGovernmentOtherAgricultureManufacturingConstructionFinanceTransportation and UtilitiesMining and ExtractionLeisure and hospitalityEducation and HealthSelf-employedInformation [Fork](https://observablehq.com/@observablehq/plot-facet-wrap "Open on Observable")

js

```
Plot.plot((() => {
  const n = 3; // number of facet columns
  const keys = Array.from(d3.union(industries.map((d) => d.industry)));
  const index = new Map(keys.map((key, i) => [key, i]));
  const fx = (key) => index.get(key) % n;
  const fy = (key) => Math.floor(index.get(key) / n);
  return {
    height: 300,
    axis: null,
    y: {insetTop: 10},
    fx: {padding: 0.03},
    marks: [\
      Plot.areaY(industries, Plot.normalizeY("extent", {\
        x: "date",\
        y: "unemployed",\
        fx: (d) => fx(d.industry),\
        fy: (d) => fy(d.industry)\
      })),\
      Plot.text(keys, {fx, fy, frameAnchor: "top-left", dx: 6, dy: 6}),\
      Plot.frame()\
    ]
  };
})())
```

TIP

If you are interested in automatic facet wrapping, please upvote [#277](https://github.com/observablehq/plot/issues/277).

INFO

This example uses an [immediately-invoked function expression (IIFE)](https://developer.mozilla.org/en-US/docs/Glossary/IIFE) to declare local variables.

The above chart also demonstrates faceted annotations, using a [text mark](https://observablehq.com/plot/marks/text) to label the facet in lieu of facet axes. Below, we apply a single text annotation to the _Adelie_ facet by setting the **fy** channel to a single-element array parallel to the data.

FEMALEMALEnull

AdelieChinstrapGentooBiscoeDreamTorgersenBiscoeDreamTorgersenBiscoeDreamTorgersen020406080100120Frequency →While Chinstrap and Gentoopenguins were each observed ononly one island, Adelie penguinswere observed on all three islands. [Fork](https://observablehq.com/@observablehq/plot-annotated-facets "Open on Observable")

js

```
Plot.plot({
  marginLeft: 60,
  marginRight: 60,
  grid: true,
  y: {label: null},
  fy: {label: null},
  color: {legend: true},
  marks: [\
    Plot.barX(penguins, Plot.groupY({x: "count"}, {fy: "species", y: "island", fill: "sex"})),\
    Plot.text([`While Chinstrap and Gentoo penguins were each observed on only one island, Adelie penguins were observed on all three islands.`], {\
      fy: ["Adelie"],\
      frameAnchor: "top-right",\
      lineWidth: 18,\
      dx: -6,\
      dy: 6\
    }),\
    Plot.frame()\
  ]
})
```

## Mark facet options [​](https://observablehq.com/plot/features/facets\#mark-facet-options)

Facets can be defined for each mark via the **fx** or **fy** channels. [^0.6.1](https://github.com/observablehq/plot/releases/tag/v0.6.1 "added in v0.6.1") The **fx** and **fy** channels are computed prior to the [mark’s transform](https://observablehq.com/plot/features/transforms), if any ( _i.e._, facet channels are not transformed). Alternatively, the [**facet** plot option](https://observablehq.com/plot/features/facets#plot-facet-options) allows top-level faceting based on data.

Faceting can be explicitly enabled or disabled on a mark with the **facet** option, which accepts the following values:

- _auto_ (default) - automatically determine if this mark should be faceted
- _include_ (or true) - draw the subset of the mark’s data in the current facet
- _exclude_ \- draw the subset of the mark’s data _not_ in the current facet
- _super_ \- draw this mark in a single frame that covers all facets
- null (or false) - repeat this mark’s data across all facets ( _i.e._, no faceting)

When mark-level faceting is used, the default _auto_ setting is equivalent to _include_: the mark will be faceted if either the **fx** or **fy** channel option (or both) is specified. The null or false option will disable faceting, while _exclude_ draws the subset of the mark’s data _not_ in the current facet. When a mark uses _super_ faceting, it is not allowed to use position scales ( _x_, _y_, _fx_, or _fy_); _super_ faceting is intended for decorations, such as labels and legends.

The **facetAnchor** option [Permalink to "facetAnchor"](https://observablehq.com/plot/features/facets#facetAnchor) [^0.6.3](https://github.com/observablehq/plot/releases/tag/v0.6.3 "added in v0.6.3") controls the placement of the mark with respect to the facets. Based on the value, the mark will be displayed on:

- null - non-empty facets
- _top_, _right_, _bottom_, or _left_ \- the given side
- _top-empty_, _right-empty_, _bottom-empty_, or _left-empty_ \- adjacent empty facet or side
- _empty_ \- empty facets

The **facetAnchor** option defaults to null for all marks except axis marks, whose default depends on the axis orientation and associated scale.

When using top-level faceting, if the mark data is parallel to the facet data ( _i.e._, it has the same length and order), but is not strictly equal (`===`), you can enable faceting by specifying the **facet** option to _include_ (or equivalently true). Likewise you can disable faceting by setting the **facet** option to null or false. Finally, the **facet** option supports the _exclude_ option to select all data points that are _not_ part of the current facet, allowing “background” marks for context.

When top-level faceting is used, the default _auto_ setting is equivalent to _include_ when the mark data is strictly equal to the top-level facet data; otherwise it is equivalent to null. When the _include_ or _exclude_ facet mode is chosen, the mark data must be parallel to the top-level facet data: the data must have the same length and order. If the data are not parallel, then the wrong data may be shown in each facet. The default _auto_ therefore requires strict equality (`===`) for safety, and using the facet data as mark data is recommended when using the _exclude_ facet mode. (To construct parallel data safely, consider using [_array_.map](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/map) on the facet data.)

## Plot facet options [​](https://observablehq.com/plot/features/facets\#plot-facet-options)

The **facet** plot option provides addition control over facet position scales and axes:

- **marginTop** \- the top margin
- **marginRight** \- the right margin
- **marginBottom** \- the bottom margin
- **marginLeft** \- the left margin
- **margin** \- shorthand for the four margins
- **grid** \- if true, draw grid lines for each facet
- **label** \- if null, disable default facet axis labels

The **facet** margin options behave largely the same as the margin [plot options](https://observablehq.com/plot/features/plots); the only difference is the positioning of the associated scale label for the _x_ and _y_ scales. Likewise, the **grid** and **label** options have the same meaning as the plot options, except the facet options only apply to the _fx_ and _fy_ scales.

The **facet** plot option is also an alternative to the **fx** and **fy** mark options. It is useful when multiple marks share the same data; the **x** and **y** facet channels are then shared by all marks that use the facet data. (Other marks will be repeated across facets.) For example, we can visualize the famous [Anscombe’s quartet](https://en.wikipedia.org/wiki/Anscombe's_quartet) as a scatterplot with horizontal facets.

1234series4681012↑ y10101010x → [Fork](https://observablehq.com/@observablehq/plot-anscombes-quartet "Open on Observable")

js

```
Plot.plot({
  grid: true,
  aspectRatio: 0.5,
  facet: {data: anscombe, x: "series"},
  marks: [\
    Plot.frame(),\
    Plot.line(anscombe, {x: "x", y: "y"}),\
    Plot.dot(anscombe, {x: "x", y: "y"})\
  ]
})
```

For top-level faceting, these **facet** options determine the facets:

- **data** \- the data to be faceted
- **x** \- the horizontal↔︎ position; bound to the _fx_ scale
- **y** \- the vertical↕︎ position; bound to the _fy_ scale

With top-level faceting, any mark that uses the specified facet data will be faceted by default, whereas marks that use different data will be repeated across all facets. Use the mark **facet** option to change the behavior.

## Facet scales [​](https://observablehq.com/plot/features/facets\#facet-scales)

When faceting, two additional [band scales](https://observablehq.com/plot/features/scales#discrete-scales) may be configured:

- _fx_ \- the horizontal↔︎ position, a _band_ scale
- _fy_ \- the vertical↕︎ position, a _band_ scale

You can adjust the space between facets using the **padding**, **round**, and **align** scale options.

Pager

[Previous pageInteractions](https://observablehq.com/plot/features/interactions)

[Next pageLegends](https://observablehq.com/plot/features/legends)

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

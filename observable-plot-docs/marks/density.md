---
url: "https://observablehq.com/plot/marks/density"
title: "Density mark | Plot"
---

# Density mark [^0.5.1](https://github.com/observablehq/plot/releases/tag/v0.5.1 "added in v0.5.1") [​](https://observablehq.com/plot/marks/density\#density-mark)

TIP

For contours of spatially-distributed quantitative values, see the [contour mark](https://observablehq.com/plot/marks/contour).

The **density mark** shows the [estimated density](https://en.wikipedia.org/wiki/Multivariate_kernel_density_estimation) of two-dimensional point clouds. Contours guide the eye towards the local peaks of concentration of the data, much like a topographic map does with elevation. This is especially useful given overplotting in dense datasets.

2.02.53.03.54.04.55.0↑ eruptions4550556065707580859095waiting → [Fork](https://observablehq.com/@observablehq/plot-point-cloud-density "Open on Observable")

js

```
Plot.plot({
  inset: 10,
  marks: [\
    Plot.density(faithful, {x: "waiting", y: "eruptions", stroke: "blue", strokeWidth: 0.25}),\
    Plot.density(faithful, {x: "waiting", y: "eruptions", stroke: "blue", thresholds: 4}),\
    Plot.dot(faithful, {x: "waiting", y: "eruptions", fill: "currentColor", r: 1.5})\
  ]
})
```

The **bandwidth** option specifies the radius of the [Gaussian kernel](https://en.wikipedia.org/wiki/Gaussian_function) describing the influence of each point as a function of distance; this kernel is summed over a discrete grid covering the plot, and then contours ( _isolines_) are derived for values between 0 (exclusive) and the maximum density (exclusive) using the [marching squares algorithm](https://en.wikipedia.org/wiki/Marching_squares).

Bandwidth: 20.0

2.02.53.03.54.04.55.0↑ eruptions5060708090waiting → [Fork](https://observablehq.com/@observablehq/plot-density-options "Open on Observable")

js

```
Plot.plot({
  inset: 20,
  marks: [\
    Plot.density(faithful, {x: "waiting", y: "eruptions", bandwidth}),\
    Plot.dot(faithful, {x: "waiting", y: "eruptions"})\
  ]
})
```

The **thresholds** option specifies the number of contour lines (minus one) to be computed, or an explicit array of threshold values. For example, with 4 thresholds and a maximum density of 10, contour lines would be drawn for the values 2.5, 5, and 7.5. The default number of thresholds is 20.

Thresholds: 20

2.02.53.03.54.04.55.0↑ eruptions5060708090waiting → [Fork](https://observablehq.com/@observablehq/plot-density-options "Open on Observable")

js

```
Plot.plot({
  inset: 20,
  marks: [\
    Plot.density(faithful, {x: "waiting", y: "eruptions", thresholds}),\
    Plot.dot(faithful, {x: "waiting", y: "eruptions"})\
  ]
})
```

The density mark also works with one-dimensional values:

4550556065707580859095waiting → [Fork](https://observablehq.com/@observablehq/plot-one-dimensional-density "Open on Observable")

js

```
Plot.plot({
  height: 100,
  inset: 10,
  marks: [\
    Plot.density(faithful, {x: "waiting", stroke: "blue", strokeWidth: 0.25, bandwidth: 10}),\
    Plot.density(faithful, {x: "waiting", stroke: "blue", thresholds: 4, bandwidth: 10}),\
    Plot.dot(faithful, {x: "waiting", fill: "currentColor", r: 1.5})\
  ]
})
```

The density mark supports Plot’s [projection system](https://observablehq.com/plot/features/projections), as in this heatmap showing the density of Walmart stores across the contiguous United States (which is a decent proxy for population density).

[Fork](https://observablehq.com/@observablehq/plot-walmart-density "Open on Observable")

js

```
Plot.plot({
  projection: "albers",
  color: {scheme: "YlGnBu"},
  marks: [\
    Plot.density(walmarts, {x: "longitude", y: "latitude", bandwidth: 10, fill: "density"}),\
    Plot.geo(statemesh, {strokeOpacity: 0.3}),\
    Plot.geo(nation),\
    Plot.dot(walmarts, {x: "longitude", y: "latitude", r: 1, fill: "currentColor"})\
  ]
})
```

TIP

Use an equal-area projection with the density mark.

By using the _density_ keyword as a **fill** or **stroke** color, you can draw regions with a sequential color encoding.

4005001k2k3k4k5k10k↑ price200m300m400m500m12345carat → [Fork](https://observablehq.com/@observablehq/plot-density-stroke "Open on Observable")

js

```
Plot.plot({
  inset: 10,
  grid: true,
  x: {type: "log"},
  y: {type: "log"},
  marks: [\
    Plot.density(diamonds, {x: "carat", y: "price", stroke: "density"})\
  ]
})
```

To facilitate comparison across facets ( **fx** or **fy**) and series ( **z**, **stroke**, or **fill**), the thresholds are determined by the series with the highest density. For instance, the chart below shows the highest concentration of penguins, arranged by flipper length and culmen length, on Biscoe island; the contours in the other facets use the same thresholds.

BiscoeDreamTorgersenisland34363840424446485052545658↑ culmen\_length\_mm180200220180200220180200220flipper\_length\_mm → [Fork](https://observablehq.com/@observablehq/plot-density-faceted "Open on Observable")

js

```
Plot.plot({
  marks: [\
    Plot.density(penguins, {fx: "island", x: "flipper_length_mm", y: "culmen_length_mm", stroke: "density", clip: true}),\
    Plot.frame()\
  ]
})
```

The **weight** channel specifies the contribution of each data point to the estimated density; it defaults to 1, weighing each point equally. This can be used to give some points more influence than others. Try adjusting the skew slider below to transition between female- and male-weighted density.

Skew (-F/+M): +0.00

FEMALEMALE

34363840424446485052545658↑ culmen\_length\_mm180190200210220230flipper\_length\_mm → [Fork](https://observablehq.com/@observablehq/plot-density-weighted "Open on Observable")

js

```
Plot.plot({
  inset: 10,
  color: {legend: true},
  marks: [\
    Plot.density(penguins.filter((d) => d.sex), {\
      weight: (d) => d.sex === "FEMALE" ? 1 - skew : 1 + skew,\
      x: "flipper_length_mm",\
      y: "culmen_length_mm",\
      strokeOpacity: 0.5,\
      clip: true\
    }),\
    Plot.dot(penguins.filter((d) => d.sex), {\
      x: "flipper_length_mm",\
      y: "culmen_length_mm",\
      stroke: "sex",\
      strokeOpacity: (d) => d.sex === "FEMALE" ? 1 - skew : 1 + skew\
    }),\
    Plot.frame()\
  ]
})
```

You can specify a negative weight for points that the density contours should avoid, resulting in regions of influence that do not overlap.

AdelieChinstrapGentoo

34363840424446485052545658↑ culmen\_length\_mm180190200210220230flipper\_length\_mm → [Fork](https://observablehq.com/@observablehq/plot-non-overlapping-density-regions "Open on Observable")

js

```
Plot.plot({
  inset: 10,
  color: {legend: true},
  marks: [\
    d3.groups(penguins, (d) => d.species).map(([s]) =>\
      Plot.density(penguins, {\
        x: "flipper_length_mm",\
        y: "culmen_length_mm",\
        weight: (d) => d.species === s ? 1 : -1,\
        fill: () => s,\
        fillOpacity: 0.2,\
        thresholds: [0.05]\
      })\
    ),\
    Plot.dot(penguins, {\
      x: "flipper_length_mm",\
      y: "culmen_length_mm",\
      stroke: "species"\
    }),\
    Plot.frame()\
  ]
})
```

## Density options [​](https://observablehq.com/plot/marks/density\#density-options)

In addition to the [standard mark options](https://observablehq.com/plot/features/marks#mark-options), the following optional channels are supported:

- **x** \- the horizontal position; bound to the _x_ scale
- **y** \- the vertical position; bound to the _y_ scale
- **weight** \- the contribution to the estimated density

If either of the **x** or **y** channels are not specified, the corresponding position is controlled by the **frameAnchor** option.

The **thresholds** option, which defaults to 20, specifies one more than the number of contours that will be computed at uniformly-spaced intervals between 0 (exclusive) and the maximum density (exclusive). The **thresholds** option may also be specified as an array or iterable of explicit density values. The **bandwidth** option, which defaults to 20, specifies the standard deviation of the Gaussian kernel used for estimation in pixels.

If a **z**, **stroke** or **fill** channel is specified, the input points are grouped by series, and separate sets of contours are generated for each series. If the **stroke** or **fill** is specified as _density_, a color channel is constructed with values representing the density threshold value of each contour.

## density( _data_, _options_) [​](https://observablehq.com/plot/marks/density\#density)

js

```
Plot.density(faithful, {x: "waiting", y: "eruptions"})
```

Returns a new density mark for the given _data_ and _options_.

Pager

[Previous pageDelaunay](https://observablehq.com/plot/marks/delaunay)

[Next pageDifference](https://observablehq.com/plot/marks/difference)

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

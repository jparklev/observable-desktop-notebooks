---
url: "https://observablehq.com/plot/marks/frame"
title: "Frame mark | Plot"
---

# Frame mark [​](https://observablehq.com/plot/marks/frame\#frame-mark)

The **frame mark** draws a rectangle around the plot area.

0.00.10.20.30.40.50.60.70.80.91.0

js

```
Plot.frame().plot({x: {domain: [0, 1], grid: true}})
```

Frames are most commonly used in conjunction with facets to provide better separation (Gestalt grouping) of faceted marks. Without a frame, it can be hard to tell where one facet ends and the next begins.

Show frame:

AdelieChinstrapGentoospecies1415161718192021↑ culmen\_depth\_mm405040504050culmen\_length\_mm →

js

```
Plot.plot({
  grid: true,
  inset: 10,
  marks: [\
    framed ? Plot.frame() : null,\
    Plot.dot(penguins, {x: "culmen_length_mm", y: "culmen_depth_mm", fill: "#eee"}),\
    Plot.dot(penguins, {x: "culmen_length_mm", y: "culmen_depth_mm", fx: "species"})\
  ]
})
```

Unlike most marks, a frame never takes _data_; the first argument to [frame](https://observablehq.com/plot/marks/frame#frame) is the _options_ object. (For data-driven rectangles, see the [rect mark](https://observablehq.com/plot/marks/rect).)

0.00.10.20.30.40.50.60.70.80.91.0

js

```
Plot.frame({stroke: "red"}).plot({x: {domain: [0, 1], grid: true}})
```

While options are often specified in literal values, such as _red_ above, the standard [mark channels](https://observablehq.com/plot/features/marks#mark-options) such as **fill** and **stroke** can also be specified as abstract values. For example, in the density heatmap below comparing the delay between eruptions of the Old Faithful geyser ( _waiting_) in _x_ → and the duration of the eruption ( _eruptions_) in _y_ ↑, both in minutes, we fill the frame with black representing zero density.

2.02.53.03.54.04.55.0↑ eruptions5060708090waiting →

js

```
Plot.plot({
  inset: 30,
  marks: [\
    Plot.frame({fill: 0}),\
    Plot.density(faithful, {x: "waiting", y: "eruptions", fill: "density"})\
  ]
})
```

TIP

This is equivalent to a [rect](https://observablehq.com/plot/marks/rect): `Plot.rect({length: 1}, {fill: 0})`.

You can also place a frame on a specific facet using the **fx** or **fy** option. Below, a frame emphasizes the _Gentoo_ facet, say to draw attention to how much bigger they are. 🐧

AdelieChinstrapGentoospecies3,0003,5004,0004,5005,0005,5006,000body\_mass\_g →

js

```
Plot.plot({
  marginLeft: 80,
  inset: 10,
  marks: [\
    Plot.frame({fy: "Gentoo"}),\
    Plot.dot(penguins, {x: "body_mass_g", fy: "species"})\
  ]
})
```

TIP

Or: `Plot.rect({length: 1}, {fy: ["Gentoo"], stroke: "currentColor"})`.

The **anchor** option [^0.6.3](https://github.com/observablehq/plot/releases/tag/v0.6.3 "added in v0.6.3"), if specified to a value of _left_, _right_, _top_ or _bottom_, draws only that side of the frame. In that case, the **fill** and **rx**, **ry** options are ignored.

0.00.10.20.30.40.50.60.70.80.91.0

js

```
Plot.plot({
  x: {
    domain: [0, 1],
    grid: true
  },
  marks: [\
    Plot.frame({stroke: "red", anchor: "bottom"})\
  ]
})
```

## Frame options [​](https://observablehq.com/plot/marks/frame\#frame-options)

The frame mark supports the [standard mark options](https://observablehq.com/plot/features/marks#mark-options), including [insets](https://observablehq.com/plot/features/marks#insets) and [rounded corners](https://observablehq.com/plot/features/marks#rounded-corners). It does not accept any data. The default **stroke** is _currentColor_, and the default **fill** is _none_.

If the **anchor** option is specified as one of _left_, _right_, _top_, or _bottom_, that side is rendered as a single line (and the **fill**, **fillOpacity**, **rx**, and **ry** options are ignored).

## frame( _options_) [​](https://observablehq.com/plot/marks/frame\#frame)

js

```
Plot.frame({stroke: "red"})
```

Returns a new frame mark with the specified _options_.

Pager

[Previous pageDot](https://observablehq.com/plot/marks/dot)

[Next pageGeo](https://observablehq.com/plot/marks/geo)

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

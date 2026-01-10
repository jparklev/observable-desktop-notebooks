---
url: "https://observablehq.com/plot/interactions/crosshair"
title: "Crosshair mark | Plot"
---

# Crosshair mark [^0.6.7](https://github.com/observablehq/plot/releases/tag/v0.6.7 "added in v0.6.7") [​](https://observablehq.com/plot/interactions/crosshair\#crosshair-mark)

The **crosshair mark** shows the _x_ (horizontal↔︎ position) and _y_ (vertical↕︎ position) value of the point closest to the [pointer](https://observablehq.com/plot/interactions/pointer) on the bottom and left sides of the frame, respectively.

1415161718192021↑ culmen\_depth\_mm3540455055culmen\_length\_mm → [Fork](https://observablehq.com/@observablehq/plot-crosshair "Open on Observable")

js

```
Plot.plot({
  marks: [\
    Plot.dot(penguins, {x: "culmen_length_mm", y: "culmen_depth_mm", stroke: "sex"}),\
    Plot.crosshair(penguins, {x: "culmen_length_mm", y: "culmen_depth_mm"})\
  ]
})
```

For charts which have a “dominant” dimension, such as time in a time-series chart, use the crosshairX or crosshairY mark for the [pointerX](https://observablehq.com/plot/interactions/pointer#pointerX) or [pointerY](https://observablehq.com/plot/interactions/pointer#pointerY) transform as appropriate.

60708090100110120130140150160170180190↑ Close20142015201620172018 [Fork](https://observablehq.com/@observablehq/plot-crosshairx "Open on Observable")

js

```
Plot.plot({
  marks: [\
    Plot.lineY(aapl, {x: "Date", y: "Close"}),\
    Plot.crosshairX(aapl, {x: "Date", y: "Close"})\
  ]
})
```

If either **x** or **y** is not specified, the crosshair is one-dimensional.

3,0003,5004,0004,5005,0005,5006,000body\_mass\_g → [Fork](https://observablehq.com/@observablehq/plot-one-dimensional-crosshair "Open on Observable")

js

```
Plot.plot({
  marks: [\
    Plot.tickX(penguins, {x: "body_mass_g"}),\
    Plot.crosshairX(penguins, {x: "body_mass_g"})\
  ]
})
```

The **color** option sets the fill color of the text and the stroke color of the rule. This option can be specified as a channel to reinforce a color encoding.

1415161718192021↑ culmen\_depth\_mm3540455055culmen\_length\_mm → [Fork](https://observablehq.com/@observablehq/plot-color-crosshair "Open on Observable")

js

```
Plot.plot({
  marks: [\
    Plot.dot(penguins, {x: "culmen_length_mm", y: "culmen_depth_mm", stroke: "sex"}),\
    Plot.crosshair(penguins, {x: "culmen_length_mm", y: "culmen_depth_mm", color: "sex", opacity: 0.5})\
  ]
})
```

The crosshair mark does not currently support any format options; values are displayed with the default format. If you are interested in this feature, please upvote [#1596](https://github.com/observablehq/plot/issues/1596). In the meantime, you can implement a custom crosshair using the [pointer transform](https://observablehq.com/plot/interactions/pointer) and a [text mark](https://observablehq.com/plot/marks/text).

## Crosshair options [​](https://observablehq.com/plot/interactions/crosshair\#crosshair-options)

The following options are supported:

- **x** \- the horizontal position; bound to the _x_ scale
- **y** \- the vertical position; bound to the _y_ scale
- **color** \- shorthand for setting both **ruleStroke** and **textFill**
- **opacity** \- shorthand for setting **ruleStrokeOpacity**
- **ruleStroke** \- the rule stroke color
- **ruleStrokeOpacity** \- the rule stroke opacity; defaults to 0.2
- **ruleStrokeWidth** \- the rule stroke width; defaults to 1
- **textFill** \- the text fill color
- **textFillOpacity** \- the text fill opacity
- **textStroke** \- the text stroke color; defaults to _white_ to improve legibility
- **textStrokeOpacity** \- the text stroke opacity; defaults to 1
- **textStrokeWidth** \- the text stroke width; defaults to 5
- **maxRadius** \- the maximum pointing distance, in pixels; defaults to 40

The crosshair mark supports faceting, but most other mark options are ignored.

## crosshair( _data_, _options_) [​](https://observablehq.com/plot/interactions/crosshair\#crosshair)

js

```
Plot.crosshair(cars, {x: "economy (mpg)", y: "cylinders"})
```

Returns a new crosshair for the given _data_ and _options_, drawing horizontal and vertical rules. The corresponding **x** and **y** values are also drawn just outside the bottom and left sides of the frame, respectively, typically on top of the axes. If either **x** or **y** is not specified, the crosshair will be one-dimensional.

## crosshairX( _data_, _options_) [​](https://observablehq.com/plot/interactions/crosshair\#crosshairX)

js

```
Plot.crosshairX(aapl, {x: "Date", y: "Close"})
```

Like crosshair, but using [pointerX](https://observablehq.com/plot/interactions/pointer#pointerX) when _x_ is the dominant dimension, like time in a time-series chart.

## crosshairY( _data_, _options_) [​](https://observablehq.com/plot/interactions/crosshair\#crosshairY)

js

```
Plot.crosshairY(aapl, {x: "Date", y: "Close"})
```

Like crosshair, but using [pointerY](https://observablehq.com/plot/interactions/pointer#pointerY) when _y_ is the dominant dimension.

Pager

[Previous pageWindow](https://observablehq.com/plot/transforms/window)

[Next pagePointer](https://observablehq.com/plot/interactions/pointer)

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

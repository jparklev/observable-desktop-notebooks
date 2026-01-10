---
url: "https://observablehq.com/plot/marks/arrow"
title: "Arrow mark | Plot"
---

# Arrow mark [^0.4.0](https://github.com/observablehq/plot/releases/tag/v0.4.0 "added in v0.4.0") [​](https://observablehq.com/plot/marks/arrow\#arrow-mark)

TIP

See also the [vector mark](https://observablehq.com/plot/marks/vector), which draws arrows of a given length and direction.

The **arrow mark** draws arrows between two points \[ **x1**, **y1**\] and \[ **x2**, **y2**\] in quantitative dimensions. It is similar to the [link mark](https://observablehq.com/plot/marks/link), except it draws an arrowhead and is suitable for directed edges. With the **bend** option, it can be swoopy.⤵︎

For example, below we show the rising inequality (and population) in various U.S. cities from 1980 to 2015. Each arrow represents two observations of a city: the city’s population ( **x**) and inequality ( **y**) in 1980, and the same in 2015. The arrow’s **stroke** redundantly encodes the change in inequality: red indicates rising inequality, while blue (there are only four) indicates declining inequality.

−2+0+2Change in inequality from 1980 to 201545678↑ Inequality200k300k400k1M2M3M4M10M20MPopulation →New YorkChicagoHoustonWashington, D.C.San FranciscoSan JoseFairfield, Conn.Binghamton, N.Y. [Fork](https://observablehq.com/@observablehq/plot-arrow-variation-chart "Open on Observable")

js

```
Plot.plot({
  grid: true,
  inset: 10,
  x: {
    type: "log",
    label: "Population"
  },
  y: {
    label: "Inequality",
    ticks: 4
  },
  color: {
    scheme: "BuRd",
    label: "Change in inequality from 1980 to 2015",
    legend: true,
    tickFormat: "+f"
  },
  marks: [\
    Plot.arrow(metros, {\
      x1: "POP_1980",\
      y1: "R90_10_1980",\
      x2: "POP_2015",\
      y2: "R90_10_2015",\
      bend: true,\
      stroke: (d) => d.R90_10_2015 - d.R90_10_1980\
    }),\
    Plot.text(metros, {\
      x: "POP_2015",\
      y: "R90_10_2015",\
      filter: "highlight",\
      text: "nyt_display",\
      fill: "currentColor",\
      stroke: "white",\
      dy: -6\
    })\
  ]
})
```

The arrow mark is also useful for drawing directed graph edges, say representing transition frequencies in a finite state machine.

ABC325172118 [Fork](https://observablehq.com/@observablehq/plot-finite-state-machine "Open on Observable")

js

```
Plot.plot({
  inset: 60,
  aspectRatio: 1,
  axis: null,
  marks: [\
    Plot.dot(markov.nodes, {r: 40}),\
    Plot.arrow(markov.edges, {\
      x1: ([[x1]]) => x1,\
      y1: ([[, y1]]) => y1,\
      x2: ([, [x2]]) => x2,\
      y2: ([, [, y2]]) => y2,\
      bend: true,\
      strokeWidth: ([,, value]) => value,\
      strokeLinejoin: "miter",\
      headLength: 24,\
      inset: 48\
    }),\
    Plot.text(markov.nodes, {text: ["A", "B", "C"], dy: 12}),\
    Plot.text(markov.edges, {\
      x: ([[x1, y1], [x2, y2]]) => (x1 + x2) / 2 + (y1 - y2) * 0.15,\
      y: ([[x1, y1], [x2, y2]]) => (y1 + y2) / 2 - (x1 - x2) * 0.15,\
      text: ([,, value]) => value\
    })\
  ]
})
```

For undirected edges, as in the arc diagram of character co-occurrence in _Les Misérables_ below, set the **sweep** option to the desired orientation: _-y_ for right-bulging links whose endpoints are vertically separated.

MyrielNapoleonMlle.BaptistineMme.MagloireCountessdeLoGeborandChamptercierCravatteCountOldManLabarreValjeanMargueriteMme.deRIsabeauGervaisTholomyesListolierFameuilBlachevilleFavouriteDahliaZephineFantineMme.ThenardierThenardierCosetteJavertFaucheleventBamataboisPerpetueSimpliceScaufflaireWoman1JudgeChampmathieuBrevetChenildieuCochepaillePontmercyBoulatruelleEponineAnzelmaWoman2MotherInnocentGribierJondretteMme.BurgonGavrocheGillenormandMagnonMlle.GillenormandMme.PontmercyMlle.VauboisLt.GillenormandMariusBaronessTMabeufEnjolrasCombeferreProuvaireFeuillyCourfeyracBahorelBossuetJolyGrantaireMotherPlutarchGueulemerBabetClaquesousMontparnasseToussaintChild1Child2BrujonMme.Hucheloup [Fork](https://observablehq.com/@observablehq/plot-arc-diagram "Open on Observable")

js

```
Plot.plot({
  height: 1080,
  marginLeft: 100,
  axis: null,
  x: {domain: [0, 1]}, // see https://github.com/observablehq/plot/issues/1541
  color: {domain: d3.range(10), unknown: "#ccc"},
  marks: [\
    Plot.dot(miserables.nodes, {x: 0, y: "id", fill: "group", sort: {y: "fill"}}),\
    Plot.text(miserables.nodes, {x: 0, y: "id", text: "id", textAnchor: "end", dx: -6, fill: "group"}),\
    Plot.arrow(miserables.links, {x: 0, y1: "source", y2: "target", sweep: "-y", bend: 90, headLength: 0, stroke: samegroup, sort: samegroup, reverse: true})\
  ]
})
```

## Arrow options [​](https://observablehq.com/plot/marks/arrow\#arrow-options)

The following channels are required:

- **x1** \- the starting horizontal position; bound to the _x_ scale
- **y1** \- the starting vertical position; bound to the _y_ scale
- **x2** \- the ending horizontal position; bound to the _x_ scale
- **y2** \- the ending vertical position; bound to the _y_ scale

For vertical or horizontal arrows, the **x** option can be specified as shorthand for **x1** and **x2**, and the **y** option can be specified as shorthand for **y1** and **y2**, respectively.

The arrow mark supports the [standard mark options](https://observablehq.com/plot/features/marks#mark-options). The **stroke** defaults to _currentColor_. The **fill** defaults to _none_. The **strokeWidth** defaults to 1.5, and the **strokeMiterlimit** defaults to 1. The following additional options are supported:

- **bend** \- the bend angle, in degrees; defaults to 0°; true for 22.5°
- **headAngle** \- the arrowhead angle, in degrees; defaults to 60°
- **headLength** \- the arrowhead scale; defaults to 8
- **insetEnd** \- inset at the end of the arrow (useful if the arrow points to a dot)
- **insetStart** \- inset at the start of the arrow
- **inset** \- shorthand for the two insets
- **sweep** \- the sweep order

The **bend** option sets the angle between the straight line connecting the two points and the outgoing direction of the arrow from the start point. It must be within ±90°. A positive angle will produce a clockwise curve; a negative angle will produce a counterclockwise curve; zero will produce a straight line. The **headAngle** determines how pointy the arrowhead is; it is typically between 0° and 180°. The **headLength** determines the scale of the arrowhead relative to the stroke width. Assuming the default of stroke width 1.5px, the **headLength** is the length of the arrowhead’s side in pixels.

The **sweep** option [^0.6.10](https://github.com/observablehq/plot/releases/tag/v0.6.10 "added in v0.6.10") controls the bend orientation. It defaults to 1 indicating a positive (clockwise) bend angle; -1 indicates a negative (anticlockwise) bend angle; 0 effectively clears the bend angle. If _-x_, the bend angle is flipped when the ending point is to the left of the starting point — ensuring all arrows bulge up (down if bend is negative); if _-y_, the bend angle is flipped when the ending point is above the starting point — ensuring all arrows bulge right (left if bend is negative); the sign is negated for _+x_ and _+y_.

## arrow( _data_, _options_) [​](https://observablehq.com/plot/marks/arrow\#arrow)

js

```
Plot.arrow(inequality, {x1: "POP_1980", y1: "R90_10_1980", x2: "POP_2015", y2: "R90_10_2015", bend: true})
```

Returns a new arrow with the given _data_ and _options_.

Pager

[Previous pageArea](https://observablehq.com/plot/marks/area)

[Next pageAuto](https://observablehq.com/plot/marks/auto)

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

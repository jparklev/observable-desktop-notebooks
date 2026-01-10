---
url: "https://observablehq.com/plot/marks/vector"
title: "Vector mark | Plot"
---

# Vector mark [^0.4.0](https://github.com/observablehq/plot/releases/tag/v0.4.0 "added in v0.4.0") [​](https://observablehq.com/plot/marks/vector\#vector-mark)

TIP

See also the [arrow mark](https://observablehq.com/plot/marks/arrow), which draws arrows between two points.

The **vector mark** draws little arrows, typically positioned in **x** and **y** quantitative dimensions, with an optional magnitude ( **length**) and direction ( **rotate**), as in a vector field. For example, the chart below, based on a [LitVis example](https://github.com/gicentre/litvis/blob/main/examples/windVectors.md), shows wind speed and direction for a section of western Europe.

0510Speed (m/s)4647484950515253545556575859↑ latitude−8−6−4−202468longitude → [Fork](https://observablehq.com/@observablehq/plot-wind-map "Open on Observable")

js

```
Plot.plot({
  inset: 10,
  aspectRatio: 1,
  color: {label: "Speed (m/s)", zero: true, legend: true},
  marks: [\
    Plot.vector(wind, {\
      x: "longitude",\
      y: "latitude",\
      rotate: ({u, v}) => Math.atan2(u, v) * 180 / Math.PI,\
      length: ({u, v}) => Math.hypot(u, v),\
      stroke: ({u, v}) => Math.hypot(u, v)\
    })\
  ]
})
```

INFO

Regarding this data, [Remote Sensing Systems](https://www.remss.com/measurements/ccmp/) says: _“Standard U and V coordinates apply, meaning the positive U is to the right and positive V is above the axis. U and V are relative to true north. CCMP winds are expressed using the oceanographic convention, meaning a wind blowing toward the Northeast has a positive U component and a positive V component… Longitude is given in degrees East from 0.125 to 359.875 and latitude is given in degrees North with negative values representing southern locations.”_

Vectors can be used with Plot’s [projection system](https://observablehq.com/plot/features/projections). The map below shows the margin by which the winner of the US presidential election of 2020 won the vote in each county. The arrow’s length encodes the difference in votes, and the orientation and color show who won ( for the Democratic candidate, and  for the Republican candidate).

[Fork](https://observablehq.com/@observablehq/plot-election-wind-map "Open on Observable")

js

```
Plot.plot({
  projection: "albers-usa",
  length: {type: "sqrt", transform: Math.abs},
  marks: [\
    Plot.geo(statemesh, {strokeWidth: 0.5}),\
    Plot.geo(nation),\
    Plot.vector(\
      counties,\
      Plot.centroid({\
        anchor: "start",\
        length: (d) => d.properties.margin2020 * d.properties.votes,\
        stroke: (d) => d.properties.margin2020 > 0 ? "red" : "blue",\
        rotate: (d) => d.properties.margin2020 > 0 ? 60 : -60\
      })\
    )\
  ]
})
```

The **shape** option [^0.6.2](https://github.com/observablehq/plot/releases/tag/v0.6.2 "added in v0.6.2") controls the vector’s appearance, while the **anchor** option positions the vector relative to its anchor point specified in **x** and **y**. The [spike constructor](https://observablehq.com/plot/marks/vector#spike) sets the **shape** to _spike_ and the **anchor** to _start_. For example, this can be used to produce a [spike map](https://observablehq.com/@observablehq/plot-spike) of U.S. county population.

[Fork](https://observablehq.com/@observablehq/plot-spike-map-example "Open on Observable")

js

```
Plot.plot({
  width: 688,
  projection: "albers-usa",
  length: {range: [0, 200]},
  marks: [\
    Plot.geo(statemesh, {strokeOpacity: 0.5}),\
    Plot.geo(nation),\
    Plot.spike(counties, Plot.geoCentroid({length: (d) => d.properties.population, stroke: "green"}))\
  ]
})
```

You can even implement a custom **shape** by supplying an object with a **draw** method. This method takes a _context_ for drawing paths and the _length_ of the vector. See the [moon phase calendar](https://observablehq.com/@observablehq/plot-phases-of-the-moon) for an example.

Lastly, here is an example showing a Perlin noise field, just because it’s pretty:

[Fork](https://observablehq.com/@observablehq/plot-perlin-noise "Open on Observable")

js

```
Plot.plot({
  inset: 6,
  width: 1024,
  aspectRatio: 1,
  axis: null,
  marks: [\
    Plot.vector(poisson([0, 0, 2, 2], 4000), {\
      length: ([x, y]) => (noise(x + 2, y) + 0.5) * 24,\
      rotate: ([x, y]) => noise(x, y) * 360\
    })\
  ]
})
```

This example uses a noise( _x_, _y_) function defined as:

js

```
noise = octave(perlin2, 2)
```

See Mike Bostock’s [Perlin Noise](https://observablehq.com/@mbostock/perlin-noise) and [Poisson Disk Sampling](https://observablehq.com/@mbostock/poisson-disk-sampling) notebooks for source code.

## Vector options [​](https://observablehq.com/plot/marks/vector\#vector-options)

In addition to the [standard mark options](https://observablehq.com/plot/features/marks#mark-options), the following optional channels are supported:

- **x** \- the horizontal position; bound to the _x_ scale
- **y** \- the vertical position; bound to the _y_ scale
- **length** \- the length in pixels; bound to the _length_ scale; defaults to 12
- **rotate** \- the rotation angle in degrees clockwise; defaults to 0

If either of the **x** or **y** channels are not specified, the corresponding position is controlled by the **frameAnchor** option.

The following constant options are also supported:

- **shape** \- the shape of the vector; defaults to _arrow_
- **r** \- a radius in pixels; defaults to 3.5
- **anchor** \- one of _start_, _middle_, or _end_; defaults to _middle_
- **frameAnchor** \- how to position the vector within the frame; defaults to _middle_

The **shape** option controls the visual appearance (path geometry) of the vector and supports the following values:

- _arrow_ (default) - an arrow with head size proportional to its length
- _spike_ \- an isosceles triangle with open base
- any object with a **draw** method; it receives a _context_, _length_, and _radius_

If the **anchor** is _start_, the arrow will start at the given _xy_ position and point in the direction given by the rotation angle. If the **anchor** is _end_, the arrow will maintain the same orientation, but be positioned such that it ends in the given _xy_ position. If the **anchor** is _middle_, the arrow will be likewise be positioned such that its midpoint intersects the given _xy_ position.

If the **x** channel is not specified, vectors will be horizontally centered in the plot (or facet). Likewise if the **y** channel is not specified, vectors will be vertically centered in the plot (or facet). Typically either _x_, _y_, or both are specified.

The **rotate** and **length** options can be specified as either channels or constants. When specified as a number, it is interpreted as a constant; otherwise it is interpreted as a channel. The length defaults to 12 pixels, and the rotate defaults to 0 degrees (pointing up↑). Vectors with a negative length will be drawn inverted. Positive angles proceed clockwise from noon.

The **stroke** defaults to _currentColor_. The **strokeWidth** defaults to 1.5, and the **strokeLinecap** defaults to _round_.

Vectors are drawn in input order, with the last data drawn on top. If sorting is needed, say to mitigate overplotting by drawing the smallest vectors on top, consider a [sort transform](https://observablehq.com/plot/transforms/sort).

## vector( _data_, _options_) [​](https://observablehq.com/plot/marks/vector\#vector)

js

```
Plot.vector(wind, {x: "longitude", y: "latitude", length: "speed", rotate: "direction"})
```

Returns a new vector with the given _data_ and _options_. If neither the **x** nor **y** options are specified, _data_ is assumed to be an array of pairs \[\[ _x₀_, _y₀_\], \[ _x₁_, _y₁_\], \[ _x₂_, _y₂_\], …\] such that **x** = \[ _x₀_, _x₁_, _x₂_, …\] and **y** = \[ _y₀_, _y₁_, _y₂_, …\].

## vectorX( _data_, _options_) [​](https://observablehq.com/plot/marks/vector\#vectorX)

js

```
Plot.vectorX(cars.map((d) => d["economy (mpg)"]))
```

Equivalent to [vector](https://observablehq.com/plot/marks/vector#vector) except that if the **x** option is not specified, it defaults to the identity function and assumes that _data_ = \[ _x₀_, _x₁_, _x₂_, …\].

## vectorY( _data_, _options_) [​](https://observablehq.com/plot/marks/vector\#vectorY)

js

```
Plot.vectorY(cars.map((d) => d["economy (mpg)"]))
```

Equivalent to [vector](https://observablehq.com/plot/marks/vector#vector) except that if the **y** option is not specified, it defaults to the identity function and assumes that _data_ = \[ _y₀_, _y₁_, _y₂_, …\].

## spike( _data_, _options_) [^0.6.2](https://github.com/observablehq/plot/releases/tag/v0.6.2 "added in v0.6.2") [​](https://observablehq.com/plot/marks/vector\#spike)

js

```
Plot.spike(counties, Plot.geoCentroid({length: (d) => d.properties.population}))
```

Equivalent to [vector](https://observablehq.com/plot/marks/vector#vector) except that the **shape** defaults to _spike_, the **stroke** defaults to _currentColor_, the **strokeWidth** defaults to 1, the **fill** defaults to **stroke**, the **fillOpacity** defaults to 0.3, and the **anchor** defaults to _start_.

Pager

[Previous pageTree](https://observablehq.com/plot/marks/tree)

[Next pageWaffle](https://observablehq.com/plot/marks/waffle)

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

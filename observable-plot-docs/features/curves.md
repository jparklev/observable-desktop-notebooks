---
url: "https://observablehq.com/plot/features/curves"
title: "Curves | Plot"
---

# Curves [​](https://observablehq.com/plot/features/curves\#curves)

A **curve** defines how to turn a discrete representation of a line as a sequence of points \[\[ _x₀_, _y₀_\], \[ _x₁_, _y₁_\], \[ _x₂_, _y₂_\], …\] into a continuous path; _i.e._, how to interpolate between points. Curves are used by the [line](https://observablehq.com/plot/marks/line), [area](https://observablehq.com/plot/marks/area), and [link](https://observablehq.com/plot/marks/link) marks, and are implemented by [d3-shape](https://d3js.org/d3-shape/curve).

Curve: basisbasis-openbasis-closedbump-xbump-ybundlecardinalcardinal-opencardinal-closedcatmull-romcatmull-rom-opencatmull-rom-closedlinearlinear-closedmonotone-xmonotone-ynaturalstepstep-afterstep-before

0.10.20.30.40.50.60.70.80.9024681012141618 [Fork](https://observablehq.com/@observablehq/plot-curve-option "Open on Observable")

js

```
Plot.plot({
  marks: [\
    Plot.lineY(numbers, {curve: "catmull-rom"}),\
    Plot.dotY(numbers, {x: (d, i) => i})\
  ]
})
```

The supported curve options are:

- **curve** \- the curve method, either a string or a function
- **tension** \- the curve tension (for fine-tuning)

The following named curve methods are supported:

- _basis_ \- a cubic basis spline (repeating the end points)
- _basis-open_ \- an open cubic basis spline
- _basis-closed_ \- a closed cubic basis spline
- _bump-x_ \- a Bézier curve with horizontal tangents
- _bump-y_ \- a Bézier curve with vertical tangents
- _bundle_ \- a straightened cubic basis spline (suitable for lines only, not areas)
- _cardinal_ \- a cubic cardinal spline (with one-sided differences at the ends)
- _cardinal-open_ \- an open cubic cardinal spline
- _cardinal-closed_ \- an closed cubic cardinal spline
- _catmull-rom_ \- a cubic Catmull–Rom spline (with one-sided differences at the ends)
- _catmull-rom-open_ \- an open cubic Catmull–Rom spline
- _catmull-rom-closed_ \- a closed cubic Catmull–Rom spline
- _linear_ \- a piecewise linear curve ( _i.e._, straight line segments)
- _linear-closed_ \- a closed piecewise linear curve ( _i.e._, straight line segments)
- _monotone-x_ \- a cubic spline that preserves monotonicity in _x_
- _monotone-y_ \- a cubic spline that preserves monotonicity in _y_
- _natural_ \- a natural cubic spline
- _step_ \- a piecewise constant function where _y_ changes at the midpoint of _x_
- _step-after_ \- a piecewise constant function where _y_ changes after _x_
- _step-before_ \- a piecewise constant function where _x_ changes after _y_
- _auto_ \- like _linear_, but use the (possibly spherical) [projection](https://observablehq.com/plot/features/projections), if any [^0.6.1](https://github.com/observablehq/plot/releases/tag/v0.6.1 "added in v0.6.1")

If **curve** is a function, it will be invoked with a given _context_ in the same fashion as a [D3 curve factory](https://d3js.org/d3-shape/curve#custom-curves). The _auto_ curve is only available for the [line mark](https://observablehq.com/plot/marks/line) and [link mark](https://observablehq.com/plot/marks/link) and is typically used in conjunction with a spherical [projection](https://observablehq.com/plot/features/projections) to interpolate along [geodesics](https://en.wikipedia.org/wiki/Geodesic).

The tension option only has an effect on bundle, cardinal and Catmull–Rom splines ( _bundle_, _cardinal_, _cardinal-open_, _cardinal-closed_, _catmull-rom_, _catmull-rom-open_, and _catmull-rom-closed_). For bundle splines, it corresponds to [beta](https://d3js.org/d3-shape/curve#curveBundle_beta); for cardinal splines, [tension](https://d3js.org/d3-shape/curve#curveCardinal_tension); for Catmull–Rom splines, [alpha](https://d3js.org/d3-shape/curve#curveCatmullRom_alpha).

Pager

[Previous pageLegends](https://observablehq.com/plot/features/legends)

[Next pageFormats](https://observablehq.com/plot/features/formats)

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

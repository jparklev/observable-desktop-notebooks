---
url: "https://observablehq.com/plot/marks/hexgrid"
title: "Hexgrid mark | Plot"
---

# Hexgrid mark [^0.5.0](https://github.com/observablehq/plot/releases/tag/v0.5.0 "added in v0.5.0") [​](https://observablehq.com/plot/marks/hexgrid\#hexgrid-mark)

The **hexgrid mark** draws a hexagonal grid spanning the frame. It can be used with the [hexbin transform](https://observablehq.com/plot/transforms/hexbin) to show how points are binned. The **binWidth** option specifies the distance between centers of neighboring hexagons in pixels; it defaults to 20, matching the hexbin transform.

1415161718192021↑ culmen\_depth\_mm3540455055culmen\_length\_mm → [Fork](https://observablehq.com/@observablehq/plot-hexgrid-example "Open on Observable")

js

```
Plot.plot({
  marks: [\
    Plot.hexgrid(),\
    Plot.dot(penguins, Plot.hexbin({r: "count"}, {x: "culmen_length_mm", y: "culmen_depth_mm", fill: "currentColor"}))\
  ]
})
```

## Hexgrid options [​](https://observablehq.com/plot/marks/hexgrid\#hexgrid-options)

The hexgrid mark supports the [standard mark options](https://observablehq.com/plot/features/marks#mark-options). It does not accept any data or support channels. The default **stroke** is _currentColor_, the default **strokeOpacity** is 0.1, and the default **clip** is true. The **binWidth** defaults to 20, matching the [hexbin transform](https://observablehq.com/plot/transforms/hexbin). The **fill** option is not supported, but a [frame mark](https://observablehq.com/plot/marks/frame) can be used to the same effect.

## hexgrid( _options_) [​](https://observablehq.com/plot/marks/hexgrid\#hexgrid)

js

```
Plot.hexgrid({stroke: "red"})
```

Returns a new hexgrid mark with the specified _options_.

Pager

[Previous pageGrid](https://observablehq.com/plot/marks/grid)

[Next pageImage](https://observablehq.com/plot/marks/image)

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

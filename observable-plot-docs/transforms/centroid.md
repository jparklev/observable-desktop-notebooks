---
url: "https://observablehq.com/plot/transforms/centroid"
title: "Centroid transform | Plot"
---

# Centroid transform [^0.6.2](https://github.com/observablehq/plot/releases/tag/v0.6.2 "added in v0.6.2") [​](https://observablehq.com/plot/transforms/centroid\#centroid-transform)

Plot offers two transforms that derive centroids from GeoJSON geometries: [centroid](https://observablehq.com/plot/transforms/centroid#centroid) and [geoCentroid](https://observablehq.com/plot/transforms/centroid#geoCentroid). These transforms can be used by any mark that accepts **x** and **y** channels. Below, a [text mark](https://observablehq.com/plot/marks/text) labels the U.S. states.

ArizonaLouisianaIdahoMinnesotaNorth DakotaSouth DakotaNew YorkAlaskaGeorgiaIndianaMichiganMississippiOhioTexasNebraskaColoradoMarylandKansasIllinoisWisconsinCaliforniaIowaPennsylvaniaMontanaMissouriFloridaKentuckyMaineUtahOklahomaTennesseeOregonWest VirginiaArkansasWashingtonNorth CarolinaVirginiaWyomingAlabamaSouth CarolinaNew MexicoNew HampshireVermontNevadaHawaiiMassachusettsRhode IslandNew JerseyDelawareConnecticutDistrict of Columbia [Fork](https://observablehq.com/@observablehq/plot-state-labels "Open on Observable")

js

```
Plot.plot({
  projection: "albers-usa",
  marks: [\
    Plot.geo(statemesh),\
    Plot.text(states, Plot.centroid({text: (d) => d.properties.name, fill: "currentColor", stroke: "white"}))\
  ]
})
```

For fun, we can pass county centroids to the [voronoi mark](https://observablehq.com/plot/marks/delaunay).

[Fork](https://observablehq.com/@observablehq/plot-centroid-voronoi "Open on Observable")

js

```
Plot.voronoi(counties, Plot.centroid()).plot({projection: "albers"})
```

While the centroid transform computes the centroid of a geometry _after_ projection, the geoCentroid transform computes it _before_ projection, then projects the resulting coordinates. This difference has a few implications, as follows.

As an [initializer](https://observablehq.com/plot/features/transforms#custom-initializers), the centroid transform operates _after_ the geometries have been projected to screen coordinates. The resulting **x** and **y** channels reference the pixel coordinates of the planar centroid of the _projected_ shapes. No assumption is made about the geometries: they can be in any coordinate system, and the returned value is in the frame — as long as the projected geometry returns at least one visible point.

[Fork](https://observablehq.com/@observablehq/plot-centroid-dot "Open on Observable")

js

```
Plot.dot(counties, Plot.centroid()).plot({projection: "albers-usa"})
```

The geoCentroid transform is more specialized as the **x** and **y** channels it derives represent the longitudes and latitudes of the centroids of the given GeoJSON geometries, before projection. It expects the geometries to be specified in _spherical_ coordinates. It is more correct, in a geospatial sense — for example, the spherical centroid always represents the center of mass of the original shape, and it will be rotated exactly in line with the projection’s rotate argument. However, this also means that it might land outside the frame if only a part of the land mass is visible, and might be clipped by the projection. In practice, the difference is generally imperceptible.

[Fork](https://observablehq.com/@observablehq/plot-centroid-dot "Open on Observable")

js

```
Plot.dot(counties, Plot.geoCentroid()).plot({projection: "albers-usa"})
```

The geoCentroid transform is slightly faster than the centroid initializer — which might be useful if you have tens of thousands of features and want to show their density on a [hexbin map](https://observablehq.com/plot/transforms/hexbin):

[Fork](https://observablehq.com/@observablehq/plot-centroid-hexbin "Open on Observable")

js

```
Plot.dot(counties, Plot.hexbin({r:"count"}, Plot.geoCentroid())).plot({projection: "albers"})
```

Combined with the [pointer transform](https://observablehq.com/plot/interactions/pointer), the centroid transform can add [interactive tips](https://observablehq.com/plot/marks/tip) on a map:

[Fork](https://observablehq.com/@observablehq/plot-state-centroids "Open on Observable")

js

```
Plot.plot({
  projection: "albers-usa",
  marks: [\
    Plot.geo(statemesh, {strokeOpacity: 0.2}),\
    Plot.geo(nation),\
    Plot.dot(states, Plot.centroid({fill: "red", stroke: "white"})),\
    Plot.tip(states, Plot.pointer(Plot.centroid({title: (d) => d.properties.name})))\
  ]
})
```

## centroid( _options_) [​](https://observablehq.com/plot/transforms/centroid\#centroid)

js

```
Plot.centroid({geometry: Plot.identity})
```

The centroid initializer derives **x** and **y** channels representing the planar (projected) centroids for the given GeoJSON geometry. If the **geometry** option is not specified, the mark’s data is assumed to be GeoJSON objects.

## geoCentroid( _options_) [​](https://observablehq.com/plot/transforms/centroid\#geoCentroid)

js

```
Plot.geoCentroid({geometry: Plot.identity})
```

The geoCentroid transform derives **x** and **y** channels representing the spherical centroids for the given GeoJSON geometry. If the **geometry** option is not specified, the mark’s data is assumed to be GeoJSON objects.

Pager

[Previous pageBin](https://observablehq.com/plot/transforms/bin)

[Next pageDodge](https://observablehq.com/plot/transforms/dodge)

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

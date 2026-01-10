---
url: "https://observablehq.com/framework/lib/topojson"
title: "TopoJSON | Observable Framework"
---

# [TopoJSON](https://observablehq.com/framework/lib/topojson\#topo-json)

[TopoJSON](https://github.com/topojson/topojson) is an extension of [GeoJSON](https://geojson.org/), a format for encoding geometry and geographic data structures, that further encodes topology. The [TopoJSON client](https://github.com/topojson/topojson-client) library allows you to transform compact TopoJSON files to GeoJSON and display a map with — for instance — [Leaflet](https://observablehq.com/framework/lib/leaflet), [D3](https://observablehq.com/framework/lib/d3), or [Observable Plot](https://observablehq.com/framework/lib/plot). The TopoJSON client library is available in Markdown as `topojson`, but you can also import it like so:

```js
import * as topojson from "npm:topojson-client";
```

To demonstrate, let’s load a file that describes the counties, states and general outline of the United States, already projected using [Albers’ equal area-conic projection](https://d3js.org/d3-geo/conic#geoAlbersUsa) to a frame of 975×610 pixels:

```js
const us = FileAttachment("counties-albers-10m.json").json();
```

Object {type: "Topology", bbox: Array(4), transform: Object, objects: Object, arcs: Array(9462)}

```js
us
```

We can then create a GeoJSON object for each feature we want to display. First, the general outline of the nation:

```js
const nation = topojson.feature(us, us.objects.nation);
```

Object {type: "FeatureCollection", features: Array(1)}

```js
nation
```

The counties mesh, which includes each of the delimitations once (instead of once per county). This avoids an additional stroke on the perimeter of the map, which would otherwise mask intricate features such as islands and inlets.

```js
const countiesmesh = topojson.mesh(us, us.objects.counties);
```

Object {type: "MultiLineString", coordinates: Array(3214)}

```js
countiesmesh
```

The _statemesh_ likewise contains the internal borders between states, _i.e._, everything but the coastlines and country borders.

```js
const statemesh = topojson.mesh(us, us.objects.states, (a, b) => a !== b)
```

Object {type: "MultiLineString", coordinates: Array(59)}

```js
statemesh
```

Putting it together as a map using [Observable Plot](https://observablehq.com/framework/lib/plot):

```js
Plot.plot({
  projection: "identity",
  width: 975,
  height: 610,
  marks: [\
    Plot.geo(countiesmesh, {strokeOpacity: 0.5}),\
    Plot.geo(statemesh, {strokeWidth: 0.75}),\
    Plot.geo(nation, {strokeWidth: 1.5})\
  ]
})
```

If you need to manipulate topologies, for example to simplify the shapes on-the-fly, you may need to import the [TopoJSON server](https://github.com/topojson/topojson-server) and [TopoJSON simplify](https://github.com/topojson/topojson-simplify) libraries, too.

```js
import {topology} from "npm:topojson-server";
import {presimplify, simplify} from "npm:topojson-simplify";
```

For more details, please refer to the [TopoJSON documentation](https://github.com/topojson).

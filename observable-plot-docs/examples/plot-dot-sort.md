---
url: "https://observablehq.com/@observablehq/plot-dot-sort"
title: "Bubble map"
---

# Bubble map

By default, [dots](https://observablehq.com/plot/marks/dot) are sorted by descending radius. Toggle the checkbox to draw the dots in input order with sort: null.

```js
viewof sorted = Inputs.toggle({value: true, label: "Use default sort"})
```

```js
Plot.plot({
  projection: "albers-usa",
  marks: [
    Plot.geo(statemesh, {strokeOpacity: 0.4}),
    Plot.dot(counties, Plot.geoCentroid({
      r: (d) => d.properties.population,
      fill: "currentColor",
      stroke: "white",
      strokeWidth: 1,
      sort: sorted
        ? {channel: "r", order: "descending"} // explicitly sort “by descending radius”, which is the default
        : null // draw points in input order
    }))
  ]
})
```

```js
us = FileAttachment("us-counties-10m.json").json()
```

```js
statemesh = topojson.mesh(us, us.objects.states)
```

The cell below joins the counties geographies with the population data; see our [tutorial](https://observablehq.com/@observablehq/build-your-first-choropleth-map-with-observable-plot) for more details.

```js
counties = {
  const counties = topojson.feature(us, us.objects.counties);
  const pop = await FileAttachment("us-county-population.csv").csv();
  const map = new Map(pop.map((d) => [`${d.state}${d.county}`, +d.population]));
  counties.features.forEach((g) => {
    g.properties.population = map.get(g.id);
  });
  return counties.features;
}
```

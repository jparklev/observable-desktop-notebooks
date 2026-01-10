---
url: "https://observablehq.com/@observablehq/observable-plot-grid-choropleth"
title: "Grid choropleth"
---

# Grid choropleth

This grid choropleth created in [Observable Plot](https://observablehq.com/@observablehq/plot) shows the population change in each state (and DC) in the United States between 2019 and 2010. A grid map, shown here using the [cell mark](https://observablehq.com/plot/marks/cell) makes each state the same size shape while keeping the states roughly aligned geographically. The diverging-log color scale with the green/pink scheme indicates if the state is increasing or decreasing in population, with darker colors representing a larger change.

```js
Plot.plot({
  height: 420,
  axis: null,
  color: {
    type: "diverging-log", // diverging-log scales pivot at 1 by default
    scheme: "piyg"
  },
  marks: [
    Plot.cell(states, {x: "x", y: "y", fill: change}),
    Plot.text(states, {x: "x", y: "y", text: "key", dy: -2}), // state abbr
    Plot.text(states, {x: "x", y: "y", text: formatChange, dy: 10, fillOpacity: 0.6})
  ]
})
```

### US Grid & Data

```js
grid = FileAttachment("grid.csv").csv({ typed: true })
  .then((states) => new Map(states.map((state) => [state.name, state])))
```

```js
population = FileAttachment("population.csv").csv({typed: true})
```

```js
states = population
  .filter((d) => grid.has(d.State))
  .map((d) => ({ ...d, ...grid.get(d.State) }))
```

```js
change = d => d["2019"] / d["2010"]
```

```js
formatChange = ((f) => (d) => f(change(d) - 1))(d3.format("+.0%"))
```

*Thank you to [@severo](https://observablehq.com/@severo) for [Quality Criteria for Existing Gridmaps](https://observablehq.com/@severo/quality-criteria-for-existing-grid-maps), to Krist Wongsuphasawat for his [analysis](https://kristw.medium.com/whose-grid-map-is-better-quality-metrics-for-grid-map-layouts-e3d6075d9e80), and to the New York Times for their grid map layout.*

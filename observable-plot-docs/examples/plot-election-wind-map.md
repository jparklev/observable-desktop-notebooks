---
url: "https://observablehq.com/@observablehq/plot-election-wind-map"
title: "Election wind map"
---

# Election wind map

A map where the margin by which the winner of the US presidential election of 2020 won the vote in each county is represented as a non-gridded [wind map](https://observablehq.com/@observablehq/plot-wind-map). The length of the [vector](https://observablehq.com/plot/marks/vector) encodes the difference in votes for the Democratic candidate vs the Republican candidate , with color and direction both showing who won.

```js
Plot.plot({
  projection: "albers-usa",
  length: {type: "sqrt", transform: Math.abs},
  marks: [
    Plot.geo(statemesh, {strokeWidth: 0.5}),
    Plot.geo(nation),
    Plot.vector(
      counties,
      Plot.centroid({
        anchor: "start",
        length: (d) => d.properties.margin2020 * d.properties.votes,
        stroke: (d) => d.properties.margin2020 > 0 ? "red" : "blue",
        rotate: (d) => d.properties.margin2020 > 0 ? 60 : -60
      })
    )
  ]
})
```

```js
counties = {
  const counties = topojson.feature(us, us.objects.counties).features;
  const _election = new Map(election.map((d) => [d.fips, d]));
  counties.forEach(county => {
    county.properties.margin2020 = +_election.get(county.id)?.margin2020;
    county.properties.votes = +_election.get(county.id)?.votes;
  });
  return counties;
}
```

```js
statemesh = topojson.mesh(us, us.objects.states)
```

```js
nation = topojson.feature(us, us.objects.nation)
```

```js
election = FileAttachment("us-presidential-election-2020.csv").csv()
```

```js
us = FileAttachment("us-counties-10m.json").json()
```

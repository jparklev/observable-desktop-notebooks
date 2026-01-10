---
url: "https://observablehq.com/@observablehq/plot-ridgeline"
title: "Ridgeline Plot"
---

# Ridgeline Plot

Ridgeline plots are an alternative to [horizon charts](/@observablehq/plot-horizon) and small-multiple area charts that allow greater precision for a given vertical space at the expense of occlusion (overlapping areas). See also the [D3 version](/@d3/ridgeline-plot). Data: [Christopher Möller](https://gist.github.com/chrtze/c74efb46cadb6a908bbbf5227934bfea).

```js
viewof overlap = Inputs.range([0, 9], {step: 0.1, label: "Overlap"})
```

```js
chart = Plot.plot({
  height: 40 + new Set(traffic.map(d => d.name)).size * 17,
  width,
  marginBottom: 1,
  marginLeft: 120,
  x: {axis: "top"},
  y: {axis: null, range: [2.5 * 17 - 2, (2.5 - overlap) * 17 - 2]},
  fy: {label: null, domain: traffic.map(d => d.name)}, // preserve input order
  marks: [
    d3.groups(traffic, d => d.name).map(([, values]) => [
      Plot.areaY(values, {x: "date", y: "value", fy: "name", curve: "basis", sort: "date", fill: "#ccc"}),
      Plot.lineY(values, {x: "date", y: "value", fy: "name", curve: "basis", sort: "date", strokeWidth: 1})
    ])
  ]
})
```

```js
traffic = FileAttachment("traffic.csv").csv({typed: true})
```

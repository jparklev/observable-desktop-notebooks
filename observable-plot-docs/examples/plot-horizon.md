---
url: "https://observablehq.com/@observablehq/plot-horizon"
title: "Horizon Chart"
---

# Horizon Chart

Horizon charts are an alternative to [ridgeline plots](/@observablehq/plot-ridgeline) and small-multiple area charts that allow greater precision for a given vertical space by using colored bands. These charts can be used with diverging color scales to differentiate positive and negative values. See also the [D3 version](/@d3/horizon-chart/2). Data: [Christopher Möller](https://gist.github.com/chrtze/c74efb46cadb6a908bbbf5227934bfea).

```js
viewof bands = Inputs.range([2, 8], {step: 1, label: "Bands"})
```

```js
chart = Plot.plot({
  height: 1100,
  width: 928,
  x: {axis: "top"},
  y: {domain: [0, step], axis: null},
  fy: {axis: null, domain: traffic.map((d) => d.name), padding: 0.05},
  color: {
    type: "ordinal",
    scheme: "Greens",
    label: "Vehicles per hour",
    tickFormat: (i) => ((i + 1) * step).toLocaleString("en"),
    legend: true
  },
  marks: [
    d3.range(bands).map((band) => Plot.areaY(traffic, {x: "date", y: (d) => d.value - band * step, fy: "name", fill: band, sort: "date", clip: true})),
    Plot.axisFy({frameAnchor: "left", dx: -28, fill: "currentColor", textStroke: "white", label: null})
  ]
})
```

```js
traffic = FileAttachment("traffic.csv").csv({typed: true})
```

```js
step = +(d3.max(traffic, (d) => d.value) / bands).toPrecision(2)
```

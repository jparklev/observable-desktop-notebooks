---
url: "https://observablehq.com/@observablehq/plot-stack-offset"
title: "Wiggle streamgraph"
---

# Wiggle streamgraph

The *wiggle* **offset** translates [stacks](https://observablehq.com/plot/transforms/stack#stack-options) to minimize apparent movement. It is recommended for streamgraphs, and if used, changes the default **order** to inside-out; see [Byron & Wattenberg](http://leebyron.com/streamgraph/).

```js
viewof offset = Inputs.select(
  new Map([
    ["null", null],
    ["center", "center"],
    ["wiggle", "wiggle"]
  ]),
  { label: "offset", value: "wiggle" }
)
```

```js
Plot.plot({
  y: {
    grid: true,
    label: "↑ Annual revenue (billions, adj.)",
    transform: (d) => d / 1000
  },
  marks: [
    Plot.areaY(riaa, {x: "year", y: "revenue", z: "format", fill: "group", offset})
  ]
})
```

```js
riaa = FileAttachment("riaa-us-revenue.csv").csv({typed: true})
```

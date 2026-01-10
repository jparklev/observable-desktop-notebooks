---
url: "https://observablehq.com/@observablehq/plot-normalized-stack"
title: "Normalized stack"
---

# Normalized stack

Use the *normalize* **offset** to rescale each [stack](https://observablehq.com/plot/transforms/stack#stack-options) to fill [0, 1]. Percentages are shown with the scale’s [percent](https://observablehq.com/plot/features/scales#scale-transforms) option.

```js
Plot.plot({
  y: {
    label: "↑ Annual revenue (%)",
    percent: true
  },
  marks: [
    Plot.areaY(riaa, Plot.stackY({offset: "normalize", order: "group", reverse: true}, {x: "year", y: "revenue", z: "format", fill: "group"})),
    Plot.ruleY([0, 1])
  ]
})
```

```js
riaa = FileAttachment("riaa-us-revenue.csv").csv({typed: true})
```

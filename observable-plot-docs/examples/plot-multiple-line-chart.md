---
url: "https://observablehq.com/@observablehq/plot-multiple-line-chart"
title: "Multiple line chart"
---

# Multiple line chart

Use the **z** channel (or **stroke**, or **fill**) to group [tidy data](https://r4ds.had.co.nz/tidy-data.html) into series and create multiple lines.

```js
Plot.plot({
  y: {
    grid: true,
    label: "↑ Unemployment (%)"
  },
  marks: [
    Plot.ruleY([0]),
    Plot.lineY(bls, {x: "date", y: "unemployment", z: "division"})
  ]
})
```

```js
bls = FileAttachment("bls-metro-unemployment.csv").csv({typed: true})
```

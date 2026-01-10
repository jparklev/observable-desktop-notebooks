---
url: "https://observablehq.com/@observablehq/plot-area-chart-missing-data"
title: "Area chart, missing data"
---

# Area chart, missing data

The [area mark](/plot/marks/area), in blue, shows gaps for missing data—points where the value is NaN, undefined, or Infinite. A second area, in grey, has these data points filtered out altogether, resulting instead in linear interpolation for the gaps.

```js
Plot.plot({
  y: {grid: true, label: "Daily close ($)"},
  marks: [
    Plot.areaY(aaplMissing, {filter: (d) => !isNaN(d.Close), x: "Date", y1: "Close", fill: "#ccc"}),
    Plot.areaY(aaplMissing, {x: "Date", y1: "Close", fill: "steelblue"}),
    Plot.ruleY([0]),
  ]
})
```

```js
aaplMissing = aapl.map(d => ({...d, Close: d.Date.getUTCMonth() < 3 ? NaN : d.Close})) // simulate gaps
```

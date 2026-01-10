---
url: "https://observablehq.com/@observablehq/plot-sorted-heatmap"
title: "Sorted heatmap"
---

# Sorted heatmap

[Grouping](https://observablehq.com/plot/transforms/group) by *x* (hour of day) and *y* (location) produces a heatmap. Locations are [sorted](https://observablehq.com/plot/features/scales#sort-mark-option) by the maximum highway traffic (measured as vehicles per hour) they have during the day. Data: [Christopher Möller](https://gist.github.com/chrtze).

```js
Plot.plot({
  marginLeft: 120,
  padding: 0,
  y: {label: null},
  color: {legend: true, zero: true},
  marks: [
    Plot.cell(
      traffic,
      Plot.group(
        {fill: "median"},
        {x: (d) => d.date.getUTCHours(), y: "location", fill: "vehicles", inset: 0.5, sort: {y: "fill"}}
      )
    )
  ]
})
```

```js
traffic = FileAttachment("traffic.csv").csv({typed: true})
```

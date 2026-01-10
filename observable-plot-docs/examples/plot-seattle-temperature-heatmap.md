---
url: "https://observablehq.com/@observablehq/plot-seattle-temperature-heatmap"
title: "Seattle temperature temporal heatmap"
---

# Seattle temperature temporal heatmap

A calendar with a [cell](https://observablehq.com/plot/marks/cell) for each day (*x*) of each month (*y*), [colored](https://observablehq.com/plot/features/scales#color-scales) by maximum temperature on that day.

```js
Plot.plot({
  padding: 0,
  y: {tickFormat: Plot.formatMonth("en", "short")},
  marks: [
    Plot.cell(seattle, Plot.group({fill: "max"}, {
      x: (d) => d.date.getUTCDate(),
      y: (d) => d.date.getUTCMonth(),
      fill: "temp_max",
      inset: 0.5
    }))
  ]
})
```

```js
seattle = FileAttachment("seattle-weather.csv").csv({ typed: true })
```

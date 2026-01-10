---
url: "https://observablehq.com/@observablehq/plot-line-chart-with-markers"
title: "Line chart with markers"
---

# Line chart with markers

Use [markers](https://observablehq.com/plot/features/markers) to indicate the data points that are interpolated by the [line](https://observablehq.com/plot/marks/line) mark.

```js
Plot.plot({
  marks: [
    Plot.ruleY([0]),
    Plot.lineY(crimea, {x: "date", y: "deaths", stroke: "cause", marker: true})
  ]
})
```

```js
crimea = {
  const data = await FileAttachment("crimean-war.csv").csv({typed: true});
  return data.columns.slice(2).flatMap((cause) => data.map(({date, [cause]: deaths}) => ({date, cause, deaths}))); // pivot taller
}
```

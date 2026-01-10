---
url: "https://observablehq.com/@observablehq/plot-stacked-waffles"
title: "Stacked waffles"
---

# Stacked waffles

Like the bar and rect marks, the [waffle mark](https://observablehq.com/plot/marks/waffle) supports implicit stacking.

```js
Plot.waffleY(olympians, Plot.groupZ(
  {y: "sum"},
  {fill: "sex", y: d => d.sex === "female" ? 1 : -1, sort: "sex", fx: "weight", unit: 10}
)).plot({fx: {interval: 10}, color: {legend: true}})
```

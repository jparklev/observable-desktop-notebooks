---
url: "https://observablehq.com/@observablehq/plot-crosshair"
title: "Crosshair"
---

# Crosshair

The [crosshair mark](https://observablehq.com/plot/interactions/crosshair) uses the [pointer transform](https://observablehq.com/plot/interactions/pointer) internally to display a [rule](https://observablehq.com/plot/marks/rule) and a [text](https://observablehq.com/plot/marks/text) showing the **x** (horizontal↔︎ position) and **y** (vertical↕︎ position) value of the nearest data.

```js
Plot.plot({
  marks: [
    Plot.dot(olympians, {x: "weight", y: "height", stroke: "sex"}),
    Plot.crosshair(olympians, {x: "weight", y: "height"})
  ]
})
```

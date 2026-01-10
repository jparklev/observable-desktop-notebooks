---
url: "https://observablehq.com/@observablehq/plot-random-walk"
title: "Random walk"
---

# Random walk

This [map transform](https://observablehq.com/plot/transforms/map) computes a cumulative sum (_cumsum_) of the values. Applied to a [random number generator](https://observablehq.com/@d3/d3-random#normal), this generates a random walk. Brownian movement in a single line of code!

```js
Plot.plot({
  marks: [
    Plot.ruleY([0]),
    Plot.lineY({length: 10000}, Plot.mapY("cumsum", {y: d3.randomNormal()}))
  ]
})
```

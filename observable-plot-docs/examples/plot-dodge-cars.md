---
url: "https://observablehq.com/@observablehq/plot-dodge-cars"
title: "Dodge cars (beeswarm)"
---

# Dodge cars (beeswarm)

The [dodge](https://observablehq.com/plot/transforms/dodge) transform helps to create a beeswarm chart.

```js
viewof anchor = Inputs.select([null, "top", "middle", "bottom"], {label: "anchor"})
```

```js
Plot.plot({
  height: 160,
  marks: [
    Plot.dotX(cars, Plot.dodgeY({x: "weight (lb)", title: "name", fill: "currentColor", anchor: anchor ?? undefined}))
  ]
})
```

For comparison, here are a few other ways to display the same data:

```js
Plot.plot({
  height: 180,
  marks: [
    Plot.rectY(cars, Plot.binX({y: "count"}, {x: "weight (lb)"})),
    Plot.ruleY([0])
  ]
})
```

```js
Plot.dotX(cars, {x: "weight (lb)"}).plot()
```

```js
Plot.ruleX(cars, {x: "weight (lb)"}).plot()
```

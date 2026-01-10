---
url: "https://observablehq.com/@observablehq/plot-density-weighted"
title: "Density skew (weight) interactive"
---

# Density skew (weight) interactive

Using a variable weight, we can make the [density](https://observablehq.com/plot/marks/density) mark progressively ignore some points and take others into account.

```js
viewof skew = Inputs.range([-1, 1], {label: "skew (-F/+M)", step: 0.01})
```

```js
Plot.plot({
  inset: 10,
  color: {legend: true},
  marks: [
    Plot.density(penguins.filter((d) => d.sex), {
      weight: (d) => d.sex === "FEMALE" ? 1 - skew : 1 + skew,
      x: "flipper_length_mm",
      y: "culmen_length_mm",
      strokeOpacity: 0.5,
      clip: true
    }),
    Plot.dot(penguins.filter((d) => d.sex), {
      x: "flipper_length_mm",
      y: "culmen_length_mm",
      stroke: "sex",
      strokeOpacity: (d) => d.sex === "FEMALE" ? 1 - skew : 1 + skew
    }),
    Plot.frame()
  ]
})
```

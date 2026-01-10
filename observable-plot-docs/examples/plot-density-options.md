---
url: "https://observablehq.com/@observablehq/plot-density-options"
title: "Density options"
---

# Density options

An interactive demo of the main options for the [density](https://observablehq.com/plot/marks/density) mark.

```js
viewof bandwidth= Inputs.range([0, 40], {step: 0.2, label: "bandwidth"})
```

```js
viewof thresholds = Inputs.range([1, 40], {
  step: 1,
  value: 20,
  label: "thresholds"
})
```

```js
Plot.plot({
  inset: 20,
  marks: [
    Plot.density(faithful, {x: "waiting", y: "eruptions", bandwidth, thresholds}),
    Plot.dot(faithful, {x: "waiting", y: "eruptions"})
  ]
})
```

```js
faithful = FileAttachment("faithful.tsv").tsv({typed: true})
```

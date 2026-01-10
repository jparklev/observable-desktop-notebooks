---
url: "https://observablehq.com/@observablehq/plot-highlighted-bin"
title: "Highlighted bin"
---

# Highlighted bin

A custom [function reducer](https://observablehq.com/plot/transforms/bin#bin-transform) that tests if [Aaron Brown](https://en.wikipedia.org/wiki/Aaron_Brown_(sprinter%29) belongs to a given bin.

```js
Plot.plot({
  y: {
    grid: true
  },
  marks: [
    Plot.rectY(
      olympians,
      Plot.binX(
        {
          y: "count",
          fill: test
        },
        { x: "weight" }
      )
    ),
    Plot.ruleY([0])
  ]
})
```

In this example we highlight the bin that has a certain athlete.

```js
test = (bin) => bin.some((d) => d.name === "Aaron Brown")
```

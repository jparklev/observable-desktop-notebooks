---
url: "https://observablehq.com/@observablehq/plot-image-scatterplot-2"
title: "Default image scatterplot"
---

# Default image scatterplot

The default size of the [image](https://observablehq.com/plot/marks/image) mark is only 16×16 pixels. Data: [YouGov](https://today.yougov.com/topics/politics/articles-reports/2021/07/27/most-and-least-popular-us-presidents-according-ame)

```js
Plot.plot({
  aspectRatio: 1,
  grid: true,
  x: {label: "Favorable opinion (%) →"},
  y: {label: "↑ Unfavorable opinion (%)"},
  marks: [
    Plot.ruleY([0]),
    Plot.ruleX([0]),
    Plot.image(presidents, {
      x: (d) => d["Very Favorable %"] + d["Somewhat Favorable %"],
      y: (d) => d["Very Unfavorable %"] + d["Somewhat Unfavorable %"],
      src: "Portrait URL",
      title: "Name"
    })
  ]
})
```

```js
presidents = FileAttachment("us-president-favorability@2.csv").csv({typed: true})
```

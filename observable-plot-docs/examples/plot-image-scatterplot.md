---
url: "https://observablehq.com/@observablehq/plot-image-scatterplot"
title: "Image scatterplot"
---

# Image scatterplot

Showing the net favorability of past presidents among people today using the [image](https://observablehq.com/plot/marks/image) mark. Data from [YouGov](https://today.yougov.com/topics/politics/articles-reports/2021/07/27/most-and-least-popular-us-presidents-according-ame); inspired by [Robert Lesser](https://observablehq.com/@rlesser/when-presidents-fade-away).

```js
Plot.plot({
  inset: 20,
  x: {label: "First inauguration date →"},
  y: {grid: true, label: "↑ Net favorability (%)", tickFormat: "+f"},
  marks: [
    Plot.ruleY([0]),
    Plot.image(presidents, {
      x: "First Inauguration Date",
      y: (d) => d["Very Favorable %"] + d["Somewhat Favorable %"] - d["Very Unfavorable %"] - d["Somewhat Unfavorable %"],
      src: "Portrait URL",
      width: 40,
      title: "Name"
    })
  ]
})
```

```js
presidents = FileAttachment("us-president-favorability@1.csv").csv({typed: true})
```

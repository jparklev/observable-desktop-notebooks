---
url: "https://observablehq.com/@observablehq/plot-image-dodge"
title: "Image beeswarm"
---

# Image beeswarm

(dodge) The [image](https://observablehq.com/plot/marks/image) mark supports the *r* option, and can be used with the [dodge](https://observablehq.com/plot/transforms/dodge) transform. data: [YouGov](https://today.yougov.com/topics/politics/articles-reports/2021/07/27/most-and-least-popular-us-presidents-according-ame)

```js
Plot.plot({
  inset: 20,
  height: 280,
  marks: [
    Plot.image(
      presidents,
      Plot.dodgeY({
        x: "First Inauguration Date",
        r: 20, // clip to a circle
        preserveAspectRatio: "xMidYMin slice", // try not to clip heads
        src: "Portrait URL",
        title: "Name"
      })
    )
  ]
})
```

```js
presidents = FileAttachment("us-president-favorability@2.csv").csv({typed: true})
```

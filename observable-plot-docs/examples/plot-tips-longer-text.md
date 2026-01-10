---
url: "https://observablehq.com/@observablehq/plot-tips-longer-text"
title: "Interactive tips with longer text"
---

# Interactive tips with longer text

The [tip mark](https://observablehq.com/plot/marks/tip) supports the **title** channel for longer texts.

```js
Plot.plot({
  grid: true,
  marks: [
    Plot.dot(olympians, {
      x: "weight",
      y: "height",
      fy: "sex",
      sort: (d) => !!d.info,
      stroke: (d) => d.info ? "currentColor" : "#aaa"
    }),
    Plot.tip(olympians, Plot.pointer({
      x: "weight",
      y: "height",
      fy: "sex",
      filter: (d) => d.info,
      title: (d) => [d.name, d.info].join("\n\n")
    }))
  ]
})
```

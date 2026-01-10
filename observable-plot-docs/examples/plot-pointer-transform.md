---
url: "https://observablehq.com/@observablehq/plot-pointer-transform"
title: "Pointer transform"
---

# Pointer transform

The [pointer transform](https://observablehq.com/plot/interactions/pointer) is not limited to the [tip mark](https://observablehq.com/plot/marks/tip). Below, it is used to filter a filled red dot behind a stroked black dot. As you hover the chart, only the closest red dot to the pointer is rendered. If you remove the pointer transform by toggling the checkbox, all the red dots will be visible.

```js
viewof pointered = Inputs.toggle({label: "Use pointer", value: true})
```

```js
Plot.plot({
  marks: [
    Plot.dot(
      penguins,
      pointered
        ? Plot.pointer({
            x: "culmen_length_mm",
            y: "culmen_depth_mm",
            fill: "red",
            r: 8
          })
        : {x: "culmen_length_mm", y: "culmen_depth_mm", fill: "red", r: 8}
    ),
    Plot.dot(penguins, {x: "culmen_length_mm", y: "culmen_depth_mm"})
  ]
})
```

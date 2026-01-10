---
url: "https://observablehq.com/@observablehq/plot-burndown-chart"
title: "Burndown chart"
---

# Burndown chart

Ref. https://observablehq.com/@tmcw/github-burndown

```js
Plot.plot({
  width,
  height: 600,
  x: {label: null},
  color: {legend: true, label: "Opened"},
  marks: [
    Plot.areaY(
      issues.flatMap((i) =>
        d3
          .utcDays(i.created_at, i.closed_at ?? new Date("2024-10-18"))
          .map((at) => ({created_at: i.created_at, at}))
      ),
      Plot.binX(
        {y: "count", filter: null},
        {
          x: "at",
          fill: (d) => d3.utcWeek(d.created_at),
          reverse: true,
          curve: "step",
          tip: {format: {x: null, z: null}},
          interval: "day"
        }
      )
    )
  ]
})
```

```js
issues = FileAttachment("framework-issues.json")
  .text()
  .then((text) => JSON.parse(text, (key, value) => /_at$/.test(key) && value ? new Date(value) : value))
```

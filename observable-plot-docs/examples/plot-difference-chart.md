---
url: "https://observablehq.com/@observablehq/plot-difference-chart"
title: "Difference chart"
---

# Difference chart

A difference chart highlights the difference between two values, typically entries vs exits. The amount is encoded as height, and the sign (surplus vs. deficit) as a solid color. In the chart below, we compare the temperatures on the same day; days when San Francisco was warmer are orange , and colder days are blue .

```js
chart = Plot.plot({
  width: 928,
  height: 550,
  x: { inset: 4 },
  y: { grid: true, label: "temperature (°F)" },
  color: { scheme: "RdYlBu", label: "colder" },
  marks: [
    Plot.differenceY(weather, {
      x: "date",
      y1: "New York",
      y2: "San Francisco",
      curve: "step-after",
      positiveFill: () => "NY",
      negativeFill: () => "SF",
      tip: true
    }),
    Plot.text(
      weather,
      Plot.selectMaxY({
        x: "date",
        y: "New York",
        text: () => "New York",
        dy: -6
      })
    ),
    Plot.text(weather, {
      ...Plot.selectMaxY({
        x: "date",
        y: "New York"
      }),
      y: "San Francisco",
      text: () => "San Francisco",
      dy: 13
    }),
    Plot.text(
      weather,
      Plot.selectMinY({
        x: "date",
        y: "New York",
        text: () => "New York",
        textAnchor: "start",
        dy: -10,
        dx: 6
      })
    ),
    Plot.text(weather, {
      ...Plot.selectMinY({
        x: "date",
        y: "New York",
        text: () => "San Francisco"
      }),
      y: "San Francisco",
      dy: -40
    })
  ]
})
```

```js
weather = FileAttachment("weather.tsv").tsv({typed: true})
  .then(l => l.map(d => ({...d, date: d3.utcParse("%Y%m%d")(`${d.date}`)})))
```

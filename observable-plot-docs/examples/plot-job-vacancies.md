---
url: "https://observablehq.com/@observablehq/plot-job-vacancies"
title: "Job vacancies"
---

# Job vacancies

This area chart uses an [interval](https://observablehq.com/plot/transforms/interval) transform to avoid interpolation for the values missing in the original dataset. Data: [Australian Bureau of Statistics](https://www.abs.gov.au/statistics/labour/jobs/job-vacancies-australia/may-2022), 30 June 2022.

```js
Plot.plot({
  width,
  y: { label: "↑ Job vacancies, seasonally adj. (thousands)", grid: true },
  marks: [
    Plot.areaY(vacancies, {
      x: "month",
      y: "vacancies",
      curve: "step-before",
      interval: "quarter",
      fill: "pink"
    }),
    Plot.lineY(vacancies, {
      x: "month",
      y: "vacancies",
      curve: "step-before",
      interval: "quarter"
    }),
    Plot.ruleY([0])
  ]
})
```

```js
vacancies = FileAttachment("vacancies.csv").csv({typed: true})
```

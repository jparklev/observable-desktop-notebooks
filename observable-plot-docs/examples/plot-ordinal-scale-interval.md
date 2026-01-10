---
url: "https://observablehq.com/@observablehq/plot-ordinal-scale-interval"
title: "Ordinal scale interval"
---

# Ordinal scale interval

Use the [interval scale option](https://observablehq.com/plot/features/scales#interval) to make sure that missing data is not invisibly skipped. See also [a variant for time scales](https://observablehq.com/@observablehq/plot-ordinal-bar-chart).

```js
viewof checked = Inputs.toggle({label: "interval", value: true})
```

```js
Plot.barY(timeseries, {x: "year", y: "population"})
  .plot({x: {tickFormat: "", interval: checked ? 1 : undefined}})
```

```js
timeseries = [
  {year: 2014, population: 7295.290765},
  {year: 2015, population: 7379.797139},
  {year: 2016, population: 7464.022049},
  {year: 2017, population: 7547.858925},
  // {year: 2018, population: 7631.091040},
  {year: 2019, population: 7713.468100},
  {year: 2020, population: 7794.798739}
];
```

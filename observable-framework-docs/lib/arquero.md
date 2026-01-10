---
url: "https://observablehq.com/framework/lib/arquero"
title: "Arquero | Observable Framework"
---

# [Arquero](https://observablehq.com/framework/lib/arquero\#arquero)

[Arquero](https://uwdata.github.io/arquero/) is a JavaScript library for “query processing and transformation of array-backed data tables.” Arquero is available by default as `aq` in Markdown, but you can import it explicitly like so:

```js
import * as aq from "npm:arquero";
```

Following the documentation website’s [introduction](https://uwdata.github.io/arquero/), let’s create a table of the Average hours of sunshine per month, from [usclimatedata.com](https://usclimatedata.com/).

```js
const dt = aq.table({
  "Seattle": [69, 108, 178, 207, 253, 268, 312, 281, 221, 142, 72, 52],
  "Chicago": [135, 136, 187, 215, 281, 311, 318, 283, 226, 193, 113, 106],
  "San Francisco": [165, 182, 251, 281, 314, 330, 300, 272, 267, 243, 189, 156]
});
```

Arquero is column-oriented: each column is an array of values of a given type. Here, numbers representing hours of sunshine per month. But an Arquero table is also iterable and as such, its contents can be displayed with [`Inputs.table`](https://observablehq.com/framework/inputs/table).

|  | Seattle | Chicago | San Francisco |
| --- | --- | --- | --- |
|  | 69 | 135 | 165 |
|  | 108 | 136 | 182 |
|  | 178 | 187 | 251 |
|  | 207 | 215 | 281 |
|  | 253 | 281 | 314 |
|  | 268 | 311 | 330 |
|  | 312 | 318 | 300 |
|  | 281 | 283 | 272 |
|  | 221 | 226 | 267 |
|  | 142 | 193 | 243 |
|  | 72 | 113 | 189 |
|  | 52 | 106 | 156 |

```js
Inputs.table(dt)
```

An Arquero table can also be used to make charts with [Observable Plot](https://observablehq.com/framework/lib/plot):

050100150200250300↑ Hours of sunshine ☀️ per monthJanMarMayJulSepNov

```js
Plot.plot({
  x: {tickFormat: Plot.formatMonth()},
  y: {grid: true, label: "Hours of sunshine ☀️ per month"},
  marks: [\
    Plot.ruleY([0]),\
    Plot.lineY(dt, {y: "Seattle", marker: true, stroke: "red"}),\
    Plot.lineY(dt, {y: "Chicago", marker: true, stroke: "turquoise"}),\
    Plot.lineY(dt, {y: "San Francisco", marker: true, stroke: "orange"})\
  ]
})
```

Arquero supports a range of data transformation tasks, including filter, sample, aggregation, window, join, and reshaping operations. For example, the following operation derives differences between Seattle and Chicago and sorts the months accordingly.

|  | month | diff |
| --- | --- | --- |
|  | 8 | -2 |
|  | 9 | -5 |
|  | 7 | -6 |
|  | 4 | -8 |
|  | 3 | -9 |
|  | 2 | -28 |
|  | 5 | -28 |
|  | 11 | -41 |
|  | 6 | -43 |
|  | 10 | -51 |
|  | 12 | -54 |
|  | 1 | -66 |

```js
Inputs.table(
  dt.derive({
      month: (d) => aq.op.row_number(),
      diff: (d) => d.Seattle - d.Chicago
    })
    .select("month", "diff")
    .orderby(aq.desc("diff"))
)
```

Is Seattle more correlated with San Francisco or Chicago?

|  | corr\_sf | corr\_chi |
| --- | --- | --- |
|  | 0.933 | 0.978 |

```js
Inputs.table(
  dt.rollup({
    corr_sf: aq.op.corr("Seattle", "San Francisco"),
    corr_chi: aq.op.corr("Seattle", "Chicago")
  })
)
```

We can aggregate statistics per city. The following code reshapes (or “folds”) the data into two columns _city_ & _sun_ and shows the output as objects:

Array(3) \[Object, Object, Object\]

```js
dt.fold(aq.all(), {as: ["city", "sun"]})
  .groupby("city")
  .rollup({
    min: aq.op.min("sun"),
    max: aq.op.max("sun"),
    avg: (d) => aq.op.average(d.sun), // equivalent to aq.op.average("sun")
    med: (d) => aq.op.median(d.sun), // equivalent to aq.op.median("sun")
    skew: ({sun}) => (aq.op.mean(sun) - aq.op.median(sun)) / aq.op.stdev(sun)
  })
  .objects()
```

To load an Arquero table from an Apache Arrow, Apache Parquet, CSV, TSV, or JSON file, use [`file.arquero`](https://observablehq.com/framework/files#supported-formats) [Added in 1.10.0](https://github.com/observablehq/framework/releases/tag/v1.10.0 "Added in 1.10.0"):

```js
const flights = FileAttachment("flights-200k.arrow").arquero();
```

This is equivalent to:

```js
const flights = aq.loadArrow(FileAttachment("flights-200k.arrow").href);
```

For more, see [Arquero’s official documentation](https://uwdata.github.io/arquero/).

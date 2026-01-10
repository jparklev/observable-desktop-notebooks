---
url: "https://observablehq.com/@observablehq/plot-index-chart"
title: "Index chart"
---

# Index chart

A [normalize](https://observablehq.com/plot/transforms/normalize) transform is applied on the reference day, allowing comparison of stocks performance.

```js
viewof date = Scrubber(d3.union(stocks.map((d) => d.Date)), {
  format: Plot.formatIsoDate,
  initial: 500,
  loop: false,
  autoplay: false
})
```

```js
{
  const bisector = d3.bisector((i) => stocks[i].Date);
  const basis = (I, Y) => Y[I[bisector.center(I, date)]];
  return Plot.plot({
    style: "overflow: visible;",
    y: {
      type: "log",
      grid: true,
      label: "Change in price (%)",
      tickFormat: ((f) => (x) => f((x - 1) * 100))(d3.format("+d"))
    },
    marks: [
      Plot.ruleY([1]),
      Plot.ruleX([date]),
      Plot.lineY(stocks, Plot.normalizeY(basis, {
        x: "Date",
        y: "Close",
        stroke: "Symbol"
      })),
      Plot.text(stocks, Plot.selectLast(Plot.normalizeY(basis, {
        x: "Date",
        y: "Close",
        z: "Symbol",
        text: "Symbol",
        textAnchor: "start",
        dx: 3
      })))
    ]
  });
}
```

The cell below merges four CSV files, adding the symbol for each stock as the first column for each row.

```js
stocks = (await Promise.all([
  FileAttachment("aapl.csv").csv({typed: true}).then((values) => ["AAPL", values]),
  FileAttachment("amzn.csv").csv({typed: true}).then((values) => ["AMZN", values]),
  FileAttachment("goog.csv").csv({typed: true}).then((values) => ["GOOG", values]),
  FileAttachment("ibm.csv").csv({typed: true}).then((values) => ["IBM", values]),
])).flatMap(([Symbol, values]) => values.map(d => ({Symbol, ...d})))
```

```js
import {Scrubber} from "@mbostock/scrubber"
```

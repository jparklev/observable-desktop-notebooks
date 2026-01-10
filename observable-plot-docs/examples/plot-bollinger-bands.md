---
url: "https://observablehq.com/@observablehq/plot-bollinger-bands"
title: "Bollinger bands"
---

# Bollinger bands

The [bollinger mark](https://observablehq.com/plot/marks/bollinger) draws an area where the top-line (**y2**) is the mean of the *N* most recent values plus *K* times the deviation of the *N* most recent values, and the bottom-line (**y1**) is symmetrically the mean of the *N* most recent values minus *K* times the deviation of the *N* most recent values. A central line usually represents the mean of the *N* most recent values — in the cart below we cancel it by setting the **stroke** option to none, and display the actual values instead:

```js
viewof n = Inputs.range([2, 100], {step: 1, value: 20, label: "Periods (N)"})
```

```js
viewof k = Inputs.range([0, 4], {step: 0.1, value: 2, label: "Deviations (K)"})
```

```js
Plot.plot({
  y: {grid: true},
  marks: [
    Plot.bollingerY(aapl, {n, k, x: "Date", y: "Close", stroke: "none"}),
    Plot.lineY(aapl, {x: "Date", y: "Close", strokeWidth: 1})
  ]
})
```

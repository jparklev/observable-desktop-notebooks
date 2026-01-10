---
url: "https://observablehq.com/@observablehq/plot-crimean-war-bary"
title: "Crimean war casualties by cause (with barY)"
---

# Crimean war casualties by cause (with barY)

# Crimean war casualties by cause A stacked bar chart of [deaths in the Crimean War](https://en.wikipedia.org/wiki/Florence_Nightingale#Crimean_War)—predominantly from disease —using Florence Nightingale’s data. This uses the [bar](https://observablehq.com/plot/marks/bar) mark, with dates quantized by the [interval scale option](https://observablehq.com/plot/features/scales#interval)—compare with the [rect-mark](https://observablehq.com/@observablehq/plot-crimean-war-recty) variant.

```js
Plot.plot({
  x: {
    interval: "month",
    tickFormat: (d) => d.toLocaleString("en", {month: "narrow"}),
    label: null
  },
  y: {grid: true},
  marks: [
    Plot.barY(crimea, {x: "date", y: "deaths", fill: "cause"}),
    Plot.ruleY([0])
  ]
})
```

```js
crimea = {
  const data = await FileAttachment("crimean-war.csv").csv({ typed: true });
  return data.columns.slice(2)
    .flatMap((cause) => data.map(({ date, [cause]: deaths }) => ({ date, cause, deaths })));
}
```

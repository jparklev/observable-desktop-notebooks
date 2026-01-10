---
url: "https://observablehq.com/@observablehq/plot-crimean-war-recty"
title: "Crimean war casualties by cause (with rectY)"
---

# Crimean war casualties by cause (with rectY)

# Crimean war casualties by cause 2 A stacked bar chart of [deaths in the Crimean War](https://en.wikipedia.org/wiki/Florence_Nightingale#Crimean_War)—predominantly from disease —using Florence Nightingale’s data. This uses the [rect](https://observablehq.com/plot/marks/rect) mark, with binned dates—compare with the [bar-mark](https://observablehq.com/@observablehq/plot-crimean-war-bary) variant.

```js
Plot.plot({
  y: {grid: true},
  marks: [
    Plot.rectY(crimea, {x: "date", y: "deaths", interval: "month", fill: "cause"}),
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

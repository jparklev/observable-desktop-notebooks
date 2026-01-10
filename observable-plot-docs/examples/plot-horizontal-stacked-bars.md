---
url: "https://observablehq.com/@observablehq/plot-horizontal-stacked-bars"
title: "Horizontal stacked bars"
---

# Horizontal stacked bars

The [bar](https://observablehq.com/plot/marks/bar) mark implicitly [stacks](https://observablehq.com/plot/transforms/stack) values, allowing to immediately see a total as well as do part-to-whole comparisons.

Let’s look at the gender distribution of members of the U.S. Congress in 2023. First, the number of women (F) and men (M):

```js
Plot.plot({
  marginLeft: 90,
  color: { legend: true },
  marks: [Plot.barX(congress, Plot.groupZ({ x: "count" }, { fill: "gender" }))]
})
```

We can split these by party affiliation (sorting the parties by their number of seats):

```js
Plot.plot({
  marginLeft: 90,
  marks: [
    Plot.barX(
      congress,
      Plot.groupY(
        { x: "count" },
        { fill: "gender", y: "party", sort: { y: "x", reverse: true } }
      )
    )
  ]
})
```

Or reverse the grouping and color encoding, and compare the party affiliation of women representatives vs men representatives, using the _normalize_ [stack offset](https://observablehq.com/plot/transforms/stack#stack-options) to compare proportions rather than absolute counts:

```js
Plot.plot({
  marginLeft: 90,
  color: { scheme: "Dark2", legend: true },
  x: { percent: true },
  marks: [
    Plot.barX(
      congress,
      Plot.groupY(
        { x: "count" },
        {
          fill: "party",
          y: "gender",
          sort: { y: "x", reverse: true, color: "width" },
          offset: "normalize"
        }
      )
    )
  ]
})
```

```js
congress = FileAttachment("us-congress-2023.csv").csv({typed: true})
```

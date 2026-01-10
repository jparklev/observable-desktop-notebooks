---
url: "https://observablehq.com/@observablehq/plot-sparse-line"
title: "Line with sparse data"
---

# Line with sparse data

Say you have some continuous function — oscillating temperature, say — with some irregularly sampled observations. Maybe you have a lot of samples in the summer months, but only sparse observations the rest of the year. You may be tempted to visualize the data as a line chart.

```js
Plot.lineY(data, {x: "date", y: "value", marker: true}).plot()
```

This approach works fine in the summer, when the observations are dense. But when the observations are sparse, interpolating linearly between the samples makes the data look pretty choppy! So what can you do instead?

Well to start, let’s just look at when the observations occur to get a sense of the temporal distribution. In Plot, that’s the bin transform with the _count_ reducer.

```js
Plot.rectY(data, Plot.binX({y: "count"}, {x: "date"})).plot()
```

For more precision, we can choose a specific **interval**:

```js
Plot.rectY(data, Plot.binX({y: "count"}, {x: "date", interval: "day", tip: true})).plot()
```

During the summer months, we generally have multiple observations per day. So it’d be reasonable to aggregate those observations into a single value to produce a smooth line, say by using the _mean_ or _median_.

```js
Plot.lineY(data, Plot.binX({y: "mean"}, {x: "date", y: "value", interval: "day", marker: true})).plot()
```

But again, this approach doesn’t work well when data is sparse. That’s because the bin transform won’t emit empty bins, and so the line mark will happily interpolate over the days when data is missing.

We can tell the bin transform to emit empty bins using the **filter** output option.

```js
Plot.lineY(data, Plot.binX({y: "mean", filter: null}, {x: "date", y: "value", interval: "day", marker: true})).plot()
```

Now we get gaps when there aren’t any samples for a particular day, and thus no meaningful mean observed value.

If this feels a little verbose to you, Plot has shorthand **interval** and **reduce** options that you can pass directly to the line mark. Plot knows to set the **filter** output option to null automatically since the line will interpolate across bins.

```js
Plot.lineY(data, {x: "date", y: "value", reduce: "mean", interval: "day", marker: true}).plot()
```

Filling in the gaps is especially important when using the _count_ reducer because by definition, without the empty bins we would never see a zero value! (I’ll plot the bins as rects below, too, so you can see the gaps more clearly.)

```js
Plot.plot({
  marks: [
    Plot.rectY(data, Plot.binX({y: "count"}, {x: "date", interval: "day", fill: "#ccc"})),
    Plot.lineY(data, Plot.binX({y: "count"}, {x: "date", interval: "day"})),
    Plot.ruleY([0])
  ]
})
```

Compare to dense bins:

```js
Plot.plot({
  marks: [
    Plot.rectY(data, Plot.binX({y: "count"}, {x: "date", interval: "day", fill: "#ccc"})),
    Plot.lineY(data, Plot.binX({y: "count", filter: null}, {x: "date", interval: "day"})),
    Plot.ruleY([0])
  ]
})
```

Or, as shorthand:

```js
Plot.lineY(data, {x: "date", reduce: "count", interval: "day"}).plot()
```

You can do the same with an area mark, but it seems like you also have to set the **y** option to anything. That’s probably [a bug](https://github.com/observablehq/plot/issues/2328).

```js
Plot.areaY(data, {x: "date", y: true, reduce: "count", interval: "day"}).plot()
```

Here’s another way of putting it together:

```js
Plot.plot({
  marks: [
    Plot.rectY(data, Plot.binX({y: "count"}, {x: "date", interval: "day", fill: "#ccc"})),
    Plot.lineY(data, {x: "date", y: "value", reduce: "mean", interval: "day"}),
    Plot.ruleY([0])
  ]
})
```

--- ## Appendix

```js
data = {
  const r = d3.randomNormal.source(d3.randomLcg(42))(0, 20);
  const r2 = d3.randomNormal.source(d3.randomLcg(44))(0, 0.1);
  const origin = new Date("2024-07-01");
  return d3.range(1000).map(() => {
    const offset = r();
    return {date: new Date(+origin + offset * 864e5), value: Math.sin(offset / 4) + r2()};
  }).sort((a, b) => d3.ascending(a.date, b.date));
}
```

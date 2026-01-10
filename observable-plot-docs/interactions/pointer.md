---
url: "https://observablehq.com/plot/interactions/pointer"
title: "Pointer transform | Plot"
---

# Pointer transform [^0.6.7](https://github.com/observablehq/plot/releases/tag/v0.6.7 "added in v0.6.7") [​](https://observablehq.com/plot/interactions/pointer\#pointer-transform)

The **pointer transform** filters a mark interactively such that only the point closest to the pointer is rendered. It is typically used to show details on hover, often with a [tip](https://observablehq.com/plot/marks/tip) or [crosshair](https://observablehq.com/plot/interactions/crosshair) mark, but it can be paired with any mark.

To demonstrate, below the pointer transform filters a filled red dot behind a stroked black dot. As you hover the chart, only the closest red dot to the pointer is rendered. If you remove the pointer transform by toggling the checkbox, all the red dots will be visible.

Use pointer:

1415161718192021↑ culmen\_depth\_mm3540455055culmen\_length\_mm →

js

```
Plot.plot({
  marks: [\
    Plot.dot(penguins, (pointered ? Plot.pointer : (o) => o)({x: "culmen_length_mm", y: "culmen_depth_mm", fill: "red", r: 8})),\
    Plot.dot(penguins, {x: "culmen_length_mm", y: "culmen_depth_mm"})\
  ]
})
```

js

```
Plot.plot({
  marks: [\
    Plot.dot(penguins, Plot.pointer({x: "culmen_length_mm", y: "culmen_depth_mm", fill: "red", r: 8})),\
    Plot.dot(penguins, {x: "culmen_length_mm", y: "culmen_depth_mm"})\
  ]
})
```

The pointer transform is similar to the [filter](https://observablehq.com/plot/transforms/filter) and [select](https://observablehq.com/plot/transforms/select) transforms: it filters the mark’s index to show a subset of the data. The difference is that the pointer transform is _interactive_: it listens to [pointer events](https://developer.mozilla.org/en-US/docs/Web/API/Pointer_events) and re-renders the mark as the closest point changes. Since the mark is lazily rendered during interaction, it is fast: only the visible elements are rendered as needed. And, like the filter and select transforms, unfiltered channel values are incorporated into default scale domains.

The pointer transform supports both one- and two-dimensional pointing modes. The two-dimensional mode, [pointer](https://observablehq.com/plot/interactions/pointer#pointer), is used above and is suitable for scatterplots and the general case: it finds the point closest to the pointer by measuring distance in _x_ and _y_. The one-dimensional modes, [pointerX](https://observablehq.com/plot/interactions/pointer#pointerX) and [pointerY](https://observablehq.com/plot/interactions/pointer#pointerY), in contrast only consider distance in one dimension; this is desirable when a chart has a “dominant” dimension, such as time in a time-series chart, the binned quantitative dimension in a histogram, or the categorical dimension of a bar chart.

Try the different modes on the line chart below to get a feel for their behavior.

Pointing mode:  pointer pointerX pointerY

60708090100110120130140150160170180190↑ Close20142015201620172018 [Fork](https://observablehq.com/@observablehq/plot-pointer-modes-x-y-and-xy "Open on Observable")

js

```
Plot.lineY(aapl, {x: "Date", y: "Close", tip: "x"}).plot()
```

“One-dimensional” is a slight misnomer: the pointerX and pointerY transforms consider distance in both dimensions, but the distance along the non-dominant dimension is divided by 100. Below, the pointerX transform is applied to a multi-series line chart; the closest point in _x_ is chosen, while _y_ is used to “break ties” such that you can focus different series by moving the mouse vertically.

02004006008001,0001,2001,4001,6001,8002,0002,2002,400↑ unemployed20002001200220032004200520062007200820092010 [Fork](https://observablehq.com/@observablehq/plot-multi-series-line-chart-interactive-tips "Open on Observable")

js

```
Plot.plot({
  marks: [\
    Plot.ruleY([0]),\
    Plot.lineY(industries, {x: "date", y: "unemployed", stroke: "industry", tip: "x"})\
  ]
})
```

One-dimensional pointing makes even small bars or rects easily hoverable. If you switch the histogram below to two-dimensional pointing, you must hover near a rect’s centroid (shown in red) to trigger a tip, whereas one-dimensional pointing triggers the tip anywhere in the chart.

Pointing mode:  pointer pointerX

0102030405060708090100110↑ Frequency7.27.47.67.88.08.28.4Daily volume (log₁₀) → [Fork](https://observablehq.com/@observablehq/plot-one-dimensional-pointing "Open on Observable")

js

```
Plot.plot({
  x: {label: "Daily volume (log₁₀)"},
  marks: [\
    Plot.rectY(aapl, Plot.binX({y: "count"}, {x: (d) => Math.log10(d.Volume), thresholds: 40, tip: "x"})),\
    Plot.dot(aapl, Plot.stackY(Plot.binX({y: "count"}, {x: (d) => Math.log10(d.Volume), thresholds: 40, stroke: "red"})))\
  ]
})
```

This reveals an important caveat: the pointer transform understands only points and not the arbitrary geometry of marks. By default, the pointer transform only focuses the closest point if it is within 40 pixels of the pointer (in either one or two dimensions, depending on the pointing mode). With large marks, there may be “dead spots” that do not trigger pointing even when the pointer is within the displayed mark. You can mitigate dead spots either by switching to one-dimensional pointing, if appropriate, or by setting the **maxRadius** option to increase the pointing distance cutoff.

Another caveat is that since the pointer transform only focuses one point at a time, if points are coincident (or nearly so), some points may not be focusable. In the future, the pointer transform might allow focusing multiple points simultaneously, or some method of cycling through nearby points. If you are interested in this feature, please upvote [#1621](https://github.com/observablehq/plot/issues/1621).

The pointer transform will prefer the midpoint of the **x1** and **x2** channels, if present, to the **x** channel, and likewise for **y1**, **y2**, and **y**; this allows the pointer transform to be applied to a rect, bar, area, or other mark with paired channels. It also enables these marks to support the **tip** mark option. (If no _x_ or _y_ channels are specified, the pointer transform respects the **frameAnchor** option.)

The **px** and **py** channels may be used to specify pointing target positions independent of the displayed mark. Below, text in the top-left corner shows the focused date and closing price. The focused point is also highlighted with a red dot and rule.

50100150200Close ↑20142015201620172018 [Fork](https://observablehq.com/@observablehq/plot-pointer-target-position "Open on Observable")

js

```
Plot.plot({
  height: 160,
  y: {axis: "right", grid: true, nice: true},
  marks: [\
    Plot.lineY(aapl, {x: "Date", y: "Close"}),\
    Plot.ruleX(aapl, Plot.pointerX({x: "Date", py: "Close", stroke: "red"})),\
    Plot.dot(aapl, Plot.pointerX({x: "Date", y: "Close", stroke: "red"})),\
    Plot.text(aapl, Plot.pointerX({px: "Date", py: "Close", dy: -17, frameAnchor: "top-left", fontVariant: "tabular-nums", text: (d) => [`Date ${Plot.formatIsoDate(d.Date)}`, `Close ${d.Close.toFixed(2)}`].join("   ")}))\
  ]
})
```

As the above chart shows, a plot can have multiple pointer transforms. Each pointer transform functions independently (with the exception of _click-to-stick_, described next), though we recommend configuring them with the same target positions and pointing mode so that the same point is focused across marks.

The pointer transform supports “click-to-stick”: clicking on the chart locks the currently-focused point until you click again. By locking the pointer, you can select text from the tip for copy and paste. If a plot has multiple pointer transforms, clicking will lock all pointer transforms.

The pointer transform emits an [_input_ event](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/input_event) whenever the focused points changes, and sets the value of the plot element to the focused data. This allows you to use a plot as an [Observable view](https://observablehq.com/@observablehq/views) (viewof), or to register an _input_ event listener to react to pointing.

js

```
const plot = Plot.plot(options);

plot.addEventListener("input", (event) => {
  console.log(plot.value);
});
```

## Pointer options [​](https://observablehq.com/plot/interactions/pointer\#pointer-options)

The following options control the pointer transform:

- **px** \- the horizontal↔︎ target position; bound to the _x_ scale
- **py** \- the vertical↕︎ target position; bound to the _y_ scale
- **x** \- the fallback horizontal↔︎ target position; bound to the _x_ scale
- **y** \- the fallback vertical↕︎ target position; bound to the _y_ scale
- **x1** \- the starting horizontal↔︎ target position; bound to the _x_ scale
- **y1** \- the starting vertical↕︎ target position; bound to the _y_ scale
- **x2** \- the ending horizontal↔︎ target position; bound to the _x_ scale
- **y2** \- the ending vertical↕︎ target position; bound to the _y_ scale
- **maxRadius** \- the reach, or maximum distance, in pixels; defaults to 40
- **frameAnchor** \- how to position the target within the frame; defaults to _middle_

To resolve the horizontal target position, the pointer transform applies the following order of precedence:

1. the **px** channel, if present;
2. the midpoint of the **x1** and **x2** channels, if both are present;
3. the **x** channel, if present;
4. the **x1** channel, if present;
5. and lastly the position given by the **frameAnchor**.

The same precedence applies to the **py**, **y**, **y1**, and **y2** channels.

## pointer( _options_) [​](https://observablehq.com/plot/interactions/pointer\#pointer)

js

```
Plot.tip(penguins, Plot.pointer({x: "culmen_length_mm", y: "culmen_depth_mm"}))
```

Applies the pointer render transform to the specified _options_ to filter the mark index such that only the point closest to the pointer is rendered; the mark will re-render interactively in response to pointer events.

## pointerX( _options_) [​](https://observablehq.com/plot/interactions/pointer\#pointerX)

js

```
Plot.tip(aapl, Plot.pointerX({x: "Date", y: "Close"}))
```

Like [pointer](https://observablehq.com/plot/interactions/pointer#pointer), except the determination of the closest point considers mostly the _x_ (horizontal↔︎) position; this should be used for plots where _x_ is the dominant dimension, such as time in a time-series chart, the binned quantitative dimension in a histogram, or the categorical dimension of a bar chart.

## pointerY( _options_) [​](https://observablehq.com/plot/interactions/pointer\#pointerY)

js

```
Plot.tip(alphabet, Plot.pointerY({x: "frequency", y: "letter"}))
```

Like [pointer](https://observablehq.com/plot/interactions/pointer#pointer), except the determination of the closest point considers mostly the _y_ (vertical↕︎) position; this should be used for plots where _y_ is the dominant dimension, such as time in a time-series chart, the binned quantitative dimension in a histogram, or the categorical dimension of a bar chart.

Pager

[Previous pageCrosshair](https://observablehq.com/plot/interactions/crosshair)

[Next pageAPI index](https://observablehq.com/plot/api)

[Home](https://observablehq.com/ "Home")

Resources

- [Forum](https://talk.observablehq.com/)
- [Slack](https://observablehq.com/slack/join)
- [Releases](https://github.com/observablehq/plot/releases)

Observable

- [Product](https://observablehq.com/product)
- [Plot](https://observablehq.com/plot)
- [Integrations](https://observablehq.com/data-integrations)
- [Pricing](https://observablehq.com/pricing)

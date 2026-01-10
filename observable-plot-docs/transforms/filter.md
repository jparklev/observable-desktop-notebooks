---
url: "https://observablehq.com/plot/transforms/filter"
title: "Filter transform | Plot"
---

# Filter transform [​](https://observablehq.com/plot/transforms/filter\#filter-transform)

The **filter transform** filters a mark’s index to show a subset of the data. For example, below the **filter** option controls which text labels are displayed in a dense scatterplot.

Use filter:

4.04.55.05.56.06.57.07.58.08.5↑ R90\_10\_2015200k300k400k1M2M3M4M10M20MPOP\_2015 →New YorkChicagoHoustonWashington, D.C.San FranciscoSan JoseFairfield, Conn.Binghamton, N.Y. [Fork](https://observablehq.com/@observablehq/plot-filter-demo "Open on Observable")

js

```
Plot.plot({
  grid: true,
  x: {type: "log"},
  marks: [\
    Plot.dot(metros, {\
      x: "POP_2015",\
      y: "R90_10_2015"\
    }),\
    Plot.text(metros, {\
      filter: filtered ? "highlight" : null,\
      x: "POP_2015",\
      y: "R90_10_2015",\
      text: "nyt_display",\
      frameAnchor: "bottom",\
      dy: -6\
    })\
  ]
})
```

TIP

As an alternative to the filter transform here, you could set the **text** channel value to null using a function: `text: (d) => d.highlight ? d.nyt_display : null`.

The filter transform can be applied either via the **filter** [mark option](https://observablehq.com/plot/features/marks#mark-options), as above, or as an explicit [filter transform](https://observablehq.com/plot/transforms/filter#filter). The latter is generally only needed when composing multiple transforms.

To highlight the vowels in a bar chart of English letter frequency, you can use a filtered bar with a red stroke. A filtered mark allows you to set options on a subset of the data, even if those options — such as mark insets — are not expressible as a channels.

0.000.010.020.030.040.050.060.070.080.090.100.110.12↑ frequencyABCDEFGHIJKLMNOPQRSTUVWXYZletter [Fork](https://observablehq.com/@observablehq/plot-filtered-bars "Open on Observable")

js

```
Plot.plot({
  marks: [\
    Plot.barY(alphabet, {\
      x: "letter",\
      y: "frequency"\
    }),\
    Plot.barY(alphabet, {\
      filter: (d) => /[aeiouy]/i.test(d.letter),\
      x: "letter",\
      y: "frequency",\
      stroke: "red",\
      strokeWidth: 3,\
      inset: -3 // expand the bars\
    })\
  ]
})
```

Since the filter transform only affects the mark’s index and not the channel values, it does not affect the default scale domains. Below, the _x_ scale contains every English letter, even though the only the bars for the vowels are shown.

0.000.010.020.030.040.050.060.070.080.090.100.110.12↑ frequencyABCDEFGHIJKLMNOPQRSTUVWXYZletter [Fork](https://observablehq.com/@observablehq/plot-filtered-bars "Open on Observable")

js

```
Plot.plot({
  marks: [\
    Plot.barY(alphabet, {\
      filter: (d) => /[aeiouy]/i.test(d.letter),\
      x: "letter",\
      y: "frequency"\
    })\
  ]
})
```

If you want to drop values completely, you can filter the data with [_array_.filter](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/filter).

0.000.010.020.030.040.050.060.070.080.090.100.110.12↑ frequencyAEIOUYletter [Fork](https://observablehq.com/@observablehq/plot-filtered-bars "Open on Observable")

js

```
Plot.plot({
  marks: [\
    Plot.barY(\
      alphabet.filter((d) => /[aeiouy]/i.test(d.letter)),\
      {x: "letter", y: "frequency"}\
    )\
  ]
})
```

## filter( _test_, _options_) [​](https://observablehq.com/plot/transforms/filter\#filter)

js

```
Plot.filter((d) => /[aeiouy]/i.test(d.letter), {x: "letter", y: "frequency"})
```

Filters the data given the specified _test_. The test can be given as an accessor function (which receives the datum and index), or as a channel value definition such as a field name; truthy values are retained.

Pager

[Previous pageDodge](https://observablehq.com/plot/transforms/dodge)

[Next pageGroup](https://observablehq.com/plot/transforms/group)

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

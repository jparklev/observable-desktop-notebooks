---
url: "https://observablehq.com/plot/marks/text"
title: "Text mark | Plot"
---

# Text mark [​](https://observablehq.com/plot/marks/text\#text-mark)

The **text mark** draws text at the given position in **x** and **y**. It is often used to label other marks, such as to show the value of a [bar](https://observablehq.com/plot/marks/bar). When space is available, direct labeling can allow faster and more accurate reading of values than an axis alone (or a tooltip).

0123456789101112↑ Frequency (%)ABCDEFGHIJKLMNOPQRSTUVWXYZ12.79.18.27.57.06.76.36.16.04.34.02.82.82.42.42.32.02.01.91.51.00.80.20.10.10.1 [Fork](https://observablehq.com/@observablehq/plot-labeled-bars "Open on Observable")

js

```
Plot.plot({
  label: null,
  y: {
    grid: true,
    label: "Frequency (%)",
    percent: true
  },
  marks: [\
    Plot.barY(alphabet, {x: "letter", y: "frequency"}),\
    Plot.text(alphabet, {x: "letter", y: "frequency", text: (d) => (d.frequency * 100).toFixed(1), dy: -6, lineAnchor: "bottom"}),\
    Plot.ruleY([0])\
  ]
})
```

TIP

For formatting numbers and dates, consider [_number_.toLocaleString](https://observablehq.com/@mbostock/number-formatting), [_date_.toLocaleString](https://observablehq.com/@mbostock/date-formatting), [d3-format](https://d3js.org/d3-format), or [d3-time-format](https://d3js.org/d3-time-format).

If there are too many data points, labels may overlap, making them hard to read. Use the [filter transform](https://observablehq.com/plot/transforms/filter) to choose which points to label. In the connected scatterplot below, recreating Hannah Fairfield’s [“Driving Shifts Into Reverse”](http://www.nytimes.com/imagepages/2010/05/02/business/02metrics.html) from 2009, every fifth year is labeled.

1.41.61.82.02.22.42.62.83.03.2↑ Cost of gasoline ($ per gallon)4,0005,0006,0007,0008,0009,00010,000Miles driven (per person-year) →19601965197019751980198519901995200020052010 [Fork](https://observablehq.com/@observablehq/plot-connected-scatterplot "Open on Observable")

js

```
Plot.plot({
  inset: 10,
  grid: true,
  x: {label: "Miles driven (per person-year)"},
  y: {label: "Cost of gasoline ($ per gallon)"},
  marks: [\
    Plot.line(driving, {x: "miles", y: "gas", curve: "catmull-rom", marker: true}),\
    Plot.text(driving, {filter: (d) => d.year % 5 === 0, x: "miles", y: "gas", text: (d) => `${d.year}`, dy: -6, lineAnchor: "bottom"})\
  ]
})
```

TIP

If you’d like automatic labeling, please upvote [#27](https://github.com/observablehq/plot/issues/27).

For line charts with multiple series, you may wish to label only the start or end of each series; this can be done using the [select transform](https://observablehq.com/plot/transforms/select), as shown in the chart below comparing the number of daily travelers at airports in the U.S. between 2019 and 2020. The impact of the COVID-19 pandemic is dramatic.

0.00.20.40.60.81.01.21.41.61.82.02.22.42.62.8↑ Travelers per day (millions)Mar2020AprMayJunJulAugSepOctNovDec20192020 [Fork](https://observablehq.com/@observablehq/plot-labeled-line-chart "Open on Observable")

js

```
Plot.plot({
  y: {
    grid: true,
    label: "Travelers per day (millions)",
    transform: (d) => d / 1e6 // convert to millions
  },
  marks: [\
    Plot.ruleY([0]),\
    Plot.line(travelers, {x: "date", y: "previous", strokeOpacity: 0.5}),\
    Plot.line(travelers, {x: "date", y: "current"}),\
    Plot.text(travelers, Plot.selectFirst({x: "date", y: "previous", text: ["2019"], fillOpacity: 0.5, lineAnchor: "bottom", dy: -6})),\
    Plot.text(travelers, Plot.selectFirst({x: "date", y: "current", text: ["2020"], lineAnchor: "top", dy: 6}))\
  ]
})
```

CAUTION

The select transform uses input order, not natural order by value, to determine the meaning of _first_ and _last_. Since this dataset is in reverse chronological order, the first element is the most recent.

A text mark can also be used to visualize data directly, similar to a [dot mark](https://observablehq.com/plot/marks/dot) in a scatterplot. Below a “stem and leaf” plot of Caltrain’s Palo Alto station schedule uses [stacked](https://observablehq.com/plot/transforms/stack) text. The **fill** channel provides a color encoding to distinguish trains that make every stop (N), limited trains that make fewer stops (L), and “baby bullet” trains that make the fewest stops (B).

NLB

NorthboundSouthbound5a6a7a8a9a10a11a12p1p2p3p4p5p6p7p8p9p10p11p12a111111112333333355566101111111212121616161616181818212123232324242425252526262626363636363636363838383841414141414144494951515154545757 [Fork](https://observablehq.com/@observablehq/plot-caltrain-schedule "Open on Observable")

js

```
Plot.plot({
  width: 240,
  axis: null,
  x: {type: "point"},
  y: {type: "point", domain: d3.range(4, 25)},
  color: {domain: "NLB", range: ["currentColor", "peru", "brown"], legend: true},
  marks: [\
    Plot.text([[0.5, 4]], {text: ["Northbound"], textAnchor: "start", dx: 16}),\
    Plot.text([[-0.5, 4]], {text: ["Southbound"], textAnchor: "end", dx: -16}),\
    Plot.text(d3.range(5, 25), {x: 0, y: Plot.identity, text: (y) => `${y % 12 || 12}${y % 24 >= 12 ? "p": "a"}`}),\
    Plot.text(caltrain, Plot.stackX2({x: (d) => d.orientation === "N" ? 1 : -1, y: "hours", fill: "type", text: "minutes"})),\
    Plot.ruleX([-0.5, 0.5])\
  ]
})
```

INFO

Since the **textAnchor** option is a constant rather than a channel, separate text marks are used for the _Northbound_ and _Southbound_ labels.

The **x** and **y** channels are optional; a one-dimensional text mark can be produced by specifying only one position dimension. If both **x** and **y** are not defined, the text mark assumes that the data is an iterable of points \[\[ _x₁_, _y₁_\], \[ _x₂_, _y₂_\], …\], allowing for [shorthand](https://observablehq.com/plot/features/shorthand). Furthermore, the default **text** channel is the associated datum’s index. (This is rarely what you want, but at least it gets something on the screen.)

−9−8−7−6−5−4−3−2−101234567891011−10−8−6−4−202468100123456789101112131415161718192021222324252627282930313233343536373839404142434445464748495051525354555657585960616263646566676869707172737475767778798081828384858687888990919293949596979899100101102103104105106107108109110111112113114115116117118119120121122123124125126127128129130131132133134135136137138139140141142143144145146147148149150 [Fork](https://observablehq.com/@observablehq/plot-text-spiral "Open on Observable")

js

```
Plot.plot({
  aspectRatio: 1,
  inset: 10,
  grid: true,
  marks: [\
    Plot.text(d3.range(151).map((i) => [\
      Math.sqrt(i) * Math.sin(i / 10),\
      Math.sqrt(i) * Math.cos(i / 10)\
    ]))\
  ]
})
```

The text mark will generate multiple lines if the **text** contains newline characters (`\n`). This may be useful for longer annotations.

This Is Just To SayWilliam Carlos Williams, 1934I have eatenthe plumsthat were inthe iceboxand whichyou were probablysavingfor breakfastForgive methey were deliciousso sweetand so cold [Fork](https://observablehq.com/@observablehq/plot-this-is-just-to-say "Open on Observable")

js

```
Plot.plot({
  height: 200,
  marks: [\
    Plot.frame(),\
    Plot.text([`This Is Just To Say\
William Carlos Williams, 1934\
\
I have eaten\
the plums\
that were in\
the icebox\
\
and which\
you were probably\
saving\
for breakfast\
\
Forgive me\
they were delicious\
so sweet\
and so cold`], {frameAnchor: "middle"})\
  ]
})
```

Alternatively, the **lineWidth** option enables automatic line wrapping. This option must be specified as a number in [ems](https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/Values_and_units). When a word contains a [soft-hyphen](https://en.wikipedia.org/wiki/Soft_hyphen) (`\xad`), it may be replaced by a hyphen when wrapping. The **textOverflow** option can also be used to truncate lines that exceed the specified line width, like in the incipit of Herman Melville’s _Moby-Dick_ (1851).

123Call me Ishmael. Some years ago — nevermind how long precisely — having little orno money in my purse, and nothingparticular to interest me on shore, Ithought I would sail about a little and seethe watery part of the world. It is a way Ihave of driving off the spleen andregulating the circulation. Whenever Ifind myself growing grim about themouth; whenever it is a damp, drizzlyNovember in my soul; whenever I findmyself involuntarily pausing before cof­-fin warehouses, and bringing up the rearof every funeral I meet; and especiallywhenever my hypos get such an upperhand of me, that it requires a strongmoral principle to prevent me fromdeliberately stepping into the street, andmethodically knocking people’s hats off— then, I account it high time to get tosea as soon as I can. This is mysubstitute for pistol and ball. With aphilosophical flourish Cato throwshimself upon his sword; I quietly take tothe ship. There is nothing surprising inthis. If they but knew it, almost all men intheir degree, some time or other, cherishvery nearly the same feelings towardsthe ocean with me.There now is your insular city of theManhattoes, belted round by wharves asIndian isles by coral reefs — commercesurrounds it with her surf. Right and left,the streets take you waterward. Itsextreme downtown is the battery, wherethat noble mole is washed by waves, andcooled by breezes, which a few hoursprevious were out of sight of land. Lookat the crowds of water-gazers there.Circumambulate the city of a dreamySabbath afternoon. Go from CorlearsHook to Coenties Slip, and from thence,by Whitehall, northward. What do yousee? — Posted like silent sentinels allaround the town, stand thousands uponthousands of mortal men fixed in oceanreveries. Some leaning against thespiles; some seated upon the pier-heads;some looking over the bulwarks of shipsfrom China; some high aloft in therigging, as if striving to get a still betterseaward peep. But these are alllandsmen; of week days pent up in lathand plaster — tied to counters, nailed tobenches, clinched to desks. How then isthis? Are the green fields gone? What dothey here? [Fork](https://observablehq.com/@observablehq/plot-moby-dick "Open on Observable")

js

```
Plot.plot({
  height: 320,
  x: {type: "point", align: 0, axis: "top", tickSize: 0},
  marks: [\
    Plot.text(\
      [\
        "Call me Ishmael. Some years ago — never mind how long precisely — having little or no money in my purse, and nothing particular to interest me on shore, I thought I would sail about a little and see the watery part of the world. It is a way I have of driving off the spleen and regulating the circulation. Whenever I find myself growing grim about the mouth; whenever it is a damp, drizzly November in my soul; whenever I find myself involuntarily pausing before cof\xadfin warehouses, and bringing up the rear of every funeral I meet; and especially whenever my hypos get such an upper hand of me, that it requires a strong moral principle to prevent me from deliberately stepping into the street, and methodically knocking people’s hats off — then, I account it high time to get to sea as soon as I can. This is my substitute for pistol and ball. With a philosophical flourish Cato throws himself upon his sword; I quietly take to the ship. There is nothing surprising in this. If they but knew it, almost all men in their degree, some time or other, cherish very nearly the same feelings towards the ocean with me.",\
        "There now is your insular city of the Manhattoes, belted round by wharves as Indian isles by coral reefs — commerce surrounds it with her surf. Right and left, the streets take you waterward. Its extreme downtown is the battery, where that noble mole is washed by waves, and cooled by breezes, which a few hours previous were out of sight of land. Look at the crowds of water-gazers there.",\
        "Circumambulate the city of a dreamy Sabbath afternoon. Go from Corlears Hook to Coenties Slip, and from thence, by Whitehall, northward. What do you see? — Posted like silent sentinels all around the town, stand thousands upon thousands of mortal men fixed in ocean reveries. Some leaning against the spiles; some seated upon the pier-heads; some looking over the bulwarks of ships from China; some high aloft in the rigging, as if striving to get a still better seaward peep. But these are all landsmen; of week days pent up in lath and plaster — tied to counters, nailed to benches, clinched to desks. How then is this? Are the green fields gone? What do they here?"\
      ],\
      {\
        x: (d, i) => 1 + i, // paragraph number\
        lineWidth: 20,\
        frameAnchor: "top",\
        textAnchor: "start"\
      }\
    )\
  ]
})
```

CAUTION

For performance and simplicity, Plot does not measure text exactly and instead uses an approximate heuristic. If Plot’s automatic wrapping is not doing what you want, consider hard wrapping with manual newlines (`\n`) instead. There is also a **monospace** option suitable for fixed-width fonts.

## Text options [​](https://observablehq.com/plot/marks/text\#text-options)

The following channels are required:

- **text** \- the text contents (a string, possibly with multiple lines)

If the **text** contains `\n`, `\r\n`, or `\r`, it will be rendered as multiple lines. If the **text** is specified as numbers or dates, a default formatter will automatically be applied, and the **fontVariant** will default to _tabular-nums_ instead of _normal_. If **text** is not specified, it defaults to [identity](https://observablehq.com/plot/features/transforms#identity) for primitive data (such as numbers, dates, and strings), and to the zero-based index \[0, 1, 2, …\] for objects (so that something identifying is visible by default).

In addition to the [standard mark options](https://observablehq.com/plot/features/marks#mark-options), the following optional channels are supported:

- **x** \- the horizontal position; bound to the _x_ scale
- **y** \- the vertical position; bound to the _y_ scale
- **fontSize** \- the font size in pixels
- **rotate** \- the rotation angle in degrees clockwise

If either of the **x** or **y** channels are not specified, the corresponding position is controlled by the **frameAnchor** option.

The following text-specific constant options are also supported:

- **textAnchor** \- the [text anchor](https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/text-anchor) for horizontal position; _start_, _end_, or _middle_
- **lineAnchor** \- the line anchor for vertical position; _top_, _bottom_, or _middle_
- **lineHeight** \- the line height in ems; defaults to 1
- **lineWidth** \- the line width in ems, for wrapping; defaults to Infinity
- **textOverflow** \- how to wrap or clip lines longer than the specified line width [^0.6.4](https://github.com/observablehq/plot/releases/tag/v0.6.4 "added in v0.6.4")
- **monospace** \- if true, changes the default **fontFamily** and metrics to monospace
- **fontFamily** \- the font name; defaults to [_system-ui_](https://drafts.csswg.org/css-fonts-4/#valdef-font-family-system-ui)
- **fontSize** \- the font size in pixels; defaults to 10
- **fontStyle** \- the [font style](https://developer.mozilla.org/en-US/docs/Web/CSS/font-style); defaults to _normal_
- **fontVariant** \- the [font variant](https://developer.mozilla.org/en-US/docs/Web/CSS/font-variant); defaults to _normal_
- **fontWeight** \- the [font weight](https://developer.mozilla.org/en-US/docs/Web/CSS/font-weight); defaults to _normal_
- **frameAnchor** \- how to position the text within the frame; defaults to _middle_
- **rotate** \- the rotation angle in degrees clockwise; defaults to 0

If a **lineWidth** is specified, input text values will be wrapped as needed to fit while preserving existing newlines. The line wrapping implementation is rudimentary: it replaces the space before the word that overflows with a line feed (`\n`). Lines might also be split on words that contain a soft-hyphen (`\xad`), replacing it with a hyphen (-). For non-ASCII, non-U.S. English text, or for when a different font is used, you may get better results by hard-wrapping the text yourself (by supplying line feeds in the input). If the **monospace** option is truthy, the default **fontFamily** changes to monospace and the **lineWidth** option is interpreted as characters (ch) rather than ems.

The **textOverflow** option can be used to truncate lines of text longer than the given **lineWidth**. If the mark does not have a **title** channel, a title with the non-truncated text is also added. The following **textOverflow** values are supported:

- null (default) - preserve overflowing characters
- _clip_ or _clip-end_ \- remove characters from the end
- _clip-start_ \- remove characters from the start
- _ellipsis_ or _ellipsis-end_ \- replace characters from the end with an ellipsis (…)
- _ellipsis-start_ \- replace characters from the start with an ellipsis (…)
- _ellipsis-middle_ \- replace characters from the middle with an ellipsis (…)

The **fontSize** and **rotate** options can be specified as either channels or constants. When fontSize or rotate is specified as a number, it is interpreted as a constant; otherwise it is interpreted as a channel.

If the **frameAnchor** option is not specified, then **textAnchor** and **lineAnchor** default to middle. Otherwise, **textAnchor** defaults to start if **frameAnchor** is on the left, end if **frameAnchor** is on the right, and otherwise middle. Similarly, **lineAnchor** defaults to top if **frameAnchor** is on the top, bottom if **frameAnchor** is on the bottom, and otherwise middle.

The **paintOrder** option defaults to _stroke_ and the **strokeWidth** option defaults to 3. By setting **fill** to the foreground color and **stroke** to the background color (such as _black_ and _white_, respectively), you can surround text with a “halo” which may improve legibility against a busy background.

## text( _data_, _options_) [​](https://observablehq.com/plot/marks/text\#text)

js

```
Plot.text(driving, {x: "miles", y: "gas", text: "year"})
```

Returns a new text mark with the given _data_ and _options_. If neither the **x** nor **y** nor **frameAnchor** options are specified, _data_ is assumed to be an array of pairs \[\[ _x₀_, _y₀_\], \[ _x₁_, _y₁_\], \[ _x₂_, _y₂_\], …\] such that **x** = \[ _x₀_, _x₁_, _x₂_, …\] and **y** = \[ _y₀_, _y₁_, _y₂_, …\].

## textX( _data_, _options_) [​](https://observablehq.com/plot/marks/text\#textX)

js

```
Plot.textX(alphabet.map((d) => d.frequency))
```

Equivalent to [text](https://observablehq.com/plot/marks/text#text), except **x** defaults to [identity](https://observablehq.com/plot/features/transforms#identity) and assumes that _data_ = \[ _x₀_, _x₁_, _x₂_, …\].

If an **interval** is specified, such as d3.utcDay, **y** is transformed to ( _interval_.floor( _y_) \+ _interval_.offset( _interval_.floor( _y_))) / 2\. If the interval is specified as a number _n_, _y_ will be the midpoint of two consecutive multiples of _n_ that bracket _y_. Named UTC intervals such as _day_ are also supported; see [scale options](https://observablehq.com/plot/features/scales#scale-options).

## textY( _data_, _options_) [​](https://observablehq.com/plot/marks/text\#textY)

js

```
Plot.textY(alphabet.map((d) => d.frequency))
```

Equivalent to [text](https://observablehq.com/plot/marks/text#text), except **y** defaults to [identity](https://observablehq.com/plot/features/transforms#identity) and assumes that _data_ = \[ _y₀_, _y₁_, _y₂_, …\].

If an **interval** is specified, such as d3.utcDay, **x** is transformed to ( _interval_.floor( _x_) \+ _interval_.offset( _interval_.floor( _x_))) / 2\. If the interval is specified as a number _n_, _x_ will be the midpoint of two consecutive multiples of _n_ that bracket _x_. Named UTC intervals such as _day_ are also supported; see [scale options](https://observablehq.com/plot/features/scales#scale-options).

Pager

[Previous pageRule](https://observablehq.com/plot/marks/rule)

[Next pageTick](https://observablehq.com/plot/marks/tick)

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

---
url: "https://observablehq.com/plot/features/transforms"
title: "Transforms | Plot"
---

# Transforms [​](https://observablehq.com/plot/features/transforms\#transforms)

**Transforms** derive data as part of the plot specification. This accelerates what is often the most onerous task in visualization: getting data into the right shape.

For example, given a [dataset of highway traffic](https://gist.github.com/chrtze/c74efb46cadb6a908bbbf5227934bfea) measured as vehicles per hour by location, plotting every observation is straightforward: use a [tick](https://observablehq.com/plot/marks/tick) (or [dot](https://observablehq.com/plot/marks/dot)) and assign **x** = vehicles per hour and **y** = location. But to draw a quantifiable insight, we may want a summary statistic such as the _median_ traffic by location. 👩‍💻 Below we use the [group transform](https://observablehq.com/plot/transforms/group) to group by location and apply a _median_ reducer to position the red tick.

Saarbrücken-NeuhausOldenburg (Holstein)HolzGöttelbornRiegelsbergKastelNeustadt i. H.-SüdNettersheimHasbornLaufeldOtzenhausenNonnweilerKirschheckAS EppelbornBierfeldVon der HeydtIllingenHetzerathGroß IppenerBockelLadbergenDibbersenEuskirchen/BliesheimHürthLotteAschebergBad SchwartauSchloss BurgUphusenHB-SilberseeBarsbüttelHB-Mahndorfer SeeGlüsingenHB-WeserbrückeHengsenKöln-NordHagen-VorhalleUnna0123456789Vehicles per hour (thousands) → [Fork](https://observablehq.com/@observablehq/plot-sorted-groups "Open on Observable")

js

```
Plot.plot({
  marginLeft: 120,
  x: {label: "Vehicles per hour (thousands)", transform: (x) => x / 1000},
  y: {label: null},
  marks: [\
    Plot.ruleX([0]),\
    Plot.tickX(\
      traffic,\
      {x: "vehicles", y: "location", strokeOpacity: 0.3}\
    ),\
    Plot.tickX(\
      traffic,\
      Plot.groupY(\
        {x: "median"},\
        {x: "vehicles", y: "location", stroke: "red", strokeWidth: 4, sort: {y: "x"}}\
      )\
    )\
  ]
})
```

As you might expect, traffic varies significantly throughout the day, so perhaps it would be better to look at the median by hour by location? Instead of grouping only by **y**, we can group by both **x** and **y** to produce a heatmap.

02,0004,0006,000vehiclesSaarbrücken-NeuhausKastelOldenburg (Holstein)NettersheimOtzenhausenLaufeldNeustadt i. H.-SüdHasbornNonnweilerBierfeldGöttelbornHolzKirschheckVon der HeydtAS EppelbornRiegelsbergHetzerathGroß IppenerIllingenDibbersenBockelLadbergenHürthEuskirchen/BliesheimAschebergLotteBad SchwartauSchloss BurgBarsbüttelUphusenHB-SilberseeHengsenHB-Mahndorfer SeeHagen-VorhalleGlüsingenHB-WeserbrückeKöln-NordUnna01234567891011121314151617181920212223 [Fork](https://observablehq.com/@observablehq/plot-sorted-heatmap "Open on Observable")

js

```
Plot.plot({
  marginLeft: 120,
  padding: 0,
  y: {label: null},
  color: {scheme: "YlGnBu", legend: true, zero: true},
  marks: [\
    Plot.cell(\
      traffic,\
      Plot.group(\
        {fill: "median"},\
        {x: (d) => d.date.getUTCHours(), y: "location", fill: "vehicles", inset: 0.5, sort: {y: "fill"}}\
      )\
    )\
  ]
})
```

Plot includes many useful transforms! For example, you can compute a [rolling average](https://observablehq.com/plot/transforms/window) to smooth a noisy signal, [stack layers](https://observablehq.com/plot/transforms/stack) for a streamgraph, or [dodge dots](https://observablehq.com/plot/transforms/dodge) for a beeswarm. Plot’s various built-in transforms include: [bin](https://observablehq.com/plot/transforms/bin), [centroid](https://observablehq.com/plot/transforms/centroid), [dodge](https://observablehq.com/plot/transforms/dodge), [filter](https://observablehq.com/plot/transforms/filter), [group](https://observablehq.com/plot/transforms/group), [hexbin](https://observablehq.com/plot/transforms/hexbin), [interval](https://observablehq.com/plot/transforms/interval), [map](https://observablehq.com/plot/transforms/map), [normalize](https://observablehq.com/plot/transforms/normalize), [reverse](https://observablehq.com/plot/transforms/sort#reverse), [select](https://observablehq.com/plot/transforms/select), [shuffle](https://observablehq.com/plot/transforms/sort#shuffle), [sort](https://observablehq.com/plot/transforms/sort), [stack](https://observablehq.com/plot/transforms/stack), [tree](https://observablehq.com/plot/transforms/tree), and [window](https://observablehq.com/plot/transforms/window). If these don’t meet your needs, you can even implement a [custom transform](https://observablehq.com/plot/features/transforms#custom-transforms).

Transforms are never required — you can always aggregate and derive data yourself outside of Plot, and then pass in the binned values. For example, we could use [d3.bin](https://d3js.org/d3-array/bin) to compute a histogram of athletes’ weights as an array of { _x0_, _x1_, _length_} objects.

js

```
bins = d3.bin().thresholds(80).value((d) => d.weight)(olympians)
```

We can then pass that to the [rect mark](https://observablehq.com/plot/marks/rect), assigning to the **x1**, **x2**, and **y2** channels:

050100150200250300350400450500550600↑ length406080100120140160

js

```
Plot.rectY(bins, {x1: "x0", x2: "x1", y2: "length"}).plot()
```

INFO

This is for demonstration only; you wouldn’t normally bin “by hand” as shown here.

But Plot’s transforms are often more convenient, especially in conjunction with Plot’s other features such as [faceting](https://observablehq.com/plot/features/facets) and automatic grouping by **z**. For example, if we want to add a color encoding to our histogram, we simply add the **fill** option and the bin transform partitions each bin accordingly; doing this with d3.bin would be a lot more work!

femalemale

050100150200250300350400450500550600↑ Frequency406080100120140160weight → [Fork](https://observablehq.com/@observablehq/plot-vertical-histogram "Open on Observable")

js

```
Plot.rectY(olympians, Plot.binX({y: "count"}, {x: "weight", fill: "sex"})).plot({color: {legend: true}})
```

Plot’s transforms typically take two _options_ objects as arguments: the first object contains the _transform_ options (above, `{y: "count"}`), while the second object contains _mark_ options to be “passed through” to the mark (`{x: "weight", fill: "sex"}`). The transform returns a new options object representing the _transformed_ mark options to be passed to a mark.

Breaking down the above code:

js

```
const options = {x: "weight", fill: "sex"}; // initial mark options
const binOptions = {y: "count"}; // bin transform options
const binned = Plot.binX(binOptions, options); // transformed mark options
const rect = Plot.rectY(olympians, binned); // rect mark
const plot = rect.plot({color: {legend: true}}); // plot!
```

TIP

If a transform isn’t doing what you expect, try inspecting the options object returned by the transform. Does it contain the options you expect?

Transforms can derive channels (such as **y** above) as well as changing the default options. For example, the bin transform sets default insets for a one-pixel gap between adjacent rects.

Transforms are composable: you can pass _options_ through more than one transform before passing it to a mark. For example, above it’s a bit difficult to compare the weight distribution by sex because there are fewer female than male athletes in the data. We can remove this effect using the [normalize transform](https://observablehq.com/plot/transforms/normalize) with the _sum_ reducer.

012345678↑ Frequency (%)406080100120140160weight → [Fork](https://observablehq.com/@observablehq/plot-overlapping-relative-histogram "Open on Observable")

js

```
Plot.plot({
  y: {percent: true},
  marks: [\
    Plot.rectY(\
      olympians,\
      Plot.normalizeY(\
        "sum", // normalize each series by the sum per series\
        Plot.binX(\
          {y2: "count"}, // disable implicit stack transform\
          {x: "weight", fill: "sex", mixBlendMode: "multiply"}\
        )\
      )\
    )\
  ]
})
```

And, as you may have wondered above, many of Plot’s [marks](https://observablehq.com/plot/features/marks) provide implicit transforms: for example, the [rectY mark](https://observablehq.com/plot/marks/rect) applies an implicit [stackY transform](https://observablehq.com/plot/transforms/stack) if you use the **y** option, and the [dot mark](https://observablehq.com/plot/marks/dot) applies an implicit [sort transform](https://observablehq.com/plot/transforms/sort) to mitigate the effect of occlusion by drawing the smallest dots on top.

## Custom transforms [​](https://observablehq.com/plot/features/transforms\#custom-transforms)

For greater control, you can also implement a custom **transform** function, allowing data, indexes, or channels to be derived prior to rendering. Custom transforms are rarely implemented directly; see the built-in transforms above. For example, below we implement the [filter transform](https://observablehq.com/plot/transforms/filter) “by hand” as a custom transform to show the unemployment rates only in Michigan metropolitan divisions.

0246810121416↑ Unemployment (%)2000200220042006200820102012 [Fork](https://observablehq.com/@observablehq/plot-custom-transform-example "Open on Observable")

js

```
Plot.plot({
  y: {
    grid: true,
    label: "Unemployment (%)"
  },
  color: {
    domain: [false, true],
    range: ["#ccc", "red"]
  },
  marks: [\
    Plot.ruleY([0]),\
    Plot.line(bls, {\
      x: "date",\
      y: "unemployment",\
      z: "division",\
      transform: (data, facets) => ({\
        data,\
        facets: facets.map((facet) => {\
          return facet.filter((i) => {\
            return /, MI /.test(data[i].division);\
          });\
        })\
      })\
    })\
  ]
})
```

The **transform** function is passed three arguments, _data_, _facets_, and _options_ representing the mark’s data and facet indexes, and the plot’s options; it must then return a { _data_, _facets_} object with the transformed data and facet indexes. The _facets_ are represented as a nested array of arrays such as \[\[0, 1, 3, …\], \[2, 5, 10, …\], …\]; each element in _facets_ specifies the zero-based indexes of elements in _data_ that are in a given facet ( _i.e._, have a distinct value in the associated _fx_ or _fy_ dimension).

If the **transform** option is specified, it supersedes any basic transforms ( _i.e._, the **filter**, **sort** and **reverse** options are ignored). However, the **transform** option is rarely used directly; instead one of Plot’s built-in transforms are used, and these transforms automatically compose with the basic **filter**, **sort** and **reverse** transforms.

While transform functions often produce new _data_ or _facets_, they may return the passed-in _data_ and _facets_ as-is, and often have a side effect of constructing derived channels. For example, the count of elements in a [groupX transform](https://observablehq.com/plot/transforms/group) might be returned as a new _y_ channel. In this case, the transform is typically expressed as an options transform: a function that takes a mark _options_ object and returns a new, transformed options object, where the returned options object implements the **transform** option. Transform functions should not mutate the input _data_ or _facets_. Likewise options transforms should not mutate the input _options_ object.

When implementing a custom transform for generic usage, keep in mind that it needs to be compatible with Plot’s [faceting system](https://observablehq.com/plot/features/facets), which partitions the original dataset into discrete subsets.

## Custom initializers [^0.5.0](https://github.com/observablehq/plot/releases/tag/v0.5.0 "added in v0.5.0") [​](https://observablehq.com/plot/features/transforms\#custom-initializers)

Initializers are a special class of transform; whereas transforms operate in abstract data space, initializers operate in screen space such as pixel coordinates and colors. For example, initializers can modify a marks’ positions to avoid occlusion. Initializers are invoked _after_ the initial scales are constructed and can modify the channels or derive new channels; these in turn may (or may not, as desired) be passed to scales. Plot’s [hexbin](https://observablehq.com/plot/transforms/hexbin) and [dodge](https://observablehq.com/plot/transforms/dodge) transforms are initializers.

You can specify a custom initializer by specifying a function as the mark **initializer** option. This function is called after the scales have been computed, and receives as inputs the (possibly transformed) array of _data_, the _facets_ index of elements of this array that belong to each facet, the input _channels_ (as an object of named channels), the _scales_, and the _dimensions_. The mark itself is the _this_ context. The initializer function must return an object with _data_, _facets_, and new _channels_. Any new channels are merged with existing channels, replacing channels of the same name.

If an initializer desires a channel that is not supported by the downstream mark, additional channels can be declared using the mark **channels** option.

## transform( _options_, _transform_) [^0.4.3](https://github.com/observablehq/plot/releases/tag/v0.4.3 "added in v0.4.3") [​](https://observablehq.com/plot/features/transforms\#transform)

js

```
Plot.transform(options, (data, facets) => {
  return {
    data,
    facets: facets.map((I) => I.filter(() => Math.random() > 0.5))
  };
})
```

Given an _options_ object that may specify some basic transforms ( **filter**, **sort**, or **reverse**) or a custom **transform** function, composes those transforms if any with the given _transform_ function, returning a new _options_ object. If a custom **transform** function is present on the given _options_, any basic transforms are ignored. Any additional input _options_ are passed through in the returned _options_ object. This method facilitates applying the basic transforms prior to applying the given custom _transform_ and is used internally by Plot’s built-in transforms.

## initializer( _options_, _initializer_) [^0.5.0](https://github.com/observablehq/plot/releases/tag/v0.5.0 "added in v0.5.0") [​](https://observablehq.com/plot/features/transforms\#initializer)

This helper composes the _initializer_ function with any other transforms present in the _options_, and returns a new _options_ object. It is used internally by Plot’s built-in initializer transforms.

## valueof( _data_, _value_, _type_) [​](https://observablehq.com/plot/features/transforms\#valueof)

js

```
Plot.valueof(aapl, "Close")
```

Given an iterable _data_ and some _value_ accessor, returns an array (a column) of the specified _type_ with the corresponding value of each element of the data. The _value_ accessor may be one of the following types:

- a string - corresponding to the field accessor (`(d) => d[value]`)
- an accessor function - called as _type_.from( _data_, _value_)
- a number, Date, or boolean — resulting in an array uniformly filled with the _value_
- an object with a **transform** method — called as _value_.transform( _data_)
- an array of values - returning the same
- null or undefined - returning the same

If _type_ is specified, it must be Array or a similar class that implements the [Array.from](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/from) interface such as a typed array. When _type_ is Array or a typed array class, the return value of valueof will be an instance of the same (or null or undefined). When _type_ is a typed array, values will be implicitly coerced numbers, and if _type_ is Float64Array, Float32Array, or a subclass of the same, null values will be implicitly replaced with NaN. If _type_ is not specified, valueof may return either an array or a typed array (or null or undefined).

valueof is not guaranteed to return a new array. When a transform method is used, or when the given _value_ is an array that is compatible with the requested _type_, the array may be returned as-is without making a copy.

## column( _source_) [^0.4.3](https://github.com/observablehq/plot/releases/tag/v0.4.3 "added in v0.4.3") [​](https://observablehq.com/plot/features/transforms\#column)

js

```
const [X, setX] = Plot.column();
```

This helper for constructing derived columns returns a \[ _column_, _setColumn_\] array. The _column_ object implements _column_.transform, returning whatever value was most recently passed to _setColumn_. If _setColumn_ is not called, then _column_.transform returns undefined. If a _source_ is specified, then _column_.label exposes the given _source_’s label, if any: if _source_ is a string as when representing a named field of data, then _column_.label is _source_; otherwise _column_.label propagates _source_.label. This allows derived columns to propagate a human-readable axis or legend label.

This method is used by Plot’s transforms to derive channels; the associated columns are populated (derived) when the **transform** option function is invoked.

## identity [^0.6.2](https://github.com/observablehq/plot/releases/tag/v0.6.2 "added in v0.6.2") [​](https://observablehq.com/plot/features/transforms\#identity)

js

```
Plot.contour(data, {width: w, height: h, fill: Plot.identity})
```

This channel helper returns a source array as-is, avoiding an extra copy when defining a channel as being equal to the data.

## indexOf [^0.6.6](https://github.com/observablehq/plot/releases/tag/v0.6.6 "added in v0.6.6") [​](https://observablehq.com/plot/features/transforms\#indexOf)

js

```
Plot.lineY(numbers, {x: Plot.indexOf, y: Plot.identity})
```

This channel helper returns an array of numbers \[0, 1, 2, 3, …\]. It is used internally by marks with zero-based index defaults for channels.

Pager

[Previous pageProjections](https://observablehq.com/plot/features/projections)

[Next pageInteractions](https://observablehq.com/plot/features/interactions)

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

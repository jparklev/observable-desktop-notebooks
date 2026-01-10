---
url: "https://observablehq.com/plot/transforms/group"
title: "Group transform | Plot"
---

# Group transform [​](https://observablehq.com/plot/transforms/group\#group-transform)

TIP

The group transform is for aggregating ordinal or nominal data. For quantitative or temporal data, use the [bin transform](https://observablehq.com/plot/transforms/bin).

The **group transform** groups ordinal or nominal data — discrete values such as name, type, or category. You can then compute summary statistics for each group, such as a count, sum, or proportion. The group transform is most often used to make bar charts with the [bar mark](https://observablehq.com/plot/marks/bar).

For example, the bar chart below shows a distribution of Olympic athletes by sport.

02004006008001,0001,2001,4001,6001,8002,0002,200↑ Frequencyaquaticsarcheryathleticsbadmintonbasketballboxingcanoecyclingequestrianfencingfootballgolfgymnasticshandballhockeyjudomodern pentathlonrowingrugby sevenssailingshootingtable tennistaekwondotennistriathlonvolleyballweightliftingwrestling [Fork](https://observablehq.com/@observablehq/plot-group-olympic-athletes-by-sport "Open on Observable")

js

```
Plot.plot({
  marginBottom: 100,
  x: {label: null, tickRotate: 90},
  y: {grid: true},
  marks: [\
    Plot.barY(olympians, Plot.groupX({y: "count"}, {x: "sport"})),\
    Plot.ruleY([0])\
  ]
})
```

TIP

Ordinal domains are sorted naturally (alphabetically) by default. Either set the [scale **domain**](https://observablehq.com/plot/features/scales) explicitly to change the order, or use the mark [**sort** option](https://observablehq.com/plot/features/scales#sort-mark-option) to derive the scale domain from a channel.

The groupX transform groups on **x**. The _outputs_ argument (here `{y: "count"}`) declares desired output channels ( **y**) and the associated reducer ( _count_). Hence the height of each bar above represents the number of Olympic athletes by sport.

While the groupX transform is often used to generate **y**, it can output to any channel. For example, by declaring **r** in _outputs_, we can generate dots of size proportional to the number of athletes in each sport.

aquaticsarcheryathleticsbadmintonbasketballboxingcanoecyclingequestrianfencingfootballgolfgymnasticshandballhockeyjudomodern pentathlonrowingrugby sevenssailingshootingtable tennistaekwondotennistriathlonvolleyballweightliftingwrestling [Fork](https://observablehq.com/@observablehq/plot-groups-as-dots "Open on Observable")

js

```
Plot.plot({
  marginBottom: 100,
  x: {label: null, tickRotate: 90},
  r: {range: [0, 14]},
  marks: [\
    Plot.dot(olympians, Plot.groupX({r: "count"}, {x: "sport"}))\
  ]
})
```

The **fill** channel meanwhile will produce a one-dimensional heatmap. Since there is no **y** channel below, we use a [cell](https://observablehq.com/plot/marks/cell) instead of a bar.

aquaticsarcheryathleticsbadmintonbasketballboxingcanoecyclingequestrianfencingfootballgolfgymnasticshandballhockeyjudomodern pentathlonrowingrugby sevenssailingshootingtable tennistaekwondotennistriathlonvolleyballweightliftingwrestlingsport [Fork](https://observablehq.com/@observablehq/plot-groups-as-cells "Open on Observable")

js

```
Plot.plot({
  marginBottom: 80,
  x: {tickRotate: 90},
  color: {scheme: "YlGnBu"},
  marks: [\
    Plot.cell(olympians, Plot.groupX({fill: "count"}, {x: "sport"}))\
  ]
})
```

We aren’t limited to the _count_ reducer. We can use the _mode_ reducer, for example, to show which sex is more prevalent in each sport: men are represented more often than women in every sport except gymnastics and fencing.

aquaticsarcheryathleticsbadmintonbasketballboxingcanoecyclingequestrianfencingfootballgolfgymnasticshandballhockeyjudomodern pentathlonrowingrugby sevenssailingshootingtable tennistaekwondotennistriathlonvolleyballweightliftingwrestlingsport [Fork](https://observablehq.com/@observablehq/plot-group-and-mode-reducer "Open on Observable")

js

```
Plot.plot({
  marginBottom: 80,
  x: {tickRotate: 90},
  marks: [\
    Plot.cell(olympians, Plot.groupX({fill: "mode"}, {fill: "sex", x: "sport"}))\
  ]
})
```

You can partition groups using **z**. If **z** is undefined, it defaults to **fill** or **stroke**, if any. In conjunction with the barY mark’s implicit [stackY transform](https://observablehq.com/plot/transforms/stack), this will produce stacked bars.

femalemale

02004006008001,0001,2001,4001,6001,8002,0002,200↑ Frequencyaquaticsarcheryathleticsbadmintonbasketballboxingcanoecyclingequestrianfencingfootballgolfgymnasticshandballhockeyjudomodern pentathlonrowingrugby sevenssailingshootingtable tennistaekwondotennistriathlonvolleyballweightliftingwrestling [Fork](https://observablehq.com/@observablehq/plot-two-class-stacked-bars "Open on Observable")

js

```
Plot.plot({
  marginBottom: 100,
  x: {label: null, tickRotate: 90},
  y: {grid: true},
  color: {legend: true},
  marks: [\
    Plot.barY(olympians, Plot.groupX({y: "count"}, {x: "sport", fill: "sex"})),\
    Plot.ruleY([0])\
  ]
})
```

TIP

You can invoke the stack transform explicitly as `Plot.stackY(Plot.groupX({y: "count"}, {x: "sport", fill: "sex"}))`, producing an identical chart.

You can opt-out of the implicit stackY transform by having groupX generate **y1** or **y2** instead of **y** (and similarly **x1** or **x2** for stackX and groupY). When overlapping marks, use either opacity or blending to make the overlap visible.

femalemale

01002003004005006007008009001,0001,1001,200↑ Frequencyaquaticsarcheryathleticsbadmintonbasketballboxingcanoecyclingequestrianfencingfootballgolfgymnasticshandballhockeyjudomodern pentathlonrowingrugby sevenssailingshootingtable tennistaekwondotennistriathlonvolleyballweightliftingwrestling [Fork](https://observablehq.com/@observablehq/plot-two-class-overlapping-bars "Open on Observable")

js

```
Plot.plot({
  marginBottom: 100,
  x: {label: null, tickRotate: 90},
  y: {grid: true},
  color: {legend: true},
  marks: [\
    Plot.barY(olympians, Plot.groupX({y2: "count"}, {x: "sport", fill: "sex", mixBlendMode: "multiply"})),\
    Plot.ruleY([0])\
  ]
})
```

CAUTION

While the **mixBlendMode** option is useful for mitigating occlusion, it can be slow to render if there are many elements. More than two overlapping histograms may also be hard to read.

Perhaps better would be to make a grouped bar chart using [faceting](https://observablehq.com/plot/features/facets). This is accomplished by setting the **fx** channel to facet horizontally on _sport_, while the **x** channel is used within each facet to draw side-by-side bars for each _sex_. The group transform automatically partitions groups by facet.

femalemale

aquaticsarcheryathleticsbadmintonbasketballboxingcanoecyclingequestrianfencingfootballgolfgymnasticshandballhockeyjudomodern pentathlonrowingrugby sevenssailingshootingtable tennistaekwondotennistriathlonvolleyballweightliftingwrestling01002003004005006007008009001,0001,1001,200↑ Frequency [Fork](https://observablehq.com/@observablehq/plot-olympians-grouped-bar-chart "Open on Observable")

js

```
Plot.plot({
  marginBottom: 100,
  fx: {padding: 0, label: null, tickRotate: 90, tickSize: 6},
  x: {axis: null, paddingOuter: 0.2},
  y: {grid: true},
  color: {legend: true},
  marks: [\
    Plot.barY(olympians, Plot.groupX({y2: "count"}, {x: "sex", fx: "sport", fill: "sex"})),\
    Plot.ruleY([0])\
  ]
})
```

Alternatively, below we use directional arrows (a [link mark](https://observablehq.com/plot/marks/link) with [markers](https://observablehq.com/plot/features/markers)) to indicate the difference in counts of male and female athletes by sport. The color of the arrow indicates which sex is more prevalent, while its length is proportional to the difference.

01002003004005006007008009001,0001,1001,200↑ Frequencyaquaticsarcheryathleticsbadmintonbasketballboxingcanoecyclingequestrianfencingfootballgolfgymnasticshandballhockeyjudomodern pentathlonrowingrugby sevenssailingshootingtable tennistaekwondotennistriathlonvolleyballweightliftingwrestling [Fork](https://observablehq.com/@observablehq/plot-difference-arrows "Open on Observable")

js

```
Plot.plot({
  marginBottom: 100,
  x: {label: null, tickRotate: 90},
  y: {grid: true, label: "Frequency"},
  color: {type: "categorical", domain: [-1, 1], unknown: "#aaa", transform: Math.sign},
  marks: [\
    Plot.ruleY([0]),\
    Plot.link(\
      olympians,\
      Plot.groupX(\
        {\
          y1: (D) => d3.sum(D, (d) => d === "female"),\
          y2: (D) => d3.sum(D, (d) => d === "male"),\
          stroke: (D) => d3.sum(D, (d) => d === "male") - d3.sum(D, (d) => d === "female")\
        },\
        {\
          x: "sport",\
          y1: "sex",\
          y2: "sex",\
          markerStart: "dot",\
          markerEnd: "arrow",\
          stroke: "sex",\
          strokeWidth: 2\
        }\
      )\
    )\
  ]
})
```

The group transform comes in four orientations:

- [groupX](https://observablehq.com/plot/transforms/group#groupX) groups on **x**, and often outputs **y** as in a vertical↑ bar chart;
- [groupY](https://observablehq.com/plot/transforms/group#groupY) groups on **y**, and often outputs **x** as in a horizontal→ bar chart;
- [groupZ](https://observablehq.com/plot/transforms/group#groupZ) groups on _neither_ **x** nor **y**, combining everything into one group; and
- [group](https://observablehq.com/plot/transforms/group#group) groups on _both_ **x** and **y**, and often outputs to **fill** or **r** as in a heatmap.

As you might guess, the groupY transform with the barX mark produces a horizontal→ bar chart. (We must increase the **marginLeft** to avoid the _y_ axis labels from being cut off.)

modern pentathlontriathlongolfarcherytaekwondobadmintontable tennistennisequestrianfencingweightliftingboxingbasketballrugby sevensgymnasticscanoewrestlinghandballsailingvolleyballshootingjudohockeycyclingrowingfootballaquaticsathletics05001,0001,5002,000Frequency → [Fork](https://observablehq.com/@observablehq/plot-sorted-horizontal-bars "Open on Observable")

js

```
Plot.plot({
  marginLeft: 100,
  x: {grid: true},
  y: {label: null},
  marks: [\
    Plot.barX(olympians, Plot.groupY({x: "count"}, {y: "sport", sort: {y: "x"}})),\
    Plot.ruleX([0])\
  ]
})
```

You can produce a two-dimensional heatmap with group transform and a cell mark by generating a **fill** output channel. For example, we could show the median weight of athletes by sport ( **x**) and sex ( **y**).

5060708090100Median weight (kg)femalemaleaquaticsarcheryathleticsbadmintonbasketballboxingcanoecyclingequestrianfencingfootballgolfgymnasticshandballhockeyjudomodern pentathlonrowingrugby sevenssailingshootingtable tennistaekwondotennistriathlonvolleyballweightliftingwrestling [Fork](https://observablehq.com/@observablehq/plot-grouped-olympians-heatmap "Open on Observable")

js

```
Plot.plot({
  marginBottom: 80,
  x: {label: null, tickRotate: 90},
  y: {label: null},
  color: {label: "Median weight (kg)", legend: true, scheme: "YlGnBu"},
  marks: [\
    Plot.cell(olympians, Plot.group({fill: "median"}, {fill: "weight", x: "sport", y: "sex"}))\
  ]
})
```

Or, we could group athletes by sport and the number of gold medals 🥇 won. ( [Michael Phelps](https://en.wikipedia.org/wiki/Michael_Phelps), the most decorated Olympian of all time, won five gold medals in the 2016 Summer Olympics. [Simone Biles](https://en.wikipedia.org/wiki/Simone_Biles) and [Katie Ledecky](https://en.wikipedia.org/wiki/Katie_Ledecky) each won four.)

543210↑ goldaquaticsarcheryathleticsbadmintonbasketballboxingcanoecyclingequestrianfencingfootballgolfgymnasticshandballhockeyjudomodern pentathlonrowingrugby sevenssailingshootingtable tennistaekwondotennistriathlonvolleyballweightliftingwrestling [Fork](https://observablehq.com/@observablehq/plot-olympians-by-gold-medals "Open on Observable")

js

```
Plot.plot({
  marginBottom: 100,
  x: {label: null, tickRotate: 90},
  y: {label: "gold", labelAnchor: "top", labelArrow: true, reverse: true},
  color: {type: "sqrt", scheme: "YlGnBu"},
  marks: [\
    Plot.cell(olympians, Plot.group({fill: "count"}, {x: "sport", y: "gold"}))\
  ]
})
```

We could instead output **r** and use a [dot mark](https://observablehq.com/plot/marks/dot) whose size again represents the number of athletes in each group.

543210↑ goldaquaticsarcheryathleticsbadmintonbasketballboxingcanoecyclingequestrianfencingfootballgolfgymnasticshandballhockeyjudomodern pentathlonrowingrugby sevenssailingshootingtable tennistaekwondotennistriathlonvolleyballweightliftingwrestling [Fork](https://observablehq.com/@observablehq/plot-olympians-by-gold-medals-proportional-dots "Open on Observable")

js

```
Plot.plot({
  marginBottom: 100,
  x: {label: null, tickRotate: 90},
  y: {type: "point", label: "gold", labelAnchor: "top", labelArrow: true, reverse: true},
  r: {range: [0, 12]},
  marks: [\
    Plot.dot(olympians, Plot.group({r: "count"}, {x: "sport", y: "gold"}))\
  ]
})
```

We can add the **stroke** channel to show overlapping distributions by sex.

543210↑ goldaquaticsarcheryathleticsbadmintonbasketballboxingcanoecyclingequestrianfencingfootballgolfgymnasticshandballhockeyjudomodern pentathlonrowingrugby sevenssailingshootingtable tennistaekwondotennistriathlonvolleyballweightliftingwrestling [Fork](https://observablehq.com/@observablehq/plot-olympians-by-gold-medals-overlapping-dots "Open on Observable")

js

```
Plot.plot({
  marginBottom: 100,
  x: {label: null, tickRotate: 90},
  y: {type: "point", label: "gold", labelAnchor: "top", labelArrow: true, reverse: true},
  r: {range: [0, 12]},
  marks: [\
    Plot.dot(olympians, Plot.group({r: "count"}, {x: "sport", y: "gold", stroke: "sex"}))\
  ]
})
```

To group solely on **z** (or **fill** or **stroke**), use [groupZ](https://observablehq.com/plot/transforms/group#groupZ). The single stacked bar chart below (an alternative to a pie chart) shows the proportion of athletes by sport. The _proportion_ reducer converts counts into normalized proportions adding up to 1, while the _first_ reducer pulls out the name of the sport for labeling.

0102030405060708090100Frequency (%) →athleticsaquaticsfootballrowingcyclinghockeyjudoshootingvolleyballsailinghandballwrestlingcanoegymnasticsrugby sevensbasketballboxingweightliftingfencingequestrian [Fork](https://observablehq.com/@observablehq/plot-single-stacked-bar "Open on Observable")

js

```
Plot.plot({
  height: 100,
  x: {percent: true},
  marks: [\
    Plot.barX(\
      olympians,\
      Plot.stackX(\
        {order: "x", reverse: true},\
        Plot.groupZ(\
          {x: "proportion"},\
          {z: "sport", fillOpacity: 0.2, inset: 0.5}\
        )\
      )\
    ),\
    Plot.text(\
      olympians,\
      Plot.filter(\
        (D) => D.length > 200,\
        Plot.stackX(\
          {order: "x", reverse: true},\
          Plot.groupZ(\
            {x: "proportion", text: "first"},\
            {z: "sport", text: "sport", rotate: 90}\
          )\
        )\
      )\
    ),\
    Plot.ruleX([0, 1])\
  ]
})
```

INFO

Although barX applies an implicit stackX transform, [textX](https://observablehq.com/plot/marks/text) does not; this example uses an explicit stackX transform in both cases for clarity, and to pass the additional **order** and **reverse** options to place the largest sport on the left. The [filter transform](https://observablehq.com/plot/transforms/filter) is applied after the stack transform to hide the labels on the smallest sports where the bars are too thin.

## Group options [​](https://observablehq.com/plot/transforms/group\#group-options)

Given input _data_ = \[ _d₀_, _d₁_, _d₂_, …\], by default the resulting grouped data is an array of arrays where each inner array is a subset of the input data such as \[\[ _d₁_, _d₂_, …\], \[ _d₀_, …\], …\]. Each inner array is in input order. The outer array is in input order according to the first element of each group.

By specifying a different reducer for the **data** output, as described below, you can change how the grouped data is computed. The outputs may also include **filter** and **sort** options specified as reducers, and a **reverse** option to reverse the order of generated groups. By default, empty groups are omitted, and non-empty groups are generated in ascending (natural) order.

In addition to data, the following channels are automatically output:

- **x** \- the horizontal position of the group
- **y** \- the vertical position of the group
- **z** \- the first value of the _z_ channel, if any
- **fill** \- the first value of the _fill_ channel, if any
- **stroke** \- the first value of the _stroke_ channel, if any

The **x** output channel is only computed by the groupX and group transform; similarly the **y** output channel is only computed by the groupY and group transform.

You can declare additional output channels by specifying the channel name and desired reducer in the _outputs_ object which is the first argument to the transform. For example, to use groupX to generate a **y** channel of group counts as in a frequency histogram:

js

```
Plot.groupX({y: "count"}, {x: "species"})
```

The following named reducers are supported:

- _first_ \- the first value, in input order
- _last_ \- the last value, in input order
- _count_ \- the number of elements (frequency)
- _sum_ \- the sum of values
- _proportion_ \- the sum proportional to the overall total (weighted frequency)
- _proportion-facet_ \- the sum proportional to the facet total
- _min_ \- the minimum value
- _min-index_ \- the zero-based index of the minimum value
- _max_ \- the maximum value
- _max-index_ \- the zero-based index of the maximum value
- _mean_ \- the mean value (average)
- _median_ \- the median value
- _mode_ \- the value with the most occurrences
- _pXX_ \- the percentile value, where XX is a number in \[00,99\]
- _deviation_ \- the standard deviation
- _variance_ \- the variance per [Welford’s algorithm](https://en.wikipedia.org/wiki/Algorithms_for_calculating_variance#Welford's_online_algorithm)
- _identity_ \- the array of values
- _x_ [^0.6.12](https://github.com/observablehq/plot/releases/tag/v0.6.12 "added in v0.6.12") \- the group’s _x_ value (when grouping on _x_)
- _y_ [^0.6.12](https://github.com/observablehq/plot/releases/tag/v0.6.12 "added in v0.6.12") \- the group’s _y_ value (when grouping on _y_)
- _z_ [^0.6.14](https://github.com/observablehq/plot/releases/tag/v0.6.14 "added in v0.6.14") \- the group’s _z_ value ( _z_, _fill_, or _stroke_)

In addition, a reducer may be specified as:

- a function to be passed the array of values for each group and the extent of the group
- an object with a **reduceIndex** method, an optionally a **scope**

In the last case, the **reduceIndex** method is repeatedly passed three arguments: the index for each group (an array of integers), the input channel’s array of values, and the extent of the group (an object {data, x, y}); it must then return the corresponding aggregate value for the group.

If the reducer object’s **scope** is _data_, then the **reduceIndex** method is first invoked for the full data; the return value of the **reduceIndex** method is then made available as a third argument (making the extent the fourth argument). Similarly if the **scope** is _facet_, then the **reduceIndex** method is invoked for each facet, and the resulting reduce value is made available while reducing the facet’s groups. (This optional **scope** is used by the _proportion_ and _proportion-facet_ reducers.)

Most reducers require binding the output channel to an input channel; for example, if you want the **y** output channel to be a _sum_ (not merely a count), there should be a corresponding **y** input channel specifying which values to sum. If there is not, _sum_ will be equivalent to _count_.

js

```
Plot.groupX({y: "sum"}, {x: "species", y: "body_mass_g"})
```

You can control whether a channel is computed before or after grouping. If a channel is declared only in _options_ (and it is not a special group-eligible channel such as **x**, **y**, **z**, **fill**, or **stroke**), it will be computed after grouping and be passed the grouped data: each datum is the array of input data corresponding to the current group.

js

```
Plot.groupX({y: "count"}, {x: "species", title: (group) => group.map((d) => d.body_mass_g).join("\n")})
```

This is equivalent to declaring the channel only in _outputs_.

js

```
Plot.groupX({y: "count", title: (group) => group.map((d) => d.body_mass_g).join("\n")}, {x: "species"})
```

However, if a channel is declared in both _outputs_ and _options_, then the channel in _options_ is computed before grouping and can be aggregated using any built-in reducer (or a custom reducer function) during the group transform.

js

```
Plot.groupX({y: "count", title: (masses) => masses.join("\n")}, {x: "species", title: "body_mass_g"})
```

If any of **z**, **fill**, or **stroke** is a channel, the first of these channels is considered the _z_ dimension and will be used to subdivide groups.

The default reducer for the **title** channel returns a summary list of the top 5 values with the corresponding number of occurrences.

## group( _outputs_, _options_) [​](https://observablehq.com/plot/transforms/group\#group)

js

```
Plot.group({fill: "count"}, {x: "island", y: "species"})
```

Groups on **x**, **y**, and the first channel of **z**, **fill**, or **stroke**, if any.

## groupX( _outputs_, _options_) [​](https://observablehq.com/plot/transforms/group\#groupX)

js

```
Plot.groupX({y: "sum"}, {x: "species", y: "body_mass_g"})
```

Groups on **x** and the first channel of **z**, **fill**, or **stroke**, if any.

## groupY( _outputs_, _options_) [​](https://observablehq.com/plot/transforms/group\#groupY)

js

```
Plot.groupY({x: "sum"}, {y: "species", x: "body_mass_g"})
```

Groups on **y** and the first channel of **z**, **fill**, or **stroke**, if any.

## groupZ( _outputs_, _options_) [​](https://observablehq.com/plot/transforms/group\#groupZ)

js

```
Plot.groupZ({x: "proportion"}, {fill: "species"})
```

Groups on the first channel of **z**, **fill**, or **stroke**, if any. If none of **z**, **fill**, or **stroke** are channels, then all data (within each facet) is placed into a single group.

## find( _test_) [^0.6.12](https://github.com/observablehq/plot/releases/tag/v0.6.12 "added in v0.6.12") [​](https://observablehq.com/plot/transforms/group\#find)

js

```
Plot.groupX(
  {y1: Plot.find((d) => d.sex === "F"), y2: Plot.find((d) => d.sex === "M")},
  {x: "date", y: "value"}
)
```

Returns a reducer that finds the first datum for which the given _test_ function returns a truthy value, and returns the corresponding channel value. This may be used with the group or bin transform to implement a “pivot wider” transform; for example, a “tall” dataset with separate rows for male and female observations may be transformed into a “wide” dataset with separate columns for male and female values.

Pager

[Previous pageFilter](https://observablehq.com/plot/transforms/filter)

[Next pageHexbin](https://observablehq.com/plot/transforms/hexbin)

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

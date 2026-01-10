---
url: "https://observablehq.com/plot/features/intervals"
title: "Intervals | Plot"
---

# Intervals [^0.6.15](https://github.com/observablehq/plot/releases/tag/v0.6.15 "added in v0.6.15") [​](https://observablehq.com/plot/features/intervals\#intervals)

Plot provides several built-in interval implementations for use with the **tick** option for [scales](https://observablehq.com/plot/features/scales), as the **thresholds** option for a [bin transform](https://observablehq.com/plot/transforms/bin), or other use. See also [d3-time](https://d3js.org/d3-time). You can also implement custom intervals.

At a minimum, intervals implement _interval_. **floor** and _interval_. **offset**. Range intervals additionally implement _interval_. **range**, and nice intervals additionally implement _interval_. **ceil**. These latter implementations are required in some contexts; see Plot’s TypeScript definitions for details.

The _interval_. **floor** method takes a _value_ and returns the corresponding value representing the greatest interval boundary less than or equal to the specified _value_. For example, for the “day” time interval, it returns the preceding midnight:

js

```
Plot.utcInterval("day").floor(new Date("2013-04-12T12:34:56Z")) // 2013-04-12
```

The _interval_. **offset** method takes a _value_ and returns the corresponding value equal to _value_ plus _step_ intervals. If _step_ is not specified it defaults to 1. If _step_ is negative, then the returned value will be less than the specified _value_. For example:

js

```
Plot.utcInterval("day").offset(new Date("2013-04-12T12:34:56Z"), 1) // 2013-04-13T12:34:56Z
Plot.utcInterval("day").offset(new Date("2013-04-12T12:34:56Z"), -2) // 2013-04-10T12:34:56Z
```

The _interval_. **range** method returns an array of values representing every interval boundary greater than or equal to _start_ (inclusive) and less than _stop_ (exclusive). The first value in the returned array is the least boundary greater than or equal to _start_; subsequent values are offset by intervals and floored.

js

```
Plot.utcInterval("week").range(new Date("2013-04-12T12:34:56Z"), new Date("2013-05-12T12:34:56Z")) // [2013-04-14, 2013-04-21, 2013-04-28, 2013-05-05, 2013-05-12]
```

The _interval_. **ceil** method returns the value representing the least interval boundary value greater than or equal to the specified _value_. For example, for the “day” time interval, it returns the preceding midnight:

js

```
Plot.utcInterval("day").ceil(new Date("2013-04-12T12:34:56Z")) // 2013-04-13
```

## numberInterval( _period_) [​](https://observablehq.com/plot/features/intervals\#numberInterval)

js

```
Plot.numberInterval(2)
```

Given a number _period_, returns a corresponding range interval implementation. If _period_ is a negative number, the resulting interval uses 1 / - _period_; this allows more precise results when _period_ is a negative integer. The returned interval implements the _interval_.range, _interval_.floor, and _interval_.offset methods.

## timeInterval( _period_) [​](https://observablehq.com/plot/features/intervals\#timeInterval)

js

```
Plot.timeInterval("2 days")
```

Given a string _period_ describing a local time interval, returns a corresponding nice interval implementation. The period can be _second_, _minute_, _hour_, _day_, _week_, _month_, _quarter_, _half_, _year_, _monday_, _tuesday_, _wednesday_, _thursday_, _friday_, _saturday_, or _sunday_, or a skip interval consisting of a number followed by the interval name (possibly pluralized), such as _3 months_ or _10 years_. The returned interval implements the _interval_.range, _interval_.floor, _interval_.ceil, and _interval_.offset methods.

## utcInterval( _period_) [​](https://observablehq.com/plot/features/intervals\#utcInterval)

js

```
Plot.utcInterval("2 days")
```

Given a string _period_ describing a UTC time interval, returns a corresponding nice interval implementation. The period can be _second_, _minute_, _hour_, _day_, _week_, _month_, _quarter_, _half_, _year_, _monday_, _tuesday_, _wednesday_, _thursday_, _friday_, _saturday_, or _sunday_, or a skip interval consisting of a number followed by the interval name (possibly pluralized), such as _3 months_ or _10 years_. The returned interval implements the _interval_.range, _interval_.floor, _interval_.ceil, and _interval_.offset methods.

Pager

[Previous pageFormats](https://observablehq.com/plot/features/formats)

[Next pageMarkers](https://observablehq.com/plot/features/markers)

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

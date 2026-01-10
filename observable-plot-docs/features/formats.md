---
url: "https://observablehq.com/plot/features/formats"
title: "Formats | Plot"
---

# Formats [​](https://observablehq.com/plot/features/formats\#formats)

These helper functions are provided for convenience as a **tickFormat** option for the [axis mark](https://observablehq.com/plot/marks/axis), as the **text** option for a [text mark](https://observablehq.com/plot/marks/text), or other use. See also [d3-format](https://d3js.org/d3-format), [d3-time-format](https://d3js.org/d3-time-format), and JavaScript’s built-in [date formatting](https://observablehq.com/@mbostock/date-formatting) and [number formatting](https://observablehq.com/@mbostock/number-formatting).

## formatNumber( _locale_) [^0.6.15](https://github.com/observablehq/plot/releases/tag/v0.6.15 "added in v0.6.15") [​](https://observablehq.com/plot/features/formats\#formatNumber)

js

```
Plot.formatNumber("en-US")(Math.PI) // "3.142"
```

Returns a function that formats a given number according to the specified _locale_. The _locale_ is a [BCP 47 language tag](https://tools.ietf.org/html/bcp47) and defaults to U.S. English.

## formatIsoDate( _date_) [​](https://observablehq.com/plot/features/formats\#formatIsoDate)

js

```
Plot.formatIsoDate(new Date("2020-01-01T00:00:00.000Z")) // "2020-01-01"
```

Given a _date_, returns the shortest equivalent ISO 8601 UTC string. If the given _date_ is not valid, returns `"Invalid Date"`. See [isoformat](https://github.com/mbostock/isoformat).

## formatWeekday( _locale_, _format_) [​](https://observablehq.com/plot/features/formats\#formatWeekday)

SunMonTueWedThuFriSat0123456 [Fork](https://observablehq.com/@observablehq/plot-format-helpers "Open on Observable")

js

```
Plot.textX(d3.range(7)).plot({x: {tickFormat: Plot.formatWeekday()}})
```

js

```
Plot.formatWeekday("es-MX", "long")(0) // "domingo"
```

Returns a function that formats a given week day number (from 0 = Sunday to 6 = Saturday) according to the specified _locale_ and _format_. The _locale_ is a [BCP 47 language tag](https://tools.ietf.org/html/bcp47) and defaults to U.S. English. The _format_ is a [weekday format](https://tc39.es/ecma402/#datetimeformat-objects): either _narrow_, _short_, or _long_; if not specified, it defaults to _short_.

## formatMonth( _locale_, _format_) [​](https://observablehq.com/plot/features/formats\#formatMonth)

JanFebMarAprMayJunJulAugSepOctNovDec01234567891011 [Fork](https://observablehq.com/@observablehq/plot-format-helpers "Open on Observable")

js

```
Plot.textX(d3.range(12)).plot({x: {tickFormat: Plot.formatMonth(), ticks: 12}})
```

js

```
Plot.formatMonth("es-MX", "long")(0) // "enero"
```

Returns a function that formats a given month number (from 0 = January to 11 = December) according to the specified _locale_ and _format_. The _locale_ is a [BCP 47 language tag](https://tools.ietf.org/html/bcp47) and defaults to U.S. English. The _format_ is a [month format](https://tc39.es/ecma402/#datetimeformat-objects): either _2-digit_, _numeric_, _narrow_, _short_, _long_; if not specified, it defaults to _short_.

Pager

[Previous pageCurves](https://observablehq.com/plot/features/curves)

[Next pageIntervals](https://observablehq.com/plot/features/intervals)

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

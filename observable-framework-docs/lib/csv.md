---
url: "https://observablehq.com/framework/lib/csv"
title: "Comma-separated values | Observable Framework"
---

1. [Type coercion](https://observablehq.com/framework/lib/csv#type-coercion)

# [Comma-separated values](https://observablehq.com/framework/lib/csv\#comma-separated-values)

To load a [comma-separated values](https://en.wikipedia.org/wiki/Comma-separated_values) (CSV) file, use [`FileAttachment`](https://observablehq.com/framework/files)`.csv`. The `csv`, `tsv`, and `dsv` method implementations are based on [RFC 4180](https://datatracker.ietf.org/doc/html/rfc4180).

```js
const gistemp = FileAttachment("gistemp.csv").csv({typed: true});
```

The value of `gistemp` above is a [promise](https://observablehq.com/framework/reactivity#promises) to an array of objects. In other code blocks, the promise is resolved implicitly and hence you can refer to it as an array of objects.

Array(1644) \[Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, …\]

```js
gistemp
```

The column names are listed in the `columns` property:

Array(2) \["Date", "Anomaly"\]

```js
gistemp.columns
```

You can also load a tab-separated values (TSV) file using `file.tsv`:

```js
const capitals = FileAttachment("us-state-capitals.tsv").tsv({typed: true});
```

|  | State | Capital | Since | Area | Population | MSA/µSA | CSA | Rank |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Alabama | Montgomery | 1846-01-01 | 159.8 | 198,525 | 373,290 | 461,516 | 3 |
|  | Alaska | Juneau | 1906-01-01 | 2,716.7 | 32,113 | 32,113 |  | 3 |
|  | Arizona | Phoenix | 1912-01-01 | 517.6 | 1,680,992 | 4,948,203 | 5,002,221 | 1 |
|  | Arkansas | Little Rock | 1821-01-01 | 116.2 | 197,312 | 742,384 | 908,941 | 1 |
|  | California | Sacramento | 1854-01-01 | 97.9 | 513,624 | 2,363,730 | 2,639,124 | 6 |
|  | Colorado | Denver | 1867-01-01 | 153.3 | 727,211 | 2,967,239 | 3,617,927 | 1 |
|  | Connecticut | Hartford | 1875-01-01 | 17.3 | 122,105 | 1,204,877 | 1,470,083 | 3 |
|  | Delaware | Dover | 1777-01-01 | 22.4 | 38,079 | 180,786 | 7,209,620 | 2 |
|  | Florida | Tallahassee | 1824-01-01 | 95.7 | 194,500 | 387,227 |  | 7 |
|  | Georgia | Atlanta | 1868-01-01 | 133.5 | 506,811 | 6,020,364 | 6,853,392 | 1 |
|  | Hawaii | Honolulu | 1845-01-01 | 68.4 | 345,064 | 974,563 |  | 1 |
|  | Idaho | Boise | 1865-01-01 | 63.8 | 228,959 | 749,202 | 831,235 | 1 |
|  | Illinois | Springfield | 1837-01-01 | 54 | 114,230 | 206,868 | 306,399 | 6 |
|  | Indiana | Indianapolis | 1825-01-01 | 361.5 | 876,384 | 2,074,537 | 2,457,286 | 1 |
|  | Iowa | Des Moines | 1857-01-01 | 75.8 | 214,237 | 699,292 | 877,991 | 1 |
|  | Kansas | Topeka | 1856-01-01 | 56 | 125,310 | 231,969 |  | 4 |
|  | Kentucky | Frankfort | 1792-01-01 | 14.7 | 27,679 | 73,663 | 745,033 | 15 |
|  | Louisiana | Baton Rouge | 1880-01-01 | 76.8 | 220,236 | 854,884 |  | 2 |
|  | Maine | Augusta | 1832-01-01 | 55.4 | 18,681 | 122,302 |  | 8 |
|  | Maryland | Annapolis | 1694-01-01 | 6.73 | 39,174 | 2,800,053 | 9,814,928 | 7 |
|  | Massachusetts | Boston | 1630-01-01 | 89.6 | 692,600 | 4,873,019 | 8,287,710 | 1 |
|  | Michigan | Lansing | 1847-01-01 | 35 | 118,210 | 550,391 |  | 5 |
|  | Minnesota | Saint Paul | 1849-01-01 | 52.8 | 308,096 | 3,654,908 | 4,027,861 | 2 |

```js
Inputs.table(capitals)
```

For a different delimiter, use `file.dsv`. [Added in 1.6.0](https://github.com/observablehq/framework/releases/tag/v1.6.0 "Added in 1.6.0") For example, for semicolon separated values:

```js
const capitals = FileAttachment("us-state-capitals.csv").dsv({delimiter: ";", typed: true});
```

## [Type coercion](https://observablehq.com/framework/lib/csv\#type-coercion)

A common pitfall with CSV is that it is untyped: numbers, dates, booleans, and every other possible value are represented as text and there is no universal way to automatically determine the correct type.

For example, a map might identify U.S. states by [FIPS code](https://transition.fcc.gov/oet/info/maps/census/fips/fips.txt) — Alabama as `"01"`, Michigan as `"26"`, and so on — and these identifiers should be treated as strings when looking up the values in your dataset. But in other cases — say if `1` and `26` represent temperature in degrees Celsius — you should convert these values to numbers before doing math or passing them to [Observable Plot](https://observablehq.com/framework/lib/plot). If you don’t type your data, you may inadvertently concatenate when you meant to add, or get an ordinal rather than quantitative scale. You should type data as early as possible — when you load it — to prevent unexpected behavior later.

Dates can be particularly challenging in CSV as there are myriad ways to encode dates as text. We recommend [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) and [UTC](https://en.wikipedia.org/wiki/Coordinated_Universal_Time).

To coerce types automatically, set the **typed** option to true with `file.csv` or `file.tsv`. This uses [`d3.autoType`](https://d3js.org/d3-dsv#autoType) to infer types and then coerce them.

If your file is not compatible with `d3.autoType`, you may get unexpected or invalid results; you should inspect the returned data and if needed use `{typed: false}` (the default) and coerce the types yourself. Here is an example of coercing types manually using a custom date format:

```js
import {utcParse} from "npm:d3-time-format";

const parseDate = utcParse("%Y-%m-%d");
const coerceRow = (d) => ({Date: parseDate(d.Date), Anomaly: Number(d.Anomaly)});
const gistemp = FileAttachment("gistemp.csv").csv().then((D) => D.map(coerceRow));
```

Above, any date value that does not match the expected format will be cast as an `Invalid Date`, and any anomaly value that is not a number (as when the file says `N/A` to represent missing data) will be cast as `NaN`.

The `file.csv` and `file.tsv` methods assume that the first line of the file is a header indicating the (distinct) name of each column. Each subsequent line is considered as a row and converted to an object with the column names as keys.

If your file does not have such a header line, set the **array** option to true to get back an array of arrays instead:

Array(1645) \[Array(2), Array(2), Array(2), Array(2), Array(2), Array(2), Array(2), Array(2), Array(2), Array(2), Array(2), Array(2), Array(2), Array(2), Array(2), Array(2), Array(2), Array(2), Array(2), Array(2), …\]

```js
FileAttachment("gistemp.csv").csv({array: true, typed: true})
```

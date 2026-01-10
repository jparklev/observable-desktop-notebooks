---
url: "https://observablehq.com/framework/lib/arrow"
title: "Apache Arrow | Observable Framework"
---

1. [Apache Parquet](https://observablehq.com/framework/lib/arrow#apache-parquet)

# [Apache Arrow](https://observablehq.com/framework/lib/arrow\#apache-arrow)

[Apache Arrow](https://arrow.apache.org/) “defines a language-independent columnar memory format for flat and hierarchical data, organized for efficient analytic operations.” You will probably not consume it directly, but it is used by [Arquero](https://observablehq.com/framework/lib/arquero), [DuckDB](https://observablehq.com/framework/lib/duckdb), and other libraries to handle data efficiently.

To load an [Arrow IPC file](https://arrow.apache.org/docs/format/Columnar.html#format-ipc), use [`FileAttachment`](https://observablehq.com/framework/files).

```js
const flights = FileAttachment("flights-200k.arrow").arrow();
```

This returns a [promise](https://observablehq.com/framework/reactivity#promises) to an [Arrow table](https://arrow.apache.org/docs/js/classes/Arrow_dom.Table.html).

Da {schema: Schema, batches: Array(1), \_offsets: Uint32Array(2)}

```js
flights
```

This table records 231,083 flights. It’s easier to inspect as an array of rows:

Array(231083) \[Row, Row, Row, Row, Row, Row, Row, Row, Row, Row, Row, Row, Row, Row, Row, Row, Row, Row, Row, Row, …\]

```js
[...flights]
```

Or using [`Inputs.table`](https://observablehq.com/framework/inputs/table):

|  | delay | distance | time |
| --- | --- | --- | --- |
|  | 14 | 405 | 0.017 |
|  | -11 | 370 | 5.5 |
|  | 5 | 389 | 5.667 |
|  | -5 | 337 | 6 |
|  | 3 | 303 | 6 |
|  | 5 | 236 | 6.083 |
|  | -4 | 405 | 6.167 |
|  | -2 | 188 | 6.25 |
|  | 0 | 197 | 6.25 |
|  | 0 | 399 | 6.25 |
|  | 5 | 562 | 6.25 |
|  | -5 | 358 | 6.333 |
|  | 0 | 491 | 6.333 |
|  | -6 | 361 | 6.417 |
|  | 0 | 313 | 6.417 |
|  | 1 | 271 | 6.417 |
|  | 5 | 689 | 6.417 |
|  | -1 | 487 | 6.5 |
|  | -10 | 399 | 6.5 |
|  | -15 | 621 | 6.5 |
|  | -2 | 361 | 6.5 |
|  | -3 | 220 | 6.5 |
|  | -3 | 397 | 6.5 |

```js
Inputs.table(flights)
```

We can visualize the distribution of flight delays with a [Plot rect mark](https://observablehq.com/plot/marks/rect) and [bin transform](https://observablehq.com/plot/transforms/bin):

051015202530354045↑ Flights (thousands)−50050100150delay →

```js
Plot.plot({
  y: {
    transform: (d) => d / 1000,
    label: "Flights (thousands)"
  },
  marks: [\
    Plot.rectY(flights, Plot.binX({y: "count"}, {x: "delay", interval: 5, fill: "var(--theme-blue)"})),\
    Plot.ruleY([0])\
  ]
})
```

You can also work directly with the Apache Arrow API to create in-memory tables. Apache Arrow is available by default as `Arrow` in Markdown, but you can import it explicitly like so:

```js
import * as Arrow from "npm:apache-arrow";
```

For example, to create a table representing a year-long random walk:

```js
const date = d3.utcDay.range(new Date("2023-01-01"), new Date("2024-01-02"));
const random = d3.randomNormal.source(d3.randomLcg(42))(); // seeded random
const value = d3.cumsum(date, random);
const table = Arrow.tableFromArrays({date, value});
```

Visualized with [Plot’s difference mark](https://observablehq.com/plot/marks/difference):

−8−6−4−202468101214161820↑ valueJan2023FebMarAprMayJunJulAugSepOctNovDecJan2024

```js
Plot.plot({
  x: {type: "utc"},
  marks: [\
    Plot.ruleY([0]),\
    Plot.differenceY(table, {x: "date", y: "value"})\
  ]
})
```

The chart above specifies _x_ as a UTC scale because Apache Arrow represents dates as numbers (milliseconds since [Unix epoch](https://en.wikipedia.org/wiki/Epoch_(computing))) rather than Date objects; without this hint, Plot would assume that _date_ column is quantitative rather than temporal and produce a less legible axis.

## [Apache Parquet](https://observablehq.com/framework/lib/arrow\#apache-parquet)

The [Apache Parquet](https://parquet.apache.org/) format is optimized for storage and transfer. To load a Parquet file — such as this sample of 250,000 stars from the [Gaia Star Catalog](https://observablehq.com/@cmudig/peeking-into-the-gaia-star-catalog) — use [`FileAttachment`](https://observablehq.com/framework/files). This is implemented using Kyle Barron’s [parquet-wasm](https://kylebarron.dev/parquet-wasm/) library.

```js
const gaia = FileAttachment("gaia-sample.parquet").parquet();
```

Like `file.arrow`, this returns an Arrow table.

Da {schema: Schema, batches: Array(245), \_offsets: Uint32Array(246)}

```js
gaia
```

|  | source\_id | ra | dec | parallax | parallax\_error | phot\_g\_mean\_mag | bp\_rp | dr2\_radial\_velocity | dr2\_radial\_velocity\_error |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | 1,870,084,251,657,671,040 | 313.268 | 36.766 | 0.183 | 0.123 | 18.439 | 1.291 |  |  |
|  | 5,878,343,892,046,245,376 | 217.941 | -61.587 | 0.23 | 0.116 | 18.057 | 2.154 |  |  |
|  | 2,028,328,031,008,716,288 | 297.95 | 27.565 | -0.502 | 0.515 | 20.204 | 2.217 |  |  |
|  | 2,076,498,116,457,016,960 | 294.708 | 40.148 | -0.097 | 0.331 | 19.944 | 0.941 |  |  |
|  | 4,315,266,827,603,868,160 | 294.747 | 12.216 | 0.63 | 0.987 | 20.557 | 1.25 |  |  |
|  | 4,123,529,214,004,874,624 | 264.558 | -17.433 | 1.318 | 0.949 | 19.511 | 1.275 |  |  |
|  | 5,312,548,578,630,777,344 | 141.799 | -51.545 |  |  | 21.115 | 1.876 |  |  |
|  | 4,650,844,304,713,528,704 | 84.676 | -72.54 |  |  | 20.737 | 0.23 |  |  |
|  | 1,826,703,952,413,405,568 | 297.763 | 21.162 | 0.055 | 0.296 | 19.601 | 1.56 |  |  |
|  | 6,028,595,665,071,486,592 | 255.557 | -30.387 | 0.874 | 0.098 | 16.767 | 1.367 |  |  |
|  | 1,824,295,815,826,574,720 | 294.831 | 18.218 | 0.215 | 0.06 | 16.709 | 2.578 |  |  |
|  | 5,796,748,653,096,620,032 | 221.589 | -73.26 | 0.055 | 0.178 | 18.729 | 0.979 |  |  |
|  | 5,986,065,318,262,022,016 | 236.742 | -48.249 | 0.04 | 0.907 | 20.291 | 2.257 |  |  |
|  | 5,242,713,608,675,530,624 | 147.164 | -70.046 | 0.157 | 0.304 | 19.792 | 1.365 |  |  |
|  | 5,837,366,369,273,836,160 | 192.9 | -75.475 | 0.425 | 0.108 | 18.279 | 1.39 |  |  |
|  | 4,474,534,965,207,478,272 | 270.945 | 6.181 | 0.508 | 0.199 | 18.449 | 2.208 |  |  |
|  | 273,058,043,402,287,104 | 72.369 | 53.298 | 0.17 | 0.134 | 18.047 | 1.577 |  |  |
|  | 6,062,031,195,094,070,528 | 200.97 | -59.028 | 0.432 | 0.183 | 18.399 | 1.997 |  |  |
|  | 4,116,979,144,049,523,328 | 265.755 | -22.338 |  |  | 20.447 |  |  |  |
|  | 2,040,968,355,983,155,712 | 286.176 | 30.499 | 0.129 | 0.147 | 18.663 | 1.38 |  |  |
|  | 5,336,084,415,334,864,640 | 172.484 | -60.091 | 0.417 | 0.031 | 15.797 | 1.021 |  |  |
|  | 5,871,896,772,471,721,344 | 206.382 | -57.429 |  |  | 20.929 | 1.264 |  |  |
|  | 4,062,539,785,017,096,960 | 269.575 | -28.994 | 0.952 | 0.27 | 18.207 | 1.628 |  |  |

```js
Inputs.table(gaia)
```

We can [plot](https://observablehq.com/framework/lib/plot) these stars binned by intervals of 2° to reveal the [Milky Way](https://en.wikipedia.org/wiki/Milky_Way).

−80−60−40−20020406080↑ dec050100150200250300350ra →

```js
Plot.plot({
  aspectRatio: 1,
  marks: [\
    Plot.frame({fill: 0}),\
    Plot.rect(gaia, Plot.bin({fill: "count"}, {x: "ra", y: "dec", interval: 2, inset: 0}))\
  ]
})
```

Parquet files work especially well with [DuckDB](https://observablehq.com/framework/lib/duckdb) for in-process SQL queries. The Parquet format is optimized for this use case: data is compressed in a columnar format, allowing DuckDB to load only the subset of data needed (via [range requests](https://developer.mozilla.org/en-US/docs/Web/HTTP/Range_requests)) to execute the current query. This can give a huge performance boost when working with larger datasets.

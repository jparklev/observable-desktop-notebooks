---
url: "https://observablehq.com/framework/lib/xlsx"
title: "Microsoft Excel (XLSX) | Observable Framework"
---

# [Microsoft Excel (XLSX)](https://observablehq.com/framework/lib/xlsx\#microsoft-excel-xlsx)

[`FileAttachment`](https://observablehq.com/framework/files) supports the [Microsoft Excel Open XML format](https://en.wikipedia.org/wiki/Office_Open_XML) via the `file.xlsx` method. This is implemented using the MIT-licensed [ExcelJS](https://github.com/exceljs/exceljs) library.

```js
const workbook = FileAttachment("laser-report.xlsx").xlsx();
```

This returns a [promise](https://observablehq.com/framework/reactivity#promises) to a `Workbook` instance.

Workbook {sheetNames: Array(1)}

```js
workbook
```

The workbook’s sheet names are exposed as `workbook.sheetNames`.

Array(1) \["Laser Report 2020"\]

```js
workbook.sheetNames
```

To load a sheet, call `workbook.sheet`, passing in a sheet name. You can also pass a **range** option to indicate which part of the sheet to materialize, such as `A:J` for columns A through J (inclusive) or `B4:K123` for column B, row 4 through column K, row 123. The **headers** option indicates whether to treat the first row of the given range as column names. If the **headers** option is false, the default, the returned object properties will reflect the column letters.

```js
const reports = workbook.sheet("Laser Report 2020", {range: "A:J", headers: true});
```

This returns an array of objects.

Array(6852) \[Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, …\]

```js
reports
```

Each object represents a row, and each object property represents a cell value. Values may be represented as numbers, strings, booleans, Date objects, or [other values](https://github.com/exceljs/exceljs/blob/master/README.md#value-types). Row numbers are also exposed as a non-enumerable `#` property to assist with recognition and range specification.

We can display these objects using [`Inputs.table`](https://observablehq.com/framework/inputs/table):

|  | # | Incident Date | Incident Time | Flight ID | Aircraft | Altitude | Airport | Laser Color | Injury | City | State |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | 2 | 2020-01-01 | 148 | N424RP | DA42/A | 8,500 | SBA | Green | No | Santa Barbara | California |
|  | 3 | 2020-01-01 | 155 | AMF1829 | B190 | 40,000 | SSF | Green | No | San Antonio | Texas |
|  | 4 | 2020-01-01 | 214 | NKS1881 | A320 | 2,500 | TPA | Green | No | Tampa | Florida |
|  | 5 | 2020-01-01 | 217 | FDX3873 | B763 | 3,000 | DFW | Green | No | Dallas-Fort Worth | Texas |
|  | 6 | 2020-01-01 | 218 | SWA3635 | B739 | 11,000 | MOD | Green | No | Modesto | California |
|  | 7 | 2020-01-01 | 239 | PCOP1 | HELO | 1,200 | MDW | Green | No | Chicago | Illinois |
|  | 8 | 2020-01-01 | 243 | AAL473 | A320 | 22,000 | DEN | Green | No | Denver | Colorado |
|  | 9 | 2020-01-01 | 310 | SWA6092 | B737 | 11,000 | SNS | Green | No | Salinas | California |
|  | 10 | 2020-01-01 | 325 | DAL930 | A319 | 5,000 | MYF | Green | No | San Diego | California |
|  | 11 | 2020-01-01 | 435 | DAL1211 | A320 | 7,500 | LAX | Green | No | Los Angeles | California |
|  | 12 | 2020-01-01 | 437 | UAL309 | B753 | 10,000 | LAX | Green | No | Los Angeles | California |
|  | 13 | 2020-01-01 | 505 | ASQ4195 | E145 | 10,000 | JAX | Green | No | Jacksonville | Florida |
|  | 14 | 2020-01-01 | 510 | QXE2564 | E75L | 3,500 | SNA | Purple | No | Santa Ana | California |
|  | 15 | 2020-01-01 | 550 | ENY4136 | E145 | 12,000 | DLH | Green | No | Duluth | Minnesota |
|  | 16 | 2020-01-01 | 600 | CKS1820 | B767 | 16,000 | SBA | Green | No | Santa Barbara | California |
|  | 17 | 2020-01-01 | 605 | PAC997 | B747 | 17,000 | SBA | Green | No | Santa Barbara | California |
|  | 18 | 2020-01-01 | 658 | DAL8838 | B757 | 11,500 | HKY | Green | No | Hickory | North Carolina |
|  | 19 | 2020-01-01 | 805 | N736UG | C172 | 2,500 | YKM | Green | No | Yakima | Washington |
|  | 20 | 2020-01-01 | 903 | N85PH | BE9L | 10,000 | MAF | Green | No | Midland | Texas |
|  | 21 | 2020-01-01 | 1,020 | N232HH | R44 | 1,500 | OGG | Green | No | Kahului | Hawaii |
|  | 22 | 2020-01-01 | 2,325 | UCA5007 | E45X | 10,000 | CLE | Green | No | Cleveland | Ohio |
|  | 23 | 2020-01-02 | 14 | JIA5416 | CRJ2 | 1,700 | CAK | Green | No | North Canton | Ohio |
|  | 24 | 2020-01-02 | 20 | N6234W | P28A | 6,000 | GSP | Green | No | Greer | South Carolina |

```js
Inputs.table(reports)
```

Or as a scatterplot using [`Plot.dot`](https://observablehq.com/plot/marks/dot):

0102030405060708090100↑ Altitude (feet, thousands)Jan2020FebMarAprMayJunJulAugSepOctNovDecIncident Date →

```js
Plot.plot({
  y: {
    label: "Altitude (feet, thousands)",
    domain: [0, 100],
    transform: (y) => y / 1000,
    grid: true,
    clamp: true
  },
  marks: [\
    Plot.ruleY([0]),\
    Plot.dot(reports, {x: "Incident Date", y: "Altitude", r: 1, stroke: "Incident Time", tip: true})\
  ]
})
```

Some additional details on values: dates are interpreted as UTC; formula results are included, but formula definitions ignored and formula errors are represented as `NaN`; hyperlinks are returned as strings, with a space between URL and text if they differ; empty rows are kept, but empty cells are skipped (row objects will lack properties for missing values).

If you’d prefer to use [ExcelJS](https://github.com/exceljs/exceljs) directly, you can import it like so:

```js
import Excel from "npm:exceljs";
```

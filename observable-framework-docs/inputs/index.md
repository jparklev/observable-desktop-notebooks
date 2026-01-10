---
url: "https://observablehq.com/framework/inputs/"
title: "Observable Inputs | Observable Framework"
---

# [Observable Inputs](https://observablehq.com/framework/inputs/\#observable-inputs)

[Observable Inputs](https://github.com/observablehq/inputs) provides “lightweight interface components — buttons, sliders, dropdowns, tables, and the like — to help you explore data and build interactive displays.” Observable Inputs is available by default as `Inputs` in Markdown, but you can import it explicitly like so:

```js
import * as Inputs from "npm:@observablehq/inputs";
```

Or, just import the specific inputs you want:

```js
import {button, color} from "npm:@observablehq/inputs";
```

Inputs are typically passed to the [`view` function](https://observablehq.com/framework/reactivity#inputs) for display, while exposing the input’s [value generator](https://observablehq.com/framework/reactivity#generators) as a [reactive variable](https://observablehq.com/framework/reactivity). Options differ between inputs. For example, the checkbox input accepts options to disable all or certain values, sort displayed values, and only display repeated values _once_ (among others):

Choose categories:

ABDGZ⚠️F⚠️Q

```js
const checkout = view(
  Inputs.checkbox(["B", "A", "Z", "Z", "⚠️F", "D", "G", "G", "G", "⚠️Q"], {
    disabled: ["⚠️F", "⚠️Q"],
    sort: true,
    unique: true,
    value: "B",
    label: "Choose categories:"
  })
);
```

Array(1) \["B"\]

```js
checkout
```

To demonstrate Observable Inputs, let’s look at a sample dataset of athletes from the 2016 Rio olympics via [Matt Riggott](https://flother.is/2017/olympic-games-data/). Here’s a [table input](https://observablehq.com/framework/inputs/table) — always a good starting point for an agnostic view of the data:

|  | id | name | nationality | sex | date\_of\_birth | height | weight | sport | gold | silver | bronze | info |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | A Jesus Garcia | ESP | male | 1969-10-17 | 1.72 | 64 | athletics | 0 | 0 | 0 |  |
|  |  | A Lam Shin | KOR | female | 1986-09-23 | 1.68 | 56 | fencing | 0 | 0 | 0 |  |
|  |  | Aaron Brown | CAN | male | 1992-05-27 | 1.98 | 79 | athletics | 0 | 0 | 1 |  |
|  |  | Aaron Cook | MDA | male | 1991-01-02 | 1.83 | 80 | taekwondo | 0 | 0 | 0 |  |
|  |  | Aaron Gate | NZL | male | 1990-11-26 | 1.81 | 71 | cycling | 0 | 0 | 0 |  |
|  |  | Aaron Royle | AUS | male | 1990-01-26 | 1.8 | 67 | triathlon | 0 | 0 | 0 |  |
|  |  | Aaron Russell | USA | male | 1993-06-04 | 2.05 | 98 | volleyball | 0 | 0 | 1 |  |
|  |  | Aaron Younger | AUS | male | 1991-09-25 | 1.93 | 100 | aquatics | 0 | 0 | 0 |  |
|  |  | Aauri Lorena Bokesa | ESP | female | 1988-12-14 | 1.8 | 62 | athletics | 0 | 0 | 0 |  |
|  |  | Ababel Yeshaneh | ETH | female | 1991-07-22 | 1.65 | 54 | athletics | 0 | 0 | 0 |  |
|  |  | Abadi Hadis | ETH | male | 1997-11-06 | 1.7 | 63 | athletics | 0 | 0 | 0 |  |
|  |  | Abbas Abubakar Abbas | BRN | male | 1996-05-17 | 1.75 | 66 | athletics | 0 | 0 | 0 |  |
|  |  | Abbas Qali | IOA | male | 1992-10-11 |  |  | aquatics | 0 | 0 | 0 |  |
|  |  | Abbey D'Agostino | USA | female | 1992-05-25 | 1.61 | 49 | athletics | 0 | 0 | 0 |  |
|  |  | Abbey Weitzeil | USA | female | 1996-12-03 | 1.78 | 68 | aquatics | 1 | 1 | 0 |  |
|  |  | Abbie Brown | GBR | female | 1996-04-10 | 1.76 | 71 | rugby sevens | 0 | 0 | 0 |  |
|  |  | Abbos Rakhmonov | UZB | male | 1998-07-07 | 1.61 | 57 | wrestling | 0 | 0 | 0 |  |
|  |  | Abbubaker Mobara | RSA | male | 1994-02-18 | 1.75 | 64 | football | 0 | 0 | 0 |  |
|  |  | Abby Erceg | NZL | female | 1989-11-20 | 1.75 | 68 | football | 0 | 0 | 0 |  |
|  |  | Abd Elhalim Mohamed Abou | EGY | male | 1989-06-03 | 2.1 | 88 | volleyball | 0 | 0 | 0 |  |
|  |  | Abdalaati Iguider | MAR | male | 1987-03-25 | 1.73 | 57 | athletics | 0 | 0 | 0 |  |
|  |  | Abdalelah Haroun | QAT | male | 1997-01-01 | 1.85 | 80 | athletics | 0 | 0 | 0 |  |
|  |  | Abdalla Targan | SUD | male | 1996-09-28 | 1.77 | 65 | athletics | 0 | 0 | 0 |  |

```js
Inputs.table(olympians)
```

Tables can be inputs, too! The value of the table is the subset of rows that you select using the checkboxes in the first column.

Now let’s wire up the table to a [search input](https://observablehq.com/framework/inputs/search). Type anything into the box and the search input will find the matching rows in the data. The value of the search input is the subset of rows that match the query.

A few examples to try: **\[mal\]** will match _sex_ = male, but also names that start with “mal”, such as Anna Malova; **\[1986\]** will match anyone born in 1986 (and a few other results); **\[USA gym\]** will match USA’s gymnastics team. Each space-separated term in your query is prefix-matched against all columns in the data.

11,538 results

```js
const searchResults = view(Inputs.search(olympians, {
  datalist: ["mal", "1986", "USA gym"],
  placeholder: "Search athletes"
}))
```

|  | id | name | nationality | sex | date\_of\_birth | height | weight | sport | gold | silver | bronze | info |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | A Jesus Garcia | ESP | male | 1969-10-17 | 1.72 | 64 | athletics | 0 | 0 | 0 |  |
|  |  | A Lam Shin | KOR | female | 1986-09-23 | 1.68 | 56 | fencing | 0 | 0 | 0 |  |
|  |  | Aaron Brown | CAN | male | 1992-05-27 | 1.98 | 79 | athletics | 0 | 0 | 1 |  |
|  |  | Aaron Cook | MDA | male | 1991-01-02 | 1.83 | 80 | taekwondo | 0 | 0 | 0 |  |
|  |  | Aaron Gate | NZL | male | 1990-11-26 | 1.81 | 71 | cycling | 0 | 0 | 0 |  |
|  |  | Aaron Royle | AUS | male | 1990-01-26 | 1.8 | 67 | triathlon | 0 | 0 | 0 |  |
|  |  | Aaron Russell | USA | male | 1993-06-04 | 2.05 | 98 | volleyball | 0 | 0 | 1 |  |
|  |  | Aaron Younger | AUS | male | 1991-09-25 | 1.93 | 100 | aquatics | 0 | 0 | 0 |  |
|  |  | Aauri Lorena Bokesa | ESP | female | 1988-12-14 | 1.8 | 62 | athletics | 0 | 0 | 0 |  |
|  |  | Ababel Yeshaneh | ETH | female | 1991-07-22 | 1.65 | 54 | athletics | 0 | 0 | 0 |  |
|  |  | Abadi Hadis | ETH | male | 1997-11-06 | 1.7 | 63 | athletics | 0 | 0 | 0 |  |
|  |  | Abbas Abubakar Abbas | BRN | male | 1996-05-17 | 1.75 | 66 | athletics | 0 | 0 | 0 |  |
|  |  | Abbas Qali | IOA | male | 1992-10-11 |  |  | aquatics | 0 | 0 | 0 |  |
|  |  | Abbey D'Agostino | USA | female | 1992-05-25 | 1.61 | 49 | athletics | 0 | 0 | 0 |  |
|  |  | Abbey Weitzeil | USA | female | 1996-12-03 | 1.78 | 68 | aquatics | 1 | 1 | 0 |  |
|  |  | Abbie Brown | GBR | female | 1996-04-10 | 1.76 | 71 | rugby sevens | 0 | 0 | 0 |  |
|  |  | Abbos Rakhmonov | UZB | male | 1998-07-07 | 1.61 | 57 | wrestling | 0 | 0 | 0 |  |
|  |  | Abbubaker Mobara | RSA | male | 1994-02-18 | 1.75 | 64 | football | 0 | 0 | 0 |  |
|  |  | Abby Erceg | NZL | female | 1989-11-20 | 1.75 | 68 | football | 0 | 0 | 0 |  |
|  |  | Abd Elhalim Mohamed Abou | EGY | male | 1989-06-03 | 2.1 | 88 | volleyball | 0 | 0 | 0 |  |
|  |  | Abdalaati Iguider | MAR | male | 1987-03-25 | 1.73 | 57 | athletics | 0 | 0 | 0 |  |
|  |  | Abdalelah Haroun | QAT | male | 1997-01-01 | 1.85 | 80 | athletics | 0 | 0 | 0 |  |
|  |  | Abdalla Targan | SUD | male | 1996-09-28 | 1.77 | 65 | athletics | 0 | 0 | 0 |  |

```js
Inputs.table(searchResults)
```

You can sort columns by clicking on the column name: click once to sort ascending, and click again to sort descending. Note that the sort order is temporary: it’ll go away if you reload the page. Specify the column name as the _sort_ option above if you want this order to persist.

For a more structured approach, we can use a select input to choose a sport, then _array_.filter to determine which rows are shown in the table. The _sort_ and _unique_ options tell the input to show only distinct values and to sort them alphabetically. Try comparing the **\[gymnastics\]** and **\[basketball\]** sports.

sportaquaticsarcheryathleticsbadmintonbasketballcanoecyclingequestrianfencingfootballgolfgymnasticshandballhockeyjudomodern pentathlonrowingrugby sevenssailingshootingtable tennistaekwondotennistriathlonvolleyballweightliftingwrestling

```js
const sport = view(
  Inputs.select(
    olympians.filter((d) => d.weight && d.height).map((d) => d.sport),
    {sort: true, unique: true, label: "sport"}
  )
);
```

## How aquatics athletes compare

1.31.41.51.61.71.81.92.02.12.2↑ height406080100120140160weight →

```js
Plot.plot({
  title: `How ${sport} athletes compare`,
  marks: [\
    Plot.dot(olympians, {x: "weight", y: "height"}),\
    Plot.dot(olympians.filter((d) => d.sport === sport), {x: "weight", y: "height", stroke: "red"})\
  ]
})
```

You can pass grouped data to a [select input](https://observablehq.com/framework/inputs/select) as a [Map](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map) from key to array of values, say using [d3.group](https://d3js.org/d3-array/group). The value of the select input in this mode is the data in the selected group. Note that _unique_ is no longer required, and that _sort_ works here, too, sorting the keys of the map returned by d3.group.

sportaquaticsarcheryathleticsbadmintonbasketballboxingcanoecyclingequestrianfencingfootballgolfgymnasticshandballhockeyjudomodern pentathlonrowingrugby sevenssailingshootingtable tennistaekwondotennistriathlonvolleyballweightliftingwrestling

```js
const sportAthletes = view(
  Inputs.select(
    d3.group(olympians, (d) => d.sport),
    {sort: true, label: "sport"}
  )
);
```

|  | name | nationality | sex | date\_of\_birth | height | weight | sport | gold | silver | bronze |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Aaron Younger | AUS | male | 1991-09-25 | 1.93 | 100 | aquatics | 0 | 0 | 0 |
|  | Abbas Qali | IOA | male | 1992-10-11 |  |  | aquatics | 0 | 0 | 0 |
|  | Abbey Weitzeil | USA | female | 1996-12-03 | 1.78 | 68 | aquatics | 1 | 1 | 0 |
|  | Abdelaziz Mohamed Ahmed | SUD | male | 1994-10-12 | 1.81 | 72 | aquatics | 0 | 0 | 0 |
|  | Abdoul Khadre Mbaye Niane | SEN | male | 1988-08-20 | 1.9 | 90 | aquatics | 0 | 0 | 0 |
|  | Abeku Gyekye Jackson | GHA | male | 2000-04-12 |  |  | aquatics | 0 | 0 | 0 |
|  | Abigail Johnston | USA | female | 1989-11-16 | 1.66 | 61 | aquatics | 0 | 0 | 0 |
|  | Adam Decker | HUN | male | 1984-02-29 | 2.03 | 115 | aquatics | 0 | 0 | 0 |
|  | Adam Peaty | GBR | male | 1994-12-28 | 1.93 | 88 | aquatics | 1 | 1 | 0 |
|  | Adam Telegdy | HUN | male | 1995-11-01 | 1.94 | 77 | aquatics | 0 | 0 | 0 |
|  | Adam Viktora | SEY | male | 1996-09-06 | 1.88 | 94 | aquatics | 0 | 0 | 0 |
|  | Adrian Baches | BRA | male | 1990-04-07 | 1.84 | 83 | aquatics | 0 | 0 | 0 |
|  | Adzo Rebecca Kpossi | TOG | female | 1999-01-25 | 1.58 | 53 | aquatics | 0 | 0 | 0 |
|  | Africa Zamorano Sanz | ESP | female | 1998-01-11 | 1.7 | 58 | aquatics | 0 | 0 | 0 |
|  | Aglaia Pezzato | ITA | female | 1994-04-22 | 1.75 | 60 | aquatics | 0 | 0 | 0 |
|  | Ahmad Amsyar Azman | MAS | male | 1992-08-28 | 1.62 | 62 | aquatics | 0 | 0 | 0 |
|  | Ahmed Akram | EGY | male | 1996-10-20 | 1.88 | 80 | aquatics | 0 | 0 | 0 |
|  | Ahmed Attellesey | LBA | male | 1995-07-30 |  |  | aquatics | 0 | 0 | 0 |
|  | Ahmed Gebrel | PLE | male | 1991-01-22 |  |  | aquatics | 0 | 0 | 0 |
|  | Ahmed Mathlouthi | TUN | male | 1989-12-18 | 1.9 | 90 | aquatics | 0 | 0 | 0 |
|  | Aidan Roach | AUS | male | 1990-09-07 | 1.87 | 88 | aquatics | 0 | 0 | 0 |
|  | Aika Hakoyama | JPN | female | 1991-07-27 | 1.76 | 62 | aquatics | 0 | 0 | 1 |
|  | Aiko Hayashi | JPN | female | 1993-11-17 | 1.66 | 56 | aquatics | 0 | 0 | 1 |

```js
Inputs.table(sportAthletes)
```

The select input works well for categorical data, such as sports or nationalities, but how about quantitative dimensions such as height or weight? Here’s a [range input](https://observablehq.com/framework/inputs/range) that lets you pick a target weight; we then filter the table rows for any athlete within 10% of the target weight. Notice that some columns, such as sport, are strongly correlated with weight.

weight (kg)

```js
const weight = view(
  Inputs.range(
    d3.extent(olympians, (d) => d.weight),
    {step: 1, label: "weight (kg)"}
  )
);
```

|  | name | nationality | sex | date\_of\_birth | height | ▴weight | sport | gold | silver | bronze |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Alexander Hartmann | AUS | male | 1993-03-07 | 1.98 | 91 | athletics | 0 | 0 | 0 |
|  | Alexander Hill | AUS | male | 1993-03-11 | 1.93 | 91 | rowing | 0 | 1 | 0 |
|  | Allan Julie | SEY | male | 1977-03-23 | 1.81 | 91 | sailing | 0 | 0 | 0 |
|  | Amer Hrustanovic | AUT | male | 1988-06-11 | 1.8 | 91 | wrestling | 0 | 0 | 0 |
|  | Badawy Mohamed Moneim | EGY | male | 1986-01-11 | 1.95 | 91 | volleyball | 0 | 0 | 0 |
|  | Bjorn Hornikel | GER | male | 1992-05-06 | 1.92 | 91 | aquatics | 0 | 0 | 0 |
|  | Christopher Guccione | AUS | male | 1985-07-30 | 2 | 91 | tennis | 0 | 0 | 0 |
|  | Danniel Thomas | JAM | female | 1992-11-11 | 1.68 | 91 | athletics | 0 | 0 | 0 |
|  | Dariusz Radosz | POL | male | 1986-08-13 | 1.99 | 91 | rowing | 0 | 0 | 0 |
|  | Dionysios Angelopoulos | GRE | male | 1992-08-05 | 1.89 | 91 | rowing | 0 | 0 | 0 |
|  | Dongmin Cha | KOR | male | 1986-08-24 | 1.9 | 91 | taekwondo | 0 | 0 | 1 |
|  | Dongyong Kim | KOR | male | 1990-12-12 | 1.89 | 91 | rowing | 0 | 0 | 0 |
|  | Edigerson Gomes | DEN | male | 1988-11-17 | 1.92 | 91 | football | 0 | 0 | 0 |
|  | Evgenii Lukantsov | RUS | male | 1991-12-05 | 1.87 | 91 | canoe | 0 | 0 | 0 |
|  | Fernando Garcia | ARG | male | 1981-08-31 | 1.9 | 91 | handball | 0 | 0 | 0 |
|  | Fidel Antonio Vargas | CUB | male | 1992-07-28 | 1.86 | 91 | canoe | 0 | 0 | 0 |
|  | Gavin Kyle Green | MAS | male | 1993-12-28 | 1.87 | 91 | golf | 0 | 0 | 0 |
|  | Georgios Tziallas | GRE | male | 1987-07-14 | 1.89 | 91 | rowing | 0 | 0 | 0 |
|  | Ieuan Lloyd | GBR | male | 1993-07-09 | 1.94 | 91 | aquatics | 0 | 0 | 0 |
|  | Igor Karacic | CRO | male | 1988-11-02 | 1.91 | 91 | handball | 0 | 0 | 0 |
|  | Jan-Lennard Struff | GER | male | 1990-04-25 | 1.96 | 91 | tennis | 0 | 0 | 0 |
|  | Javid Hamzatau | BLR | male | 1989-12-27 | 1.76 | 91 | wrestling | 0 | 0 | 1 |
|  | Jiri Sykora | CZE | male | 1995-01-20 | 1.9 | 91 | athletics | 0 | 0 | 0 |

```js
Inputs.table(
  olympians.filter((d) => d.weight < weight * 1.1 && weight * 0.9 < d.weight),
  {sort: "weight"}
)
```

For more, see the individual input pages:

- [Button](https://observablehq.com/framework/inputs/button) \- do something when a button is clicked
- [Toggle](https://observablehq.com/framework/inputs/toggle) \- toggle between two values (on or off)
- [Checkbox](https://observablehq.com/framework/inputs/checkbox) \- choose any from a set
- [Radio](https://observablehq.com/framework/inputs/radio) \- choose one from a set
- [Range](https://observablehq.com/framework/inputs/range) or [Number](https://observablehq.com/framework/inputs/range) \- choose a number in a range (slider)
- [Select](https://observablehq.com/framework/inputs/select) \- choose one or any from a set (drop-down menu)
- [Text](https://observablehq.com/framework/inputs/text) \- enter freeform single-line text
- [Textarea](https://observablehq.com/framework/inputs/textarea) \- enter freeform multi-line text
- [Date](https://observablehq.com/framework/inputs/date) or [Datetime](https://observablehq.com/framework/inputs/date) \- choose a date
- [Color](https://observablehq.com/framework/inputs/color) \- choose a color
- [File](https://observablehq.com/framework/inputs/file) \- choose a local file
- [Search](https://observablehq.com/framework/inputs/search) \- query a tabular dataset
- [Table](https://observablehq.com/framework/inputs/table) \- browse a tabular dataset

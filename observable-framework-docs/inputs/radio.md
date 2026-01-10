---
url: "https://observablehq.com/framework/inputs/radio"
title: "Radio input | Observable Framework"
---

1. [Options](https://observablehq.com/framework/inputs/radio#options)

# [Radio input](https://observablehq.com/framework/inputs/radio\#radio-input)

[API](https://github.com/observablehq/inputs/blob/main/README.md#radio) · [Source](https://github.com/observablehq/inputs/blob/main/src/checkbox.js) · The radio input allows the user to choose one of a given set of values. (See the [checkbox](https://observablehq.com/framework/inputs/checkbox) input for multiple-choice.) A radio is recommended over a [select](https://observablehq.com/framework/inputs/select) input when the number of values to choose from is small — say, seven or fewer — because all choices will be visible up-front, improving usability.

color

redgreenblue

```js
const color = view(Inputs.radio(["red", "green", "blue"], {label: "color"}));
```

null

```js
color
```

Note that a radio cannot be cleared by the user once selected; if you wish to allow no selection, include null in the allowed values.

YeaNayAbstain

```js
const vote = view(Inputs.radio(["Yea", "Nay", null], {value: null, format: (x) => x ?? "Abstain"}));
```

null

```js
vote
```

A radio’s values need not be strings: they can be anything. Specify a _format_ function to control how these values are presented to the reader.

```js
const teams = [\
  {name: "Lakers", location: "Los Angeles, California"},\
  {name: "Warriors", location: "San Francisco, California"},\
  {name: "Celtics", location: "Boston, Massachusetts"},\
  {name: "Nets", location: "New York City, New York"},\
  {name: "Raptors", location: "Toronto, Ontario"},\
];
```

Favorite team

LakersWarriorsCelticsNetsRaptors

```js
const favorite = view(Inputs.radio(teams, {label: "Favorite team", format: x => x.name}));
```

null

```js
favorite
```

A radio can be disabled by setting the _disabled_ option to true. Alternatively, specific options can be disabled by passing an array of values to disable.

Vowel

AEIOUY

```js
const vowel = view(Inputs.radio([..."AEIOUY"], {label: "Vowel", disabled: ["Y"]}));
```

null

```js
vowel
```

The _format_ function, like the _label_, can return either a text string or an HTML element. This allows extensive control over the appearance of the radio, if desired.

**Colors**

redgreenblue

```js
const color2 = view(
  Inputs.radio(["red", "green", "blue"], {
    value: "red",
    label: html`<b>Colors</b>`,
    format: (x) =>
      html`<span style="
          text-transform: capitalize;
          border-bottom: solid 2px ${x};
          margin-bottom: -2px;
        ">${x}</span>`
  })
);
```

"red"

```js
color2
```

If the radio’s data are specified as a [Map](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map), the values will be the map’s values while the keys will be the displayed options. (This behavior can be customized by passing _keyof_ and _valueof_ function options.) Below, the displayed sizes are named, but the value is the corresponding number of fluid ounces.

Size

ShortTallGrandeVenti

```js
const size = view(
  Inputs.radio(
    new Map([\
      ["Short", 8],\
      ["Tall", 12],\
      ["Grande", 16],\
      ["Venti", 20]\
    ]),
    {value: 12, label: "Size"}
  )
);
```

12

```js
size
```

Since the _format_ function is passed elements from the data, it can access both the key and value from the corresponding Map entry.

Size

Short (8 oz)Tall (12 oz)Grande (16 oz)Venti (20 oz)

```js
const size2 = view(
  Inputs.radio(
    new Map([\
      ["Short", 8],\
      ["Tall", 12],\
      ["Grande", 16],\
      ["Venti", 20]\
    ]),
    {value: 12, label: "Size", format: ([name, value]) => `${name} (${value} oz)`}
  )
);
```

12

```js
size2
```

Passing a Map to radio is especially useful in conjunction with [d3.group](https://d3js.org/d3-array/group). For example, given a tabular dataset of Olympic athletes (`olympians`), we can use d3.group to group them by gold medal count, and then a radio input to select the athletes for the chosen count.

Gold medal count

543210

```js
const goldAthletes = view(
  Inputs.radio(
    d3.group(olympians, (d) => d.gold),
    {label: "Gold medal count", sort: "descending"}
  )
);
```

null

```js
goldAthletes
```

If the _sort_ and _unique_ options are specified, the radio’s keys will be sorted and duplicate keys will be discarded, respectively.

ACGT

```js
const base = view(Inputs.radio("GATTACA", {sort: true, unique: true}));
```

null

```js
base
```

## [Options](https://observablehq.com/framework/inputs/radio\#options)

**Inputs.radio( _data_, _options_)**

The available radio input options are:

- _label_ \- a label; either a string or an HTML element
- _sort_ \- true, _ascending_, _descending_, or a comparator to sort keys; defaults to false
- _unique_ \- true to only show unique keys; defaults to false
- _locale_ \- the current locale; defaults to English
- _format_ \- a format function; defaults to [formatLocaleAuto](https://github.com/observablehq/inputs/blob/main/README.md#inputsformatlocaleautolocale) composed with _keyof_
- _keyof_ \- a function to return the key for the given element in _data_
- _valueof_ \- a function to return the value of the given element in _data_
- _value_ \- the initial value; defaults to null (no selection)
- _disabled_ \- whether input is disabled, or the disabled values; defaults to false

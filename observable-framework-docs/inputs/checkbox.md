---
url: "https://observablehq.com/framework/inputs/checkbox"
title: "Checkbox input | Observable Framework"
---

1. [Options](https://observablehq.com/framework/inputs/checkbox#options)

# [Checkbox input](https://observablehq.com/framework/inputs/checkbox\#checkbox-input)

[API](https://github.com/observablehq/inputs/blob/main/README.md#checkbox) · [Source](https://github.com/observablehq/inputs/blob/main/src/checkbox.js) · The checkbox input allows the user to choose any of a given set of values. (See the [radio](https://observablehq.com/framework/inputs/radio) input for single-choice.) A checkbox is recommended over a [select](https://observablehq.com/framework/inputs/select) input when the number of values to choose from is small — say, seven or fewer — because all choices will be visible up-front, improving usability. For zero or one choice, see the [toggle](https://observablehq.com/framework/inputs/toggle) input.

The initial value of a checkbox defaults to an empty array. You can override this by specifying the _value_ option, which should also be an array (or iterable).

color

redgreenblue

```js
const colors = view(Inputs.checkbox(["red", "green", "blue"], {label: "color"}));
```

Array(0) \[\]

```js
colors
```

A checkbox’s values need not be strings: they can be anything. Specify a _format_ function to control how these values are presented to the reader.

```js
const teams = [\
  {name: "Lakers", location: "Los Angeles, California"},\
  {name: "Warriors", location: "San Francisco, California"},\
  {name: "Celtics", location: "Boston, Massachusetts"},\
  {name: "Nets", location: "New York City, New York"},\
  {name: "Raptors", location: "Toronto, Ontario"},\
];
```

Watching

LakersWarriorsCelticsNetsRaptors

```js
const watching = view(Inputs.checkbox(teams, {label: "Watching", format: (x) => x.name}));
```

Array(0) \[\]

```js
watching
```

A checkbox can be disabled by setting the _disabled_ option to true. Alternatively, specific options can be disabled by passing an array of values to disable.

Vowel

AEIOUY

```js
const vowels = view(Inputs.checkbox([..."AEIOUY"], {label: "Vowel", disabled: ["Y"]}));
```

Array(0) \[\]

```js
vowels
```

The _format_ function, like the _label_, can return either a text string or an HTML element. This allows extensive control over the appearance of the checkbox, if desired.

**Colors**

redgreenblue

```js
const colors2 = view(
  Inputs.checkbox(["red", "green", "blue"], {
    value: ["red"],
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

Array(1) \["red"\]

```js
colors2
```

If the checkbox’s data are specified as a [Map](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map), the values will be the map’s values while the keys will be the displayed options. (This behavior can be customized by passing _keyof_ and _valueof_ function options.) Below, the displayed sizes are named, but the value is the corresponding number of fluid ounces.

Size

ShortTallGrandeVenti

```js
const sizes = view(
  Inputs.checkbox(
    new Map([\
      ["Short", 8],\
      ["Tall", 12],\
      ["Grande", 16],\
      ["Venti", 20]\
    ]),
    {value: [12], label: "Size"}
  )
);
```

Array(1) \[12\]

```js
sizes
```

Since the _format_ function is passed elements from the data, it can access both the key and value from the corresponding Map entry.

Size

Short (8 oz)Tall (12 oz)Grande (16 oz)Venti (20 oz)

```js
const size2 = view(
  Inputs.checkbox(
    new Map([\
      ["Short", 8],\
      ["Tall", 12],\
      ["Grande", 16],\
      ["Venti", 20]\
    ]),
    {value: [12], label: "Size", format: ([name, value]) => `${name} (${value} oz)`}
  )
);
```

Array(1) \[12\]

```js
size2
```

Passing a Map to checkbox is especially useful in conjunction with [d3.group](https://d3js.org/d3-array/group). For example, given a the sample `olympians` dataset of Olympic athletes, we can use d3.group to group them by gold medal count, and then checkbox to select the athletes for the chosen count. Note that the value of the checkbox will be an array of arrays, since d3.group returns a Map from key to array; use [_array_.flat](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/flat) to merge these arrays if desired.

Gold medal count

543210

```js
const goldAthletes = view(
  Inputs.checkbox(
    d3.group(olympians, (d) => d.gold),
    {label: "Gold medal count", sort: "descending", key: [4, 5]}
  )
);
```

Array(3) \[Object, Object, Object\]

```js
goldAthletes.flat()
```

If the _sort_ and _unique_ options are specified, the checkbox’s keys will be sorted and duplicate keys will be discarded, respectively.

ACGT

```js
const bases = view(Inputs.checkbox("GATTACA", {sort: true, unique: true}));
```

Array(0) \[\]

```js
bases
```

## [Options](https://observablehq.com/framework/inputs/checkbox\#options)

**Inputs.checkbox( _data_, _options_)**

The available checkbox input options are:

- _label_ \- a label; either a string or an HTML element
- _sort_ \- true, _ascending_, _descending_, or a comparator to sort keys; defaults to false
- _unique_ \- true to only show unique keys; defaults to false
- _locale_ \- the current locale; defaults to English
- _format_ \- a format function; defaults to [formatLocaleAuto](https://github.com/observablehq/inputs/blob/main/README.md#inputsformatlocaleautolocale) composed with _keyof_
- _keyof_ \- a function to return the key for the given element in _data_
- _valueof_ \- a function to return the value of the given element in _data_
- _value_ \- the initial value, an array; defaults to an empty array (no selection)
- _disabled_ \- whether input is disabled, or the disabled values; defaults to false

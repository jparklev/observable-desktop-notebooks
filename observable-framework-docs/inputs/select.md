---
url: "https://observablehq.com/framework/inputs/select"
title: "Select input | Observable Framework"
---

1. [Options](https://observablehq.com/framework/inputs/select#options)

# [Select input](https://observablehq.com/framework/inputs/select\#select-input)

[API](https://github.com/observablehq/inputs/blob/main/README.md#select) · [Source](https://github.com/observablehq/inputs/blob/main/src/select.js) · The select input allows the user to choose from a given set of values. A select is recommended over a [radio](https://observablehq.com/framework/inputs/radio) or [checkbox](https://observablehq.com/framework/inputs/checkbox) input when the number of values to choose from is large — say, eight or more — to save space.

The default appearance of a select is a drop-down menu that allows you to choose a single value. The initial value is the first of the allowed values, but you can override this by specifying the _value_ option.

Favorite coloraliceblueantiquewhiteaquaaquamarineazurebeigebisqueblackblanchedalmondbluebluevioletbrownburlywoodcadetbluechartreusechocolatecoralcornflowerbluecornsilkcrimsoncyandarkbluedarkcyandarkgoldenroddarkgraydarkgreendarkgreydarkkhakidarkmagentadarkolivegreendarkorangedarkorchiddarkreddarksalmondarkseagreendarkslatebluedarkslategraydarkslategreydarkturquoisedarkvioletdeeppinkdeepskybluedimgraydimgreydodgerbluefirebrickfloralwhiteforestgreenfuchsiagainsboroghostwhitegoldgoldenrodgraygreengreenyellowgreyhoneydewhotpinkindianredindigoivorykhakilavenderlavenderblushlawngreenlemonchiffonlightbluelightcorallightcyanlightgoldenrodyellowlightgraylightgreenlightgreylightpinklightsalmonlightseagreenlightskybluelightslategraylightslategreylightsteelbluelightyellowlimelimegreenlinenmagentamaroonmediumaquamarinemediumbluemediumorchidmediumpurplemediumseagreenmediumslatebluemediumspringgreenmediumturquoisemediumvioletredmidnightbluemintcreammistyrosemoccasinnavajowhitenavyoldlaceoliveolivedraborangeorangeredorchidpalegoldenrodpalegreenpaleturquoisepalevioletredpapayawhippeachpuffperupinkplumpowderbluepurplerebeccapurpleredrosybrownroyalbluesaddlebrownsalmonsandybrownseagreenseashellsiennasilverskyblueslateblueslategrayslategreysnowspringgreensteelbluetantealthistletomatoturquoisevioletwheatwhitewhitesmokeyellowyellowgreen

```js
const color = view(Inputs.select(x11colors, {value: "steelblue", label: "Favorite color"}));
```

"steelblue"

```js
color
```

If the _multiple_ option is true, the select will allow multiple values to be selected and the value of the select will be the array of selected values. The initial value is the empty array. You can choose a range of values by dragging or Shift-clicking, and select or deselect a value by Command-clicking.

Favorite colorsaliceblueantiquewhiteaquaaquamarineazurebeigebisqueblackblanchedalmondbluebluevioletbrownburlywoodcadetbluechartreusechocolatecoralcornflowerbluecornsilkcrimsoncyandarkbluedarkcyandarkgoldenroddarkgraydarkgreendarkgreydarkkhakidarkmagentadarkolivegreendarkorangedarkorchiddarkreddarksalmondarkseagreendarkslatebluedarkslategraydarkslategreydarkturquoisedarkvioletdeeppinkdeepskybluedimgraydimgreydodgerbluefirebrickfloralwhiteforestgreenfuchsiagainsboroghostwhitegoldgoldenrodgraygreengreenyellowgreyhoneydewhotpinkindianredindigoivorykhakilavenderlavenderblushlawngreenlemonchiffonlightbluelightcorallightcyanlightgoldenrodyellowlightgraylightgreenlightgreylightpinklightsalmonlightseagreenlightskybluelightslategraylightslategreylightsteelbluelightyellowlimelimegreenlinenmagentamaroonmediumaquamarinemediumbluemediumorchidmediumpurplemediumseagreenmediumslatebluemediumspringgreenmediumturquoisemediumvioletredmidnightbluemintcreammistyrosemoccasinnavajowhitenavyoldlaceoliveolivedraborangeorangeredorchidpalegoldenrodpalegreenpaleturquoisepalevioletredpapayawhippeachpuffperupinkplumpowderbluepurplerebeccapurpleredrosybrownroyalbluesaddlebrownsalmonsandybrownseagreenseashellsiennasilverskyblueslateblueslategrayslategreysnowspringgreensteelbluetantealthistletomatoturquoisevioletwheatwhitewhitesmokeyellowyellowgreen

```js
const colors = view(Inputs.select(x11colors, {multiple: true, label: "Favorite colors"}));
```

Array(0) \[\]

```js
colors
```

The _multiple_ option can also be a number indicating the desired size: the number of rows to show. If _multiple_ is true, the size defaults to the number of allowed values, or ten, whichever is fewer.

Favorite colorsaliceblueantiquewhiteaquaaquamarineazurebeigebisqueblackblanchedalmondbluebluevioletbrownburlywoodcadetbluechartreusechocolatecoralcornflowerbluecornsilkcrimsoncyandarkbluedarkcyandarkgoldenroddarkgraydarkgreendarkgreydarkkhakidarkmagentadarkolivegreendarkorangedarkorchiddarkreddarksalmondarkseagreendarkslatebluedarkslategraydarkslategreydarkturquoisedarkvioletdeeppinkdeepskybluedimgraydimgreydodgerbluefirebrickfloralwhiteforestgreenfuchsiagainsboroghostwhitegoldgoldenrodgraygreengreenyellowgreyhoneydewhotpinkindianredindigoivorykhakilavenderlavenderblushlawngreenlemonchiffonlightbluelightcorallightcyanlightgoldenrodyellowlightgraylightgreenlightgreylightpinklightsalmonlightseagreenlightskybluelightslategraylightslategreylightsteelbluelightyellowlimelimegreenlinenmagentamaroonmediumaquamarinemediumbluemediumorchidmediumpurplemediumseagreenmediumslatebluemediumspringgreenmediumturquoisemediumvioletredmidnightbluemintcreammistyrosemoccasinnavajowhitenavyoldlaceoliveolivedraborangeorangeredorchidpalegoldenrodpalegreenpaleturquoisepalevioletredpapayawhippeachpuffperupinkplumpowderbluepurplerebeccapurpleredrosybrownroyalbluesaddlebrownsalmonsandybrownseagreenseashellsiennasilverskyblueslateblueslategrayslategreysnowspringgreensteelbluetantealthistletomatoturquoisevioletwheatwhitewhitesmokeyellowyellowgreen

```js
const fewerColors = view(Inputs.select(x11colors, {multiple: 4, label: "Favorite colors"}));
```

Array(0) \[\]

```js
fewerColors
```

For single-choice selects, if you wish to allow no choice to be selected, we recommend including null as an explicit option.

Favorite coloraliceblueantiquewhiteaquaaquamarineazurebeigebisqueblackblanchedalmondbluebluevioletbrownburlywoodcadetbluechartreusechocolatecoralcornflowerbluecornsilkcrimsoncyandarkbluedarkcyandarkgoldenroddarkgraydarkgreendarkgreydarkkhakidarkmagentadarkolivegreendarkorangedarkorchiddarkreddarksalmondarkseagreendarkslatebluedarkslategraydarkslategreydarkturquoisedarkvioletdeeppinkdeepskybluedimgraydimgreydodgerbluefirebrickfloralwhiteforestgreenfuchsiagainsboroghostwhitegoldgoldenrodgraygreengreenyellowgreyhoneydewhotpinkindianredindigoivorykhakilavenderlavenderblushlawngreenlemonchiffonlightbluelightcorallightcyanlightgoldenrodyellowlightgraylightgreenlightgreylightpinklightsalmonlightseagreenlightskybluelightslategraylightslategreylightsteelbluelightyellowlimelimegreenlinenmagentamaroonmediumaquamarinemediumbluemediumorchidmediumpurplemediumseagreenmediumslatebluemediumspringgreenmediumturquoisemediumvioletredmidnightbluemintcreammistyrosemoccasinnavajowhitenavyoldlaceoliveolivedraborangeorangeredorchidpalegoldenrodpalegreenpaleturquoisepalevioletredpapayawhippeachpuffperupinkplumpowderbluepurplerebeccapurpleredrosybrownroyalbluesaddlebrownsalmonsandybrownseagreenseashellsiennasilverskyblueslateblueslategrayslategreysnowspringgreensteelbluetantealthistletomatoturquoisevioletwheatwhitewhitesmokeyellowyellowgreen

```js
const maybeColor = view(Inputs.select([null].concat(x11colors), {label: "Favorite color"}));
```

null

```js
maybeColor
```

A select’s values need not be strings: they can be anything. Specify a _format_ function to control how these values are presented to the reader.

```js
const teams = [\
  {name: "Lakers", location: "Los Angeles, California"},\
  {name: "Warriors", location: "San Francisco, California"},\
  {name: "Celtics", location: "Boston, Massachusetts"},\
  {name: "Nets", location: "New York City, New York"},\
  {name: "Raptors", location: "Toronto, Ontario"},\
];
```

Favorite teamLakersWarriorsCelticsNetsRaptors

```js
const favorite = view(
  Inputs.select(teams, {
    label: "Favorite team",
    format: (t) => t.name,
    value: teams.find((t) => t.name === "Warriors")
  })
);
```

Object {name: "Warriors", location: "San Francisco, California"}

```js
favorite
```

If the select’s data are specified as a Map, the values will be the map’s values while the keys will be the displayed options. (This behavior can be customized by passing _keyof_ and _valueof_ function options.) Below, the displayed sizes are named, but the value is the corresponding number of fluid ounces.

SizeShortTallGrandeVenti

```js
const size = view(
  Inputs.select(
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

SizeShort (8 oz)Tall (12 oz)Grande (16 oz)Venti (20 oz)

```js
const size2 = view(
  Inputs.select(
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

Passing a Map to select is especially useful in conjunction with [d3.group](https://d3js.org/d3-array/group). For example, given a tabular dataset of Olympic athletes (`olympians`), we can use d3.group to group them by sport, and then the select input to select only athletes for the chosen sport.

Sportathleticsfencingtaekwondocyclingtriathlonvolleyballaquaticsrugby sevenswrestlingfootballshootingboxingequestrianrowingjudohandballbadmintonhockeymodern pentathlontable tenniscanoebasketballgolfarcheryweightliftingsailingtennisgymnastics

```js
const sportAthletes = view(
  Inputs.select(
    d3.group(olympians, (d) => d.sport),
    {label: "Sport"}
  )
);
```

Array(2363) \[Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, …\]

```js
sportAthletes
```

If the _sort_ and _unique_ options are specified, the select’s keys will be sorted and duplicate keys will be discarded, respectively.

Sportaquaticsarcheryathleticsbadmintonbasketballboxingcanoecyclingequestrianfencingfootballgolfgymnasticshandballhockeyjudomodern pentathlonrowingrugby sevenssailingshootingtable tennistaekwondotennistriathlonvolleyballweightliftingwrestling

```js
const sport = view(
  Inputs.select(
    olympians.map((d) => d.sport),
    {label: "Sport", sort: true, unique: true}
  )
);
```

"aquatics"

```js
sport
```

The _disabled_ option, if true, disables the entire select. If _disabled_ is an array, then only the specified values are disabled.

VowelAEIOUY

```js
Inputs.select(["A", "E", "I", "O", "U", "Y"], {label: "Vowel", disabled: true})
```

VowelAEIOUY

```js
Inputs.select(["A", "E", "I", "O", "U", "Y"], {label: "Vowel", disabled: ["Y"]})
```

## [Options](https://observablehq.com/framework/inputs/select\#options)

**Inputs.select( _data_, _options_)**

The available select input options are:

- _label_ \- a label; either a string or an HTML element
- _multiple_ \- whether to allow multiple choice; defaults to false
- _size_ \- if _multiple_ is true, the number of options to show
- _sort_ \- true, _ascending_, _descending_, or a comparator to sort keys; defaults to false
- _unique_ \- true to only show unique keys; defaults to false
- _locale_ \- the current locale; defaults to English
- _format_ \- a format function; defaults to [formatLocaleAuto](https://github.com/observablehq/inputs/blob/main/README.md#inputsformatlocaleautolocale) composed with _keyof_
- _keyof_ \- a function to return the key for the given element in _data_
- _valueof_ \- a function to return the value of the given element in _data_
- _value_ \- the initial value, an array if multiple choice is allowed
- _width_ \- the width of the input (not including the label)
- _disabled_ \- whether input is disabled, or the disabled values; defaults to false

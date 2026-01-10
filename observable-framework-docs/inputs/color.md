---
url: "https://observablehq.com/framework/inputs/color"
title: "Color input | Observable Framework"
---

1. [Options](https://observablehq.com/framework/inputs/color#options)

# [Color input](https://observablehq.com/framework/inputs/color\#color-input)

[API](https://github.com/observablehq/inputs/blob/main/README.md#inputscoloroptions) · [Source](https://github.com/observablehq/inputs/blob/main/src/color.js) · The color input specifies an RGB color as a hexadecimal string `#rrggbb`. The initial value defaults to black (`#000000`) and can be specified with the _value_ option.

Favorite color

#4682b4

```js
const color = view(Inputs.color({label: "Favorite color", value: "#4682b4"}));
```

"#4682b4"

```js
color
```

The color input is currently strict in regards to input: it does not accept any CSS color string. If you’d like greater flexibility, consider using D3 to parse colors and format them as hexadecimal.

Fill

#4682b4

```js
const fill = view(Inputs.color({label: "Fill", value: d3.color("steelblue").formatHex()}));
```

If you specify the _datalist_ option as an array of hexadecimal color strings, the color picker will show this set of colors for convenient picking. (The user will still be allowed to pick another color, however; if you want to limit the choice to a specific set, then a radio or select input may be more appropriate.)

Stroke

#000000

```js
const stroke = view(Inputs.color({label: "Stroke", datalist: d3.schemeTableau10}));
```

"#000000"

```js
stroke
```

The _readonly_ property is not supported for color inputs, but you can use the _disabled_ option to prevent the input value from being changed.

Disabled

#f28e2c

```js
const disabled = view(Inputs.color({label: "Disabled", value: "#f28e2c", disabled: true}));
```

"#f28e2c"

```js
disabled
```

## [Options](https://observablehq.com/framework/inputs/color\#options)

**Inputs.color( _options_)**

Like [Inputs.text](https://observablehq.com/framework/inputs/text), but where _type_ is color. The color value is represented as an RGB hexadecimal string such as #ff00ff. This type of input does not support the following options: _placeholder_, _pattern_, _spellcheck_, _autocomplete_, _autocapitalize_, _min_, _max_, _minlength_, _maxlength_.

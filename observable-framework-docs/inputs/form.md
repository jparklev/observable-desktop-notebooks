---
url: "https://observablehq.com/framework/inputs/form"
title: "Form input | Observable Framework"
---

1. [Options](https://observablehq.com/framework/inputs/form#options)

# [Form input](https://observablehq.com/framework/inputs/form\#form-input)

[API](https://github.com/observablehq/inputs/blob/main/README.md#inputsforminputs-options) · [Source](https://github.com/observablehq/inputs/blob/main/src/form.js) · The form input combines a number of inputs into a single compound input. It’s intended for a more compact display of closely-related inputs, say for a color’s red, green, and blue channels.

r

g

b

```js
const rgb = view(Inputs.form([\
  Inputs.range([0, 255], {step: 1, label: "r"}),\
  Inputs.range([0, 255], {step: 1, label: "g"}),\
  Inputs.range([0, 255], {step: 1, label: "b"})\
]));
```

Array(3) \[128, 128, 128\]

```js
rgb
```

You can pass either an array of inputs to Inputs.form, as shown above, or a simple object with enumerable properties whose values are inputs. In the latter case, the value of the form input is an object with the same structure whose values are the respective input’s value.

r

g

b

```js
const rgb2 = view(Inputs.form({
  r: Inputs.range([0, 255], {step: 1, label: "r"}),
  g: Inputs.range([0, 255], {step: 1, label: "g"}),
  b: Inputs.range([0, 255], {step: 1, label: "b"})
}));
```

Object {r: 128, g: 128, b: 128}

```js
rgb2
```

## [Options](https://observablehq.com/framework/inputs/form\#options)

**Inputs.form( _inputs_, _options_)**

The available form input options are:

- _template_ \- a function that takes the given _inputs_ and returns an HTML element

If the _template_ object is not specified, the given inputs are wrapped in a DIV.

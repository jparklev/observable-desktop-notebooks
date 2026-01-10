---
url: "https://observablehq.com/framework/inputs/toggle"
title: "Toggle input | Observable Framework"
---

1. [Options](https://observablehq.com/framework/inputs/toggle#options)

# [Toggle input](https://observablehq.com/framework/inputs/toggle\#toggle-input)

[API](https://github.com/observablehq/inputs/blob/main/README.md#toggle) · [Source](https://github.com/observablehq/inputs/blob/main/src/checkbox.js) · The toggle input allows the user to choose one of two values, representing on or off. It is a specialized form of the [checkbox input](https://observablehq.com/framework/inputs/checkbox).

The initial value of a toggle defaults to false. You can override this by specifying the _value_ option.

Mute

```js
const  mute = view(Inputs.toggle({label: "Mute", value: true}));
```

true

```js
mute
```

The on and off values of a toggle can be changed with the _values_ option which defaults to \[true, false\].

Binary

```js
const binary = view(Inputs.toggle({label: "Binary", values: [1, 0]}));
```

0

```js
binary
```

The _label_ can be either a text string or an HTML element. This allows more control over the label’s appearance, if desired.

**Fancy**

```js
const fancy = view(Inputs.toggle({label: html`<b>Fancy</b>`}));
```

false

```js
fancy
```

A toggle can be disabled to prevent its value from being changed.

Frozen

```js
const frozen = view(Inputs.toggle({label: "Frozen", value: true, disabled: true}));
```

true

```js
frozen
```

## [Options](https://observablehq.com/framework/inputs/toggle\#options)

**Inputs.toggle( _options_)**

The available toggle input options are:

- _label_ \- a label; either a string or an HTML element
- _values_ \- the two values to toggle between; defaults to \[true, false\]
- _value_ \- the initial value; defaults to the second value (false)
- _disabled_ \- whether input is disabled; defaults to false

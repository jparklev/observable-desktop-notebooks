---
url: "https://observablehq.com/framework/inputs/range"
title: "Range input | Observable Framework"
---

1. [Options](https://observablehq.com/framework/inputs/range#options)

# [Range input](https://observablehq.com/framework/inputs/range\#range-input)

[API](https://github.com/observablehq/inputs/blob/main/README.md#range) · [Source](https://github.com/observablehq/inputs/blob/main/src/range.js) · The range input specifies a number between the given _min_ and _max_ (inclusive). This number can be adjusted roughly by sliding, or precisely by typing. A range input is also known as a slider.

By default, a range chooses a floating point number between 0 and 1 with full precision, which is often more precision than desired.

```js
const x = view(Inputs.range());
```

0.5

```js
x
```

The _step_ option is strongly encouraged to set the desired precision (the interval between adjacent values). For integers, use _step_ = 1\. The up and down buttons in the number input will only work if a _step_ is specified. To change the extent, pass \[ _min_, _max_\] as the first argument.

```js
const y = view(Inputs.range([0, 255], {step: 1}));
```

The _min_, _max_ and _step_ options affect only the slider behavior, the number input’s buttons, and whether the browser shows a warning if a typed number is invalid; they do not constrain the typed number.

The _value_ option sets the initial value, which defaults to the middle of the range: ( _min_ \+ _max_) / 2.

```js
const z = view(Inputs.range([0, 255], {step: 1, value: 0}));
```

0

```js
z
```

To describe the meaning of the input, supply a _label_. A _placeholder_ string may also be specified; it will only be visible when the number input is empty.

Gain

```js
const gain = view(Inputs.range([0, 11], {label: "Gain", step: 0.1, placeholder: "0–11"}));
```

5.5

```js
gain
```

For more control over typography, the _label_ may be an HTML element.

Top _n_

```js
const n = view(Inputs.range([1, 10], {label: html`Top <i>n</i>`, step: 1}));
```

You can even use a TE​X label, if you’re into that sort of thing.

ψ(r)

```js
const psir = view(Inputs.range([0, 1], {label: tex`\psi(\textbf{r})`}));
```

For an unbounded range, or simply to suppress the range input, you can use Inputs.number instead of Inputs.range. If you don’t specify an initial value, it defaults to undefined which causes referencing cells to wait for valid input.

Favorite integer

```js
const m = view(Inputs.number([0, Infinity], {step: 1, label: "Favorite integer", placeholder: ""}));
```

```js
m
```

If differences in the numeric range are not uniformly interesting — for instance, when looking at log-distributed values — pass a _transform_ function to produce a [nonlinear slider](https://mathisonian.github.io/idyll/nonlinear-sliders/). The built-in Math.log and Math.sqrt transform functions are recommended. If you supply a custom function, you should also provide an _invert_ function that implements the inverse transform. (Otherwise, the Range will use [Newton’s method](https://en.wikipedia.org/wiki/Newton's_method) which may be inaccurate.)

```js
Inputs.range([1, 100], {transform: Math.log})
```

```js
Inputs.range([0, 1], {transform: Math.sqrt})
```

The _format_ option allows you to specify a function that is called to format the displayed number. Note that the returned string must be a [valid floating-point number](https://html.spec.whatwg.org/multipage/common-microsyntaxes.html#valid-floating-point-number) according to the HTML specification; no commas allowed!

```js
const f = view(Inputs.range([0, 1], {format: x => x.toFixed(2)}));
```

0.5

```js
f
```

To prevent a range’s value from being changed, use the _disabled_ option.

```js
const d = view(Inputs.range([0, 1], {disabled: true}));
```

0.5

```js
d
```

## [Options](https://observablehq.com/framework/inputs/range\#options)

**Inputs.range( _extent_, _options_)**

The available range input options are:

- _label_ \- a label; either a string or an HTML element
- _step_ \- the step (precision); the interval between adjacent values
- _format_ \- a format function; defaults to [formatTrim](https://github.com/observablehq/inputs?tab=readme-ov-file#inputsformattrimnumber)
- _placeholder_ \- a placeholder string for when the input is empty
- _transform_ \- an optional non-linear transform
- _invert_ \- the inverse transform
- _validate_ \- a function to check whether the number input is valid
- _value_ \- the initial value; defaults to ( _min_ \+ _max_) / 2
- _width_ \- the width of the input (not including the label)
- _disabled_ \- whether input is disabled; defaults to false

The given _value_ is clamped to the given extent, and rounded if _step_ is defined. However, note that the _min_, _max_ and _step_ options affect only the slider behavior, the number input’s buttons, and whether the browser shows a warning if a typed number is invalid; they do not constrain the typed number.

If _validate_ is not defined, [_number_.checkValidity](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#dom-cva-checkvalidity) is used. While the input is not considered valid, changes to the input will not be reported.

The _format_ function should return a string value that is compatible with native number parsing. Hence, the default [formatTrim](https://github.com/observablehq/inputs?tab=readme-ov-file#inputsformattrimnumber) is recommended.

If a _transform_ function is specified, an inverse transform function _invert_ is strongly recommended. If _invert_ is not provided, the Range will fallback to Newton’s method, but this may be slow or inaccurate. Passing Math.sqrt, Math.log, or Math.exp as a _transform_ will automatically supply the corresponding _invert_. If _min_ is greater than _max_, _i.e._ if the extent is inverted, then _transform_ and _invert_ will default to `(value) => -value`.

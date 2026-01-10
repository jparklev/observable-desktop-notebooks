---
url: "https://observablehq.com/framework/inputs/textarea"
title: "Text area input | Observable Framework"
---

1. [Options](https://observablehq.com/framework/inputs/textarea#options)

# [Text area input](https://observablehq.com/framework/inputs/textarea\#text-area-input)

[API](https://github.com/observablehq/inputs/blob/main/README.md#textarea) · [Source](https://github.com/observablehq/inputs/blob/main/src/textarea.js) · The textarea input allows freeform multi-line text entry. For a single line, see the [text](https://observablehq.com/framework/inputs/text) input.

In its most basic form, a textarea is a blank box whose value is the empty string. The textarea’s value changes as the user types into the box.

```js
const text = view(Inputs.textarea());
```

""

```js
text
```

We recommend providing a _label_ and _placeholder_ to improve usability. You can also supply an initial _value_ if desired. The _label_ may be either a text string or an HTML element, if more control over styling is desired.

Biography

```js
const bio = view(Inputs.textarea({label: "Biography", placeholder: "What’s your story?"}));
```

""

```js
bio
```

If the input will trigger some expensive calculation, such as fetching from a remote server, the _submit_ option can be used to defer the textarea from reporting the new value until the user clicks the Submit button or hits Command-Enter. The value of _submit_ can also be the desired contents of the submit button (a string or HTML).

Essay

Submit

```js
const essay = view(Inputs.textarea({label: "Essay", rows: 6, minlength: 40, submit: true}));
```

```js
essay
```

The HTML5 _spellcheck_, _minlength_, and _maxlength_ options are supported. If the user enters invalid input, the browser may display a warning (e.g., “Use at least 80 characters”).

To prevent a textarea’s value from being changed, use the _disabled_ option.

Fixed value

```js
const fixed = view(Inputs.textarea({label: "Fixed value", value: "Can’t edit me!", disabled: true}));
```

"Can’t edit me!"

```js
fixed
```

## [Options](https://observablehq.com/framework/inputs/textarea\#options)

**Inputs.textarea( _options_)**

The available text area options are:

- _label_ \- a label; either a string or an HTML element
- _value_ \- the initial value; defaults to the empty string
- _placeholder_ \- the [placeholder](https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes/placeholder) attribute
- _spellcheck_ \- whether to activate the browser’s spell-checker
- _autocomplete_ \- the [autocomplete](https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes/autocomplete) attribute, as text or boolean
- _autocapitalize_ \- the [autocapitalize](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/autocapitalize) attribute, as text or boolean
- _minlength_ \- [minimum length](https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes/minlength) attribute
- _maxlength_ \- [maximum length](https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes/maxlength) attribute
- _required_ \- if true, the input must be non-empty; defaults to _minlength_ \> 0
- _validate_ \- a function to check whether the text input is valid
- _width_ \- the width of the input (not including the label)
- _rows_ \- the number of rows of text to show
- _resize_ \- if true, allow vertical resizing; defaults to _rows_ < 12
- _submit_ \- whether to require explicit submission; defaults to false
- _readonly_ \- whether input is readonly; defaults to false
- _disabled_ \- whether input is disabled; defaults to false
- _monospace_ \- if true, use a monospace font

If _validate_ is not defined, [_text_.checkValidity](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#dom-cva-checkvalidity) is used. While the input is not considered valid, changes to the input will not be reported.

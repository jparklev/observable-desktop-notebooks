---
url: "https://observablehq.com/framework/inputs/text"
title: "Text input | Observable Framework"
---

1. [Options](https://observablehq.com/framework/inputs/text#options)

# [Text input](https://observablehq.com/framework/inputs/text\#text-input)

[API](https://github.com/observablehq/inputs/blob/main/README.md#text) · [Source](https://github.com/observablehq/inputs/blob/main/src/text.js) · The text input allows freeform single-line text entry. For multiple lines, see the [text area](https://observablehq.com/framework/inputs/textarea) input.

In its most basic form, a text input is a blank box whose value is the empty string. The text’s value changes as the user types into the box.

```js
const text = view(Inputs.text());
```

""

```js
text
```

We recommend providing a _label_ and _placeholder_ to improve usability. You can also supply an initial _value_ if desired.

Name

```js
const name = view(
  Inputs.text({
    label: "Name",
    placeholder: "Enter your name",
    value: "Anonymous"
  })
);
```

"Anonymous"

```js
name
```

The _label_ may be either a text string or an HTML element, if more control over styling is desired.

**Fancy**

```js
const signature = view(
  Inputs.text({
    label: html`<b>Fancy</b>`,
    placeholder: "What’s your fancy?"
  })
);
```

For specific classes of text, such as email addresses and telephone numbers, you can supply one of the [HTML5 input types](https://developer.mozilla.org/en-US/docs/Learn/Forms/HTML5_input_types), such as email, tel (for a telephone number), or url, as the _type_ option. Or, use a convenience method: Inputs.email, Inputs.password, Inputs.tel, or Inputs.url.

Password

```js
const password = view(Inputs.password({label: "Password", value: "open sesame"}));
```

"open sesame"

```js
password
```

The HTML5 _pattern_, _spellcheck_, _minlength_, and _maxlength_ options are also supported. If the user enters invalid input, the browser may display a warning ( _e.g._, “Enter an email address”).

Email

```js
const email = view(
  Inputs.text({
    type: "email",
    label: "Email",
    placeholder: "Enter your email"
  })
);
```

If the input will trigger some expensive calculation, such as fetching from a remote server, the _submit_ option can be used to defer the text input from reporting the new value until the user clicks the Submit button or hits Enter. The value of _submit_ can also be the desired contents of the submit button (a string or HTML).

Query

Submit

```js
const query = view(Inputs.text({label: "Query", placeholder: "Search", submit: true}));
```

""

```js
query
```

To provide a recommended set of values, pass an array of strings as the _datalist_ option. For example, the input below is intended to accept the name of a U.S. state; you can either type the state name by hand or click one of the suggestions on focus.

```js
const capitals = FileAttachment("us-state-capitals.tsv").tsv({typed: true});
```

U.S. state

```js
const state = view(Inputs.text({
  label: "U.S. state",
  placeholder: "Enter state name",
  datalist: capitals.map((d) => d.State)
}));
```

""

```js
state
```

To prevent a text input’s value from being changed, use the _disabled_ option.

Fixed value

```js
const fixed = view(Inputs.text({label: "Fixed value", value: "Can’t edit me!", disabled: true}));
```

"Can’t edit me!"

```js
fixed
```

## [Options](https://observablehq.com/framework/inputs/text\#options)

**Inputs.text( _options_)**

The available text input options are:

- _label_ \- a label; either a string or an HTML element
- _type_ \- the [input type](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input#input_types), such as “password” or “email”; defaults to “text”
- _value_ \- the initial value; defaults to the empty string
- _placeholder_ \- the [placeholder](https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes/placeholder) attribute
- _spellcheck_ \- whether to activate the browser’s spell-checker
- _autocomplete_ \- the [autocomplete](https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes/autocomplete) attribute, as text or boolean
- _autocapitalize_ \- the [autocapitalize](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/autocapitalize) attribute, as text or boolean
- _pattern_ \- the [pattern](https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes/pattern) attribute
- _minlength_ \- [minimum length](https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes/minlength) attribute
- _maxlength_ \- [maximum length](https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes/maxlength) attribute
- _min_ \- [minimum value](https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes/min) attribute (`YYYY-MM-DD` for the date type)
- _max_ \- [maximum value](https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes/max) attribute
- _required_ \- if true, the input must be non-empty; defaults to _minlength_ \> 0
- _validate_ \- a function to check whether the text input is valid
- _width_ \- the width of the input (not including the label)
- _submit_ \- whether to require explicit submission; defaults to false
- _datalist_ \- an iterable of suggested values
- _readonly_ \- whether input is readonly; defaults to false
- _disabled_ \- whether input is disabled; defaults to false

If _validate_ is not defined, [_text_.checkValidity](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#dom-cva-checkvalidity) is used. While the input is not considered valid, changes to the input will not be reported.

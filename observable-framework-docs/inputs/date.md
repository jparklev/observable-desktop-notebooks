---
url: "https://observablehq.com/framework/inputs/date"
title: "Date input | Observable Framework"
---

1. [Options](https://observablehq.com/framework/inputs/date#options)

# [Date input](https://observablehq.com/framework/inputs/date\#date-input)

[API](https://github.com/observablehq/inputs/blob/main/README.md#date) · [Source](https://github.com/observablehq/inputs/blob/main/src/date.js) · The date input specifies a date.

```js
const date = view(Inputs.date());
```

null

```js
date
```

We recommend providing a _label_ to improve usability. You can also supply an initial _value_; this can be specified as a Date instance, a string of the form _YYYY-MM-DD_, or the corresponding number of milliseconds since UNIX epoch.

Start

```js
const start = view(Inputs.date({label: "Start", value: "2021-09-21"}));
```

2021-09-21

```js
start
```

The value of a date input is a [Date](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date) instance at UTC midnight, or null if an initial value is not specified. If the _required_ option is set to true, then the initial value of the date input will be undefined instead of null, causing referencing cells to wait until a valid input is entered.

Date

```js
const rdate = view(Inputs.date({label: "Date", required: true}));
```

```js
rdate
```

The datetime input is similar to the date input, except it allows a time to be specified in addition to a date. The time is specified in the user’s local time zone (for you, that’s America/New\_York). Like a date input, the value is exposed as a Date instance. Dates are formatted by the Observable inspector as UTC; note the `Z`.

Moment

```js
const datetime = view(Inputs.datetime({label: "Moment"}));
```

null

```js
datetime
```

The _min_ and _max_ option allow you to set a lower and upper bound for valid inputs. Like the _value_ option, these options may be specified either as a Date instance, as _YYYY-MM-DD_ strings, or epoch milliseconds.

Birthday

```js
const birthday = view(Inputs.date({label: "Birthday", min: "2021-01-01", max: "2021-12-31"}));
```

null

```js
birthday
```

If the input will trigger some expensive calculation, such as fetching from a remote server, the _submit_ option can be used to defer the input from reporting the new value until the user clicks the Submit button or hits Enter. The value of _submit_ can also be the desired contents of the submit button (a string or HTML).

Date

Submit

```js
const sdate = view(Inputs.date({label: "Date", submit: true}));
```

null

```js
sdate
```

To prevent the value from being changed, use the _disabled_ or _readonly_ option.

Fixed date

```js
const fixed = view(Inputs.date({label: "Fixed date", value: "2021-01-01", disabled: true}));
```

2021-01-01

```js
fixed
```

Readonly date

```js
const readonly = view(Inputs.date({label: "Readonly date", value: "2021-01-01", readonly: true}));
```

2021-01-01

```js
readonly
```

## [Options](https://observablehq.com/framework/inputs/date\#options)

**Inputs.date( _options_)**

The available date input options are:

- _label_ \- a label; either a string or an HTML element
- _value_ \- the initial value as a [Date](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date) or `YYYY-MM-DD` string; defaults to null
- _min_ \- [minimum value](https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes/min) attribute
- _max_ \- [maximum value](https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes/max) attribute
- _required_ \- if true, the input must be a valid date
- _validate_ \- a function to check whether the text input is valid
- _width_ \- the width of the input (not including the label)
- _submit_ \- whether to require explicit submission; defaults to false
- _readonly_ \- whether input is readonly; defaults to false
- _disabled_ \- whether input is disabled; defaults to false

The value of the input is a Date instance at UTC midnight of the specified date, or null if no (valid) value has been specified. Note that the displayed date format is [based on the browser’s locale](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/date).

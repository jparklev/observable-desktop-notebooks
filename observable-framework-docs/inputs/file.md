---
url: "https://observablehq.com/framework/inputs/file"
title: "File input | Observable Framework"
---

1. [Options](https://observablehq.com/framework/inputs/file#options)

# [File input](https://observablehq.com/framework/inputs/file\#file-input)

[API](https://github.com/observablehq/inputs/blob/main/README.md#file) · [Source](https://github.com/observablehq/inputs/blob/main/src/file.js) · The file input specifies a local file and is intended for prompting the user to select a file from their own machine. The exposed value provides the same interface as [`FileAttachment`](https://observablehq.com/framework/files) for convenient parsing in various formats such as text, image, JSON, CSV, ZIP, and XLSX.

By default, any file is allowed, and the value of the input resolves to null.

```js
const file = view(Inputs.file());
```

null

```js
file
```

We recommend providing a _label_ to improve usability.

Specify the _accept_ option to limit the allowed file extensions. This is useful when you intend to parse the file as a specific file format, such as CSV. By setting the _required_ option to true, the value of the input won’t resolve until the user choses a file.

CSV file

```js
const csvfile = view(Inputs.file({label: "CSV file", accept: ".csv", required: true}));
```

Once a file has been selected, you can read its contents like so:

```js
csvfile.csv({typed: true})
```

Here are examples of other supported file types.

JSON file

```js
const jsonfile = view(Inputs.file({label: "JSON file", accept: ".json", required: true}));
```

```js
jsonfile.json()
```

Text file

```js
const textfile = view(Inputs.file({label: "Text file", accept: ".txt", required: true}));
```

```js
textfile.text()
```

Image file

```js
const imgfile = view(Inputs.file({label: "Image file", accept: ".png,.jpg", required: true}));
```

```js
imgfile.image()
```

Excel file

```js
const xlsxfile = view(Inputs.file({label: "Excel file", accept: ".xlsx", required: true}));
```

```js
xlsxfile.xlsx()
```

ZIP archive

```js
const zipfile = view(Inputs.file({label: "ZIP archive", accept: ".zip", required: true}));
```

```js
zipfile.zip()
```

The _multiple_ option allows the user to pick multiple files. In this mode, the exposed value is an array of files instead of a single file.

Files

```js
const files = view(Inputs.file({label: "Files", multiple: true}));
```

Array(0) \[\]

```js
files
```

## [Options](https://observablehq.com/framework/inputs/file\#options)

**Inputs.file( _options_)**

The available file input options are:

- _label_ \- a label; either a string or an HTML element
- _required_ \- if true, a valid file must be selected
- _validate_ \- a function to check whether the file input is valid
- _accept_ \- the [acceptable file types](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/file#accept)
- _capture_ \- for [capturing image or video data](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/file#capture)
- _multiple_ \- whether to allow multiple files to be selected; defaults to false
- _width_ \- the width of the input (not including the label)
- _disabled_ \- whether input is disabled; defaults to false

The value of file input cannot be set programmatically; it can only be changed by the user.

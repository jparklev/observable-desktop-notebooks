---
url: "https://observablehq.com/framework/files"
title: "Files | Observable Framework"
---

1. [Static analysis](https://observablehq.com/framework/files#static-analysis)
2. [Supported formats](https://observablehq.com/framework/files#supported-formats)
3. [Basic formats](https://observablehq.com/framework/files#basic-formats)
4. [Binary formats](https://observablehq.com/framework/files#binary-formats)
5. [Routing](https://observablehq.com/framework/files#routing)

# [Files](https://observablehq.com/framework/files\#files)

Load files — whether static or generated dynamically by a [data loader](https://observablehq.com/framework/data-loaders) — using the built-in `FileAttachment` function. This is available by default in Markdown, but you can import it explicitly like so:

```js
import {FileAttachment} from "observablehq:stdlib";
```

The `FileAttachment` function takes a path and returns a file handle. This handle exposes:

- `name` \- the file’s name (such as `volcano.json`),
- `mimeType` \- [MIME type](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types) (such as `application/json`),
- `lastModified` \- modification time [Added in 1.4.0](https://github.com/observablehq/framework/releases/tag/v1.4.0 "Added in 1.4.0") (in milliseconds since epoch), and
- `size` \- size in bytes [Added in 1.11.0](https://github.com/observablehq/framework/releases/tag/v1.11.0 "Added in 1.11.0").

FileAttachment {name: "volcano.json", mimeType: "application/json", lastModified: 1767954143919, size: 20846}

```js
FileAttachment("volcano.json")
```

Like a [local import](https://observablehq.com/framework/imports#local-imports), the path is relative to the calling code’s source file: either the page’s Markdown file or the imported local JavaScript module. To load a remote file, use [`fetch`](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API), or use a [data loader](https://observablehq.com/framework/data-loaders) to download the file at build time.

Calling `FileAttachment` doesn’t actually load the file; the contents are only loaded when you invoke a [file contents method](https://observablehq.com/framework/files#supported-formats). For example, to load a JSON file:

```js
const volcano = FileAttachment("volcano.json").json();
```

The value of `volcano` above is a [promise](https://observablehq.com/framework/reactivity#promises). In other code blocks, the promise is implicitly awaited and hence you can refer to the resolved value directly.

Object {width: 87, height: 61, values: Array(5307)}

```js
volcano
```

## [Static analysis](https://observablehq.com/framework/files\#static-analysis)

The `FileAttachment` function can _only_ be passed a static string literal; constructing a dynamic path such as ``FileAttachment(`frame${i}.png`)`` is invalid syntax. Static analysis is used to invoke [data loaders](https://observablehq.com/framework/data-loaders) at build time, and ensures that only referenced files are included in the generated output during build. This also allows a content hash in the file name for cache breaking during deploy.

If you have multiple files, you can enumerate them explicitly like so:

```js
const frames = [\
  FileAttachment("frame1.png"),\
  FileAttachment("frame2.png"),\
  FileAttachment("frame3.png"),\
  FileAttachment("frame4.png"),\
  FileAttachment("frame5.png"),\
  FileAttachment("frame6.png"),\
  FileAttachment("frame7.png"),\
  FileAttachment("frame8.png"),\
  FileAttachment("frame9.png")\
];
```

None of the files in `frames` above are loaded until a [content method](https://observablehq.com/framework/files#supported-formats) is invoked, for example by saying `frames[0].image()`.

For missing files, `file.size` and `file.lastModified` are undefined. The `file.mimeType` is determined by checking the file extension against the [`mime-db` media type database](https://github.com/jshttp/mime-db); it defaults to `application/octet-stream`.

## [Supported formats](https://observablehq.com/framework/files\#supported-formats)

`FileAttachment` supports a variety of methods for loading file contents:

| method | return type |
| --- | --- |
| [`file.arquero`](https://observablehq.com/framework/lib/arquero) | Arquero [`Table`](https://idl.uw.edu/arquero/api/#table) |
| [`file.arrayBuffer`](https://observablehq.com/framework/files#binary-formats) | [`ArrayBuffer`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/ArrayBuffer) |
| [`file.arrow`](https://observablehq.com/framework/lib/arrow) | Arrow [`Table`](https://arrow.apache.org/docs/js/classes/Arrow.dom.Table.html) |
| [`file.blob`](https://observablehq.com/framework/files#binary-formats) | [`Blob`](https://developer.mozilla.org/en-US/docs/Web/API/Blob) |
| [`file.csv`](https://observablehq.com/framework/lib/csv) | [`Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array) |
| [`file.dsv`](https://observablehq.com/framework/lib/csv) | [`Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array) |
| [`file.html`](https://observablehq.com/framework/files#markup) | [`Document`](https://developer.mozilla.org/en-US/docs/Web/API/Document) |
| [`file.image`](https://observablehq.com/framework/files#media) | [`HTMLImageElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLImageElement) |
| [`file.json`](https://observablehq.com/framework/files#json) | [`Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array), [`Object`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object), _etc._ |
| [`file.parquet`](https://observablehq.com/framework/lib/arrow) | Arrow [`Table`](https://arrow.apache.org/docs/js/classes/Arrow.dom.Table.html) |
| [`file.sqlite`](https://observablehq.com/framework/lib/sqlite) | [`SQLiteDatabaseClient`](https://observablehq.com/framework/lib/sqlite) |
| [`file.stream`](https://observablehq.com/framework/files#binary-formats) | [`ReadableStream`](https://developer.mozilla.org/en-US/docs/Web/API/ReadableStream) |
| [`file.text`](https://observablehq.com/framework/files#text) | [`string`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String) |
| [`file.tsv`](https://observablehq.com/framework/lib/csv) | [`Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array) |
| [`file.xlsx`](https://observablehq.com/framework/lib/xlsx) | [`Workbook`](https://observablehq.com/framework/lib/xlsx) |
| [`file.xml`](https://observablehq.com/framework/files#markup) | [`Document`](https://developer.mozilla.org/en-US/docs/Web/API/Document) |
| [`file.zip`](https://observablehq.com/framework/lib/zip) | [`ZipArchive`](https://observablehq.com/framework/lib/zip) |

The contents of a file often dictate the appropriate method — for example, an Excel XLSX file is almost always read with `file.xlsx`. When multiple methods are valid, choose based on your needs. For example, you can load a CSV file using `file.arquero` to load it into [Arquero](https://observablehq.com/framework/lib/arquero) [Added in 1.10.0](https://github.com/observablehq/framework/releases/tag/v1.10.0 "Added in 1.10.0"), or even using `file.text` to implement parsing yourself.

In addition to the above, you can get the resolved absolute URL of the file using `file.href`: [Added in 1.5.0](https://github.com/observablehq/framework/releases/tag/v1.5.0 "Added in 1.5.0")

"https://observablehq.com/framework/\_file/volcano.f5223ec9.json"

```js
FileAttachment("volcano.json").href
```

See [file-based routing](https://observablehq.com/framework/files#routing) for additional details.

## [Basic formats](https://observablehq.com/framework/files\#basic-formats)

The following common basic formats are supported natively.

### [Text](https://observablehq.com/framework/files\#text)

To load a humble text file, use `file.text`:

```js
const hello = FileAttachment("hello.txt").text();
```

"Hello! I am a text file."

```js
hello
```

By default, `file.text` expects the file to be encoded in [UTF-8](https://en.wikipedia.org/wiki/UTF-8). To use a different encoding, pass the [desired encoding](https://developer.mozilla.org/en-US/docs/Web/API/Encoding_API/Encodings) name to `file.text`.

```js
const pryvit = FileAttachment("pryvit.txt").text("utf-16be");
```

"Привіт Світ"

```js
pryvit
```

### [JSON](https://observablehq.com/framework/files\#json)

To load a [JSON (JavaScript Object Notation)](https://www.json.org/) file, use `file.json`

Object {width: 87, height: 61, values: Array(5307)}

```js
FileAttachment("volcano.json").json()
```

A common gotcha with JSON is that it has no built-in date type; dates are therefore typically represented as ISO 8601 strings, or as a number of milliseconds or seconds since UNIX epoch.

### [Media](https://observablehq.com/framework/files\#media)

To display an image, you can use a static image in [Markdown](https://observablehq.com/framework/markdown) such as `<img src="horse.jpg">` or `![horse](horse.jpg)`. Likewise, you can use a `video` or `audio` element. Per [file-based routing](https://observablehq.com/framework/files#routing), static references to these files are automatically detected and therefore these files will be included in the built output.

```html
<video src="horse.mp4" autoplay muted loop controls></video>
```

If you want to manipulate an image in JavaScript, use `file.image`. For example, below we load an image and invert the RGB channel values.

```js
const canvas = document.querySelector("#horse-canvas");
const context = canvas.getContext("2d");
const horse = await FileAttachment("horse.jpg").image();
context.drawImage(horse, 0, 0, canvas.width, canvas.height);
const data = context.getImageData(0, 0, canvas.width, canvas.height);
for (let j = 0, k = 0; j < canvas.height; ++j) {
  for (let i = 0; i < canvas.width; ++i, k += 4) {
    data.data[k + 0] = 255 - data.data[k + 0];
    data.data[k + 1] = 255 - data.data[k + 1];
    data.data[k + 2] = 255 - data.data[k + 2];
  }
}
context.putImageData(data, 0, 0);
```

(The images above are from [Eadweard Muybridge](https://www.loc.gov/search/?fa=contributor:muybridge,+eadweard)’s studies of animal locomotion.)

### [Markup](https://observablehq.com/framework/files\#markup)

The `file.xml` method reads an XML file and returns a promise to a [`Document`](https://developer.mozilla.org/en-US/docs/Web/API/Document); it takes a single argument with the file’s MIME-type, which defaults to `"application/xml"`. The `file.html` method similarly reads an [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML) file; it is equivalent to `file.xml("text/html")`.

## [Binary formats](https://observablehq.com/framework/files\#binary-formats)

Load binary data using `file.blob` to get a [`Blob`](https://developer.mozilla.org/en-US/docs/Web/API/Blob), or `file.arrayBuffer` to get an [`ArrayBuffer`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/ArrayBuffer). For example, to read [Exif](https://en.wikipedia.org/wiki/Exif) image metadata with [ExifReader](https://github.com/mattiasw/ExifReader):

Object {Bits Per Sample: Object, Image Height: Object, Image Width: Object, Color Components: Object, Subsampling: Object, JFIF Version: Object, Resolution Unit: Object, XResolution: Object, YResolution: Object, JFIF Thumbnail Width: Object, JFIF Thumbnail Height: Object, FileType: Object}

```js
import ExifReader from "npm:exifreader";

const buffer = await FileAttachment("horse.jpg").arrayBuffer();
const tags = ExifReader.load(buffer);

display(tags);
```

To read a file incrementally, get a [`ReadableStream`](https://developer.mozilla.org/en-US/docs/Web/API/ReadableStream) with `file.stream`. For example, to count the number of bytes in a file:

631

```js
const stream = await FileAttachment("horse.jpg").stream();
const reader = stream.getReader();
let total = 0;

while (true) {
  const {done, value} = await reader.read();
  if (done) break;
  total += value.length;
}

display(total);
```

## [Routing](https://observablehq.com/framework/files\#routing)

Attached files live in the source root (typically `src`) alongside your Markdown pages. For example, say `index.md` has some JavaScript code that references `FileAttachment("quakes.csv")`:

```ini
.
├─ src
│  ├─ index.md
│  └─ quakes.csv
└─ …
```

On build, any files referenced by `FileAttachment` will automatically be copied to the `_file` folder under the output root (`dist`), here resulting in:

```ini
.
├─ dist
│  ├─ _file
│  │  └─ quakes.e5f2eb94.csv
│  ├─ _observablehq
│  │  └─ … # additional assets
│  └─ index.html
└─ …
```

`FileAttachment` references are automatically rewritten during build; for example, a reference to `quakes.csv` might be replaced with `_file/quakes.e5f2eb94.csv`. (As with imports, file names are given a content hash, here `e5f2eb94`, to improve performance.) Only the files you reference statically are copied to the output root (`dist`), so nothing extra or unused is included in the built site.

[Imported local modules](https://observablehq.com/framework/imports#local-imports) can use `FileAttachment`, too. In this case, the path to the file is _relative to the importing module_ in the same fashion as `import`; this is accomplished by resolving relative paths at runtime with [`import.meta.url`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/import.meta).

Some additional assets are automatically promoted to file attachments and copied to `_file`. For example, if you have a `<link rel="stylesheet" href="style.css">` declared statically in a Markdown page, the `style.css` file will be copied to `_file`, too (and the file name given a content hash). The HTML elements eligible for file attachments are `audio`, `img`, `link`, `picture`, and `video`.

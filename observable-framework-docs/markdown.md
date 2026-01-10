---
url: "https://observablehq.com/framework/markdown"
title: "Markdown | Observable Framework"
---

1. [Front matter](https://observablehq.com/framework/markdown#front-matter)
2. [HTML](https://observablehq.com/framework/markdown#html)
3. [Grids](https://observablehq.com/framework/markdown#grids)
4. [Cards](https://observablehq.com/framework/markdown#cards)
5. [Notes](https://observablehq.com/framework/markdown#notes)
6. [Basic syntax](https://observablehq.com/framework/markdown#basic-syntax)

# [Markdown](https://observablehq.com/framework/markdown\#markdown)

Markdown is a language for formatting text and content; it’s a lightweight, ergonomic alternative (and complement) to HTML. Markdown in Framework extends [CommonMark](https://commonmark.org/) with a handful of features useful for data apps, including [reactive](https://observablehq.com/framework/reactivity) [JavaScript](https://observablehq.com/framework/javascript), [HTML](https://observablehq.com/framework/markdown#html), [YAML front matter](https://observablehq.com/framework/markdown#front-matter), [grids](https://observablehq.com/framework/markdown#grids), [cards](https://observablehq.com/framework/markdown#cards), and [notes](https://observablehq.com/framework/markdown#notes). This page covers Framework’s extensions to Markdown, along with [basic syntax](https://observablehq.com/framework/markdown#basic-syntax).

## [Front matter](https://observablehq.com/framework/markdown\#front-matter)

```yaml
---
title: My favorite page
toc: false
---
```

The front matter supports the following options:

- **title** \- the page title; defaults to the (first) first-level heading of the page, if any
- **index** \- whether to index this page if [search](https://observablehq.com/framework/search) is enabled; defaults to true for listed pages
- **keywords** [Added in v1.1.0](https://github.com/observablehq/framework/releases/tag/v1.1.0 "Added in v1.1.0") \- additional words to index for [search](https://observablehq.com/framework/search); boosted at the same weight as the title
- **draft** [Added in v1.1.0](https://github.com/observablehq/framework/releases/tag/v1.1.0 "Added in v1.1.0") \- whether to skip this page during build; drafts are also not listed in the default sidebar nor searchable
- **sql** [Added in v1.2.0](https://github.com/observablehq/framework/releases/tag/v1.2.0 "Added in v1.2.0") \- table definitions for [SQL code blocks](https://observablehq.com/framework/sql)

The front matter can also override the following [app-level configuration](https://observablehq.com/framework/config) options:

- **toc** \- the [table of contents](https://observablehq.com/framework/config#toc)
- **style** \- the [custom stylesheet](https://observablehq.com/framework/config#style)
- **theme** \- the [theme](https://observablehq.com/framework/config#theme)
- **head** \- the [head](https://observablehq.com/framework/config#head)
- **header** \- the [header](https://observablehq.com/framework/config#header)
- **footer** \- the [footer](https://observablehq.com/framework/config#footer)
- **sidebar** \- whether to show the [sidebar](https://observablehq.com/framework/config#sidebar)

## [HTML](https://observablehq.com/framework/markdown\#html)

You can write HTML directly into Markdown. HTML is useful for greater control over layout, say to use CSS grid for a responsive bento box layout in a dashboard, or adding an external stylesheet via a link element. For example, here is an HTML details element:

```html
<details>
  <summary>Click me</summary>
  This text is not visible by default.
</details>
```

This produces:

Click me
This text is not visible by default.

You can put Markdown inside of HTML by surrounding it with blank lines:

This is **Markdown** inside of _HTML_!

```md
<div class="grid grid-cols-4">
  <div class="card">

This is **Markdown** inside of _HTML_!

  </div>
</div>
```

## [Grids](https://observablehq.com/framework/markdown\#grids)

The `grid` class declares a [CSS grid](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_grid_layout) container. The `grid` class is designed to pair with the [`card` class](https://observablehq.com/framework/markdown#cards) and the [`dashboard` theme](https://observablehq.com/framework/themes) for dashboard layout.

# A

# B

# C

# D

```html
<div class="grid grid-cols-4">
  <div class="card"><h1>A</h1></div>
  <div class="card"><h1>B</h1></div>
  <div class="card"><h1>C</h1></div>
  <div class="card"><h1>D</h1></div>
</div>
```

Grids have a single column by default, but you can declare two, three, or four columns using the `grid-cols-2`, `grid-cols-3`, or `grid-cols-4` class.

The built-in `grid` class is automatically responsive: in narrow windows, the number of columns is automatically reduced. The four-column grid can be reduced to two or one columns, while the three- and two-column grid can be reduced to one column. (If you want more columns or more control over the grid layout, you can always write custom styles.)

To see the responsive grid layout, resize the window or collapse the sidebar on the left. You can also zoom to change the effective window size.

With multi-column and multi-row grids, you can use the `grid-colspan-*` and `grid-rowspan-*` classes to have cells that span columns and rows, respectively.

# A

1 × 1

# B

1 × 2

# C

1 × 1

# D

2 × 1

```html
<div class="grid grid-cols-2">
  <div class="card"><h1>A</h1>1 × 1</div>
  <div class="card grid-rowspan-2"><h1>B</h1>1 × 2</div>
  <div class="card"><h1>C</h1>1 × 1</div>
  <div class="card grid-colspan-2"><h1>D</h1>2 × 1</div>
</div>
```

By default, the `grid` uses `grid-auto-rows: 1fr`, which means that every row of the grid has the same height. The “rhythm” of equal-height rows is often desirable.

Call me Ishmael.

Some years ago—never mind how long precisely—having little or no money in my purse, and nothing particular to interest me on shore, I thought I would sail about a little and see the watery part of the world.

It is a way I have of driving off the spleen and regulating the circulation.

```html
<div class="grid grid-cols-2">
  <div class="card">Call me Ishmael.</div>
  <div class="card">Some years ago—never mind how long precisely—having little or no money in my purse, and nothing particular to interest me on shore, I thought I would sail about a little and see the watery part of the world.</div>
  <div class="card">It is a way I have of driving off the spleen and regulating the circulation.</div>
</div>
```

On the other hand, forcing all rows to the same height can waste space, since the height of all rows is based on the tallest content across rows. To have variable-height rows instead, you can either set [`grid-auto-rows`](https://developer.mozilla.org/en-US/docs/Web/CSS/grid-auto-rows) on the grid container:

Call me Ishmael.

Some years ago—never mind how long precisely—having little or no money in my purse, and nothing particular to interest me on shore, I thought I would sail about a little and see the watery part of the world.

It is a way I have of driving off the spleen and regulating the circulation.

```html
<div class="grid grid-cols-2" style="grid-auto-rows: auto;">
  <div class="card">Call me Ishmael.</div>
  <div class="card">Some years ago—never mind how long precisely—having little or no money in my purse, and nothing particular to interest me on shore, I thought I would sail about a little and see the watery part of the world.</div>
  <div class="card">It is a way I have of driving off the spleen and regulating the circulation.</div>
</div>
```

Or break your grid into multiple grids:

Call me Ishmael.

Some years ago—never mind how long precisely—having little or no money in my purse, and nothing particular to interest me on shore, I thought I would sail about a little and see the watery part of the world.

It is a way I have of driving off the spleen and regulating the circulation.

```html
<div class="grid grid-cols-2">
  <div class="card">Call me Ishmael.</div>
  <div class="card">Some years ago—never mind how long precisely—having little or no money in my purse, and nothing particular to interest me on shore, I thought I would sail about a little and see the watery part of the world.</div>
</div>
<div class="grid grid-cols-2">
  <div class="card">It is a way I have of driving off the spleen and regulating the circulation.</div>
</div>
```

The `card` class is not required to use `grid`. If you use `grid` by itself, you’ll get the same layout but without the card aesthetics.

Some years ago—never mind how long precisely—having little or no money in my purse, and nothing particular to interest me on shore, I thought I would sail about a little and see the watery part of the world.

Call me Ishmael.

```html
<div class="grid grid-cols-2">
  <div>Some years ago—never mind how long precisely—having little or no money in my purse, and nothing particular to interest me on shore, I thought I would sail about a little and see the watery part of the world.</div>
  <div class="card">Call me Ishmael.</div>
</div>
```

Use the `resize` helper to re-render content when the container resizes.

This card is 1904px wide.

```html
<div class="grid grid-cols-4">
  <div class="card">
    ${resize((width) => `This card is ${width}px wide.`)}
  </div>
</div>
```

See [Responsive display](https://observablehq.com/framework/javascript#responsive-display) for more.

## [Cards](https://observablehq.com/framework/markdown\#cards)

The `card` class is used to group and delineate content. The `card` classes applies a background and border (with colors determined by the current [theme](https://observablehq.com/framework/themes)). A card can have a title and subtitle using `h2` and `h3` elements, respectively.

## It gets hotter during summer

### And months have 28–31 days

0123456789101112345678910111213141516171819202122232425262728293031

```html
<div class="card" style="max-width: 640px;">
  <h2>It gets hotter during summer</h2>
  <h3>And months have 28–31 days</h3>
  ${Plot.cell(weather.slice(-365), {x: (d) => d.date.getUTCDate(), y: (d) => d.date.getUTCMonth(), fill: "temp_max", tip: true, inset: 0.5}).plot({marginTop: 0, height: 240, padding: 0})}
</div>
```

[Observable Plot](https://observablehq.com/framework/lib/plot)’s **title** and **subtitle** options generate `h2` and `h3` elements, respectively, and so will inherit these card styles.

Cards can be used on their own, but they most often exist in a [grid](https://observablehq.com/framework/markdown#grids). Cards can contain whatever you like, including text, images, charts, tables, inputs, and more.

## Lorem ipsum

Id ornare arcu odio ut sem nulla pharetra. Aliquet lectus proin nibh nisl condimentum id venenatis a. Feugiat sed lectus vestibulum mattis ullamcorper velit. Aliquet nec ullamcorper sit amet. Sit amet tellus cras adipiscing. Condimentum id venenatis a condimentum vitae. Semper eget duis at tellus. Ut faucibus pulvinar elementum integer enim.

Et malesuada fames ac turpis. Integer vitae justo eget magna fermentum iaculis eu non diam. Aliquet risus feugiat in ante metus dictum at. Consectetur purus ut faucibus pulvinar.

|  | date | industry | unemployed |
| --- | --- | --- | --- |
|  | 2000-01-01 | Wholesale and Retail Trade | 1,000 |
|  | 2000-01-01 | Manufacturing | 734 |
|  | 2000-01-01 | Leisure and hospitality | 782 |
|  | 2000-01-01 | Business services | 655 |
|  | 2000-01-01 | Construction | 745 |
|  | 2000-01-01 | Education and Health | 353 |
|  | 2000-01-01 | Government | 430 |
|  | 2000-01-01 | Finance | 228 |
|  | 2000-01-01 | Self-employed | 239 |
|  | 2000-01-01 | Other | 274 |
|  | 2000-01-01 | Transportation and Utilities | 236 |
|  | 2000-01-01 | Information | 125 |
|  | 2000-01-01 | Agriculture | 154 |
|  | 2000-01-01 | Mining and Extraction | 19 |
|  | 2000-02-01 | Wholesale and Retail Trade | 1,023 |
|  | 2000-02-01 | Manufacturing | 694 |
|  | 2000-02-01 | Leisure and hospitality | 779 |
|  | 2000-02-01 | Business services | 587 |
|  | 2000-02-01 | Construction | 812 |
|  | 2000-02-01 | Education and Health | 349 |
|  | 2000-02-01 | Government | 409 |
|  | 2000-02-01 | Finance | 240 |
|  | 2000-02-01 | Self-employed | 262 |

```html
<div class="grid grid-cols-2">
  <div class="card">
    <h2>Lorem ipsum</h2>
    <p>Id ornare arcu odio ut sem nulla pharetra. Aliquet lectus proin nibh nisl condimentum id venenatis a. Feugiat sed lectus vestibulum mattis ullamcorper velit. Aliquet nec ullamcorper sit amet. Sit amet tellus cras adipiscing. Condimentum id venenatis a condimentum vitae. Semper eget duis at tellus. Ut faucibus pulvinar elementum integer enim.</p>
    <p>Et malesuada fames ac turpis. Integer vitae justo eget magna fermentum iaculis eu non diam. Aliquet risus feugiat in ante metus dictum at. Consectetur purus ut faucibus pulvinar.</p>
  </div>
  <div class="card" style="padding: 0;">
    ${Inputs.table(industries)}
  </div>
</div>
```

Remove the padding from a card if it contains only a table.

To place an input inside a card, first declare a detached input as a [top-level variable](https://observablehq.com/framework/reactivity#top-level-variables) and use [`Generators.input`](https://observablehq.com/framework/lib/generators#input-element) to expose its reactive value:

```js
const industryInput = Inputs.select(industries.map((d) => d.industry), {unique: true, sort: true, label: "Industry:"});
const industry = Generators.input(industryInput);
```

Then, insert the input into the card:

Industry:AgricultureBusiness servicesConstructionEducation and HealthFinanceGovernmentInformationLeisure and hospitalityManufacturingMining and ExtractionOtherSelf-employedTransportation and UtilitiesWholesale and Retail Trade

050100150200250300↑ Unemployed (thousands)Jan2000AprJulOctJan2001AprJulOctJan2002AprJulOctJan2003AprJulOctJan2004AprJulOctJan2005AprJulOctJan2006AprJulOctJan2007AprJulOctJan2008AprJulOctJan2009AprJulOctJan2010

```html
<div class="card" style="display: flex; flex-direction: column; gap: 1rem;">
  ${industryInput}
  ${resize((width) => Plot.plot({
    width,
    y: {grid: true, label: "Unemployed (thousands)"},
    marks: [\
      Plot.areaY(industries.filter((d) => d.industry === industry), {x: "date", y: "unemployed", fill: "var(--theme-foreground-muted)", curve: "step"}),\
      Plot.lineY(industries.filter((d) => d.industry === industry), {x: "date", y: "unemployed", curve: "step"}),\
      Plot.ruleY([0])\
    ]
  }))}
</div>
```

## [Notes](https://observablehq.com/framework/markdown\#notes)

The `note`, `tip`, `warning`, and `caution` classes can be used to insert labeled notes (also known as callouts) into prose. These are intended to emphasize important information that could otherwise be overlooked.

This is a note.

```html
<div class="note">This is a note.</div>
```

This is a tip.

```html
<div class="tip">This is a tip.</div>
```

This is a warning.

```html
<div class="warning">This is a warning.</div>
```

This is a caution.

```html
<div class="caution">This is a caution.</div>
```

Per [CommonMark](https://spec.commonmark.org/0.30/#html-blocks), the contents of an HTML block (such as a `<div class="note">`) are interpreted as HTML. For rich formatting or links within a note, use HTML.

This is a _styled_ tip using HTML.

```html
<div class="tip">
  <p>This is a <i>styled</i> tip using <small>HTML</small>.</p>
</div>
```

Alternatively, use blank lines to separate the contents of the note from the note container, and then the contents will be interpreted as Markdown.

This is a _styled_ tip using **Markdown**.

```md
<div class="tip">

This is a *styled* tip using **Markdown**.

</div>
```

You can override the note’s label using the `label` attribute.

No lifeguard on duty. Swim at your own risk!

```html
<div class="warning" label="⚠️ Danger ⚠️">No lifeguard on duty. Swim at your own risk!</div>
```

You can disable the label entirely with an empty `label` attribute.

This note has no label.

```html
<div class="note" label>This note has no label.</div>
```

## [Basic syntax](https://observablehq.com/framework/markdown\#basic-syntax)

Here are some examples of common Markdown features.

For more, see [GitHub’s guide to Markdown](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax).

### [Headings](https://observablehq.com/framework/markdown\#headings)

```md
# A first-level heading
## A second-level heading
### A third-level heading
```

A second-level heading (`##`) immediately following a first-level heading (`#`) is styled specially as a subtitle.

### [Styling](https://observablehq.com/framework/markdown\#styling)

```md
this is **bold** text
this is __bold__ text
this is *italic* text
this is _italic_ text
this is ~~strikethrough~~ text
this is `monospaced` text
> this is quoted text
```

### [Tables](https://observablehq.com/framework/markdown\#tables)

```md
Column 1   | Column 2     | Column 3
---------- | ------------ | ----------
Cell 1-1   | Cell 2-1     | Cell 3-1
Cell 1-2   | Cell 2-2     | Cell 3-2
```

```md
Align left | Align center | Align right
:--------- | :----------: | ----------:
Cell 1-1   |   Cell 2-1   |    Cell 3-1
Cell 1-2   |   Cell 2-2   |    Cell 3-2
```

### [Lists](https://observablehq.com/framework/markdown\#lists)

```md
- red
- green
- blue
  - light blue
  - dark blue
```

```md
1. first
1. second
1. third
   1. third first
   1. third second
```

### [Links](https://observablehq.com/framework/markdown\#links)

```md
<https://example.com>
[relative link](./dashboard)
[external link](https://example.com)
[external link](<https://en.wikipedia.org/wiki/Tar_(computing)>)
```

For privacy and convenience, external links are given a default `rel` attribute of [`noreferrer`](https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes/rel/noreferrer) [`noopener`](https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes/rel/noopener) and a default `target` attribute of [`_blank`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/a#target). [Added in 1.5.0](https://github.com/observablehq/framework/releases/tag/v1.5.0 "Added in 1.5.0") Hence by default an external link will open in a new window and not pass the (potentially sensitive) referrer to the (potentially untrusted) external site. You can override this behavior by specifying the `rel` or `target` attribute explicitly. For example `<a href="https://example.com" target="_self">` will open in the same window, and `<a href="https://acme.com" rel="">` will allow the referrer.

Framework normalizes page links, converting absolute paths into relative paths. This allows built sites to be served correctly under any root when deployed. This means you can use absolute paths, such as `/index` for the main page, to link to pages from any other page, including the global [header](https://observablehq.com/framework/config#header) or [footer](https://observablehq.com/framework/config#footer).

To link to a page or asset that’s _not_ controlled by Framework (or to disable link normalization), set the [`rel` attribute](https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes/rel) to `external`. [Added in 1.10.1](https://github.com/observablehq/framework/releases/tag/v1.10.1 "Added in 1.10.1") For example:

```html
<a href="/robots.txt" rel="external">robots.txt</a>
```

You may also want to add `noopener noreferrer` if linking to an untrusted origin. See also [Files: Media](https://observablehq.com/framework/files#media) regarding images and other linked assets.

### [Images](https://observablehq.com/framework/markdown\#images)

```md
![A horse](./horse.jpg)
![A happy kitten](https://placekitten.com/200/300)
```

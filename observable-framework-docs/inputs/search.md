---
url: "https://observablehq.com/framework/inputs/search"
title: "Search input | Observable Framework"
---

1. [Options](https://observablehq.com/framework/inputs/search#options)

# [Search input](https://observablehq.com/framework/inputs/search\#search-input)

[API](https://github.com/observablehq/inputs/blob/main/README.md#search) · [Source](https://github.com/observablehq/inputs/blob/main/src/search.js) · The search input allows freeform, full-text search of a tabular dataset (or a single column of values) using a simple query parser. It is often paired with a [table input](https://observablehq.com/framework/inputs/table).

By default, the query is split into terms separated by spaces; each term is then prefix-matched against the property values (the fields) of each row in the data. Try searching for “gen” below to find Gentoo penguins.

344 results

```js
const search = view(Inputs.search(penguins, {placeholder: "Search penguins…"}));
```

Array(344) \[Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, …\]

```js
search
```

Or, as a table:

|  | species | island | culmen\_length\_mm | culmen\_depth\_mm | flipper\_length\_mm | body\_mass\_g | sex |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | Adelie | Torgersen | 39.1 | 18.7 | 181 | 3,750 | MALE |
|  | Adelie | Torgersen | 39.5 | 17.4 | 186 | 3,800 | FEMALE |
|  | Adelie | Torgersen | 40.3 | 18 | 195 | 3,250 | FEMALE |
|  | Adelie | Torgersen |  |  |  |  |  |
|  | Adelie | Torgersen | 36.7 | 19.3 | 193 | 3,450 | FEMALE |
|  | Adelie | Torgersen | 39.3 | 20.6 | 190 | 3,650 | MALE |
|  | Adelie | Torgersen | 38.9 | 17.8 | 181 | 3,625 | FEMALE |
|  | Adelie | Torgersen | 39.2 | 19.6 | 195 | 4,675 | MALE |
|  | Adelie | Torgersen | 34.1 | 18.1 | 193 | 3,475 |  |
|  | Adelie | Torgersen | 42 | 20.2 | 190 | 4,250 |  |
|  | Adelie | Torgersen | 37.8 | 17.1 | 186 | 3,300 |  |
|  | Adelie | Torgersen | 37.8 | 17.3 | 180 | 3,700 |  |
|  | Adelie | Torgersen | 41.1 | 17.6 | 182 | 3,200 | FEMALE |
|  | Adelie | Torgersen | 38.6 | 21.2 | 191 | 3,800 | MALE |
|  | Adelie | Torgersen | 34.6 | 21.1 | 198 | 4,400 | MALE |
|  | Adelie | Torgersen | 36.6 | 17.8 | 185 | 3,700 | FEMALE |
|  | Adelie | Torgersen | 38.7 | 19 | 195 | 3,450 | FEMALE |
|  | Adelie | Torgersen | 42.5 | 20.7 | 197 | 4,500 | MALE |
|  | Adelie | Torgersen | 34.4 | 18.4 | 184 | 3,325 | FEMALE |
|  | Adelie | Torgersen | 46 | 21.5 | 194 | 4,200 | MALE |
|  | Adelie | Biscoe | 37.8 | 18.3 | 174 | 3,400 | FEMALE |
|  | Adelie | Biscoe | 37.7 | 18.7 | 180 | 3,600 | MALE |
|  | Adelie | Biscoe | 35.9 | 19.2 | 189 | 3,800 | FEMALE |

```js
Inputs.table(search)
```

If you search for multiple terms, such as “gen bis” (for Gentoos on the Biscoe Islands) or “gen fem” (for female Gentoos), every term must match: there’s an implicit logical AND.

If you’d like different search syntax or behavior, pass the _filter_ option. This function is passed the current search query and returns the [filter test function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/filter) to be applied to the data.

## [Options](https://observablehq.com/framework/inputs/search\#options)

**Inputs.search( _data_, _options_)**

The available search input options are:

- _label_ \- a label; either a string or an HTML element
- _query_ \- the initial search terms; defaults to the empty string
- _placeholder_ \- a placeholder string for when the query is empty
- _columns_ \- an array of columns to search; defaults to _data_.columns
- _locale_ \- the current locale; defaults to English
- _format_ \- a function to show the number of results
- _spellcheck_ \- whether to activate the browser’s spell-checker
- _autocomplete_ \- the [autocomplete](https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes/autocomplete) attribute, as text or boolean
- _autocapitalize_ \- the [autocapitalize](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/autocapitalize) attribute, as text or boolean
- _filter_ \- the filter factory: a function that receives the query and returns a filter
- _width_ \- the width of the input (not including the label)
- _datalist_ \- an iterable of suggested values
- _disabled_ \- whether input is disabled; defaults to false
- _required_ \- if true, the search’s value is all _data_ if no query; defaults to true

If a _filter_ function is specified, it is invoked whenever the query changes; the function it returns is then passed each element from _data_, along with its zero-based index, and should return a truthy value if the given element matches the query. The default filter splits the current query into space-separated tokens and checks that each token matches the beginning of at least one string in the data’s columns, case-insensitive. For example, the query \[hello world\] will match the string “Worldwide Hello Services” but not “hello”.

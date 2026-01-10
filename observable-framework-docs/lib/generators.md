---
url: "https://observablehq.com/framework/lib/generators"
title: "Observable Generators | Observable Framework"
---

1. [input(element)](https://observablehq.com/framework/lib/generators#input-element)
2. [observe(initialize)](https://observablehq.com/framework/lib/generators#observe-initialize)
3. [queue(change)](https://observablehq.com/framework/lib/generators#queue-change)
4. [now()](https://observablehq.com/framework/lib/generators#now)
5. [width(element)](https://observablehq.com/framework/lib/generators#width-element)
6. [dark()](https://observablehq.com/framework/lib/generators#dark)

# [Observable Generators](https://observablehq.com/framework/lib/generators\#observable-generators)

The Observable standard library includes several generator utilities. These are available by default in Markdown as `Generators`, but you can import them explicitly:

```js
import {Generators} from "observablehq:stdlib";
```

## [input( _element_)](https://observablehq.com/framework/lib/generators\#input-element)

[Source](https://github.com/observablehq/framework/blob/main/src/client/stdlib/generators/input.js) · Returns an async generator that yields whenever the given _element_ emits an _input_ event, with the given _element_’s current value. (It’s a bit fancier than that because we special-case a few element types.) The built-in [`view` function](https://observablehq.com/framework/reactivity#inputs) uses this.

```js
const nameInput = display(document.createElement("input"));
const name = Generators.input(nameInput);
```

""

```js
name
```

## [observe( _initialize_)](https://observablehq.com/framework/lib/generators\#observe-initialize)

[Source](https://github.com/observablehq/framework/blob/main/src/client/stdlib/generators/observe.js) · Returns an async generator that immediately invokes the specified _initialize_ function, being passed a _change_ callback function, and yields the passed value whenever _change_ is called. The _initialize_ function may optionally return a _dispose_ function that will be called when the generator is terminated.

```js
const hash = Generators.observe((change) => {
  const changed = () => change(location.hash);
  addEventListener("hashchange", changed);
  changed();
  return () => removeEventListener("hashchange", changed);
});
```

""

```js
hash
```

## [queue( _change_)](https://observablehq.com/framework/lib/generators\#queue-change)

[Source](https://github.com/observablehq/framework/blob/main/src/client/stdlib/generators/queue.js) · Returns an async generator that immediately invokes the specified _initialize_ function, being passed a _change_ callback function, and yields the passed value whenever _change_ is called. The _initialize_ function may optionally return a _dispose_ function that will be called when the generator is terminated.

This is identical to `Generators.observe` except that if _change_ is called multiple times before the consumer has a chance to process the yielded result, values will not be dropped; use this if you require that the consumer not miss a yielded value.

```js
const hash = Generators.queue((change) => {
  const changed = () => change(location.hash);
  addEventListener("hashchange", changed);
  changed();
  return () => removeEventListener("hashchange", changed);
});
```

""

```js
hash
```

## [now()](https://observablehq.com/framework/lib/generators\#now)

[Source](https://github.com/observablehq/framework/blob/main/src/client/stdlib/generators/now.js) · Returns a generator that repeatedly yields `Date.now()`, forever. This generator is available by default as `now` in Markdown.

```js
const now = Generators.now();
```

1768013365401

```js
now
```

## [width( _element_)](https://observablehq.com/framework/lib/generators\#width-element)

[Source](https://github.com/observablehq/framework/blob/main/src/client/stdlib/generators/width.ts) · Returns an async generator that yields the width of the given target _element_. Using a [ResizeObserver](https://developer.mozilla.org/en-US/docs/Web/API/ResizeObserver), the generator will yield whenever the width of the _element_ changes. This generator for the `main` element is available by default as `width` in Markdown.

```js
const width = Generators.width(document.querySelector("main"));
```

1888

```js
width
```

## [dark()](https://observablehq.com/framework/lib/generators\#dark) [Added in 1.3.0](https://github.com/observablehq/framework/releases/tag/v1.3.0 "Added in 1.3.0")

[Source](https://github.com/observablehq/framework/blob/main/src/client/stdlib/generators/dark.ts) · Returns an async generator that yields a boolean indicating whether the page is currently displayed with a dark [color scheme](https://developer.mozilla.org/en-US/docs/Web/CSS/color-scheme).

```js
const dark = Generators.dark();
```

If the page supports both light and dark mode (as with the [default theme](https://observablehq.com/framework/themes)), the value reflects the user’s [preferred color scheme](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-color-scheme). The generator will yield a new value if the preferred color changes — as when the user changes their system settings, or if the user’s system adapts automatically to the diurnal cycle — allowing you to update the display as needed without requiring a page reload.

If the page only supports light mode, the value is always false; likewise it is always true if the page only has a dark theme.

The current theme is: _light_.

```md
The current theme is: *${dark ? "dark" : "light"}*.
```

This generator is available by default as `dark` in Markdown. It can be used to pick a [color scheme](https://observablehq.com/plot/features/scales#color-scales) for a chart, or an appropriate [mix-blend-mode](https://developer.mozilla.org/en-US/docs/Web/CSS/mix-blend-mode):

0100200300400↑ Frequency406080100120140160weight →

```js
Plot.plot({
  height: 260,
  color: {scheme: dark ? "turbo" : "ylgnbu"},
  marks: [\
    Plot.rectY(\
      olympians,\
      Plot.binX(\
        {y2: "count"},\
        {\
          x: "weight",\
          fill: "weight",\
          z: "sex",\
          mixBlendMode: dark ? "screen" : "multiply"\
        }\
      )\
    ),\
    Plot.ruleY([0])\
  ]
})
```

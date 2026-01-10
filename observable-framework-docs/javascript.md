---
url: "https://observablehq.com/framework/javascript"
title: "JavaScript | Observable Framework"
---

01. [Fenced code blocks](https://observablehq.com/framework/javascript#fenced-code-blocks)
02. [Inline expressions](https://observablehq.com/framework/javascript#inline-expressions)
03. [TypeScript](https://observablehq.com/framework/javascript#type-script)
04. [Explicit display](https://observablehq.com/framework/javascript#explicit-display)
05. [Implicit display](https://observablehq.com/framework/javascript#implicit-display)
06. [Responsive display](https://observablehq.com/framework/javascript#responsive-display)
07. [display(value)](https://observablehq.com/framework/javascript#display-value)
08. [resize(render)](https://observablehq.com/framework/javascript#resize-render)
09. [width](https://observablehq.com/framework/javascript#width)
10. [now](https://observablehq.com/framework/javascript#now)

# [JavaScript](https://observablehq.com/framework/javascript\#java-script)

Use JavaScript to render charts, inputs, and other dynamic, interactive, and graphical content on the client. JavaScript in [Markdown](https://observablehq.com/framework/markdown) can be expressed either as [fenced code blocks](https://observablehq.com/framework/javascript#fenced-code-blocks) or [inline expressions](https://observablehq.com/framework/javascript#inline-expressions). You can also [import](https://observablehq.com/framework/imports) JavaScript modules to share code across pages.

JavaScript runs on load, and re-runs [reactively](https://observablehq.com/framework/reactivity) when variables change.

## [Fenced code blocks](https://observablehq.com/framework/javascript\#fenced-code-blocks)

JavaScript fenced code blocks (``````js```) are typically used to display content such as charts and inputs. They can also be used to declare top-level variables, say to load data or declare helper functions.

JavaScript blocks come in two forms: _expression_ blocks and _program_ blocks. An expression block looks like this (and note the lack of semicolon):

````md
```js
1 + 2
```
````

Expression blocks [implicitly display](https://observablehq.com/framework/javascript#implicit-display), producing:

3

A program block looks like this (note the semicolon):

```js
const foo = 1 + 2;
```

A program block doesn’t display anything by default, but you can call [`display`](https://observablehq.com/framework/javascript#display-value) to display something.

JavaScript blocks do not show their code by default. If you want to show the code, use the `echo` directive:

````md
```js echo
1 + 2
```
````

The code is rendered below the output, like so:

3

```js
1 + 2
```

Alternatively, if you just want to show the code _without_ running it, set the `run` directive to `false`:

````md
```js run=false
1 + 2
```
````

If an expression evaluates to a DOM node, the node is inserted into the page directly above the code block. Use this to create dynamic content such as charts and tables.

\[insert chart here\]

```js
document.createTextNode("[insert chart here]") // some imagination required
```

You can use the [DOM API](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model) to create content as above, but typically you’ll use a helper library such as [Hypertext Literal](https://observablehq.com/framework/lib/htl), [Observable Plot](https://observablehq.com/framework/lib/plot), or [D3](https://observablehq.com/framework/lib/d3) to create content. For example, here’s a component that displays a greeting:

```js
function greeting(name) {
  return html`Hello, <i>${name}</i>!`;
}
```

Hello, _world_!

```js
greeting("world")
```

And here’s a line chart of Apple’s stock price using [Observable Plot](https://observablehq.com/framework/lib/plot):

60708090100110120130140150160170180190↑ Close20142015201620172018

```js
Plot.lineY(aapl, {x: "Date", y: "Close"}).plot({y: {grid: true}})
```

Code blocks automatically re-run when referenced [reactive variables](https://observablehq.com/framework/reactivity) change, or when you edit the page during preview. The block below references the built-in variable `now` representing the current time in milliseconds; because `now` is reactive, this block runs sixty times a second and each each new span it returns replaces the one previously displayed.

Rainbow text!

```js
html`<span style=${{color: `hsl(${(now / 10) % 360} 100% 50%)`}}>Rainbow text!</span>`
```

## [Inline expressions](https://observablehq.com/framework/javascript\#inline-expressions)

JavaScript inline expressions `${…}` interpolate values into Markdown. They are typically used to display numbers such as metrics, or to arrange visual elements such as charts into rich HTML layouts.

For example, this paragraph simulates rolling a 20-sided dice:

```md
You rolled ${Math.floor(Math.random() * 20) + 1}.
```

You rolled 8. (Reload the page to re-roll.)

Like fenced code blocks, inline expressions automatically re-run when referenced reactive variables change or when you edit the page during preview.

The current time is 9:45:31 PM.

```md
The current time is ${new Date(now).toLocaleTimeString("en-US")}.
```

Likewise, if an inline expression evaluates to a DOM element or node, it will be inserted into the page. For example, you can…

interpolate a sparkline

```md
interpolate a sparkline ${Plot.plot({axis: null, margin: 0, width: 80, height: 17, x: {type: "band", round: false}, marks: [Plot.rectY(aapl.slice(-15 - number, -1 - number), {x: "Date", y1: 150, y2: "Close", fill: "var(--theme-foreground-focus)"})]})}
```

or even a reactive input  0

```md
or even a reactive input ${Inputs.bind(html`<input type=range style="width: 120px;">`, numberInput)} ${number}
```

into prose.

```js
const numberInput = Inputs.input(0);
const number = Generators.input(numberInput);
```

Expressions cannot declare top-level reactive variables. To declare a variable, use a code block instead. You can declare a variable in a code block (without displaying it) and then display it somewhere else using an inline expression.

## [TypeScript](https://observablehq.com/framework/javascript\#type-script) [Added in 1.11.0](https://github.com/observablehq/framework/releases/tag/v1.11.0 "Added in 1.11.0")

TypeScript fenced code blocks (``````ts```) allow TypeScript to be used in place of JavaScript. You can also import TypeScript modules (`.ts`). Use the `.js` file extension when importing TypeScript modules; TypeScript is transpiled to JavaScript during build.

Framework does not perform type checking during preview or build. If you want the additional safety of type checks, considering using [`tsc`](https://www.typescriptlang.org/docs/handbook/compiler-options.html).

TypeScript fenced code blocks do not currently support [implicit display](https://observablehq.com/framework/javascript#implicit-display), and TypeScript is not currently allowed in [inline expressions](https://observablehq.com/framework/javascript#inline-expressions).

## [Explicit display](https://observablehq.com/framework/javascript\#explicit-display)

The built-in [`display` function](https://observablehq.com/framework/javascript#display-value) displays the specified value.

0.8159814123091581

```js
const x = Math.random();

display(x);
```

You can display structured objects, too. Click on the object below to inspect it.

Object {hello: Object, numbers: Array(4)}

```js
display({hello: {subject: "world"}, numbers: [1, 2, 3, 4]})
```

Calling `display` multiple times will display multiple values. Values are displayed in the order they are received. Previously-displayed values will be cleared when the associated code block or inline expression is invalidated.

0

1

2

3

4

```js
for (let i = 0; i < 5; ++i) {
  display(i);
}
```

If you pass `display` a DOM node, it will be inserted directly into the page. Use this technique to render dynamic displays of data, such as charts and tables.

Your lucky number is 2!

```js
display(html`Your lucky number is ${Math.floor(Math.random () * 10)}!`);
```

This is a contrived example — you normally use an [inline expression](https://observablehq.com/framework/javascript#inline-expressions) to interpolate a value into Markdown. For example:

```md
Your lucky number is ${Math.floor(Math.random () * 10)}!
```

The `display` function returns the passed-in value. You can display any value (any expression) in code, not only top-level variables; use this as an alternative to `console.log` to debug your code.

0.16644519791232748

```js
const y = display(Math.random());
```

The value of `y` is 0.16644519791232748.

```md
The value of `y` is ${y}.
```

When the value passed to `display` is not a DOM element or node, the behavior of `display` depends on whether it is called within a fenced code block or an inline expression. In fenced code blocks, `display` will use the [inspector](https://github.com/observablehq/inspector).

Array(3) \[1, 2, 3\]

```js
display([1, 2, 3]);
```

In inline expressions, `display` will coerce non-DOM values to strings and concatenate iterables.

123

```md
${display([1, 2, 3])}
```

The `display` function is scoped to each code block, meaning that the `display` function is a closure bound to where it will display on the page. But you can capture a code block’s `display` function by assigning it to a top-level variable:

```js
const displayThere = display;
```

Then you can reference it from other cells:

Click me

```js
Inputs.button("Click me", {value: 0, reduce: (i) => displayThere(++i)})
```

## [Implicit display](https://observablehq.com/framework/javascript\#implicit-display)

JavaScript expression fenced code blocks are implicitly wrapped with a call to [`display`](https://observablehq.com/framework/javascript#display-value). For example, this arithmetic expression displays implicitly:

3

```js
1 + 2 // implicit display
```

Implicit display only applies to expression code blocks, not program code blocks: the value won’t implicitly display if you add a semicolon. (Watch out for [Prettier](https://prettier.io/)!)

```js
1 + 2; // no implicit display
```

Implicit display also doesn’t apply if you reference the `display` function explicitly ( _i.e._, we wouldn’t want to show `2` twice below).

1

2

```js
display(1), display(2) // no implicit display
```

The same is true for inline expressions `${…}`.

3

```md
${1 + 2}
```

12

```md
${display(1), display(2)}
```

Implicit display also implicitly awaits promises.

## [Responsive display](https://observablehq.com/framework/javascript\#responsive-display)

In Markdown, the built-in [`width` reactive variable](https://observablehq.com/framework/javascript#width) represents the current width of the main element. This variable is implemented by [`Generators.width`](https://observablehq.com/framework/lib/generators#width-element) and backed by a [`ResizeObserver`](https://developer.mozilla.org/en-US/docs/Web/API/ResizeObserver). The reactive width can be a handy thing to pass, say, as the **width** option to [Observable Plot](https://observablehq.com/framework/lib/plot).

01234567890.00.51.01.52.02.53.03.54.04.55.05.56.06.57.07.58.08.59.09.510.010.511.0

```js
Plot.barX([9, 4, 8, 1, 11, 3, 4, 2, 7, 5]).plot({width})
```

For non-top-level elements, as when rendering content within an inline expression, use the built-in [`resize` function](https://observablehq.com/framework/javascript#resize-render) instead. This takes a _render_ function which is called whenever the width or height [changes](https://developer.mozilla.org/en-US/docs/Web/API/ResizeObserver), and the element returned by the render function is inserted into the DOM.

01234567890.00.51.01.52.02.53.03.54.04.55.05.56.06.57.07.58.08.59.09.510.010.511.0

```html
<div class="card">
  ${resize((width) => Plot.barX([9, 4, 8, 1, 11, 3, 4, 2, 7, 5]).plot({width}))}
</div>
```

If your container defines a height, such as `240px` in the example below, then you can use both the `width` and `height` arguments to the render function:

0123456789

0123456789

```html
<div class="grid grid-cols-2" style="grid-auto-rows: 240px;">
  <div class="card" style="padding: 0;">
    ${resize((width, height) => Plot.barY([9, 4, 8, 1, 11, 3, 4, 2, 7, 5]).plot({width, height}))}
  </div>
  <div class="card" style="padding: 0;">
    ${resize((width, height) => Plot.barY([3, 4, 2, 7, 5, 9, 4, 8, 1, 11]).plot({width, height}))}
  </div>
</div>
```

If you are using `resize` with both `width` and `height` and see nothing rendered, it may be because your parent container does not have its own height specified. When both arguments are used, the rendered element is implicitly `position: absolute` to avoid affecting the size of its parent and causing a feedback loop.

## [display( _value_)](https://observablehq.com/framework/javascript\#display-value)

Displays the specified _value_ in the current context, returning _value_. If _value_ is a DOM element or node, it is inserted directly into the page. Otherwise, if the current context is a fenced code block, inspects the specified _value_; or, if the current context is an inline expression, coerces the specified _value_ to a string and displays it as text.

3

```js
display(1 + 2);
```

See [Explicit display](https://observablehq.com/framework/javascript#explicit-display) for more.

## [resize( _render_)](https://observablehq.com/framework/javascript\#resize-render)

Creates and returns a DIV element to contain responsive content; then, using a [`ResizeObserver`](https://developer.mozilla.org/en-US/docs/Web/API/ResizeObserver) to observe changes to the returned element’s size, calls the specified _render_ function with the new width and height whenever the size changes. The element returned by the _render_ function is inserted into the DIV element, replacing any previously-rendered content. This is useful for responsive charts.

I am 1888 pixels wide.

```js
resize((width) => `I am ${width} pixels wide.`)
```

If the _render_ function returns a promise, the promise is implicitly awaited. If the resulting value is null, the DIV element is cleared; otherwise, if the resulting value is not a DOM element, it is coerced to a string and displayed as text.

See [Responsive display](https://observablehq.com/framework/javascript#responsive-display) for more.

## [width](https://observablehq.com/framework/javascript\#width)

The current width of the main element in pixels as a reactive variable. A fenced code block or inline expression that references `width` will re-run whenever the width of the main element changes, such as when the window is resized; often used for responsive charts.

1888

```js
width
```

See [`Generators.width`](https://observablehq.com/framework/lib/generators#width-element) for implementation.

## [now](https://observablehq.com/framework/javascript\#now)

The current time in milliseconds since Unix epoch as a reactive variable. A fenced code block or inline expression that references `now` will run continuously; often used for simple animations.

1768013131651

```js
now
```

See [`Generators.now`](https://observablehq.com/framework/lib/generators#now) for implementation.

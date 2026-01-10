---
url: "https://observablehq.com/framework/inputs/button"
title: "Button input | Observable Framework"
---

1. [Options](https://observablehq.com/framework/inputs/button#options)

# [Button input](https://observablehq.com/framework/inputs/button\#button-input)

[API](https://github.com/observablehq/inputs/blob/main/README.md#button) · [Source](https://github.com/observablehq/inputs/blob/main/src/button.js) · The button input emits an _input_ event when you click it. Buttons may be used to trigger the evaluation of cells, say to restart an animation. For example, below is an animation that progressively hides a bar. Clicking the button will restart the animation.

Replay

```js
const replay = view(Inputs.button("Replay"));
```

The code block below references `replay`, so it will run automatically whenever the replay button is clicked.

```js
replay; // run this block when the button is clicked
const progress = (function* () {
  for (let i = canvas.width; i >= 0; --i) {
    context.clearRect(0, 0, canvas.width, canvas.height);
    context.fillRect(0, 0, i, canvas.height);
    yield canvas;
  }
})();
```

The `progress` top-level variable is declared as a [generator](https://observablehq.com/framework/reactivity#generators). This causes the Observable runtime to automatically advance the generator on each animation frame. If you prefer, you could write this animation using a standard `requestAnimationFrame` loop, but generators are nice because the animation will automatically be interrupted when the code is [invalidated](https://observablehq.com/framework/reactivity#invalidation).

You can also use buttons to count clicks. While the value of a button is often not needed, it defaults to zero and is incremented each time the button is clicked.

Click me

```js
const clicks = view(Inputs.button("Click me"));
```

0

```js
clicks
```

You have clicked 0 times.

```md
You have clicked ${clicks} times.
```

While buttons count clicks by default, you can change the behavior by specifying the _value_ and _reduce_ options: _value_ is the initial value, and _reduce_ is called whenever the button is clicked, being passed the current value and returning the new value. The value of the button below is the last time the button was clicked, or null if the button has not been clicked.

Update

```js
const time = view(Inputs.button("Update", {value: null, reduce: () => new Date}));
```

null

Note that even if the value of the button doesn’t change, it will still trigger any cells that reference the button’s value to run. (The Observable runtime listens for _input_ events on the view, and doesn’t check whether the value of the view has changed.)

For multiple buttons, pass an array of \[ _content_, _reduce_\] tuples. For example, to have a counter that can be incremented, decremented, and reset:

CounterIncrementDecrementReset

```js
const counter = view(Inputs.button([\
  ["Increment", value => value + 1],\
  ["Decrement", value => value - 1],\
  ["Reset", value => 0]\
], {value: 0, label: "Counter"}));
```

0

```js
counter
```

The first argument to `Inputs.button()` is the contents of the button. It’s not required, but is strongly encouraged.

≡

```js
const x = view(Inputs.button());
```

The contents of the button input can be an HTML element if desired, say for control over typography.

_Fancy_

```js
const y = view(Inputs.button(html`<i>Fancy</i>`));
```

Like other basic inputs, buttons can have an optional label, which can also be either a text string or an HTML element.

Continue?OK

```js
const confirm = view(Inputs.button("OK", {label: "Continue?"}));
```

You can change the rendered text in Markdown based on whether a button is clicked. Try clicking the `OK` button with the `Continue?` label.

```md
confirm ? "Confirmed!" : "Awaiting confirmation…"
```

Awaiting confirmation…

You can also use a button to copy something to the clipboard.

Copy to clipboard

```js
Inputs.button("Copy to clipboard", {value: null, reduce: () => navigator.clipboard.writeText(time)})
```

## [Options](https://observablehq.com/framework/inputs/button\#options)

**Inputs.button( _content_, _options_)**

The available button input options are:

- _label_ \- a label; either a string or an HTML element
- _required_ \- if true, the initial value defaults to undefined.
- _value_ \- the initial value; defaults to 0 or null if _required_ is false
- _reduce_ \- a function to update the value on click; by default returns _value_ \+ 1
- _width_ \- the width of the input (not including the label)
- _disabled_ \- whether input is disabled; defaults to false

---
url: "https://observablehq.com/@observablehq/plot-this-is-just-to-say"
title: "This is just to say"
---

# This is just to say

The [text](https://observablehq.com/plot/marks/text) mark respects multiline text.

```js
Plot.plot({
  height: 200,
  marks: [
    Plot.frame(),
    Plot.text([`This Is Just To Say
William Carlos Williams, 1934

I have eaten
the plums
that were in
the icebox

and which
you were probably
saving
for breakfast

Forgive me
they were delicious
so sweet
and so cold`], {frameAnchor: "middle"})
  ]
})
```

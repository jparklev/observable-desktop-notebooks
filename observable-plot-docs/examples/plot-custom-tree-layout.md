---
url: "https://observablehq.com/@observablehq/plot-custom-tree-layout"
title: "Indented tree diagram"
---

# Indented tree diagram

A [tree](https://observablehq.com/plot/marks/tree) with a custom layout.

```js
Plot.plot({
  axis: null,
  inset: 10,
  insetRight: 120,
  round: true,
  width: 200,
  height: 3600,
  marks: Plot.tree(flare, {
    path: "name",
    delimiter: ".",
    treeLayout: indent,
    strokeWidth: 1,
    curve: "step-before",
    textStroke: "none"
  })
})
```

```js
function indent() {
  return (root) => {
    root.eachBefore((node, i) => {
      node.y = node.depth;
      node.x = i;
    });
  };
}
```

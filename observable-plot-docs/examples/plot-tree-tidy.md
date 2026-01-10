---
url: "https://observablehq.com/@observablehq/plot-tree-tidy"
title: "Tree, tidy"
---

# Tree, tidy

# Tidy tree Plot’s [tree transform](https://observablehq.com/plot/marks/tree) implements the [Reingold–Tilford “tidy” algorithm](http://reingold.co/tidier-drawings.pdf) for constructing hierarchical node-link diagrams, improved to run in linear time by [Buchheim *et al.*](http://dirk.jivas.de/papers/buchheim02improving.pdf) Tidy trees are typically more compact than [cluster dendrograms](/@observablehq/plot-cluster-diagram), which place all leaves at the same level. See also the [radial variant](/@d3/radial-tidy-tree) (using D3).

```js
Plot.plot({
  axis: null,
  margin: 10,
  marginLeft: 40,
  marginRight: 160,
  width: 928,
  height: 1800,
  marks: [
    Plot.tree(flare, {path: "name", delimiter: "."})
  ]
})
```

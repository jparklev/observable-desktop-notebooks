---
url: "https://observablehq.com/plot/transforms/tree"
title: "Tree transform | Plot"
---

# Tree transform [^0.4.3](https://github.com/observablehq/plot/releases/tag/v0.4.3 "added in v0.4.3") [​](https://observablehq.com/plot/transforms/tree\#tree-transform)

The **tree transform** is rarely used directly; the two variants, [treeNode](https://observablehq.com/plot/transforms/tree#treeNode) and [treeLink](https://observablehq.com/plot/transforms/tree#treeLink), are typically used internally by the composite [tree mark](https://observablehq.com/plot/marks/tree). The tree transform arranges a tabular dataset into a hierarchy according to the given **path** channel, which is typically a slash-separated string; it then executes a tree layout algorithm to compute **x** and **y**; these channels can then be used to construct a node-link diagram.

As a contrived example, we can construct the equivalent of the tree mark using a [link](https://observablehq.com/plot/marks/link), [dot](https://observablehq.com/plot/marks/dot), and [text](https://observablehq.com/plot/marks/text), and the corresponding tree transforms.

ChaosErosErebusTartarusGaiaMountainsPontusUranus [Fork](https://observablehq.com/@observablehq/plot-tree-and-link "Open on Observable")

js

```
Plot.plot({
  axis: null,
  height: 100,
  margin: 20,
  marginRight: 120,
  marks: [\
    Plot.link(gods, Plot.treeLink()),\
    Plot.dot(gods, Plot.treeNode()),\
    Plot.text(gods, Plot.treeNode({text: "node:name", dx: 6}))\
  ]
})
```

Here `gods` is an array of slash-separated paths, similar to paths in a file system. Each path represents the hierarchical position of a node in the tree.

js

```
gods = [\
  "Chaos/Gaia/Mountains",\
  "Chaos/Gaia/Pontus",\
  "Chaos/Gaia/Uranus",\
  "Chaos/Eros",\
  "Chaos/Erebus",\
  "Chaos/Tartarus"\
]
```

TIP

Given a text file, you can use `text.split("\n")` to split the contents into multiple lines.

## Tree options [​](https://observablehq.com/plot/transforms/tree\#tree-options)

The following options control how the tabular data is organized into a hierarchy:

- **path** \- a column specifying each node’s hierarchy location; defaults to identity
- **delimiter** \- the path separator, a single character; defaults to forward slash (/)

The **path** column is typically slash-separated, as with UNIX-based file systems or URLs.

The following options control how the node-link diagram is laid out:

- **treeLayout** \- a tree layout algorithm; defaults to [d3.tree](https://d3js.org/d3-hierarchy/tree)
- **treeAnchor** \- a tree layout orientation, either _left_ or _right_; defaults to _left_
- **treeSort** \- a node comparator, or null to preserve input order
- **treeSeparation** \- a node separation function, or null for uniform separation

The default **treeLayout** implements the Reingold–Tilford “tidy” algorithm based on Buchheim _et al._’s linear time approach. Use [d3.cluster](https://d3js.org/d3-hierarchy/cluster) instead to align leaf nodes; see also the [cluster mark](https://observablehq.com/plot/marks/tree#cluster).

If **treeAnchor** is _left_, the root of the tree will be aligned with the left side of the frame; if **treeAnchor** is _right_, the root of the tree will be aligned with the right side of the frame; use the **insetLeft** and **insetRight** [scale options](https://observablehq.com/plot/features/scales) if horizontal padding is desired, say to make room for labels.

If the **treeSort** option is not null, it is typically a function that is passed two nodes in the hierarchy and compares them, similar to [_array_.sort](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/sort); see [d3-hierarchy’s _node_.sort](https://d3js.org/d3-hierarchy/hierarchy#node_sort) for more. The **treeSort** option can also be specified as a string, in which case it refers either to a named column in data, or if it starts with “node:”, a node value.

If the **treeSeparation** is not null, it is a function that is passed two nodes in the hierarchy and returns the desired (relative) amount of separation; see [d3-hierarchy’s _tree_.separation](https://d3js.org/d3-hierarchy/tree#tree_separation) for more. By default, non-siblings are at least twice as far apart as siblings.

## treeNode( _options_) [​](https://observablehq.com/plot/transforms/tree\#treeNode)

Populates **x** and **y** with the positions for each node in the tree. The default **frameAnchor** inherits the **treeAnchor**. This transform is often used with the [dot](https://observablehq.com/plot/marks/dot) or [text](https://observablehq.com/plot/marks/text) mark.

The treeNode transform will derive output columns for any _options_ that have one of the following named node values:

- _node:name_ \- the node’s name (the last part of its path)
- _node:path_ \- the node’s full, normalized, slash-separated path
- _node:internal_ \- true if the node is internal, or false for leaves
- _node:external_ \- true if the node is a leaf, or false for internal nodes
- _node:depth_ \- the distance from the node to the root
- _node:height_ \- the distance from the node to its deepest descendant

In addition, if any option value is specified as an object with a **node** method, a derived output column will be generated by invoking the **node** method for each node in the tree.

## treeLink( _options_) [​](https://observablehq.com/plot/transforms/tree\#treeLink)

Populates **x1**, **y1**, **x2**, and **y2** with the positions for each link in the tree, where **x1** & **y1** represents the position of the parent node and **x2** & **y2** the position of the child node. The default **curve** is _bump-x_, the default **stroke** is #555, the default **strokeWidth** is 1.5, and the default **strokeOpacity** is 0.5. This transform is often used with the [link](https://observablehq.com/plot/marks/link) or [arrow](https://observablehq.com/plot/marks/arrow) mark.

The treeLink transform will likewise derive output columns for any _options_ that have one of the following named link values:

- _node:name_ \- the child node’s name (the last part of its path)
- _node:path_ \- the child node’s full, normalized, slash-separated path
- _node:internal_ \- true if the child node is internal, or false for leaves
- _node:external_ \- true if the child node is a leaf, or false for internal nodes
- _node:depth_ \- the distance from the child node to the root
- _node:height_ \- the distance from the child node to its deepest descendant
- _parent:name_ \- the parent node’s name (the last part of its path)
- _parent:path_ \- the parent node’s full, normalized, slash-separated path
- _parent:depth_ \- the distance from the parent node to the root
- _parent:height_ \- the distance from the parent node to its deepest descendant

In addition, if any option value is specified as an object with a **node** method, a derived output column will be generated by invoking the **node** method for each child node in the tree; likewise if any option value is specified as an object with a **link** method, a derived output column will be generated by invoking the **link** method for each link in the tree, being passed two node arguments, the child and the parent.

Pager

[Previous pageStack](https://observablehq.com/plot/transforms/stack)

[Next pageWindow](https://observablehq.com/plot/transforms/window)

[Home](https://observablehq.com/ "Home")

Resources

- [Forum](https://talk.observablehq.com/)
- [Slack](https://observablehq.com/slack/join)
- [Releases](https://github.com/observablehq/plot/releases)

Observable

- [Product](https://observablehq.com/product)
- [Plot](https://observablehq.com/plot)
- [Integrations](https://observablehq.com/data-integrations)
- [Pricing](https://observablehq.com/pricing)

---
url: "https://observablehq.com/framework/lib/lodash"
title: "Lodash | Observable Framework"
---

# [Lodash](https://observablehq.com/framework/lib/lodash\#lodash)

[Lodash](https://lodash.com/) is a “utility library delivering modularity, performance & extras.” It is available by default in Markdown as `_` but you can import it explicitly like so:

```js
import _ from "npm:lodash";
```

Object {a: 1, b: 2}

```js
_.defaults({a: 1}, {a: 3, b: 2})
```

Array(2) \[Array(2), Array(2)\]

```js
_.partition([1, 2, 3, 4], (n) => n % 2)
```

---
url: "https://observablehq.com/framework/lib/vega-lite"
title: "Vega-Lite | Observable Framework"
---

# [Vega-Lite](https://observablehq.com/framework/lib/vega-lite\#vega-lite)

[Vega-Lite](https://vega.github.io/vega-lite/) is a “high-level grammar of interactive graphics” with “concise, declarative syntax to create an expressive range of visualizations for data analysis and presentation.” It is an alternative to [Observable Plot](https://observablehq.com/framework/lib/plot). Vega-Lite is available by default in Markdown as `vl`, but you can import it explicitly as:

```js
import * as vega from "npm:vega";
import * as vegaLite from "npm:vega-lite";
import * as vegaLiteApi from "npm:vega-lite-api";

const vl = vegaLiteApi.register(vega, vegaLite);
```

You can use the [Vega-Lite JavaScript API](https://vega.github.io/vega-lite-api/) to construct a chart:

```js
vl.markBar()
  .data(alphabet)
  .encode(vl.x().fieldQ("frequency"), vl.y().fieldN("letter"))
  .width(640)
  .render()
```

Or you can use a [Vega-Lite JSON view specification](https://vega.github.io/vega-lite/docs/spec.html):

```js
vl.render({
  spec: {
    width: 640,
    height: 400,
    data: {url: await FileAttachment("gistemp.csv").url(), format: {type: "csv"}},
    mark: "point",
    encoding: {
      x: {type: "temporal", field: "Date"},
      y: {type: "quantitative", field: "Anomaly"},
      color: {type: "quantitative", field: "Anomaly", scale: {range: "diverging", reverse: true}}
    }
  }
})
```

When loading data from a file as above, use [`FileAttachment`](https://observablehq.com/framework/files) so that referenced files are included on [build](https://observablehq.com/framework/files#static-analysis).

---
url: "https://observablehq.com/framework/lib/echarts"
title: "Apache ECharts  | Observable Framework"
---

# [Apache ECharts](https://observablehq.com/framework/lib/echarts\#apache-e-charts) [Added in v1.1.0](https://github.com/observablehq/framework/releases/tag/v1.1.0 "Added in v1.1.0")

[Apache ECharts](https://echarts.apache.org/), an open-source JavaScript visualization library, is available by default as `echarts` in Markdown. You can also import it explicitly like so:

```js
import * as echarts from "npm:echarts";
```

To use ECharts, declare a container element with the desired dimensions, [display it](https://observablehq.com/framework/javascript#explicit-display), and then call `echarts.init`.

```js
const myChart = echarts.init(display(html`<div style="width: 600px; height:400px;"></div>`));

myChart.setOption({
  title: {
    text: "ECharts getting started example"
  },
  tooltip: {},
  xAxis: {
    data: ["shirt", "cardigan", "chiffon", "pants", "heels", "socks"]
  },
  yAxis: {},
  series: [\
    {\
      name: "sales",\
      type: "bar",\
      data: [5, 20, 36, 10, 10, 20]\
    }\
  ]
});
```

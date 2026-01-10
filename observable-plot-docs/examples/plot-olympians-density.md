---
url: "https://observablehq.com/@observablehq/plot-olympians-density"
title: "Olympians density"
---

# Olympians density

Use the [density](https://observablehq.com/plot/marks/density) mark to show the spread of two classes of Olympic athletes. Data: [Matt Riggott/IOC](https://www.flother.is/2017/olympic-games-data/)

```js
Plot.density(olympians, {x: "weight", y: "height", stroke: "sex"}).plot()
```

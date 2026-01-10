---
url: "https://observablehq.com/@observablehq/plot-floor-plan"
title: "Floor plan"
---

# Floor plan

The [geo](https://observablehq.com/plot/marks/geo) mark can display large scale maps such as this floor plan of the Westport House in Dundee, Ireland—using the _identity_ [projection](https://observablehq.com/plot/features/projections).

```js
Plot.geo(westport).plot({projection: {type: "identity", domain: westport}})
```

```js
westport = FileAttachment("westport-house.json").json()
```

---
title: Notebook Viewer Demo
theme: parchment
---

<style>
:root { --max-width: 100%; }
body { padding: 0; }
</style>

# Notebook Viewer Demo

This notebook is a small, self-contained Observable Framework page meant to validate the Tauri viewer:

- interactive inputs via `view(...)`
- Plot rendering
- JS bridge (`/eval`, `/cells`, `/cell/{name}`)
- Element screenshots (`/screenshot/element`)

## Controls

```js echo
const n = view(Inputs.range([10, 200], { value: 80, step: 1, label: "Number of points" }))
```

```js echo
const noise = view(Inputs.range([0, 2], { value: 0.6, step: 0.1, label: "Noise" }))
```

```js
const points = Array.from({length: n}, (_, i) => {
  const x = i / (n - 1);
  const y = Math.sin(x * Math.PI * 2) + d3.randomNormal(0, noise)();
  return {x, y};
})
```

## Plot

```js
Object.assign(Plot.plot({
  height: 360,
  grid: true,
  marks: [
    Plot.line(points, {x: "x", y: "y", stroke: "steelblue"}),
    Plot.ruleY([0], {stroke: "#999"})
  ]
}), {id: "chart-sine"})
```

## Values Exposed to the Viewer

The viewer lists cells and reads values via `expose()` from `bridge.js`. This merges values into `window.__exposed` and dispatches a custom event for change notification.

```js
import { expose } from "./bridge.js";

expose({
  n,
  noise,
  pointCount: points.length,
  meanY: d3.mean(points, d => d.y)
});
```

## Calibration Element

This is useful for verifying element screenshots.

```js
htl.html`<div id="calibration" style="width: 100px; height: 100px; background: #ff2d2d; border-radius: 8px;"></div>`
```

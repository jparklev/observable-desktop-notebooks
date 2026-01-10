---
title: The Art of Throwing Darts
theme: parchment
---

# The Art of Throwing Darts
## Monte Carlo Simulation for the Curious

*"What if you could solve math problems by throwing darts at a wall?"*

This notebook explores **Monte Carlo simulation** — the surprising idea that randomness can solve deterministic problems. We'll estimate π by throwing virtual darts, watch chaos converge to order, and discover why doubling your precision costs four times the effort.

---

# I. The Dartboard

Imagine a square dartboard with a circle inscribed inside it. If you throw darts randomly at the board, some land inside the circle, some outside.

The ratio of darts inside the circle to total darts approximates the ratio of areas:

```tex
\frac{\text{darts in circle}}{\text{total darts}} \approx \frac{\pi r^2}{(2r)^2} = \frac{\pi}{4}
```

Therefore:

```tex
\pi \approx 4 \times \frac{\text{darts in circle}}{\text{total darts}}
```

Let's throw some darts.

```js echo
const N = view(Inputs.range([10, 10000], {value: 500, step: 10, label: "Number of darts (N)"}))
```

```js
// Seeded random for reproducibility
function mulberry32(seed) {
  return function() {
    let t = seed += 0x6D2B79F5;
    t = Math.imul(t ^ t >>> 15, t | 1);
    t ^= t + Math.imul(t ^ t >>> 7, t | 61);
    return ((t ^ t >>> 14) >>> 0) / 4294967296;
  }
}

const random = mulberry32(42);

// Generate dart positions
const darts = Array.from({length: N}, () => {
  const x = random();
  const y = random();
  const inside = (x - 0.5) ** 2 + (y - 0.5) ** 2 <= 0.25;
  return {x, y, inside};
});

const insideCount = darts.filter(d => d.inside).length;
const piEstimate = 4 * insideCount / N;
```

**Estimate:** π ≈ ${piEstimate.toFixed(6)} (true value: ${Math.PI.toFixed(6)})

**Error:** ${Math.abs(piEstimate - Math.PI).toFixed(6)} (${(Math.abs(piEstimate - Math.PI) / Math.PI * 100).toFixed(2)}%)

```js
{
  // Draw the circle boundary
  const circlePoints = d3.range(0, 2 * Math.PI + 0.1, 0.1).map(t => ({
    x: 0.5 + 0.5 * Math.cos(t),
    y: 0.5 + 0.5 * Math.sin(t)
  }));

  display(Plot.plot({
    width: 500,
    height: 500,
    aspectRatio: 1,
    x: {domain: [0, 1], label: null, ticks: []},
    y: {domain: [0, 1], label: null, ticks: []},
    color: {
      domain: [true, false],
      range: ["#4ecdc4", "#ff6b6b"],
      legend: true
    },
    marks: [
      Plot.frame({stroke: "#ccc"}),
      Plot.line(circlePoints, {x: "x", y: "y", stroke: "#666", strokeWidth: 2}),
      Plot.dot(darts, {x: "x", y: "y", fill: "inside", r: Math.max(1.5, 400 / Math.sqrt(N)), opacity: 0.6})
    ]
  }));
}
```

Drag the slider above. With just 100 darts, the estimate wobbles wildly. With 10,000, it settles near π. This is the **Law of Large Numbers** in action.

---

# II. Watching Convergence

Let's watch how the estimate evolves as we throw more darts. Each point shows the running estimate of π after that many throws.

```js echo
const showTheory = view(Inputs.toggle({label: "Show theoretical bounds", value: true}))
```

```js
{
  // Calculate running estimate at each step
  const steps = [];
  let hits = 0;
  const stepRandom = mulberry32(42);

  for (let i = 1; i <= N; i++) {
    const x = stepRandom();
    const y = stepRandom();
    if ((x - 0.5) ** 2 + (y - 0.5) ** 2 <= 0.25) hits++;

    const estimate = 4 * hits / i;

    // Theoretical 95% CI: ±1.96 * σ / √n
    // For Bernoulli with p ≈ π/4, σ ≈ √(p(1-p)) ≈ 0.43
    const sigma = 0.43;
    const ci = 1.96 * sigma * 4 / Math.sqrt(i);

    steps.push({
      n: i,
      estimate,
      ciUpper: Math.PI + ci,
      ciLower: Math.PI - ci
    });
  }

  const marks = [
    Plot.ruleY([Math.PI], {stroke: "#4ecdc4", strokeWidth: 2, strokeDasharray: "5,5"}),
    Plot.line(steps, {x: "n", y: "estimate", stroke: "#333", strokeWidth: 1.5})
  ];

  if (showTheory) {
    marks.unshift(
      Plot.areaY(steps, {x: "n", y1: "ciLower", y2: "ciUpper", fill: "#4ecdc4", fillOpacity: 0.15})
    );
  }

  marks.push(
    Plot.text([{x: N, y: Math.PI}], {x: "x", y: "y", text: ["π"], dx: 15, fill: "#4ecdc4", fontWeight: "bold"})
  );

  display(Plot.plot({
    width: 800,
    height: 400,
    x: {label: "Number of darts (N)", type: "log"},
    y: {label: "π estimate", domain: [2, 4.5], grid: true},
    marks
  }));
}
```

The **teal dashed line** is the true value of π. The black line is our running estimate. Notice how it starts wild and gradually settles.

The **shaded region** shows the theoretical 95% confidence interval — where we expect 95% of estimates to fall. As N grows, this funnel narrows. The estimate is **trapped** into convergence.

---

# III. Multiple Universes

But wait — that was just *one* sequence of random throws. What if we ran the experiment again with different random numbers?

```js echo
const numPaths = view(Inputs.range([1, 20], {value: 5, step: 1, label: "Number of parallel runs"}))
```

```js
{
  // Generate multiple convergence paths with different seeds
  const allPaths = [];

  for (let pathIdx = 0; pathIdx < numPaths; pathIdx++) {
    const pathRandom = mulberry32(pathIdx * 1000 + 1);
    let hits = 0;

    for (let i = 1; i <= N; i++) {
      const x = pathRandom();
      const y = pathRandom();
      if ((x - 0.5) ** 2 + (y - 0.5) ** 2 <= 0.25) hits++;

      if (i % Math.max(1, Math.floor(N / 200)) === 0 || i === N) {
        allPaths.push({
          n: i,
          estimate: 4 * hits / i,
          path: pathIdx
        });
      }
    }
  }

  display(Plot.plot({
    width: 800,
    height: 400,
    x: {label: "Number of darts (N)", type: "log"},
    y: {label: "π estimate", domain: [2, 4.5], grid: true},
    color: {scheme: "tableau10"},
    marks: [
      Plot.ruleY([Math.PI], {stroke: "#4ecdc4", strokeWidth: 2, strokeDasharray: "5,5"}),
      Plot.line(allPaths, {x: "n", y: "estimate", z: "path", stroke: "path", strokeWidth: 1.2, opacity: 0.7}),
      Plot.text([{x: N, y: Math.PI}], {x: "x", y: "y", text: ["π"], dx: 15, fill: "#4ecdc4", fontWeight: "bold"})
    ]
  }));
}
```

Each colored line is a different "universe" — a different sequence of random throws. They all start chaotic, wandering in different directions. But they all **converge to the same truth**.

This is the power of Monte Carlo: individual randomness averages out into deterministic results.

---

# IV. The √N Tax

Here's the catch: precision is expensive.

```tex
\text{Standard Error} = \frac{\sigma}{\sqrt{N}}
```

To halve your error, you need **four times** the samples. To get 10x more precise, you need **100x** the samples.

```js
{
  // Calculate error at various N values
  const sampleSizes = [10, 30, 100, 300, 1000, 3000, 10000];
  const trials = 50;

  const errorData = [];

  for (const n of sampleSizes) {
    const errors = [];

    for (let t = 0; t < trials; t++) {
      const trialRandom = mulberry32(t * 10000 + n);
      let hits = 0;

      for (let i = 0; i < n; i++) {
        const x = trialRandom();
        const y = trialRandom();
        if ((x - 0.5) ** 2 + (y - 0.5) ** 2 <= 0.25) hits++;
      }

      const estimate = 4 * hits / n;
      errors.push(Math.abs(estimate - Math.PI));
    }

    const meanError = d3.mean(errors);
    const theoreticalError = 1.7 / Math.sqrt(n); // σ ≈ 0.43 * 4 ≈ 1.7

    errorData.push({n, meanError, theoreticalError, type: "Observed"});
  }

  display(Plot.plot({
    width: 700,
    height: 400,
    x: {type: "log", label: "Sample size (N)", grid: true},
    y: {type: "log", label: "Mean absolute error", grid: true, domain: [0.01, 1]},
    marks: [
      Plot.line(errorData, {x: "n", y: "theoreticalError", stroke: "#4ecdc4", strokeWidth: 2, strokeDasharray: "5,5"}),
      Plot.dot(errorData, {x: "n", y: "meanError", fill: "#333", r: 6}),
      Plot.text([{x: 100, y: 0.3}], {x: "x", y: "y", text: ["1/√N"], fill: "#4ecdc4", fontWeight: "bold", fontSize: 14})
    ]
  }));
}
```

On this log-log plot, the theoretical error line (teal dashed) has a slope of -0.5, meaning error ∝ 1/√N.

The dots are our observed errors (averaged over 50 trials at each N). They follow the theory.

| N | Expected Error | Cost to reach |
|---|----------------|---------------|
| 100 | ~0.17 | 1x |
| 10,000 | ~0.017 | 100x |
| 1,000,000 | ~0.0017 | 10,000x |

Monte Carlo is powerful but inefficient. For high precision, you pay dearly.

---

# V. Beyond the Dartboard

We estimated π with darts. But Monte Carlo solves much harder problems:

- **Integration** — finding areas under complex curves
- **Optimization** — searching high-dimensional spaces
- **Risk analysis** — simulating thousands of possible futures
- **Physics** — modeling particle interactions

The Kelly Criterion notebook uses Monte Carlo to simulate investment trajectories. Each line in those plots is one possible future, shaped by randomness but bounded by mathematics.

The insight is always the same: **randomness reveals truth when you have enough of it**.

---

## Key Takeaways

1. **Random sampling solves deterministic problems** — counterintuitive but powerful
2. **The Law of Large Numbers** — chaos converges to order
3. **The √N tax** — precision is expensive (4x samples for 2x precision)
4. **Multiple runs show robustness** — different random seeds, same answer

---

```js
import { expose } from "./bridge.js";

expose({
  N,
  piEstimate,
  error: Math.abs(piEstimate - Math.PI),
  numPaths,
  showTheory
});
```

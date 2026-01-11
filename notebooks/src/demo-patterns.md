---
title: Educational Patterns Demo
theme: parchment
---

# Educational Patterns Demo

This notebook demonstrates the interactive educational patterns and testing utilities for building rigorous, engaging notebooks.

**What you'll see:**
1. Inline testing with `testing.js`
2. Interactive quizzes with `quiz.js`
3. Prediction exercises ("guess before reveal")
4. Goal-seeking exploration
5. Data manipulation with DuckDB & Arquero

---

## 1. Testing Utilities

Every quantitative notebook should verify its calculations. Here's how to use `testing.js`:

```js
import { createSuite } from "./testing.js";

// Define functions to test
function kellyBet(p, b) {
  const q = 1 - p;
  return (b * p - q) / b;
}

function recoveryGain(loss) {
  // What gain is needed to recover from a loss?
  return 1 / (1 - loss) - 1;
}

// Create a test suite
const { test, view: kellyView, stats } = createSuite("KellyMath");

// Run tests
test("Kelly: even money, 60% win rate", (expect) => {
  expect(kellyBet(0.6, 1)).toBeCloseTo(0.20, 2);
});

test("Kelly: 2:1 odds, 55% win rate", (expect) => {
  expect(kellyBet(0.55, 2)).toBeCloseTo(0.325, 2);
});

test("Recovery: 50% loss needs 100% gain", (expect) => {
  expect(recoveryGain(0.5)).toBeCloseTo(1.0, 2);
});

test("Recovery: 20% loss needs 25% gain", (expect) => {
  expect(recoveryGain(0.2)).toBeCloseTo(0.25, 2);
});

test("Kelly edge case: no edge = no bet", (expect) => {
  expect(kellyBet(0.5, 1)).toBeCloseTo(0, 2);
});

// Display test results
display(kellyView());
```

**Test Results:** (rendered above)

The test results are automatically exposed to the bridge for `./viewer.py verify` to check.

---

## 2. Interactive Quizzes

Use `quiz.js` for knowledge check questions:

```js
import { Quiz } from "./quiz.js";
```

```js
display(Quiz({
  question: "If an asset falls 50%, what percentage gain is needed to return to the original value?",
  options: ["25%", "50%", "75%", "100%"],
  correctIndex: 3,
  explanation: "A 50% loss turns $100 into $50. To get back to $100, you need to gain $50, which is 100% of $50. This asymmetry is why position sizing matters—losses hurt more than gains help."
}));
```

```js
display(Quiz({
  question: "According to the Kelly Criterion, what happens if you bet MORE than 2x the optimal amount?",
  options: [
    "You grow faster but with more volatility",
    "You have negative expected growth (eventual ruin)",
    "Your returns stay the same but risk increases",
    "Nothing changes significantly"
  ],
  correctIndex: 1,
  explanation: "Above 2x Kelly, the expected geometric growth rate becomes negative. Even with a positive edge, overbetting guarantees eventual ruin. This is why practitioners use fractional Kelly (typically 50% or less)."
}));
```

---

## 3. Prediction Exercise ("Guess Before Reveal")

This pattern creates a "curiosity gap" by forcing commitment before showing the answer:

```js echo
const userGuess = view(Inputs.range([0, 200], {
  label: "Your guess: If a stock falls 50%, what % gain is needed to recover?",
  value: 50,
  step: 5
}));
```

```js echo
const revealAnswer = view(Inputs.button("Check My Answer"))
```

```js
{
  if (revealAnswer) {
    const correct = 100;
    const isClose = Math.abs(userGuess - correct) <= 10;

    display(html`
      <div class="card" style="border-left: 4px solid ${isClose ? "#2d724f" : "#b3312c"}; margin: 1rem 0;">
        <h3 style="color: ${isClose ? "#2d724f" : "#b3312c"}; margin-top: 0;">
          ${isClose ? "Close!" : "Not quite."}
        </h3>
        <p>
          You guessed <strong>${userGuess}%</strong>. The answer is <strong>100%</strong>.
        </p>
        <p>
          <strong>Why?</strong> A 50% loss turns $100 into $50. To get back to $100,
          you need +$50 on a $50 base = <strong>100%</strong> gain.
        </p>
        <p style="color: #666; font-style: italic;">
          This asymmetry is called "volatility drag" and is why losses hurt more than equivalent gains help.
        </p>
      </div>
    `);

    // Visual proof
    display(Plot.plot({
      title: "The Recovery Trap",
      subtitle: "Required gain grows exponentially as losses deepen",
      width: 700,
      height: 350,
      x: {label: "Loss %", domain: [0, 90]},
      y: {label: "Required Gain to Recover %", domain: [0, 1000], grid: true},
      marks: [
        Plot.areaY(d3.range(0, 91, 1).map(loss => ({
          loss,
          gain: (1 / (1 - loss/100) - 1) * 100
        })), {x: "loss", y: "gain", fill: "#b3312c", fillOpacity: 0.2}),
        Plot.line(d3.range(0, 91, 1).map(loss => ({
          loss,
          gain: (1 / (1 - loss/100) - 1) * 100
        })), {x: "loss", y: "gain", stroke: "#b3312c", strokeWidth: 2}),
        Plot.dot([{loss: 50, gain: 100}], {x: "loss", y: "gain", r: 8, fill: "#0f5499"}),
        Plot.text([{loss: 50, gain: 100}], {x: "loss", y: "gain", text: ["50% loss → 100% to recover"], dy: -15, fontWeight: "bold"}),
        Plot.ruleY([100], {stroke: "#666", strokeDasharray: "4,4"}),
        Plot.text([{loss: 80, gain: 100}], {x: "loss", y: "gain", text: ["Break-even line"], dy: 10, fill: "#666"})
      ]
    }));
  }
}
```

---

## 4. Goal-Seeking Exploration

Instead of passive slider exploration, give the user a specific challenge:

<div class="card" style="background: #faf6f3; padding: 1.5rem; margin: 1.5rem 0;">

### Challenge: Find the Optimal Kelly Bet

You have a coin that lands heads **60% of the time**. Each flip, you can bet any fraction of your bankroll. Heads = you win what you bet. Tails = you lose your bet.

**Your goal:** Find the bet size that **maximizes long-term growth**.

</div>

```js echo
const betSize = view(Inputs.range([0, 1], {
  label: "Bet Size (fraction of bankroll)",
  value: 0.1,
  step: 0.02
}));
```

```js
{
  const p = 0.6;  // Win probability
  const b = 1;    // Even money
  const optimalF = p - (1 - p);  // 0.20

  // Growth rate formula: E[log(wealth)] = p*log(1+b*f) + q*log(1-f)
  const growth = (f) => {
    if (f <= 0) return 0;
    if (f >= 1) return -Infinity;
    return p * Math.log(1 + b * f) + (1 - p) * Math.log(1 - f);
  };

  const currentGrowth = growth(betSize);
  const maxGrowth = growth(optimalF);
  const efficiency = maxGrowth > 0 ? (currentGrowth / maxGrowth * 100) : 0;

  // Determine zone
  const inRuinZone = betSize > 2 * optimalF;
  const isOptimal = Math.abs(betSize - optimalF) < 0.02;

  const color = inRuinZone ? "#b3312c" : isOptimal ? "#2d724f" : "#0f5499";
  const status = inRuinZone ? "RUIN ZONE" : isOptimal ? "OPTIMAL!" : currentGrowth > 0 ? "Positive Growth" : "Zero Growth";

  display(html`
    <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 1rem; margin: 1rem 0;">
      <div class="card" style="text-align: center; border-top: 4px solid ${color};">
        <div style="font-size: 2rem; font-weight: bold; color: ${color};">${(efficiency).toFixed(0)}%</div>
        <div>Efficiency</div>
      </div>
      <div class="card" style="text-align: center;">
        <div style="font-size: 2rem; font-weight: bold;">${(currentGrowth * 100).toFixed(2)}%</div>
        <div>Growth Rate</div>
      </div>
      <div class="card" style="text-align: center; border-top: 4px solid ${color};">
        <div style="font-size: 1.5rem; font-weight: bold; color: ${color};">${status}</div>
        <div>Status</div>
      </div>
    </div>
  `);

  // Growth curve
  const curveData = d3.range(0, 0.99, 0.01).map(f => ({
    f,
    growth: growth(f) * 100,
    zone: f <= optimalF ? "optimal" : f <= 2 * optimalF ? "inefficient" : "ruin"
  }));

  display(Plot.plot({
    title: "Growth Rate vs. Bet Size",
    subtitle: `Optimal Kelly = ${(optimalF * 100).toFixed(0)}% | Ruin threshold = ${(2 * optimalF * 100).toFixed(0)}%`,
    width: 700,
    height: 400,
    x: {label: "Bet Size (fraction)", tickFormat: ".0%"},
    y: {label: "Expected Growth Rate per Bet (%)", grid: true, tickFormat: "+.1f"},
    marks: [
      // Ruin zone shading
      Plot.areaY(curveData.filter(d => d.f > 2 * optimalF), {
        x: "f", y1: -10, y2: "growth", fill: "#b3312c", fillOpacity: 0.2
      }),
      // Growth curve
      Plot.line(curveData, {x: "f", y: "growth", stroke: "#666", strokeWidth: 2}),
      // Zero line
      Plot.ruleY([0], {stroke: "#999", strokeDasharray: "4,4"}),
      // Ruin threshold
      Plot.ruleX([2 * optimalF], {stroke: "#b3312c", strokeWidth: 2, strokeDasharray: "4,4"}),
      // Optimal point
      Plot.dot([{f: optimalF, growth: maxGrowth * 100}], {x: "f", y: "growth", r: 8, fill: "#2d724f", stroke: "white"}),
      Plot.text([{f: optimalF, growth: maxGrowth * 100}], {x: "f", y: "growth", text: ["Optimal"], dy: -15, fill: "#2d724f", fontWeight: "bold"}),
      // Current position
      Plot.dot([{f: betSize, growth: currentGrowth * 100}], {x: "f", y: "growth", r: 10, fill: color, stroke: "white", strokeWidth: 2}),
      Plot.text([{f: betSize, growth: currentGrowth * 100}], {x: "f", y: "growth", text: ["You"], dy: 20, fill: color, fontWeight: "bold"}),
      // Ruin label
      Plot.text([{f: 0.55, growth: -3}], {x: "f", y: "growth", text: ["RUIN ZONE"], fill: "#b3312c", fontWeight: "bold"})
    ]
  }));
}
```

**Hint:** The Kelly formula says bet `f* = p - q` where `p` is win probability and `q = 1 - p`. With `p = 0.6`, what's the optimal bet?

---

## 5. Data Manipulation with DuckDB

DuckDB brings SQL to the browser. Here's a demo with synthetic trading data:

```js
// Generate synthetic trade data
const trades = d3.range(500).map((_, i) => ({
  id: i + 1,
  date: d3.timeDay.offset(new Date("2024-01-01"), Math.floor(i / 5)),
  symbol: ["AAPL", "GOOGL", "MSFT", "AMZN", "META"][i % 5],
  side: Math.random() > 0.5 ? "BUY" : "SELL",
  quantity: Math.floor(Math.random() * 100) + 10,
  price: 100 + Math.random() * 50,
  pnl: (Math.random() - 0.45) * 1000  // Slight positive edge
}));
```

```js
// Create DuckDB client and run SQL
const db = await DuckDBClient.of({ trades });

const symbolStats = await db.query(`
  SELECT
    symbol,
    COUNT(*) as trade_count,
    ROUND(SUM(pnl), 2) as total_pnl,
    ROUND(AVG(pnl), 2) as avg_pnl,
    ROUND(SUM(CASE WHEN pnl > 0 THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 1) as win_rate
  FROM trades
  GROUP BY symbol
  ORDER BY total_pnl DESC
`);
```

**SQL Aggregation Results:**

```js
display(Inputs.table(symbolStats, {
  format: {
    total_pnl: d => `$${d.toLocaleString()}`,
    avg_pnl: d => `$${d.toLocaleString()}`,
    win_rate: d => `${d}%`
  }
}))
```

**Pivot-Style Analysis with Arquero:**

```js
// Use Arquero for pivot-table style operations
const tradesAq = aq.from(trades);

const pivotData = tradesAq
  .groupby("symbol", "side")
  .rollup({
    count: d => aq.op.count(),
    total_pnl: d => aq.op.sum(d.pnl),
    avg_price: d => aq.op.mean(d.price)
  })
  .orderby("symbol", "side");

display(Inputs.table(pivotData.objects(), {
  columns: ["symbol", "side", "count", "total_pnl", "avg_price"],
  format: {
    total_pnl: d => `$${d.toFixed(2)}`,
    avg_price: d => `$${d.toFixed(2)}`
  }
}));
```

---

## 6. Combined Example: Trade Analysis with Testing

Let's analyze our trading data with verified calculations:

```js
import { createSuite as createSuite2 } from "./testing.js";

// Calculate statistics
const totalPnl = d3.sum(trades, d => d.pnl);
const winCount = trades.filter(d => d.pnl > 0).length;
const winRate = winCount / trades.length;
const avgWin = d3.mean(trades.filter(d => d.pnl > 0), d => d.pnl);
const avgLoss = d3.mean(trades.filter(d => d.pnl <= 0), d => d.pnl);
const profitFactor = Math.abs(d3.sum(trades.filter(d => d.pnl > 0), d => d.pnl) / d3.sum(trades.filter(d => d.pnl <= 0), d => d.pnl));

// Test our calculations
const { test: test2, view: view2, stats: stats2 } = createSuite2("TradeAnalysis");

test2("Win rate should be between 0 and 1", (expect) => {
  expect(winRate).toBeInRange(0, 1);
});

test2("Profit factor calculation is positive", (expect) => {
  expect(profitFactor).toBeGreaterThan(0);
});

test2("Trade count matches", (expect) => {
  expect(trades.length).toBe(500);
});

test2("Win + Loss = Total", (expect) => {
  const lossCount = trades.filter(d => d.pnl <= 0).length;
  expect(winCount + lossCount).toBe(500);
});
```

<div class="grid grid-cols-4">
  <div class="card">
    <h3>Total P&L</h3>
    <div style="font-size: 2rem; font-weight: bold; color: ${totalPnl >= 0 ? "#2d724f" : "#b3312c"};">
      ${totalPnl >= 0 ? "+" : ""}$${totalPnl.toFixed(2)}
    </div>
  </div>
  <div class="card">
    <h3>Win Rate</h3>
    <div style="font-size: 2rem; font-weight: bold;">${(winRate * 100).toFixed(1)}%</div>
  </div>
  <div class="card">
    <h3>Profit Factor</h3>
    <div style="font-size: 2rem; font-weight: bold;">${profitFactor.toFixed(2)}</div>
  </div>
  <div class="card">
    <h3>Avg Win / Avg Loss</h3>
    <div style="font-size: 1.2rem;">$${avgWin?.toFixed(0) || "N/A"} / $${avgLoss?.toFixed(0) || "N/A"}</div>
  </div>
</div>

```js
display(view2())
```

---

## Summary

This notebook demonstrated:

| Pattern | Use Case |
|---------|----------|
| `testing.js` | Verify calculations automatically |
| `quiz.js` | Knowledge check questions |
| Prediction exercises | Build curiosity and challenge assumptions |
| Goal-seeking | Active learning through exploration |
| DuckDB SQL | Fast data aggregation |
| Arquero | Pivot-table style transforms |

These patterns help create **rigorous, engaging** educational content that catches bugs early and builds genuine understanding.

---

```js
import { expose } from "./bridge.js";

// Expose test results and key metrics for verification
expose({
  kellyTests: stats(),
  tradeTests: stats2(),
  totalPnl,
  winRate,
  profitFactor,
  tradeCount: trades.length
});
```

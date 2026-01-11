---
title: Hyperliquid Usage Patterns
theme: parchment
---

# Hyperliquid Usage Patterns
## Real-Time DEX Analytics

Hyperliquid is a high-performance perpetuals DEX built on its own L1. This notebook fetches live data from the Hyperliquid API to analyze trading activity across markets.

```js
// Fetch perpetual market data from Hyperliquid API
const perpData = await fetch("https://api.hyperliquid.xyz/info", {
  method: "POST",
  headers: {"Content-Type": "application/json"},
  body: JSON.stringify({type: "metaAndAssetCtxs"})
}).then(r => r.json())
```

```js
// Parse and combine market metadata with context
const perpMeta = perpData[0].universe
const perpCtxs = perpData[1]

const markets = perpMeta.map((m, i) => {
  const ctx = perpCtxs[i]
  const markPx = parseFloat(ctx.markPx)
  const openInterest = parseFloat(ctx.openInterest)
  return {
    name: m.name,
    dayNtlVlm: parseFloat(ctx.dayNtlVlm),
    openInterest,
    openInterestUsd: openInterest * markPx,
    markPx,
    prevDayPx: parseFloat(ctx.prevDayPx),
    priceChange: ((markPx - parseFloat(ctx.prevDayPx)) / parseFloat(ctx.prevDayPx)) * 100,
    funding: parseFloat(ctx.funding) * 100,  // Convert to percentage
    maxLeverage: m.maxLeverage,
    isDelisted: m.isDelisted || false
  }
}).filter(m => !m.isDelisted && m.dayNtlVlm > 0)

// Sort by volume
markets.sort((a, b) => b.dayNtlVlm - a.dayNtlVlm)
```

---

## Protocol Overview

```js
const totalVolume = d3.sum(markets, d => d.dayNtlVlm)
const totalOI = d3.sum(markets, d => d.openInterestUsd)
const activeMarkets = markets.length
```

<div class="grid grid-cols-3">
  <div class="card">
    <h3>24h Volume</h3>
    <div style="font-size: 2em; font-weight: bold; color: #0f5499;">
      ${d3.format("$,.0f")(totalVolume)}
    </div>
  </div>
  <div class="card">
    <h3>Open Interest</h3>
    <div style="font-size: 2em; font-weight: bold; color: #a0616a;">
      ${d3.format("$,.0f")(totalOI)}
    </div>
  </div>
  <div class="card">
    <h3>Active Markets</h3>
    <div style="font-size: 2em; font-weight: bold; color: #c78c39;">
      ${activeMarkets}
    </div>
  </div>
</div>

---

## Volume Distribution

Trading volume is heavily concentrated in a few major markets. The top 5 markets typically account for the vast majority of activity.

```js echo
const topN = view(Inputs.range([5, 30], {value: 15, step: 1, label: "Top N Markets"}))
```

```js
{
  const topMarkets = markets.slice(0, topN)
  const otherVolume = d3.sum(markets.slice(topN), d => d.dayNtlVlm)

  const chartData = [...topMarkets]
  if (otherVolume > 0) {
    chartData.push({name: "Other", dayNtlVlm: otherVolume})
  }

  display(Plot.plot({
    title: `Top ${topN} Markets by 24h Volume`,
    subtitle: `Top ${topN} represent ${d3.format(".1%")(d3.sum(topMarkets, d => d.dayNtlVlm) / totalVolume)} of total volume`,
    width: 800,
    height: 400,
    marginLeft: 80,
    x: {label: "24h Volume (USD)", grid: true, tickFormat: d => d3.format("$.2s")(d)},
    y: {label: null},
    marks: [
      Plot.barX(chartData, {
        y: "name",
        x: "dayNtlVlm",
        fill: d => d.name === "Other" ? "#7a8b8a" : "#0f5499",
        sort: {y: "-x"}
      }),
      Plot.text(chartData, {
        y: "name",
        x: "dayNtlVlm",
        text: d => d3.format("$,.0f")(d.dayNtlVlm),
        dx: 5,
        textAnchor: "start",
        fill: "#888",
        fontSize: 10
      }),
      Plot.ruleX([0])
    ]
  }))
}
```

### Volume Concentration (Cumulative)

```js
{
  // Calculate cumulative volume share
  let cumulative = 0
  const cumulativeData = markets.slice(0, 30).map((m, i) => {
    cumulative += m.dayNtlVlm
    return {
      rank: i + 1,
      name: m.name,
      share: cumulative / totalVolume * 100
    }
  })

  display(Plot.plot({
    title: "Cumulative Volume Share by Market Rank",
    subtitle: "How many markets does it take to capture X% of volume?",
    width: 800,
    height: 350,
    x: {label: "Market Rank", domain: [1, 30]},
    y: {label: "Cumulative % of Volume", domain: [0, 100], grid: true},
    marks: [
      Plot.areaY(cumulativeData, {x: "rank", y: "share", fill: "#0f5499", fillOpacity: 0.3}),
      Plot.line(cumulativeData, {x: "rank", y: "share", stroke: "#0f5499", strokeWidth: 2}),
      Plot.dot(cumulativeData, {x: "rank", y: "share", fill: "#0f5499", r: 4, tip: true,
        channels: {market: "name"}}),
      Plot.ruleY([50, 90], {stroke: "#666", strokeDasharray: "3,3"}),
      Plot.text([{x: 30, y: 50}], {text: ["50%"], dx: -10, fill: "#666"}),
      Plot.text([{x: 30, y: 90}], {text: ["90%"], dx: -10, fill: "#666"})
    ]
  }))
}
```

---

## Open Interest Analysis

Open Interest (OI) represents the total value of outstanding positions. High OI relative to volume can indicate longer-term positioning; low OI/volume ratio suggests more day trading.

```js
{
  const topOI = markets.slice().sort((a, b) => b.openInterestUsd - a.openInterestUsd).slice(0, 15)

  display(Plot.plot({
    title: "Top 15 Markets by Open Interest",
    width: 800,
    height: 400,
    marginLeft: 80,
    x: {label: "Open Interest (USD)", grid: true, tickFormat: d => d3.format("$.2s")(d)},
    y: {label: null},
    marks: [
      Plot.barX(topOI, {
        y: "name",
        x: "openInterestUsd",
        fill: "#a0616a",
        sort: {y: "-x"}
      }),
      Plot.text(topOI, {
        y: "name",
        x: "openInterestUsd",
        text: d => d3.format("$,.0f")(d.openInterestUsd),
        dx: 5,
        textAnchor: "start",
        fill: "#888",
        fontSize: 10
      }),
      Plot.ruleX([0])
    ]
  }))
}
```

### Volume vs Open Interest

Markets in the upper-left have high turnover (volume relative to OI) — more speculative/day trading. Markets in the lower-right have positions held longer.

```js
{
  const scatterData = markets.filter(m => m.openInterestUsd > 100000 && m.dayNtlVlm > 100000)

  display(Plot.plot({
    title: "Trading Activity: Volume vs Open Interest",
    subtitle: "Size = 24h Volume | Diagonal = 1x daily turnover",
    width: 800,
    height: 500,
    x: {type: "log", label: "Open Interest (USD)", grid: true, tickFormat: d => d3.format("$.0s")(d)},
    y: {type: "log", label: "24h Volume (USD)", grid: true, tickFormat: d => d3.format("$.0s")(d)},
    marks: [
      // Reference lines for turnover ratios
      Plot.line([[1e5, 1e5], [1e10, 1e10]], {stroke: "#666", strokeDasharray: "5,5", strokeOpacity: 0.5}),
      Plot.line([[1e5, 1e6], [1e9, 1e10]], {stroke: "#666", strokeDasharray: "2,2", strokeOpacity: 0.3}),
      Plot.dot(scatterData, {
        x: "openInterestUsd",
        y: "dayNtlVlm",
        r: d => Math.sqrt(d.dayNtlVlm) / 500,
        fill: d => d.priceChange > 0 ? "#2d724f" : "#b3312c",
        fillOpacity: 0.7,
        stroke: "#fff",
        strokeWidth: 0.5,
        tip: true,
        channels: {
          market: "name",
          price: d => d3.format("$,.2f")(d.markPx),
          change: d => d3.format("+.2f")(d.priceChange) + "%"
        }
      }),
      // Label top markets
      Plot.text(scatterData.slice(0, 8), {
        x: "openInterestUsd",
        y: "dayNtlVlm",
        text: "name",
        dy: -12,
        fontSize: 10,
        fill: "#888"
      })
    ]
  }))
}
```

---

## Funding Rates

Funding rates indicate market sentiment. Positive funding = longs pay shorts (bullish pressure). Negative funding = shorts pay longs (bearish pressure).

```js echo
const minVolume = view(Inputs.range([0, 50], {value: 5, step: 1, label: "Min Volume ($M)", transform: d => d * 1e6}))
```

```js
{
  const fundingData = markets
    .filter(m => m.dayNtlVlm >= minVolume)
    .slice()
    .sort((a, b) => b.funding - a.funding)
    .slice(0, 30)

  display(Plot.plot({
    title: "Funding Rates (8h)",
    subtitle: `Markets with ≥$${d3.format(".0f")(minVolume / 1e6)}M daily volume | Positive = longs pay shorts`,
    width: 800,
    height: 450,
    marginLeft: 80,
    x: {label: "Funding Rate (%)", grid: true, tickFormat: d => d.toFixed(4) + "%"},
    y: {label: null},
    marks: [
      Plot.barX(fundingData, {
        y: "name",
        x: "funding",
        fill: d => d.funding >= 0 ? "#2d724f" : "#b3312c",
        sort: {y: "-x"}
      }),
      Plot.ruleX([0], {stroke: "#fff", strokeWidth: 2})
    ]
  }))
}
```

### Funding Distribution

```js
{
  const allFunding = markets.filter(m => m.dayNtlVlm > 1e6).map(d => d.funding)

  display(Plot.plot({
    title: "Distribution of Funding Rates",
    subtitle: "Markets with >$1M daily volume",
    width: 700,
    height: 300,
    x: {label: "Funding Rate (%)"},
    y: {label: "Count", grid: true},
    marks: [
      Plot.rectY(allFunding, Plot.binX({y: "count"}, {x: d => d, fill: "#0f5499", thresholds: 30})),
      Plot.ruleX([0], {stroke: "#b3312c", strokeWidth: 2}),
      Plot.ruleX([d3.median(allFunding)], {stroke: "#a0616a", strokeWidth: 2, strokeDasharray: "5,5"})
    ]
  }))
}
```

Median funding: **${d3.format(".4f")(d3.median(markets.filter(m => m.dayNtlVlm > 1e6).map(d => d.funding)))}%** (8h rate)

---

## Price Performance (24h)

```js
{
  const priceData = markets.slice(0, 30)

  display(Plot.plot({
    title: "24h Price Change (Top 30 by Volume)",
    width: 800,
    height: 450,
    marginLeft: 80,
    x: {label: "Price Change (%)", grid: true, tickFormat: d => d.toFixed(1) + "%"},
    y: {label: null},
    marks: [
      Plot.barX(priceData, {
        y: "name",
        x: "priceChange",
        fill: d => d.priceChange >= 0 ? "#2d724f" : "#b3312c",
        sort: {y: "-x"}
      }),
      Plot.ruleX([0], {stroke: "#fff", strokeWidth: 2})
    ]
  }))
}
```

---

## Market Table

```js
{
  const tableData = markets.slice(0, 50).map(m => ({
    Market: m.name,
    Price: d3.format("$,.4f")(m.markPx),
    "24h Change": d3.format("+.2f")(m.priceChange) + "%",
    "24h Volume": d3.format("$,.0f")(m.dayNtlVlm),
    "Open Interest": d3.format("$,.0f")(m.openInterestUsd),
    "Funding (8h)": d3.format(".4f")(m.funding) + "%",
    "Max Leverage": m.maxLeverage + "x"
  }))

  display(Inputs.table(tableData, {
    format: {
      "24h Change": d => html`<span style="color: ${d.startsWith("+") ? "#2d724f" : "#b3312c"}">${d}</span>`,
      "Funding (8h)": d => html`<span style="color: ${parseFloat(d) >= 0 ? "#2d724f" : "#b3312c"}">${d}</span>`
    }
  }))
}
```

---

## Appendix: Data Sources

This notebook fetches live data from the Hyperliquid Info API.

### API Endpoint

**Source:** [Hyperliquid Info API](https://hyperliquid.gitbook.io/hyperliquid-docs/for-developers/api/info-endpoint)

The `metaAndAssetCtxs` endpoint returns perpetual market metadata combined with real-time context (prices, volume, funding rates, open interest).

```javascript
// Fetch perpetual market data from Hyperliquid API
const perpData = await fetch("https://api.hyperliquid.xyz/info", {
  method: "POST",
  headers: {"Content-Type": "application/json"},
  body: JSON.stringify({type: "metaAndAssetCtxs"})
}).then(r => r.json())
```

### Data Transformation

The raw API response is parsed and combined into a unified market object:

```javascript
// Parse and combine market metadata with context
const perpMeta = perpData[0].universe
const perpCtxs = perpData[1]

const markets = perpMeta.map((m, i) => {
  const ctx = perpCtxs[i]
  const markPx = parseFloat(ctx.markPx)
  const openInterest = parseFloat(ctx.openInterest)
  return {
    name: m.name,
    dayNtlVlm: parseFloat(ctx.dayNtlVlm),
    openInterest,
    openInterestUsd: openInterest * markPx,
    markPx,
    prevDayPx: parseFloat(ctx.prevDayPx),
    priceChange: ((markPx - parseFloat(ctx.prevDayPx)) / parseFloat(ctx.prevDayPx)) * 100,
    funding: parseFloat(ctx.funding) * 100,  // Convert to percentage
    maxLeverage: m.maxLeverage,
    isDelisted: m.isDelisted || false
  }
}).filter(m => !m.isDelisted && m.dayNtlVlm > 0)

// Sort by volume
markets.sort((a, b) => b.dayNtlVlm - a.dayNtlVlm)
```

### Data Notes

- **Funding rates** are 8-hour rates (annualized = rate × 3 × 365)
- **Open Interest** is calculated as position size × mark price
- **Volume** is 24h notional volume in USD
- Data refreshes on page load (not real-time streaming)

```js
import { expose } from "./bridge.js";

expose({
  totalVolume,
  totalOI,
  activeMarkets,
  topMarkets: markets.slice(0, 10).map(m => m.name)
})
```

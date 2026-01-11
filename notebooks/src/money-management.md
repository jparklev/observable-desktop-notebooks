---
title: Sizing the Trade, Surviving the Storm
theme: parchment
---

# Sizing the Trade, Surviving the Storm
## From Kelly Theory to Real-World Money Management

*"It's not whether you're right or wrong that's important, but how much money you make when you're right and how much you lose when you're wrong."* — George Soros

This notebook applies position sizing theory to real historical data. We'll explore 10 years of Bitcoin, Tesla, the S&P 500, and Gold — four very different beasts — and ask: *What if you had sized your bets differently?*

We'll cover:
- **The Reality Gap** — what actually happened to these assets (2015-2025)
- **Legends of Sizing** — how Buffett, Druckenmiller, Sundheim, and Renaissance think about position size
- **Kelly Meets Reality** — estimating optimal bet size from historical volatility
- **The What-If Machine** — interactive backtests with different Kelly fractions
- **Protecting the Downside** — options strategies for tail risk

The math gives you a number. The legends give you context. The data shows you the consequences.

---

```js
// FT Paper color palette for parchment theme
const colors = {
  btc: "#a0616a",      // Dusty Rose
  tsla: "#c78c39",     // Warm Amber
  spy: "#0f5499",      // FT Dark Blue
  gld: "#7a8b8a",      // Gray-Green
  positive: "#2d724f", // Muted Green
  negative: "#b3312c"  // Brick Red
};

const assetColors = {
  BTC: colors.btc,
  TSLA: colors.tsla,
  SPY: colors.spy,
  GLD: colors.gld
};
```

```js
// Load market data from data loader (fetched at build time)
const marketData = await FileAttachment("market-data.json").json()

// Parse dates and convert to Date objects
const btcData = marketData.btc.map(d => ({
  ...d,
  date: new Date(d.date)
}))

const tslaData = marketData.tsla.map(d => ({
  ...d,
  date: new Date(d.date)
}))

const spyData = marketData.spy.map(d => ({
  ...d,
  date: new Date(d.date)
}))

const gldData = marketData.gld.map(d => ({
  ...d,
  date: new Date(d.date)
}))
```

```js
// Calculate returns and volatility for each asset
function calculateReturns(data) {
  const sorted = [...data].sort((a, b) => a.date - b.date);
  return sorted.map((d, i) => ({
    ...d,
    return: i > 0 ? (d.close - sorted[i-1].close) / sorted[i-1].close : 0,
    logReturn: i > 0 ? Math.log(d.close / sorted[i-1].close) : 0
  })).slice(1); // Remove first row with no return
}

function calculateDrawdown(data) {
  const sorted = [...data].sort((a, b) => a.date - b.date);
  let peak = sorted[0].close;
  return sorted.map(d => {
    peak = Math.max(peak, d.close);
    return {
      ...d,
      drawdown: (d.close - peak) / peak
    };
  });
}

const btc = calculateReturns(btcData);
const tsla = calculateReturns(tslaData);
const spy = calculateReturns(spyData);
const gld = calculateReturns(gldData);

// Add drawdowns
const btcDD = calculateDrawdown(btcData);
const tslaDD = calculateDrawdown(tslaData);
const spyDD = calculateDrawdown(spyData);
const gldDD = calculateDrawdown(gldData);
```

```js
// Combine all data for charts
const allData = [...btcData, ...tslaData, ...spyData, ...gldData];
const allReturns = [...btc, ...tsla, ...spy, ...gld];
```

---

# I. The Reality Gap

Ten years. Four very different assets. Let's see what $100 invested in January 2015 would have become.

```js
{
  // Normalize each asset to $100 at their first data point
  function normalizeAsset(data) {
    const sorted = [...data].sort((a, b) => a.date - b.date);
    const firstValue = sorted[0].close;
    return sorted.map(d => ({
      ...d,
      normalized: (d.close / firstValue) * 100
    }));
  }

  const btcNorm = normalizeAsset(btcData);
  const tslaNorm = normalizeAsset(tslaData);
  const spyNorm = normalizeAsset(spyData);
  const gldNorm = normalizeAsset(gldData);

  const normalized = [...btcNorm, ...tslaNorm, ...spyNorm, ...gldNorm];

  // Get terminal values for labels
  const terminals = {
    BTC: btcNorm[btcNorm.length - 1]?.normalized,
    TSLA: tslaNorm[tslaNorm.length - 1]?.normalized,
    SPY: spyNorm[spyNorm.length - 1]?.normalized,
    GLD: gldNorm[gldNorm.length - 1]?.normalized
  };

  display(Plot.plot({
    title: "The Reality: $100 Invested in January 2015",
    width: 900,
    height: 500,
    style: "overflow: visible;",
    marginRight: 100,
    y: {
      type: "log",
      grid: true,
      label: "Portfolio Value ($)",
      tickFormat: d => `$${d3.format(",.0f")(d)}`
    },
    x: {label: "Date"},
    color: {
      domain: ["BTC", "TSLA", "SPY", "GLD"],
      range: [colors.btc, colors.tsla, colors.spy, colors.gld],
      legend: true
    },
    marks: [
      Plot.ruleY([100], {stroke: "#999", strokeDasharray: "4,4"}),
      Plot.lineY(normalized, {
        x: "date",
        y: "normalized",
        stroke: "asset",
        strokeWidth: 2.5
      }),
      Plot.text(
        Object.entries(terminals).map(([asset, value]) => ({
          asset,
          date: new Date("2024-12-01"),
          value
        })),
        {
          x: "date",
          y: "value",
          text: d => `${d.asset}: $${d3.format(",.0f")(d.value)}`,
          textAnchor: "start",
          dx: 5,
          fill: d => assetColors[d.asset],
          fontWeight: "bold"
        }
      )
    ]
  }));
}
```

Bitcoin turned $100 into over $10,000. But that's only half the story.

The other half is *how it felt along the way*.

---

## The Pain: Maximum Drawdowns

A drawdown is how far you've fallen from your peak. It's the number that makes you question everything at 3am.

```js
{
  // Calculate max drawdown for each asset
  function maxDrawdown(ddData) {
    return Math.min(...ddData.map(d => d.drawdown));
  }

  const drawdowns = [
    {asset: "BTC", maxDD: maxDrawdown(btcDD), color: colors.btc},
    {asset: "TSLA", maxDD: maxDrawdown(tslaDD), color: colors.tsla},
    {asset: "SPY", maxDD: maxDrawdown(spyDD), color: colors.spy},
    {asset: "GLD", maxDD: maxDrawdown(gldDD), color: colors.gld}
  ].sort((a, b) => a.maxDD - b.maxDD);

  display(Plot.plot({
    title: "Maximum Drawdowns (2015-2025)",
    subtitle: "How much you would have lost from peak to trough",
    width: 700,
    height: 300,
    x: {
      label: "Max Drawdown",
      tickFormat: d => `${(d * 100).toFixed(0)}%`,
      domain: [-1, 0]
    },
    y: {label: null, padding: 0.3},
    marks: [
      Plot.barX(drawdowns, {
        x: "maxDD",
        y: "asset",
        fill: "color",
        sort: {y: "x"}
      }),
      Plot.text(drawdowns, {
        x: "maxDD",
        y: "asset",
        text: d => `${(d.maxDD * 100).toFixed(0)}%`,
        dx: -25,
        fill: "white",
        fontWeight: "bold"
      }),
      Plot.ruleX([0])
    ]
  }));
}
```

Bitcoin's 80%+ drawdowns happened *multiple times*. Tesla crashed 70%. Even the S&P 500 dropped 34% during COVID.

**The question isn't just "what would I have made?" but "could I have held through that?"**

If you went all-in on Bitcoin with 100% of your portfolio, you'd need the stomach for an 80% drawdown. At 2x leverage (200% position), you'd have been wiped out entirely.

This is why position sizing matters.

---

## Volatility Comparison

```js
{
  // Calculate annualized volatility (std of daily returns * sqrt(252))
  function annualizedVol(returns) {
    const dailyReturns = returns.map(d => d.return);
    const std = d3.deviation(dailyReturns);
    return std * Math.sqrt(252);
  }

  // Calculate annualized return
  function annualizedReturn(data) {
    const sorted = [...data].sort((a, b) => a.date - b.date);
    const years = (sorted[sorted.length-1].date - sorted[0].date) / (365.25 * 24 * 60 * 60 * 1000);
    const totalReturn = sorted[sorted.length-1].close / sorted[0].close;
    return Math.pow(totalReturn, 1/years) - 1;
  }

  const stats = [
    {asset: "BTC", vol: annualizedVol(btc), ret: annualizedReturn(btcData), color: colors.btc},
    {asset: "TSLA", vol: annualizedVol(tsla), ret: annualizedReturn(tslaData), color: colors.tsla},
    {asset: "SPY", vol: annualizedVol(spy), ret: annualizedReturn(spyData), color: colors.spy},
    {asset: "GLD", vol: annualizedVol(gld), ret: annualizedReturn(gldData), color: colors.gld}
  ];

  display(Plot.plot({
    title: "Risk vs. Return (Annualized)",
    width: 600,
    height: 400,
    x: {
      label: "Annualized Volatility",
      tickFormat: d => `${(d * 100).toFixed(0)}%`
    },
    y: {
      label: "Annualized Return",
      tickFormat: d => `${(d * 100).toFixed(0)}%`
    },
    grid: true,
    marks: [
      Plot.dot(stats, {
        x: "vol",
        y: "ret",
        fill: "color",
        r: 12
      }),
      Plot.text(stats, {
        x: "vol",
        y: "ret",
        text: "asset",
        dy: -18,
        fontWeight: "bold"
      }),
      Plot.ruleY([0], {stroke: "#999", strokeDasharray: "4,4"}),
      Plot.ruleX([0], {stroke: "#999", strokeDasharray: "4,4"})
    ]
  }));
}
```

Higher return came with *much* higher volatility. Bitcoin's annual volatility is often 60-80%, compared to ~15% for the S&P 500.

This sets up the central question: **How much of your portfolio should you allocate to high-volatility assets?**

---

# II. Legends of Sizing

Different investors have different answers to the sizing question. Their approaches range from extreme concentration to statistical diversification.

<div class="grid grid-cols-2" style="gap: 1.5rem; margin: 2rem 0;">

<div class="card" style="padding: 1.5rem; background: #faf6f3; border-left: 4px solid #0f5499;">

### Warren Buffett
**The Concentrated Compounder**

*"Diversification is protection against ignorance. It makes little sense if you know what you are doing."*

**Framework:**
- 80% of capital in 5 positions
- Top position can be 25-40%
- "Punch card" mentality: 20 great ideas per lifetime

**When it works:** Deep research, long holding periods, businesses you truly understand.

</div>

<div class="card" style="padding: 1.5rem; background: #faf6f3; border-left: 4px solid #a0616a;">

### Stanley Druckenmiller
**The Conviction Aggressor**

*"The way to build long-term returns is through preservation of capital and home runs."*

**Framework:**
- Normal position: 10-15%
- High conviction: 30-50%
- "When you see it, bet big" — go to 100%+ when the setup is perfect

**Famous trade:** The Soros pound short started as a $1.5B idea. Soros called it "pathetic" and sized it to $10B.

</div>

<div class="card" style="padding: 1.5rem; background: #faf6f3; border-left: 4px solid #c78c39;">

### Dan Sundheim (D1 Capital)
**The Risk-Budgeted Concentrator**

*"Size positions so you can survive a 20-30% move against you."*

**Framework:**
- Top positions: ~15% of long book
- Gross exposure: 150-200%
- Short book capped at 25-30% to prevent squeeze risk

**Post-2021 adjustment:** Reduced gross from 218% to 165% after GameStop exposed tail risk in crowded shorts.

</div>

<div class="card" style="padding: 1.5rem; background: #faf6f3; border-left: 4px solid #2d724f;">

### Renaissance Technologies
**The Statistical Arbitrageur**

*"We're right 50.75% of the time. But we're 100% right about that."*

**Framework:**
- Thousands of small positions
- Leverage: 12.5x to 20x
- No single position conviction — conviction is in the *model*

**Key insight:** When your edge is statistical, not analytical, diversification *is* the strategy.

</div>

</div>

---

**The lesson:** Buffett and Druckenmiller concentrate because they believe their *individual* conviction is the edge. Renaissance diversifies because their *statistical* model is the edge.

**Your sizing should match your edge type.**

---

# III. Kelly Meets Reality

The Kelly Criterion gives you an "optimal" bet size — the fraction of capital that maximizes long-term geometric growth.

```tex
f^* = \frac{\mu - r}{\sigma^2}
```

For a self-financing portfolio (no risk-free rate): *f* = μ / σ²

Where μ is expected return and σ is volatility.

The problem? **You don't know μ and σ. You can only estimate them from history.**

```js echo
const estimationWindow = view(Inputs.range([21, 252], {value: 63, step: 1, label: "Estimation Window (days)"}))
```

```js echo
const selectedAsset = view(Inputs.select(["BTC", "TSLA", "SPY", "GLD"], {value: "SPY", label: "Asset"}))
```

```js
{
  const assetData = selectedAsset === "BTC" ? btc :
                    selectedAsset === "TSLA" ? tsla :
                    selectedAsset === "SPY" ? spy : gld;

  // Calculate rolling Kelly estimate
  const window = estimationWindow;
  const rollingKelly = assetData.map((d, i) => {
    if (i < window - 1) return {...d, kelly: null, vol: null};

    const slice = assetData.slice(i - window + 1, i + 1);
    const returns = slice.map(s => s.return);
    const mean = d3.mean(returns) * 252; // Annualized
    const vol = d3.deviation(returns) * Math.sqrt(252); // Annualized
    const kelly = mean / (vol * vol);

    return {...d, kelly, vol, mean};
  }).filter(d => d.kelly !== null);

  // Summary stats
  const kellyValues = rollingKelly.map(d => d.kelly).filter(d => isFinite(d));
  const medianKelly = d3.median(kellyValues);
  const stdKelly = d3.deviation(kellyValues);

  display(html`<div style="margin-bottom: 1rem;">
    <strong>Estimated Kelly for ${selectedAsset}:</strong>
    Median = ${(medianKelly * 100).toFixed(0)}%,
    Std Dev = ${(stdKelly * 100).toFixed(0)}%
  </div>`);

  display(Plot.plot({
    title: `Rolling ${window}-Day Kelly Estimate for ${selectedAsset}`,
    subtitle: "If Kelly swings from -50% to +200%, how confident are you in any single estimate?",
    width: 900,
    height: 400,
    y: {
      label: "Kelly Fraction",
      tickFormat: d => `${(d * 100).toFixed(0)}%`,
      domain: [-1, 3]
    },
    x: {label: "Date"},
    marks: [
      Plot.ruleY([0], {stroke: "#999"}),
      Plot.ruleY([1], {stroke: colors.negative, strokeDasharray: "4,4"}),
      Plot.areaY(rollingKelly, {
        x: "date",
        y1: 0,
        y2: "kelly",
        fill: d => d.kelly > 0 ? colors.positive : colors.negative,
        fillOpacity: 0.3
      }),
      Plot.lineY(rollingKelly, {
        x: "date",
        y: "kelly",
        stroke: assetColors[selectedAsset],
        strokeWidth: 2
      }),
      Plot.text([{x: new Date("2023-01-01"), y: 1}], {
        x: "x", y: "y",
        text: ["← Full Kelly = 100%"],
        textAnchor: "start",
        fill: colors.negative
      })
    ]
  }));
}
```

The rolling Kelly estimate is **wildly unstable**. It swings from negative (don't touch this asset!) to 200%+ (lever up!).

This is why practitioners use **Fractional Kelly**:

| Strategy | Fraction | Rationale |
|----------|----------|-----------|
| Quarter Kelly | 25% | Conservative — prioritizes survival |
| Half Kelly | 50% | Standard practitioner choice |
| Full Kelly | 100% | Mathematically optimal but stomach-churning |
| 2x Kelly | 200% | Ruin zone — negative expected growth |

Half Kelly gives you 75% of the growth with 50% of the volatility. It's a margin of safety against estimation error.

---

# IV. The What-If Machine

Let's simulate what would have happened if you had applied different Kelly fractions to these assets.

```js echo
const whatIfAsset = view(Inputs.select(["BTC", "TSLA", "SPY", "GLD"], {value: "BTC", label: "Asset"}))
```

```js echo
const kellyFraction = view(Inputs.range([0.1, 2.5], {value: 0.5, step: 0.1, label: "Kelly Fraction"}))
```

```js echo
const startYear = view(Inputs.range([2015, 2022], {value: 2017, step: 1, label: "Start Year"}))
```

```js
{
  const assetReturns = whatIfAsset === "BTC" ? btc :
                       whatIfAsset === "TSLA" ? tsla :
                       whatIfAsset === "SPY" ? spy : gld;

  const filtered = assetReturns.filter(d => d.date >= new Date(startYear, 0, 1));

  if (filtered.length === 0) {
    display(html`<p>No data for ${whatIfAsset} starting in ${startYear}</p>`);
  } else {
    // Calculate rolling Kelly to get average position size
    const window = 63;
    let positions = [];

    // Simulate portfolio trajectory
    let buyHold = 100;
    let kellyPortfolio = 100;

    const trajectory = filtered.map((d, i) => {
      // Update buy & hold
      buyHold *= (1 + d.return);

      // For Kelly, use lagged estimate
      let kellyEstimate = 1;
      if (i >= window) {
        const slice = filtered.slice(i - window, i);
        const returns = slice.map(s => s.return);
        const mean = d3.mean(returns) * 252;
        const vol = d3.deviation(returns) * Math.sqrt(252);
        kellyEstimate = mean / (vol * vol);
      }

      // Clip Kelly to reasonable range
      kellyEstimate = Math.max(-2, Math.min(5, kellyEstimate));
      const position = kellyFraction * kellyEstimate;

      // Cap position at 300% and floor at -100%
      const cappedPosition = Math.max(-1, Math.min(3, position));

      kellyPortfolio *= (1 + cappedPosition * d.return);

      return {
        date: d.date,
        buyHold,
        kellyPortfolio,
        drawdown: 0 // Will calculate below
      };
    });

    // Calculate drawdowns
    let bhPeak = 100;
    let kPeak = 100;
    trajectory.forEach(d => {
      bhPeak = Math.max(bhPeak, d.buyHold);
      kPeak = Math.max(kPeak, d.kellyPortfolio);
      d.bhDrawdown = (d.buyHold - bhPeak) / bhPeak;
      d.kDrawdown = (d.kellyPortfolio - kPeak) / kPeak;
    });

    const finalBH = trajectory[trajectory.length - 1].buyHold;
    const finalK = trajectory[trajectory.length - 1].kellyPortfolio;
    const maxKDD = Math.min(...trajectory.map(d => d.kDrawdown));

    display(html`<div class="grid grid-cols-3" style="gap: 1rem; margin: 1rem 0;">
      <div class="card" style="padding: 1rem; text-align: center;">
        <div style="font-size: 2rem; font-weight: bold; color: ${colors.spy};">$${d3.format(",.0f")(finalBH)}</div>
        <div>Buy & Hold</div>
      </div>
      <div class="card" style="padding: 1rem; text-align: center;">
        <div style="font-size: 2rem; font-weight: bold; color: ${assetColors[whatIfAsset]};">$${d3.format(",.0f")(finalK)}</div>
        <div>${kellyFraction}x Kelly</div>
      </div>
      <div class="card" style="padding: 1rem; text-align: center;">
        <div style="font-size: 2rem; font-weight: bold; color: ${colors.negative};">${(maxKDD * 100).toFixed(0)}%</div>
        <div>Max Drawdown</div>
      </div>
    </div>`);

    display(Plot.plot({
      title: `${whatIfAsset} Portfolio with ${kellyFraction}x Kelly Sizing (from ${startYear})`,
      width: 900,
      height: 450,
      y: {
        type: "log",
        label: "Portfolio Value ($)",
        tickFormat: d => `$${d3.format(",.0f")(d)}`,
        grid: true
      },
      x: {label: "Date"},
      marks: [
        Plot.ruleY([100], {stroke: "#999", strokeDasharray: "4,4"}),
        Plot.areaY(trajectory.filter(d => d.kDrawdown < -0.1), {
          x: "date",
          y1: d => d.kellyPortfolio / (1 + d.kDrawdown),
          y2: "kellyPortfolio",
          fill: colors.negative,
          fillOpacity: 0.2
        }),
        Plot.lineY(trajectory, {
          x: "date",
          y: "buyHold",
          stroke: "#999",
          strokeWidth: 2,
          strokeDasharray: "4,4"
        }),
        Plot.lineY(trajectory, {
          x: "date",
          y: "kellyPortfolio",
          stroke: assetColors[whatIfAsset],
          strokeWidth: 2.5
        }),
        Plot.text([{x: trajectory[trajectory.length - 1].date, y: finalBH}], {
          x: "x", y: "y", text: ["Buy & Hold"], dx: 5, textAnchor: "start", fill: "#999"
        }),
        Plot.text([{x: trajectory[trajectory.length - 1].date, y: finalK}], {
          x: "x", y: "y", text: [`${kellyFraction}x Kelly`], dx: 5, textAnchor: "start", fill: assetColors[whatIfAsset]
        })
      ]
    }));
  }
}
```

**Try different combinations:**
- BTC with 0.25x Kelly from 2017 — moderate gains, survives the 2018 crash
- BTC with 2.0x Kelly from 2017 — explosive gains... until the 2018 crash wipes you out
- SPY with 1.0x Kelly — stable, boring, effective

The red shading shows drawdown periods. Notice how higher Kelly fractions amplify both gains *and* losses.

---

# V. Protecting the Downside

Position sizing tells you how much to bet. But what if you want to *bound* your downside?

Options let you define your risk precisely.

## The Protective Put

A **protective put** is insurance: you own the stock, and you buy a put option that gives you the right to sell at a fixed price (the strike).

```js echo
const spotPrice = view(Inputs.range([50, 200], {value: 100, step: 1, label: "Current Stock Price ($)"}))
```

```js echo
const putStrike = view(Inputs.range([0.7, 1.0], {value: 0.9, step: 0.01, label: "Put Strike (% of spot)"}))
```

```js echo
const putPremium = view(Inputs.range([0.01, 0.10], {value: 0.03, step: 0.005, label: "Put Premium (% of spot)"}))
```

```js
{
  const strike = spotPrice * putStrike;
  const premium = spotPrice * putPremium;

  // Generate P/L data across price range
  const priceRange = d3.range(spotPrice * 0.5, spotPrice * 1.5, 1);

  const payoffData = priceRange.flatMap(price => {
    // Stock only P/L
    const stockPL = price - spotPrice;

    // Put payoff at expiration
    const putPayoff = Math.max(strike - price, 0) - premium;

    // Combined
    const protectedPL = stockPL + putPayoff;

    return [
      {price, pl: stockPL, strategy: "Unhedged Stock"},
      {price, pl: protectedPL, strategy: "Stock + Put"}
    ];
  });

  // Calculate breakeven and max loss
  const maxLoss = (strike - spotPrice) - premium;
  const breakeven = spotPrice + premium;

  display(html`<div style="margin: 1rem 0;">
    <strong>Strike:</strong> $${strike.toFixed(0)} (${(putStrike * 100).toFixed(0)}% of spot) |
    <strong>Premium:</strong> $${premium.toFixed(2)} (${(putPremium * 100).toFixed(1)}%) |
    <strong>Max Loss:</strong> ${(maxLoss / spotPrice * 100).toFixed(1)}% |
    <strong>Breakeven:</strong> $${breakeven.toFixed(0)}
  </div>`);

  display(Plot.plot({
    title: "Protective Put: P/L at Expiration",
    width: 800,
    height: 400,
    x: {
      label: "Stock Price at Expiration ($)",
      domain: [spotPrice * 0.5, spotPrice * 1.5]
    },
    y: {
      label: "Profit/Loss ($)",
      tickFormat: d => d >= 0 ? `+$${d}` : `-$${Math.abs(d)}`,
      grid: true
    },
    color: {
      domain: ["Unhedged Stock", "Stock + Put"],
      range: ["#999", colors.positive],
      legend: true
    },
    marks: [
      Plot.ruleY([0], {stroke: "#ccc"}),
      Plot.ruleX([spotPrice], {stroke: "#ccc", strokeDasharray: "4,4"}),
      Plot.ruleX([strike], {stroke: colors.negative, strokeDasharray: "4,4"}),
      Plot.line(payoffData, {
        x: "price",
        y: "pl",
        stroke: "strategy",
        strokeWidth: 2.5
      }),
      Plot.text([{x: strike, y: -40}], {
        x: "x", y: "y",
        text: ["Strike"],
        fill: colors.negative
      }),
      Plot.areaY(payoffData.filter(d => d.strategy === "Stock + Put" && d.price < strike), {
        x: "price",
        y1: d => payoffData.find(p => p.price === d.price && p.strategy === "Unhedged Stock").pl,
        y2: "pl",
        fill: colors.positive,
        fillOpacity: 0.2
      })
    ]
  }));
}
```

The green shaded area shows where the put *saves* you. Below the strike, your losses are capped.

**The tradeoff:** You pay the premium even if the stock goes up. That's the cost of insurance.

---

## The Collar

A **collar** combines a protective put with a covered call. You sell an out-of-the-money call to pay for the put.

```js echo
const callStrike = view(Inputs.range([1.0, 1.3], {value: 1.1, step: 0.01, label: "Call Strike (% of spot)"}))
```

```js
{
  const pStrike = spotPrice * putStrike;
  const cStrike = spotPrice * callStrike;
  const pPremium = spotPrice * putPremium;
  const cPremium = spotPrice * putPremium * 0.8; // Approximate
  const netPremium = pPremium - cPremium;

  const priceRange = d3.range(spotPrice * 0.5, spotPrice * 1.5, 1);

  const collarData = priceRange.flatMap(price => {
    const stockPL = price - spotPrice;
    const putPayoff = Math.max(pStrike - price, 0) - pPremium;
    const callPayoff = -Math.max(price - cStrike, 0) + cPremium;

    return [
      {price, pl: stockPL, strategy: "Unhedged"},
      {price, pl: stockPL + putPayoff, strategy: "Protective Put"},
      {price, pl: stockPL + putPayoff + callPayoff, strategy: "Collar"}
    ];
  });

  // Max gain/loss for collar
  const collarMaxGain = (cStrike - spotPrice) - netPremium;
  const collarMaxLoss = (pStrike - spotPrice) - netPremium;

  display(html`<div style="margin: 1rem 0;">
    <strong>Put Strike:</strong> $${pStrike.toFixed(0)} |
    <strong>Call Strike:</strong> $${cStrike.toFixed(0)} |
    <strong>Net Premium:</strong> ${netPremium >= 0 ? "Pay" : "Receive"} $${Math.abs(netPremium).toFixed(2)} |
    <strong>Max Gain:</strong> +${(collarMaxGain / spotPrice * 100).toFixed(1)}% |
    <strong>Max Loss:</strong> ${(collarMaxLoss / spotPrice * 100).toFixed(1)}%
  </div>`);

  display(Plot.plot({
    title: "Collar Strategy: Bounded Risk, Bounded Reward",
    width: 800,
    height: 400,
    x: {
      label: "Stock Price at Expiration ($)",
      domain: [spotPrice * 0.5, spotPrice * 1.5]
    },
    y: {
      label: "Profit/Loss ($)",
      tickFormat: d => d >= 0 ? `+$${d}` : `-$${Math.abs(d)}`,
      grid: true
    },
    color: {
      domain: ["Unhedged", "Protective Put", "Collar"],
      range: ["#999", colors.positive, colors.spy],
      legend: true
    },
    marks: [
      Plot.ruleY([0], {stroke: "#ccc"}),
      Plot.ruleX([spotPrice], {stroke: "#ccc", strokeDasharray: "4,4"}),
      Plot.ruleX([pStrike], {stroke: colors.negative, strokeDasharray: "4,4"}),
      Plot.ruleX([cStrike], {stroke: colors.positive, strokeDasharray: "4,4"}),
      Plot.line(collarData, {
        x: "price",
        y: "pl",
        stroke: "strategy",
        strokeWidth: 2.5
      })
    ]
  }));
}
```

The collar creates a "corridor" for your returns:
- Below the put strike: losses are capped
- Above the call strike: gains are also capped (you sold that upside)

**This is often used for concentrated stock positions** — you own a lot of company stock (maybe from compensation) and want to protect it without selling and triggering taxes.

---

## Tail Risk Hedging

Institutional investors sometimes allocate **2-5% of the portfolio** to permanent "tail hedges" — deep out-of-the-money puts that lose money 95% of the time but pay off massively during crashes.

<div class="card" style="padding: 1.5rem; background: #faf6f3; margin: 1.5rem 0;">

### The Universa Model

Nassim Taleb's fund Universa Investments runs a permanent tail-hedge strategy:

- **Allocation:** ~3% of portfolio to deep OTM puts
- **Normal years:** Lose the premium (drag on returns)
- **Crash years:** 100%+ returns on the hedge, allowing you to buy the dip

**2020 COVID crash:** Universa reportedly returned 4,000% on their hedges in March 2020.

The strategy only works if you *stay invested* in the core portfolio. The hedge is what lets you stay invested.

</div>

---

# VI. Putting It Together

Let's combine everything: position sizing, diversification, and risk budgeting.

```js echo
const weights = view(Inputs.form({
  btc: Inputs.range([0, 50], {value: 10, step: 5, label: "BTC %"}),
  tsla: Inputs.range([0, 50], {value: 10, step: 5, label: "TSLA %"}),
  spy: Inputs.range([0, 80], {value: 60, step: 5, label: "SPY %"}),
  gld: Inputs.range([0, 50], {value: 20, step: 5, label: "GLD %"})
}))
```

```js
{
  const totalWeight = weights.btc + weights.tsla + weights.spy + weights.gld;

  if (totalWeight !== 100) {
    display(html`<div style="color: ${colors.negative}; font-weight: bold;">
      Weights sum to ${totalWeight}%. Adjust to equal 100%.
    </div>`);
  } else {
    // Align all returns to common dates
    const dateSet = new Set(spy.map(d => d.date.toISOString().slice(0, 10)));

    const btcAligned = btc.filter(d => dateSet.has(d.date.toISOString().slice(0, 10)));
    const tslaAligned = tsla.filter(d => dateSet.has(d.date.toISOString().slice(0, 10)));
    const spyAligned = spy.filter(d => dateSet.has(d.date.toISOString().slice(0, 10)));
    const gldAligned = gld.filter(d => dateSet.has(d.date.toISOString().slice(0, 10)));

    // Create portfolio returns
    let portfolioValue = 100;
    const portfolio = spyAligned.map((d, i) => {
      const btcReturn = btcAligned[i]?.return || 0;
      const tslaReturn = tslaAligned[i]?.return || 0;
      const spyReturn = d.return;
      const gldReturn = gldAligned[i]?.return || 0;

      const portfolioReturn =
        (weights.btc / 100) * btcReturn +
        (weights.tsla / 100) * tslaReturn +
        (weights.spy / 100) * spyReturn +
        (weights.gld / 100) * gldReturn;

      portfolioValue *= (1 + portfolioReturn);

      return {
        date: d.date,
        value: portfolioValue,
        return: portfolioReturn
      };
    });

    // Calculate stats
    const finalValue = portfolio[portfolio.length - 1].value;
    const returns = portfolio.map(d => d.return);
    const annualizedVol = d3.deviation(returns) * Math.sqrt(252);
    const years = portfolio.length / 252;
    const annualizedReturn = Math.pow(finalValue / 100, 1/years) - 1;
    const sharpe = annualizedReturn / annualizedVol;

    // Max drawdown
    let peak = 100;
    let maxDD = 0;
    portfolio.forEach(d => {
      peak = Math.max(peak, d.value);
      const dd = (d.value - peak) / peak;
      maxDD = Math.min(maxDD, dd);
    });

    display(html`<div class="grid grid-cols-4" style="gap: 1rem; margin: 1rem 0;">
      <div class="card" style="padding: 1rem; text-align: center;">
        <div style="font-size: 1.8rem; font-weight: bold;">$${d3.format(",.0f")(finalValue)}</div>
        <div>Final Value</div>
      </div>
      <div class="card" style="padding: 1rem; text-align: center;">
        <div style="font-size: 1.8rem; font-weight: bold;">${(annualizedReturn * 100).toFixed(1)}%</div>
        <div>Annual Return</div>
      </div>
      <div class="card" style="padding: 1rem; text-align: center;">
        <div style="font-size: 1.8rem; font-weight: bold;">${(annualizedVol * 100).toFixed(1)}%</div>
        <div>Volatility</div>
      </div>
      <div class="card" style="padding: 1rem; text-align: center;">
        <div style="font-size: 1.8rem; font-weight: bold; color: ${sharpe > 0.5 ? colors.positive : colors.negative};">${sharpe.toFixed(2)}</div>
        <div>Sharpe Ratio</div>
      </div>
    </div>`);

    display(Plot.plot({
      title: "Portfolio Growth",
      subtitle: `Max Drawdown: ${(maxDD * 100).toFixed(0)}%`,
      width: 900,
      height: 400,
      y: {
        type: "log",
        label: "Portfolio Value ($)",
        tickFormat: d => `$${d3.format(",.0f")(d)}`,
        grid: true
      },
      x: {label: "Date"},
      marks: [
        Plot.ruleY([100], {stroke: "#999", strokeDasharray: "4,4"}),
        Plot.lineY(portfolio, {
          x: "date",
          y: "value",
          stroke: colors.spy,
          strokeWidth: 2.5
        })
      ]
    }));

    // Allocation pie
    const allocation = [
      {asset: "BTC", weight: weights.btc, color: colors.btc},
      {asset: "TSLA", weight: weights.tsla, color: colors.tsla},
      {asset: "SPY", weight: weights.spy, color: colors.spy},
      {asset: "GLD", weight: weights.gld, color: colors.gld}
    ].filter(d => d.weight > 0);

    display(Plot.plot({
      title: "Portfolio Allocation",
      width: 400,
      height: 300,
      marks: [
        Plot.barY(allocation, {
          x: "asset",
          y: "weight",
          fill: "color"
        }),
        Plot.text(allocation, {
          x: "asset",
          y: "weight",
          text: d => `${d.weight}%`,
          dy: -10,
          fontWeight: "bold"
        }),
        Plot.ruleY([0])
      ]
    }));
  }
}
```

---

## Key Takeaways

<div class="grid grid-cols-2" style="gap: 1.5rem; margin: 2rem 0;">

<div class="card" style="padding: 1.5rem;">

### Know Your Edge Type

**Analytical edge** (Buffett, Druckenmiller): You understand something others don't. Concentrate.

**Statistical edge** (Renaissance): You have a model with a small but consistent edge. Diversify and lever.

**No edge**: Index and keep costs low.

</div>

<div class="card" style="padding: 1.5rem;">

### Size for Survival

The Kelly Criterion gives you a target, but:
- You don't know the true parameters
- Use **Half Kelly** as a margin of safety
- Size so you can survive a 30% move against you

</div>

<div class="card" style="padding: 1.5rem;">

### Volatility is the Tax

High-volatility assets (BTC, TSLA) have higher *arithmetic* returns but pay a volatility tax.

A 10% allocation to BTC gives you exposure without betting the farm.

</div>

<div class="card" style="padding: 1.5rem;">

### Define Your Risk

Options let you bound outcomes:
- **Protective put**: Cap your downside
- **Collar**: Cap both upside and downside
- **Tail hedge**: Pay small premium for crash protection

</div>

</div>

---

## Appendix: Data Sources

This notebook fetches real historical price data from public APIs.

### Bitcoin (CoinGecko)

**API Documentation:** [CoinGecko API](https://www.coingecko.com/en/api/documentation)

```javascript
// Fetch 10 years of daily BTC prices (shown, not executed)
const btcData = await fetch(
  "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency=usd&days=3650&interval=daily"
).then(r => r.json())

// Returns: { prices: [[timestamp, price], ...], market_caps: [...], total_volumes: [...] }
```

### Stocks (Stooq)

**Source:** [Stooq.com](https://stooq.com/) - Free historical data for global equities.

```javascript
// Fetch Tesla daily data (shown, not executed)
const tsla = await fetch(
  "https://stooq.com/q/d/l/?s=tsla.us&i=d&d1=20150101&d2=20250101"
).then(r => r.text())

// Returns CSV: Date,Open,High,Low,Close,Volume
```

### Data Notes

- **BTC**: Trades 24/7/365, so has more data points than stocks
- **Stocks (TSLA, SPY, GLD)**: Trade ~252 days/year
- **All returns**: Calculated as daily close-to-close percentage change
- **Volatility**: Annualized using √252 multiplier

---

```js
import { expose } from "./bridge.js";

// Calculate key metrics for verification
const btcFinal = btcData[btcData.length - 1]?.close;
const spyFinal = spyData[spyData.length - 1]?.close;

expose({
  assetsLoaded: allData.length > 0,
  btcDataPoints: btcData.length,
  spyDataPoints: spyData.length,
  selectedAsset,
  kellyFraction,
  startYear
});
```

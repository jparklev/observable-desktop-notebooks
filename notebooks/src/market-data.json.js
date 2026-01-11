// Data loader for historical price data
// Runs at build time, bypassing CORS restrictions

const startDate = new Date("2015-01-01");
const endDate = new Date("2025-01-01");

// Fetch Bitcoin from CryptoCompare (free, no auth required for limited use)
async function fetchBTC() {
  try {
    // CryptoCompare histoday endpoint - max 2000 per request
    const allData = [];
    let toTs = Math.floor(Date.now() / 1000);

    // Fetch in chunks going backwards
    for (let i = 0; i < 3; i++) { // ~6000 days = ~16 years
      const url = `https://min-api.cryptocompare.com/data/v2/histoday?fsym=BTC&tsym=USD&limit=2000&toTs=${toTs}`;
      const res = await fetch(url);
      if (!res.ok) throw new Error(`CryptoCompare: ${res.status}`);
      const json = await res.json();

      if (!json.Data || !json.Data.Data) break;
      const data = json.Data.Data;

      const parsed = data.map(d => ({
        date: new Date(d.time * 1000).toISOString().slice(0, 10),
        close: d.close,
        asset: "BTC"
      }));

      allData.push(...parsed);

      // Go back before first candle
      toTs = data[0].time - 86400;

      // Rate limit protection
      await new Promise(r => setTimeout(r, 200));
    }

    // Remove duplicates and filter
    const seen = new Set();
    return allData
      .filter(d => {
        if (seen.has(d.date)) return false;
        seen.add(d.date);
        return new Date(d.date) >= startDate && new Date(d.date) < endDate && d.close > 0;
      })
      .sort((a, b) => new Date(a.date) - new Date(b.date));
  } catch (e) {
    console.error("Failed to fetch BTC:", e);
    return [];
  }
}

// Fetch from Stooq
async function fetchStooq(symbol, name) {
  try {
    const url = `https://stooq.com/q/d/l/?s=${symbol}&i=d&d1=20150101&d2=20250101`;
    const res = await fetch(url);
    if (!res.ok) throw new Error(`Stooq ${name}: ${res.status}`);
    const text = await res.text();

    const lines = text.trim().split('\n');
    if (lines.length < 2) return [];

    return lines.slice(1).map(line => {
      const values = line.split(',');
      const dateStr = values[0];
      const close = parseFloat(values[4]);
      return {
        date: dateStr,
        close: close,
        asset: name
      };
    }).filter(d => !isNaN(d.close) && new Date(d.date) >= startDate && new Date(d.date) < endDate);
  } catch (e) {
    console.error(`Failed to fetch ${name}:`, e);
    return [];
  }
}

// Fetch all data in parallel
const [btc, tsla, spy, gld] = await Promise.all([
  fetchBTC(),
  fetchStooq("tsla.us", "TSLA"),
  fetchStooq("spy.us", "SPY"),
  fetchStooq("gld.us", "GLD")
]);

const result = {
  btc,
  tsla,
  spy,
  gld,
  fetchedAt: new Date().toISOString()
};

process.stdout.write(JSON.stringify(result, null, 2));

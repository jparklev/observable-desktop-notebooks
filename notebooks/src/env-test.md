---
title: Environment Variables Test
theme: parchment
---

# Environment Variables Test

This notebook demonstrates how to use environment variables in Observable Framework.

## How it works

1. Secrets are stored in a `.env` file (not checked into git)
2. Data loaders read secrets at **build time** using `dotenv`
3. Only safe, derived data is sent to the browser

## Data from the loader

```js
const config = await FileAttachment("env-config.json").json()
```

```js
display(config)
```

```js
display(html`<p>The secret message: <strong>${config.message}</strong></p>`)
display(html`<p>API key present: ${config.hasApiKey ? "Yes" : "No"} (prefix: <code>${config.apiKeyPrefix}</code>)</p>`)
display(html`<p>Data was generated at: ${config.timestamp}</p>`)
```

## Key insight

Notice how the full API key (`sk-test-12345`) is NOT exposed to the browser - only a safe prefix. The data loader ran at build time, read the secret, and output only what we chose to expose.

## Source files

**`.env`** (gitignored):
```
SECRET_MESSAGE=Hello from the .env file!
API_KEY=sk-test-12345
```

**`env-config.json.js`** (data loader):
```javascript
import "dotenv/config";

const cfg = {
  message: process.env.SECRET_MESSAGE || "No secret found",
  hasApiKey: !!process.env.API_KEY,
  apiKeyPrefix: process.env.API_KEY?.slice(0, 7) + "...",
  timestamp: new Date().toISOString()
};

process.stdout.write(JSON.stringify(cfg, null, 2));
```

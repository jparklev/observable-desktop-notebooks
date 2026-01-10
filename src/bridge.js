(() => {
  if (window.__notebook_viewer__) return;

  let computeDepth = 0;
  let lastCompute = performance.now();
  let runtimeHookPromise = null;

  // Notify the API that the page has loaded
  const notifyLoaded = async () => {
    try {
      await fetch("http://127.0.0.1:9847/_internal/loaded", {
        method: "POST",
        headers: { "content-type": "application/json" },
        body: "{}",
      });
    } catch {
      // Best-effort; API might not be ready yet
    }
  };
  notifyLoaded();

  // Console log capture
  const MAX_LOG_ENTRIES = 500;
  const logBuffer = [];

  const captureLog = (level, args) => {
    const entry = {
      level,
      timestamp: Date.now(),
      message: args.map(arg => {
        if (typeof arg === "string") return arg;
        try {
          return JSON.stringify(arg);
        } catch {
          return String(arg);
        }
      }).join(" ")
    };
    logBuffer.push(entry);
    if (logBuffer.length > MAX_LOG_ENTRIES) {
      logBuffer.shift();
    }
  };

  const originalConsole = {
    log: console.log.bind(console),
    warn: console.warn.bind(console),
    error: console.error.bind(console),
  };

  console.log = (...args) => {
    captureLog("log", args);
    originalConsole.log(...args);
  };

  console.warn = (...args) => {
    captureLog("warn", args);
    originalConsole.warn(...args);
  };

  console.error = (...args) => {
    captureLog("error", args);
    originalConsole.error(...args);
  };

  const getLogs = (clear = false) => {
    const logs = [...logBuffer];
    if (clear) {
      logBuffer.length = 0;
    }
    return logs;
  };

  const clearLogs = () => {
    logBuffer.length = 0;
  };

  const postJson = async (port, path, payload) => {
    const url = `http://127.0.0.1:${port}${path}`;
    await fetch(url, {
      method: "POST",
      headers: { "content-type": "application/json" },
      body: JSON.stringify(payload),
    });
  };

  const toJsonSafe = (value) => {
    if (value === undefined) return null;
    try {
      return JSON.parse(JSON.stringify(value));
    } catch (err) {
      console.warn("[notebook-viewer] toJsonSafe: value not JSON-serializable, using String():", err.message);
      return String(value);
    }
  };

  const hookRuntime = () => {
    if (runtimeHookPromise) return runtimeHookPromise;

    runtimeHookPromise = (async () => {
      try {
        const mod = await import("/_observablehq/runtime.js");
        const Runtime = mod?.Runtime;
        if (!Runtime?.prototype) return;

        const original = Runtime.prototype._computeNow;
        if (typeof original !== "function") return;
        if (original.__notebook_viewer_wrapped) return;

        const wrapped = async function (...args) {
          computeDepth += 1;
          try {
            return await original.apply(this, args);
          } finally {
            computeDepth -= 1;
            lastCompute = performance.now();
          }
        };
        wrapped.__notebook_viewer_wrapped = true;

        Runtime.prototype._computeNow = wrapped;
      } catch (err) {
        // Best-effort; not all pages expose the runtime bundle path.
        console.warn("[notebook-viewer] hookRuntime failed (idle detection may be less accurate):", err.message);
      }
    })();

    return runtimeHookPromise;
  };

  const waitForIdle = async (timeoutMs = 5000) => {
    await hookRuntime();

    const started = performance.now();
    const waitBody = () =>
      new Promise((resolve) => {
        if (document.body) return resolve();
        const onReady = () => {
          if (document.body) {
            document.removeEventListener("DOMContentLoaded", onReady);
            resolve();
          }
        };
        document.addEventListener("DOMContentLoaded", onReady);
        setTimeout(resolve, 250);
      });

    await waitBody();

    let lastMutation = performance.now();
    const observer = new MutationObserver(() => {
      lastMutation = performance.now();
    });

    observer.observe(document.body, {
      subtree: true,
      childList: true,
      characterData: true,
      attributes: true,
    });

    return await new Promise((resolve) => {
      const tick = () => {
        const now = performance.now();
        const waitedMs = Math.round(now - started);
        const computeIdle = computeDepth === 0 && now - lastCompute >= 200;
        if (waitedMs >= timeoutMs) {
          observer.disconnect();
          resolve({ waited_ms: waitedMs, timeout: true });
          return;
        }
        if (computeIdle && now - lastMutation >= 200) {
          observer.disconnect();
          resolve({ waited_ms: waitedMs, timeout: false });
          return;
        }
        setTimeout(tick, 16);
      };

      tick();
    });
  };

  const listCells = async (timeoutMs = 5000) => {
    await waitForIdle(timeoutMs);
    return Object.keys(window.__exposed || {});
  };

  const getCellValue = async (name, timeoutMs = 5000) => {
    await waitForIdle(timeoutMs);
    const exposed = window.__exposed;
    if (!exposed || typeof exposed !== "object") return null;
    return exposed[name];
  };

  const evalAndPost = async (port, id, code) => {
      const payload = { id, ok: true, value: null };
    try {
      const fn = new Function("return (async () => {\n" + code + "\n})();");
      const value = await fn();
      payload.value = toJsonSafe(value);
    } catch (err) {
      payload.ok = false;
      payload.error = String(err);
    }

    try {
      await postJson(port, "/_internal/reply", payload);
    } catch (err) {
      // Best-effort: don't throw if the API is restarting.
      console.warn("[notebook-viewer] evalAndPost: failed to post reply:", err.message);
    }
  };

  const waitIdleAndPost = async (port, id, timeoutMs) => {
    const payload = { id, ok: true, value: null };
    try {
      payload.value = await waitForIdle(timeoutMs);
    } catch (err) {
      payload.ok = false;
      payload.error = String(err);
    }

    try {
      await postJson(port, "/_internal/reply", payload);
    } catch (err) {
      console.warn("[notebook-viewer] waitIdleAndPost: failed to post reply:", err.message);
    }
  };

  // Input manipulation
  const setInputValue = (selector, value) => {
    const el = document.querySelector(selector);
    if (!el) {
      throw new Error(`selector not found: ${selector}`);
    }

    // Handle different input types
    if (el.tagName === "INPUT") {
      const inputType = el.type?.toLowerCase();
      if (inputType === "range" || inputType === "number") {
        el.value = value;
        el.dispatchEvent(new Event("input", { bubbles: true }));
        el.dispatchEvent(new Event("change", { bubbles: true }));
      } else if (inputType === "checkbox") {
        el.checked = Boolean(value);
        el.dispatchEvent(new Event("change", { bubbles: true }));
      } else {
        el.value = value;
        el.dispatchEvent(new Event("input", { bubbles: true }));
        el.dispatchEvent(new Event("change", { bubbles: true }));
      }
    } else if (el.tagName === "SELECT") {
      el.value = value;
      el.dispatchEvent(new Event("change", { bubbles: true }));
    } else if (el.tagName === "TEXTAREA") {
      el.value = value;
      el.dispatchEvent(new Event("input", { bubbles: true }));
    } else {
      // Try setting value anyway
      if ("value" in el) {
        el.value = value;
        el.dispatchEvent(new Event("input", { bubbles: true }));
        el.dispatchEvent(new Event("change", { bubbles: true }));
      } else {
        throw new Error(`element does not support value setting: ${el.tagName}`);
      }
    }
    return true;
  };

  const clickElement = (selector) => {
    const el = document.querySelector(selector);
    if (!el) {
      throw new Error(`selector not found: ${selector}`);
    }
    el.click();
    return true;
  };

  /**
   * Auto-discover visualizations in the page.
   * Finds SVGs, canvases, and Observable Plot elements that are large enough
   * to be meaningful charts (not icons). No notebook modifications required.
   */
  const discoverVisualizations = () => {
    const MIN_SIZE = 100;
    const results = [];

    // Selectors for chart-like elements
    const selectors = [
      'svg',
      'canvas',
      '.observablehq-plot',
      '.plot',
      '[class*="chart"]',
      '[class*="Chart"]'
    ];

    const seen = new Set();
    const allMatches = [];

    // First pass: collect all valid visualizations
    for (const selector of selectors) {
      for (const el of document.querySelectorAll(selector)) {
        if (seen.has(el)) continue;

        const rect = el.getBoundingClientRect();
        if (rect.width < MIN_SIZE || rect.height < MIN_SIZE) continue;
        if (rect.width === 0 || rect.height === 0) continue;
        if (getComputedStyle(el).display === 'none') continue;

        seen.add(el);
        allMatches.push({ el, rect });
      }
    }

    // Sort by document position (top to bottom)
    allMatches.sort((a, b) => {
      const aTop = window.scrollY + a.rect.top;
      const bTop = window.scrollY + b.rect.top;
      return aTop - bTop;
    });

    // Second pass: build results with unique selectors
    // We'll add a temporary data attribute for reliable selection
    for (const { el, rect } of allMatches) {
      const tag = el.tagName.toLowerCase();
      const vizId = `__viz_${results.length}`;

      // Add temporary data attribute for reliable selection
      el.setAttribute('data-viz-id', vizId);

      let uniqueSelector;
      if (el.id) {
        uniqueSelector = `#${el.id}`;
      } else {
        uniqueSelector = `[data-viz-id="${vizId}"]`;
      }

      const contextText = extractContext(el);

      results.push({
        index: results.length,
        type: tag,
        selector: uniqueSelector,
        rect: {
          x: rect.x,
          y: rect.y,
          width: rect.width,
          height: rect.height
        },
        scrollY: window.scrollY + rect.top,
        contextText
      });
    }

    return results;
  };

  /**
   * Extract preceding markdown/text context for a visualization.
   */
  const extractContext = (el) => {
    const texts = [];
    let node = el.previousElementSibling;
    let count = 0;
    const MAX_SIBLINGS = 3;

    while (node && count < MAX_SIBLINGS) {
      // Look for text-heavy elements (paragraphs, headings, lists)
      if (['P', 'H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'UL', 'OL', 'BLOCKQUOTE'].includes(node.tagName)) {
        const text = node.textContent?.trim();
        if (text && text.length > 10) {
          texts.unshift(text);
        }
      }
      node = node.previousElementSibling;
      count++;
    }

    return texts.join('\n\n') || null;
  };

  window.__notebook_viewer__ = {
    clearLogs,
    clickElement,
    discoverVisualizations,
    evalAndPost,
    getCellValue,
    getLogs,
    hookRuntime,
    listCells,
    setInputValue,
    toJsonSafe,
    waitForIdle,
    waitIdleAndPost,
  };
})();

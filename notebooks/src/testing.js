import { expose } from "./bridge.js";

// A simple test runner for Observable Framework notebooks
// Usage:
//   const { test, view, stats } = createSuite("Kelly");
//   test("Even money bet", (expect) => {
//     expect(kellyBet(0.6, 1)).toBeCloseTo(0.20, 2);
//   });
//   display(view());  // Render test results (recommended for debugging)

// FT Paper colors
const colors = {
  positive: "#2d724f",
  negative: "#b3312c",
  background: "#faf6f3"
};

export function createSuite(name) {
  // Simple state (not reactive - tests run once during cell execution)
  const results = [];
  let statsObj = { total: 0, passed: 0, failed: 0 };

  function updateStats() {
    statsObj = {
      total: results.length,
      passed: results.filter(t => t.passed).length,
      failed: results.filter(t => !t.passed).length
    };
    // Expose results to the bridge for automated verification
    try {
      expose({ [`test_suite_${name}`]: statsObj });
    } catch (e) {
      // May fail in non-browser environments (SSR, Node.js tests, etc.)
      console.error("Bridge exposure failed:", e);
    }
  }

  // Current test name for better error messages
  let currentTestName = "";

  const expect = (actual) => ({
    // Strict equality (===). For objects/arrays, use toEqual instead.
    toBe: (expected) => {
      const passed = actual === expected;
      results.push({
        test: currentTestName,
        assertion: "toBe",
        expected,
        actual,
        passed
      });
      updateStats();
      return passed;
    },
    // Deep equality for objects/arrays using JSON serialization.
    toEqual: (expected) => {
      let passed;
      try {
        passed = JSON.stringify(actual) === JSON.stringify(expected);
      } catch {
        passed = false;  // Non-serializable values
      }
      results.push({
        test: currentTestName,
        assertion: "toEqual",
        expected,
        actual,
        passed
      });
      updateStats();
      return passed;
    },
    // precision: number of decimal places. Values within 0.5 * 10^(-precision) are equal.
    // e.g., precision=2 means values within 0.005 pass. Note: Jest uses 10^(-precision) (2x looser).
    toBeCloseTo: (expected, precision = 2) => {
      const diff = Math.abs(actual - expected);
      const passed = diff < Math.pow(10, -precision) / 2;
      results.push({
        test: currentTestName,
        assertion: `toBeCloseTo(${precision})`,
        expected,
        actual,
        diff,
        passed
      });
      updateStats();
      return passed;
    },
    toBeTruthy: () => {
      const passed = !!actual;
      results.push({
        test: currentTestName,
        assertion: "toBeTruthy",
        expected: "truthy",
        actual,
        passed
      });
      updateStats();
      return passed;
    },
    toBeGreaterThan: (expected) => {
      const passed = actual > expected;
      results.push({
        test: currentTestName,
        assertion: "toBeGreaterThan",
        expected,
        actual,
        passed
      });
      updateStats();
      return passed;
    },
    toBeLessThan: (expected) => {
      const passed = actual < expected;
      results.push({
        test: currentTestName,
        assertion: "toBeLessThan",
        expected,
        actual,
        passed
      });
      updateStats();
      return passed;
    },
    toBeInRange: (min, max) => {
      const passed = actual >= min && actual <= max;
      results.push({
        test: currentTestName,
        assertion: `toBeInRange(${min}, ${max})`,
        expected: `${min} ≤ x ≤ ${max}`,
        actual,
        passed
      });
      updateStats();
      return passed;
    }
  });

  const test = (desc, fn) => {
    currentTestName = desc;
    try {
      fn(expect);
    } catch (e) {
      // Log full error with stack for debugging
      console.error(`Test "${desc}" threw:`, e);
      results.push({
        test: desc,
        assertion: "execution",
        error: e.message,
        stack: e.stack,
        passed: false
      });
      updateStats();
    }
  };

  // UI Component to display results in the notebook
  const view = () => {
    const statusColor = statsObj.failed > 0 ? colors.negative : colors.positive;
    const statusText = statsObj.failed > 0 ? `${statsObj.failed} FAILED` : "ALL PASSED";

    // Build DOM imperatively
    const container = document.createElement("div");
    container.style.cssText = `
      font-family: system-ui;
      margin: 1rem 0;
      padding: 1rem;
      background: ${colors.background};
      border-radius: 8px;
      border-left: 4px solid ${statusColor};
    `;

    const header = document.createElement("div");
    header.style.cssText = `font-weight: bold; margin-bottom: 0.5rem; color: ${statusColor};`;
    header.textContent = `Test Suite: ${name} — ${statusText} (${statsObj.passed}/${statsObj.total})`;
    container.appendChild(header);

    if (results.length === 0) {
      const empty = document.createElement("div");
      empty.style.color = "#666";
      empty.textContent = "No tests run yet";
      container.appendChild(empty);
    } else {
      const table = document.createElement("table");
      table.style.cssText = "width: 100%; border-collapse: collapse; font-size: 0.9rem;";

      // Header
      const thead = document.createElement("thead");
      thead.innerHTML = `
        <tr style="border-bottom: 1px solid #ccc;">
          <th style="text-align: left; padding: 4px;">Test</th>
          <th style="text-align: left; padding: 4px;">Expected</th>
          <th style="text-align: left; padding: 4px;">Actual</th>
          <th style="text-align: center; padding: 4px;">Result</th>
        </tr>
      `;
      table.appendChild(thead);

      // Body
      const tbody = document.createElement("tbody");
      results.forEach(t => {
        const row = document.createElement("tr");
        row.style.borderBottom = "1px solid #eee";
        row.innerHTML = `
          <td style="padding: 4px;">${t.test}</td>
          <td style="padding: 4px; font-family: monospace;">${t.error || String(t.expected)}</td>
          <td style="padding: 4px; font-family: monospace;">${t.error ? "—" : String(t.actual)}</td>
          <td style="padding: 4px; text-align: center; color: ${t.passed ? colors.positive : colors.negative};">
            ${t.passed ? "✓" : "✗"}
          </td>
        `;
        tbody.appendChild(row);
      });
      table.appendChild(tbody);
      container.appendChild(table);
    }

    return container;
  };

  // Return stats as a getter function, returns a copy to prevent external mutation
  const stats = () => ({ ...statsObj });

  // Return results as a getter to prevent external mutation
  const getResults = () => [...results];

  return { test, view, stats, results: getResults };
}

/**
 * Helper for exposing Observable cell values to the notebook viewer.
 *
 * Usage:
 *   import { expose } from "./bridge.js";
 *   expose({ meanY, pointCount });
 *
 * Values are merged into window.__exposed and a custom event is dispatched
 * to notify the viewer of changes.
 */
export function expose(values) {
  window.__exposed = { ...window.__exposed, ...values };
  window.dispatchEvent(
    new CustomEvent("notebook-exposed", { detail: values })
  );
}

// Track which values have been seen before (serialized form)
const _tracked = new Map();

/**
 * Like expose(), but only triggers updates when values actually change.
 * Useful in reactive cells that re-run frequently.
 *
 * Usage:
 *   import { track } from "./bridge.js";
 *   track({ meanY, pointCount });  // Only exposes when values differ
 *
 * Returns the values object for chaining.
 */
export function track(values) {
  const changes = {};
  let hasChanges = false;

  for (const [key, value] of Object.entries(values)) {
    let serialized;
    try {
      serialized = JSON.stringify(value);
    } catch {
      // Not JSON-serializable, use a unique symbol each time to force update
      serialized = Symbol();
    }

    const prev = _tracked.get(key);
    if (prev !== serialized) {
      _tracked.set(key, serialized);
      changes[key] = value;
      hasChanges = true;
    }
  }

  if (hasChanges) {
    expose(changes);
  }

  return values;
}

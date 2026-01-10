export default {
  root: "src",
  title: "Notebook Viewer",
  theme: "parchment",
  head: `
<script>
// In hidden/offscreen WKWebViews, requestAnimationFrame can exist but never fire,
// which stalls Observable's runtime scheduler. Force a timer-based rAF so
// notebooks compute reliably in "Jeeves" mode.
(() => {
  let nextId = 1;
  const timers = new Map();
  window.requestAnimationFrame = (cb) => {
    const id = nextId++;
    const t = setTimeout(() => {
      timers.delete(id);
      cb(performance.now());
    }, 0);
    timers.set(id, t);
    return id;
  };
  window.cancelAnimationFrame = (id) => {
    const t = timers.get(id);
    if (t !== undefined) {
      clearTimeout(t);
      timers.delete(id);
    }
  };
})();
</script>
`,
  sidebar: false  // Hide for screenshot use
};

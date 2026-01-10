---
url: "https://observablehq.com/plot/features/accessibility"
title: "Accessibility | Plot"
---

# Accessibility [​](https://observablehq.com/plot/features/accessibility\#accessibility)

Plot uses [ARIA](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA) to make plots more **accessible** through assistive technology such as screen readers, browser add-ons, and browser developer tools.

The [aria-label](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Attributes/aria-label) and [aria-description](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Attributes/aria-description) attributes on the root SVG element can be set via the top-level **ariaLabel** and **ariaDescription** [plot options](https://observablehq.com/plot/features/plots). These default to null.

[Marks](https://observablehq.com/plot/features/marks) automatically generate an aria-label attribute on the rendered SVG G element; this attribute includes the mark’s type, such as “dot”. The [axis mark](https://observablehq.com/plot/marks/axis) and [grid mark](https://observablehq.com/plot/marks/grid) also include the associated scale’s name, such as “y-axis tick”, “y-axis label”, or “x-grid”.

Use the **ariaLabel** mark option to apply per-instance aria-label attributes ( _e.g._, on individual dots in a scatterplot), say for a short, human-readable textual representation of each displayed data point. Use the **ariaDescription** mark option for a longer description; this is applied to the mark’s G element. These options both default to null.

Setting the **ariaHidden** mark option to true hides the mark from the accessibility tree. This is useful for decorative or redundant marks (such as rules or lines between dots).

Pager

[Previous pageShorthand](https://observablehq.com/plot/features/shorthand)

[Next pageArea](https://observablehq.com/plot/marks/area)

[Home](https://observablehq.com/ "Home")

Resources

- [Forum](https://talk.observablehq.com/)
- [Slack](https://observablehq.com/slack/join)
- [Releases](https://github.com/observablehq/plot/releases)

Observable

- [Product](https://observablehq.com/product)
- [Plot](https://observablehq.com/plot)
- [Integrations](https://observablehq.com/data-integrations)
- [Pricing](https://observablehq.com/pricing)

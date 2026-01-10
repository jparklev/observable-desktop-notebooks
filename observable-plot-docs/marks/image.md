---
url: "https://observablehq.com/plot/marks/image"
title: "Image mark | Plot"
---

# Image mark [^0.3.0](https://github.com/observablehq/plot/releases/tag/v0.3.0 "added in v0.3.0") [​](https://observablehq.com/plot/marks/image\#image-mark)

The **image mark** draws images centered at the given position in **x** and **y**. It is often used to construct scatterplots in place of a [dot mark](https://observablehq.com/plot/marks/dot). For example, the chart below, based on one by [Robert Lesser](https://observablehq.com/@rlesser/when-presidents-fade-away), shows the favorability of U.S. presidents over time alongside their portraits.

−30−20−10+0+10+20+30+40+50+60+70↑ Net favorability (%)180018201840186018801900192019401960198020002020First inauguration date →George WashingtonJohn AdamsThomas JeffersonJames MadisonJames MonroeJohn Quincy AdamsAndrew JacksonMartin Van BurenWilliam Henry HarrisonJohn TylerJames K. PolkZachary TaylorMillard FillmoreFranklin PierceJames BuchananAbraham LincolnAndrew JohnsonUlysses S. GrantRutherford B. HayesJames A. GarfieldChester A. ArthurGrover ClevelandBenjamin HarrisonWilliam McKinleyTheodore RooseveltWilliam Howard TaftWoodrow WilsonWarren G. HardingCalvin CoolidgeHerbert HooverFranklin D. RooseveltHarry S. TrumanDwight D. EisenhowerJohn F. KennedyLyndon B. JohnsonRichard NixonGerald FordJimmy CarterRonald ReaganGeorge H. W. BushBill ClintonGeorge W. BushBarack ObamaDonald TrumpJoe Biden [Fork](https://observablehq.com/@observablehq/plot-image-scatterplot "Open on Observable")

js

```
Plot.plot({
  inset: 20,
  x: {label: "First inauguration date"},
  y: {grid: true, label: "Net favorability (%)", tickFormat: "+f"},
  marks: [\
    Plot.ruleY([0]),\
    Plot.image(presidents, {\
      x: "First Inauguration Date",\
      y: (d) => d["Very Favorable %"] + d["Somewhat Favorable %"] - d["Very Unfavorable %"] - d["Somewhat Unfavorable %"],\
      src: "Portrait URL",\
      width: 40,\
      title: "Name"\
    })\
  ]
})
```

Images are drawn in input order by default. This dataset is ordered chronologically, and hence above the more recent presidents are drawn on top. You can change the order with the [sort transform](https://observablehq.com/plot/transforms/sort).

With the **r** option, images will be clipped to circles of the given radius. Use the [**preserveAspectRatio** option](https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/preserveAspectRatio) to control which part of the image appears within the circle; below, we favor the top part of the image to show the presidential head.

+0+10+20+30+40+50+60+70+80+90↑ Any opinion (%)180018201840186018801900192019401960198020002020First inauguration date →George WashingtonJohn AdamsThomas JeffersonJames MadisonJames MonroeJohn Quincy AdamsAndrew JacksonMartin Van BurenWilliam Henry HarrisonJohn TylerJames K. PolkZachary TaylorMillard FillmoreFranklin PierceJames BuchananAbraham LincolnAndrew JohnsonUlysses S. GrantRutherford B. HayesJames A. GarfieldChester A. ArthurGrover ClevelandBenjamin HarrisonWilliam McKinleyTheodore RooseveltWilliam Howard TaftWoodrow WilsonWarren G. HardingCalvin CoolidgeHerbert HooverFranklin D. RooseveltHarry S. TrumanDwight D. EisenhowerJohn F. KennedyLyndon B. JohnsonRichard NixonGerald FordJimmy CarterRonald ReaganGeorge H. W. BushBill ClintonGeorge W. BushBarack ObamaDonald TrumpJoe Biden [Fork](https://observablehq.com/@observablehq/plot-image-medals "Open on Observable")

js

```
Plot.plot({
  x: {inset: 20, label: "First inauguration date"},
  y: {insetTop: 4, grid: true, label: "Any opinion (%)", tickFormat: "+f"},
  marks: [\
    Plot.ruleY([0]),\
    Plot.image(presidents, {\
      x: "First Inauguration Date",\
      y: (d) => d["Very Favorable %"] + d["Somewhat Favorable %"] + d["Very Unfavorable %"] + d["Somewhat Unfavorable %"],\
      src: "Portrait URL",\
      r: 20,\
      preserveAspectRatio: "xMidYMin slice",\
      title: "Name"\
    })\
  ]
})
```

TIP

You can also use the **r** channel as a size encoding, and the **rotate** channel, as with dots.

The **r** option works well with the [dodge transform](https://observablehq.com/plot/transforms/dodge) for an image beeswarm plot. This chart isn’t particularly interesting because new presidents are inaugurated at a fairly consistent rate, but at least it avoids overlapping portraits.

180018201840186018801900192019401960198020002020First Inauguration Date →George WashingtonJohn AdamsThomas JeffersonJames MadisonJames MonroeJohn Quincy AdamsAndrew JacksonMartin Van BurenWilliam Henry HarrisonJohn TylerJames K. PolkZachary TaylorMillard FillmoreFranklin PierceJames BuchananAbraham LincolnAndrew JohnsonUlysses S. GrantRutherford B. HayesJames A. GarfieldChester A. ArthurGrover ClevelandBenjamin HarrisonWilliam McKinleyTheodore RooseveltWilliam Howard TaftWoodrow WilsonWarren G. HardingCalvin CoolidgeHerbert HooverFranklin D. RooseveltHarry S. TrumanDwight D. EisenhowerJohn F. KennedyLyndon B. JohnsonRichard NixonGerald FordJimmy CarterRonald ReaganGeorge H. W. BushBill ClintonGeorge W. BushBarack ObamaDonald TrumpJoe Biden [Fork](https://observablehq.com/@observablehq/plot-image-dodge "Open on Observable")

js

```
Plot.plot({
  inset: 20,
  height: 280,
  marks: [\
    Plot.image(\
      presidents,\
      Plot.dodgeY({\
        x: "First Inauguration Date",\
        r: 20, // clip to a circle\
        preserveAspectRatio: "xMidYMin slice", // try not to clip heads\
        src: "Portrait URL",\
        title: "Name"\
      })\
    )\
  ]
})
```

The default size of an image is only 16×16 pixels. This may be acceptable if the image is a small glyph, such as a categorical symbol in a scatterplot. But often you will want to set **width**, **height**, or **r** to increase the image size.

0510152025303540455055↑ Unfavorable opinion (%)01020304050607080Favorable opinion (%) →George WashingtonJohn AdamsThomas JeffersonJames MadisonJames MonroeJohn Quincy AdamsAndrew JacksonMartin Van BurenWilliam Henry HarrisonJohn TylerJames K. PolkZachary TaylorMillard FillmoreFranklin PierceJames BuchananAbraham LincolnAndrew JohnsonUlysses S. GrantRutherford B. HayesJames A. GarfieldChester A. ArthurGrover ClevelandBenjamin HarrisonWilliam McKinleyTheodore RooseveltWilliam Howard TaftWoodrow WilsonWarren G. HardingCalvin CoolidgeHerbert HooverFranklin D. RooseveltHarry S. TrumanDwight D. EisenhowerJohn F. KennedyLyndon B. JohnsonRichard NixonGerald FordJimmy CarterRonald ReaganGeorge H. W. BushBill ClintonGeorge W. BushBarack ObamaDonald TrumpJoe Biden [Fork](https://observablehq.com/@observablehq/plot-image-scatterplot-2 "Open on Observable")

js

```
Plot.plot({
  aspectRatio: 1,
  grid: true,
  x: {label: "Favorable opinion (%)"},
  y: {label: "Unfavorable opinion (%)"},
  marks: [\
    Plot.ruleY([0]),\
    Plot.ruleX([0]),\
    Plot.image(presidents, {\
      x: (d) => d["Very Favorable %"] + d["Somewhat Favorable %"],\
      y: (d) => d["Very Unfavorable %"] + d["Somewhat Unfavorable %"],\
      src: "Portrait URL",\
      title: "Name"\
    })\
  ]
})
```

If — _for reasons_ — you want to style the plot with a background image, you can do that using the top-level **style** option rather than an image mark. Below, Kristen Gorman’s penguins dataset is visualized atop her photograph of sea ice near Palmer Station on the Antarctic peninsula, where she collected the measurements.

1415161718192021↑ culmen\_depth\_mm3540455055culmen\_length\_mm → [Fork](https://observablehq.com/@observablehq/plot-background-image "Open on Observable")

js

```
Plot.plot({
  margin: 30,
  inset: 10,
  grid: true,
  style: {
    padding: "10px",
    color: "black",
    background: "url(../sea-ice.jpg)",
    backgroundSize: "cover"
  },
  marks: [\
    Plot.frame(),\
    Plot.dot(penguins, {x: "culmen_length_mm", y: "culmen_depth_mm", fill: "white", stroke: "black"})\
  ]
})
```

## Image options [​](https://observablehq.com/plot/marks/image\#image-options)

The required **src** option specifies the URL (or relative path) of each image. If **src** is specified as a string that starts with a dot, slash, or URL protocol ( _e.g._, “https:”) it is assumed to be a constant; otherwise it is interpreted as a channel.

In addition to the [standard mark options](https://observablehq.com/plot/features/marks#mark-options), the following optional channels are supported:

- **x** \- the horizontal position; bound to the _x_ scale
- **y** \- the vertical position; bound to the _y_ scale
- **width** \- the image width (in pixels)
- **height** \- the image height (in pixels)
- **r** \- the image radius; bound to the _r_ scale [^0.6.6](https://github.com/observablehq/plot/releases/tag/v0.6.6 "added in v0.6.6")
- **rotate** \- the rotation angle in degrees clockwise [^0.6.6](https://github.com/observablehq/plot/releases/tag/v0.6.6 "added in v0.6.6")

If either of the **x** or **y** channels are not specified, the corresponding position is controlled by the **frameAnchor** option.

The **width** and **height** options default to 16 pixels (unless **r** is specified) and can be specified as either a channel or constant. When the width or height is specified as a number, it is interpreted as a constant; otherwise it is interpreted as a channel. Images with a nonpositive width or height are not drawn. If a **width** is specified but not a **height**, or vice versa, the one defaults to the other. Images do not support either a fill or a stroke.

The **r** option, if not null (the default), enables circular clipping; it may be specified as a constant in pixels or a channel. Use the **preserveAspectRatio** option to control which part of the image is clipped. Also defaults the **width** and **height** to twice the effective radius.

The following image-specific constant options are also supported:

- **frameAnchor** \- how to position the image within the frame; defaults to _middle_
- **preserveAspectRatio** \- the [aspect ratio](https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/preserveAspectRatio); defaults to _xMidYMid meet_
- **crossOrigin** \- the [cross-origin](https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/crossorigin) behavior
- **imageRendering** \- the [image-rendering attribute](https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/image-rendering); defaults to _auto_ (bilinear) [^0.6.4](https://github.com/observablehq/plot/releases/tag/v0.6.4 "added in v0.6.4")

To crop the image instead of scaling it to fit, set **preserveAspectRatio** to _xMidYMid slice_. The **imageRendering** option may be set to _pixelated_ to disable bilinear interpolation on enlarged images; however, note that this is not supported in WebKit.

Images are drawn in input order, with the last data drawn on top. If sorting is needed, say to mitigate overplotting, consider a [sort transform](https://observablehq.com/plot/transforms/sort).

## image( _data_, _options_) [​](https://observablehq.com/plot/marks/image\#image)

js

```
Plot.image(presidents, {x: "inauguration", y: "favorability", src: "portrait"})
```

Returns a new image with the given _data_ and _options_. If neither the **x** nor **y** nor **frameAnchor** options are specified, _data_ is assumed to be an array of pairs \[\[ _x₀_, _y₀_\], \[ _x₁_, _y₁_\], \[ _x₂_, _y₂_\], …\] such that **x** = \[ _x₀_, _x₁_, _x₂_, …\] and **y** = \[ _y₀_, _y₁_, _y₂_, …\].

Pager

[Previous pageHexgrid](https://observablehq.com/plot/marks/hexgrid)

[Next pageLine](https://observablehq.com/plot/marks/line)

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

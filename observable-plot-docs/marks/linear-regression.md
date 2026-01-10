---
url: "https://observablehq.com/plot/marks/linear-regression"
title: "Linear regression mark | Plot"
---

# Linear regression mark [^0.5.1](https://github.com/observablehq/plot/releases/tag/v0.5.1 "added in v0.5.1") [​](https://observablehq.com/plot/marks/linear-regression\#linear-regression-mark)

The **linear regression** mark draws [linear regression](https://en.wikipedia.org/wiki/Linear_regression) lines with confidence bands, representing the estimated linear relation of a dependent variable (typically **y**) on an independent variable (typically **x**). Below we can see that, in this example dataset at least, the weight of a car is a good linear predictor of its power.

6080100120140160180200220↑ power (hp)2,0002,5003,0003,5004,0004,5005,000weight (lb) → [Fork](https://observablehq.com/@observablehq/plot-cars-linear-regression "Open on Observable")

js

```
Plot.plot({
  marks: [\
    Plot.dot(cars, {x: "weight (lb)", y: "power (hp)"}),\
    Plot.linearRegressionY(cars, {x: "weight (lb)", y: "power (hp)", stroke: "red"})\
  ]
})
```

A linear model posits that _y_ is determined by an underlying affine function _y_ = _a_ ﹢ _b x_, where _a_ is a constant (intercept of the line on the _y_-axis when _x_ = 0) and _b_ is the slope. Given a set of points in **x** and **y**, the linear regression method returns the most likely parameters _a_ and _b_ for the linear model, as well as a confidence band showing the range where these parameters lie with a certain probability, called **ci** (for confidence interval), which defaults to 0.95.

INFO

The regression line is fit using the [least squares](https://en.wikipedia.org/wiki/Least_squares) approach. See Torben Jansen’s [“Linear regression with confidence bands”](https://observablehq.com/@toja/linear-regression-with-confidence-bands) and [this StatExchange question](https://stats.stackexchange.com/questions/101318/understanding-shape-and-calculation-of-confidence-bands-in-linear-regression) for details.

Use the slider below to build a linear model from a subset of the data with **m** points. As you can see, the model gives a line as soon as two points are available, and gets more refined and stable as the size of the subset increases.

Number of points (m): 0

6080100120140160180200220↑ power (hp)2,0002,5003,0003,5004,0004,5005,000weight (lb) → [Fork](https://observablehq.com/@observablehq/plot-linear-regression-confidence-band "Open on Observable")

js

```
Plot.plot({
  marks: [\
    Plot.dot(cars, {x: "weight (lb)", y: "power (hp)", fill: "currentColor", fillOpacity: 0.2}),\
    Plot.dot(cars.slice(0, m), {x: "weight (lb)", y: "power (hp)"}),\
    Plot.linearRegressionY(cars.slice(0, m), {x: "weight (lb)", y: "power (hp)", stroke: "red"})\
  ]
})
```

TIP

When operating on a subset of the data (the “training dataset”, in machine learning parlance), randomly shuffling the data can reduce bias.

This type of model is regularly criticized for pushing people to the wrong conclusions about their data when the actual underlying structure or process is nonlinear. For example, if you measure the relationship between culmen depth and length in a mixed population of penguins, it is positively correlated in each of the three species (bigger penguins with the longer culmens also tend to have the deeper ones); however, the Gentoo population has a smaller aspect ratio of depth against length, and the overall correlation across the three species is negative. This is called [Simpson’s paradox](https://en.wikipedia.org/wiki/Simpson%27s_paradox), and it applies to any data that contains underlying populations with different properties or outcomes.

AdelieChinstrapGentoo

1415161718192021↑ culmen\_depth\_mm3540455055culmen\_length\_mm → [Fork](https://observablehq.com/@observablehq/plot-linear-regression-simpson "Open on Observable")

js

```
Plot.plot({
  grid: true,
  color: {legend: true},
  marks: [\
    Plot.dot(penguins, {x: "culmen_length_mm", y: "culmen_depth_mm", fill: "species"}),\
    Plot.linearRegressionY(penguins, {x: "culmen_length_mm", y: "culmen_depth_mm", stroke: "species"}),\
    Plot.linearRegressionY(penguins, {x: "culmen_length_mm", y: "culmen_depth_mm"})\
  ]
})
```

Finally, note that regression is not a symmetric method: the model computed to express _y_ as a function of _x_ (linearRegressionY) doesn’t give the same result as the regression of _x_ as a function of _y_ (linearRegressionX) unless the points are all perfectly aligned. In the worst case, where the two variables are statistically independent, the linear regression of _y_ against _x_ is an horizontal line, whereas the linear regression of _x_ against _y_ is a vertical line.

6080100120140160180200220↑ power (hp)2,0002,5003,0003,5004,0004,5005,000weight (lb) → [Fork](https://observablehq.com/@observablehq/plot-linear-regression-is-not-symmetric "Open on Observable")

js

```
Plot.plot({
  marks: [\
    Plot.dot(cars, {x: "weight (lb)", y: "power (hp)", strokeOpacity: 0.5, r: 2}),\
    Plot.linearRegressionY(cars, {x: "weight (lb)", y: "power (hp)", stroke: "steelblue"}),\
    Plot.linearRegressionX(cars, {x: "weight (lb)", y: "power (hp)", stroke: "orange"})\
  ]
})
```

## Linear regression options [​](https://observablehq.com/plot/marks/linear-regression\#linear-regression-options)

The given _options_ are passed through to these underlying marks, with the exception of the following options:

- **stroke** \- the stroke color of the regression line; defaults to _currentColor_
- **fill** \- the fill color of the confidence band; defaults to the line’s _stroke_
- **fillOpacity** \- the fill opacity of the confidence band; defaults to 0.1
- **ci** \- the confidence interval in \[0, 1), or 0 to hide bands; defaults to 0.95\
- **precision** \- the distance (in pixels) between samples of the confidence band; defaults to 4\
\
Multiple regressions can be defined by specifying **z**, **fill**, or **stroke**.\
\
## linearRegressionX( _data_, _options_) [​](https://observablehq.com/plot/marks/linear-regression\#linearRegressionX)\
\
js\
\
```\
Plot.linearRegressionX(mtcars, {y: "wt", x: "hp"})\
```\
\
Returns a linear regression mark where **x** is the dependent variable and **y** is the independent variable. (This is the uncommon orientation.)\
\
## linearRegressionY( _data_, _options_) [​](https://observablehq.com/plot/marks/linear-regression\#linearRegressionY)\
\
js\
\
```\
Plot.linearRegressionY(mtcars, {x: "wt", y: "hp"})\
```\
\
Returns a linear regression mark where **y** is the dependent variable and **x** is the independent variable. (This is the common orientation.)\
\
Pager\
\
[Previous pageLine](https://observablehq.com/plot/marks/line)\
\
[Next pageLink](https://observablehq.com/plot/marks/link)\
\
[Home](https://observablehq.com/ "Home")\
\
Resources\
\
- [Forum](https://talk.observablehq.com/)\
- [Slack](https://observablehq.com/slack/join)\
- [Releases](https://github.com/observablehq/plot/releases)\
\
Observable\
\
- [Product](https://observablehq.com/product)\
- [Plot](https://observablehq.com/plot)\
- [Integrations](https://observablehq.com/data-integrations)\
- [Pricing](https://observablehq.com/pricing)\
\

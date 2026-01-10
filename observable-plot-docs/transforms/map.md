---
url: "https://observablehq.com/plot/transforms/map"
title: "Map transform | Plot"
---

# Map transform [​](https://observablehq.com/plot/transforms/map\#map-transform)

The **map transform** groups data into series and then transforms each series’ values, say to normalize them relative to some basis or to apply a moving average. For example, below the map transform computes a cumulative sum ( _cumsum_) of a series of random numbers sampled from a normal distribution — in other words, a random walk.

−8−6−4−2024681012141618200100200300400500 [Fork](https://observablehq.com/@observablehq/plot-random-walk-cumsum-map "Open on Observable")

js

```
Plot.plot({
  marks: [\
    Plot.ruleY([0]),\
    Plot.lineY({length: 600}, Plot.mapY("cumsum", {y: d3.randomNormal()}))\
  ]
})
```

As another example, we can map the daily trading volume of Apple stock to a [_p_-quantile](https://en.wikipedia.org/wiki/Quantile) in \[0, 1\] using the _quantile_ map method, where 0 represents the minimum daily trade volume and 1 represents the maximum, and then apply a 30-day rolling mean with the [window transform](https://observablehq.com/plot/transforms/window) to smooth out the noise.

0.00.10.20.30.40.50.60.70.80.91.0↑ Volume20142015201620172018 [Fork](https://observablehq.com/@observablehq/plot-quantile-map-transform "Open on Observable")

js

```
Plot.plot({
  marks: [\
    Plot.ruleY([0, 1]),\
    Plot.lineY(aapl, Plot.mapY("quantile", {x: "Date", y: "Volume", strokeOpacity: 0.2})),\
    Plot.lineY(aapl, Plot.windowY(30, Plot.mapY("quantile", {x: "Date", y: "Volume"})))\
  ]
})
```

The [mapY transform](https://observablehq.com/plot/transforms/map#mapY) above is shorthand for applying the given map method to all _y_ channels. There’s also a less-common [mapX transform](https://observablehq.com/plot/transforms/map#mapX) for _x_ channels.

The more explicit [map](https://observablehq.com/plot/transforms/map#map) transform lets you specify which channels to map, and what map method to use for each channel. Like the [group](https://observablehq.com/plot/transforms/group) and [bin](https://observablehq.com/plot/transforms/bin) transforms, it takes two arguments: an _outputs_ object that describes the output channels to compute, and an _options_ object that describes the input channels and additional options. So this:

js

```
Plot.mapY("cumsum", {y: d3.randomNormal()})
```

Is shorthand for this:

js

```
Plot.map({y: "cumsum"}, {y: d3.randomNormal()})
```

As a more practical example, we can use the map transform to construct [Bollinger bands](https://observablehq.com/plot/marks/bollinger), showing both the price and volatility of Apple stock.

Window size (n):20Radius (k):2

60708090100110120130140150160170180190↑ Close20142015201620172018 [Fork](https://observablehq.com/@observablehq/plot-bollinger-band "Open on Observable")

js

```
Plot.plot({
  y: {
    grid: true
  },
  marks: [\
    Plot.areaY(aapl, Plot.map({y1: Plot.bollinger({n, k: -k}), y2: Plot.bollinger({n, k})}, {x: "Date", y: "Close", fillOpacity: 0.2})),\
    Plot.lineY(aapl, Plot.map({y: Plot.bollinger({n})}, {x: "Date", y: "Close", stroke: "blue"})),\
    Plot.lineY(aapl, {x: "Date", y: "Close", strokeWidth: 1})\
  ]
})
```

The [bollinger map method](https://observablehq.com/plot/marks/bollinger#bollinger) is implemented atop the [window map method](https://observablehq.com/plot/transforms/window#window), computing the mean of values within the rolling window, and then offsetting the mean by a multiple of the rolling deviation.

The map transform is akin to running [_array_.map](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/map) on the input channel’s values with the given map method. However, the map transform is series-aware: the data are first grouped into series using the **z**, **fill**, or **stroke** channel in the same fashion as the [area](https://observablehq.com/plot/marks/area) and [line](https://observablehq.com/plot/marks/line) marks so that series are processed independently.

## Map options [​](https://observablehq.com/plot/transforms/map\#map-options)

The following map methods are supported:

- _cumsum_ \- a cumulative sum
- _rank_ \- the rank of each value in the sorted array
- _quantile_ \- the rank, normalized between 0 and 1
- a function to be passed an array of values, returning new values
- a function to be passed an index and array of channel values, returning new values
- an object that implements the _mapIndex_ method

If a function is used, it must return an array of the same length as the given input. If a _mapIndex_ method is used, it is repeatedly passed the index for each series (an array of integers), the corresponding input channel’s array of values, and the output channel’s array of values; it must populate the slots specified by the index in the output array.

## map( _outputs_, _options_) [​](https://observablehq.com/plot/transforms/map\#map)

js

```
Plot.map({y: "cumsum"}, {y: d3.randomNormal()})
```

Groups on the first channel of **z**, **fill**, or **stroke**, if any, and then for each channel declared in the specified _outputs_ object, applies the corresponding map method. Each channel in _outputs_ must have a corresponding input channel in _options_.

## mapX( _map_, _options_) [​](https://observablehq.com/plot/transforms/map\#mapX)

js

```
Plot.mapX("cumsum", {x: d3.randomNormal()})
```

Equivalent to Plot.map({x: _map_, x1: _map_, x2: _map_}, _options_), but ignores any of **x**, **x1**, and **x2** not present in _options_. In addition, if none of **x**, **x1**, or **x2** are specified, then **x** defaults to [identity](https://observablehq.com/plot/features/transforms#identity).

## mapY( _map_, _options_) [​](https://observablehq.com/plot/transforms/map\#mapY)

js

```
Plot.mapY("cumsum", {y: d3.randomNormal()})
```

Equivalent to Plot.map({y: _map_, y1: _map_, y2: _map_}, _options_), but ignores any of **y**, **y1**, and **y2** not present in _options_. In addition, if none of **y**, **y1**, or **y2** are specified, then **y** defaults to [identity](https://observablehq.com/plot/features/transforms#identity).

Pager

[Previous pageInterval](https://observablehq.com/plot/transforms/interval)

[Next pageNormalize](https://observablehq.com/plot/transforms/normalize)

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

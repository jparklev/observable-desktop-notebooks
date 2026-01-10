---
url: "https://observablehq.com/framework/lib/mapbox-gl"
title: "Mapbox GL JS | Observable Framework"
---

# [Mapbox GL JS](https://observablehq.com/framework/lib/mapbox-gl\#mapbox-gl-js)

[Mapbox GL JS](https://docs.mapbox.com/mapbox-gl-js/guides/) is a library for building web maps and web applications with Mapbox’s modern mapping technology. Mapbox GL JS is available by default as `mapboxgl` in Markdown, but you can import it explicitly like so:

```js
import mapboxgl from "npm:mapbox-gl";
```

If you import Mapbox GL JS, its stylesheet will automatically be added to the page.

To create a map, create a container element with the desired dimensions, then call the `Map` constructor:

[© Mapbox](https://www.mapbox.com/about/maps) [© OpenStreetMap](https://www.openstreetmap.org/copyright/) [Improve this map](https://apps.mapbox.com/feedback/?access_token=pk.eyJ1Ijoib2JzZXJ2YWJsZWhxLWVuZy1hZG1pbiIsImEiOiJjbHMxaTBwdDkwYnRsMmpxeG12M2kzdWFvIn0.Ga6eIWP2YNQrEW4FzHRcTQ#/2.2932/48.86069/15.1/-20/62)

[Mapbox homepage](https://www.mapbox.com/)

```js
const div = display(document.createElement("div"));
div.style = "height: 400px;";

const map = new mapboxgl.Map({
  container: div,
  accessToken: ACCESS_TOKEN, // replace with your token, "pk.…"
  center: [2.2932, 48.86069], // starting position [longitude, latitude]
  zoom: 15.1,
  pitch: 62,
  bearing: -20
});

invalidation.then(() => map.remove());
```

You will need to create a [Mapbox account](https://account.mapbox.com/) and obtain an API access token. Replace `ACCESS_TOKEN` with your token above.

For inspiration, see Mapbox’s [examples page](https://docs.mapbox.com/mapbox-gl-js/example/).

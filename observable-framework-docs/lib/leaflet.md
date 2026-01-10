---
url: "https://observablehq.com/framework/lib/leaflet"
title: "Leaflet | Observable Framework"
---

# [Leaflet](https://observablehq.com/framework/lib/leaflet\#leaflet)

[Leaflet](https://leafletjs.com/) is an “open-source JavaScript library for mobile-friendly interactive maps.” Leaflet is available by default as `L` in Observable markdown. You can import it explicitly like so:

```js
import * as L from "npm:leaflet";
```

If you import Leaflet, Leaflet’s stylesheet will automatically be added to the page.

To create a map, follow the [tutorial](https://leafletjs.com/examples/quick-start/):

![](https://tile.openstreetmap.org/13/4093/2723.png)![](https://tile.openstreetmap.org/13/4094/2723.png)![](https://tile.openstreetmap.org/13/4093/2724.png)![](https://tile.openstreetmap.org/13/4094/2724.png)![](https://tile.openstreetmap.org/13/4092/2723.png)![](https://tile.openstreetmap.org/13/4095/2723.png)![](https://tile.openstreetmap.org/13/4092/2724.png)![](https://tile.openstreetmap.org/13/4095/2724.png)![](https://tile.openstreetmap.org/13/4091/2723.png)![](https://tile.openstreetmap.org/13/4096/2723.png)![](https://tile.openstreetmap.org/13/4091/2724.png)![](https://tile.openstreetmap.org/13/4096/2724.png)![](https://tile.openstreetmap.org/13/4090/2723.png)![](https://tile.openstreetmap.org/13/4097/2723.png)![](https://tile.openstreetmap.org/13/4090/2724.png)![](https://tile.openstreetmap.org/13/4097/2724.png)

![](https://observablehq.com/framework/_npm/leaflet@1.9.4/distmarker-shadow.png)

![Marker](https://observablehq.com/framework/_npm/leaflet@1.9.4/distmarker-icon.png)

A nice popup

indicating a point of interest.

[×](https://observablehq.com/framework/lib/leaflet#close)

[+](https://observablehq.com/framework/lib/leaflet# "Zoom in") [−](https://observablehq.com/framework/lib/leaflet# "Zoom out")

[Leaflet](https://leafletjs.com/ "A JavaScript library for interactive maps") \| © [OpenStreetMap](https://www.openstreetmap.org/copyright)

```js
const div = display(document.createElement("div"));
div.style = "height: 400px;";

const map = L.map(div)
  .setView([51.505, -0.09], 13);

L.tileLayer("https://tile.openstreetmap.org/{z}/{x}/{y}.png", {
  attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>'
})
  .addTo(map);

L.marker([51.5, -0.09])
  .addTo(map)
  .bindPopup("A nice popup<br> indicating a point of interest.")
  .openPopup();
```

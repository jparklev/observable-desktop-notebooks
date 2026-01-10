---
url: "https://observablehq.com/@observablehq/plot-impact-of-vaccines"
title: "The impact of vaccines"
---

# The impact of vaccines

A recreation of [a WSJ graphic](http://graphics.wsj.com/infectious-diseases-and-vaccines/) by Tynan DeBold and Dov Friedman.

```js
viewof disease = Inputs.select(vaccines.map(d => d.disease), {unique: true, label: "Disease"})
```

```js
Plot.plot({
  width,
  height: 930,
  marginBottom: 30,
  padding: 0,
  round: false,
  label: null,
  x: {axis: "top"},
  color: {
    scheme: "purd",
    legend: true,
    type: "sqrt",
    label: "Cases per 100,000 people"
  },
  marks: [
    Plot.barX(vaccines.filter(d => d.disease === disease), {
      x: "date",
      y: "state",
      interval: "year",
      inset: 0.5,
      fill: "cases",
      title: "cases"
    }),
    Plot.ruleX([introductions.find(d => d.disease === disease)], {
      x: "date"
    }),
    Plot.text([introductions.find(d => d.disease === disease)], {
      x: "date",
      dy: 4,
      lineAnchor: "top",
      frameAnchor: "bottom",
      text: (d) => `${d.date.getUTCFullYear()}\nVaccine introduced`
    })
  ]
})
```

```js
vaccines = {
  const vaccines = await FileAttachment("vaccines.json").json();
  return vaccines
    .flatMap(({title: disease, data: {values: {data}}}) => data
    .map(([date, stateIndex, cases]) => ({
      disease, 
      date: new Date(`${date}-01-01`), 
      state: states[stateIndex], 
      cases
    })));
}
```

```js
introductions = {
  const vaccines = await FileAttachment("vaccines.json").json();
  return vaccines
    .map(({title: disease, data: {chart_options: {vaccine_year}}}) => ({
      disease,
      date: new Date(Date.UTC(vaccine_year, (vaccine_year % 1) * 12, 1))
    }));
}
```

```js
states = ["Alaska", "Ala.", "Ark.", "Ariz.", "Calif.", "Colo.", "Conn.", "D.C.", "Del.", "Fla.", "Ga.", "Hawaii", "Iowa", "Idaho", "Ill.", "Ind.", "Kan.", "Ky.", "La.", "Mass.", "Md.", "Maine", "Mich.", "Minn.", "Mo.", "Miss.", "Mont.", "N.C.", "N.D.", "Neb.", "N.H.", "N.J.", "N.M", "Nev.", "N.Y.", "Ohio", "Okla.", "Ore.", "Pa.", "R.I.", "S.C.", "S.D.", "Tenn.", "Texas", "Utah", "Va.", "Vt.", "Wash.", "Wis.", "W.Va.", "Wyo."]
```

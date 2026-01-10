---
url: "https://observablehq.com/plot/transforms/sort"
title: "Sort transform | Plot"
---

# Sort transform [​](https://observablehq.com/plot/transforms/sort\#sort-transform)

The **sort transform** sorts a mark’s index to change the effective order of data. The sort transform affects the order in which a mark’s graphical elements are drawn ( [z-order](https://en.wikipedia.org/wiki/Z-order)), which can have a dramatic effect when these elements overlap. For example, see the bubble map of U.S. county population below; when the null sort order is used for input order, many small dots are hidden underneath larger ones.

Sort by descending radius (r):

[Fork](https://observablehq.com/@observablehq/plot-dot-sort "Open on Observable")

js

```
Plot.plot({
  projection: "albers-usa",
  marks: [\
    Plot.geo(statemesh, {strokeOpacity: 0.4}),\
    Plot.dot(counties, Plot.geoCentroid({\
      r: (d) => d.properties.population,\
      fill: "currentColor",\
      stroke: "white",\
      strokeWidth: 1,\
      sort: sorted ? {channel: "-r"} : null\
    }))\
  ]
})
```

TIP

Dots are sorted by descending **r** by default, so you may not need the **sort** option.

The sort transform can be applied either via the **sort** [mark option](https://observablehq.com/plot/features/marks#mark-options), as above, or as an explicit [sort transform](https://observablehq.com/plot/transforms/sort#sort). The latter is generally only needed when composing multiple transforms, or to disambiguate the sort transform from imputed ordinal scale domains, _i.e._, [scale sorting](https://observablehq.com/plot/features/scales#sort-mark-option).

As another example, in the line chart of unemployment rates below, lines for metropolitan areas in Michigan (which saw exceptionally high unemployment following the [financial crisis of 2008](https://en.wikipedia.org/wiki/2007%E2%80%932008_financial_crisis), in part due to the [auto industry collapse](https://en.wikipedia.org/wiki/2008%E2%80%932010_automotive_industry_crisis)) are highlighted in red, and the **sort** option is used to draw them on top of other series.

0246810121416↑ Unemployment (%)2000200220042006200820102012 [Fork](https://observablehq.com/@observablehq/plot-multiple-line-highlight "Open on Observable")

js

```
Plot.plot({
  y: {
    grid: true,
    label: "Unemployment (%)"
  },
  color: {
    domain: [false, true],
    range: ["#ccc", "red"]
  },
  marks: [\
    Plot.ruleY([0]),\
    Plot.line(bls, {\
      x: "date",\
      y: "unemployment",\
      z: "division",\
      sort: (d) => /, MI /.test(d.division),\
      stroke: (d) => /, MI /.test(d.division)\
    })\
  ]
})
```

TIP

You could say `sort: {channel: "stroke"}` here to avoid repeating the test function.

The index order also affects the behavior of certain transforms such as [stack](https://observablehq.com/plot/transforms/stack) and [dodge](https://observablehq.com/plot/transforms/dodge).

Sort x order:  ascending descending

2,0002,5003,0003,5004,0004,5005,000weight (lb) →Datsun 1200Toyota CoronaToyota StarletHonda Civic 1300Toyota Corolla 1200Honda Civic CVCCHonda CivicFord FiestaHonda Civic CVCCRenault 5 GtlVolkswagen RabbitVolkswagen Model 111Renault Lecar DeluxeVolkswagen 1131 Deluxe SedanToyota Corolla 1200Vokswagen RabbitHonda Civic 1500 GLFiat 128Plymouth ChampDodge Colt Hatchback CustomVolkswagen Rabbit CustomVolkswagen RabbitVolkswagen RabbitVolkswagen Rabbit CustomDatsun F-10 HatchbackDatsun B210Volkswagen Super BeetlePlymouth CricketVolkswagen DasherHonda Civic (Auto)Honda CivicToyota Corolla TercelMazda GLC CustomDatsun 210Maxda GLC DeluxeVolkswagen Super Beetle 117Volkswagen Rabbit LMazda GLC 4Mazda GLC DeluxeSubaru DLVolkswagen Rabbit Custom DieselDatsun B-210Volkswagen SciroccoDatsun 310 GXFiat X1.9Datsun 710Datsun 310Datsun 210Mazda GLC Custom LChevrolet ChevetteFord Escort 4WHonda Accord CVCCFord PintoToyota TercelChevrolet ChevetteFiat 124BSubaruDatsun B210 GXPeugeot 304Dodge Colt M/MVolkswagen Rabbit C (Diesel)Toyota Corolla 1600 (Wagon)Fiat 128Datsun 210Mazda GLCChevrolet ChevetteOpel 1900Maxda RX-3Dodge ColtMercury Lynx LPlymouth Horizon MiserDodge Colt HardtopDatsun PL510Datsun PL510Fiat Strada CustomVolkswagen PickupHonda Accord LXVolkswagen RabbitSubaru DLPlymouth Horizon TC3Buick Opel Isuzu DeluxeChevrolet ChevetteToyota CorollaOpel MantaNissan Stanza XEChevrolet WoodyDodge Colt (Wagon)Toyota CorollaAudi 4000Renault 12 (Wagon)Volkswagen DasherVolkswagen JettaPlymouth HorizonRenault 12TLHonda AccordHonda PreludePlymouth Horizon 4Audi FoxMercury Capri 2000Opel 1900Volkswagen DasherFord Pinto RunaboutToyota CoronaDodge OmniBMW 2002Toyota CorollaFiat 124 TCVolkswagen Type 3Dodge ColtChevrolet Vega 2300Fiat 124 Sport CoupeToyota Corolla LiftbackToyota CorollaToyota Corona HardtopToyota CarinaDatsun 510 (Wagon)Honda AccordDodge RampageDatsun 510Opel MantaPlymouth Arrow GSFord PintoRenault 18IMazda RX-2 CoupeVolkswagen Dasher (Diesel)Toyota CorollaDodge Charger 2.2Toyota Corona Mark IISaab 99EDatsun 610Ford Escort 2HPlymouth ReliantSubaruChevrolet Cavalier 2-DoorFord Pinto (Wagon)Chevrolet VegaDatsun 200SXChevrolet Vega (Wagon)Chevrolet VegaMazda RX-7 GsAudi 100 LSDatsun 510 HatchbackFord PintoFiat 131Mercury Capri V6Honda CivicPlymouth ReliantTriumph TR7 CoupeToyouta Corona Mark II (Wagon)Volkswagen 411 (Wagon)Toyota Celica GT LiftbackDodge Aries SEChevrolet VegaMazda 626Datsun 710Pontiac PhoenixToyota CoronaFord PintoFord Capri IIPontiac J2000 Se HatchbackAudi 100 LSChrysler Lebaron MedallionFord MaverickPontiac AstroChevrolet CitationBMW 320iChevrolet CavalierDatsun 200SXDodge Aries Wagon (Wagon)Ford RangerAMC GremlinBuick SkylarkMazda 626Ford PintoChevrolet Cavalier WagonAMC GremlinSaab 99LEToyota Celica GTAMC Spirit DLBuick Skylark LimitedSaab 99LEPeugeot 504Chevrolet CitationAudi 100 LSOldsmobile Omega BroughamToyota CoronaToyota Corona LiftbackChevy S-10Ford Fairmont (Man)Mazda RX-4Chevrolet CitationPontiac PhoenixPontiac Sunbird CoupePlymouth SapporoFord Mustang II 2+2AMC HornetAMC GremlinFord Mustang GLSaab 99GLEDodge ColtSaab 900SToyota Mark IIDatsun 810Audi 5000Plymouth DusterFord Granada LOldsmobile Starfire SXFord Fairmont FuturaVolvo 144EAFord FairmontFord MaverickFord Fairmont 4Toyota CressidaAMC HornetPlymouth DusterFord Mustang CobraDatsun 280ZXAMC GremlinDatsun 810 MaximaToyota Mark IIVolvo 145E (Wagon)AMC HornetBuick Century LimitedVolvo 244DLAudi 5000S (Diesel)Chevrolet CamaroPeugeot 504AMC Hornet Sportabout (Wagon)Ford Fairmont (Auto)Peugeot 504 (Wagon)Ford PintoMercury Zephyr 6AMC ConcordFord MaverickOldsmobile Cutlass Ciera (Diesel)Ford MaverickAMC Concord DLBuick SkyhawkFord Granada GLMercury ZephyrAMC HornetBuick Estate Wagon (Wagon)Citroen DS-21 PallasPlymouth DusterPlymouth ValiantFord MustangVolvo 264GLVolvo 245Chevrolet MalibuFord MaverickVolvo DieselFord Mustang IIPeugeot 504AMC Pacer D/LFord FuturaAMC ConcordAMC PacerChevrolet Monza 2+2Peugeot 505S Turbo DieselPlymouth ValiantPontiac Lemans V6Mercedes-Benz 240DPlymouth Valiant CustomAMC Concord DL 6Peugeot 504Chevrolet Nova CustomPontiac FirebirdAMC MatadorFord Torino 500Chevrolet Chevelle MalibuChevrolet NovaChevrolet NovaFord Mustang Boss 302Dodge Aspen 6Oldsmobile Cutlass Salon BroughamBuick Century SpecialDodge AspenDodge Dart CustomAMC Concord DLPeugeot 604SLBuick CenturyOldsmobile Cutlass Salon BroughamBuick SkylarkChevrolet Monte Carlo LandauPlymouth VolareMercury MonarchAMC Rebel SSTPlymouth SatellitePlymouth Satellite CustomBuick Regal Sport Coupe (Turbo)Ford TorinoChevrolet NovaChrysler Lebaron SalonChevrolet Chevelle MalibuChevrolet ConcoursFord GranadaMercedes-Benz 300DPontiac Phoenix LJDodge Challenger SEMercury Monarch GhiaFord Granada GhiaChevrolet Malibu Classic (Wagon)Plymouth Barracuda 340Plymouth Satellite SebringDodge AspenPlymouth Volare CustomAMC MatadorPontiac Ventura SjDodge Aspen SEOldsmobile OmegaAMC Ambassador SSTAMC MatadorBuick Skylark 320Ford LTD LandauOldsmobile Cutlass LSAMC MatadorDodge DiplomatDodge D100Chevrolet Monte CarloDodge Coronet CustomChevrolet Chevelle Malibu ClassicPlymouth FuryMercedes-Benz 280SAMC Ambassador BroughamDodge St. RegisChevrolet Caprice ClassicAMC Ambassador DPLAMC Rebel SST (Wagon)Ford F108Chevrolet Caprice ClassicAMC Matador (Wagon)Chevroelt Chevelle MalibuCadillac EldoradoBuick CenturyChrysler Lebaron Town & Country (Wagon)Plymouth Volare Premier V8Mercury Grand MarquisAMC MatadorChevrolet MalibuFord Torino (Wagon)Ford Gran TorinoFord Country Squire (Wagon)Chevy C10Oldsmobile Cutlass SupremePlymouth Satellite Custom (Wagon)Dodge Magnum XEChevrolet Monte Carlo SPlymouth Fury IIIChevrolet Chevelle Concours (Wagon)Buick Century 350Ford Galaxie 500Plymouth Fury IIIDodge Monaco BroughamFord Gran TorinoChevrolet Chevelle Concours (Wagon)Ford Galaxie 500Chevrolet Monte Carlo LandauPlymouth Satellite (Wagon)Dodge Coronet BroughamChevrolet ImpalaChevrolet Chevelle Malibu ClassicFord Gran TorinoPontiac Grand Prix LjPlymouth Fury Gran SedanAMC Matador (Wagon)Chevrolet ImpalaPontiac Grand PrixFord Gran Torino (Wagon)Mercury Cougar BroughamPlymouth Fury IIIChrysler CordobaFord ThunderbirdFord Galaxie 500Chevrolet ImpalaBuick Estate Wagon (Wagon)Ford LTDChevy C20Cadillac SevilleDodge D200Pontiac CatalinaChrysler Newport RoyalPontiac CatalinaChevrolet Bel AirOldsmobile Delta 88 RoyaleDodge Coronet Custom (Wagon)Chevrolet Caprice ClassicPontiac Catalina BroughamPlymouth Grand FuryOldsmobile Vista CruiserBuick Lesabre CustomFord F250Mercury MarquisFord Gran Torino (Wagon)Plymouth Custom SuburbFord LTDPontiac CatalinaBuick Century Luxus (Wagon)Hi 1200DChrysler New Yorker BroughamFord Country Squire (Wagon)Ford CountryBuick Electra 225 CustomMercury Marquis BroughamDodge Monaco (Wagon)Chevrolet ImpalaPontiac Safari (Wagon) [Fork](https://observablehq.com/@observablehq/plot-dodge-cars-2 "Open on Observable")

js

```
Plot.plot({
  height: 180,
  marks: [\
    Plot.dotX(cars, Plot.dodgeY({\
      x: "weight (lb)",\
      title: "name",\
      fill: "currentColor",\
      sort: {channel: "x", order}\
    }))\
  ]
})
```

The closely-related [reverse transform](https://observablehq.com/plot/transforms/sort#reverse) likewise reverses the mark index, while the [shuffle transform](https://observablehq.com/plot/transforms/sort#shuffle) for randomizes the mark index’s order.

## sort( _order_, _options_) [​](https://observablehq.com/plot/transforms/sort\#sort)

js

```
Plot.sort("body_mass_g", {x: "culmen_length_mm", y: "culmen_depth_mm"})
```

Sorts the data by the specified _order_, which is one of:

- a comparator function, as with [_array_.sort](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/sort)
- an accessor function
- a field name
- a { _channel_, _order_} object

In the object case, the **channel** option specifies the name of the channel, while the **order** option specifies _ascending_ (the default) or _descending_ order. You can also use the shorthand _-name_ [^0.6.7](https://github.com/observablehq/plot/releases/tag/v0.6.7 "added in v0.6.7") to sort by descending order of the channel with the given _name_. For example, `sort: {channel: "-r"}` will sort by descending radius ( **r**).

In the function case, if the sort function does not take exactly one argument, it is interpreted as a comparator function; otherwise it is interpreted as an accessor function.

## shuffle( _options_) [​](https://observablehq.com/plot/transforms/sort\#shuffle)

js

```
Plot.shuffle({x: "culmen_length_mm", y: "culmen_depth_mm"})
```

Shuffles the data randomly. If a **seed** option is specified, a [linear congruential generator](https://d3js.org/d3-random#randomLcg) with the given seed is used to generate random numbers; otherwise, Math.random is used.

## reverse( _options_) [​](https://observablehq.com/plot/transforms/sort\#reverse)

js

```
Plot.reverse({x: "culmen_length_mm", y: "culmen_depth_mm"})
```

Reverses the order of the data.

Pager

[Previous pageShift](https://observablehq.com/plot/transforms/shift)

[Next pageStack](https://observablehq.com/plot/transforms/stack)

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

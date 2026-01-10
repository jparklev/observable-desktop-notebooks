---
url: "https://observablehq.com/plot/transforms/dodge"
title: "Dodge transform | Plot"
---

# Dodge transform [^0.5.0](https://github.com/observablehq/plot/releases/tag/v0.5.0 "added in v0.5.0") [​](https://observablehq.com/plot/transforms/dodge\#dodge-transform)

Given one position dimension (either **x** or **y**), the **dodge** transform computes the other position dimension such that dots are packed densely without overlapping. The [dodgeX transform](https://observablehq.com/plot/transforms/dodge#dodgeX) computes **x** (horizontal position) given **y** (vertical position), while the [dodgeY transform](https://observablehq.com/plot/transforms/dodge#dodgeY) computes **y** given **x**.

The dodge transform is commonly used to produce beeswarm 🐝 plots, a way of showing a one-dimensional distribution that preserves the visual identity of individual data points. For example, the dots below represent the weights of cars; the rough shape of the pile gives a sense of the overall distribution (peaking around 2,100 pounds), and you can hover an individual dot to see which car it represents.

2,0002,5003,0003,5004,0004,5005,000weight (lb) →AMC Ambassador BroughamAMC Ambassador DPLAMC Ambassador SSTAMC Concord DL 6AMC Concord DLAMC Concord DLAMC ConcordAMC ConcordAMC GremlinAMC GremlinAMC GremlinAMC GremlinAMC Hornet Sportabout (Wagon)AMC HornetAMC HornetAMC HornetAMC HornetAMC Matador (Wagon)AMC Matador (Wagon)AMC MatadorAMC MatadorAMC MatadorAMC MatadorAMC MatadorAMC Pacer D/LAMC PacerAMC Rebel SST (Wagon)AMC Rebel SSTAMC Spirit DLAudi 100 LSAudi 100 LSAudi 100 LSAudi 4000Audi 5000Audi 5000S (Diesel)Audi FoxBMW 2002BMW 320iBuick Century 350Buick Century LimitedBuick Century Luxus (Wagon)Buick Century SpecialBuick CenturyBuick CenturyBuick Electra 225 CustomBuick Estate Wagon (Wagon)Buick Estate Wagon (Wagon)Buick Lesabre CustomBuick Opel Isuzu DeluxeBuick Regal Sport Coupe (Turbo)Buick SkyhawkBuick Skylark 320Buick Skylark LimitedBuick SkylarkBuick SkylarkCadillac EldoradoCadillac SevilleChevroelt Chevelle MalibuChevrolet Bel AirChevrolet CamaroChevrolet Caprice ClassicChevrolet Caprice ClassicChevrolet Caprice ClassicChevrolet Cavalier 2-DoorChevrolet Cavalier WagonChevrolet CavalierChevrolet Chevelle Concours (Wagon)Chevrolet Chevelle Concours (Wagon)Chevrolet Chevelle Malibu ClassicChevrolet Chevelle Malibu ClassicChevrolet Chevelle MalibuChevrolet Chevelle MalibuChevrolet ChevetteChevrolet ChevetteChevrolet ChevetteChevrolet ChevetteChevrolet CitationChevrolet CitationChevrolet CitationChevrolet ConcoursChevrolet ImpalaChevrolet ImpalaChevrolet ImpalaChevrolet ImpalaChevrolet Malibu Classic (Wagon)Chevrolet MalibuChevrolet MalibuChevrolet Monte Carlo LandauChevrolet Monte Carlo LandauChevrolet Monte Carlo SChevrolet Monte CarloChevrolet Monza 2+2Chevrolet Nova CustomChevrolet NovaChevrolet NovaChevrolet NovaChevrolet Vega (Wagon)Chevrolet Vega 2300Chevrolet VegaChevrolet VegaChevrolet VegaChevrolet WoodyChevy C10Chevy C20Chevy S-10Chrysler CordobaChrysler Lebaron MedallionChrysler Lebaron SalonChrysler Lebaron Town & Country (Wagon)Chrysler New Yorker BroughamChrysler Newport RoyalCitroen DS-21 PallasDatsun 1200Datsun 200SXDatsun 200SXDatsun 210Datsun 210Datsun 210Datsun 280ZXDatsun 310 GXDatsun 310Datsun 510 (Wagon)Datsun 510 HatchbackDatsun 510Datsun 610Datsun 710Datsun 710Datsun 810 MaximaDatsun 810Datsun B-210Datsun B210 GXDatsun B210Datsun F-10 HatchbackDatsun PL510Datsun PL510Dodge Aries SEDodge Aries Wagon (Wagon)Dodge Aspen 6Dodge Aspen SEDodge AspenDodge AspenDodge Challenger SEDodge Charger 2.2Dodge Colt (Wagon)Dodge Colt HardtopDodge Colt Hatchback CustomDodge Colt M/MDodge ColtDodge ColtDodge ColtDodge Coronet BroughamDodge Coronet Custom (Wagon)Dodge Coronet CustomDodge D100Dodge D200Dodge Dart CustomDodge DiplomatDodge Magnum XEDodge Monaco (Wagon)Dodge Monaco BroughamDodge OmniDodge RampageDodge St. RegisFiat 124 Sport CoupeFiat 124 TCFiat 124BFiat 128Fiat 128Fiat 131Fiat Strada CustomFiat X1.9Ford Capri IIFord Country Squire (Wagon)Ford Country Squire (Wagon)Ford CountryFord Escort 2HFord Escort 4WFord F108Ford F250Ford Fairmont (Auto)Ford Fairmont (Man)Ford Fairmont 4Ford Fairmont FuturaFord FairmontFord FiestaFord FuturaFord Galaxie 500Ford Galaxie 500Ford Galaxie 500Ford Gran Torino (Wagon)Ford Gran Torino (Wagon)Ford Gran TorinoFord Gran TorinoFord Gran TorinoFord Granada GhiaFord Granada GLFord Granada LFord GranadaFord LTD LandauFord LTDFord LTDFord MaverickFord MaverickFord MaverickFord MaverickFord MaverickFord Mustang Boss 302Ford Mustang CobraFord Mustang GLFord Mustang II 2+2Ford Mustang IIFord MustangFord Pinto (Wagon)Ford Pinto RunaboutFord PintoFord PintoFord PintoFord PintoFord PintoFord PintoFord RangerFord ThunderbirdFord Torino (Wagon)Ford Torino 500Ford TorinoHi 1200DHonda Accord CVCCHonda Accord LXHonda AccordHonda AccordHonda Civic (Auto)Honda Civic 1300Honda Civic 1500 GLHonda Civic CVCCHonda Civic CVCCHonda CivicHonda CivicHonda CivicHonda PreludeMaxda GLC DeluxeMaxda RX-3Mazda 626Mazda 626Mazda GLC 4Mazda GLC Custom LMazda GLC CustomMazda GLC DeluxeMazda GLCMazda RX-2 CoupeMazda RX-4Mazda RX-7 GsMercedes-Benz 240DMercedes-Benz 280SMercedes-Benz 300DMercury Capri 2000Mercury Capri V6Mercury Cougar BroughamMercury Grand MarquisMercury Lynx LMercury Marquis BroughamMercury MarquisMercury Monarch GhiaMercury MonarchMercury Zephyr 6Mercury ZephyrNissan Stanza XEOldsmobile Cutlass Ciera (Diesel)Oldsmobile Cutlass LSOldsmobile Cutlass Salon BroughamOldsmobile Cutlass Salon BroughamOldsmobile Cutlass SupremeOldsmobile Delta 88 RoyaleOldsmobile Omega BroughamOldsmobile OmegaOldsmobile Starfire SXOldsmobile Vista CruiserOpel 1900Opel 1900Opel MantaOpel MantaPeugeot 304Peugeot 504 (Wagon)Peugeot 504Peugeot 504Peugeot 504Peugeot 504Peugeot 505S Turbo DieselPeugeot 604SLPlymouth Arrow GSPlymouth Barracuda 340Plymouth ChampPlymouth CricketPlymouth Custom SuburbPlymouth DusterPlymouth DusterPlymouth DusterPlymouth Fury Gran SedanPlymouth Fury IIIPlymouth Fury IIIPlymouth Fury IIIPlymouth FuryPlymouth Grand FuryPlymouth Horizon 4Plymouth Horizon MiserPlymouth Horizon TC3Plymouth HorizonPlymouth ReliantPlymouth ReliantPlymouth SapporoPlymouth Satellite (Wagon)Plymouth Satellite Custom (Wagon)Plymouth Satellite CustomPlymouth Satellite SebringPlymouth SatellitePlymouth Valiant CustomPlymouth ValiantPlymouth ValiantPlymouth Volare CustomPlymouth Volare Premier V8Plymouth VolarePontiac AstroPontiac Catalina BroughamPontiac CatalinaPontiac CatalinaPontiac CatalinaPontiac FirebirdPontiac Grand Prix LjPontiac Grand PrixPontiac J2000 Se HatchbackPontiac Lemans V6Pontiac Phoenix LJPontiac PhoenixPontiac PhoenixPontiac Safari (Wagon)Pontiac Sunbird CoupePontiac Ventura SjRenault 12 (Wagon)Renault 12TLRenault 18IRenault 5 GtlRenault Lecar DeluxeSaab 900SSaab 99ESaab 99GLESaab 99LESaab 99LESubaru DLSubaru DLSubaruSubaruToyota CarinaToyota Celica GT LiftbackToyota Celica GTToyota Corolla 1200Toyota Corolla 1200Toyota Corolla 1600 (Wagon)Toyota Corolla LiftbackToyota Corolla TercelToyota CorollaToyota CorollaToyota CorollaToyota CorollaToyota CorollaToyota Corona HardtopToyota Corona LiftbackToyota Corona Mark IIToyota CoronaToyota CoronaToyota CoronaToyota CoronaToyota CressidaToyota Mark IIToyota Mark IIToyota StarletToyota TercelToyouta Corona Mark II (Wagon)Triumph TR7 CoupeVokswagen RabbitVolkswagen 1131 Deluxe SedanVolkswagen 411 (Wagon)Volkswagen Dasher (Diesel)Volkswagen DasherVolkswagen DasherVolkswagen DasherVolkswagen JettaVolkswagen Model 111Volkswagen PickupVolkswagen Rabbit C (Diesel)Volkswagen Rabbit Custom DieselVolkswagen Rabbit CustomVolkswagen Rabbit CustomVolkswagen Rabbit LVolkswagen RabbitVolkswagen RabbitVolkswagen RabbitVolkswagen RabbitVolkswagen SciroccoVolkswagen Super Beetle 117Volkswagen Super BeetleVolkswagen Type 3Volvo 144EAVolvo 145E (Wagon)Volvo 244DLVolvo 245Volvo 264GLVolvo Diesel [Fork](https://observablehq.com/@observablehq/plot-dodge-cars "Open on Observable")

js

```
Plot.plot({
  height: 160,
  marks: [\
    Plot.dotX(cars, Plot.dodgeY({x: "weight (lb)", title: "name", fill: "currentColor"}))\
  ]
})
```

Compare this to a conventional histogram using a [rect mark](https://observablehq.com/plot/marks/rect).

020406080100↑ Frequency1,5002,0002,5003,0003,5004,0004,5005,0005,500weight (lb) → [Fork](https://observablehq.com/@observablehq/plot-dodge-cars "Open on Observable")

js

```
Plot.plot({
  height: 180,
  marks: [\
    Plot.rectY(cars, Plot.binX({y: "count"}, {x: "weight (lb)"})),\
    Plot.ruleY([0])\
  ]
})
```

The dodge transform works with Plot’s [faceting system](https://observablehq.com/plot/features/facets), allowing independent beeswarm plots on discrete partitions of the data. Below, penguins are grouped by species and colored by sex, while vertical↕︎ position ( **y**) encodes body mass.

FEMALEMALEnull

AdelieChinstrapGentoospecies3,0003,5004,0004,5005,0005,5006,000↑ body\_mass\_g [Fork](https://observablehq.com/@observablehq/plot-dodge-penguins "Open on Observable")

js

```
Plot.plot({
  y: {grid: true},
  color: {legend: true},
  marks: [\
    Plot.dot(penguins, Plot.dodgeX("middle", {fx: "species", y: "body_mass_g", fill: "sex"}))\
  ]
})
```

Beeswarm plots avoid the occlusion problem of dense scatterplots and barcode plots.

2,0002,5003,0003,5004,0004,5005,000weight (lb) → [Fork](https://observablehq.com/@observablehq/plot-dodge-cars "Open on Observable")

js

```
Plot.dotX(cars, {x: "weight (lb)"}).plot()
```

2,0002,5003,0003,5004,0004,5005,000weight (lb) → [Fork](https://observablehq.com/@observablehq/plot-dodge-cars "Open on Observable")

js

```
Plot.ruleX(cars, {x: "weight (lb)"}).plot()
```

The **anchor** option specifies the layout baseline: the optimal output position. For the dodgeX transform, the supported anchors are: _left_ (default), _middle_, _right_. For the dodgeY transform, the supported anchors are: _bottom_ (default), _middle_, _top_. When the _middle_ anchor is used, the dots are placed symmetrically around the baseline.

Anchor: topmiddlebottom

2,0002,5003,0003,5004,0004,5005,000weight (lb) → [Fork](https://observablehq.com/@observablehq/plot-dodge-cars "Open on Observable")

js

```
Plot.plot({
  height: 180,
  marks: [\
    Plot.dot(cars, Plot.dodgeY(anchor, {x: "weight (lb)", fill: "currentColor"}))\
  ]
})
```

When using dodgeY, you must typically specify the plot’s **height** to create suitable space for the layout. The dodge transform is not currently able to set the height automatically. For dodgeX, the default **width** of 640 is often sufficient, though you may need to adjust it as well depending on your data.

The dodge transform differs from the [stack transform](https://observablehq.com/plot/transforms/stack) in that the dots do not need the exact same input position to avoid overlap; the dodge transform respects the radius **r** of each dot. Try adjusting the radius below to see the effect.

Radius (r): 3.0

2,0002,5003,0003,5004,0004,5005,000weight (lb) → [Fork](https://observablehq.com/@observablehq/plot-variable-radius-dodge "Open on Observable")

js

```
Plot.plot({
  height: 180,
  marks: [\
    Plot.dot(cars, Plot.dodgeY({x: "weight (lb)", r, fill: "currentColor"}))\
  ]
})
```

The dodge transform also supports a **padding** option (default 1), which specifies the minimum separating distance between dots. Increase it for more breathing room.

Padding: 2.0

2,0002,5003,0003,5004,0004,5005,000weight (lb) → [Fork](https://observablehq.com/@observablehq/plot-variable-radius-dodge "Open on Observable")

js

```
Plot.plot({
  height: 180,
  marks: [\
    Plot.dot(cars, Plot.dodgeY({x: "weight (lb)", padding, fill: "currentColor"}))\
  ]
})
```

If **r** is a channel, the dodge transform will position circles of varying radius. The chart below shows twenty years of IPO offerings leading up to Facebook’s $104B offering in 2012; each circle is sized proportionally to the associated company’s valuation at IPO. (This data comes from [“The Facebook Offering: How It Compares”](https://archive.nytimes.com/www.nytimes.com/interactive/2012/05/17/business/dealbook/how-the-facebook-offering-compares.html?hp) by Jeremy Ashkenas, Matthew Bloch, Shan Carter, and Amanda Cox.) Facebook’s valuation was nearly four times that of Google, the previous record. The 2000 [dot-com bubble](https://en.wikipedia.org/wiki/Dot-com_bubble) is also visible.

1980198519901995200020052010Facebook
104.1BGoogle
27.7BCorvis Corp
15.6BInfonet Services Corp
13.2BGroupon
12.8BKPNQwest
12.4BMetroPCS Communications
8.7BYandex NV
8.0BEquant NV
7.3BZynga
7.0BWebVan Group
6.5BMcCaw Cellular Communications
4.8BClearwire Corp
4.4BSGS-Thomson Microelectronics
4.3BLinkedIn Corp
4.3BIridium World Communications
4.2BFlag Telecom Holdings Ltd
4.1BVerisk Analytics
4.1BONI Systems Corp
4.0BSycamore Networks
4.0BNorthPoint Communications Grp
3.9BOplink Communications
3.6BTeleport Communications Group
3.6BTransmeta Corp
3.5BAPPLE COMPUTER
3.4BICO Global Communications
3.4BHandspring
3.3BStoragenetworks
3.2BAkamai Technologies
3.2BSensata Tech Hldg NV
3.1BPriceline.com
3.1BCosine Communications
3.0BCIENA Corp
3.0BVonage Hldgs Corp
2.9BAvanex Corp
2.9BJD Edwards & Company
2.9BBoston Scientific
2.8BeToys
2.7BPandora Media
2.6BMP3.COM
2.5BPanAmSat
2.5BExcel Communications
2.3BJuniper Networks
2.3BTeleCorp PCS
2.3BDIASONICS, INC.
2.2BNetZero
2.2BBuy.com
2.2BFreemarkets
2.2BOnvia.com
2.2BNiku Corp
2.2BHomeAway
2.2BTelesystem International
2.1BCellcom Israel Ltd
2.1BDolby Laboratories
2.1BUTStarcom
2.1BTellium
2.1BOrganic
2.1BInternet Capital Group
2.0BRhythms NetConnections
2.0BGarmin Ltd
2.0BHomeGrocer.com
2.0BSilicon Laboratories
1.9BPerot Systems Corp
1.9BFoundry Networks
1.9BAvici Systems
1.9BSonus Networks
1.8BHomestore.com
1.8BBlue Martini Software
1.8BAvenue A
1.7B1-800-Flowers.com
1.7BGigamedia Ltd
1.7BBell Canada International
1.7BAt Home Corp
1.7Be Machines
1.7BInterNAP Network Services
1.7BNetSuite
1.7BGateway 2000
1.7BTELEVIDEO SYSTEMS
1.7BMarvell Technology Group Ltd
1.6BDivine Interventures
1.6BNetscape Communications
1.6BVA Linux Systems
1.6BIMPSAT Fiber Networks
1.6BSplunk
1.6BUniversal Access
1.6BExfo Electro Optical
1.6BNew Focus
1.5BArrowPoint Communications
1.5BIndigo
1.5BRackspace Hosting
1.5BAllied Riser Communications Co
1.5BXYLAN
1.5BwebMethods
1.5BFusion-io
1.5BPeoplePC
1.5BNetScreen Technologies
1.4BVIA NET.WORKS
1.4BTriton PCS Holdings
1.4BNetpliance
1.4BPortal Software
1.4BAriba
1.4BBroadcom Corp
1.4BDemand Media
1.4BiBeam Broadcasting Corp
1.4BUnivision Communications
1.4BSelectica
1.4BLookSmart Ltd
1.4BUbiquiti Networks
1.3BValue America
1.3BGlobal TeleSystems Group
1.3B724 Solutions
1.3BAlamosa PCS Holdings
1.3BSalesForce.com
1.3BTelocity Delaware
1.3BFinisar
1.3BOrbitz
1.3BMcLeod
1.3BRed Hat
1.3BMatrixOne
1.2BAmkor Technology
1.2BPixar
1.2BCompuWare
1.2BExactTarget
1.2BLSI LOGIC CORP.
1.2BGT Interactive Software
1.2BVersata
1.2BInfinera Corp
1.2BAGENCY.COM Ltd
1.2BAsiaInfo Holdings
1.2BOptionsXpress Holdings
1.2BNextcard
1.2BCellNet Data Systems
1.2BEquinix
1.2BNetwork Plus Corp
1.1BNextLink Communications
1.1BFORTUNE SYSTEMS
1.1BMarquette Electronics
1.1BCogent
1.1BTurnstone Systems
1.1BCovad Communications Group
1.1BExult
1.1BCritical Path
1.1BUS Internetworking
1.1BFirstWorld Communications
1.1BExtreme Networks
1.1BPlanetRx.com
1.1BMicrosoft
1.1BStar Media Network
1.1BSoftware Technologies Corp
1.1BRiskMetrics Group
1.1BCacheFlow
1.1BAdvanced Fibre Communications
1.0BAllegiance Telecom
1.0BOmnipoint
1.0BFocal Communications Corp
1.0BAccuray
1.0BiXL Enterprises
1.0BDrugstore.com
1.0BOmniSky Corp
1.0BCypress Communications Corp
1.0BTomotherapy Incorporated
1.0BLante Corp
1.0BVerio
1.0BIpass
1.0BHyperion Telecommunications
1.0BAPOLLO COMPUTER
1.0BPaging Network
1.0BGoAmerica
1.0BNeoforma.com
1.0BeBay
1.0BAlteon Websystems
1.0BAccelerated Networks
1.0BMillennial Media
1.0BSunrise Telecom
1.0BIntegrated Telecom Express
1.0BPaypal
1.0BRegister.com
1.0BInet Technologies
1.0BTickets.com
1.0BiVillage
1.0BExcel Switching Corp
0.9BFirePond
0.9BArterial Vascular Engineering
0.9BScient Corporation
0.9B3PAR
0.9BInterTrust Technologies Corp
0.9BTheraSense
0.9BNet 2000 Communications
0.9BHigh Speed Access Corp
0.9BAruba Networks
0.9BBruker Daltonics
0.9BYelp
0.9BIXIA Communications
0.9BGoto.com
0.9BSina.com
0.9BMcClatchy Newspapers
0.9BLiberate Technologies
0.9BCorio
0.9BDice Holdings
0.9BIsilon Systems
0.9BSun Microsystems
0.9BASM Lithography Holding
0.9BE-Stamp Corp
0.9BCTI Molecular Imaging
0.9BM/A-COM Technology Solutions
0.9BMercadolibre
0.9BAclara Biosciences
0.9BWit Capital Group
0.9BObjective Systems Integrators
0.9BMetaSolv Software
0.8BData Domain
0.8BInterXion Holding NV
0.8BFortinet
0.8BBrooks Fiber Properties
0.8BSolarWinds
0.8BCheckFree
0.8BEl Sitio International Corp
0.8BSaba Software
0.8BSoftware.com
0.8BCreative Technology
0.8BCentillium Communications
0.8BStarent Networks Corp
0.8BPacific Biosciences of CA
0.8BChordiant Software
0.8BKAYPRO CORPORATION
0.8BBigband Networks
0.8BAdvanced Switching Communic
0.8BCobalt Networks
0.8BAmerican Mobile Satellite
0.8BThe Active Network
0.8Bev3
0.8BMicrotune
0.8BWireless Facilities
0.8BRealD
0.8BLexent
0.8BESS Technology
0.8BSaifun Semiconductors Ltd
0.8BQuintus Corp
0.8BTenFold Corp
0.8BInsweb Corp
0.8BNova
0.8BQlik Technologies
0.8BAtheros Communications
0.8BinterWAVE Communications
0.8BGT Group Telecom
0.8BSplitRock Services
0.7BIlluminet Holdings
0.7BHypercom Corp
0.7BCabletron Systems
0.7BMultilink Technology Corp
0.7BHealtheon Corp
0.7BPageMart Wireless
0.7BInterland
0.7BNetwork Engines
0.7BInPhonic
0.7BNexGen
0.7BEfficient Networks
0.7BNetezza Corp
0.7BAngie's List
0.7BLoudeye Technologies
0.7BOpen Market
0.7BHeartport
0.7BOndisplay
0.7BResonate
0.7BNetwork Access Solutions Corp
0.7BE-Loan
0.7BMedicaLogic
0.7BQuest Software
0.7BGeoCities
0.7BALTOS COMPUTERS
0.7BJive Software
0.7BInternatnl Network Services
0.7BInfoblox
0.7BIXC Communications
0.7BQuokka Sports
0.7BDecisionOne
0.7BRiverbed Technology
0.7BCaldera Systems
0.7Bi2 Technologies
0.7BRealPage
0.7BTelular
0.7BGadzoox Networks
0.7BQiao Xing Mobile Commun
0.7BDelano Technology Corp
0.7BQuinStreet
0.7BBazaarvoice
0.7BUNGERMANN-BASS, INC.
0.7BPATHCOM
0.7BElectroCom Automation
0.7BGetthere.Com
0.7BHigher One Holdings
0.7BLightspan Partnership
0.7BVignette Corp
0.7BTelco Communications Group
0.7BiAsia Works
0.7BDealerTrack Holdings
0.7BKyphon
0.7BMIPS Computer Systems
0.7BTriton Network Systems
0.7BWebex Communications
0.7BAMDAHL
0.7Bibasis
0.7BPhone.com
0.7BBrocade Comm Sys
0.7BGuidewire Software
0.7BCheckPoint Software Tech
0.7BIllumina
0.7BUbiquitel
0.7BOpus360 Corp
0.6BVitria Technology
0.6BRedback Networks
0.6BBSquare Corp
0.6BMapQuest.com
0.6BCOMPUTER LANGUAGE
0.6BAshford.Com
0.6BAsiacontent.com Ltd
0.6BArrow International
0.6BChemdex Corp
0.6BHighwayMaster Communications
0.6BFTP Software
0.6BLOTUS DEVELOPMENT
0.6BINTECOM INC
0.6BCommerce One
0.6BOTG Software
0.6BEmerge Interactive
0.6BCopper Mountain Networks
0.6BVastera
0.6BCOMPAQ COMPUTER
0.6BZapme Corp
0.6BSiRF Technology Holdings
0.6BSwitch And Data
0.6BWink Communications
0.6BCONVERGENT TECH
0.6Bathenahealth
0.6BCalico Commerce
0.6BCrossroads Systems
0.6BSupport.com
0.6BMarimba
0.6BNuance Communications
0.6BSigmatel
0.6BCornerstone OnDemand
0.6BJuno Online Services
0.6BDigitalthink
0.6BData Return Corp
0.6BWomen.com Networks
0.6BAcme Packet
0.6BVicinity Corp
0.6BTheStreet.com
0.6BAncestry.com
0.6BTessera Technologies
0.6BOccuLogix
0.6BShopping.com Ltd
0.6BExtensity
0.6BInvenSense
0.6BEndWave Corp
0.6BAmazon.com
0.6BDivX
0.6BVyyo
0.6BCypress Semiconductor
0.6BFairMarket
0.6BQAD
0.6BHarris Interactive
0.6BScreamingMedia
0.6BARTISTdirect
0.6BVerifone
0.6BICx Technologies
0.6BUUNet Technologies
0.6BWorldGate Communications
0.6BPRIAM CORPORATION
0.6BLuminant Worldwide Corp
0.6BDSL.net
0.6BOneMain.com
0.6BDocent
0.6BDYSAN
0.6BPerformance Systems
0.6BMicroStrategy
0.6BMusicmaker.com
0.6BSanta Cruz Operation
0.6BCavium Networks
0.6BFormFactor
0.6BInterliant
0.6BLEE DATA
0.6BMetroNet Communications Corp
0.6BPinnacle Holdings
0.6BTherma-Wave
0.6BITXC Corp
0.6BKana Communications
0.6BAether Systems
0.6BAgile Software Corp
0.6BJNI Corp
0.6BWitness Systems
0.6BE.piphany
0.6BVisicu
0.6BLoudcloud
0.6BTechTarget
0.6BITC Deltacom
0.6BAutobytel.com
0.6BVistaPrint Limited
0.6BForte Software
0.5BHittite Microwave Corp
0.5BCSG Systems International
0.5BNovatel Wireless
0.5BPredictive Systems
0.5BSMTC Corp
0.5BInterWorld Corp
0.5BSuccessFactors
0.5BQuantum Effect Devices
0.5BUSCS International
0.5BCyberian Outpost
0.5BShopNow.com
0.5BZillow
0.5BIDX Systems
0.5BVixel Corp
0.5BSkullcandy
0.5BMellanox Technologies Ltd
0.5BK12
0.5BFloware Wireless Systems Ltd
0.5B@Road
0.5BCylink
0.5BQUALCOMM
0.5BNumerical Technologies
0.5BMICRON TECHNOLOGY
0.5BRealNetworks
0.5BComputron Software
0.5BUS LEC Corp
0.5BNightHawk Radiology Holdings
0.5BPremiere Technologies
0.5BSohu.com
0.5BResponsys
0.5BSciQuest.com
0.5BClarent Corp
0.5BFogdog Sports
0.5BPacketeer
0.5BVina Technologies
0.5BINTERGRAPH
0.5BAvantGo
0.5BGenomica Corp
0.5BLHS Group
0.5BRazorfish
0.5BMENTOR GRAPHICS
0.5BTeradata
0.5BAffinity Technology Group
0.5BClearnet Communications
0.5BGeneral Magic
0.5BMpath Interactive
0.5BStamps.com
0.5BTeleCommunications Systems
0.5BNetcentives
0.5BConner Peripherals
0.5BSYSTEMS & COMPUTERS
0.5BRead-Rite
0.5BSignalSoft Corp
0.5BIntraware
0.5BInktomi Corporation
0.5BAspec Technology
0.5BARBINET THEXCHANGE INC
0.5BCenCall Communications
0.5BArtisoft
0.5BKanbay International
0.5BAlliance Fiber Optic Products
0.5BVentritex
0.5BDAISY SYSTEMS
0.5BInterwoven
0.5BMediaplex
0.5BMICOM SYSTEMS
0.5BConvergent Communications
0.5BComscore
0.5BArt Technology Group
0.5BISS Group
0.5BADTRAN
0.5BInforte Corp
0.5BEvoke Communications
0.5BYahoo!
0.5BClick Commerce
0.5BMakeMyTrip Ltd
0.5BChina.com Corp
0.5BCAIS Internet
0.5BAirvana
0.5BSTRATUS COMPUTER
0.5BConor Medsystems
0.5Bnet.Genesis Corp
0.5BPalmer Wireless
0.5BCalix
0.5BBladeLogic
0.5BGenesys Telecommun Labs
0.5BEMC
0.5BDocumentum
0.5BOptium Corp
0.5BManhattan Associates
0.5BDigital Impact
0.5BAdvanced Analogic Technologies
0.5BFlyCast Communications
0.5BMagma Design Automation
0.5BConstant Contact
0.5BNetro Corporation
0.5BRADVision Ltd
0.5BMINISCRIBECORP.
0.5BSEAGATE TECHNOLOGY
0.5BEverex Systems
0.5BAutoweb.com
0.5BBE Semiconductor Industries
0.5BMedscape
0.5BLantronix
0.5BPrime Response
0.5BVanguard Cellular Systems
0.5BPixelworks
0.5BLoopNet
0.5B3DO
0.5BGalileo Technology
0.5BMastech
0.5BUSN Communications
0.5BDemandware
0.5BMASSTOR SYSTEMS
0.5BNVidia Corporation
0.5BAUTOMATIX INCORPORATED
0.5BStac Electronics
0.5BAsk Jeeves
0.5BLeadis Technology
0.5BSemiLEDs Corp
0.5BWebsense
0.5BDigital Island
0.5BMetro Mobile CTS
0.5BCanadian Solar
0.5BVLSI TECHNOLOGY
0.5BCyrix
0.5BPegasystems
0.5BMKS Instruments
0.5BSynnex Information Tech
0.5BOpenTable
0.5BNeutral Tandem
0.5BEprise Corp
0.4BTadiran
0.4Bi3 Mobile
0.4BPortalPlayer
0.4BeGain Communications
0.4BZY MOS CORPORATION
0.4BSRA International
0.4BBlaze Software
0.4BMortgage.com
0.4BSonicWALL
0.4BORBCOMM
0.4BBEA Systems
0.4BNational Instruments
0.4BNess Technologies
0.4BHouseValues
0.4BPrecise Software Solutions Ltd
0.4BEntropic Communications
0.4BE\*Trade Group
0.4BBoingo Wireless
0.4BInternet.com Corp
0.4BAppliedTheory Corporation
0.4BViant Corp
0.4BBruker AXS
0.4BCeragon Networks Ltd
0.4BCompellent Technologies
0.4BMMC Networks
0.4BCaliper Technologies Corp
0.4BInfoseek
0.4BUnited Video Satellite Group
0.4BMetawave Communications
0.4BCardioNet
0.4BMaxLinear
0.4BEvolve Software
0.4BAuspex Systems
0.4BL90
0.4BEgreetings Network
0.4BKeynote Systems
0.4BNellcor
0.4BTransition Systems
0.4BDigital Lightwave
0.4BQUANTUM CORP
0.4BZELTIQ Aesthetics
0.4BCentra Software
0.4BMASS. COMPUTER CORP.
0.4BBlue Nile
0.4BSERENA Software
0.4BBe Free
0.4BIntermolecular
0.4BCheap Tickets
0.4BAldus
0.4BBroadcast.Com
0.4BInsulet Corp
0.4BTelegroup
0.4BJFAX Com
0.4BBlackboard
0.4BAirNet Communications Corp
0.4BDestia Communications
0.4BProxicom
0.4BMAI Basic Four
0.4BTeleconnect
0.4BHeart Technology
0.4BSybase
0.4BOfficial Payments Corp
0.4BInfoSpace.com
0.4BInfinity Financial Technology
0.4BDallas-Semiconductor
0.4BNetwork Equipment Technologies
0.4BYurie Systems
0.4BInteractive Pictures Corp
0.4BEbenx
0.4BHealthextras
0.4BSilicon Image
0.4BAlpha & Omega Semiconductor Lt
0.4BJupiter Communications
0.4BNorthstar Neuroscience
0.4BSync Research
0.4BStanford Microdevices
0.4BEclipsys Corp
0.4BWellfleet Communications
0.4BTanning Technology Corp
0.4BNet Perceptions
0.4BTalarian Corp
0.4BImperva
0.4BBusiness Objects
0.4BOracle Systems
0.4BXtent
0.4BConvergent Group Corp
0.4BMultex.com
0.4BCareerBuilder
0.4BIndustri-Matematik
0.4BApropos Technology
0.4BShutterfly
0.4BEAGLE COMPUTER
0.4BIntraLase Corp
0.4BAvistar Communications Corp
0.4BIntegrated Information Systems
0.4BMiningCo.com
0.4BTalk City
0.4BXilinx
0.4BPECO II
0.4BBioForm Medical
0.4BNeoMagic Corp
0.4BDiscreet Logic
0.4BPemstar
0.4BKEY TRONIC CORP.
0.4BPure Software
0.4BProofpoint
0.4BAdForce
0.4BMGC Communications
0.4BVeriSign
0.4BNetflix.com
0.4BCisco Systems
0.4BMCK Communications
0.4BViatel
0.4BCallidus Software
0.4BAtlantic Tel-Network
0.4BSyntel
0.4BPets.com
0.4BNovadigm
0.4Biprint.com
0.4BSourcefire
0.4BNetScout Systems
0.4BCarrier Access Corporation
0.4BC3
0.4BSiebel Systems
0.4BJAMDAT Mobile
0.4BAdvanced Communications Group
0.4BOratec Interventions
0.4BMonolithic System Technology
0.4BTelematics International
0.4BWeb Street
0.4BC-bridge Internet Solutions
0.4BOpenVision Technologies
0.4BSawtek
0.4BFoxHollow Technologies
0.4BExodus Communications
0.4BSilverStream Software
0.4BSynopsys
0.4BVirata Corp
0.4BAdvantage Learning System
0.4BNetzee
0.4BInternet Brands
0.4BSmarterKids com
0.4BMONOLITHIC MEMORIES
0.4BLiquid Audio
0.4BAndover.net
0.4BI Many
0.4BCCC Information Srvcs Group
0.4BXCarenet
0.4BOmnivision Technologies
0.4BN2H2
0.4BElcom International
0.4BReachLocal
0.4BPNV
0.4BLogMeIn
0.4BEpocrates
0.4BRambus
0.4BDoubleClick
0.4BGlu Mobile
0.4BVALID LOGIC SYSTEMS
0.4BMICROPOLIS CORP.
0.4BPC-Tel
0.4BCbeyond Communications
0.4BTANDON
0.4BLaunch Media
0.4BPAR TECHNOLOGY
0.4BMetro Networks
0.4Bcoolsavings.com inc
0.4BAcuson
0.4BEloquent
0.4BiMagicTV
0.4BTaleo Corp
0.4BTELLABS
0.3BDexcom
0.3BVeraz Networks
0.3BNova Measuring Instruments
0.3BExabyte
0.3BTransgenomic
0.3BVocera Communications
0.3BVirtusa Corp
0.3BMobius Management Systems
0.3BO2Wireless Solutions
0.3BBluestone Software
0.3BVerticalNet
0.3BTERA CORP
0.3BImproveNet
0.3BVitacost.com
0.3BEdify
0.3BIntuit
0.3BFabrinet
0.3BActive Software
0.3BCellularVision USA
0.3BCapella Education Co
0.3BC-Cube Microsystems
0.3BTumbleweed Communications Corp
0.3BOpen Solutions
0.3BCardioGenesis
0.3BTelaxis Communications Corp
0.3BSunquest Information Systems
0.3BZYCAD CORP.
0.3BNetRatings
0.3BTriple P
0.3BOpen Text
0.3BTripath Technology
0.3BOneWave
0.3BEQUATORIAL COMMUNIC.
0.3BOmega Research
0.3BPDF Solutions
0.3BAspect Development
0.3BAtmel
0.3BBroadBand Technologies
0.3BDavidson & Associates
0.3BPacific Gateway Exchange
0.3BGRIC Communications
0.3BCardioThoracic Systems
0.3BTeleNav
0.3Bdrkoop.com
0.3BIkanos Communications
0.3BHPL Technologies
0.3BNassda Corp
0.3BAudioCodes Ltd
0.3BSS&C Technologies
0.3BDORADO MICRO SYSTEMS
0.3BWestell Technologies
0.3BCDnow
0.3BMetro Information Services
0.3BGolden Telecom
0.3B012 Smile.Communications Ltd
0.3BStudent Advantage
0.3BPRT Group
0.3BMedidata Solutions
0.3BSapient
0.3BEHealth
0.3BCrossWorlds Software
0.3BOmniture
0.3Bsoftware.net Corp
0.3BBroadbase Software
0.3BAnimas Corp
0.3BUS Auto Parts Networks
0.3BMicro Warehouse
0.3BVisioneer
0.3BOrckit Communications
0.3BSandisk
0.3BLCC International
0.3BQuarterdeck Office Systems
0.3BCorel
0.3BWatchguard Technologies
0.3BDigimarc Corp
0.3BMemco Software
0.3BNetwork Appliance
0.3BPrism Solutions
0.3BXircom
0.3BPower-One
0.3BDigital Microwave
0.3BOak Technology
0.3BSykes Enterprises
0.3BCyberSource
0.3BUSWeb Corp
0.3BBreakaway Solutions
0.3BiManage
0.3BTangoe
0.3BDemandTec
0.3BSyneron Medical Ltd
0.3BVirage
0.3BGupta
0.3BAksys
0.3BSmart Modular Technologies
0.3BMaker Communications
0.3BSynaptics
0.3BAuthenTec
0.3BIgo Corp
0.3BAspect Medical Systems
0.3BPhase Forward
0.3BVisio
0.3BTvia
0.3BPEC Solutions
0.3BPlumtree Software
0.3BAdvanced Energy Industries
0.3BPros Holdings
0.3BCorillian Corp
0.3BVideoServer
0.3BInformatica Corp
0.3BTelvent SA
0.3BEchelon Corp
0.3BTrans1
0.3BLivePerson
0.3BTrident Microsystems
0.3BFore Systems
0.3BCascade Communications
0.3BMetaTools
0.3BTRIAD SYSTEMS
0.3BAvid Technology
0.3BNuvasive
0.3BFlashNet Communications
0.3BFileNet
0.3BZebra Technologies
0.3BLiquidity Services
0.3BAeroGen
0.3BVirtual Radiologic Corp
0.3BC/NET
0.3BAudible
0.3BSilknet Software
0.3BMail.com
0.3BANSYS
0.3BSilicon Storage Technology
0.3BTivoli Systems
0.3BYesmail.com
0.3BVerilink
0.3BSeer Technologies
0.3BMotive
0.3BRudolph Technologies
0.3BLatitude Communications
0.3BAffiliated Computer Services
0.3BCytyc
0.3BSEEQ TECHNOLOGY
0.3BIDT
0.3BInternet Gold-Golden Lines Ltd
0.3BRamp Networks
0.3BDaleen Technologies
0.3B24/7 Media
0.3BOpnet Technologies
0.3BN2K
0.3BVirage Logic Corp
0.3BEmageon
0.3BASE Test
0.3BMainspring
0.3BInphi Corp
0.3BRubicon Technology
0.3BGenesis Microchip
0.3BGlobalstar Telecommunications
0.3BASHTON-TATE
0.3BHotjobs Com LTD
0.3BCINCINNATI MICRO.
0.3BPrivate Business
0.3BAlliant Computer Systems
0.3BINTEGRATED DEVICE
0.3BHealthcentral.com
0.3BVisual Networks
0.3BCOM21
0.3BArcSight
0.3BBrightcove
0.3BChipSoft
0.3BPurchasepro.com
0.3BBrooktree
0.3BMarketAxess Holdings
0.3BComputer Access Technology
0.3BIntegrated Silicon Solutions
0.3BTerayon Communication Systems
0.3BOnyx Software Corp
0.3BIOMEGA CORPORATION
0.3BGreat Plains Software
0.3BAlloy Online
0.3BRelational Technology
0.3BSagent Technology
0.3BAccord Networks Ltd
0.3BRed Brick Systems
0.3BValiCert
0.3BDigital Insight Corp
0.3BETINUUM INC
0.3BSequoia Software Corp
0.3BVolcano Corp
0.3BPowersoft
0.3BPeritus Software Services
0.3BMcAfee Associates
0.3BMission Critical Software
0.3BGuidance Software
0.3BEnvestnet
0.3BGeneral Surgical Innovations
0.3BPeopleSoft
0.3BConcur Technologies
0.3BHBO & COMPANY
0.3BAllaire Corp
0.3BSOFTWARE AG
0.3BKomag
0.3BCidco
0.3BPacific Internet Pte Ltd
0.3BNetwork Computing Devices
0.3BAllot Communications
0.3BMedia Vision Technology
0.3BPremenos Technology
0.3BMind C.T.I. Ltd
0.3BSYMBOLICS INC.
0.3BWalker Interactive Systems
0.3BPowerCerv
0.3BSeaChange International
0.3BTechnology Solutions
0.3BSynchronoss Technologies
0.3BPANSOPHIC SYSTEMS
0.3BPremisys Communications
0.3BGreenway Medical Tech
0.3BIntl Microelectronic Products
0.3BPyramid Technology
0.3BBox Hill Systems Corp
0.3BMAGNUSON COMPUTER
0.3BNAMIC USA
0.3BQuotesmith.com
0.3BGarden.com
0.3BPersistence Software
0.3BGTECH CORPORATION
0.3BDatalogix International
0.3BBe
0.3BSmartDisk(Toshiba,Fischer)
0.3BSilicon Graphics
0.3BHOGAN SYSTEMS
0.3BCorsair Communications
0.3BDigital Systems International
0.3BINTERTEC DATA
0.3BLendingTree
0.3BMedical Manager Corp
0.3BArbor Software
0.3BNanogen
0.3BLIEBERT
0.3BExcite
0.3BNetlogic Microsystems
0.3BCuron Medical
0.3BCirrus Logic
0.3BFriendFinder Networks
0.3BWebstakes.com
0.3BMTI Technology
0.3BINFOTRON SYSTEMS
0.3BFirst Virtual Corp
0.3BPSi Technologies
0.3BPairGain Technologies
0.3BRepeater Technologies
0.3BPrimus Telecommunications
0.3BPilot Network Services
0.3BSmarTalk TeleServices
0.3BBanyan Systems
0.3BTut Systems
0.3BRaptor Systems
0.3BRSL Communications Ltd
0.3BMediSense
0.3BObject Design
0.3BATV SYSTEMS, INC.
0.3BCommTouch Software
0.3BAccrue Software
0.3BNortheast Optic Network
0.3BNextest Systems Corp
0.3BMotherNature.com
0.3BAware
0.3BRemedy
0.3BNetcreations
0.3BPLX Technology
0.3BInternational Integration
0.3BPowerwave Technologies
0.3BCitrix Systems
0.3BSequent Computer Systems
0.3BNeoPhotonics Corp
0.3BCrossKeys Systems Corp
0.3BLinear Technology
0.3BCyberCash
0.3BMetalink LTD
0.3BTraffic.com
0.3BDigital Sound
0.3BSTAR TECHNOLOGIES
0.3BFirst Pacific Networks
0.3BDigirad Corp
0.3BDeltek Systems
0.3BBindview Development
0.3BVMX, INC.
0.3BFluidigm Corp
0.3BGoal Systems International
0.3BViewlogic Systems
0.3BVNUS Medical Technologies
0.3BTrimble Navigation
0.3BPowerDsine Ltd
0.3BGeoScience
0.3BMaxis
0.3BConvex Computer
0.3BMyPoints.com
0.3BWall Data
0.3BAurum Software
0.3BSynQuest
0.3BStereotaxis
0.3BCysive
0.3BFarallon Communications
0.3BUS Xpress Enterprises
0.3BHorizon Medical Products
0.3BTel-Save Holdings
0.3BCardiac Pathways
0.3BFlexiInternational Software
0.3BAspect Telecommunications
0.3BI-Stat
0.3BDouble-Take Software
0.3BCyberMedia
0.3BANDREW
0.3BMercury Interactive
0.2BXoom.com
0.2BF5 Networks
0.2BAirGate PCS
0.2BRacotek
0.2BSuper Micro Computer
0.2BRavisent Technologies
0.2BUS Interactive
0.2BImmersion Corp
0.2BRWD Technologies
0.2BHealthGate Data Corp
0.2BRegistry
0.2BPhoenix Technologies
0.2BPolycom
0.2BUroMed
0.2BCobalt Group
0.2BBMC Software
0.2BRF Micro Devices
0.2BCarreker-Antinori
0.2BMemsic
0.2BActel
0.2BTransaction Systems
0.2BSynplicity
0.2BBoston Communications Group
0.2BKnowledgeWare
0.2BDell Computer
0.2BNETWORK SYSTEMS
0.2BBorland International
0.2BDialogic
0.2BSmith Micro Software
0.2BCellular Information Systems
0.2BFreeShop.com
0.2BMicromuse,
0.2BCarbonite
0.2BFrame Technology
0.2BEnvivio
0.2BIndividual
0.2BZipLink
0.2BStreamline.com
0.2BAstea International
0.2BRadware Ltd
0.2BRightNow Technologies
0.2BTriZetto Group
0.2BQuickLogic Corp
0.2BEnphase Energy
0.2BCIRCON CORPORATION
0.2BSUPERTEX, INC.
0.2BEncore Computer
0.2BAPPLIED CIRCUIT
0.2BSYSTEMS INTEGRATORS
0.2BVideo Lottery Technologies
0.2BFastnet Corp
0.2BHome Diagnostics
0.2BIntelligent Life Corp
0.2BCybergold
0.2BNetSolve
0.2BVocalTec
0.2BServiceWare Technologies
0.2BNxStage Medical
0.2BWonderware
0.2BInteractive Intelligence
0.2BMIDCOM Communications
0.2BAscend Communications
0.2BPharsight Corp
0.2BRRSat Global Communications
0.2BElectronic Retailing Systems
0.2BLernout en Hauspie
0.2BARCHIVE CORP.
0.2BOverstock.com
0.2BFactSet Research Systems
0.2BNogatech
0.2B3Dlabs
0.2BSkillSoft Corp
0.2BHealthStream
0.2BClicksoftware Ltd
0.2BData Technology
0.2BAboveNet Communications
0.2BMeru Networks
0.2BLannet Data Communications
0.2BShiva
0.2BProgress Software
0.2BExactis.com
0.2BAtlantic Data Services
0.2BBroadSoft
0.2BDATA I/O
0.2BJDA Software Group
0.2BDendrite International
0.2BSHARED MEDICAL SYSTEMS
0.2BQuickturn Design Systems
0.2BPriCellular
0.2BGeotel Communications
0.2BViryaNet LTD
0.2BInterleaf
0.2BINFORMATION RESOURCES
0.2BProteon
0.2BItron
0.2BConcord Communications
0.2BMIM
0.2BLegato Systems
0.2BON Technology
0.2BConcentric Network Corp
0.2BMicrocell Telecommunications
0.2BScientific Learning
0.2BMovieFone
0.2BOrion Network Systems
0.2BQuepasa.com
0.2BFLOATING POINT SYSTEM
0.2BRadius
0.2BMANAGEMENT SCIENCE
0.2BADVANCED SEMICONDUCTOR
0.2BVolterra Semiconductor Corp
0.2BApplied Micro Circuits Corp
0.2BInnova Corp
0.2BSimplex Solutions
0.2BMARGAUX CONTROLS
0.2BeCollege.com
0.2BMiniMed
0.2BUltimate Software Group
0.2BSalesLogix Corp
0.2BBest Power Technology
0.2BSpectraLink
0.2BRetix Corp
0.2BOrtel
0.2BRita Medical Systems
0.2BComputer Programs & Systems
0.2BHoover's
0.2BRadView Software Ltd
0.2BEndosonics
0.2BUnica Corp
0.2BAdvanced Logic Research
0.2BHADCO CORP.
0.2BTower Semiconductor
0.2BEvolving Systems
0.2BVantive
0.2BCOMP-U-CARD
0.2BBrio Technology
0.2BCellular Communications
0.2B4th Dimension Software
0.2BImmunicon Corp
0.2BSpectranetics
0.2BNetManage
0.2BBiopsys Medical
0.2BLightbridge
0.2BProvide Commerce
0.2BRoweCom
0.2BVitesse Semiconductor Corp
0.2BPreferred Networks
0.2BXomed Surgical Products
0.2B@plan.inc
0.2BNatus Medical
0.2BScopus Technology
0.2BTeknekron Communications
0.2BWhittman-Hart
0.2BVarsityBooks.com
0.2BTowne Services
0.2BGEOPHYSICAL SYSTEMS
0.2BOnline Resources & Commun
0.2BBridge Communications
0.2BDSET Corp
0.2BMelita International Corp
0.2BUS Robotics
0.2BPositron Fiber Systems Corp
0.2BEvergreen Solar
0.2BITI Technologies
0.2BMACNEAL-SCHWENDLER
0.2BInterVideo
0.2BActuate Software Corp
0.2BMobility Electronics
0.2BHelicos BioSciences Corp
0.2BVoltaire Ltd
0.2BDOCUMATION
0.2BCepheid
0.2BCareScience
0.2BCamtek Ltd
0.2BAXENT Technologies
0.2BBroadVision
0.2BSYNTREX INC
0.2BPrimus Knowledge Solutions
0.2BMorino
0.2BKendall Square Research
0.2BDICEON ELECTRONICS
0.2BPower Med Interventions
0.2BPlatinum Technology
0.2BTresCom International
0.2BLionbridge Technologies
0.2BOrthofix International
0.2BAsymetrix Learning Systems
0.2BVascular Solutions
0.2BAugust Technology Corp
0.2BCollectors Universe
0.2BAdvanced Interventional Sys
0.2BSciQuest
0.2BBest Software
0.2BAris Corp
0.2BS3
0.2BIntellon Corp
0.2BWebTrends Corporation
0.2BMacromedia
0.2BElectronics for Imaging
0.2BGeneral Parametrics
0.2BAlpharel
0.2BStar Telecommunications
0.2BECtel
0.2BFlextronics International
0.2BTricord Systems
0.2BDigital River
0.2BMicroware Systems
0.2BTrusted Information Systems
0.2BZycon
0.2BCredence Systems
0.2BExcelan
0.2BTelCom Semiconductor
0.2BInformation Management
0.2BCooper & Chyan Technology
0.2BHybrid Networks
0.2BDIONEX CORP
0.2BCadnetix
0.2BViador
0.2BBamboo.com
0.2BKOLFF MEDICAL, INC.
0.2BCORVUS SYSTEMS
0.2BApplied Digital Access
0.2BWebsite Pros
0.2BXEBEC
0.2BASD Systems
0.2BnFront
0.2BPeregrine Systems
0.2BDepoTech
0.2BAbacus Direct
0.2BInfonautics
0.2BBachman Information Sys
0.2BKintera
0.2BBR COMMUNICATIONS
0.2BKnot
0.2BVECTOR GRAPHIC
0.2BBURR-BROWN CORPORATION
0.2BMarchex
0.2BSynOptics Communications
0.2BNumber Nine Visual Technology
0.2BDesktop Data
0.2BInterntnl Telecommuncation
0.2BMarcam
0.2BeOn Communications Corp
0.2BLevel One Communications
0.2BSmith-Gardner & Associates
0.2BCognicase
0.2BAltera
0.2BChemtrak
0.2BInStent
0.2BHall Kinion & Associates
0.2BSynercom Technology
0.2B3Dfx Interactive
0.2BGRADCO SYSTEMS INC.
0.2BOctel Communications
0.2BBraun Consulting
0.2BHireRight
0.2BClarify
0.2BTrunkbow Intl Hldgs Ltd
0.2BUrologix
0.2BDSP Group
0.2BOmniCell
0.2BTeledata Communication
0.2BSCM Microsystems
0.2BINTEGRATED SOFTWARE
0.2BConceptus
0.2BPlatinum Software
0.2BELECTRO SCIENTIFIC
0.2BHealthetech
0.2BPervasive Software
0.2BVital Signs
0.2BAdvent Software
0.2BArcSys
0.2BPerclose
0.2BSummit Design
0.2BSYSTEMATICS
0.2BCascade Microtech
0.2BTeknowledge
0.2BSQA
0.2BWalsh International
0.2BCondor Technology Solutions
0.2BFlextronics
0.2BOSI Systems
0.2BSPR
0.2BFocal
0.2BSyquest Technology
0.2BLogic Works
0.2BFirefox Communications
0.2BDocument Sciences
0.2BCynosure
0.2BRigNet
0.2BDigital Link
0.2BFONAR
0.2BISC SYSTEMS
0.2BHarbinger
0.2BPlanetOut
0.2BVerity
0.2BXionics Document Technologies
0.2B3COM CORP.
0.2BHeartland Wireless
0.2BSILICON VALLEY GROUP
0.2BInnovative Solns & Support
0.2BMicrus Endovascular Corp
0.2BArthrocare
0.2BBottomline Technologies
0.2BLandacorp
0.2BEnterprise Systems
0.2BMeta Software
0.2BInformation Storage Devices
0.2BZIYAD INC.
0.2BGeneral Scanning
0.2BSalary.com
0.2BParcPlace Systems
0.2BImpac Medical Systems
0.2BMICROPRO INT'L
0.2BEnvoy
0.2BSCC Communications Corp
0.2BMicrotest
0.2BEarthLink Network
0.2BNeon Systems
0.2BAutoCyte
0.2BPegasus Systems
0.2BWorkgroup Technology
0.2BInternational Imaging
0.2BImagyn Medical
0.2BParametric Technology
0.2BPlasma & Materials Tech
0.2BStrataCom
0.2BCatapult Communications
0.2BMaxtor
0.2BCutera
0.2BP-COM
0.2BInterspeed
0.2BIntelligent Medical Imaging
0.2BSegue Software
0.2BKENTRON INT'L
0.2BInformation Management Assocs
0.2BCyberonics
0.2BAtriCure
0.2BLanVision Systems
0.2BGSI Technology
0.2BArtisan Components
0.2BHPR
0.2BONTRACK Data International
0.2BCygnus Therapeutic Systems
0.2BBroderbund Software
0.2BIPC Information Systems
0.2BTTR
0.2BMolecular Dynamics
0.2BNetGravity
0.2BDATASOUTH COMPUTER
0.2BFARO Technologies
0.2BNetframe Systems
0.2BCADO SYSTEMS
0.2BPuma Technology
0.2BARGOSYSTEMS
0.2BSunGard Data Systems
0.2BUSA Mobile Communications
0.2BAMISYS Managed Care Systems
0.2BAradigm
0.2BPeerless Systems
0.2BLogicVision
0.2BVista Medical Technologies
0.2BAlantec
0.2BQUALITY MICRO SYSTEMS
0.2BVerisity Ltd
0.2BTANDEM COMPUTERS
0.2BVitalink Communications
0.2BCellPro
0.2BECAD
0.2BK-TRON
0.2BSyntellect
0.2BSage
0.2BFINALCO GROUP
0.2BWavePhore
0.2BCONNECT
0.2BSoftware 2000
0.2BMapInfo
0.2BClaremont Technology Group
0.2BSCB Computer Technology
0.2BNeopath
0.2BAdvanced Power Technology
0.2BVideoTelecom
0.2BIntelligroup
0.2BCatalyst International
0.2BDEVELCON ELECTRONICS
0.2BESPS
0.2BMoldflow Corp
0.2BVersatility
0.2BOpen Environment
0.2BDigidesign
0.2BVocus
0.2BT/R Systems
0.2BDigex
0.2BOptical Sensors
0.2BMicro Linear
0.2BVENTREX LABS
0.2BVitech America
0.2BDIGITAL COMMUNICATIONS
0.2BNetlist
0.2BAmtech
0.2BSecure Computing
0.2BApex PC Solutions
0.2BACT Manufacturing
0.2BImageX com
0.2BWebSideStory
0.2BSalon.com
0.2BSportsLine USA
0.2BEarthWeb
0.2BImpact Systems
0.2BBackWeb Technologies Ltd
0.2BCentex Telemanagement
0.2BAlliance Semiconductor
0.2BReSourcePhoenix com
0.2BBreezeCOM
0.2BStorm Technology
0.2BJabil Circuit
0.2BPraegitzer Industries
0.1BSDL
0.1BNetrix
0.1BAST RESEARCH
0.1BAutodesk
0.1BADE
0.1BConvio
0.1BRadiant Systems
0.1BXyvision
0.1BSumma Four
0.1BGilat Satellite Networks
0.1BGlobal Village Communication
0.1BBritton Lee
0.1BIntegrated Packaging Assembly
0.1BStructural Dynamics Research
0.1BGENRAD
0.1BNBI
0.1BInnotrac Corp
0.1BEdgar Online
0.1BAmerican Dental Laser
0.1BData Processing Resources
0.1BComplete Business Solutions
0.1BExchange Applications
0.1BNitinol Medical Technologies
0.1BQuickResponse Services
0.1BTV Filme
0.1BChannell Commercial
0.1BNetRadio Corp
0.1BIMNET Systems
0.1BNCI
0.1BPROTOCOL COMPUTERS
0.1BVision-Sciences
0.1BTELCO SYSTEMS
0.1BRedEnvelope
0.1BISOMEDIX, INC.
0.1BHeadHunter.NET
0.1BLitronic
0.1BNew Era of Networks
0.1BCardioPulmonics
0.1BTranSwitch
0.1BOacis Healthcare Holdings
0.1BMetrocall
0.1BOmtool Ltd(ASA International)
0.1BEnteroMedics
0.1BEndoVascular Technologies
0.1BCardioVascular Dynamics
0.1BProcom Technology
0.1BMercury Computer Systems
0.1BAsante Technologies
0.1BZENTEC
0.1BAPPLICON
0.1BManugistics Group
0.1BVitalCom
0.1BXpedite Systems
0.1BASK COMPUTER SYSTEMS
0.1BMolecular Devices
0.1BApplied Immune Sciences
0.1BWeitek
0.1BMARQUEST MEDICAL
0.1BIntellicall
0.1BDAOU Systems
0.1BCP Clare
0.1BBrightStar Information
0.1BNumar
0.1BCybex
0.1BTri-Point Medical
0.1BONSALE
0.1BHNC Software
0.1BComputer Motion
0.1BSILICON SYSTEMS
0.1BBam Entertainment
0.1BSoftware Artistry
0.1BFractal Design
0.1BUltratech Stepper
0.1BStartec Global Communications
0.1BInterplay Entertainment
0.1BSequoia Systems
0.1BACT Networks
0.1BNanophase Technologies Corp
0.1BInnotech
0.1BPerSeptive Biosystems
0.1BElectronic Arts
0.1BJudge Group
0.1BAMERICAN SOFTWARE
0.1BARI Network Services
0.1BParadigm Technology
0.1BOverland Data
0.1BVantagemed Corp
0.1BState of the Art
0.1BCryoCor
0.1BTelemate Net Software
0.1BANADIGICS
0.1BSecurity Dynamics Technologies
0.1B8x8
0.1BUnify
0.1BINVACARE CORP.
0.1BVM Software
0.1BAdaptec
0.1BADFlex Solutions
0.1BGIGA-TRONICS
0.1BMEDIFLEX SYSTEMS
0.1BLTX CORP
0.1BCambridge Heart
0.1BData Critical Corp
0.1BTELXON CORPORATION
0.1BPrintcafe Software
0.1BIMRS
0.1BAspen Technology
0.1BNetcom On-Line Communications
0.1BSpyglass
0.1BTGV Software
0.1BXyplex
0.1BFashionmall.com
0.1BSoundBite Communications
0.1BRogue Wave Software
0.1BSenoRx
0.1BVisigenic Software
0.1BChips and Technologies
0.1BSpectrian
0.1BRoss Systems
0.1BINTER-TEL
0.1BSCIENTIFIC MICRO SYS
0.1BMathSoft
0.1BEldec
0.1BZoran
0.1BFirst Virtual Holdings
0.1BPolyMedica Industries
0.1BBoca Research
0.1BTechnology Modeling Assocs
0.1BDomain Technology
0.1BContinuus Software Corp
0.1BSynacor
0.1BPRINTRONIX
0.1BVoxware
0.1BParallan Computer
0.1BTechForce
0.1BMicrochip Technology
0.1BAPPLIED COMMUNICATIONS
0.1BBGS SYSTEMS
0.1BPower Integrations
0.1BInteg
0.1BSystem Software Associates
0.1BPhysicians Computer Network
0.1BAtria Software
0.1BMetro One Telecommunications
0.1BBANCTEC
0.1BWYSE TECHNOLOGY
0.1BAICorp
0.1BRADCOM Ltd
0.1BIPL SYSTEMS
0.1BCommand Systems
0.1BIntegrated Systems
0.1BKips Bay Medical
0.1BBionx Implants
0.1BArch Communications Group
0.1BNANOMETRICS INC.
0.1Btheglobe.com inc
0.1BON LINE SOFTWARE
0.1BInformation Advantage Software
0.1BRICHARDSON ELEC.
0.1BShowCase Corp
0.1BRestrac
0.1BPeriphonics Corp
0.1BSQL Financials International
0.1BVODAVI TECHNOLOGY
0.1BInterVU
0.1BENDATA, INC.
0.1BExide Electronics Group
0.1BWind River Systems
0.1BEllie Mae
0.1BMicrocom
0.1BIn Focus Systems
0.1BSimulation Sciences
0.1BAVANT-GARDE
0.1BSurgical Laser Technologies
0.1BIKOS Systems
0.1BProtocol Systems
0.1BProxima
0.1BRural Cellular
0.1BJacada Ltd
0.1BJetFax
0.1BSAGE Software
0.1BINTELLIGENT SYSTEMS
0.1BGlobeComm Systems
0.1BBOLT TECHNOLOGY
0.1BCredit Management Solutions
0.1BReptron Electronics
0.1BApache Medical Systems
0.1BNetSpeak Corp
0.1BCULLINANE
0.1BMicrel
0.1BDSP Communications
0.1BFDP CORPORATION
0.1BXcelleNet
0.1BNetivation.com
0.1BWhite Pine Software
0.1BIDEXX Corp
0.1BPENTA SYSTEMS
0.1BSabratek
0.1BSOUTHERN MEDIC & PHARM
0.1BISOETEC Communications
0.1BDavox
0.1BVisible Genetics
0.1BCommunity Health Computing
0.1BMaxim Integrated Products
0.1BRenaissance Solutions
0.1BMegatest
0.1BCornerstone Imaging
0.1BEpic Design Technology
0.1BKLA INSTRUMENTS
0.1BPixTech
0.1BFemRx
0.1BTelebit
0.1BTSI International Software Ltd
0.1BVERBATIM
0.1BPericom Semiconductor Corp
0.1BTECH FOR COMM
0.1BAdobe Systems
0.1BIsocor
0.1BUniversal Electronics
0.1BSymantec
0.1BHEALTHDYNE
0.1BCrossComm
0.1BDataware Technologies
0.1BQualix Group
0.1BInternet America
0.1BHTE
0.1BMattson Technology
0.1BEdunetics
0.1BAllin Communications
0.1BCerner
0.1BAUTO-TROL TECHNOLOGY
0.1BInference
0.1BRasterOps
0.1BBofI Holding
0.1BBlonder Tongue Laboratories
0.1BNeurometrix
0.1BWorldtalk Communications
0.1BSEI
0.1BContinental Circuits
0.1BSmartflex Systems
0.1BEndocardial Solutions
0.1BPrintrak International
0.1BMathstar
0.1BCaere
0.1BBEI Electronics
0.1BViaGrafix Corp
0.1BIntegrated Measurement Systems
0.1BCatalyst Semiconductor
0.1BINSTACOM
0.1BOptical Data Systems
0.1BAehr Test Systems
0.1BDataWorks
0.1BInformix
0.1BTele-Matic
0.1BMitek Surgical Products
0.1BIntevac Industries
0.1BAbaxis
0.1BARIX
0.1BMedrad
0.1BArtificial Life
0.1BSELECTERM, INC.
0.1BPARADYNE CORP
0.1BXICOR
0.1BPhysician Support Systems
0.1BHHB Systems
0.1BGilat Communications LTD
0.1BAMPLICA
0.1BVISUAL TECHNOLOGY
0.1BAmerican Superconductor
0.1BEducational Insights
0.1BScopus Video Networks
0.1BPoint of Sale Ltd
0.1BRadiSys
0.1BBHC Financial
0.1BMecon
0.1BUltradata
0.1BLandmark Graphics
0.1BLandmark Systems Corp
0.1BLaserscope
0.1BCardica
0.1BDial Page
0.1BSonic Solutions
0.1BFair Issac & Company
0.1BAsia Electronics Holding Co
0.1BPSW Technologies
0.1BTransaction Network Services
0.1Bonlinetradinginc.com
0.1BKopin
0.1BLattice Semiconductor
0.1BMicrotec Research
0.1BCrystal Systems Solutions Ltd
0.1BCABG Medical
0.1BGERBER SYSTEMS
0.1BConsilium
0.1BEmultek
0.1BSpacetec IMC
0.1BLunar
0.1BInteractive Magic
0.1BCOMPUTER ASSOCIATES
0.1BRADIONICS INC.
0.1BFundtech Ltd
0.1BTYLAN
0.1BLJL Biosystems
0.1BMicronics Computers
0.1BInterspec
0.1BABIOMED
0.1BA+ Communications
0.1BRealty Information Group
0.1BTel/Man
0.1BCATS Software
0.1BUroquest Medical
0.1BLINEAR CORPORATION
0.1BActive Voice
0.1BAxiom
0.1BWorldQuest Networks
0.1BSOFTWARE PUBLISHING
0.1BVeritas Software
0.1BWave Systems
0.1BIndex Technology
0.1BTriTeal
0.1BDIAGNOSTIC PRODUCTS
0.1BAmerica Online
0.1BAllied Healthcare Products
0.1BOculus Innovative Sciences
0.1BBrite Voice Systems
0.1BQuintalinux Ltd
0.1BAccelGraphics
0.1BSimware
0.1BLearning
0.1BTier Technologies
0.1BUnison Software
0.1BHAEMONETICS
0.1BMONCHIK-WEBER
0.1BAUTOCLAVE ENGINEERS
0.1BXeTel
0.1BSuperMac Technology
0.1BFEI
0.1BALPHA MICROSYSTEMS
0.1BTIME ENERGY SYSTEMS
0.1BQuadraMed
0.1BOPTi
0.1BMicroProse
0.1BViaSat
0.1BSTRYKER
0.1BVersant Object Technology
0.1BZITEL CORPORATION
0.1BOrCAD
0.1BApplied Voice Technology
0.1BTRO Learning
0.1BZST Digital Networks
0.1BTollgrade Communications
0.1BComputer Management Sciences
0.1BProxim
0.1BRaster Graphics
0.1BElamex
0.1BCIPHER DATA PRODUCTS
0.1BSTANFORD TELECOMM.
0.1BApplied Microsystems
0.1BTriconex
0.1BSCI. SYSTEMS SERVICE
0.1BCommunications Central
0.1BSummit Medical Systems
0.1BMicrografx
0.1BEqualNet Holdings
0.1BEagle Point Software
0.1BTemplate Software
0.1BNATIONAL BUS. SYS.
0.1BDigital Music Group
0.1BVIASOFT
0.1BKEVEX
0.1BAnsoft
0.1BPhamis
0.1BLeCroy
0.1BAlloy Computer Products
0.1BROLM
0.1BBiznessOnline.com
0.1BConcentra
0.1BVanguard Technologies Intl
0.1BADAM Software
0.1BRIT Technologies Ltd
0.1BZoll Medical
0.1BFourth Shift
0.1BDEST
0.1BLog On America
0.1BC-COR ELECTRONICS
0.1BExtended Systems
0.1BXylogics
0.1BBiomagnetic Technologies
0.1BNetStar
0.1BDATA TERMINAL
0.1BAG Associates
0.1BImageMAX
0.1BPerception Technology
0.1BNetwork General
0.1BGeoWorks
0.1BPhoton Dynamics
0.1BEP Technologies
0.1BCRAY RESEARCH
0.1BPCD
0.1BFORMASTER CORPORATION
0.1BSoftdesk
0.1BKronos
0.1BCalypte Biomedical
0.1BDavel Communications Group
0.1BAremissoft Corporation
0.1BRemec
0.1BVIALOG Corp
0.1BA Consulting Team
0.1BMinnesota Educational
0.1BAnalogy
0.1BMOSCOM
0.1BElectrostar
0.1BVideonics
0.1BULTIMATE CORPORATION
0.1BLIFELINE SYSTEMS
0.1BCardiometrics
0.1BBytex
0.1BValue-Added Communications
0.1BTencor Instruments
0.1BAVANTEK
0.1BMicrowave Power Devices
0.1BIntermedia Communications
0.1B202 DATA SYSTEMS
0.1BBird Medical Technologies
0.1BNCA
0.1BElantec Semiconductor
0.1BVidaMed
0.1BData Race
0.1BIntegrated Silicon Systems
0.1BPhysiometrix
0.1BDatalink Corp
0.1BGSE Systems
0.1BComputational Systems
0.1BNephros
0.1BIPC COMMUNICATIONS
0.1BSuperconductor Technologies
0.1BVMark Software
0.1BGensym
0.1BInterlink Computer Sciences
0.1BFLIR Systems
0.1BTriQuint Semiconductor
0.1BAudio Book Club
0.1BQUALITY SYSTEMS
0.1BMicroBilt
0.1BTotal Control Products
0.1BAMER. MGMT. SYSTEMS
0.1BAccom
0.1BMicro Component Technology
0.1BDiametrics Medical
0.1BTekelec
0.1BDETECTOR ELECTRONICS
0.1BPinnacle Micro
0.1BROBINSON NUGENT
0.1BCMC Industries
0.1BDATASWITCH
0.1BSYSTEMS ASSOCIATES
0.1BODETICS
0.1BSignal Technology
0.1BVeeco Instruments
0.1BNetwork Peripherals
0.1BConductus
0.1BIrwin Magnetic Systems
0.1BIridex
0.1BSeaMED
0.1BGMIS
0.1BMECA Software
0.1BINFORMATICS
0.1BXscribe
0.1BSystemSoft
0.1BKofax Image Products
0.1BPARLEX CORPORATION
0.1BCotelligent Group
0.1BNovAtel Inc(Alberta/Canada)
0.1BBroadway & Seymour
0.1BApplied Signal Technology
0.1BANDOVER CONTROLS
0.1BAutomated Language Processing
0.1BSTB Systems
0.1BDatastream Systems
0.1BHutchinson Technology
0.1BAMHERST ASSOCIATES
0.1BCognex
0.1BCardima
0.1BIncrediMail Ltd
0.1BUltrafem
0.1BKentek Information Systems
0.1BIAT Multimedia
0.1BPinnacle Systems
0.1BCALIF. AMPLIFIER
0.1BProNet
0.1BAutonomous Technologies
0.1BMANUFACTURING DATA
0.1BELEC OF ISRAEL
0.1BBrock Control Systems
0.1BNational FSI
0.1BEVANS & SUTHERLAND
0.1BAUTOMATED SYSTEMS
0.1BTake To Auction.com
0.1BComptronix
0.1BCABLE TV INDUSTRIES
0.1BStorage Dimensions
0.1BDH TECHNOLOGY
0.1BIntegrated Sensor Solutions In
0.1BCOMPUTER MEMORIES
0.1BMetricom
0.1BBenchmarq Microelectronics
0.1BSYSCON
0.1BMetrologic Instruments
0.1BSCAN-TRON CORP.
0.1BOdimo
0.1BSPSS
0.1BCentigram Communications
0.1BAward Software International
0.1BFieldworks
0.1BAPPLIED DATA
0.1BAce\*Comm
0.1BTessco Technologies
0.1BIA
0.1BSpectRx
0.1BLumisys
0.1BSTERLING SOFTWARE
0.1BCeleritek
0.1BCardiovascular Imaging Systems
0.1BTERAK CORP.
0.1BINTERAND CORPORATION
0.1BGo2pharmacy.com
0.1BCOMPUTONE SYSTEMS
0.1BGULL, INC.
0.1BIsco
0.1BTOPAZ
0.1BInternet Financial Services
0.1BBTG
0.1BQuality Semiconductor
0.1BLASER INDUSTRIES
0.1BWorld Heart
0.1BSatellite Technology
0.1BGaiam
0.1BSYSTEM INDUSTRIES
0.1BDigi International
0.1BALTRON INC.
0.1BBEL FUSE
0.1BAdvanced Promotion Tech
0.1BSecuracom
0.1BEmcore Corp
0.1BBARON DATA SYSTEMS
0.1BEPSILON DATA MGMT.
0.1BApplied Imaging
0.1BMySoftware
0.1BOrbit Semiconductor
0.1BInterlinq Software
0.1BEMULEX
0.1BAdvanced Technology Materials
0.1BProject Software & Development
0.1BParkerVision
0.1BMagal Security Systems
0.1BTALX
0.1BEquinox Systems
0.1BMicroTouch Systems
0.1BQiao Xing Universal Telephone
0.1BOrthoLogic
0.1BSILVAR-LISCO
0.1BClaimsnet.com
0.1BAndyne Computing Limited
0.1BApplix
0.1BEasel
0.1BSANDERS, RC TECH.
0.1BESPRIT SYSTEMS
0.1BHumaScan
0.1BSummagraphics
0.1BINTELLIGENETICS
0.1BBPI SYSTEMS
0.1BAstropower
0.1BFusion Telecommunications
0.1BPhoenix International Ltd.
0.1BInVision Technologies
0.1BCritical Industries
0.1BLogal Educational Software
0.1BMedicus Systems
0.1BCOOK DATA SERVICES
0.1BLuna Innovations
0.1BBio-Plexus
0.1BPlexus
0.1BZytec Corp
0.1BCRIME CONTROL
0.1BCIBER
0.1BJPM
0.1BKeptel
0.1BBOOLE & BABBAGE
0.1BWebSecure
0.1BIntelligent Surgical Laser
0.1BTelesis Systems
0.1BLiberty Technologies
0.1BEquitrac
0.1BEuphonix
0.1BKVH Industries
0.1BCOPYTELE, INC.
0.1BIntelli-Check
0.1BMedialink Worldwide
0.1BVALLEN
0.1BARRAYS, INC.
0.1BAdvanced Magnetics
0.1BOptiSystems Solutions Ltd
0.1BBIOSEARCH MEDICAL
0.1BIllinois Superconductor
0.1BWavefront Technologies
0.1BPhotran
0.1BCERMETEK MICROELEC.
0.1BBrooktrout Technology
0.1BPhotonics Corp
0.1BTelos
0.1BCOMPTEK RESEARCH
0.1BIntegrated Circuit Systems
0.1BSymix Systems
0.1BMizar
0.1BISG International Software
0.1BSolectron
0.1BElectro-Optical Sciences
0.1BAbsolute Entertainment
0.1BHemoSense
0.1BCONTINUOS CURVE LENS
0.1BGenesisIntermedia.com
0.1BCyberShop International
0.1BTESDATA SYSTEMS
0.1BLambert Communications
0.1BALLY & GARGANO
0.1BICU Medical
0.1BFIBRONICS INT'L
0.1BeRoom System Technologies
0.1BE-Cruiter.com
0.1BOptibase Ltd
0.1BMindscape
0.1BUOL Publishing
0.1BCOMMUNICATIONS SYSTEMS
0.1BAdvanced Communication Systems
0.1BSierra On-Line
0.1BCORCOM
0.1BPERFECT DATA CORP.
0.1BVentana Medical Systems
0.1BDelphi Information Systems
0.1BMindSpring Enterprises
0.1BCOMPUTER ENTRY
0.1BOptika Imaging Systems
0.1BIQ Software
0.1BBusyBox.com
0.1BAmerican Technical Ceramics
0.1BCYBERTEK COMPUTER
0.1BCCX NETWORK
0.1BELECTRO-BIOLOGY
0.1BINT'L ROBOMATION
0.1BSOFTECH
0.1BInterchange Corp
0.1BLifequest Medical
0.1BInformation America
0.1BCriticare Systems
0.1BRAMTEK
0.1BRegistry Magic
0.1BForeFront Group
0.1BLowrance Electronics
0.1BFSI International
0.1BMicro Therapeutics
0.1BPerformance Technologies
0.1BSCIENTIFIC TIME SHAR
0.1BMedi-Ject
0.1BParadigm Geophysical Ltd
0.1BDATEQ Information Network
0.1BRheometrics
0.1BLANE TELECOMM.
0.1BTake-Two Interactive Software
0.1BDICKEY-JOHN
0.1BUniphase
0.1BCircadian
0.1BMulticom Publishing
0.1BMade2Manage Systems
0.1BUnitech Industries
0.1BPhotronic Laboratories
0.1BWiztec Solutions
0.1BDUQUESNE SYSTEMS
0.1BSCS/Compute
0.1BLogic Devices
0.1BBrilliant Digital Ent
0.1BI D Systems
0.1BOBJECT RECOGNITION
0.1BTIE / COMMUNICATIONS
0.1BPOWERTEC, INC.
0.1BAC Teleconnect
0.1BBioanalytical Systems
0.0BBitstream
0.0BIDB Communications Group
0.0BRF Monolithics
0.0BSpatial Technology
0.0BBenchmark Electronics
0.0BGolden Systems
0.0BCDP Technologies
0.0BCEM
0.0BAcross Data Systems
0.0BPlastic Surgery Co
0.0BKinetiks.com
0.0BAseco
0.0BGo2Net
0.0BCrossZ Software Corp
0.0BAladdin Knowledge Systems
0.0BCIPRICO INC.
0.0BSEEC
0.0BWESPERCORP
0.0BNORTHERN DATA SYS
0.0BTarget Technologies
0.0BTaunton Technologies
0.0BDIAGNON CORP
0.0BKYLE TECHNOLOGY
0.0BSTARTEL CORPORATION
0.0BScanVec Co(1990)
0.0BMEDAR, INC.
0.0BMerge Technologies
0.0BComet Software International
0.0BPRIMAGES, INC.
0.0BINTERMETRICS
0.0BARTEL COMMUNICATIONS
0.0BCOMPUTRAC INC.
0.0BCoin Bill Validator
0.0BEIL INSTRUMENTS
0.0BJack Henry & Associates
0.0BINTERPHASE CORP.
0.0BVertex Communications
0.0BSunhawk.com Corp
0.0BMass Microsystems
0.0BData Translation
0.0BMER Telemanagement Solutions
0.0BLaser Power Corp
0.0BWILAND SERVICES INC.
0.0BHYTEK MICROSYSTEMS
0.0BSPECTRADYNE
0.0BCOMPUTER INPUT
0.0BCalifornia Micro Devices
0.0BSBE INC.
0.0BElcotel
0.0BInternational CompuTex
0.0BCoherent Communications
0.0BTELENET
0.0BJetForm
0.0BInfoCure Corp
0.0BAML Communications
0.0BLoronix Information Systems
0.0BEffective Management Systems
0.0BREXON BUSINESS
0.0BTECHNOLOGY MARKETING
0.0BSSE Telecom
0.0BQuad Systems
0.0BAmerican Xtal Technology
0.0BElectronic Fab Technology
0.0BPrintware
0.0BInteractive Group
0.0BTLS CO.
0.0BPanda Project
0.0BData Research Associates
0.0BResearch Engineers
0.0BFREY ASSOCIATES
0.0BElectronic Information Systems
0.0BLANGER BIOMECHANICS
0.0BMEDSTAT SYSTEMS
0.0BCavion Technologies
0.0BHealthdesk(R)Corp
0.0BNatural Microsystems
0.0Be-NET
0.0BENCAD
0.0BDiversified Security Solutions
0.0BBridgeline Software
0.0BCitation Computer Systems
0.0BIverson Technology
0.0BCliniCom
0.0BCLINICAL DATA
0.0BWINTERHALTER, INC.
0.0BCONMED
0.0BOXYGEN ENRICHMENT
0.0BASTRO-MED, INC.
0.0BCONT'L HEALTHCARE
0.0BAdvanced Photonix
0.0BUNIVERSAL MONEY
0.0BECCS
0.0BVodavi Technology
0.0BNuwave Technologies
0.0BTRIO-TECH INT'L
0.0BV BAND SYSTEMS, INC.
0.0BPercon Acquisition
0.0BCYCARE SYSTEMS
0.0BImage Business Systems
0.0BElectronic Tele-Communications
0.0BBKW, INC.
0.0BPerficient
0.0BDIAGNOSTIC/RETRIEVAL
0.0BDISTRIBUTED LOGIC
0.0BSC & T International
0.0BTruetime
0.0BTELERAM COMMUNICATIONS
0.0BHenley International
0.0BOptek Technology
0.0BPerceptron
0.0BTylan General
0.0BINFO DESIGNS, INC.
0.0BNew Image Industries
0.0BAugment Systems
0.0BCasino Data Systems
0.0BNetwork-1 Security Solutions
0.0BThrustMaster
0.0BCastelle
0.0BJakks Pacific
0.0BINNOVATIVE SOFTWARE
0.0BBIOSTIM
0.0BENVIRONMENTAL TESTING
0.0BMed-Design
0.0BIbis Technology
0.0BBlyth Holdings
0.0BMedwave
0.0BBFI COMMUNICATIONS
0.0BCONSCO ENTERPRISES
0.0BBIOCHEM INTERNATIONAL
0.0BANTENNAS FOR COMM.
0.0BBarrister Information Systems
0.0BP.C. TELEMART INC.
0.0BSCIENTIFIC COMMUN.
0.0BDATAKEY, INC.
0.0BRGB Computer & Video
0.0BTelesoft
0.0BCognitive Systems
0.0BObjective Communication
0.0BVANZETTI SYSTEMS
0.0BMicrowave Labs
0.0BRENAL SYSTEMS
0.0BWORLCO DATA SYSTEMS
0.0BTechnology Development
0.0BInnodata
0.0BM-Wave
0.0BSysComm International Corp
0.0BAutoinfo
0.0BSamna
0.0BII-VI
0.0BPhoton Technology Intl
0.0BMustang Software
0.0BII MORROW INC.
0.0BTRIANGLE MICROWAVE
0.0BBIOMET INC
0.0BRobocom Systems
0.0BCSP INC
0.0BSTOCKHOLDER SYSTEMS
0.0BIntramed Laboratories
0.0BElexis
0.0BEltek Ltd
0.0BSAC Technologies
0.0BFrisco Bay Industries Ltd
0.0BCompuRAD
0.0BKMW SYSTEMS CORP.
0.0BNITRON
0.0BCOM SYSTEMS
0.0BPACE Health Management
0.0BBell Technology Group
0.0BPHARMACONTROL
0.0BTELECI, INC.
0.0BMAGNETIC INFO. TECH.
0.0BUnited States Paging
0.0BRSI Systems
0.0BINTEGRATED CIRCUITS
0.0BEdison Control
0.0BPYRAMID MAGNETICS
0.0BBALLARD MEDICAL
0.0BEuroMed
0.0BTANO CORP
0.0BJenkon International
0.0BCellular
0.0BSigmaTron International
0.0BNOVAR ELECTRONICS
0.0BBEDFORD COMPUTER
0.0BCode-Alarm
0.0BJinpan International Ltd
0.0BTOTAL ASSETS
0.0BVerticom
0.0BC2I Solutions
0.0BIBS Interactive
0.0BXeta
0.0BCom/Tech Communication
0.0BGurunet Corp
0.0BTelecalc
0.0BCOMPUSAVE CORP.
0.0BGateway Data Sciences
0.0BComtrex Systems
0.0BENDOTRONICS, INC.
0.0BDAY TELECOMMUNIC.
0.0BUrsus Telecom Corporation
0.0BOld Dominion Systems
0.0BAdvanced Instl Mgmt Software
0.0BInnovative Tech Systems
0.0BRENAL DEVICES
0.0BResearch Frontiers
0.0BDigital Optronics
0.0BGlobal Market Information
0.0BSigma Designs
0.0BCMC INTERNATIONAL
0.0BMicrofield Graphics
0.0BPATIENT TECH
0.0BCrystallume
0.0BSoloPoint
0.0BDIMIS
0.0BSmartserv Online
0.0BCERPROBE CORPORATION
0.0BMERRIMAC INDUSTRIES
0.0BNavarre
0.0BFANON/COURIER U.S.A.
0.0BZONIC
0.0BHomeCom Communications
0.0BDIDAX
0.0BHEALTH INFORMATION
0.0BCONCORD COMPUTING
0.0BUnitronix
0.0BCOMPONENT TECHNOLOGY
0.0BIntegrated Surgical Systems
0.0BGV MEDICAL, INC.
0.0BGlobal Telecommunication
0.0BLASER PHOTONICS
0.0BComputer Petroleum
0.0BShared Technologies Cellular
0.0BAltai
0.0BSoftware Professionals
0.0BBOMED MEDICAL LTD.
0.0BSimulations Plus
0.0BCARDIOSEARCH INC.
0.0BSemiconductor Laser Intl
0.0BGridComm
0.0BMicrion
0.0BPANCRETEC INC.
0.0BINTERACTIVE RADIATN.
0.0BPacer
0.0BHEI
0.0BManatron
0.0BComputer Outsourcing Services
0.0BNetwork Long Distance
0.0BDATAPOWER
0.0BMediware Information Systems
0.0BMultimedia Concepts
0.0BElectropharmacology
0.0BJavelin Systems
0.0BVikonics
0.0BLegacy Software
0.0BNetLive Communications
0.0BBorealis Technology
0.0BSPACE MICROWAVE
0.0BDefense Software & Systems
0.0BImage Guided Technologies
0.0BHARRIS & PAULSON
0.0BPERCEPTRONICS
0.0BBureau of Electronic
0.0BCHAD THERAPEUTICS
0.0BENSUN CORP.
0.0BFine.com Corp
0.0BCOMPUTRAC INSTRUM.
0.0BPHOENIX MEDICAL
0.0BApplied Intelligence Group
0.0BSelfCare
0.0BStyles on Video
0.0BQMAX TECHNOLOGY
0.0BELECTRONIC FINANCIAL
0.0BCITISOURCE INC.
0.0BPERSONAL COMPUTER
0.0BParavant Computer Systems
0.0BSILICON ELECTRO-PHYSIC
0.0BSAZTEC International
0.0BSPAN-AMERICAN MEDICAL
0.0BGeneral Sciences
0.0BINVENTION, DESIGN
0.0BDeltaPoint
0.0BPSYCH SYSTEMS
0.0BPrecis Smart Card Systems
0.0BCompu-Dawn
0.0BLifeRate Systems
0.0BTELEPHONE SUPPORT
0.0BCandela Laser
0.0BDynatem
0.0BBIO-LOGIC SYSTEMS
0.0BConceptronic
0.0BLaserSight,
0.0BFINAL TEST, INC.
0.0BRainbow Technologies
0.0BComputer Telephone
0.0BDiasys
0.0BWorld Group Companies
0.0B3Net Systems
0.0BNationwide Cellular Service
0.0BWRIGHT LABORATORIES
0.0BImage Management Systems
0.0BHemodynamics
0.0BDigital Data Networks
0.0BSigma Circuits
0.0BCAM Data Systems
0.0BBKC Semiconductors
0.0BAdvanced Electronic Support
0.0BINT'L MEDICAL SYSTEMS
0.0BHungarian Telephone & Cable
0.0BCircuit Systems
0.0BKEY IMAGE SYSTEMS
0.0BUStel
0.0BJMAR Industries
0.0BRimage
0.0BSELECT INFORMATION
0.0BXiox
0.0BHouston Biomedical
0.0BMikron Instrument
0.0BKAPPA NETWORK
0.0BDATA MEASUREMENT
0.0B104281613131298776 [Fork](https://observablehq.com/@observablehq/plot-the-facebook-ipo "Open on Observable")

js

```
Plot.plot({
  insetRight: 10,
  height: 790,
  marks: [\
    Plot.dot(\
      ipos,\
      Plot.dodgeY({\
        x: "date",\
        r: "rMVOP",\
        title: (d) => `${d.NAME}\n${(d.rMVOP / 1e3).toFixed(1)}B`,\
        fill: "currentColor"\
      })\
    ),\
    Plot.text(\
      ipos,\
      Plot.dodgeY({\
        filter: (d) => d.rMVOP > 5e3,\
        x: "date",\
        r: "rMVOP",\
        text: (d) => (d.rMVOP / 1e3).toFixed(),\
        fill: "white",\
        pointerEvents: "none"\
      })\
    )\
  ]
})
```

The dodge transform can be used with any mark that supports **x** and **y** position. Below, we use the [text mark](https://observablehq.com/plot/marks/text) instead to show company valuations (in billions).

1980198519901995200020052010104.1Facebook27.7Google 15.6Corvis Corp13.2Infonet Services Corp12.8Groupon 12.4KPNQwest8.7MetroPCS Communications 8.0Yandex NV7.3Equant NV7.0Zynga 6.5WebVan Group 4.8McCaw Cellular Communications4.4Clearwire Corp4.3SGS-Thomson Microelectronics4.3LinkedIn Corp4.2Iridium World Communications4.1Flag Telecom Holdings Ltd4.1Verisk Analytics 4.0ONI Systems Corp4.0Sycamore Networks 3.9NorthPoint Communications Grp3.6Oplink Communications 3.6Teleport Communications Group3.5Transmeta Corp3.4APPLE COMPUTER3.4ICO Global Communications3.3Handspring 3.2Storagenetworks 3.2Akamai Technologies 3.1Sensata Tech Hldg NV3.1Priceline.com 3.0Cosine Communications 3.0CIENA Corp2.9Vonage Hldgs Corp2.9Avanex Corp2.9JD Edwards & Company2.8Boston Scientific2.7eToys 2.6Pandora Media 2.5MP3.COM 2.5PanAmSat2.3Excel Communications2.3Juniper Networks2.3TeleCorp PCS 2.2DIASONICS, INC.2.2NetZero 2.2Buy.com 2.2Freemarkets 2.2Onvia.com 2.2Niku Corp2.2HomeAway 2.1Telesystem International2.1Cellcom Israel Ltd2.1Dolby Laboratories 2.1UTStarcom 2.1Tellium 2.1Organic 2.0Internet Capital Group2.0Rhythms NetConnections2.0Garmin Ltd2.0HomeGrocer.com1.9Silicon Laboratories 1.9Perot Systems Corp1.9Foundry Networks 1.9Avici Systems 1.8Sonus Networks 1.8Homestore.com 1.8Blue Martini Software 1.7Avenue A 1.71-800-Flowers.com 1.7Gigamedia Ltd1.7Bell Canada International 1.7At Home Corp1.7e Machines 1.7InterNAP Network Services1.7NetSuite 1.7Gateway 20001.7TELEVIDEO SYSTEMS1.6Marvell Technology Group Ltd1.6Divine Interventures 1.6Netscape Communications1.6VA Linux Systems 1.6IMPSAT Fiber Networks 1.6Splunk 1.6Universal Access 1.6Exfo Electro Optical1.5New Focus 1.5ArrowPoint Communications 1.5Indigo1.5Rackspace Hosting 1.5Allied Riser Communications Co1.5XYLAN1.5webMethods 1.5Fusion-io 1.5PeoplePC 1.4NetScreen Technologies 1.4VIA NET.WORKS 1.4Triton PCS Holdings 1.4Netpliance 1.4Portal Software 1.4Ariba 1.4Broadcom Corp1.4Demand Media 1.4iBeam Broadcasting Corp1.4Univision Communications1.4Selectica 1.4LookSmart Ltd1.3Ubiquiti Networks 1.3Value America 1.3Global TeleSystems Group 1.3724 Solutions 1.3Alamosa PCS Holdings 1.3SalesForce.com 1.3Telocity Delaware 1.3Finisar 1.3Orbitz 1.3McLeod1.3Red Hat 1.2MatrixOne 1.2Amkor Technology 1.2Pixar1.2CompuWare1.2ExactTarget 1.2LSI LOGIC CORP.1.2GT Interactive Software1.2Versata 1.2Infinera Corp1.2AGENCY.COM Ltd1.2AsiaInfo Holdings 1.2OptionsXpress Holdings 1.2Nextcard 1.2CellNet Data Systems1.2Equinix 1.1Network Plus Corp1.1NextLink Communications 1.1FORTUNE SYSTEMS1.1Marquette Electronics1.1Cogent 1.1Turnstone Systems 1.1Covad Communications Group 1.1Exult 1.1Critical Path 1.1US Internetworking 1.1FirstWorld Communications 1.1Extreme Networks1.1PlanetRx.com 1.1Microsoft1.1Star Media Network 1.1Software Technologies Corp1.1RiskMetrics Group 1.1CacheFlow 1.0Advanced Fibre Communications1.0Allegiance Telecom 1.0Omnipoint1.0Focal Communications Corp1.0Accuray 1.0iXL Enterprises 1.0Drugstore.com 1.0OmniSky Corp1.0Cypress Communications Corp1.0Tomotherapy Incorporated1.0Lante Corp1.0Verio 1.0Ipass 1.0Hyperion Telecommunications1.0APOLLO COMPUTER1.0Paging Network1.0GoAmerica 1.0Neoforma.com 1.0eBay 1.0Alteon Websystems 1.0Accelerated Networks 1.0Millennial Media 1.0Sunrise Telecom 1.0Integrated Telecom Express 1.0Paypal 1.0Register.com 1.0Inet Technologies 1.0Tickets.com1.0iVillage 0.9Excel Switching Corp0.9FirePond 0.9Arterial Vascular Engineering0.9Scient Corporation0.93PAR 0.9InterTrust Technologies Corp0.9TheraSense 0.9Net 2000 Communications 0.9High Speed Access Corp0.9Aruba Networks 0.9Bruker Daltonics 0.9Yelp 0.9IXIA Communications0.9Goto.com0.9Sina.com0.9McClatchy Newspapers0.9Liberate Technologies0.9Corio 0.9Dice Holdings 0.9Isilon Systems0.9Sun Microsystems0.9ASM Lithography Holding0.9E-Stamp Corp0.9CTI Molecular Imaging 0.9M/A-COM Technology Solutions0.9Mercadolibre 0.9Aclara Biosciences 0.9Wit Capital Group 0.9Objective Systems Integrators0.8MetaSolv Software 0.8Data Domain 0.8InterXion Holding NV0.8Fortinet 0.8Brooks Fiber Properties0.8SolarWinds 0.8CheckFree0.8El Sitio International Corp0.8Saba Software 0.8Software.com 0.8Creative Technology0.8Centillium Communications 0.8Starent Networks Corp0.8Pacific Biosciences of CA 0.8Chordiant Software 0.8KAYPRO CORPORATION0.8Bigband Networks 0.8Advanced Switching Communic0.8Cobalt Networks 0.8American Mobile Satellite0.8The Active Network 0.8ev3 0.8Microtune 0.8Wireless Facilities 0.8RealD 0.8Lexent 0.8ESS Technology0.8Saifun Semiconductors Ltd0.8Quintus Corp0.8TenFold Corp0.8Insweb Corp0.8Nova0.8Qlik Technologies 0.8Atheros Communications 0.8interWAVE Communications0.8GT Group Telecom 0.7SplitRock Services 0.7Illuminet Holdings 0.7Hypercom Corp0.7Cabletron Systems0.7Multilink Technology Corp0.7Healtheon Corp0.7PageMart Wireless0.7Interland 0.7Network Engines 0.7InPhonic 0.7NexGen 0.7Efficient Networks 0.7Netezza Corp0.7Angie's List 0.7Loudeye Technologies 0.7Open Market0.7Heartport0.7Ondisplay 0.7Resonate 0.7Network Access Solutions Corp0.7E-Loan 0.7MedicaLogic 0.7Quest Software 0.7GeoCities0.7ALTOS COMPUTERS0.7Jive Software 0.7Internatnl Network Services0.7Infoblox 0.7IXC Communications0.7Quokka Sports 0.7DecisionOne0.7Riverbed Technology 0.7Caldera Systems 0.7i2 Technologies0.7RealPage 0.7Telular0.7Gadzoox Networks 0.7Qiao Xing Mobile Commun0.7Delano Technology Corp0.7QuinStreet 0.7Bazaarvoice 0.7UNGERMANN-BASS, INC.0.7PATHCOM0.7ElectroCom Automation0.7Getthere.Com 0.7Higher One Holdings 0.7Lightspan Partnership 0.7Vignette Corp0.7Telco Communications Group0.7iAsia Works 0.7DealerTrack Holdings0.7Kyphon 0.7MIPS Computer Systems0.7Triton Network Systems 0.7Webex Communications 0.7AMDAHL0.7ibasis 0.7Phone.com 0.7Brocade Comm Sys 0.7Guidewire Software 0.7CheckPoint Software Tech0.7Illumina 0.7Ubiquitel 0.6Opus360 Corp0.6Vitria Technology 0.6Redback Networks 0.6BSquare Corp0.6MapQuest.com 0.6COMPUTER LANGUAGE0.6Ashford.Com 0.6Asiacontent.com Ltd0.6Arrow International0.6Chemdex Corp0.6HighwayMaster Communications0.6FTP Software0.6LOTUS DEVELOPMENT0.6INTECOM INC0.6Commerce One 0.6OTG Software 0.6Emerge Interactive 0.6Copper Mountain Networks 0.6Vastera 0.6COMPAQ COMPUTER0.6Zapme Corp0.6SiRF Technology Holdings 0.6Switch And Data 0.6Wink Communications 0.6CONVERGENT TECH0.6athenahealth 0.6Calico Commerce 0.6Crossroads Systems 0.6Support.com 0.6Marimba 0.6Nuance Communications 0.6Sigmatel 0.6Cornerstone OnDemand 0.6Juno Online Services 0.6Digitalthink 0.6Data Return Corp0.6Women.com Networks0.6Acme Packet 0.6Vicinity Corp0.6TheStreet.com0.6Ancestry.com0.6Tessera Technologies 0.6OccuLogix 0.6Shopping.com Ltd0.6Extensity 0.6InvenSense 0.6EndWave Corp0.6Amazon.com 0.6DivX 0.6Vyyo 0.6Cypress Semiconductor0.6FairMarket 0.6QAD 0.6Harris Interactive 0.6ScreamingMedia 0.6ARTISTdirect 0.6Verifone0.6ICx Technologies 0.6UUNet Technologies0.6WorldGate Communications 0.6PRIAM CORPORATION0.6Luminant Worldwide Corp0.6DSL.net 0.6OneMain.com 0.6Docent 0.6DYSAN0.6Performance Systems0.6MicroStrategy 0.6Musicmaker.com 0.6Santa Cruz Operation0.6Cavium Networks 0.6FormFactor 0.6Interliant 0.6LEE DATA0.6MetroNet Communications Corp0.6Pinnacle Holdings 0.6Therma-Wave 0.6ITXC Corp0.6Kana Communications 0.6Aether Systems 0.6Agile Software Corp0.6JNI Corp0.6Witness Systems 0.6E.piphany 0.6Visicu 0.6Loudcloud 0.6TechTarget 0.6ITC Deltacom0.6Autobytel.com 0.6VistaPrint Limited0.5Forte Software0.5Hittite Microwave Corp0.5CSG Systems International0.5Novatel Wireless 0.5Predictive Systems 0.5SMTC Corp0.5InterWorld Corp0.5SuccessFactors 0.5Quantum Effect Devices 0.5USCS International0.5Cyberian Outpost0.5ShopNow.com 0.5Zillow 0.5IDX Systems0.5Vixel Corp0.5Skullcandy 0.5Mellanox Technologies Ltd0.5K12 0.5Floware Wireless Systems Ltd0.5@Road 0.5Cylink0.5QUALCOMM0.5Numerical Technologies 0.5MICRON TECHNOLOGY0.5RealNetworks 0.5Computron Software0.5US LEC Corp0.5NightHawk Radiology Holdings0.5Premiere Technologies0.5Sohu.com 0.5Responsys 0.5SciQuest.com 0.5Clarent Corp0.5Fogdog Sports 0.5Packeteer 0.5Vina Technologies 0.5INTERGRAPH0.5AvantGo 0.5Genomica Corp0.5LHS Group 0.5Razorfish 0.5MENTOR GRAPHICS0.5Teradata0.5Affinity Technology Group0.5Clearnet Communications0.5General Magic0.5Mpath Interactive 0.5Stamps.com 0.5TeleCommunications Systems 0.5Netcentives 0.5Conner Peripherals0.5SYSTEMS & COMPUTERS0.5Read-Rite0.5SignalSoft Corp0.5Intraware 0.5Inktomi Corporation0.5Aspec Technology 0.5ARBINET THEXCHANGE INC0.5CenCall Communications0.5Artisoft0.5Kanbay International 0.5Alliance Fiber Optic Products0.5Ventritex0.5DAISY SYSTEMS0.5Interwoven 0.5Mediaplex 0.5MICOM SYSTEMS0.5Convergent Communications 0.5Comscore 0.5Art Technology Group 0.5ISS Group 0.5ADTRAN0.5Inforte Corp0.5Evoke Communications 0.5Yahoo!0.5Click Commerce 0.5MakeMyTrip Ltd0.5China.com Corp0.5CAIS Internet 0.5Airvana 0.5STRATUS COMPUTER0.5Conor Medsystems 0.5net.Genesis Corp0.5Palmer Wireless0.5Calix 0.5BladeLogic 0.5Genesys Telecommun Labs0.5EMC0.5Documentum0.5Optium Corp0.5Manhattan Associates 0.5Digital Impact 0.5Advanced Analogic Technologies0.5FlyCast Communications0.5Magma Design Automation 0.5Constant Contact 0.5Netro Corporation0.5RADVision Ltd0.5MINISCRIBECORP.0.5SEAGATE TECHNOLOGY0.5Everex Systems0.5Autoweb.com0.5BE Semiconductor Industries0.5Medscape 0.5Lantronix 0.5Prime Response 0.5Vanguard Cellular Systems0.5Pixelworks 0.5LoopNet 0.53DO0.5Galileo Technology 0.5Mastech0.5USN Communications0.5Demandware 0.5MASSTOR SYSTEMS0.5NVidia Corporation0.5AUTOMATIX INCORPORATED0.5Stac Electronics0.5Ask Jeeves 0.5Leadis Technology 0.5SemiLEDs Corp0.5Websense 0.5Digital Island 0.5Metro Mobile CTS0.5Canadian Solar 0.5VLSI TECHNOLOGY0.5Cyrix0.5Pegasystems0.5MKS Instruments0.5Synnex Information Tech 0.5OpenTable 0.5Neutral Tandem 0.4Eprise Corp0.4Tadiran0.4i3 Mobile 0.4PortalPlayer 0.4eGain Communications0.4ZY MOS CORPORATION0.4SRA International 0.4Blaze Software 0.4Mortgage.com 0.4SonicWALL 0.4ORBCOMM 0.4BEA Systems 0.4National Instruments0.4Ness Technologies 0.4HouseValues 0.4Precise Software Solutions Ltd0.4Entropic Communications 0.4E\*Trade Group0.4Boingo Wireless 0.4Internet.com Corp0.4AppliedTheory Corporation0.4Viant Corp0.4Bruker AXS 0.4Ceragon Networks Ltd0.4Compellent Technologies 0.4MMC Networks 0.4Caliper Technologies Corp0.4Infoseek0.4United Video Satellite Group0.4Metawave Communications0.4CardioNet 0.4MaxLinear 0.4Evolve Software 0.4Auspex Systems0.4L90 0.4Egreetings Network 0.4Keynote Systems 0.4Nellcor0.4Transition Systems0.4Digital Lightwave 0.4QUANTUM CORP0.4ZELTIQ Aesthetics 0.4Centra Software 0.4MASS. COMPUTER CORP.0.4Blue Nile 0.4SERENA Software 0.4Be Free 0.4Intermolecular 0.4Cheap Tickets 0.4Aldus0.4Broadcast.Com 0.4Insulet Corp0.4Telegroup 0.4JFAX Com 0.4Blackboard 0.4AirNet Communications Corp0.4Destia Communications 0.4Proxicom 0.4MAI Basic Four0.4Teleconnect0.4Heart Technology0.4Sybase0.4Official Payments Corp0.4InfoSpace.com0.4Infinity Financial Technology0.4Dallas-Semiconductor0.4Network Equipment Technologies0.4Yurie Systems 0.4Interactive Pictures Corp0.4Ebenx 0.4Healthextras 0.4Silicon Image 0.4Alpha & Omega Semiconductor Lt0.4Jupiter Communications 0.4Northstar Neuroscience 0.4Sync Research0.4Stanford Microdevices 0.4Eclipsys Corp0.4Wellfleet Communications0.4Tanning Technology Corp0.4Net Perceptions 0.4Talarian Corp0.4Imperva 0.4Business Objects0.4Oracle Systems0.4Xtent 0.4Convergent Group Corp0.4Multex.com 0.4CareerBuilder 0.4Industri-Matematik0.4Apropos Technology 0.4Shutterfly 0.4EAGLE COMPUTER0.4IntraLase Corp0.4Avistar Communications Corp0.4Integrated Information Systems0.4MiningCo.com 0.4Talk City 0.4Xilinx0.4PECO II 0.4BioForm Medical 0.4NeoMagic Corp0.4Discreet Logic0.4Pemstar 0.4KEY TRONIC CORP.0.4Pure Software0.4Proofpoint 0.4AdForce 0.4MGC Communications 0.4VeriSign 0.4Netflix.com 0.4Cisco Systems0.4MCK Communications 0.4Viatel0.4Callidus Software 0.4Atlantic Tel-Network0.4Syntel 0.4Pets.com 0.4Novadigm0.4iprint.com 0.4Sourcefire 0.4NetScout Systems 0.4Carrier Access Corporation0.4C30.4Siebel Systems0.4JAMDAT Mobile 0.4Advanced Communications Group0.4Oratec Interventions 0.4Monolithic System Technology0.4Telematics International0.4Web Street 0.4C-bridge Internet Solutions0.4OpenVision Technologies0.4Sawtek0.4FoxHollow Technologies 0.4Exodus Communications 0.4SilverStream Software 0.4Synopsys0.4Virata Corp0.4Advantage Learning System 0.4Netzee 0.4Internet Brands 0.4SmarterKids com 0.4MONOLITHIC MEMORIES0.4Liquid Audio 0.4Andover.net 0.4I Many 0.4CCC Information Srvcs Group0.4XCarenet 0.4Omnivision Technologies 0.4N2H2 0.4Elcom International0.4ReachLocal 0.4PNV 0.4LogMeIn 0.4Epocrates 0.4Rambus 0.4DoubleClick 0.4Glu Mobile 0.4VALID LOGIC SYSTEMS0.4MICROPOLIS CORP.0.4PC-Tel 0.4Cbeyond Communications 0.4TANDON0.4Launch Media 0.4PAR TECHNOLOGY0.4Metro Networks0.4coolsavings.com inc0.4Acuson0.4Eloquent 0.4iMagicTV0.4Taleo Corp0.3TELLABS0.3Dexcom 0.3Veraz Networks 0.3Nova Measuring Instruments0.3Exabyte0.3Transgenomic 0.3Vocera Communications 0.3Virtusa Corp0.3Mobius Management Systems 0.3O2Wireless Solutions 0.3Bluestone Software 0.3VerticalNet 0.3TERA CORP0.3ImproveNet 0.3Vitacost.com 0.3Edify0.3Intuit0.3Fabrinet0.3Active Software 0.3CellularVision USA0.3Capella Education Co0.3C-Cube Microsystems0.3Tumbleweed Communications Corp0.3Open Solutions 0.3CardioGenesis0.3Telaxis Communications Corp0.3Sunquest Information Systems0.3ZYCAD CORP.0.3NetRatings 0.3Triple P0.3Open Text0.3Tripath Technology 0.3OneWave0.3EQUATORIAL COMMUNIC.0.3Omega Research 0.3PDF Solutions 0.3Aspect Development0.3Atmel0.3BroadBand Technologies0.3Davidson & Associates0.3Pacific Gateway Exchange0.3GRIC Communications 0.3CardioThoracic Systems0.3TeleNav 0.3drkoop.com 0.3Ikanos Communications 0.3HPL Technologies 0.3Nassda Corp0.3AudioCodes Ltd0.3SS&C Technologies0.3DORADO MICRO SYSTEMS0.3Westell Technologies 0.3CDnow 0.3Metro Information Services 0.3Golden Telecom 0.3012 Smile.Communications Ltd0.3Student Advantage 0.3PRT Group 0.3Medidata Solutions 0.3Sapient0.3EHealth 0.3CrossWorlds Software 0.3Omniture 0.3software.net Corp0.3Broadbase Software 0.3Animas Corp0.3US Auto Parts Networks 0.3Micro Warehouse0.3Visioneer0.3Orckit Communications0.3Sandisk0.3LCC International0.3Quarterdeck Office Systems0.3Corel0.3Watchguard Technologies 0.3Digimarc Corp0.3Memco Software0.3Network Appliance0.3Prism Solutions0.3Xircom0.3Power-One 0.3Digital Microwave0.3Oak Technology0.3Sykes Enterprises0.3CyberSource 0.3USWeb Corp0.3Breakaway Solutions 0.3iManage 0.3Tangoe 0.3DemandTec 0.3Syneron Medical Ltd0.3Virage 0.3Gupta0.3Aksys0.3Smart Modular Technologies0.3Maker Communications 0.3Synaptics 0.3AuthenTec 0.3Igo Corp0.3Aspect Medical Systems 0.3Phase Forward 0.3Visio0.3Tvia 0.3PEC Solutions 0.3Plumtree Software 0.3Advanced Energy Industries0.3Pros Holdings 0.3Corillian Corp0.3VideoServer0.3Informatica Corp0.3Telvent SA0.3Echelon Corp0.3Trans1 0.3LivePerson 0.3Trident Microsystems0.3Fore Systems0.3Cascade Communications0.3MetaTools0.3TRIAD SYSTEMS0.3Avid Technology0.3Nuvasive0.3FlashNet Communications 0.3FileNet0.3Zebra Technologies0.3Liquidity Services 0.3AeroGen 0.3Virtual Radiologic Corp0.3C/NET0.3Audible 0.3Silknet Software 0.3Mail.com 0.3ANSYS0.3Silicon Storage Technology0.3Tivoli Systems0.3Yesmail.com 0.3Verilink0.3Seer Technologies0.3Motive 0.3Rudolph Technologies 0.3Latitude Communications 0.3Affiliated Computer Services0.3Cytyc0.3SEEQ TECHNOLOGY0.3IDT0.3Internet Gold-Golden Lines Ltd0.3Ramp Networks 0.3Daleen Technologies 0.324/7 Media 0.3Opnet Technologies 0.3N2K 0.3Virage Logic Corp0.3Emageon 0.3ASE Test0.3Mainspring 0.3Inphi Corp0.3Rubicon Technology 0.3Genesis Microchip 0.3Globalstar Telecommunications0.3ASHTON-TATE0.3Hotjobs Com LTD0.3CINCINNATI MICRO.0.3Private Business 0.3Alliant Computer Systems0.3INTEGRATED DEVICE0.3Healthcentral.com 0.3Visual Networks0.3COM21 0.3ArcSight 0.3Brightcove 0.3ChipSoft0.3Purchasepro.com 0.3Brooktree0.3MarketAxess Holdings 0.3Computer Access Technology0.3Integrated Silicon Solutions0.3Terayon Communication Systems0.3Onyx Software Corp0.3IOMEGA CORPORATION0.3Great Plains Software 0.3Alloy Online 0.3Relational Technology0.3Sagent Technology 0.3Accord Networks Ltd0.3Red Brick Systems0.3ValiCert 0.3Digital Insight Corp0.3ETINUUM INC0.3Sequoia Software Corp0.3Volcano Corp0.3Powersoft0.3Peritus Software Services 0.3McAfee Associates0.3Mission Critical Software 0.3Guidance Software0.3Envestnet 0.3General Surgical Innovations0.3PeopleSoft0.3Concur Technologies 0.3HBO & COMPANY0.3Allaire Corp0.3SOFTWARE AG0.3Komag0.3Cidco0.3Pacific Internet Pte Ltd0.3Network Computing Devices0.3Allot Communications 0.3Media Vision Technology0.3Premenos Technology0.3Mind C.T.I. Ltd0.3SYMBOLICS INC.0.3Walker Interactive Systems0.3PowerCerv0.3SeaChange International0.3Technology Solutions0.3Synchronoss Technologies 0.3PANSOPHIC SYSTEMS0.3Premisys Communications0.3Greenway Medical Tech 0.3Intl Microelectronic Products0.3Pyramid Technology0.3Box Hill Systems Corp0.3MAGNUSON COMPUTER0.3NAMIC USA0.3Quotesmith.com 0.3Garden.com 0.3Persistence Software 0.3GTECH CORPORATION0.3Datalogix International0.3Be 0.3SmartDisk(Toshiba,Fischer)0.3Silicon Graphics0.3HOGAN SYSTEMS0.3Corsair Communications 0.3Digital Systems International0.3INTERTEC DATA0.3LendingTree 0.3Medical Manager Corp0.3Arbor Software0.3Nanogen 0.3LIEBERT0.3Excite 0.3Netlogic Microsystems0.3Curon Medical 0.3Cirrus Logic0.3FriendFinder Networks 0.3Webstakes.com 0.3MTI Technology0.3INFOTRON SYSTEMS0.3First Virtual Corp0.3PSi Technologies 0.3PairGain Technologies0.3Repeater Technologies 0.3Primus Telecommunications0.3Pilot Network Services0.3SmarTalk TeleServices0.3Banyan Systems0.3Tut Systems 0.3Raptor Systems0.3RSL Communications Ltd0.3MediSense0.3Object Design0.3ATV SYSTEMS, INC.0.3CommTouch Software 0.3Accrue Software 0.3Northeast Optic Network 0.3Nextest Systems Corp0.3MotherNature.com 0.3Aware0.3Remedy0.3Netcreations 0.3PLX Technology 0.3International Integration 0.3Powerwave Technologies0.3Citrix Systems0.3Sequent Computer Systems0.3NeoPhotonics Corp0.3CrossKeys Systems Corp0.3Linear Technology0.3CyberCash0.3Metalink LTD0.3Traffic.com 0.3Digital Sound0.3STAR TECHNOLOGIES0.3First Pacific Networks0.3Digirad Corp0.3Deltek Systems 0.3Bindview Development0.3VMX, INC.0.3Fluidigm Corp0.3Goal Systems International0.3Viewlogic Systems0.3VNUS Medical Technologies 0.3Trimble Navigation0.3PowerDsine Ltd0.3GeoScience0.3Maxis0.3Convex Computer0.3MyPoints.com 0.3Wall Data0.3Aurum Software0.3SynQuest 0.3Stereotaxis 0.3Cysive 0.3Farallon Communications0.3US Xpress Enterprises0.3Horizon Medical Products 0.3Tel-Save Holdings0.3Cardiac Pathways0.3FlexiInternational Software0.3Aspect Telecommunications0.3I-Stat0.3Double-Take Software0.3CyberMedia0.3ANDREW0.2Mercury Interactive0.2Xoom.com 0.2F5 Networks 0.2AirGate PCS 0.2Racotek0.2Super Micro Computer 0.2Ravisent Technologies 0.2US Interactive 0.2Immersion Corp0.2RWD Technologies 0.2HealthGate Data Corp0.2Registry0.2Phoenix Technologies0.2Polycom0.2UroMed0.2Cobalt Group 0.2BMC Software0.2RF Micro Devices 0.2Carreker-Antinori 0.2Memsic 0.2Actel0.2Transaction Systems0.2Synplicity 0.2Boston Communications Group0.2KnowledgeWare0.2Dell Computer0.2NETWORK SYSTEMS0.2Borland International0.2Dialogic0.2Smith Micro Software0.2Cellular Information Systems0.2FreeShop.com 0.2Micromuse, 0.2Carbonite 0.2Frame Technology0.2Envivio0.2Individual0.2ZipLink 0.2Streamline.com 0.2Astea International0.2Radware Ltd0.2RightNow Technologies 0.2TriZetto Group 0.2QuickLogic Corp0.2Enphase Energy 0.2CIRCON CORPORATION0.2SUPERTEX, INC.0.2Encore Computer0.2APPLIED CIRCUIT0.2SYSTEMS INTEGRATORS0.2Video Lottery Technologies0.2Fastnet Corp0.2Home Diagnostics 0.2Intelligent Life Corp0.2Cybergold 0.2NetSolve 0.2VocalTec0.2ServiceWare Technologies 0.2NxStage Medical 0.2Wonderware0.2Interactive Intelligence 0.2MIDCOM Communications0.2Ascend Communications0.2Pharsight Corp0.2RRSat Global Communications0.2Electronic Retailing Systems0.2Lernout en Hauspie0.2ARCHIVE CORP.0.2Overstock.com0.2FactSet Research Systems0.2Nogatech 0.23Dlabs 0.2SkillSoft Corp0.2HealthStream 0.2Clicksoftware Ltd0.2Data Technology0.2AboveNet Communications 0.2Meru Networks 0.2Lannet Data Communications0.2Shiva0.2Progress Software0.2Exactis.com 0.2Atlantic Data Services 0.2BroadSoft 0.2DATA I/O0.2JDA Software Group0.2Dendrite International0.2SHARED MEDICAL SYSTEMS0.2Quickturn Design Systems0.2PriCellular0.2Geotel Communications0.2ViryaNet LTD0.2Interleaf0.2INFORMATION RESOURCES0.2Proteon0.2Itron0.2Concord Communications 0.2MIM0.2Legato Systems0.2ON Technology0.2Concentric Network Corp0.2Microcell Telecommunications0.2Scientific Learning0.2MovieFone0.2Orion Network Systems0.2Quepasa.com 0.2FLOATING POINT SYSTEM0.2Radius0.2MANAGEMENT SCIENCE0.2ADVANCED SEMICONDUCTOR0.2Volterra Semiconductor Corp0.2Applied Micro Circuits Corp0.2Innova Corp0.2Simplex Solutions 0.2MARGAUX CONTROLS0.2eCollege.com0.2MiniMed0.2Ultimate Software Group0.2SalesLogix Corp0.2Best Power Technology0.2SpectraLink0.2Retix Corp0.2Ortel0.2Rita Medical Systems 0.2Computer Programs & Systems0.2Hoover's 0.2RadView Software Ltd0.2Endosonics0.2Unica Corp0.2Advanced Logic Research0.2HADCO CORP.0.2Tower Semiconductor0.2Evolving Systems 0.2Vantive0.2COMP-U-CARD0.2Brio Technology 0.2Cellular Communications0.24th Dimension Software0.2Immunicon Corp0.2Spectranetics0.2NetManage0.2Biopsys Medical0.2Lightbridge0.2Provide Commerce 0.2RoweCom 0.2Vitesse Semiconductor Corp0.2Preferred Networks0.2Xomed Surgical Products0.2@plan.inc0.2Natus Medical 0.2Scopus Technology0.2Teknekron Communications0.2Whittman-Hart0.2VarsityBooks.com 0.2Towne Services 0.2GEOPHYSICAL SYSTEMS0.2Online Resources & Commun0.2Bridge Communications0.2DSET Corp0.2Melita International Corp0.2US Robotics0.2Positron Fiber Systems Corp0.2Evergreen Solar 0.2ITI Technologies0.2MACNEAL-SCHWENDLER0.2InterVideo 0.2Actuate Software Corp0.2Mobility Electronics 0.2Helicos BioSciences Corp0.2Voltaire Ltd0.2DOCUMATION0.2Cepheid0.2CareScience 0.2Camtek Ltd0.2AXENT Technologies0.2BroadVision0.2SYNTREX INC0.2Primus Knowledge Solutions 0.2Morino0.2Kendall Square Research0.2DICEON ELECTRONICS0.2Power Med Interventions 0.2Platinum Technology0.2TresCom International0.2Lionbridge Technologies0.2Orthofix International0.2Asymetrix Learning Systems 0.2Vascular Solutions 0.2August Technology Corp0.2Collectors Universe 0.2Advanced Interventional Sys0.2SciQuest 0.2Best Software 0.2Aris Corp0.2S30.2Intellon Corp0.2WebTrends Corporation0.2Macromedia0.2Electronics for Imaging0.2General Parametrics0.2Alpharel0.2Star Telecommunications 0.2ECtel 0.2Flextronics International0.2Tricord Systems0.2Digital River 0.2Microware Systems0.2Trusted Information Systems0.2Zycon0.2Credence Systems0.2Excelan0.2TelCom Semiconductor0.2Information Management0.2Cooper & Chyan Technology0.2Hybrid Networks 0.2DIONEX CORP0.2Cadnetix0.2Viador 0.2Bamboo.com 0.2KOLFF MEDICAL, INC.0.2CORVUS SYSTEMS0.2Applied Digital Access0.2Website Pros 0.2XEBEC0.2ASD Systems 0.2nFront 0.2Peregrine Systems 0.2DepoTech0.2Abacus Direct0.2Infonautics0.2Bachman Information Sys 0.2Kintera 0.2BR COMMUNICATIONS0.2Knot 0.2VECTOR GRAPHIC0.2BURR-BROWN CORPORATION0.2Marchex 0.2SynOptics Communications0.2Number Nine Visual Technology0.2Desktop Data0.2Interntnl Telecommuncation0.2Marcam0.2eOn Communications Corp0.2Level One Communications 0.2Smith-Gardner & Associates 0.2Cognicase 0.2Altera0.2Chemtrak0.2InStent0.2Hall Kinion & Associates 0.2Synercom Technology0.23Dfx Interactive 0.2GRADCO SYSTEMS INC.0.2Octel Communications0.2Braun Consulting 0.2HireRight 0.2Clarify0.2Trunkbow Intl Hldgs Ltd0.2Urologix0.2DSP Group0.2OmniCell 0.2Teledata Communication0.2SCM Microsystems 0.2INTEGRATED SOFTWARE0.2Conceptus0.2Platinum Software0.2ELECTRO SCIENTIFIC0.2Healthetech 0.2Pervasive Software 0.2Vital Signs0.2Advent Software0.2ArcSys0.2Perclose0.2Summit Design0.2SYSTEMATICS0.2Cascade Microtech 0.2Teknowledge0.2SQA0.2Walsh International0.2Condor Technology Solutions0.2Flextronics0.2OSI Systems 0.2SPR 0.2Focal 0.2Syquest Technology0.2Logic Works0.2Firefox Communications0.2Document Sciences0.2Cynosure0.2RigNet 0.2Digital Link0.2FONAR0.2ISC SYSTEMS0.2Harbinger0.2PlanetOut 0.2Verity0.2Xionics Document Technologies0.23COM CORP.0.2Heartland Wireless0.2SILICON VALLEY GROUP0.2Innovative Solns & Support 0.2Micrus Endovascular Corp0.2Arthrocare0.2Bottomline Technologies 0.2Landacorp 0.2Enterprise Systems0.2Meta Software 0.2Information Storage Devices0.2ZIYAD INC.0.2General Scanning0.2Salary.com 0.2ParcPlace Systems0.2Impac Medical Systems0.2MICROPRO INT'L0.2Envoy0.2SCC Communications Corp0.2Microtest0.2EarthLink Network 0.2Neon Systems 0.2AutoCyte 0.2Pegasus Systems 0.2Workgroup Technology0.2International Imaging0.2Imagyn Medical0.2Parametric Technology0.2Plasma & Materials Tech0.2StrataCom0.2Catapult Communications0.2Maxtor0.2Cutera 0.2P-COM0.2Interspeed 0.2Intelligent Medical Imaging0.2Segue Software0.2KENTRON INT'L0.2Information Management Assocs0.2Cyberonics0.2AtriCure 0.2LanVision Systems0.2GSI Technology 0.2Artisan Components 0.2HPR0.2ONTRACK Data International0.2Cygnus Therapeutic Systems0.2Broderbund Software0.2IPC Information Systems0.2TTR 0.2Molecular Dynamics0.2NetGravity 0.2DATASOUTH COMPUTER0.2FARO Technologies 0.2Netframe Systems0.2CADO SYSTEMS0.2Puma Technology0.2ARGOSYSTEMS0.2SunGard Data Systems0.2USA Mobile Communications0.2AMISYS Managed Care Systems0.2Aradigm0.2Peerless Systems0.2LogicVision 0.2Vista Medical Technologies 0.2Alantec0.2QUALITY MICRO SYSTEMS0.2Verisity Ltd0.2TANDEM COMPUTERS0.2Vitalink Communications0.2CellPro0.2ECAD0.2K-TRON0.2Syntellect0.2Sage 0.2FINALCO GROUP0.2WavePhore0.2CONNECT0.2Software 20000.2MapInfo0.2Claremont Technology Group0.2SCB Computer Technology0.2Neopath0.2Advanced Power Technology 0.2VideoTelecom0.2Intelligroup0.2Catalyst International0.2DEVELCON ELECTRONICS0.2ESPS 0.2Moldflow Corp0.2Versatility0.2Open Environment0.2Digidesign0.2Vocus0.2T/R Systems 0.2Digex0.2Optical Sensors0.2Micro Linear0.2VENTREX LABS0.2Vitech America0.2DIGITAL COMMUNICATIONS0.2Netlist0.2Amtech0.2Secure Computing0.2Apex PC Solutions 0.2ACT Manufacturing0.2ImageX com 0.2WebSideStory 0.2Salon.com0.2SportsLine USA 0.2EarthWeb 0.2Impact Systems0.2BackWeb Technologies Ltd0.2Centex Telemanagement0.2Alliance Semiconductor0.2ReSourcePhoenix com0.2BreezeCOM 0.2Storm Technology0.2Jabil Circuit0.1Praegitzer Industries0.1SDL0.1Netrix0.1AST RESEARCH0.1Autodesk0.1ADE0.1Convio 0.1Radiant Systems 0.1Xyvision0.1Summa Four 0.1Gilat Satellite Networks0.1Global Village Communication0.1Britton Lee0.1Integrated Packaging Assembly0.1Structural Dynamics Research0.1GENRAD0.1NBI0.1Innotrac Corp0.1Edgar Online 0.1American Dental Laser0.1Data Processing Resources0.1Complete Business Solutions0.1Exchange Applications 0.1Nitinol Medical Technologies0.1QuickResponse Services0.1TV Filme0.1Channell Commercial0.1NetRadio Corp0.1IMNET Systems0.1NCI 0.1PROTOCOL COMPUTERS0.1Vision-Sciences0.1TELCO SYSTEMS0.1RedEnvelope 0.1ISOMEDIX, INC.0.1HeadHunter.NET 0.1Litronic 0.1New Era of Networks 0.1CardioPulmonics0.1TranSwitch0.1Oacis Healthcare Holdings0.1Metrocall0.1Omtool Ltd(ASA International)0.1EnteroMedics 0.1EndoVascular Technologies0.1CardioVascular Dynamics0.1Procom Technology0.1Mercury Computer Systems 0.1Asante Technologies0.1ZENTEC0.1APPLICON0.1Manugistics Group0.1VitalCom0.1Xpedite Systems0.1ASK COMPUTER SYSTEMS0.1Molecular Devices0.1Applied Immune Sciences0.1Weitek0.1MARQUEST MEDICAL0.1Intellicall0.1DAOU Systems 0.1CP Clare0.1BrightStar Information0.1Numar0.1Cybex0.1Tri-Point Medical0.1ONSALE 0.1HNC Software0.1Computer Motion 0.1SILICON SYSTEMS0.1Bam Entertainment 0.1Software Artistry0.1Fractal Design0.1Ultratech Stepper0.1Startec Global Communications0.1Interplay Entertainment0.1Sequoia Systems0.1ACT Networks0.1Nanophase Technologies Corp0.1Innotech0.1PerSeptive Biosystems0.1Electronic Arts0.1Judge Group 0.1AMERICAN SOFTWARE0.1ARI Network Services0.1Paradigm Technology0.1Overland Data 0.1Vantagemed Corp0.1State of the Art0.1CryoCor 0.1Telemate Net Software 0.1ANADIGICS0.1Security Dynamics Technologies0.18x8 0.1Unify0.1INVACARE CORP.0.1VM Software0.1Adaptec0.1ADFlex Solutions0.1GIGA-TRONICS0.1MEDIFLEX SYSTEMS0.1LTX CORP0.1Cambridge Heart0.1Data Critical Corp0.1TELXON CORPORATION0.1Printcafe Software 0.1IMRS0.1Aspen Technology0.1Netcom On-Line Communications0.1Spyglass0.1TGV Software0.1Xyplex0.1Fashionmall.com0.1SoundBite Communications 0.1Rogue Wave Software0.1SenoRx 0.1Visigenic Software0.1Chips and Technologies0.1Spectrian0.1Ross Systems0.1INTER-TEL0.1SCIENTIFIC MICRO SYS0.1MathSoft0.1Eldec0.1Zoran0.1First Virtual Holdings0.1PolyMedica Industries0.1Boca Research0.1Technology Modeling Assocs0.1Domain Technology0.1Continuus Software Corp0.1Synacor 0.1PRINTRONIX0.1Voxware0.1Parallan Computer0.1TechForce0.1Microchip Technology0.1APPLIED COMMUNICATIONS0.1BGS SYSTEMS0.1Power Integrations 0.1Integ0.1System Software Associates0.1Physicians Computer Network0.1Atria Software0.1Metro One Telecommunications0.1BANCTEC0.1WYSE TECHNOLOGY0.1AICorp0.1RADCOM Ltd0.1IPL SYSTEMS0.1Command Systems 0.1Integrated Systems0.1Kips Bay Medical 0.1Bionx Implants 0.1Arch Communications Group0.1NANOMETRICS INC.0.1theglobe.com inc0.1ON LINE SOFTWARE0.1Information Advantage Software0.1RICHARDSON ELEC.0.1ShowCase Corp0.1Restrac0.1Periphonics Corp0.1SQL Financials International0.1VODAVI TECHNOLOGY0.1InterVU 0.1ENDATA, INC.0.1Exide Electronics Group0.1Wind River Systems0.1Ellie Mae 0.1Microcom0.1In Focus Systems0.1Simulation Sciences0.1AVANT-GARDE0.1Surgical Laser Technologies0.1IKOS Systems0.1Protocol Systems0.1Proxima0.1Rural Cellular0.1Jacada Ltd0.1JetFax 0.1SAGE Software0.1INTELLIGENT SYSTEMS0.1GlobeComm Systems 0.1BOLT TECHNOLOGY0.1Credit Management Solutions0.1Reptron Electronics0.1Apache Medical Systems0.1NetSpeak Corp0.1CULLINANE0.1Micrel0.1DSP Communications0.1FDP CORPORATION0.1XcelleNet0.1Netivation.com 0.1White Pine Software0.1IDEXX Corp0.1PENTA SYSTEMS0.1Sabratek0.1SOUTHERN MEDIC & PHARM0.1ISOETEC Communications0.1Davox0.1Visible Genetics0.1Community Health Computing0.1Maxim Integrated Products0.1Renaissance Solutions0.1Megatest0.1Cornerstone Imaging0.1Epic Design Technology0.1KLA INSTRUMENTS0.1PixTech0.1FemRx0.1Telebit0.1TSI International Software Ltd0.1VERBATIM0.1Pericom Semiconductor Corp0.1TECH FOR COMM0.1Adobe Systems0.1Isocor0.1Universal Electronics0.1Symantec0.1HEALTHDYNE0.1CrossComm0.1Dataware Technologies0.1Qualix Group 0.1Internet America 0.1HTE 0.1Mattson Technology0.1Edunetics0.1Allin Communications0.1Cerner0.1AUTO-TROL TECHNOLOGY0.1Inference0.1RasterOps0.1BofI Holding 0.1Blonder Tongue Laboratories0.1Neurometrix 0.1Worldtalk Communications0.1SEI0.1Continental Circuits0.1Smartflex Systems0.1Endocardial Solutions 0.1Printrak International0.1Mathstar 0.1Caere0.1BEI Electronics0.1ViaGrafix Corp0.1Integrated Measurement Systems0.1Catalyst Semiconductor0.1INSTACOM0.1Optical Data Systems0.1Aehr Test Systems 0.1DataWorks0.1Informix0.1Tele-Matic0.1Mitek Surgical Products0.1Intevac Industries0.1Abaxis0.1ARIX0.1Medrad0.1Artificial Life 0.1SELECTERM, INC.0.1PARADYNE CORP0.1XICOR0.1Physician Support Systems0.1HHB Systems0.1Gilat Communications LTD0.1AMPLICA0.1VISUAL TECHNOLOGY0.1American Superconductor0.1Educational Insights0.1Scopus Video Networks0.1Point of Sale Ltd0.1RadiSys0.1BHC Financial0.1Mecon0.1Ultradata0.1Landmark Graphics0.1Landmark Systems Corp0.1Laserscope0.1Cardica 0.1Dial Page0.1Sonic Solutions0.1Fair Issac & Company0.1Asia Electronics Holding Co0.1PSW Technologies 0.1Transaction Network Services0.1onlinetradinginc.com0.1Kopin0.1Lattice Semiconductor0.1Microtec Research0.1Crystal Systems Solutions Ltd0.1CABG Medical 0.1GERBER SYSTEMS0.1Consilium0.1Emultek0.1Spacetec IMC0.1Lunar0.1Interactive Magic0.1COMPUTER ASSOCIATES0.1RADIONICS INC.0.1Fundtech Ltd0.1TYLAN0.1LJL Biosystems0.1Micronics Computers0.1Interspec0.1ABIOMED0.1A+ Communications0.1Realty Information Group 0.1Tel/Man0.1CATS Software0.1Uroquest Medical0.1LINEAR CORPORATION0.1Active Voice0.1Axiom 0.1WorldQuest Networks 0.1SOFTWARE PUBLISHING0.1Veritas Software0.1Wave Systems0.1Index Technology0.1TriTeal0.1DIAGNOSTIC PRODUCTS0.1America Online0.1Allied Healthcare Products0.1Oculus Innovative Sciences 0.1Brite Voice Systems0.1Quintalinux Ltd0.1AccelGraphics 0.1Simware0.1Learning0.1Tier Technologies 0.1Unison Software0.1HAEMONETICS0.1MONCHIK-WEBER0.1AUTOCLAVE ENGINEERS0.1XeTel0.1SuperMac Technology0.1FEI0.1ALPHA MICROSYSTEMS0.1TIME ENERGY SYSTEMS0.1QuadraMed0.1OPTi0.1MicroProse0.1ViaSat0.1STRYKER0.1Versant Object Technology0.1ZITEL CORPORATION0.1OrCAD0.1Applied Voice Technology0.1TRO Learning0.1ZST Digital Networks 0.1Tollgrade Communications0.1Computer Management Sciences0.1Proxim0.1Raster Graphics0.1Elamex0.1CIPHER DATA PRODUCTS0.1STANFORD TELECOMM.0.1Applied Microsystems0.1Triconex0.1SCI. SYSTEMS SERVICE0.1Communications Central0.1Summit Medical Systems0.1Micrografx0.1EqualNet Holdings0.1Eagle Point Software0.1Template Software 0.1NATIONAL BUS. SYS.0.1Digital Music Group 0.1VIASOFT0.1KEVEX0.1Ansoft0.1Phamis0.1LeCroy0.1Alloy Computer Products0.1ROLM0.1BiznessOnline.com 0.1Concentra0.1Vanguard Technologies Intl0.1ADAM Software0.1RIT Technologies Ltd0.1Zoll Medical0.1Fourth Shift0.1DEST0.1Log On America 0.1C-COR ELECTRONICS0.1Extended Systems 0.1Xylogics0.1Biomagnetic Technologies0.1NetStar0.1DATA TERMINAL0.1AG Associates0.1ImageMAX 0.1Perception Technology0.1Network General0.1GeoWorks 0.1Photon Dynamics 0.1EP Technologies0.1CRAY RESEARCH0.1PCD0.1FORMASTER CORPORATION0.1Softdesk0.1Kronos0.1Calypte Biomedical0.1Davel Communications Group0.1Aremissoft Corporation0.1Remec0.1VIALOG Corp0.1A Consulting Team 0.1Minnesota Educational0.1Analogy0.1MOSCOM0.1Electrostar0.1Videonics0.1ULTIMATE CORPORATION0.1LIFELINE SYSTEMS0.1Cardiometrics0.1Bytex0.1Value-Added Communications0.1Tencor Instruments0.1AVANTEK0.1Microwave Power Devices0.1Intermedia Communications0.1202 DATA SYSTEMS0.1Bird Medical Technologies0.1NCA0.1Elantec Semiconductor0.1VidaMed0.1Data Race0.1Integrated Silicon Systems0.1Physiometrix0.1Datalink Corp0.1GSE Systems0.1Computational Systems0.1Nephros 0.1IPC COMMUNICATIONS0.1Superconductor Technologies0.1VMark Software0.1Gensym0.1Interlink Computer Sciences0.1FLIR Systems0.1TriQuint Semiconductor0.1Audio Book Club 0.1QUALITY SYSTEMS0.1MicroBilt0.1Total Control Products 0.1AMER. MGMT. SYSTEMS0.1Accom0.1Micro Component Technology0.1Diametrics Medical0.1Tekelec0.1DETECTOR ELECTRONICS0.1Pinnacle Micro0.1ROBINSON NUGENT0.1CMC Industries0.1DATASWITCH0.1SYSTEMS ASSOCIATES0.1ODETICS0.1Signal Technology0.1Veeco Instruments0.1Network Peripherals0.1Conductus0.1Irwin Magnetic Systems0.1Iridex0.1SeaMED0.1GMIS0.1MECA Software0.1INFORMATICS0.1Xscribe0.1SystemSoft0.1Kofax Image Products0.1PARLEX CORPORATION0.1Cotelligent Group0.1NovAtel Inc(Alberta/Canada)0.1Broadway & Seymour0.1Applied Signal Technology0.1ANDOVER CONTROLS0.1Automated Language Processing0.1STB Systems0.1Datastream Systems0.1Hutchinson Technology0.1AMHERST ASSOCIATES0.1Cognex0.1Cardima 0.1IncrediMail Ltd0.1Ultrafem0.1Kentek Information Systems0.1IAT Multimedia 0.1Pinnacle Systems0.1CALIF. AMPLIFIER0.1ProNet0.1Autonomous Technologies0.1MANUFACTURING DATA0.1ELEC OF ISRAEL0.1Brock Control Systems0.1National FSI0.1EVANS & SUTHERLAND0.1AUTOMATED SYSTEMS0.1Take To Auction.com 0.1Comptronix0.1CABLE TV INDUSTRIES0.1Storage Dimensions 0.1DH TECHNOLOGY0.1Integrated Sensor Solutions In0.1COMPUTER MEMORIES0.1Metricom0.1Benchmarq Microelectronics0.1SYSCON0.1Metrologic Instruments0.1SCAN-TRON CORP.0.1Odimo 0.1SPSS0.1Centigram Communications0.1Award Software International0.1Fieldworks 0.1APPLIED DATA0.1Ace\*Comm0.1Tessco Technologies0.1IA0.1SpectRx 0.1Lumisys0.1STERLING SOFTWARE0.1Celeritek0.1Cardiovascular Imaging Systems0.1TERAK CORP.0.1INTERAND CORPORATION0.1Go2pharmacy.com 0.1COMPUTONE SYSTEMS0.1GULL, INC.0.1Isco0.1TOPAZ0.1Internet Financial Services0.1BTG0.1Quality Semiconductor0.1LASER INDUSTRIES0.1World Heart0.1Satellite Technology0.1Gaiam 0.1SYSTEM INDUSTRIES0.1Digi International0.1ALTRON INC.0.1BEL FUSE0.1Advanced Promotion Tech0.1Securacom 0.1Emcore Corp0.1BARON DATA SYSTEMS0.1EPSILON DATA MGMT.0.1Applied Imaging0.1MySoftware0.1Orbit Semiconductor0.1Interlinq Software0.1EMULEX0.1Advanced Technology Materials0.1Project Software & Development0.1ParkerVision0.1Magal Security Systems0.1TALX0.1Equinox Systems0.1MicroTouch Systems0.1Qiao Xing Universal Telephone0.1OrthoLogic0.1SILVAR-LISCO0.1Claimsnet.com 0.1Andyne Computing Limited0.1Applix0.1Easel0.1SANDERS, RC TECH.0.1ESPRIT SYSTEMS0.1HumaScan0.1Summagraphics0.1INTELLIGENETICS0.1BPI SYSTEMS0.1Astropower 0.1Fusion Telecommunications0.1Phoenix International Ltd.0.1InVision Technologies0.1Critical Industries0.1Logal Educational Software0.1Medicus Systems0.1COOK DATA SERVICES0.1Luna Innovations 0.1Bio-Plexus0.1Plexus0.1Zytec Corp0.1CRIME CONTROL0.1CIBER0.1JPM0.1Keptel0.1BOOLE & BABBAGE0.1WebSecure0.1Intelligent Surgical Laser0.1Telesis Systems0.1Liberty Technologies0.1Equitrac0.1Euphonix0.1KVH Industries0.1COPYTELE, INC.0.1Intelli-Check 0.1Medialink Worldwide 0.1VALLEN0.1ARRAYS, INC.0.1Advanced Magnetics0.1OptiSystems Solutions Ltd0.1BIOSEARCH MEDICAL0.1Illinois Superconductor0.1Wavefront Technologies0.1Photran0.1CERMETEK MICROELEC.0.1Brooktrout Technology0.1Photonics Corp0.1Telos0.1COMPTEK RESEARCH0.1Integrated Circuit Systems0.1Symix Systems0.1Mizar0.1ISG International Software0.1Solectron0.1Electro-Optical Sciences 0.1Absolute Entertainment0.1HemoSense 0.1CONTINUOS CURVE LENS0.1GenesisIntermedia.com 0.1CyberShop International 0.1TESDATA SYSTEMS0.1Lambert Communications0.1ALLY & GARGANO0.1ICU Medical0.1FIBRONICS INT'L0.1eRoom System Technologies 0.1E-Cruiter.com 0.1Optibase Ltd0.1Mindscape0.1UOL Publishing0.1COMMUNICATIONS SYSTEMS0.1Advanced Communication Systems0.1Sierra On-Line0.1CORCOM0.1PERFECT DATA CORP.0.1Ventana Medical Systems0.1Delphi Information Systems0.1MindSpring Enterprises0.1COMPUTER ENTRY0.1Optika Imaging Systems0.1IQ Software0.1BusyBox.com 0.1American Technical Ceramics0.1CYBERTEK COMPUTER0.1CCX NETWORK0.1ELECTRO-BIOLOGY0.1INT'L ROBOMATION0.1SOFTECH0.1Interchange Corp0.1Lifequest Medical0.1Information America0.1Criticare Systems0.1RAMTEK0.1Registry Magic 0.1ForeFront Group0.1Lowrance Electronics0.1FSI International0.1Micro Therapeutics 0.1Performance Technologies0.1SCIENTIFIC TIME SHAR0.1Medi-Ject0.1Paradigm Geophysical Ltd0.1DATEQ Information Network0.1Rheometrics0.1LANE TELECOMM.0.1Take-Two Interactive Software0.1DICKEY-JOHN0.1Uniphase0.1Circadian0.1Multicom Publishing0.1Made2Manage Systems 0.1Unitech Industries0.1Photronic Laboratories0.1Wiztec Solutions0.1DUQUESNE SYSTEMS0.1SCS/Compute0.1Logic Devices0.1Brilliant Digital Ent0.1I D Systems 0.1OBJECT RECOGNITION0.1TIE / COMMUNICATIONS0.1POWERTEC, INC.0.1AC Teleconnect0.0Bioanalytical Systems0.0Bitstream0.0IDB Communications Group0.0RF Monolithics0.0Spatial Technology0.0Benchmark Electronics0.0Golden Systems0.0CDP Technologies0.0CEM0.0Across Data Systems0.0Plastic Surgery Co0.0Kinetiks.com0.0Aseco0.0Go2Net 0.0CrossZ Software Corp0.0Aladdin Knowledge Systems0.0CIPRICO INC.0.0SEEC 0.0WESPERCORP0.0NORTHERN DATA SYS0.0Target Technologies0.0Taunton Technologies0.0DIAGNON CORP0.0KYLE TECHNOLOGY0.0STARTEL CORPORATION0.0ScanVec Co(1990)0.0MEDAR, INC.0.0Merge Technologies 0.0Comet Software International0.0PRIMAGES, INC.0.0INTERMETRICS0.0ARTEL COMMUNICATIONS0.0COMPUTRAC INC.0.0Coin Bill Validator0.0EIL INSTRUMENTS0.0Jack Henry & Associates0.0INTERPHASE CORP.0.0Vertex Communications0.0Sunhawk.com Corp0.0Mass Microsystems0.0Data Translation0.0MER Telemanagement Solutions0.0Laser Power Corp0.0WILAND SERVICES INC.0.0HYTEK MICROSYSTEMS0.0SPECTRADYNE0.0COMPUTER INPUT0.0California Micro Devices0.0SBE INC.0.0Elcotel0.0International CompuTex 0.0Coherent Communications0.0TELENET0.0JetForm0.0InfoCure Corp0.0AML Communications0.0Loronix Information Systems0.0Effective Management Systems0.0REXON BUSINESS0.0TECHNOLOGY MARKETING0.0SSE Telecom0.0Quad Systems0.0American Xtal Technology0.0Electronic Fab Technology0.0Printware0.0Interactive Group0.0TLS CO.0.0Panda Project0.0Data Research Associates0.0Research Engineers0.0FREY ASSOCIATES0.0Electronic Information Systems0.0LANGER BIOMECHANICS0.0MEDSTAT SYSTEMS0.0Cavion Technologies 0.0Healthdesk(R)Corp0.0Natural Microsystems0.0e-NET 0.0ENCAD0.0Diversified Security Solutions0.0Bridgeline Software 0.0Citation Computer Systems0.0Iverson Technology0.0CliniCom0.0CLINICAL DATA0.0WINTERHALTER, INC.0.0CONMED0.0OXYGEN ENRICHMENT0.0ASTRO-MED, INC.0.0CONT'L HEALTHCARE0.0Advanced Photonix0.0UNIVERSAL MONEY0.0ECCS 0.0Vodavi Technology0.0Nuwave Technologies0.0TRIO-TECH INT'L0.0V BAND SYSTEMS, INC.0.0Percon Acquisition0.0CYCARE SYSTEMS0.0Image Business Systems0.0Electronic Tele-Communications0.0BKW, INC.0.0Perficient 0.0DIAGNOSTIC/RETRIEVAL0.0DISTRIBUTED LOGIC0.0SC & T International0.0Truetime 0.0TELERAM COMMUNICATIONS0.0Henley International0.0Optek Technology0.0Perceptron0.0Tylan General0.0INFO DESIGNS, INC.0.0New Image Industries0.0Augment Systems 0.0Casino Data Systems0.0Network-1 Security Solutions0.0ThrustMaster0.0Castelle0.0Jakks Pacific0.0INNOVATIVE SOFTWARE0.0BIOSTIM0.0ENVIRONMENTAL TESTING0.0Med-Design0.0Ibis Technology0.0Blyth Holdings0.0Medwave0.0BFI COMMUNICATIONS0.0CONSCO ENTERPRISES0.0BIOCHEM INTERNATIONAL0.0ANTENNAS FOR COMM.0.0Barrister Information Systems0.0P.C. TELEMART INC.0.0SCIENTIFIC COMMUN.0.0DATAKEY, INC.0.0RGB Computer & Video0.0Telesoft0.0Cognitive Systems0.0Objective Communication 0.0VANZETTI SYSTEMS0.0Microwave Labs0.0RENAL SYSTEMS0.0WORLCO DATA SYSTEMS0.0Technology Development0.0Innodata 0.0M-Wave0.0SysComm International Corp0.0Autoinfo0.0Samna0.0II-VI0.0Photon Technology Intl0.0Mustang Software0.0II MORROW INC.0.0TRIANGLE MICROWAVE0.0BIOMET INC0.0Robocom Systems 0.0CSP INC0.0STOCKHOLDER SYSTEMS0.0Intramed Laboratories0.0Elexis0.0Eltek Ltd0.0SAC Technologies 0.0Frisco Bay Industries Ltd0.0CompuRAD0.0KMW SYSTEMS CORP.0.0NITRON0.0COM SYSTEMS0.0PACE Health Management0.0Bell Technology Group0.0PHARMACONTROL0.0TELECI, INC.0.0MAGNETIC INFO. TECH.0.0United States Paging0.0RSI Systems0.0INTEGRATED CIRCUITS0.0Edison Control0.0PYRAMID MAGNETICS0.0BALLARD MEDICAL0.0EuroMed0.0TANO CORP0.0Jenkon International0.0Cellular0.0SigmaTron International0.0NOVAR ELECTRONICS0.0BEDFORD COMPUTER0.0Code-Alarm0.0Jinpan International Ltd0.0TOTAL ASSETS0.0Verticom0.0C2I Solutions 0.0IBS Interactive 0.0Xeta0.0Com/Tech Communication0.0Gurunet Corp0.0Telecalc0.0COMPUSAVE CORP.0.0Gateway Data Sciences0.0Comtrex Systems0.0ENDOTRONICS, INC.0.0DAY TELECOMMUNIC.0.0Ursus Telecom Corporation0.0Old Dominion Systems0.0Advanced Instl Mgmt Software0.0Innovative Tech Systems0.0RENAL DEVICES0.0Research Frontiers0.0Digital Optronics0.0Global Market Information0.0Sigma Designs0.0CMC INTERNATIONAL0.0Microfield Graphics0.0PATIENT TECH0.0Crystallume0.0SoloPoint0.0DIMIS0.0Smartserv Online0.0CERPROBE CORPORATION0.0MERRIMAC INDUSTRIES0.0Navarre0.0FANON/COURIER U.S.A.0.0ZONIC0.0HomeCom Communications 0.0DIDAX 0.0HEALTH INFORMATION0.0CONCORD COMPUTING0.0Unitronix0.0COMPONENT TECHNOLOGY0.0Integrated Surgical Systems0.0GV MEDICAL, INC.0.0Global Telecommunication0.0LASER PHOTONICS0.0Computer Petroleum0.0Shared Technologies Cellular0.0Altai0.0Software Professionals 0.0BOMED MEDICAL LTD.0.0Simulations Plus 0.0CARDIOSEARCH INC.0.0Semiconductor Laser Intl0.0GridComm0.0Micrion0.0PANCRETEC INC.0.0INTERACTIVE RADIATN.0.0Pacer0.0HEI0.0Manatron0.0Computer Outsourcing Services0.0Network Long Distance0.0DATAPOWER0.0Mediware Information Systems0.0Multimedia Concepts0.0Electropharmacology0.0Javelin Systems0.0Vikonics0.0Legacy Software0.0NetLive Communications0.0Borealis Technology0.0SPACE MICROWAVE0.0Defense Software & Systems0.0Image Guided Technologies0.0HARRIS & PAULSON0.0PERCEPTRONICS0.0Bureau of Electronic0.0CHAD THERAPEUTICS0.0ENSUN CORP.0.0Fine.com Corp0.0COMPUTRAC INSTRUM.0.0PHOENIX MEDICAL0.0Applied Intelligence Group0.0SelfCare0.0Styles on Video0.0QMAX TECHNOLOGY0.0ELECTRONIC FINANCIAL0.0CITISOURCE INC.0.0PERSONAL COMPUTER0.0Paravant Computer Systems0.0SILICON ELECTRO-PHYSIC0.0SAZTEC International0.0SPAN-AMERICAN MEDICAL0.0General Sciences0.0INVENTION, DESIGN0.0DeltaPoint0.0PSYCH SYSTEMS0.0Precis Smart Card Systems 0.0Compu-Dawn 0.0LifeRate Systems0.0TELEPHONE SUPPORT0.0Candela Laser0.0Dynatem0.0BIO-LOGIC SYSTEMS0.0Conceptronic0.0LaserSight, 0.0FINAL TEST, INC.0.0Rainbow Technologies0.0Computer Telephone0.0Diasys0.0World Group Companies0.03Net Systems0.0Nationwide Cellular Service0.0WRIGHT LABORATORIES0.0Image Management Systems0.0Hemodynamics0.0Digital Data Networks0.0Sigma Circuits0.0CAM Data Systems0.0BKC Semiconductors0.0Advanced Electronic Support0.0INT'L MEDICAL SYSTEMS0.0Hungarian Telephone & Cable0.0Circuit Systems0.0KEY IMAGE SYSTEMS0.0UStel0.0JMAR Industries0.0Rimage0.0SELECT INFORMATION0.0Xiox0.0Houston Biomedical0.0Mikron Instrument0.0KAPPA NETWORK0.0DATA MEASUREMENT [Fork](https://observablehq.com/@observablehq/plot-text-dodge "Open on Observable")

js

```
Plot.plot({
  insetRight: 10,
  height: 790,
  marks: [\
    Plot.text(\
      ipos,\
      Plot.dodgeY({\
        x: "date",\
        r: "rMVOP",\
        text: (d) => (d.rMVOP / 1e3).toFixed(1),\
        title: "NAME",\
        fontSize: (d) => Math.min(22, Math.cbrt(d.rMVOP / 1e3) * 6)\
      })\
    )\
  ]
})
```

The dodge transform places dots sequentially, each time finding the closest position to the baseline that avoids intersection with previously-placed dots. Because this is a [greedy algorithm](https://en.wikipedia.org/wiki/Greedy_algorithm), the resulting layout depends on the input order. When **r** is a channel, dots are sorted by descending radius by default such that the largest dots are placed closest to the baseline. Otherwise, dots are placed in input order by default.

To adjust the dodge layout, use the [sort transform](https://observablehq.com/plot/transforms/sort). For example, if the **sort** option uses the same column as **x**, the dots are arranged in piles leaning right.

2,0002,5003,0003,5004,0004,5005,000weight (lb) →Datsun 1200Toyota CoronaToyota StarletHonda Civic 1300Toyota Corolla 1200Honda Civic CVCCHonda CivicFord FiestaHonda Civic CVCCRenault 5 GtlVolkswagen RabbitVolkswagen Model 111Renault Lecar DeluxeVolkswagen 1131 Deluxe SedanToyota Corolla 1200Vokswagen RabbitHonda Civic 1500 GLFiat 128Plymouth ChampDodge Colt Hatchback CustomVolkswagen Rabbit CustomVolkswagen RabbitVolkswagen RabbitVolkswagen Rabbit CustomDatsun F-10 HatchbackDatsun B210Volkswagen Super BeetlePlymouth CricketVolkswagen DasherHonda Civic (Auto)Honda CivicToyota Corolla TercelMazda GLC CustomDatsun 210Maxda GLC DeluxeVolkswagen Super Beetle 117Volkswagen Rabbit LMazda GLC 4Mazda GLC DeluxeSubaru DLVolkswagen Rabbit Custom DieselDatsun B-210Volkswagen SciroccoDatsun 310 GXFiat X1.9Datsun 710Datsun 310Datsun 210Mazda GLC Custom LChevrolet ChevetteFord Escort 4WHonda Accord CVCCFord PintoToyota TercelChevrolet ChevetteFiat 124BSubaruDatsun B210 GXPeugeot 304Dodge Colt M/MVolkswagen Rabbit C (Diesel)Toyota Corolla 1600 (Wagon)Fiat 128Datsun 210Mazda GLCChevrolet ChevetteOpel 1900Maxda RX-3Dodge ColtMercury Lynx LPlymouth Horizon MiserDodge Colt HardtopDatsun PL510Datsun PL510Fiat Strada CustomVolkswagen PickupHonda Accord LXVolkswagen RabbitSubaru DLPlymouth Horizon TC3Buick Opel Isuzu DeluxeChevrolet ChevetteToyota CorollaOpel MantaNissan Stanza XEChevrolet WoodyDodge Colt (Wagon)Toyota CorollaAudi 4000Renault 12 (Wagon)Volkswagen DasherVolkswagen JettaPlymouth HorizonRenault 12TLHonda AccordHonda PreludePlymouth Horizon 4Audi FoxMercury Capri 2000Opel 1900Volkswagen DasherFord Pinto RunaboutToyota CoronaDodge OmniBMW 2002Toyota CorollaFiat 124 TCVolkswagen Type 3Dodge ColtChevrolet Vega 2300Fiat 124 Sport CoupeToyota Corolla LiftbackToyota CorollaToyota Corona HardtopToyota CarinaDatsun 510 (Wagon)Honda AccordDodge RampageDatsun 510Opel MantaPlymouth Arrow GSFord PintoRenault 18IMazda RX-2 CoupeVolkswagen Dasher (Diesel)Toyota CorollaDodge Charger 2.2Toyota Corona Mark IISaab 99EDatsun 610Ford Escort 2HPlymouth ReliantSubaruChevrolet Cavalier 2-DoorFord Pinto (Wagon)Chevrolet VegaDatsun 200SXChevrolet Vega (Wagon)Chevrolet VegaMazda RX-7 GsAudi 100 LSDatsun 510 HatchbackFord PintoFiat 131Mercury Capri V6Honda CivicPlymouth ReliantTriumph TR7 CoupeToyouta Corona Mark II (Wagon)Volkswagen 411 (Wagon)Toyota Celica GT LiftbackDodge Aries SEChevrolet VegaMazda 626Datsun 710Pontiac PhoenixToyota CoronaFord PintoFord Capri IIPontiac J2000 Se HatchbackAudi 100 LSChrysler Lebaron MedallionFord MaverickPontiac AstroChevrolet CitationBMW 320iChevrolet CavalierDatsun 200SXDodge Aries Wagon (Wagon)Ford RangerAMC GremlinBuick SkylarkMazda 626Ford PintoChevrolet Cavalier WagonAMC GremlinSaab 99LEToyota Celica GTAMC Spirit DLBuick Skylark LimitedSaab 99LEPeugeot 504Chevrolet CitationAudi 100 LSOldsmobile Omega BroughamToyota CoronaToyota Corona LiftbackChevy S-10Ford Fairmont (Man)Mazda RX-4Chevrolet CitationPontiac PhoenixPontiac Sunbird CoupePlymouth SapporoFord Mustang II 2+2AMC HornetAMC GremlinFord Mustang GLSaab 99GLEDodge ColtSaab 900SToyota Mark IIDatsun 810Audi 5000Plymouth DusterFord Granada LOldsmobile Starfire SXFord Fairmont FuturaVolvo 144EAFord FairmontFord MaverickFord Fairmont 4Toyota CressidaAMC HornetPlymouth DusterFord Mustang CobraDatsun 280ZXAMC GremlinDatsun 810 MaximaToyota Mark IIVolvo 145E (Wagon)AMC HornetBuick Century LimitedVolvo 244DLAudi 5000S (Diesel)Chevrolet CamaroPeugeot 504AMC Hornet Sportabout (Wagon)Ford Fairmont (Auto)Peugeot 504 (Wagon)Ford PintoMercury Zephyr 6AMC ConcordFord MaverickOldsmobile Cutlass Ciera (Diesel)Ford MaverickAMC Concord DLBuick SkyhawkFord Granada GLMercury ZephyrAMC HornetBuick Estate Wagon (Wagon)Citroen DS-21 PallasPlymouth DusterPlymouth ValiantFord MustangVolvo 264GLVolvo 245Chevrolet MalibuFord MaverickVolvo DieselFord Mustang IIPeugeot 504AMC Pacer D/LFord FuturaAMC ConcordAMC PacerChevrolet Monza 2+2Peugeot 505S Turbo DieselPlymouth ValiantPontiac Lemans V6Mercedes-Benz 240DPlymouth Valiant CustomAMC Concord DL 6Peugeot 504Chevrolet Nova CustomPontiac FirebirdAMC MatadorFord Torino 500Chevrolet Chevelle MalibuChevrolet NovaChevrolet NovaFord Mustang Boss 302Dodge Aspen 6Oldsmobile Cutlass Salon BroughamBuick Century SpecialDodge AspenDodge Dart CustomAMC Concord DLPeugeot 604SLBuick CenturyOldsmobile Cutlass Salon BroughamBuick SkylarkChevrolet Monte Carlo LandauPlymouth VolareMercury MonarchAMC Rebel SSTPlymouth SatellitePlymouth Satellite CustomBuick Regal Sport Coupe (Turbo)Ford TorinoChevrolet NovaChrysler Lebaron SalonChevrolet Chevelle MalibuChevrolet ConcoursFord GranadaMercedes-Benz 300DPontiac Phoenix LJDodge Challenger SEMercury Monarch GhiaFord Granada GhiaChevrolet Malibu Classic (Wagon)Plymouth Barracuda 340Plymouth Satellite SebringDodge AspenPlymouth Volare CustomAMC MatadorPontiac Ventura SjDodge Aspen SEOldsmobile OmegaAMC Ambassador SSTAMC MatadorBuick Skylark 320Ford LTD LandauOldsmobile Cutlass LSAMC MatadorDodge DiplomatDodge D100Chevrolet Monte CarloDodge Coronet CustomChevrolet Chevelle Malibu ClassicPlymouth FuryMercedes-Benz 280SAMC Ambassador BroughamDodge St. RegisChevrolet Caprice ClassicAMC Ambassador DPLAMC Rebel SST (Wagon)Ford F108Chevrolet Caprice ClassicAMC Matador (Wagon)Chevroelt Chevelle MalibuCadillac EldoradoBuick CenturyChrysler Lebaron Town & Country (Wagon)Plymouth Volare Premier V8Mercury Grand MarquisAMC MatadorChevrolet MalibuFord Torino (Wagon)Ford Gran TorinoFord Country Squire (Wagon)Chevy C10Oldsmobile Cutlass SupremePlymouth Satellite Custom (Wagon)Dodge Magnum XEChevrolet Monte Carlo SPlymouth Fury IIIChevrolet Chevelle Concours (Wagon)Buick Century 350Ford Galaxie 500Plymouth Fury IIIDodge Monaco BroughamFord Gran TorinoChevrolet Chevelle Concours (Wagon)Ford Galaxie 500Chevrolet Monte Carlo LandauPlymouth Satellite (Wagon)Dodge Coronet BroughamChevrolet ImpalaChevrolet Chevelle Malibu ClassicFord Gran TorinoPontiac Grand Prix LjPlymouth Fury Gran SedanAMC Matador (Wagon)Chevrolet ImpalaPontiac Grand PrixFord Gran Torino (Wagon)Mercury Cougar BroughamPlymouth Fury IIIChrysler CordobaFord ThunderbirdFord Galaxie 500Chevrolet ImpalaBuick Estate Wagon (Wagon)Ford LTDChevy C20Cadillac SevilleDodge D200Pontiac CatalinaChrysler Newport RoyalPontiac CatalinaChevrolet Bel AirOldsmobile Delta 88 RoyaleDodge Coronet Custom (Wagon)Chevrolet Caprice ClassicPontiac Catalina BroughamPlymouth Grand FuryOldsmobile Vista CruiserBuick Lesabre CustomFord F250Mercury MarquisFord Gran Torino (Wagon)Plymouth Custom SuburbFord LTDPontiac CatalinaBuick Century Luxus (Wagon)Hi 1200DChrysler New Yorker BroughamFord Country Squire (Wagon)Ford CountryBuick Electra 225 CustomMercury Marquis BroughamDodge Monaco (Wagon)Chevrolet ImpalaPontiac Safari (Wagon) [Fork](https://observablehq.com/@observablehq/plot-dodge-sort "Open on Observable")

js

```
Plot.plot({
  height: 180,
  marks: [\
    Plot.dotX(cars, Plot.dodgeY({x: "weight (lb)", title: "name", fill: "currentColor", sort: "weight (lb)"}))\
  ]
})
```

Reversing the sort order produces piles leaning left.

2,0002,5003,0003,5004,0004,5005,000weight (lb) →Pontiac Safari (Wagon)Chevrolet ImpalaDodge Monaco (Wagon)Mercury Marquis BroughamBuick Electra 225 CustomFord CountryFord Country Squire (Wagon)Chrysler New Yorker BroughamHi 1200DBuick Century Luxus (Wagon)Pontiac CatalinaFord LTDPlymouth Custom SuburbFord Gran Torino (Wagon)Mercury MarquisFord F250Buick Lesabre CustomOldsmobile Vista CruiserPlymouth Grand FuryPontiac Catalina BroughamChevrolet Caprice ClassicDodge Coronet Custom (Wagon)Oldsmobile Delta 88 RoyaleChevrolet Bel AirPontiac CatalinaChrysler Newport RoyalPontiac CatalinaDodge D200Cadillac SevilleChevy C20Ford LTDBuick Estate Wagon (Wagon)Chevrolet ImpalaFord Galaxie 500Ford ThunderbirdChrysler CordobaPlymouth Fury IIIMercury Cougar BroughamFord Gran Torino (Wagon)Pontiac Grand PrixChevrolet ImpalaAMC Matador (Wagon)Plymouth Fury Gran SedanPontiac Grand Prix LjFord Gran TorinoChevrolet Chevelle Malibu ClassicChevrolet ImpalaDodge Coronet BroughamPlymouth Satellite (Wagon)Chevrolet Monte Carlo LandauFord Galaxie 500Chevrolet Chevelle Concours (Wagon)Ford Gran TorinoDodge Monaco BroughamPlymouth Fury IIIFord Galaxie 500Buick Century 350Chevrolet Chevelle Concours (Wagon)Plymouth Fury IIIChevrolet Monte Carlo SDodge Magnum XEPlymouth Satellite Custom (Wagon)Oldsmobile Cutlass SupremeChevy C10Ford Country Squire (Wagon)Ford Gran TorinoFord Torino (Wagon)Chevrolet MalibuAMC MatadorMercury Grand MarquisPlymouth Volare Premier V8Chrysler Lebaron Town & Country (Wagon)Buick CenturyCadillac EldoradoChevroelt Chevelle MalibuAMC Matador (Wagon)Chevrolet Caprice ClassicFord F108AMC Rebel SST (Wagon)AMC Ambassador DPLChevrolet Caprice ClassicDodge St. RegisAMC Ambassador BroughamMercedes-Benz 280SPlymouth FuryChevrolet Chevelle Malibu ClassicDodge Coronet CustomChevrolet Monte CarloDodge D100Dodge DiplomatAMC MatadorOldsmobile Cutlass LSFord LTD LandauBuick Skylark 320AMC MatadorAMC Ambassador SSTOldsmobile OmegaDodge Aspen SEPontiac Ventura SjAMC MatadorPlymouth Volare CustomDodge AspenPlymouth Satellite SebringPlymouth Barracuda 340Chevrolet Malibu Classic (Wagon)Ford Granada GhiaMercury Monarch GhiaDodge Challenger SEPontiac Phoenix LJMercedes-Benz 300DFord GranadaChevrolet ConcoursChevrolet Chevelle MalibuChrysler Lebaron SalonChevrolet NovaFord TorinoBuick Regal Sport Coupe (Turbo)Plymouth Satellite CustomPlymouth SatelliteAMC Rebel SSTMercury MonarchPlymouth VolareChevrolet Monte Carlo LandauBuick SkylarkOldsmobile Cutlass Salon BroughamBuick CenturyPeugeot 604SLAMC Concord DLDodge Dart CustomDodge AspenBuick Century SpecialOldsmobile Cutlass Salon BroughamDodge Aspen 6Ford Mustang Boss 302Chevrolet NovaChevrolet NovaChevrolet Chevelle MalibuFord Torino 500AMC MatadorPontiac FirebirdChevrolet Nova CustomPeugeot 504AMC Concord DL 6Plymouth Valiant CustomMercedes-Benz 240DPontiac Lemans V6Plymouth ValiantPeugeot 505S Turbo DieselChevrolet Monza 2+2AMC PacerAMC ConcordFord FuturaAMC Pacer D/LPeugeot 504Ford Mustang IIVolvo DieselFord MaverickChevrolet MalibuVolvo 245Volvo 264GLFord MustangPlymouth ValiantPlymouth DusterCitroen DS-21 PallasBuick Estate Wagon (Wagon)AMC HornetMercury ZephyrFord Granada GLBuick SkyhawkAMC Concord DLFord MaverickOldsmobile Cutlass Ciera (Diesel)Ford MaverickAMC ConcordMercury Zephyr 6Ford PintoPeugeot 504 (Wagon)Ford Fairmont (Auto)AMC Hornet Sportabout (Wagon)Peugeot 504Chevrolet CamaroAudi 5000S (Diesel)Volvo 244DLBuick Century LimitedAMC HornetVolvo 145E (Wagon)Toyota Mark IIDatsun 810 MaximaAMC GremlinDatsun 280ZXFord Mustang CobraPlymouth DusterAMC HornetToyota CressidaFord Fairmont 4Ford MaverickFord FairmontVolvo 144EAFord Fairmont FuturaOldsmobile Starfire SXFord Granada LPlymouth DusterAudi 5000Datsun 810Toyota Mark IISaab 900SDodge ColtSaab 99GLEFord Mustang GLAMC GremlinAMC HornetFord Mustang II 2+2Plymouth SapporoPontiac Sunbird CoupePontiac PhoenixChevrolet CitationMazda RX-4Ford Fairmont (Man)Chevy S-10Toyota Corona LiftbackToyota CoronaOldsmobile Omega BroughamAudi 100 LSChevrolet CitationPeugeot 504Saab 99LEBuick Skylark LimitedAMC Spirit DLToyota Celica GTSaab 99LEAMC GremlinChevrolet Cavalier WagonFord PintoMazda 626Buick SkylarkAMC GremlinFord RangerDodge Aries Wagon (Wagon)Datsun 200SXChevrolet CavalierBMW 320iChevrolet CitationPontiac AstroFord MaverickChrysler Lebaron MedallionAudi 100 LSPontiac J2000 Se HatchbackFord Capri IIFord PintoToyota CoronaPontiac PhoenixDatsun 710Mazda 626Chevrolet VegaDodge Aries SEToyota Celica GT LiftbackVolkswagen 411 (Wagon)Toyouta Corona Mark II (Wagon)Triumph TR7 CoupePlymouth ReliantHonda CivicMercury Capri V6Fiat 131Ford PintoDatsun 510 HatchbackAudi 100 LSMazda RX-7 GsChevrolet VegaChevrolet Vega (Wagon)Datsun 200SXChevrolet VegaFord Pinto (Wagon)Chevrolet Cavalier 2-DoorSubaruPlymouth ReliantFord Escort 2HDatsun 610Saab 99EToyota Corona Mark IIDodge Charger 2.2Toyota CorollaVolkswagen Dasher (Diesel)Mazda RX-2 CoupeRenault 18IFord PintoPlymouth Arrow GSOpel MantaDatsun 510Dodge RampageHonda AccordDatsun 510 (Wagon)Toyota CarinaToyota Corona HardtopToyota CorollaToyota Corolla LiftbackFiat 124 Sport CoupeChevrolet Vega 2300Dodge ColtVolkswagen Type 3Fiat 124 TCToyota CorollaBMW 2002Dodge OmniToyota CoronaFord Pinto RunaboutVolkswagen DasherOpel 1900Mercury Capri 2000Audi FoxPlymouth Horizon 4Honda PreludeHonda AccordRenault 12TLPlymouth HorizonVolkswagen JettaVolkswagen DasherRenault 12 (Wagon)Audi 4000Toyota CorollaDodge Colt (Wagon)Chevrolet WoodyNissan Stanza XEOpel MantaToyota CorollaChevrolet ChevetteBuick Opel Isuzu DeluxePlymouth Horizon TC3Subaru DLVolkswagen RabbitHonda Accord LXVolkswagen PickupFiat Strada CustomDatsun PL510Datsun PL510Dodge Colt HardtopPlymouth Horizon MiserMercury Lynx LDodge ColtMaxda RX-3Opel 1900Chevrolet ChevetteMazda GLCDatsun 210Fiat 128Toyota Corolla 1600 (Wagon)Volkswagen Rabbit C (Diesel)Dodge Colt M/MPeugeot 304Datsun B210 GXSubaruFiat 124BChevrolet ChevetteToyota TercelFord PintoHonda Accord CVCCFord Escort 4WChevrolet ChevetteMazda GLC Custom LDatsun 210Datsun 310Datsun 710Fiat X1.9Datsun 310 GXVolkswagen SciroccoDatsun B-210Volkswagen Rabbit Custom DieselSubaru DLMazda GLC DeluxeMazda GLC 4Volkswagen Rabbit LVolkswagen Super Beetle 117Maxda GLC DeluxeDatsun 210Mazda GLC CustomToyota Corolla TercelHonda CivicHonda Civic (Auto)Volkswagen DasherPlymouth CricketVolkswagen Super BeetleDatsun B210Datsun F-10 HatchbackVolkswagen Rabbit CustomVolkswagen RabbitVolkswagen RabbitVolkswagen Rabbit CustomDodge Colt Hatchback CustomPlymouth ChampFiat 128Honda Civic 1500 GLVokswagen RabbitToyota Corolla 1200Volkswagen 1131 Deluxe SedanRenault Lecar DeluxeVolkswagen Model 111Volkswagen RabbitRenault 5 GtlHonda Civic CVCCFord FiestaHonda CivicHonda Civic CVCCToyota Corolla 1200Honda Civic 1300Toyota StarletToyota CoronaDatsun 1200 [Fork](https://observablehq.com/@observablehq/plot-dodge-sort "Open on Observable")

js

```
Plot.plot({
  height: 180,
  marks: [\
    Plot.dotX(cars, Plot.dodgeY({x: "weight (lb)", title: "name", fill: "currentColor", sort: "weight (lb)", reverse: true}))\
  ]
})
```

TIP

To avoid repeating a channel definition, you can also specify the **sort** option as `{channel: "x"}`.

INFO

Unlike a [force-directed beeswarm](https://observablehq.com/@harrystevens/force-directed-beeswarm), the dodge transform exactly preserves the input position dimension, resulting in a more accurate visualization. Also, the dodge transform tends to be faster than the iterative constraint relaxation used in the force-directed approach. We use Mikola Lysenko’s [interval-tree-1d library](https://github.com/mikolalysenko/interval-tree-1d) for fast intersection testing.

## Dodge options [​](https://observablehq.com/plot/transforms/dodge\#dodge-options)

The dodge transforms accept the following options:

- **padding** — a number of pixels added to the radius of the mark to estimate its size
- **anchor** \- the dodge anchor; defaults to _left_ for dodgeX, or _bottom_ for dodgeY

The **anchor** option may one of _middle_, _right_, and _left_ for dodgeX, and one of _middle_, _top_, and _bottom_ for dodgeY. With the _middle_ anchor the piles will grow from the center in both directions; with the other anchors, the piles will grow from the specified anchor towards the opposite direction.

## dodgeY( _dodgeOptions_, _options_) [​](https://observablehq.com/plot/transforms/dodge\#dodgeY)

js

```
Plot.dodgeY({x: "date"})
```

Given marks arranged along the _x_ axis, the dodgeY transform piles them vertically by defining a _y_ position channel that avoids overlapping. The _x_ position channel is unchanged.

## dodgeX( _dodgeOptions_, _options_) [​](https://observablehq.com/plot/transforms/dodge\#dodgeX)

js

```
Plot.dodgeX({y: "value"})
```

Equivalent to Plot.dodgeY, but piling horizontally, creating a new _x_ position channel that avoids overlapping. The _y_ position channel is unchanged.

Pager

[Previous pageCentroid](https://observablehq.com/plot/transforms/centroid)

[Next pageFilter](https://observablehq.com/plot/transforms/filter)

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

---
url: "https://observablehq.com/plot/marks/dot"
title: "Dot mark | Plot"
---

# Dot mark [​](https://observablehq.com/plot/marks/dot\#dot-mark)

The **dot mark** draws circles or other symbols positioned in **x** and **y** as in a scatterplot. For example, the chart below shows the roughly-inverse relationship between car horsepower in _y_ ↑ and fuel efficiency in miles per gallon in _x_ →.

6080100120140160180200220↑ power (hp)1015202530354045economy (mpg) → [Fork](https://observablehq.com/@observablehq/plot-basic-scatterplot "Open on Observable")

js

```
Plot.dot(cars, {x: "economy (mpg)", y: "power (hp)"}).plot({grid: true})
```

Using a function for **x**, we can instead plot the roughly-linear relationship when fuel efficiency is represented as gallons per 100 miles. (For fans of the metric system, 1 gallon per 100 miles is roughly 2.4 liters per 100 km.)

6080100120140160180200220↑ Horsepower34567891011Fuel consumption (gallons per 100 miles) → [Fork](https://observablehq.com/@observablehq/plot-derived-value-scatterplot "Open on Observable")

js

```
Plot.plot({
  grid: true,
  inset: 10,
  x: {label: "Fuel consumption (gallons per 100 miles)"},
  y: {label: "Horsepower"},
  marks: [\
    Plot.dot(cars, {x: (d) => 100 / d["economy (mpg)"], y: "power (hp)"})\
  ]
})
```

Dots support **stroke** and **fill** channels in addition to position along **x** and **y**. Below, color is used as a redundant encoding to emphasize the rising trend in average global surface temperatures. A _diverging_ color scale encodes values below zero blue and above zero red.

−0.6−0.4−0.2+0.0+0.2+0.4+0.6+0.8+1.0+1.2↑ Surface temperature anomaly (°F)1880190019201940196019802000 [Fork](https://observablehq.com/@observablehq/plot-diverging-color-scatterplot "Open on Observable")

js

```
Plot.plot({
  y: {
    grid: true,
    tickFormat: "+f",
    label: "Surface temperature anomaly (°F)"
  },
  color: {
    scheme: "BuRd"
  },
  marks: [\
    Plot.ruleY([0]),\
    Plot.dot(gistemp, {x: "Date", y: "Anomaly", stroke: "Anomaly"})\
  ]
})
```

Dots also support an **r** channel allowing dot size to represent quantitative value. Below, each dot represents a day of trading; the _x_-position represents the day’s change, while the _y_-position and area ( **r**) represent the day’s trading volume. As you might expect, days with higher volatility have higher trading volume.

20M30M40M50M60M70M80M90M100M200M↑ Daily trading volume−6−4−2+0+2+4+6+8Daily change (%) → [Fork](https://observablehq.com/@observablehq/plot-proportional-symbol-scatterplot "Open on Observable")

js

```
Plot.plot({
  grid: true,
  x: {
    label: "Daily change (%)",
    tickFormat: "+f",
    percent: true
  },
  y: {
    type: "log",
    label: "Daily trading volume"
  },
  marks: [\
    Plot.ruleX([0]),\
    Plot.dot(aapl, {x: (d) => (d.Close - d.Open) / d.Open, y: "Volume", r: "Volume"})\
  ]
})
```

With the [bin transform](https://observablehq.com/plot/transforms/bin), sized dots can also be used as an alternative to a [rect-based](https://observablehq.com/plot/marks/rect) heatmap to show a two-dimensional distribution.

1,0002,0003,0004,0005,0006,0007,0008,0009,00010,00011,00012,00013,00014,00015,00016,00017,00018,000↑ Price ($)0.51.01.52.02.53.03.54.04.55.0Carats → [Fork](https://observablehq.com/@observablehq/plot-proportional-dot-heatmap "Open on Observable")

js

```
Plot.plot({
  height: 640,
  marginLeft: 60,
  grid: true,
  x: {label: "Carats"},
  y: {label: "Price ($)"},
  r: {range: [0, 20]},
  marks: [\
    Plot.dot(diamonds, Plot.bin({r: "count"}, {x: "carat", y: "price", thresholds: 100}))\
  ]
})
```

TIP

For hexagonal binning, use the [hexbin transform](https://observablehq.com/plot/transforms/hexbin) instead of the bin transform.

While dots are typically positioned in two dimensions ( **x** and **y**), one-dimensional dots (only **x** or only **y**) are also supported. Below, dot area is used to represent the frequency of letters in the English language as a compact alternative to a bar chart.

ABCDEFGHIJKLMNOPQRSTUVWXYZletter [Fork](https://observablehq.com/@observablehq/plot-dot-area-chart "Open on Observable")

js

```
Plot.dot(alphabet, {x: "letter", r: "frequency"}).plot()
```

Dots, together with [rules](https://observablehq.com/plot/marks/rule), can be used as a stylistic alternative to [bars](https://observablehq.com/plot/marks/bar) to produce a lollipop 🍭 chart. (Sadly these lollipops cannot be eaten.)

0123456789101112↑ frequency (%)ABCDEFGHIJKLMNOPQRSTUVWXYZ [Fork](https://observablehq.com/@observablehq/plot-lollipop "Open on Observable")

js

```
Plot.plot({
  x: {label: null, tickPadding: 6, tickSize: 0},
  y: {percent: true},
  marks: [\
    Plot.ruleX(alphabet, {x: "letter", y: "frequency", strokeWidth: 2}),\
    Plot.dot(alphabet, {x: "letter", y: "frequency", fill: "currentColor", r: 4})\
  ]
})
```

A dot may have an ordinal dimension on either **x** and **y**, as in the plot below comparing the demographics of states: color represents age group, **y** represents the state, and **x** represents the proportion of the state’s population in that age group. The [normalize transform](https://observablehq.com/plot/transforms/normalize) is used to compute the relative proportion of each age group within each state, while the [group transform](https://observablehq.com/plot/transforms/group) is used to pull out the _min_ and _max_ values for each state for a horizontal [rule](https://observablehq.com/plot/marks/rule).

<1010-1920-2930-3940-4950-5960-6970-79≥80

02468101214161820Population (%) →<10<10<10<10<10<10<10<10<10<10<10<10<10<10<10<10<10<10<10<10<10<10<10<10<10<10<10<10<10<10<10<10<10<10<10<10<10<10<10<10<10<10<10<10<10<10<10<10<10<10<10<1010-1910-1910-1910-1910-1910-1910-1910-1910-1910-1910-1910-1910-1910-1910-1910-1910-1910-1910-1910-1910-1910-1910-1910-1910-1910-1910-1910-1910-1910-1910-1910-1910-1910-1910-1910-1910-1910-1910-1910-1910-1910-1910-1910-1910-1910-1910-1910-1910-1910-1910-1910-1920-2920-2920-2920-2920-2920-2920-2920-2920-2920-2920-2920-2920-2920-2920-2920-2920-2920-2920-2920-2920-2920-2920-2920-2920-2920-2920-2920-2920-2920-2920-2920-2920-2920-2920-2920-2920-2920-2920-2920-2920-2920-2920-2920-2920-2920-2920-2920-2920-2920-2920-2920-2930-3930-3930-3930-3930-3930-3930-3930-3930-3930-3930-3930-3930-3930-3930-3930-3930-3930-3930-3930-3930-3930-3930-3930-3930-3930-3930-3930-3930-3930-3930-3930-3930-3930-3930-3930-3930-3930-3930-3930-3930-3930-3930-3930-3930-3930-3930-3930-3930-3930-3930-3930-3940-4940-4940-4940-4940-4940-4940-4940-4940-4940-4940-4940-4940-4940-4940-4940-4940-4940-4940-4940-4940-4940-4940-4940-4940-4940-4940-4940-4940-4940-4940-4940-4940-4940-4940-4940-4940-4940-4940-4940-4940-4940-4940-4940-4940-4940-4940-4940-4940-4940-4940-4940-4950-5950-5950-5950-5950-5950-5950-5950-5950-5950-5950-5950-5950-5950-5950-5950-5950-5950-5950-5950-5950-5950-5950-5950-5950-5950-5950-5950-5950-5950-5950-5950-5950-5950-5950-5950-5950-5950-5950-5950-5950-5950-5950-5950-5950-5950-5950-5950-5950-5950-5950-5950-5960-6960-6960-6960-6960-6960-6960-6960-6960-6960-6960-6960-6960-6960-6960-6960-6960-6960-6960-6960-6960-6960-6960-6960-6960-6960-6960-6960-6960-6960-6960-6960-6960-6960-6960-6960-6960-6960-6960-6960-6960-6960-6960-6960-6960-6960-6960-6960-6960-6960-6960-6960-6970-7970-7970-7970-7970-7970-7970-7970-7970-7970-7970-7970-7970-7970-7970-7970-7970-7970-7970-7970-7970-7970-7970-7970-7970-7970-7970-7970-7970-7970-7970-7970-7970-7970-7970-7970-7970-7970-7970-7970-7970-7970-7970-7970-7970-7970-7970-7970-7970-7970-7970-7970-79≥80≥80≥80≥80≥80≥80≥80≥80≥80≥80≥80≥80≥80≥80≥80≥80≥80≥80≥80≥80≥80≥80≥80≥80≥80≥80≥80≥80≥80≥80≥80≥80≥80≥80≥80≥80≥80≥80≥80≥80≥80≥80≥80≥80≥80≥80≥80≥80≥80≥80≥80≥80ALAKAZARCACOCTDEDCFLGAHIIDILINIAKSKYLAMEMDMAMIMNMSMOMTNENVNHNJNMNYNCNDOHOKORPARISCSDTNTXUTVTVAWAWVWIWYPR [Fork](https://observablehq.com/@observablehq/plot-dot-plot "Open on Observable")

js

```
Plot.plot({
  height: 660,
  axis: null,
  grid: true,
  x: {
    axis: "top",
    label: "Population (%)",
    percent: true
  },
  color: {
    scheme: "spectral",
    domain: stateage.ages, // in age order
    legend: true
  },
  marks: [\
    Plot.ruleX([0]),\
    Plot.ruleY(stateage, Plot.groupY({x1: "min", x2: "max"}, {...xy, sort: {y: "x1"}})),\
    Plot.dot(stateage, {...xy, fill: "age", title: "age"}),\
    Plot.text(stateage, Plot.selectMinX({...xy, textAnchor: "end", dx: -6, text: "state"}))\
  ]
})
```

js

```
xy = Plot.normalizeX("sum", {x: "population", y: "state", z: "state"})
```

TIP

To reduce code duplication, pull shared options out into an object (here `xy`) and then merge them into each mark’s options using the spread operator (`...`).

To improve accessibility, particularly for readers with color vision deficiency, the **symbol** channel can be used in addition to color (or instead of it) to represent ordinal data.

AdelieChinstrapGentoo

175180185190195200205210215220225230↑ Flipper length (mm)3,0003,5004,0004,5005,0005,5006,000Body mass (g) → [Fork](https://observablehq.com/@observablehq/plot-symbol-channel "Open on Observable")

js

```
Plot.plot({
  grid: true,
  x: {label: "Body mass (g)"},
  y: {label: "Flipper length (mm)"},
  symbol: {legend: true},
  marks: [\
    Plot.dot(penguins, {x: "body_mass_g", y: "flipper_length_mm", stroke: "species", symbol: "species"})\
  ]
})
```

Plot uses the following default symbols for filled dots:

circlecrossdiamondsquarestartrianglewye

js

```
Plot.dotX([\
  "circle",\
  "cross",\
  "diamond",\
  "square",\
  "star",\
  "triangle",\
  "wye"\
], {fill: "currentColor", symbol: Plot.identity}).plot()
```

There is a separate set of default symbols for stroked dots:

asteriskcirclediamond2plussquare2timestriangle2

js

```
Plot.dotX([\
  "circle",\
  "plus",\
  "times",\
  "triangle2",\
  "asterisk",\
  "square2",\
  "diamond2",\
], {stroke: "currentColor", symbol: Plot.identity}).plot()
```

INFO

The stroked symbols are based on [Heman Robinson’s research](https://www.tandfonline.com/doi/abs/10.1080/10618600.2019.1637746). There is also a _hexagon_ symbol; it is primarily intended for the [hexbin transform](https://observablehq.com/plot/transforms/hexbin). You can even specify a D3 or custom symbol type as an object that implements the [_symbol_.draw( _context_, _size_)](https://d3js.org/d3-shape/symbol#symbolType_draw) method.

The dot mark can be combined with the [stack transform](https://observablehq.com/plot/transforms/stack). The diverging stacked dot plot below shows the age and gender distribution of the U.S. Congress in 2023.

5051015← Women · Men →30405060708090Age (years) →Sherrod BrownMaria CantwellBenjamin L. CardinThomas R. CarperRobert P. Casey, Jr.Dianne FeinsteinAmy KlobucharRobert MenendezBernard SandersDebbie StabenowJon TesterSheldon WhitehouseJohn BarrassoRoger F. WickerSusan M. CollinsJohn CornynRichard J. DurbinLindsey GrahamMitch McConnellJeff MerkleyJack ReedJames E. RischJeanne ShaheenMark R. WarnerKirsten E. GillibrandChristopher A. CoonsJoe Manchin, IIIRobert B. AderholtTammy BaldwinMichael F. BennetGus M. BilirakisSanford D. Bishop, Jr.Marsha BlackburnEarl BlumenauerRichard BlumenthalJohn BoozmanVern BuchananLarry BucshonMichael C. BurgessKen CalvertShelley Moore CapitoAndré CarsonJohn R. CarterBill CassidyKathy CastorJudy ChuDavid N. CicillineYvette D. ClarkeEmanuel CleaverJames E. ClyburnSteve CohenTom ColeGerald E. ConnollyJim CostaJoe CourtneyMike CrapoEric A. "Rick" CrawfordHenry CuellarDanny K. DavisDiana DeGetteRosa L. DeLauroScott DesJarlaisMario Diaz-BalartLloyd DoggettJeff DuncanAnna G. EshooCharles J. "Chuck" FleischmannVirginia FoxxJohn GaramendiPaul A. GosarKay GrangerChuck GrassleySam GravesAl GreenH. Morgan GriffithRaúl M. GrijalvaBrett GuthrieAndy HarrisMartin HeinrichBrian HigginsJames A. HimesMazie K. HironoJohn HoevenSteny H. HoyerBill HuizengaSheila Jackson LeeBill JohnsonHenry C. "Hank" Johnson, Jr.Ron JohnsonJim JordanMarcy KapturWilliam R. KeatingMike KellyDoug LambornJames LankfordRick LarsenJohn B. LarsonRobert E. LattaBarbara LeeMike LeeZoe LofgrenFrank D. LucasBlaine LuetkemeyerBen Ray LujánStephen F. LynchEdward J. MarkeyDoris O. MatsuiKevin McCarthyMichael T. McCaulTom McClintockBetty McCollumJames P. McGovernPatrick T. McHenryCathy McMorris RodgersGregory W. MeeksGwen MooreJerry MoranLisa MurkowskiChristopher MurphyPatty MurrayJerrold NadlerGrace F. NapolitanoRichard E. NealEleanor Holmes NortonFrank Pallone, Jr.Bill Pascrell, Jr.Rand PaulNancy PelosiGary C. PetersChellie PingreeBill PoseyMike QuigleyHarold RogersMike RogersMarco RubioC. A. Dutch RuppersbergerGregorio Kilili Camacho SablanJohn P. SarbanesSteve ScaliseJanice D. SchakowskyAdam B. SchiffCharles E. SchumerDavid SchweikertAustin ScottDavid ScottRobert C. "Bobby" ScottTim ScottTerri A. SewellBrad ShermanMichael K. SimpsonAdam SmithAdrian SmithChristopher H. SmithLinda T. SánchezBennie G. ThompsonMike ThompsonGlenn ThompsonJohn ThunePaul TonkoMichael R. TurnerChris Van HollenNydia M. VelázquezTim WalbergDebbie Wasserman SchultzMaxine WatersDaniel WebsterPeter WelchJoe WilsonFrederica S. WilsonRobert J. WittmanSteve WomackRon WydenTodd YoungMark E. AmodeiSuzanne BonamiciSuzan K. DelBeneThomas MassieDonald M. Payne, Jr.Brian SchatzBill FosterDina TitusTom CottonKyrsten SinemaDoug LaMalfaJared HuffmanAmi BeraEric SwalwellJulia BrownleyTony CárdenasRaul RuizMark TakanoJuan VargasScott H. PetersLois FrankelTammy DuckworthAndy BarrElizabeth WarrenAngus S. King, Jr.Daniel T. KildeeAnn WagnerSteve DainesRichard HudsonKevin CramerDeb FischerAnn M. KusterGrace MengHakeem S. JeffriesBrad R. WenstrupJoyce BeattyDavid P. JoyceMarkwayne MullinScott PerryMatt CartwrightTed CruzRandy K. Weber, Sr.Joaquin CastroRoger WilliamsMarc A. VeaseyChris StewartTim KaineDerek KilmerMark PocanRobin L. KellyJason SmithCory A. BookerKatherine M. ClarkDonald NorcrossAlma S. AdamsGary J. PalmerJ. French HillBruce WestermanRuben GallegoMark DeSaulnierPete AguilarTed LieuNorma J. TorresKen BuckEarl L. "Buddy" CarterBarry LoudermilkRick W. AllenMike BostGarret GravesSeth MoultonJohn R. MoolenaarDebbie DingellTom EmmerDavid RouzerBonnie Watson ColemanElise M. StefanikBrendan F. BoyleBrian BabinDonald S. Beyer, Jr.Stacey E. PlaskettDan NewhouseGlenn GrothmanAlexander X. MooneyAumua Amata Coleman RadewagenDan SullivanJoni ErnstThom TillisMike RoundsTrent KellyDarin LaHoodWarren DavidsonJames ComerDwight EvansJohn KennedyMargaret Wood HassanCatherine Cortez MastoBradley Scott SchneiderAndy BiggsRo KhannaJimmy PanettaSalud O. CarbajalNanette Diaz BarragánJ. Luis CorreaLisa Blunt RochesterMatt GaetzNeal P. DunnJohn H. RutherfordDarren SotoBrian J. MastA. Drew Ferguson IVRaja KrishnamoorthiJim BanksRoger MarshallClay HigginsMike JohnsonJamie RaskinJack BergmanTed BuddDon BaconJosh GottheimerJacky RosenAdriano EspaillatBrian K. FitzpatrickLloyd SmuckerJenniffer González-ColónDavid KustoffVicente GonzalezJodey C. ArringtonPramila JayapalMike GallagherRon EstesRalph NormanJimmy GomezJohn R. CurtisTina SmithCindy Hyde-SmithDebbie LeskoMichael CloudTroy BaldersonKevin HernJoseph D. MorelleMary Gay ScanlonSusan WildEd CaseSteven HorsfordGreg StantonJosh HarderKatie PorterMike LevinJoe NeguseJason CrowJahana HayesMichael WaltzW. Gregory SteubeLucy McBathRuss FulcherJesús G. "Chuy" GarcíaSean CastenLauren UnderwoodJames R. BairdGreg PenceSharice DavidsLori TrahanAyanna PressleyDavid J. TroneElissa SlotkinHaley M. StevensRashida TlaibAngie CraigDean PhillipsIlhan OmarPete StauberMichael GuestKelly ArmstrongChris PappasJefferson Van DrewAndy KimMikie SherrillSusie LeeAlexandria Ocasio-CortezMadeleine DeanChrissy HoulahanDaniel MeuserJohn JoyceGuy ReschenthalerWilliam R. Timmons IVDusty JohnsonTim BurchettJohn W. RoseMark E. GreenDan CrenshawLance GoodenLizzie FletcherVeronica EscobarChip RoySylvia R. GarciaColin Z. AllredBen ClineAbigail Davis SpanbergerJennifer WextonKim SchrierBryan SteilCarol D. MillerRick ScottMike BraunJosh HawleyMitt RomneyJared F. GoldenDan BishopGregory F. MurphyKweisi MfumeThomas P. TiffanyMike GarciaMark KellyCynthia M. LummisDarrell IssaPete SessionsDavid G. ValadaoTommy TubervilleJohn W. HickenlooperBill HagertyJerry L. CarlBarry MooreJay ObernolteYoung KimMichelle SteelSara JacobsLauren BoebertKat CammackC. Scott FranklinByron DonaldsCarlos A. GimenezMaria Elvira SalazarNikema WilliamsAndrew S. ClydeMarjorie Taylor GreeneAshley HinsonMariannette Miller-MeeksRandy FeenstraMary E. MillerFrank J. MrvanVictoria SpartzTracey MannJake LaTurnerJake AuchinclossLisa C. McClainMichelle FischbachCori BushMatthew M. Rosendale, Sr.Deborah K. RossKathy E. ManningTeresa Leger FernandezAndrew R. GarbarinoNicole MalliotakisRitchie TorresJamaal BowmanStephanie I. BiceCliff BentzNancy MaceDiana HarshbargerPat FallonAugust PflugerRonny JacksonTroy E. NehlsTony GonzalesBeth Van DuyneBlake D. MooreBurgess OwensBob GoodMarilyn StricklandScott FitzgeraldAlex PadillaJon OssoffRaphael G. WarnockClaudia TenneyJulia LetlowTroy A. CarterMelanie A. StansburyJake EllzeyShontel M. BrownMike CareySheila Cherfilus-McCormickMike FloodBrad FinstadMary Sattler PeltolaPatrick RyanRudy Yakym IIIRyan K. ZinkeKatie Boyd BrittEric SchmittJ.D. VanceJohn FettermanDale W. StrongElijah CraneJuan CiscomaniKevin KileyJohn S. DuarteKevin MullinSydney Kamlager-DoveRobert GarciaBrittany PettersenYadira CaraveoAaron BeanCory MillsMaxwell FrostAnna Paulina LunaLaurel M. LeeJared MoskowitzRichard McCormickMike CollinsJames C. MoylanJill N. TokudaZachary NunnJonathan L. JacksonDelia C. RamirezNikki BudzinskiEric SorensenErin HouchinMorgan McGarveyGlenn IveyHillary J. ScholtenJohn JamesShri ThanedarMark AlfordEric BurlisonMike EzellDonald G. DavisValerie P. FousheeChuck EdwardsWiley NickelJeff JacksonThomas H. Kean, Jr.Robert MenendezGabe VasquezNick LaLotaGeorge SantosAnthony D’EspositoDaniel S. GoldmanMichael LawlerMarcus J. MolinaroBrandon WilliamsNicholas A. LangworthyGreg LandsmanMax L. MillerEmilia Strong SykesJosh BrecheenVal T. HoyleLori Chavez-DeRemerAndrea SalinasSummer L. LeeChristopher R. DeluzioSeth MagazinerRussell FryAndrew OglesNathaniel MoranKeith SelfMorgan LuttrellMonica De La CruzJasmine CrockettGreg CasarWesley HuntJennifer KiggansBecca BalintMarie Gluesenkamp PerezDerrick Van OrdenHarriet M. HagemanPete RickettsJennifer L. McClellan [Fork](https://observablehq.com/@observablehq/plot-stacked-dots "Open on Observable")

js

```
Plot.plot({
  aspectRatio: 1,
  x: {label: "Age (years)"},
  y: {
    grid: true,
    label: "← Women · Men →",
    labelAnchor: "center",
    tickFormat: Math.abs
  },
  marks: [\
    Plot.dot(\
      congress,\
      Plot.stackY2({\
        x: (d) => 2023 - d.birthday.getUTCFullYear(),\
        y: (d) => d.gender === "M" ? 1 : -1,\
        fill: "gender",\
        title: "full_name"\
      })\
    ),\
    Plot.ruleY([0])\
  ]
})
```

INFO

The stackY2 transform places each dot at the upper bound of the associated stacked interval, rather than the middle of the interval as when using stackY. Hence, the first male dot is placed at _y_ = 1, and the first female dot is placed at _y_ = -1.

TIP

The [dodge transform](https://observablehq.com/plot/transforms/dodge) can also be used to produce beeswarm plots; this is particularly effective when dots have varying radius.

Dots are sorted by descending radius by default [^0.5.0](https://github.com/observablehq/plot/releases/tag/v0.5.0 "added in v0.5.0") to mitigate occlusion; the smallest dots are drawn on top. Set the **sort** option to null to draw them in input order. Use the checkbox below to see the effect of sorting on a bubble map of U.S. county population.

Use default sort:

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
      sort: sorted ? undefined : null\
    }))\
  ]
})
```

The dot mark can also be used to construct a [quantile-quantile (QQ) plot](https://observablehq.com/@observablehq/qq-plot) for comparing two univariate distributions.

## Dot options [​](https://observablehq.com/plot/marks/dot\#dot-options)

In addition to the [standard mark options](https://observablehq.com/plot/features/marks#mark-options), the following optional channels are supported:

- **x** \- the horizontal position; bound to the _x_ scale
- **y** \- the vertical position; bound to the _y_ scale
- **r** \- the radius (area); bound to the _r_ (radius) scale, which defaults to _sqrt_
- **rotate** \- the rotation angle in degrees clockwise
- **symbol** \- the categorical symbol; bound to the _symbol_ scale [^0.4.0](https://github.com/observablehq/plot/releases/tag/v0.4.0 "added in v0.4.0")

If either of the **x** or **y** channels are not specified, the corresponding position is controlled by the **frameAnchor** option.

The following dot-specific constant options are also supported:

- **r** \- the effective radius (length); a number in pixels
- **rotate** \- the rotation angle in degrees clockwise; defaults to 0
- **symbol** \- the categorical symbol; defaults to _circle_ [^0.4.0](https://github.com/observablehq/plot/releases/tag/v0.4.0 "added in v0.4.0")
- **frameAnchor** \- how to position the dot within the frame; defaults to _middle_

The **r** option can be specified as either a channel or constant. When the radius is specified as a number, it is interpreted as a constant; otherwise it is interpreted as a channel. The radius defaults to 4.5 pixels when using the **symbol** channel, and otherwise 3 pixels. Dots with a nonpositive radius are not drawn.

The **stroke** defaults to _none_. The **fill** defaults to _currentColor_ if the stroke is _none_, and to _none_ otherwise. The **strokeWidth** defaults to 1.5. The **rotate** and **symbol** options can be specified as either channels or constants. When rotate is specified as a number, it is interpreted as a constant; otherwise it is interpreted as a channel. When symbol is a valid symbol name or symbol object (implementing the draw method), it is interpreted as a constant; otherwise it is interpreted as a channel. If the **symbol** channel’s values are all symbols, symbol names, or nullish, the channel is unscaled (values are interpreted literally); otherwise, the channel is bound to the _symbol_ scale.

## dot( _data_, _options_) [​](https://observablehq.com/plot/marks/dot\#dot)

js

```
Plot.dot(sales, {x: "units", y: "fruit"})
```

Returns a new dot with the given _data_ and _options_. If neither the **x** nor **y** nor **frameAnchor** options are specified, _data_ is assumed to be an array of pairs \[\[ _x₀_, _y₀_\], \[ _x₁_, _y₁_\], \[ _x₂_, _y₂_\], …\] such that **x** = \[ _x₀_, _x₁_, _x₂_, …\] and **y** = \[ _y₀_, _y₁_, _y₂_, …\].

## dotX( _data_, _options_) [​](https://observablehq.com/plot/marks/dot\#dotX)

js

```
Plot.dotX(cars.map((d) => d["economy (mpg)"]))
```

Equivalent to [dot](https://observablehq.com/plot/marks/dot#dot) except that if the **x** option is not specified, it defaults to the identity function and assumes that _data_ = \[ _x₀_, _x₁_, _x₂_, …\].

If an **interval** is specified, such as d3.utcDay, **y** is transformed to ( _interval_.floor( _y_) \+ _interval_.offset( _interval_.floor( _y_))) / 2\. If the interval is specified as a number _n_, _y_ will be the midpoint of two consecutive multiples of _n_ that bracket _y_. Named UTC intervals such as _day_ are also supported; see [scale options](https://observablehq.com/plot/features/scales#scale-options).

## dotY( _data_, _options_) [​](https://observablehq.com/plot/marks/dot\#dotY)

js

```
Plot.dotY(cars.map((d) => d["economy (mpg)"]))
```

Equivalent to [dot](https://observablehq.com/plot/marks/dot#dot) except that if the **y** option is not specified, it defaults to the identity function and assumes that _data_ = \[ _y₀_, _y₁_, _y₂_, …\].

If an **interval** is specified, such as d3.utcDay, **x** is transformed to ( _interval_.floor( _x_) \+ _interval_.offset( _interval_.floor( _x_))) / 2\. If the interval is specified as a number _n_, _x_ will be the midpoint of two consecutive multiples of _n_ that bracket _x_. Named UTC intervals such as _day_ are also supported; see [scale options](https://observablehq.com/plot/features/scales#scale-options).

## circle( _data_, _options_) [^0.5.0](https://github.com/observablehq/plot/releases/tag/v0.5.0 "added in v0.5.0") [​](https://observablehq.com/plot/marks/dot\#circle)

Equivalent to [dot](https://observablehq.com/plot/marks/dot#dot) except that the **symbol** option is set to _circle_.

## hexagon( _data_, _options_) [^0.5.0](https://github.com/observablehq/plot/releases/tag/v0.5.0 "added in v0.5.0") [​](https://observablehq.com/plot/marks/dot\#hexagon)

Equivalent to [dot](https://observablehq.com/plot/marks/dot#dot) except that the **symbol** option is set to _hexagon_.

Pager

[Previous pageDifference](https://observablehq.com/plot/marks/difference)

[Next pageFrame](https://observablehq.com/plot/marks/frame)

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

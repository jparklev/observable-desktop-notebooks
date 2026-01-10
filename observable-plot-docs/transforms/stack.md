---
url: "https://observablehq.com/plot/transforms/stack"
title: "Stack transform | Plot"
---

# Stack transform [​](https://observablehq.com/plot/transforms/stack\#stack-transform)

The **stack transform** comes in two orientations: [stackY](https://observablehq.com/plot/transforms/stack#stackY) replaces **y** with **y1** and **y2** to form vertical↑ stacks grouped on **x**, while [stackX](https://observablehq.com/plot/transforms/stack#stackX) replaces **x** with **x1** and **x2** for horizontal→ stacks grouped on **y**. In effect, stacking transforms a _length_ into _lower_ and _upper_ positions: the upper position of each element equals the lower position of the next element in the stack. Stacking makes it easier to perceive a total while still showing its parts.

For example, below is a stacked area chart of [deaths in the Crimean War](https://en.wikipedia.org/wiki/Florence_Nightingale#Crimean_War) — predominantly from disease — using Florence Nightingale’s data.

diseaseotherwounds

05001,0001,5002,0002,5003,000↑ deathsApr1854JulOctJan1855AprJulOctJan1856 [Fork](https://observablehq.com/@observablehq/plot-crimean-war-casualties "Open on Observable")

js

```
Plot.plot({
  y: {grid: true},
  color: {legend: true},
  marks: [\
    Plot.areaY(crimea, {x: "date", y: "deaths", fill: "cause"}),\
    Plot.ruleY([0])\
  ]
})
```

TIP

The [areaY mark](https://observablehq.com/plot/marks/area) applies the stackY transform implicitly if you do not specify either **y1** or **y2**. The same applies to [barY](https://observablehq.com/plot/marks/bar) and [rectY](https://observablehq.com/plot/marks/rect). You can invoke the stack transform explicitly as `Plot.stackY({x: "date", y: "deaths", fill: "cause"})` to produce an identical chart.

The stack transform works with any mark that consumes **y1** & **y2** or **x1** & **x2**, so you can stack rects, too.

05001,0001,5002,0002,5003,000↑ deathsApr1854JulOctJan1855AprJulOctJan1856Apr [Fork](https://observablehq.com/@observablehq/plot-crimean-war-recty "Open on Observable")

js

```
Plot.plot({
  y: {grid: true},
  marks: [\
    Plot.rectY(crimea, {x: "date", y: "deaths", interval: "month", fill: "cause"}),\
    Plot.ruleY([0])\
  ]
})
```

INFO

The [**interval** mark option](https://observablehq.com/plot/transforms/interval) specifies the periodicity of the data; without it, Plot wouldn’t know how wide to make the rects.

And you can stack bars if you’d prefer to treat _x_ as ordinal.

05001,0001,5002,0002,5003,000↑ deathsMJSDMJSD [Fork](https://observablehq.com/@observablehq/plot-crimean-war-bary "Open on Observable")

js

```
Plot.plot({
  x: {
    interval: "month",
    tickFormat: (d) => d.toLocaleString("en", {month: "narrow"}),
    label: null
  },
  y: {grid: true},
  marks: [\
    Plot.barY(crimea, {x: "date", y: "deaths", fill: "cause"}),\
    Plot.ruleY([0])\
  ]
})
```

INFO

The [**interval** scale option](https://observablehq.com/plot/features/scales#scale-transforms) specifies the periodicity of the data; without it, any gaps in the data would not be visible since barY implies that _x_ is ordinal.

The stackY transform also outputs **y** representing the midpoint of **y1** and **y2**, and likewise stackX outputs **x** representing the midpoint of **x1** and **x2**. This is useful for point-based marks such as [text](https://observablehq.com/plot/marks/text) and [dot](https://observablehq.com/plot/marks/dot). Below, a single stacked horizontal [bar](https://observablehq.com/plot/marks/bar) shows the relative frequency of English letters; this form is a compact alternative to a pie 🥧 or donut 🍩 chart.

0102030405060708090100frequency (%) →ETAOINSHRDLCUMWFGYPBVKJXQZ [Fork](https://observablehq.com/@observablehq/plot-stacked-percentages "Open on Observable")

js

```
Plot.plot({
  x: {percent: true},
  marks: [\
    Plot.barX(alphabet, Plot.stackX({x: "frequency", fillOpacity: 0.3, inset: 0.5})),\
    Plot.textX(alphabet, Plot.stackX({x: "frequency", text: "letter", inset: 0.5})),\
    Plot.ruleX([0, 1])\
  ]
})
```

The **order** option controls the order in which the layers are stacked. It defaults to null, meaning to respect the input order of the data. The _appearance_ order excels when each series has a prominent peak, as in the chart below of [recording industry](https://en.wikipedia.org/wiki/Recording_Industry_Association_of_America) revenue. Compact disc sales started declining well before the rise of downloads and streaming, suggesting that the industry was slow to provide a convenient digital product and hence lost revenue to piracy.

Order: nullappearanceinside-outsumgroupz

DiscDownloadOtherStreamingTapeVinyl

0246810121416182022↑ Annual revenue (billions, adj.)197519801985199019952000200520102015 [Fork](https://observablehq.com/@observablehq/plot-stacking-order "Open on Observable")

js

```
Plot.plot({
  y: {
    grid: true,
    label: "Annual revenue (billions, adj.)",
    transform: (d) => d / 1000 // convert millions to billions
  },
  color: {legend: true},
  marks: [\
    Plot.areaY(riaa, {x: "year", y: "revenue", z: "format", fill: "group", order}),\
    Plot.ruleY([0])\
  ]
})
```

INFO

In this data, the _group_ field is a supercategory of the _format_ field, which is useful to avoid overwhelming the color encoding with too many categories. For example, the _Vinyl_ group includes both the _LP/EP_ and _Vinyl Single_ formats.

The **reverse** option reverses the order of layers. In conjunction with the _appearance_ order, now layers enter from the bottom rather than the top.

Reverse:

DiscDownloadOtherStreamingTapeVinyl

0246810121416182022↑ Annual revenue (billions, adj.)197519801985199019952000200520102015 [Fork](https://observablehq.com/@observablehq/plot-stacking-order-and-reverse "Open on Observable")

js

```
Plot.plot({
  y: {
    grid: true,
    label: "Annual revenue (billions, adj.)",
    transform: (d) => d / 1000 // convert millions to billions
  },
  color: {legend: true},
  marks: [\
    Plot.areaY(riaa, Plot.stackY({order: "appearance", reverse}, {x: "year", y: "revenue", z: "format", fill: "group"})),\
    Plot.ruleY([0])\
  ]
})
```

TIP

The **reverse** option is also used by the [sort transform](https://observablehq.com/plot/transforms/sort). To disambiguate, pass the _stack_ options separately using the two-argument form of the stack transform as above.

The _value_ **order** is worth special mention: it sorts each stack by value independently such that the order of layers can change, emphasizing the changing ranks of layers. This is sometimes called a “ribbon” chart. (In fact, the default null **order** supports changing order of layers, too! But most often data comes already sorted by series.)

0246810121416182022↑ Annual revenue (billions, adj.)197519801985199019952000200520102015 [Fork](https://observablehq.com/@observablehq/plot-ribbon-chart "Open on Observable")

js

```
Plot.plot({
  y: {
    grid: true,
    label: "Annual revenue (billions, adj.)",
    transform: (d) => d / 1000 // convert millions to billions
  },
  marks: [\
    Plot.areaY(riaa, {x: "year", y: "revenue", z: "format", fill: "group", order: "value"}),\
    Plot.ruleY([0])\
  ]
})
```

The **offset** option controls the baseline of stacked layers. It defaults to null for a _y_ = 0 baseline (for stackY, or _x_ = 0 for stackX). The _center_ **offset** centers each stack independently per [Havre _et al._](https://innovis.cpsc.ucalgary.ca/innovis/uploads/Courses/InformationVisualizationDetails2009/Havre2000.pdf); the _wiggle_ **offset** minimizes apparent movement per [Byron & Wattenberg](http://leebyron.com/streamgraph/stackedgraphs_byron_wattenberg.pdf); these two offsets produce “streamgraphs”, so called for their fluid appearance. The _wiggle_ **offset** changes the default **order** to _inside-out_ to further minimize movement.

Offset: nullcenterwiggle

024681012141618202224↑ Annual revenue (billions, adj.)197519801985199019952000200520102015 [Fork](https://observablehq.com/@observablehq/plot-stack-offset "Open on Observable")

js

```
Plot.plot({
  y: {
    grid: true,
    label: "Annual revenue (billions, adj.)",
    transform: (d) => d / 1000
  },
  marks: [\
    Plot.areaY(riaa, {x: "year", y: "revenue", z: "format", fill: "group", offset})\
  ]
})
```

CAUTION

When **offset** is not null, the _y_ axis is harder to use because there is no longer a shared baseline at _y_ = 0, though it is still useful for eyeballing length.

The _normalize_ **offset** is again worth special mention: it scales stacks to fill the interval \[0, 1\], thereby showing the relative proportion of each layer. Sales of compact discs accounted for over 90% of revenue in the early 2000’s, but now most revenue comes from streaming.

0102030405060708090100↑ Annual revenue (%)197519801985199019952000200520102015 [Fork](https://observablehq.com/@observablehq/plot-normalized-stack "Open on Observable")

js

```
Plot.plot({
  y: {
    label: "Annual revenue (%)",
    percent: true
  },
  marks: [\
    Plot.areaY(riaa, Plot.stackY({offset: "normalize", order: "group", reverse: true}, {x: "year", y: "revenue", z: "format", fill: "group"})),\
    Plot.ruleY([0, 1])\
  ]
})
```

When the provided length (typically **y**) is negative, in conjunction with the null **offset** the stack transform will produce diverging stacks on opposites sides of the zero baseline. The diverging stacked dot plot below shows the age and gender distribution of the U.S. Congress in 2023. This form is also often _popular_ for [population pyramids](https://observablehq.com/@observablehq/plot-population-pyramid).

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

When visualizing [Likert scale](https://en.wikipedia.org/wiki/Likert_scale) survey results we may wish to place negative (disagreeing) responses on the left and positive (agreeing) responses on the right, leaving neutral responses in the middle. This is achieved below using a custom **offset** function.

Strongly DisagreeDisagreeNeutralAgreeStrongly Agree

Q1Q2Q3Q4Q5Question6040200204060Frequency → [Fork](https://observablehq.com/@observablehq/plot-diverging-stacked-bar "Open on Observable")

js

```
Plot.plot({
  x: {tickFormat: Math.abs},
  color: {domain: likert.order, scheme: "RdBu", legend: true},
  marks: [\
    Plot.barX(\
      survey,\
      Plot.groupZ({x: "count"}, {fy: "Question", fill: "Response", ...likert})\
    ),\
    Plot.ruleX([0])\
  ]
})
```

Here `likert` declares which response values are negative (`-1`), which are positive (`1`), and which are neutral (`0`).

js

```
likert = Likert([\
  ["Strongly Disagree", -1],\
  ["Disagree", -1],\
  ["Neutral", 0],\
  ["Agree", 1],\
  ["Strongly Agree", 1]\
])
```

And `Likert` implements the **order** (as an explicit array of ordinal values, such that the ordinal color scale lists in the correct order rather than sorting alphabetically) and **offset** (as a function that mutates the **x1** and **x2** channel values) stack options.

js

```
function Likert(responses) {
  const map = new Map(responses);
  return {
    order: Array.from(map.keys()),
    offset(I, X1, X2, Z) {
      for (const stacks of I) {
        for (const stack of stacks) {
          const k = d3.sum(stack, (i) => (X2[i] - X1[i]) * (1 - map.get(Z[i]))) / 2;
          for (const i of stack) {
            X1[i] -= k;
            X2[i] -= k;
          }
        }
      }
    }
  };
}
```

See the [Marimekko example](https://observablehq.com/@observablehq/plot-marimekko) for another interesting application of the stack transform.

## Stack options [​](https://observablehq.com/plot/transforms/stack\#stack-options)

The stackY transform groups on **x** and transforms **y** into **y1** and **y2**; the stackX transform groups on **y** and transforms **x** into **x1** and **x2**. If **y** is not specified for stackY, or if **x** is not specified for stackX, it defaults to the constant one, which is useful for constructing simple isotype charts ( _e.g._, stacked dots).

The supported stack options are:

- **offset** \- the offset (or baseline) method
- **order** \- the order in which stacks are layered
- **reverse** \- true to reverse order

The following **order** methods are supported:

- null (default) - input order
- _value_ \- ascending value order (or descending with **reverse**)
- _x_ \- alias of _value_; for stackX only
- _y_ \- alias of _value_; for stackY only
- _sum_ \- order series by their total value
- _appearance_ \- order series by the position of their maximum value
- _inside-out_ (default with _wiggle_) \- order the earliest-appearing series on the inside
- a named field or function of data - order data by priority
- an array of _z_ values

The **reverse** option reverses the effective order. For the _value_ order, stackY uses the _y_ value while stackX uses the _x_ value. For the _appearance_ order, stackY uses the _x_ position of the maximum _y_ value while stackX uses the _y_ position of the maximum _x_ value. If an array of _z_ values are specified, they should enumerate the _z_ values for all series in the desired order; this array is typically hard-coded or computed with [d3.groupSort](https://d3js.org/d3-array/group#groupSort). Note that the input order (null) and _value_ order can produce crossing paths: they do not guarantee a consistent series order across stacks.

The stack transform supports diverging stacks: negative values are stacked below zero while positive values are stacked above zero. For stackY, the **y1** channel contains the value of lesser magnitude (closer to zero) while the **y2** channel contains the value of greater magnitude (farther from zero); the difference between the two corresponds to the input **y** channel value. For stackX, the same is true, except for **x1**, **x2**, and **x** respectively.

After all values have been stacked from zero, an optional **offset** can be applied to translate or scale the stacks. The following **offset** methods are supported:

- null (default) - a zero baseline
- _normalize_ \- rescale each stack to fill \[0, 1\]
- _center_ \- align the centers of all stacks
- _wiggle_ \- translate stacks to minimize apparent movement
- a function to be passed a nested index, and start, end, and _z_ values

If a given stack has zero total value, the _normalize_ offset will not adjust the stack’s position. Both the _center_ and _wiggle_ offsets ensure that the lowest element across stacks starts at zero for better default axes. The _wiggle_ offset is recommended for streamgraphs, and if used, changes the default order to _inside-out_; see [Byron & Wattenberg](http://leebyron.com/streamgraph/).

If the offset is specified as a function, it will receive four arguments: an index of stacks nested by facet and then stack, an array of start values, an array of end values, and an array of _z_ values. For stackX, the start and end values correspond to **x1** and **x2**, while for stackY, the start and end values correspond to **y1** and **y2**. The offset function is then responsible for mutating the arrays of start and end values, such as by subtracting a common offset for each of the indices that pertain to the same stack.

In addition to the **y1** and **y2** output channels, stackY computes a **y** output channel that represents the midpoint of **y1** and **y2**; stackX does the same for **x**. This can be used to position a label or a dot in the center of a stacked layer. The **x** and **y** output channels are lazy: they are only computed if needed by a downstream mark or transform.

If two arguments are passed to the stack transform functions below, the stack-specific options ( **offset**, **order**, and **reverse**) are pulled exclusively from the first _options_ argument, while any channels ( _e.g._, **x**, **y**, and **z**) are pulled from second _options_ argument. Options from the second argument that are not consumed by the stack transform will be passed through. Using two arguments is sometimes necessary is disambiguate the option recipient when chaining transforms.

## stackY( _stack_, _options_) [​](https://observablehq.com/plot/transforms/stack\#stackY)

js

```
Plot.stackY({x: "year", y: "revenue", z: "format", fill: "group"})
```

Creates new channels **y1** and **y2**, obtained by stacking the original **y** channel for data points that share a common **x** (and possibly **z**) value. A new **y** channel is also returned, which lazily computes the middle value of **y1** and **y2**. The input **y** channel defaults to a constant 1, resulting in a count of the data points. The stack options ( **offset**, **order**, and **reverse**) may be specified as part of the _options_ object, if the only argument, or as a separate _stack_ options argument.

## stackY1( _stack_, _options_) [​](https://observablehq.com/plot/transforms/stack\#stackY1)

js

```
Plot.stackY1({x: "year", y: "revenue", z: "format", fill: "group"})
```

Like [stackY](https://observablehq.com/plot/transforms/stack#stackY), except that the **y1** channel is returned as the **y** channel. This can be used, for example, to draw a line at the bottom of each stacked area.

## stackY2( _stack_, _options_) [​](https://observablehq.com/plot/transforms/stack\#stackY2)

js

```
Plot.stackY2({x: "year", y: "revenue", z: "format", fill: "group"})
```

Like [stackY](https://observablehq.com/plot/transforms/stack#stackY), except that the **y2** channel is returned as the **y** channel. This can be used, for example, to draw a line at the top of each stacked area.

## stackX( _stack_, _options_) [​](https://observablehq.com/plot/transforms/stack\#stackX)

js

```
Plot.stackX({y: "year", x: "revenue", z: "format", fill: "group"})
```

Like [stackY](https://observablehq.com/plot/transforms/stack#stackY), but with _x_ as the input value channel, _y_ as the stack index, _x1_, _x2_ and _x_ as the output channels.

## stackX1( _stack_, _options_) [​](https://observablehq.com/plot/transforms/stack\#stackX1)

js

```
Plot.stackX1({y: "year", x: "revenue", z: "format", fill: "group"})
```

Like [stackX](https://observablehq.com/plot/transforms/stack#stackX), except that the **x1** channel is returned as the **x** channel. This can be used, for example, to draw a line at the left edge of each stacked area.

## stackX2( _stack_, _options_) [​](https://observablehq.com/plot/transforms/stack\#stackX2)

js

```
Plot.stackX2({y: "year", x: "revenue", z: "format", fill: "group"})
```

Like [stackX](https://observablehq.com/plot/transforms/stack#stackX), except that the **x2** channel is returned as the **x** channel. This can be used, for example, to draw a line at the right edge of each stacked area.

Pager

[Previous pageSort](https://observablehq.com/plot/transforms/sort)

[Next pageTree](https://observablehq.com/plot/transforms/tree)

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

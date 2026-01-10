---
url: "https://observablehq.com/framework/lib/sqlite"
title: "SQLite | Observable Framework"
---

# [SQLite](https://observablehq.com/framework/lib/sqlite\#sq-lite)

[SQLite](https://sqlite.org/) is “a small, fast, self-contained, high-reliability, full-featured, SQL database engine” and “the most used database engine in the world.” Observable provides a ESM-compatible distribution of [sql.js](https://sql.js.org/), a WASM-based distribution of SQLite. It is available by default as `SQLite` in Markdown, but you can import it like so:

```js
import SQLite from "npm:@observablehq/sqlite";
```

If you prefer to use sql.js directly, you can import and initialize it like so:

```js
import initSqlJs from "npm:sql.js";

const SQLite = await initSqlJs({locateFile: (name) => import.meta.resolve("npm:sql.js/dist/") + name});
```

We also provide `SQLiteDatabaseClient`, a [`DatabaseClient`](https://observablehq.com/@observablehq/database-client-specification) implementation.

```js
import {SQLiteDatabaseClient} from "npm:@observablehq/sqlite";
```

The easiest way to construct a SQLite database client is to declare a [`FileAttachment`](https://observablehq.com/framework/files) and then call `file.sqlite` to load a SQLite file. This returns a promise. (Here we rely on [implicit await](https://observablehq.com/framework/reactivity#promises).)

```js
const db = FileAttachment("chinook.db").sqlite();
```

Alternatively you can use `SQLiteDatabaseClient` and pass in a string (URL), `Blob`, `ArrayBuffer`, `Uint8Array`, `FileAttachment`, or promise to the same:

```js
const db = SQLiteDatabaseClient.open(FileAttachment("chinook.db"));
```

(Note that unlike [`DuckDBClient`](https://observablehq.com/framework/lib/duckdb), a `SQLiteDatabaseClient` takes a single argument representing _all_ of the tables in the database; that’s because a SQLite file stores multiple tables, whereas DuckDB typically uses separate Apache Parquet, CSV, or JSON files for each table.)

Using `FileAttachment` means that referenced files are automatically copied to `dist` during build, and you can even generate SQLite files using [data loaders](https://observablehq.com/framework/data-loaders). But if you want to “hot” load a live file from an external server, pass a string to `SQLiteDatabaseClient.open`:

```js
const db = SQLiteDatabaseClient.open("https://static.observableusercontent.com/files/b3711cfd9bdf50cbe4e74751164d28e907ce366cd4bf56a39a980a48fdc5f998c42a019716a8033e2b54defdd97e4a55ebe4f6464b4f0678ea0311532605a115");
```

Once you’ve loaded your `db` you can write SQL queries.

Array(59) \[Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, …\]

```js
const customers = db.sql`SELECT * FROM customers`;

display(await customers);
```

A call to `db.sql` returns a promise to an array of objects; each object represents a row returned from the query. For better readability, you can display query results using [`Inputs.table`](https://observablehq.com/framework/inputs/table).

|  | CustomerId | FirstName | LastName | Company | Address | City | State | Country | PostalCode | Phone | Fax | Email | SupportRepId |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | 1 | Luís | Gonçalves | Embraer - Empresa Brasileira de Aeronáutica S.A. | Av. Brigadeiro Faria Lima, 2170 | São José dos Campos | SP | Brazil | 12227-000 | +55 (12) 3923-5555 | +55 (12) 3923-5566 | luisg@embraer.com.br | 3 |
|  | 2 | Leonie | Köhler |  | Theodor-Heuss-Straße 34 | Stuttgart |  | Germany | 70174 | +49 0711 2842222 |  | leonekohler@surfeu.de | 5 |
|  | 3 | François | Tremblay |  | 1498 rue Bélanger | Montréal | QC | Canada | H2G 1A7 | +1 (514) 721-4711 |  | ftremblay@gmail.com | 3 |
|  | 4 | Bjørn | Hansen |  | Ullevålsveien 14 | Oslo |  | Norway | 0171 | +47 22 44 22 22 |  | bjorn.hansen@yahoo.no | 4 |
|  | 5 | František | Wichterlová | JetBrains s.r.o. | Klanova 9/506 | Prague |  | Czech Republic | 14700 | +420 2 4172 5555 | +420 2 4172 5555 | frantisekw@jetbrains.com | 4 |
|  | 6 | Helena | Holý |  | Rilská 3174/6 | Prague |  | Czech Republic | 14300 | +420 2 4177 0449 |  | hholy@gmail.com | 5 |
|  | 7 | Astrid | Gruber |  | Rotenturmstraße 4, 1010 Innere Stadt | Vienne |  | Austria | 1010 | +43 01 5134505 |  | astrid.gruber@apple.at | 5 |
|  | 8 | Daan | Peeters |  | Grétrystraat 63 | Brussels |  | Belgium | 1000 | +32 02 219 03 03 |  | daan\_peeters@apple.be | 4 |
|  | 9 | Kara | Nielsen |  | Sønder Boulevard 51 | Copenhagen |  | Denmark | 1720 | +453 3331 9991 |  | kara.nielsen@jubii.dk | 4 |
|  | 10 | Eduardo | Martins | Woodstock Discos | Rua Dr. Falcão Filho, 155 | São Paulo | SP | Brazil | 01007-010 | +55 (11) 3033-5446 | +55 (11) 3033-4564 | eduardo@woodstock.com.br | 4 |
|  | 11 | Alexandre | Rocha | Banco do Brasil S.A. | Av. Paulista, 2022 | São Paulo | SP | Brazil | 01310-200 | +55 (11) 3055-3278 | +55 (11) 3055-8131 | alero@uol.com.br | 5 |
|  | 12 | Roberto | Almeida | Riotur | Praça Pio X, 119 | Rio de Janeiro | RJ | Brazil | 20040-020 | +55 (21) 2271-7000 | +55 (21) 2271-7070 | roberto.almeida@riotur.gov.br | 3 |
|  | 13 | Fernanda | Ramos |  | Qe 7 Bloco G | Brasília | DF | Brazil | 71020-677 | +55 (61) 3363-5547 | +55 (61) 3363-7855 | fernadaramos4@uol.com.br | 4 |
|  | 14 | Mark | Philips | Telus | 8210 111 ST NW | Edmonton | AB | Canada | T6G 2C7 | +1 (780) 434-4554 | +1 (780) 434-5565 | mphilips12@shaw.ca | 5 |
|  | 15 | Jennifer | Peterson | Rogers Canada | 700 W Pender Street | Vancouver | BC | Canada | V6C 1G8 | +1 (604) 688-2255 | +1 (604) 688-8756 | jenniferp@rogers.ca | 3 |
|  | 16 | Frank | Harris | Google Inc. | 1600 Amphitheatre Parkway | Mountain View | CA | USA | 94043-1351 | +1 (650) 253-0000 | +1 (650) 253-0000 | fharris@google.com | 4 |
|  | 17 | Jack | Smith | Microsoft Corporation | 1 Microsoft Way | Redmond | WA | USA | 98052-8300 | +1 (425) 882-8080 | +1 (425) 882-8081 | jacksmith@microsoft.com | 5 |
|  | 18 | Michelle | Brooks |  | 627 Broadway | New York | NY | USA | 10012-2612 | +1 (212) 221-3546 | +1 (212) 221-4679 | michelleb@aol.com | 3 |
|  | 19 | Tim | Goyer | Apple Inc. | 1 Infinite Loop | Cupertino | CA | USA | 95014 | +1 (408) 996-1010 | +1 (408) 996-1011 | tgoyer@apple.com | 3 |
|  | 20 | Dan | Miller |  | 541 Del Medio Avenue | Mountain View | CA | USA | 94040-111 | +1 (650) 644-3358 |  | dmiller@comcast.com | 4 |
|  | 21 | Kathy | Chase |  | 801 W 4th Street | Reno | NV | USA | 89503 | +1 (775) 223-7665 |  | kachase@hotmail.com | 5 |
|  | 22 | Heather | Leacock |  | 120 S Orange Ave | Orlando | FL | USA | 32801 | +1 (407) 999-7788 |  | hleacock@gmail.com | 4 |
|  | 23 | John | Gordon |  | 69 Salem Street | Boston | MA | USA | 2113 | +1 (617) 522-1333 |  | johngordon22@yahoo.com | 4 |

```js
Inputs.table(customers)
```

For interactive or dynamic queries, you can interpolate reactive variables into SQL queries. For example, you can declare a [text input](https://observablehq.com/framework/inputs/text) to prompt the query to enter a search term, and then interpolate the input into the query parameter.

Name

```js
const name = view(Inputs.text({label: "Name", placeholder: "Search track names"}));
```

```js
const tracks = db.sql`SELECT * FROM tracks WHERE Name LIKE ${`%${name}%`}`;
```

|  | TrackId | Name | AlbumId | MediaTypeId | GenreId | Composer | Milliseconds | Bytes | UnitPrice |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | 1 | For Those About To Rock (We Salute You) | 1 | 1 | 1 | Angus Young, Malcolm Young, Brian Johnson | 343,719 | 11,170,334 | 0.99 |
|  | 2 | Balls to the Wall | 2 | 2 | 1 |  | 342,562 | 5,510,424 | 0.99 |
|  | 3 | Fast As a Shark | 3 | 2 | 1 | F. Baltes, S. Kaufman, U. Dirkscneider & W. Hoffman | 230,619 | 3,990,994 | 0.99 |
|  | 4 | Restless and Wild | 3 | 2 | 1 | F. Baltes, R.A. Smith-Diesel, S. Kaufman, U. Dirkscneider & W. Hoffman | 252,051 | 4,331,779 | 0.99 |
|  | 5 | Princess of the Dawn | 3 | 2 | 1 | Deaffy & R.A. Smith-Diesel | 375,418 | 6,290,521 | 0.99 |
|  | 6 | Put The Finger On You | 1 | 1 | 1 | Angus Young, Malcolm Young, Brian Johnson | 205,662 | 6,713,451 | 0.99 |
|  | 7 | Let's Get It Up | 1 | 1 | 1 | Angus Young, Malcolm Young, Brian Johnson | 233,926 | 7,636,561 | 0.99 |
|  | 8 | Inject The Venom | 1 | 1 | 1 | Angus Young, Malcolm Young, Brian Johnson | 210,834 | 6,852,860 | 0.99 |
|  | 9 | Snowballed | 1 | 1 | 1 | Angus Young, Malcolm Young, Brian Johnson | 203,102 | 6,599,424 | 0.99 |
|  | 10 | Evil Walks | 1 | 1 | 1 | Angus Young, Malcolm Young, Brian Johnson | 263,497 | 8,611,245 | 0.99 |
|  | 11 | C.O.D. | 1 | 1 | 1 | Angus Young, Malcolm Young, Brian Johnson | 199,836 | 6,566,314 | 0.99 |
|  | 12 | Breaking The Rules | 1 | 1 | 1 | Angus Young, Malcolm Young, Brian Johnson | 263,288 | 8,596,840 | 0.99 |
|  | 13 | Night Of The Long Knives | 1 | 1 | 1 | Angus Young, Malcolm Young, Brian Johnson | 205,688 | 6,706,347 | 0.99 |
|  | 14 | Spellbound | 1 | 1 | 1 | Angus Young, Malcolm Young, Brian Johnson | 270,863 | 8,817,038 | 0.99 |
|  | 15 | Go Down | 4 | 1 | 1 | AC/DC | 331,180 | 10,847,611 | 0.99 |
|  | 16 | Dog Eat Dog | 4 | 1 | 1 | AC/DC | 215,196 | 7,032,162 | 0.99 |
|  | 17 | Let There Be Rock | 4 | 1 | 1 | AC/DC | 366,654 | 12,021,261 | 0.99 |
|  | 18 | Bad Boy Boogie | 4 | 1 | 1 | AC/DC | 267,728 | 8,776,140 | 0.99 |
|  | 19 | Problem Child | 4 | 1 | 1 | AC/DC | 325,041 | 10,617,116 | 0.99 |
|  | 20 | Overdose | 4 | 1 | 1 | AC/DC | 369,319 | 12,066,294 | 0.99 |
|  | 21 | Hell Ain't A Bad Place To Be | 4 | 1 | 1 | AC/DC | 254,380 | 8,331,286 | 0.99 |
|  | 22 | Whole Lotta Rosie | 4 | 1 | 1 | AC/DC | 323,761 | 10,547,154 | 0.99 |
|  | 23 | Walk On Water | 5 | 1 | 1 | Steven Tyler, Joe Perry, Jack Blades, Tommy Shaw | 295,680 | 9,719,579 | 0.99 |

As an alternative to `db.sql`, you can call `db.query`.

```js
db.query(`SELECT * FROM tracks WHERE Name LIKE $1`, [`%${name}%`])
```

There’s also `db.queryRow` for just getting a single row.

Object {sqlite\_version(): "3.49.1"}

```js
db.queryRow(`SELECT sqlite_version()`)
```

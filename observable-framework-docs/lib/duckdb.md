---
url: "https://observablehq.com/framework/lib/duckdb"
title: "DuckDB | Observable Framework"
---

1. [Extensions](https://observablehq.com/framework/lib/duckdb#extensions)
2. [Configuring](https://observablehq.com/framework/lib/duckdb#configuring)
3. [Versioning](https://observablehq.com/framework/lib/duckdb#versioning)

# [DuckDB](https://observablehq.com/framework/lib/duckdb\#duck-db)

The most convenient way to use DuckDB in Observable is the built-in [SQL code blocks](https://observablehq.com/framework/sql) and [`sql` tagged template literal](https://observablehq.com/framework/sql#sql-literals). Use `DuckDBClient` or DuckDB-Wasm directly, as shown here, if you need greater control.

DuckDB is “an in-process SQL OLAP Database Management System. [DuckDB-Wasm](https://github.com/duckdb/duckdb-wasm) brings DuckDB to every browser thanks to WebAssembly.” DuckDB-Wasm is available by default as `duckdb` in Markdown, but you can explicitly import it as:

```js
import * as duckdb from "npm:@duckdb/duckdb-wasm";
```

For convenience, we provide a [`DatabaseClient`](https://observablehq.com/@observablehq/database-client-specification) implementation on top of DuckDB-Wasm, `DuckDBClient`. This is also available by default in Markdown, but you can explicitly import it like so:

```js
import {DuckDBClient} from "npm:@observablehq/duckdb";
```

To get a DuckDB client, pass zero or more named tables to `DuckDBClient.of`. Each table can be expressed as a [`FileAttachment`](https://observablehq.com/framework/files), [Arquero table](https://observablehq.com/framework/lib/arquero), [Arrow table](https://observablehq.com/framework/lib/arrow), an array of objects, or a promise to the same. For file attachments, the following formats are supported: [CSV](https://observablehq.com/framework/lib/csv), [TSV](https://observablehq.com/framework/lib/csv), [JSON](https://observablehq.com/framework/files#json), [Apache Arrow](https://observablehq.com/framework/lib/arrow), and [Apache Parquet](https://observablehq.com/framework/lib/arrow#apache-parquet). For example, below we load a sample of 250,000 stars from the [Gaia Star Catalog](https://observablehq.com/@cmudig/peeking-into-the-gaia-star-catalog) as a Parquet file:

```js
const db = DuckDBClient.of({gaia: FileAttachment("gaia-sample.parquet")});
```

Now we can run a query using `db.sql` to bin the stars by [right ascension](https://en.wikipedia.org/wiki/Right_ascension) (`ra`) and [declination](https://en.wikipedia.org/wiki/Declination) (`dec`):

```js
const bins = db.sql`SELECT
  floor(ra / 2) * 2 + 1 AS ra,
  floor(dec / 2) * 2 + 1 AS dec,
  count() AS count
FROM
  gaia
GROUP BY
  1,
  2`
```

These bins can quickly be turned into a heatmap with [Plot’s raster mark](https://observablehq.com/plot/marks/raster), showing the milky way.

```js
Plot.plot({
  aspectRatio: 1,
  x: {domain: [0, 360]},
  y: {domain: [-90, 90]},
  marks: [\
    Plot.frame({fill: 0}),\
    Plot.raster(bins, {\
      x: "ra",\
      y: "dec",\
      fill: "count",\
      width: 360 / 2,\
      height: 180 / 2,\
      imageRendering: "pixelated"\
    })\
  ]
})
```

You can also [attach](https://duckdb.org/docs/sql/statements/attach) a complete database saved as DuckDB file, [Added in 1.4.0](https://github.com/observablehq/framework/releases/tag/v1.4.0 "Added in 1.4.0") typically using the `.db` file extension (or `.ddb` or `.duckdb`). In this case, the associated name (below `base`) is a _schema_ name rather than a _table_ name.

```js
const db2 = await DuckDBClient.of({base: FileAttachment("quakes.db")});
```

```js
db2.queryRow(`SELECT COUNT() FROM base.events`)
```

For externally-hosted data, you can create an empty `DuckDBClient` and load a table from a SQL query, say using [`read_parquet`](https://duckdb.org/docs/guides/import/parquet_import) or [`read_csv`](https://duckdb.org/docs/guides/import/csv_import). DuckDB offers many affordances to make this easier. (In many cases it detects the file format and uses the correct loader automatically.)

```js
const db = await DuckDBClient.of();

await db.sql`CREATE TABLE addresses
  AS SELECT *
  FROM read_parquet('https://static.data.gouv.fr/resources/bureaux-de-vote-et-adresses-de-leurs-electeurs/20230626-135723/table-adresses-reu.parquet')
  LIMIT 100`;
```

As an alternative to `db.sql`, there’s also `db.query`:

```js
db.query("SELECT * FROM gaia LIMIT 10")
```

The `db.sql` and `db.query` methods return a promise to an [Arrow table](https://observablehq.com/framework/lib/arrow). This columnar representation is much more efficient than an array-of-objects. You can inspect the contents of an Arrow table using [`Inputs.table`](https://observablehq.com/framework/inputs/table) and pass the data to [Plot](https://observablehq.com/framework/lib/plot).

And `db.queryRow`:

```js
db.queryRow("SELECT count() AS count FROM gaia")
```

See the [DatabaseClient Specification](https://observablehq.com/@observablehq/database-client-specification) for more details on these methods.

Finally, the `DuckDBClient.sql` method [Added in 1.4.0](https://github.com/observablehq/framework/releases/tag/v1.4.0 "Added in 1.4.0") takes the same arguments as `DuckDBClient.of` and returns the corresponding `db.sql` tagged template literal. The returned function can be used to redefine the built-in [`sql` tagged template literal](https://observablehq.com/framework/sql#sql-literals) and thereby change the database used by [SQL code blocks](https://observablehq.com/framework/sql), allowing you to query dynamically-registered tables (unlike the **sql** front matter option).

Earthquake feedM4.5+M2.5+All

```js
const sql = DuckDBClient.sql({quakes: `https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/${feed}_day.csv`});
```

```sql
SELECT * FROM quakes ORDER BY updated DESC;
```

## [Extensions](https://observablehq.com/framework/lib/duckdb\#extensions) [Added in 1.13.0](https://github.com/observablehq/framework/releases/tag/v1.13.0 "Added in 1.13.0")

[DuckDB extensions](https://duckdb.org/docs/extensions/overview.html) extend DuckDB’s functionality, adding support for additional file formats, new types, and domain-specific functions. For example, the [`json` extension](https://duckdb.org/docs/data/json/overview.html) provides a `read_json` method for reading JSON files:

```sql
SELECT bbox FROM read_json('https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson');
```

To read a local file (or data loader), use `FileAttachment` and interpolation `${…}`:

```sql
SELECT bbox FROM read_json(${FileAttachment("../quakes.json").href});
```

For convenience, Framework configures the `json` and `parquet` extensions by default. Some other [core extensions](https://duckdb.org/docs/extensions/core_extensions.html) also autoload, meaning that you don’t need to explicitly enable them; however, Framework will only [self-host extensions](https://observablehq.com/framework/lib/duckdb#self-hosting-of-extensions) if you explicitly configure them, and therefore we recommend that you always use the [**duckdb** config option](https://observablehq.com/framework/config#duckdb) to configure DuckDB extensions. Any configured extensions will be automatically [installed and loaded](https://duckdb.org/docs/extensions/overview#explicit-install-and-load), making them available in SQL code blocks as well as the `sql` and `DuckDBClient` built-ins.

For example, to configure the [`spatial` extension](https://duckdb.org/docs/extensions/spatial/overview.html):

```js
export default {
  duckdb: {
    extensions: ["spatial"]
  }
};
```

You can then use the `ST_Area` function to compute the area of a polygon:

```sql
SELECT ST_Area('POLYGON((0 0, 0 1, 1 1, 1 0, 0 0))'::GEOMETRY) as area;
```

To tell which extensions have been loaded, you can run the following query:

```sql
FROM duckdb_extensions() WHERE loaded;
```

If the `duckdb_extensions()` function runs before DuckDB autoloads a core extension (such as `json`), it might not be included in the returned set.

### [Self-hosting of extensions](https://observablehq.com/framework/lib/duckdb\#self-hosting-of-extensions)

As with [npm imports](https://observablehq.com/framework/imports#self-hosting-of-npm-imports), configured DuckDB extensions are self-hosted, improving performance, stability, & security, and allowing you to develop offline. Extensions are downloaded to the DuckDB cache folder, which lives in `.observablehq/cache/_duckdb` within the source root (typically `src`). You can clear the cache and restart the preview server to re-fetch the latest versions of any DuckDB extensions. If you use an [autoloading core extension](https://duckdb.org/docs/extensions/core_extensions.html#list-of-core-extensions) that is not configured, DuckDB-Wasm [will load it](https://duckdb.org/docs/api/wasm/extensions.html#fetching-duckdb-wasm-extensions) from the default extension repository, `extensions.duckdb.org`, at runtime.

## [Configuring](https://observablehq.com/framework/lib/duckdb\#configuring)

The second argument to `DuckDBClient.of` and `DuckDBClient.sql` is a [`DuckDBConfig`](https://shell.duckdb.org/docs/interfaces/index.DuckDBConfig.html) object which configures the behavior of DuckDB-Wasm. By default, Framework sets the `castBigIntToDouble` and `castTimestampToDate` query options to true. To instead use [`BigInt`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/BigInt):

```js
const bigdb = DuckDBClient.of({}, {query: {castBigIntToDouble: false}});
```

By default, `DuckDBClient.of` and `DuckDBClient.sql` automatically load all [configured extensions](https://observablehq.com/framework/lib/duckdb#extensions). To change the loaded extensions for a particular `DuckDBClient`, use the **extensions** config option. For example, pass an empty array to instantiate a DuckDBClient with no loaded extensions (even if your configuration lists several):

```js
const simpledb = DuckDBClient.of({}, {extensions: []});
```

Alternatively, you can configure extensions to be self-hosted but not load by default using the **duckdb** config option and the `load: false` shorthand:

```js
export default {
  duckdb: {
    extensions: {
      spatial: false,
      h3: false
    }
  }
};
```

You can then selectively load extensions as needed like so:

```js
const geosql = DuckDBClient.sql({}, {extensions: ["spatial", "h3"]});
```

In the future, we’d like to allow DuckDB to be configured globally (beyond just [extensions](https://observablehq.com/framework/lib/duckdb#extensions)) via the [**duckdb** config option](https://observablehq.com/framework/config#duckdb); please upvote [#1791](https://github.com/observablehq/framework/issues/1791) if you are interested in this feature.

## [Versioning](https://observablehq.com/framework/lib/duckdb\#versioning)

Framework currently uses [DuckDB-Wasm 1.29.0](https://github.com/duckdb/duckdb-wasm/releases/tag/v1.29.0) [Added in 1.13.0](https://github.com/observablehq/framework/releases/tag/v1.13.0 "Added in 1.13.0"), which aligns with [DuckDB 1.1.1](https://github.com/duckdb/duckdb/releases/tag/v1.1.1). You can load a different version of DuckDB-Wasm by importing `npm:@duckdb/duckdb-wasm` directly, for example:

```js
import * as duckdb from "npm:@duckdb/duckdb-wasm@1.28.0";
```

However, you will not be able to change the version of DuckDB-Wasm used by SQL code blocks or the `sql` or `DuckDBClient` built-ins, nor can you use Framework’s support for self-hosting extensions with a different version of DuckDB-Wasm.

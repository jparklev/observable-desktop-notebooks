---
url: "https://observablehq.com/framework/what-is-framework"
title: "What is Framework? | Observable Framework"
---

1. [The power of code](https://observablehq.com/framework/what-is-framework#the-power-of-code)
2. [Polyglot meets the web](https://observablehq.com/framework/what-is-framework#polyglot-meets-the-web)
3. [Static-site architecture](https://observablehq.com/framework/what-is-framework#static-site-architecture)
4. [Automatic reactivity](https://observablehq.com/framework/what-is-framework#automatic-reactivity)
5. [An end-to-end solution](https://observablehq.com/framework/what-is-framework#an-end-to-end-solution)

# [What is Framework?](https://observablehq.com/framework/what-is-framework\#what-is-framework)

Observable Framework — or “Framework” for short — is an open-source static-site generator for data apps. By _data app_ we mean an application that is primarily a display of data. Data apps help you derive insights (to understand) and evaluate potential decisions (to take action).

A data app might be a set of coordinated **interactive visualizations** for “self-service” analysis, perhaps to explore a computational model or to investigate activity;

[![](https://observablehq.com/framework/_file/assets/mosaic.93ba7baf.webp)\\
Taxi rides in New York City](https://observablehq.com/framework/lib/mosaic)

… or it might be a **live dashboard** that places current events in the context of recent or historical trends;

[![](https://observablehq.com/framework/_file/assets/plot-dark.e3955bf0.webp)\\
Observable Plot downloads](https://observablehq.observablehq.cloud/framework-example-plot/)

… or a **point-in-time report** that combines graphics and prose to present in-depth analysis, perhaps with recommendations or hypotheses about observed behavior;

[![](https://observablehq.com/framework/_file/assets/api-dark.4aad268c.webp)\\
Analyzing web logs](https://observablehq.observablehq.cloud/framework-example-api/)

… or any number of other quantitative displays. Data apps are useful in almost every domain: business intelligence, product analytics, monitoring operations, scientific reporting, and more. Data apps are tools for thought — for answering questions, exploring possibilities, organizing knowledge, and communicating insights.

Why use Framework for your data app? Here are a few reasons.

## [The power of code](https://observablehq.com/framework/what-is-framework\#the-power-of-code)

Good data apps are highly customized — they present an opinionated perspective and reflect your brand. Point-and-click tools may be easy to use but suffer from limited expressivity and power. With code, there’s no limit to what you can create. (See our [D3](https://observablehq.com/@d3/gallery) and [Plot](https://observablehq.com/@observablehq/plot-gallery) galleries for inspiration.)

Modern development is a marvel. Framework is free and open-source, and projects are just local files, making it easy to incorporate into your existing workflow. Use your preferred editor, source control, and code review system. Write unit tests. Run linters. Automate builds with continuous integration or deployment. Work offline. Self-host. Generate or revise content programmatically with AI. You can do it all.

## [Polyglot meets the web](https://observablehq.com/framework/what-is-framework\#polyglot-meets-the-web)

Most application frameworks focus on a single language, such as JavaScript, Python, or R. Framework is different. Framework is _polyglot_: it brings multiple languages together. This approach is especially valuable for data apps where data teams have preferred languages for data analysis but want the full power of JavaScript for interactive graphics. Have your cake and eat it too. 🍰

With Framework, editing a Python or R data loader immediately updates the browser preview; no reloading required. Framework’s preview server automatically watches for changes and re-runs the data loader, pushing updates over a socket. And thanks to reactivity, the browser can efficiently incrementally update the display.

Whether your team prefers Python, R, SQL — or even some new language you invented — Framework can give you a best-in-class developer experience and help you build a better data app.

## [Static-site architecture](https://observablehq.com/framework/what-is-framework\#static-site-architecture)

Performance is critical for dashboards: users don’t like to wait, and dashboards only create value if users look at them. Framework’s data architecture practically forces your app to be fast because data is precomputed at build time. Furthermore, data snapshots can be highly-optimized (and aggregated and anonymized), minimizing what you send to the client. And since data loaders run only during build, viewers don’t need direct access to the underlying data sources and your dashboards are more secure and robust.

The speed of modern data warehouses is astonishing. But often time-consuming warehouse changes are needed for analysis — say adding some untapped data source or not-yet-materialized view. Framework’s data loaders let you shortcut this work and quickly produce a performant dashboard. Seeing is believing, and Framework lets you validate ideas faster.

## [Automatic reactivity](https://observablehq.com/framework/what-is-framework\#automatic-reactivity)

Like Observable notebooks, Framework has language-level support for reactivity. Instead of wrangling hooks or signals, you can write declarative code in vanilla JavaScript that automatically re-runs whenever variables change, like a spreadsheet. This helps you build complex, interactive data apps that are easier to understand and maintain.

## [An end-to-end solution](https://observablehq.com/framework/what-is-framework\#an-end-to-end-solution)

Well-designed tools let developers focus on high-value, creative work and build better apps. We’ve imbued Framework with defaults and conveniences that foster a good user experience. And since Framework seamlessly deploys to Observable, you can easily collaborate on data apps and securely share them with your team.

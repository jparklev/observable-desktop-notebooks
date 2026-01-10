---
url: "https://observablehq.com/framework/lib/mermaid"
title: "Mermaid | Observable Framework"
---

# [Mermaid](https://observablehq.com/framework/lib/mermaid\#mermaid)

[Mermaid](https://mermaid.js.org/) is a language for expressing node-link diagrams, flowcharts, sequence diagrams, and many other types of visualizations. (See also [DOT](https://observablehq.com/framework/lib/dot).) Observable provides a `mermaid` tagged template literal for convenience. This is available by default in Markdown, or you can import it like so:

```js
import mermaid from "npm:@observablehq/mermaid";
```

To use in a JavaScript code block:

A

B

C

D

```js
mermaid`graph TD;
    A-->B;
    A-->C;
    B-->D;
    C-->D;`
```

You can also write Mermaid in a `mermaid` fenced code block:

````md
```mermaid
graph TD;
    A-->B;
    A-->C;
    B-->D;
    C-->D;
```
````

This produces:

A

B

C

D

Here are some more examples.

JohnBobAliceJohnBobAliceloop\[Healthcheck\]Rational thoughts prevail!Hello John, how are you?Fight against hypochondriaGreat!How about you?Jolly good!

```mermaid
sequenceDiagram
    participant Alice
    participant Bob
    Alice->>John: Hello John, how are you?
    loop Healthcheck
        John->>John: Fight against hypochondria
    end
    Note right of John: Rational thoughts <br/>prevail!
    John-->>Alice: Great!
    John->>Bob: How about you?
    Bob-->>John: Jolly good!
```

Cool

Where am i?

Cool label

Class01

int chimp

int gorilla

size()

AveryLongClass

Class03

Class04

Class05

Class06

Class07

Object\[\] elementData

equals()

Class08

Class09

C2

C3

```mermaid
classDiagram
Class01 <|-- AveryLongClass : Cool
Class03 *-- Class04
Class05 o-- Class06
Class07 .. Class08
Class09 --> C2 : Where am i?
Class09 --* C3
Class09 --|> Class07
Class07 : equals()
Class07 : Object[] elementData
Class01 : size()
Class01 : int chimp
Class01 : int gorilla
Class08 <--> C2: Cool label
```

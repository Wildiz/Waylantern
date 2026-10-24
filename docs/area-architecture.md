# Software and systems architecture

_Design decisions, system structure, scalability and examples of how applications are built._

5 resources. [Home](../README.md) / [Catalogue](catalogue.md)

## Not sure where to start?

- [First project: software architecture](path-software-architecture.md): Turn a small application's requirements into a design you can explain and revise.
  Before you start: Ability to write and debug a small program, use Git and write a basic automated test.

For a longer learning recipe, [choose a profession curriculum](curricula.md).

The catalogue below is a reference shelf. You do not need to use every resource. [Read the access and level labels](catalogue.md#read-resource-labels).

<details><summary>Explore selected repositories after the first steps</summary>

## Selected repositories

- [500 Lines or Less](https://github.com/aosabook/500lines): Architecture of Open Source Applications book explaining design decisions and tradeoffs through walkthroughs of programs implemented in at most 500 source lines each. (intermediate in this topic; Free)
- [Markdown Architectural Decision Records (MADR)](https://github.com/adr/madr): Markdown templates and guidance for recording the context, considered options, outcome and consequences of an architectural decision, with examples from the project itself. (intermediate in this topic; Free)

</details>

Jump to: [Courses and books](#courses-and-books) | [Lists, docs and articles](#lists-docs-and-articles)

## Courses and books

| Resource | Access | Topic level | What it offers |
|---|---|---|---|
| [500 Lines or Less](https://github.com/aosabook/500lines) · [details](#resource-500-lines-or-less) | Free | intermediate | Architecture of Open Source Applications book explaining design decisions and tradeoffs through walkthroughs of programs implemented in at most 500 source lines each. |
| [System Design (Karan Pratap Singh)](https://github.com/karanpratapsingh/system-design) · [details](#resource-karan-system-design) | Free | intermediate | Written system design course covering networking, databases, architecture patterns, reliability and worked design discussions for services such as a URL shortener. |
| [The System Design Primer](https://github.com/donnemartin/system-design-primer) · [details](#resource-system-design-primer) | Free | intermediate | Open-source guide to designing large-scale systems and preparing for system design interviews. |

<a id="resource-500-lines-or-less"></a>
<details><summary>500 Lines or Less: requirements and source notes</summary>

**Topic level:** intermediate. Read the requirements below before choosing it.

**Languages recorded:** en

**Useful for:**

- Small implementations make architectural choices easier to inspect
- Written material is CC BY 3.0 and example software is MIT licensed
- Chapters connect module boundaries and interfaces to concrete programs

**Requirements, costs and limitations:**

- Requires programming experience to follow the implementations
- A collection of case studies rather than a complete architecture curriculum
- Paid book versions are separate from the freely accessible repository

**Source checked:** 2026-10-24 (github-repo).

Read the official README at https://raw.githubusercontent.com/aosabook/500lines/master/README.md and license description at https://raw.githubusercontent.com/aosabook/500lines/master/LICENSE.md. The README identifies this as the fourth Architecture of Open Source Applications book, describes the 500-source-line chapter format, and notes paid versions. LICENSE.md links CC BY 3.0 for written material and grants MIT terms for example software. Free refers to the accessible repository; paid edition prices were not checked. English README checked. Chapter code, build instructions and recent maintenance were not tested.

**Study format:** self-directed. **Focus-friendly rating:** unknown (editorial judgment).

</details>

<a id="resource-karan-system-design"></a>
<details><summary>System Design (Karan Pratap Singh): requirements and source notes</summary>

**Topic level:** intermediate. Read the requirements below before choosing it.

**Languages recorded:** en

**Useful for:**

- Readable course organized into chapters with a detailed table of contents
- Connects network and storage foundations with architecture patterns
- Includes concrete system design examples

**Requirements, costs and limitations:**

- CC BY-NC-ND 4.0 restricts commercial reuse and distribution of adaptations; this is not an open-source license
- Reading material rather than an interactive implementation lab
- Separate website and ebook editions may have different terms

**Source checked:** 2026-10-24 (github-repo).

Read the author's README course at https://raw.githubusercontent.com/karanpratapsingh/system-design/main/README.md and license at https://raw.githubusercontent.com/karanpratapsingh/system-design/main/LICENSE. The table of contents covers IP, TCP/UDP, DNS, scaling, databases, distributed transactions, architecture patterns, reliability and example systems. The LICENSE is CC BY-NC-ND 4.0, so the material must not be described as open-source software. Free refers only to reading the public repository; website and ebook pricing were not verified. English course checked. Implementation exercises and recent maintenance were not independently tested.

**Study format:** guided. **Focus-friendly rating:** unknown (editorial judgment).

</details>

<a id="resource-system-design-primer"></a>
<details><summary>The System Design Primer: requirements and source notes</summary>

**Topic level:** intermediate. Read the requirements below before choosing it.

**Languages recorded:** en

**Useful for:**

- Popular community reference
- Includes flashcards (Anki)

**Requirements, costs and limitations:**

- Translations incomplete (the Spanish link is an open issue, not a translation)
- Reading only

**Source checked:** 2026-10-21 (github-repo).

Verified from the repo README via raw.githubusercontent.com (github.com was not reachable); not read live on github.com.

**Study format:** self-directed. **Focus-friendly rating:** unknown (editorial judgment).

</details>


## Lists, docs and articles

| Resource | Access | Topic level | What it offers |
|---|---|---|---|
| [arc42 Architecture Documentation Template](https://github.com/arc42/arc42-template) · [details](#resource-arc42-template) | Free | intermediate | Architecture documentation template with explanations for recording requirements, quality goals, system building blocks and interfaces in a consistent structure. |
| [Markdown Architectural Decision Records (MADR)](https://github.com/adr/madr) · [details](#resource-madr) | Free | intermediate | Markdown templates and guidance for recording the context, considered options, outcome and consequences of an architectural decision, with examples from the project itself. |

<a id="resource-arc42-template"></a>
<details><summary>arc42 Architecture Documentation Template: requirements and source notes</summary>

**Topic level:** intermediate. Read the requirements below before choosing it.

**Languages recorded:** en

**Useful for:**

- CC BY-SA 4.0 template and documentation
- Guidance connects architectural views with the information readers need
- Source templates are readable without building a documentation site

**Requirements, costs and limitations:**

- A documentation framework rather than a complete architecture course
- The full template can be more detail than a small project needs
- Generating other output formats uses a separate generator project

**Source checked:** 2026-10-24 (github-repo).

Read https://raw.githubusercontent.com/arc42/arc42-template/master/README.adoc, https://raw.githubusercontent.com/arc42/arc42-template/master/LICENSE.txt, https://raw.githubusercontent.com/arc42/arc42-template/master/EN/adoc/01_introduction_and_goals.adoc and https://raw.githubusercontent.com/arc42/arc42-template/master/EN/adoc/05_building_block_view.adoc. The English sections explain stakeholders, quality goals, module decomposition and interfaces. LICENSE.txt states CC BY-SA 4.0 for the template and documentation, and clarifies that users' own architecture content is not automatically placed under that license. Free refers to the accessible templates. Only English content was checked, although the README lists translations. Generator output and recent maintenance were not independently tested.

**Study format:** self-directed. **Focus-friendly rating:** unknown (editorial judgment).

</details>

<a id="resource-madr"></a>
<details><summary>Markdown Architectural Decision Records (MADR): requirements and source notes</summary>

**Topic level:** intermediate. Read the requirements below before choosing it.

**Languages recorded:** en

**Useful for:**

- Templates can be read and adapted without running a service
- Minimal and full versions help choose an appropriate level of detail
- The project declares MIT OR CC0-1.0 licensing

**Requirements, costs and limitations:**

- Helps document decisions rather than teaching every architecture concept
- Useful records still require a real problem and justified tradeoffs

**Source checked:** 2026-10-24 (github-repo).

Read https://raw.githubusercontent.com/adr/madr/main/README.md, https://raw.githubusercontent.com/adr/madr/main/LICENSE, https://raw.githubusercontent.com/adr/madr/main/template/adr-template-minimal.md and https://raw.githubusercontent.com/adr/madr/main/docs/decisions/0000-use-markdown-architectural-decision-records.md. The minimal template covers context, options, decision outcome and consequences; the project's own decision explains its choice of MADR. LICENSE declares MIT OR CC0-1.0. Free refers to the repository material; no hosted service is needed to use the templates. English files checked. Local documentation builds and recent maintenance were not independently tested.

**Study format:** self-directed. **Focus-friendly rating:** unknown (editorial judgment).

</details>

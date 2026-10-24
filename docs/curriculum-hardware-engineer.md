# Editorial practice plan: Hardware Engineer

Explore digital circuit design while exposing missing electronics and laboratory coverage.

[Home](../README.md) / [Curricula](curricula.md) / [Software, interfaces and embedded systems](professions-software.md#roles-in-this-group)

[Academic-plan work and resource-matching preview](software-study-preview.md). This page is an existing editorial practice plan; it is not derived from an inspected university curriculum.

**Target profile:** [Hardware Engineer](professions-software.md#hardware-engineer)

**Starting point:** Learn the stated foundations first

**Type:** Waylantern editorial learning recipe. Related official sources are listed separately below.

## Before you start

- Basic algebra
- Binary notation
- Introductory physics

**What you will produce:** A simulated digital circuit with test vectors and a separate physical-verification plan.

**Resource coverage:** 2 of 4 stages have no recorded resource gap. Read the marked gaps before planning your study.

Resource access labels refer to the material or software. Open a resource's details to check prerequisites, hardware, APIs and other running costs before using it.

## Your sequence

1. [Relate electrical quantities](#stage-1)
2. [Build combinational logic](#stage-2)
3. [Identify physical constraints](#stage-3)
4. [Deliver the digital design study](#stage-4)

<a id="stage-1"></a>
## 1. Relate electrical quantities

**Learn:**

- Voltage and current
- Power and units
- Measurement uncertainty

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [Khan Academy Math (linear algebra, statistics, calculus)](https://www.khanacademy.org/math) — beginner in this topic; free access. [Details](area-data.md#resource-khan-academy-math).

**Resource still needed:** The mathematics resource supports calculations but no dedicated verified introductory circuit-analysis course is present.

**Practise:** Calculate units and hypothetical low-voltage power and state every electrical assumption.

**Advance when:** Check dimensions and identify properties that still require a circuit model.

After the checkpoint, [continue to stage 2](#stage-2).

<a id="stage-2"></a>
## 2. Build combinational logic

**Learn:**

- Boolean functions
- Truth tables
- Logic composition

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [From Nand to Tetris](https://www.nand2tetris.org/) — all in this topic; free access. [Details](area-cs.md#resource-nand2tetris).

**Practise:** Construct a small arithmetic or selection circuit in the course hardware simulator.

**Advance when:** Pass supplied tests and explain each row of a small truth table.

After the checkpoint, [continue to stage 3](#stage-3).

<a id="stage-3"></a>
## 3. Identify physical constraints

**Learn:**

- Timing margins
- Signal levels
- Thermal limits

**Resource still needed:** No verified datasheet-reading, signal-integrity or laboratory-measurement curriculum is available; do not build hardware from this checklist alone.

**Practise:** List component ratings and measurements needed for a hypothetical physical implementation.

**Advance when:** Distinguish logical correctness from timing, voltage and thermal claims a logic simulator cannot prove.

After the checkpoint, [continue to stage 4](#stage-4).

<a id="stage-4"></a>
## 4. Deliver the digital design study

**Learn:**

- Test vectors
- Design alternatives
- Verification boundaries

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [From Nand to Tetris](https://www.nand2tetris.org/) — all in this topic; free access. [Details](area-cs.md#resource-nand2tetris).

**Practise:** Compare two implementations of a logic function and supply simulations plus a proposed physical-test plan.

**Advance when:** Both implementations pass the same logic tests while electrical compatibility remains explicitly unverified.

## After this recipe

Seek a structured electronics curriculum and supervised laboratory practice; microcontroller tutorials do not replace circuit, PCB or hardware qualification training.

## Related guidance

These references cover related disciplines or skills; their status describes the source inspection, not an endorsement of this recipe.

- [ACM Computing Curricula Recommendations](profession-references.md#reference-acm-curricula)

[Back to roles in this group](professions-software.md#roles-in-this-group) · [Find a specific resource](catalogue.md)

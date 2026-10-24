# Learning curriculum: Video Game Tester

Investigate a permitted game build and produce reproducible testing evidence.

[Home](../README.md) / [Curricula](curricula.md) / [Software, interfaces and embedded systems](professions-software.md#roles-in-this-group)

**Target profile:** [Video Game Tester](professions-software.md#video-game-tester)

**Starting point:** Start with the basics

**Type:** Waylantern editorial learning recipe. Related official sources are listed separately below.

## Before you start

- Ability to run a permitted game build
- Basic file and screenshot skills

**What you will produce:** A game test pack with boundary cases, defect reports and retest results.

**Resource coverage:** 2 of 4 stages have no recorded resource gap. Read the marked gaps before planning your study.

Resource access labels refer to the material or software. Open a resource's details to check prerequisites, hardware, APIs and other running costs before using it.

## Your sequence

1. [Describe intended play](#stage-1)
2. [Design focused game cases](#stage-2)
3. [Report reproducible defects](#stage-3)
4. [Deliver the game test cycle](#stage-4)

<a id="stage-1"></a>
## 1. Describe intended play

**Learn:**

- Game states
- Controls and outcomes
- Test scope

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [Godot Engine Documentation](https://docs.godotengine.org/en/stable/) — beginner in this topic; free access. [Details](area-games-mobile.md#resource-godot-docs).

**Practise:** Use a tutorial game to list start, play, pause, finish and restart states.

**Advance when:** State the expected outcome of a transition between each neighboring state.

After the checkpoint, [continue to stage 2](#stage-2).

<a id="stage-2"></a>
## 2. Design focused game cases

**Learn:**

- Input sequences
- Collision boundaries
- Save and restart

**Resource still needed:** No dedicated game-testing curriculum is verified; controller matrices and platform requirements need specialist material.

**Practise:** Create cases for repeated input, edge collisions and restart after winning.

**Advance when:** Each case identifies initial state, action and an observable expected result.

After the checkpoint, [continue to stage 3](#stage-3).

<a id="stage-3"></a>
## 3. Report reproducible defects

**Learn:**

- Build identification
- Reproduction steps
- Expected versus actual

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [Open Source Guides](https://opensource.guide/) — beginner in this topic; free access. [Details](area-software.md#resource-open-source-guides).

**Practise:** Report one permitted-prototype defect using a minimal input sequence and sanitized evidence.

**Advance when:** Another person reproduces it on the same identified build.

After the checkpoint, [continue to stage 4](#stage-4).

<a id="stage-4"></a>
## 4. Deliver the game test cycle

**Learn:**

- Regression selection
- Retest evidence
- Untested platforms

**Resource still needed:** A verified game-QA reporting and platform-coverage source is absent; this exercise does not validate platform compliance.

**Practise:** Execute the matrix on two prototype revisions and record fixed, remaining and untested cases.

**Advance when:** Trace every claimed fix to a retest and distinguish untested devices from passing devices.

## After this recipe

Study platform-specific requirements on authorized builds and never claim compatibility for untested devices.

## Related guidance

These references cover related disciplines or skills; their status describes the source inspection, not an endorsement of this recipe.

- [Software Engineering Body of Knowledge](profession-references.md#reference-swebok)
- [Skills Framework for the Information Age](profession-references.md#reference-sfia)

[Back to roles in this group](professions-software.md#roles-in-this-group) · [Find a specific resource](catalogue.md)

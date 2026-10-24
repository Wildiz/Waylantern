# Learning curriculum: Game Developer

Build a complete small playable loop before increasing game scope.

[Home](../README.md) / [Curricula](curricula.md) / [Software, interfaces and embedded systems](professions-software.md#roles-in-this-group)

**Target profile:** [Game Developer](professions-software.md#game-developer)

**Starting point:** Start with the basics

**Type:** Waylantern editorial learning recipe. Related official sources are listed separately below.

## Before you start

- Basic file skills
- A computer suitable for the chosen game editor

**What you will produce:** A two-dimensional collect-and-finish game with restart behavior and a checkable win condition.

**Resource coverage:** 4 of 4 stages have no recorded resource gap. Read the marked gaps before planning your study.

Resource access labels refer to the material or software. Open a resource's details to check prerequisites, hardware, APIs and other running costs before using it.

## Your sequence

1. [Control a game object](#stage-1)
2. [Implement the play loop](#stage-2)
3. [Handle replay and timing](#stage-3)
4. [Deliver the playable mini-game](#stage-4)

<a id="stage-1"></a>
## 1. Control a game object

**Learn:**

- Scenes and objects
- Input events
- Movement

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [Godot Engine Documentation](https://docs.godotengine.org/en/stable/) — beginner in this topic; free access. [Details](area-games-mobile.md#resource-godot-docs).

**Practise:** Follow a first-game introduction and move a player within a bounded scene.

**Advance when:** Show input-driven movement without leaving the intended play area.

After the checkpoint, [continue to stage 2](#stage-2).

<a id="stage-2"></a>
## 2. Implement the play loop

**Learn:**

- Collision events
- Score state
- Win conditions

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [Godot Engine Documentation](https://docs.godotengine.org/en/stable/) — beginner in this topic; free access. [Details](area-games-mobile.md#resource-godot-docs).

**Practise:** Add three collectibles and a visible finish condition.

**Advance when:** Each collectible changes score once and the target score ends the round.

After the checkpoint, [continue to stage 3](#stage-3).

<a id="stage-3"></a>
## 3. Handle replay and timing

**Learn:**

- Restart state
- Frame-independent movement
- Pause

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [Godot Engine Documentation](https://docs.godotengine.org/en/stable/) — beginner in this topic; free access. [Details](area-games-mobile.md#resource-godot-docs).

**Practise:** Add restart and pause and clear leftover objects between rounds.

**Advance when:** Replay two rounds with consistent movement and scoring.

After the checkpoint, [continue to stage 4](#stage-4).

<a id="stage-4"></a>
## 4. Deliver the playable mini-game

**Learn:**

- Build instructions
- Playtest notes
- Known defects

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [Godot Engine Documentation](https://docs.godotengine.org/en/stable/) — beginner in this topic; free access. [Details](area-games-mobile.md#resource-godot-docs).

**Practise:** Deliver controls, a scripted test run and one revision based on an observed player difficulty.

**Advance when:** A new player can start, finish and restart from the instructions.

## After this recipe

Learn asset pipelines and performance through small additions; one prototype does not establish a complete commercial production pipeline.

## Related guidance

These references cover related disciplines or skills; their status describes the source inspection, not an endorsement of this recipe.

- [CS2023 — Computer Science Curricula](profession-references.md#reference-cs2023)
- [Skills Framework for the Information Age](profession-references.md#reference-sfia)

[Back to roles in this group](professions-software.md#roles-in-this-group) · [Find a specific resource](catalogue.md)

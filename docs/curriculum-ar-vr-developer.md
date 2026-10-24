# Learning curriculum: AR/VR Developer

Prototype spatial interaction with explicit tracking and comfort limitations.

[Home](../README.md) / [Curricula](curricula.md) / [Software, interfaces and embedded systems](professions-software.md#roles-in-this-group)

**Target profile:** [AR/VR Developer](professions-software.md#ar-vr-developer)

**Starting point:** Learn the stated foundations first

**Type:** Waylantern editorial learning recipe. Related official sources are listed separately below.

## Before you start

- Basic programming
- Vectors and coordinate systems
- A computer suitable for a 3D editor

**What you will produce:** A simulated object-placement interaction with defined device-validation gaps.

**Resource coverage:** 2 of 4 stages have no recorded resource gap. Read the marked gaps before planning your study.

Resource access labels refer to the material or software. Open a resource's details to check prerequisites, hardware, APIs and other running costs before using it.

## Your sequence

1. [Build a scene at known scale](#stage-1)
2. [Model tracked interaction](#stage-2)
3. [Design spatial feedback](#stage-3)
4. [Deliver the spatial mini-project](#stage-4)

<a id="stage-1"></a>
## 1. Build a scene at known scale

**Learn:**

- Coordinate frames
- Transforms
- Camera and object scale

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [Unity Learn](https://learn.unity.com/) — beginner in this topic; free access. [Details](area-games-mobile.md#resource-unity-learn).
- [3Blue1Brown: Essence of Linear Algebra](https://www.3blue1brown.com/topics/linear-algebra) — beginner in this topic; free access. [Details](area-math.md#resource-3blue1brown-linear-algebra).

**Practise:** Create three labelled objects and inspect translation and rotation in a small scene.

**Advance when:** Explain local versus world coordinates and reproduce a known arrangement.

After the checkpoint, [continue to stage 2](#stage-2).

<a id="stage-2"></a>
## 2. Model tracked interaction

**Learn:**

- Tracking origin
- Selection and manipulation
- Input abstraction

**Resource still needed:** Device-specific XR interaction and tracking guidance is not verified; general Unity learning does not validate the chosen XR runtime.

**Practise:** Specify a hand or controller interaction and implement an equivalent simulator input.

**Advance when:** Demonstrate select, release and a loss-of-tracking fallback.

After the checkpoint, [continue to stage 3](#stage-3).

<a id="stage-3"></a>
## 3. Design spatial feedback

**Learn:**

- Interaction affordances
- Comfort constraints
- Fallback behavior

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [Penpot](https://github.com/penpot/penpot) — beginner in this topic; freemium access. [Details](area-design-product.md#resource-penpot).
- [Unity Learn](https://learn.unity.com/) — beginner in this topic; free access. [Details](area-games-mobile.md#resource-unity-learn).

**Resource still needed:** Dedicated XR comfort, accessibility and calibration guidance remains unverified and must be checked before headset testing.

**Practise:** Prototype selection and cancellation feedback with a static alternative to scene movement.

**Advance when:** A reviewer can identify selection and cancel without unexplained movement.

After the checkpoint, [continue to stage 4](#stage-4).

<a id="stage-4"></a>
## 4. Deliver the spatial mini-project

**Learn:**

- Frame-time observations
- Interaction tests
- Device boundaries

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [Unity Learn](https://learn.unity.com/) — beginner in this topic; free access. [Details](area-games-mobile.md#resource-unity-learn).

**Practise:** Deliver a three-object placement prototype with a scripted checklist and performance observations.

**Advance when:** Reproduce select, place and cancel while labelling headset and tracking claims untested unless measured.

## After this recipe

Verify runtime-specific XR documentation before headset deployment; a simulator does not prove comfort or tracking accuracy.

## Related guidance

These references cover related disciplines or skills; their status describes the source inspection, not an endorsement of this recipe.

- [Computer Science curriculum recommendations project](profession-references.md#reference-cs2023)
- [Skills Framework for the Information Age](profession-references.md#reference-sfia)

[Back to roles in this group](professions-software.md#roles-in-this-group) · [Find a specific resource](catalogue.md)

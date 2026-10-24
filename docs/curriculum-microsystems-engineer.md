# Learning curriculum: Microsystems Engineer

Examine a simplified microsensor model without implying fabrication training.

[Home](../README.md) / [Curricula](curricula.md) / [Software, interfaces and embedded systems](professions-software.md#roles-in-this-group)

**Target profile:** [Microsystems Engineer](professions-software.md#microsystems-engineer)

**Starting point:** Prior practical experience required

**Type:** Waylantern editorial learning recipe. Related official sources are listed separately below.

## Before you start

- Electronics and physics foundations
- Calculus and linear algebra
- Numerical programming

**What you will produce:** A computational microsensor study with sensitivity analysis and calibration assumptions.

**Resource coverage:** 2 of 4 stages have no recorded resource gap. Read the marked gaps before planning your study.

Resource access labels refer to the material or software. Open a resource's details to check prerequisites, hardware, APIs and other running costs before using it.

## Your sequence

1. [Frame a microsystem model](#stage-1)
2. [Analyze sensitivity](#stage-2)
3. [Plan measurement evidence](#stage-3)
4. [Deliver the microsensor study](#stage-4)

<a id="stage-1"></a>
## 1. Frame a microsystem model

**Learn:**

- Transduction principle
- Dimensions and scaling
- Operating assumptions

**Resource still needed:** No MEMS, microfabrication or microsensor course is verified; a specialist source must support the selected physical relationship.

**Practise:** Specify a hypothetical microsensor, measured quantity and simplified physical relationship.

**Advance when:** Check units and explicitly exclude physical effects outside the model.

After the checkpoint, [continue to stage 2](#stage-2).

<a id="stage-2"></a>
## 2. Analyze sensitivity

**Learn:**

- Symbolic relationships
- Parameter derivatives
- Numerical sweeps

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [SymPy](https://github.com/sympy/sympy) — intermediate in this topic; free access. [Details](area-math.md#resource-sympy).
- [3Blue1Brown: Essence of Calculus](https://www.3blue1brown.com/topics/calculus) — beginner in this topic; free access. [Details](area-math.md#resource-3blue1brown-calculus).

**Practise:** Vary two model parameters and plot the predicted output.

**Advance when:** Compare a numerical output change with the derivative of the same relationship.

After the checkpoint, [continue to stage 3](#stage-3).

<a id="stage-3"></a>
## 3. Plan measurement evidence

**Learn:**

- Calibration error
- Repeatability
- Process variation

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [OpenIntro Statistics](https://www.openintro.org/book/os/) — beginner in this topic; free access. [Details](area-data.md#resource-openintro-statistics).

**Resource still needed:** The statistics material does not cover cleanroom processes or device metrology; these specialist sources remain unverified.

**Practise:** Generate synthetic calibration observations and estimate residual error.

**Advance when:** Distinguish measurement variation from model error and label every observation as synthetic.

After the checkpoint, [continue to stage 4](#stage-4).

<a id="stage-4"></a>
## 4. Deliver the microsensor study

**Learn:**

- Reproducibility
- Sensitivity limits
- Validation plan

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [SymPy](https://github.com/sympy/sympy) — intermediate in this topic; free access. [Details](area-math.md#resource-sympy).
- [The Python Tutorial (official)](https://docs.python.org/3/tutorial/) — beginner in this topic; free access. [Details](area-software.md#resource-python-tutorial).

**Practise:** Deliver the model, synthetic calibration analysis and proposed laboratory-validation plan.

**Advance when:** Another reader reproduces the parameter sweep and identifies every claim requiring a physical measurement.

## After this recipe

Obtain specialist microfabrication and metrology instruction in a supervised facility; a numerical study is not a validated device.

## Related guidance

These references cover related disciplines or skills; their status describes the source inspection, not an endorsement of this recipe.

- [ACM Computing Curricula Recommendations](profession-references.md#reference-acm-curricula)

[Back to roles in this group](professions-software.md#roles-in-this-group) · [Find a specific resource](catalogue.md)

# Learning curriculum: Robotics Engineer

Model sensing and motion before operating a physical robot.

[Home](../README.md) / [Curricula](curricula.md) / [Software, interfaces and embedded systems](professions-software.md#roles-in-this-group)

**Target profile:** [Robotics Engineer](professions-software.md#robotics-engineer)

**Starting point:** Learn the stated foundations first

**Type:** Waylantern editorial learning recipe. Related official sources are listed separately below.

## Before you start

- Python functions
- Algebra and trigonometry
- Ability to plot numerical results

**What you will produce:** A simulated two-dimensional controller with measured tracking error and explicit physical-validation gaps.

**Resource coverage:** 3 of 4 stages have no recorded resource gap. Read the marked gaps before planning your study.

Resource access labels refer to the material or software. Open a resource's details to check prerequisites, hardware, APIs and other running costs before using it.

## Your sequence

1. [Represent position and motion](#stage-1)
2. [Close a feedback loop](#stage-2)
3. [Map sensing to interfaces](#stage-3)
4. [Deliver the robot simulation](#stage-4)

<a id="stage-1"></a>
## 1. Represent position and motion

**Learn:**

- Vectors and frames
- Discrete time
- Pose updates

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [3Blue1Brown: Essence of Linear Algebra](https://www.3blue1brown.com/topics/linear-algebra) — beginner in this topic; free access. [Details](area-math.md#resource-3blue1brown-linear-algebra).
- [The Python Tutorial (official)](https://docs.python.org/3/tutorial/) — beginner in this topic; free access. [Details](area-software.md#resource-python-tutorial).

**Practise:** Implement two-dimensional robot motion and plot its trajectory.

**Advance when:** Check a straight move and a turn against hand-calculated positions.

After the checkpoint, [continue to stage 2](#stage-2).

<a id="stage-2"></a>
## 2. Close a feedback loop

**Learn:**

- Setpoints and error
- Proportional control
- Actuator limits

**Resource still needed:** No dedicated robotics or control-theory curriculum is verified; stability and tuning require a suitable specialist source.

**Practise:** Simulate steering with bounded output and a noisy position measurement.

**Advance when:** Plot error over time and demonstrate a case with oscillation or saturation.

After the checkpoint, [continue to stage 3](#stage-3).

<a id="stage-3"></a>
## 3. Map sensing to interfaces

**Learn:**

- Sampling intervals
- Actuator commands
- Missing measurements

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [Microsoft IoT for Beginners](https://github.com/microsoft/IoT-For-Beginners) — beginner in this topic; free access. [Details](area-embedded.md#resource-microsoft-iot-for-beginners).

**Practise:** Map simulated measurements and commands to a device interface without connecting moving hardware.

**Advance when:** Explain sampling delay and define the response to an absent reading.

After the checkpoint, [continue to stage 4](#stage-4).

<a id="stage-4"></a>
## 4. Deliver the robot simulation

**Learn:**

- Trajectory tests
- Noise experiments
- Reproducible parameters

**Study resources** — consult the sections needed for this task; the resources may teach complementary skills:

- [The Python Tutorial (official)](https://docs.python.org/3/tutorial/) — beginner in this topic; free access. [Details](area-software.md#resource-python-tutorial).
- [pytest - Get Started](https://github.com/pytest-dev/pytest/blob/main/doc/en/getting-started.rst) — beginner in this topic; free access. [Details](area-testing.md#resource-pytest-getting-started).

**Practise:** Package a waypoint-following simulation with parameter settings and fixed failure cases.

**Advance when:** Reproduce straight and turning paths, compare tracking error and show the missing-sensor response.

## After this recipe

Use supervised robotics instruction for dynamics, localization and physical safety before operating moving mechanisms.

## Related guidance

These references cover related disciplines or skills; their status describes the source inspection, not an endorsement of this recipe.

- [ACM Computing Curricula Recommendations](profession-references.md#reference-acm-curricula)
- [Computer Science curriculum recommendations project](profession-references.md#reference-cs2023)

[Back to roles in this group](professions-software.md#roles-in-this-group) · [Find a specific resource](catalogue.md)

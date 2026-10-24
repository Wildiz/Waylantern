# Block 1 — Connecting academic requirements to the existing resources

## The relationship

**Published academic plan → required course or knowledge unit → selected learning resources → relevant specialisation and profession.**

The catalogue currently contains 325 resource records: courses, books, reference collections, repositories, applications and communities. They form the resource library for the plan. A repository is a container for material or code, not an academic requirement by itself.

Use one record per resource and refer to its existing slug from the requirements it helps teach. A resource may support several requirements without being duplicated. Resources belonging to other profession groups remain available for those later blocks.

## An initial correlation we can review now

The academic reference currently inspected is [CS2023's knowledge-area framework](https://csed.acm.org/knowledge-areas/). The rows below are **editorial topic-level correlations**, supported by the descriptions and inspection notes already recorded in our catalogue. They are not verified course equivalences, complete coverage of the knowledge areas, credit recognition or an institution-issued course order.

Once we can read the actual US and Chinese university programme plans, the left side must use their exact requirements, cohort and prerequisites. A knowledge area must not be renamed as a university course without that evidence.

| Academic area inspected in CS2023 | Existing study material | Function in the plan | Coverage still to check |
|---|---|---|---|
| Software Development Fundamentals (SDF) | [CS50 Python](https://cs50.harvard.edu/python/) and [Exercism](https://exercism.org/) | A taught introduction plus practice; the stored IDs are `cs50-python` and `exercism`. | Compare individual learning outcomes and assignments with the selected programme. Python instruction alone does not cover the whole degree foundation. |
| Algorithmic Foundations (AL) | [MIT 6.006](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/) and [The Algorithms — Python](https://github.com/TheAlgorithms/Python) | A course with problem sets and exams, supported by implementations to inspect; IDs `mit-6006-introduction-to-algorithms` and `the-algorithms-python`. | Check the mathematical prerequisites, algorithms and assessment against the specific requirement. Reading implementations is not a substitute for algorithm analysis. |
| Mathematical and Statistical Foundations (MSF) | [Discrete Mathematics: An Open Introduction](https://discrete.openmathbooks.org/dmoi4.html) | A textbook and selected exercises; ID `discrete-mathematics-open-introduction`. | This selection addresses discrete mathematics. It does not establish coverage of the area's calculus, linear algebra or statistics requirements. |
| Architecture and Organization (AR) / Systems Fundamentals (SF) | [From Nand to Tetris](https://www.nand2tetris.org/) | A project-based bridge between digital logic and software; ID `nand2tetris`. | Match projects and learning outcomes to the programme. It does not replace all electronic engineering, physical hardware or laboratory requirements. |
| Software Engineering (SE) | [Pro Git](https://git-scm.com/book/en/v2), [pytest introduction](https://github.com/pytest-dev/pytest/blob/main/doc/en/getting-started.rst) and [500 Lines or Less](https://github.com/aosabook/500lines) | Supporting references and practice in version control, tests and small-system design; IDs `pro-git`, `pytest-getting-started`, `500-lines-or-less`. | These selections are partial. Requirements engineering, lifecycle, maintenance and other required outcomes still need a programme-level comparison. |
| Human-Computer Interaction (HCI) | [Penpot](https://github.com/penpot/penpot) and [GOV.UK Design System](https://github.com/alphagov/govuk-design-system) | A prototyping tool and examples of interface patterns; IDs `penpot` and `govuk-design-system`. | They are not a complete HCI curriculum. Select verified teaching material for user research, evaluation and the programme's other HCI outcomes. |
| Specialized Platform Development (SPD) | [MDN Web Docs](https://developer.mozilla.org/) and [Arduino Blink](https://github.com/arduino/docs-content/blob/main/content/built-in-examples/01.basics/Blink/Blink.md) | References and starter practice for two different platform specialisations; IDs `mdn-web-docs` and `arduino-built-in-examples`. | Web and embedded study are separate choices. Mobile needs its own selection. Neither starter represents full platform mastery or the whole SPD area. |
| Graphics and Interactive Techniques (GIT) | [raylib Introduction Course](https://github.com/raysan5/raylib-intro-course) | An applied game-programming project; ID `raylib-introduction-course`. | Requires C. The stored source notes mention raylib 4.2 and untested current compatibility. It does not cover a complete graphics curriculum or a game-design degree. |

Only a subset of CS2023's seventeen knowledge areas is correlated here. Databases, operating systems, networks, security, ethics and the remaining areas must also be assessed when matching a complete Computer Science programme. This table is a pilot for the first profession group, not a claim that the curriculum is already complete.

## What an accepted mapping record needs

For a real programme requirement, record:

- The institution, degree, catalogue year and exact course or requirement identifier.
- The source URL and the requirement's prerequisites and learning outcomes.
- The existing resource slug and the specific lesson, chapter or exercise that covers an outcome.
- Its function: primary teaching, supporting explanation, practice/assessment, or a tool.
- Coverage: outcome checked, partial support, or a resource gap. A matching title alone is insufficient.
- Accounts, hardware, running costs, language and prior knowledge needed to use it.

Keep three evidence questions separate: **did we read the academic requirement, did we inspect the learning material, and did we compare their outcomes?** Verification of one does not establish the others.

## How a reader would use it

For a backend specialisation, the reader would see the selected academic base, its actual foundational requirements, and the resources correlated to each requirement. The specialisation would then add the verified database, networking and service-development requirements rather than repeat the common foundation.

For UX, a prototyping tool would appear under practice. The actual HCI or design teaching would come from a documented programme and its outcomes. For embedded systems, the relevant computing and physical engineering preparation would be explicit before using a small board example.

The same approach can reuse resources across profiles while preserving differences between disciplines. It does not require inventing 31 degrees or forcing all 325 resources into this block.

[Review Block 1's academic sources and proposed families](2026-10-25-block-1-academic-bases.md) · [Explore the existing catalogue](../docs/catalogue.md)

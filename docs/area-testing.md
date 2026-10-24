# Software testing and QA

_Automated tests, browser testing and techniques for checking software quality._

5 resources. [Home](../README.md) / [Catalogue](catalogue.md)

## Not sure where to start?

- [First project: software testing and QA](path-software-testing.md): Learn to describe expected behavior, automate checks and investigate failures in one small project.
  Before you start: Basic programming and terminal skills; the Playwright option also needs JavaScript or TypeScript and basic HTML.

For a longer learning recipe, [choose a profession curriculum](curricula.md).

The catalogue below is a reference shelf. You do not need to use every resource. [Read the access and level labels](catalogue.md#read-resource-labels).

<details><summary>Explore selected repositories after the first steps</summary>

## Selected repositories

- [pytest - Get Started](https://github.com/pytest-dev/pytest): Official introductory guide to installing pytest, writing a first Python test and interpreting assertion failures before progressing to multiple tests. (beginner in this topic; Free)
- [Cypress Real World App](https://github.com/cypress-io/cypress-realworld-app): Educational full-stack payment demo with example data and Cypress tests for practising application testing patterns, authentication flows and test setup. (intermediate in this topic; Free)

</details>

Jump to: [Practice by doing](#practice-by-doing) | [Lists, docs and articles](#lists-docs-and-articles)

## Practice by doing

| Resource | Access | Topic level | What it offers |
|---|---|---|---|
| [Cypress Real World App](https://github.com/cypress-io/cypress-realworld-app) · [details](#resource-cypress-real-world-app) | Free | intermediate | Educational full-stack payment demo with example data and Cypress tests for practising application testing patterns, authentication flows and test setup. |

<a id="resource-cypress-real-world-app"></a>
<details><summary>Cypress Real World App: requirements and source notes</summary>

**Topic level:** intermediate. Read the requirements below before choosing it.

**Languages recorded:** en

**Useful for:**

- MIT-licensed demonstration application with tests to inspect and modify
- Includes seeded local data rather than requiring a separate database service
- Authentication test source demonstrates sign-up, login, redirects and session checks

**Requirements, costs and limitations:**

- Requires web development knowledge, the repository's Node.js version and Yarn Classic
- Maintainers explicitly describe it as educational rather than a production payment system
- Optional Cypress Cloud and other external services have terms and costs not verified here

**Source checked:** 2026-10-24 (github-repo).

Read cypress-io/cypress-realworld-app develop README.md, LICENSE and cypress/tests/ui/auth.spec.ts via raw.githubusercontent.com. README explicitly invites learning, experimentation and testing practice, describes Express/React with a local JSON database, bundled sample data, Node.js pinned in .node-version and Yarn Classic requirements. Authentication tests show database seeding and concrete user flows. LICENSE is MIT. Free refers to repository code and local practice, not external hosted testing services. Only English checked; dependency installation, tests, service pricing and current maintenance activity were not verified.

**Study format:** self-directed. **Focus-friendly rating:** unknown (editorial judgment).

</details>


## Lists, docs and articles

| Resource | Access | Topic level | What it offers |
|---|---|---|---|
| [FuzzTest - CMake Quickstart](https://github.com/google/fuzztest/blob/main/doc/quickstart-cmake.md) · [details](#resource-fuzztest-cmake-quickstart) | Free | advanced | Official C++ tutorial introducing property-based fuzz testing with a small CMake project, a property test and separate unit-test and coverage-guided fuzzing modes. |
| [Playwright - Getting Started](https://github.com/microsoft/playwright) · [details](#resource-playwright-getting-started) | Free | intermediate | Official Playwright introduction with installation commands and sample end-to-end web tests using browser automation, locators and assertions. |
| [pytest - Get Started](https://github.com/pytest-dev/pytest/blob/main/doc/en/getting-started.rst) · [details](#resource-pytest-getting-started) | Free | beginner | Official introductory guide to installing pytest, writing a first Python test and interpreting assertion failures before progressing to multiple tests. |
| [React Testing Library - Examples](https://github.com/testing-library/react-testing-library#examples) · [details](#resource-react-testing-library-examples) | Free | intermediate | Official React component testing examples that query rendered elements and simulate user interactions instead of relying on component implementation details. |

<a id="resource-fuzztest-cmake-quickstart"></a>
<details><summary>FuzzTest - CMake Quickstart: requirements and source notes</summary>

**Topic level:** advanced. Read the requirements below before choosing it.

**Languages recorded:** en

**Useful for:**

- Contrasts a specific unit test with a property evaluated across generated inputs
- Includes CMake configuration and commands for building and running a sample
- Framework is Apache-2.0 licensed with additional third-party notices

**Requirements, costs and limitations:**

- Requires C++ and build-system familiarity
- The verified quickstart requires Linux, Clang and CMake; it does not claim general GCC support
- Fuzzing mode can run indefinitely unless stopped or given a time limit

**Source checked:** 2026-10-24 (github-repo).

Read google/fuzztest main README.md, LICENSE, doc/quickstart-cmake.md and doc/overview.md via raw.githubusercontent.com. The quickstart provides IntegerAdditionCommutes with FUZZ_TEST, C++17 CMake configuration, Linux/Clang/CMake prerequisites, and unit versus fuzzing execution modes. Overview demonstrates input domains with a string-parsing property. LICENSE applies Apache-2.0 generally and lists Lucent and BSD notices for particular files. The README's separate doc/tutorial.md codelab link returned 404, so this entry links the verified CMake quickstart instead. Free refers to source and tutorial; external compute is not included. English checked; no code compiled or executed and current maintenance activity was not verified.

**Study format:** guided. **Focus-friendly rating:** unknown (editorial judgment).

</details>

<a id="resource-playwright-getting-started"></a>
<details><summary>Playwright - Getting Started: requirements and source notes</summary>

**Topic level:** intermediate. Read the requirements below before choosing it.

**Languages recorded:** en

**Useful for:**

- Open-source framework under Apache-2.0
- README includes a small test and commands to run it
- Supports Chromium, Firefox and WebKit through one API

**Requirements, costs and limitations:**

- Assumes basic web development and JavaScript or TypeScript knowledge
- Running the examples requires Node.js and browser installation
- External CI or hosted testing services can have separate costs

**Source checked:** 2026-10-24 (github-repo).

Read microsoft/playwright main README.md and LICENSE via raw.githubusercontent.com. README documents installation, an end-to-end test, browser isolation, locators, auto-waiting and Chromium, Firefox and WebKit support; LICENSE is Apache-2.0. The README links playwright.dev documentation, but the hosted introduction returned a proxy access denial, so claims here rely on the repository source. Free refers to the documentation and open-source framework, not external infrastructure. English checked; not installed or executed.

**Study format:** semi. **Focus-friendly rating:** unknown (editorial judgment).

</details>

<a id="resource-pytest-getting-started"></a>
<details><summary>pytest - Get Started: requirements and source notes</summary>

**Before you start:** Basic Python and command-line use.

**Topic level:** beginner. Read the requirements below before choosing it.

**Languages recorded:** en

**Useful for:**

- Framework and accompanying documentation use the MIT license
- Starts with a small test and explains its deliberate failure
- Shows how ordinary Python assertions produce useful failure reports

**Requirements, costs and limitations:**

- Assumes basic Python knowledge and command-line use
- Requires installing Python and pytest to run examples
- Introduces a testing tool rather than a complete software testing curriculum

**Source checked:** 2026-10-24 (github-repo).

Read pytest-dev/pytest main README.rst, LICENSE and doc/en/getting-started.rst via raw.githubusercontent.com. The guide shows installation, version checking, a first intentionally failing test, failure interpretation and running multiple tests. LICENSE explicitly covers the software and associated documentation under MIT. Hosted docs.pytest.org access returned a proxy denial, so this entry links the verified repository source. Free refers to the guide and local framework. English checked; no tests from the guide were executed.

**Study format:** guided. **Focus-friendly rating:** unknown (editorial judgment).

</details>

<a id="resource-react-testing-library-examples"></a>
<details><summary>React Testing Library - Examples: requirements and source notes</summary>

**Topic level:** intermediate. Read the requirements below before choosing it.

**Languages recorded:** en

**Useful for:**

- MIT-licensed library and examples
- Basic example pairs a checkbox-controlled message component with a test
- Explains testing through observable user behavior

**Requirements, costs and limitations:**

- Assumes React, JavaScript or JSX and a configured test environment
- Examples are illustrations rather than a complete testing curriculum
- README includes historical compatibility sections; select setup instructions matching your React version

**Source checked:** 2026-10-24 (github-repo).

Read testing-library/react-testing-library main README.md and LICENSE via raw.githubusercontent.com. The Examples section supplies HiddenMessage component code and a test using render, screen queries, a checkbox interaction and assertions on visible content; a more complex login example follows. The README explains testing without implementation details, npm installation, optional jest-dom matchers and React-version compatibility notes. LICENSE is MIT. Free refers to the library and examples, not any separately advertised paid course. English checked; examples and setup were not executed, and current maintenance activity was not verified.

**Study format:** semi. **Focus-friendly rating:** unknown (editorial judgment).

</details>

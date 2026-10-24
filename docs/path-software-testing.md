# Path: software testing and QA

QA and test automation engineers investigate how software behaves, report problems and build repeatable checks. This introductory route practises those tasks on code you own; it is not a complete qualification or a promise of employment. Start with basic programming and command-line skills. Choose one track for the whole route: Python functions with pytest, or a small local web application with Playwright if you already know JavaScript or TypeScript and basic HTML. The paired resources below are alternatives, not two required courses. You need a computer and the chosen toolchain; Playwright also needs its browser installation. No special hardware or paid testing service is required for this local exercise.

[Back to the start](../README.md)

If a step assumes programming or terminal skills you have not learned, use the relevant parts of [Path 0](path-0-fundamentals.md) first. Work through one small step at a time; you do not need to finish every linked course.

## Step 1: Choose one small behavior and describe its expected results

Follow only your chosen track. For Python, use a tiny function such as calculating a basket total from a list of prices. For the web track, use a local page where a button changes a visible message. Write down the starting state, the action or input, and the result you expect. Keep the project small enough to explain without a framework tour.


- [pytest - Get Started](https://github.com/pytest-dev/pytest/blob/main/doc/en/getting-started.rst) (Free): Official introductory guide to installing pytest, writing a first Python test and interpreting assertion failures before progressing to multiple tests.
- [Playwright - Getting Started](https://github.com/microsoft/playwright) (Free): Official Playwright introduction with installation commands and sample end-to-end web tests using browser automation, locators and assertions.

**Advance when:** You can demonstrate the behavior manually and write three clear input or action examples with expected outcomes, including an empty input or initial state where relevant.


## Step 2: Automate one check and deliberately make it fail

Use the installation and first-test instructions for the same track. With pytest, call your function and assert the expected result. With Playwright, run your local application, find the control using a suitable locator, perform the action and assert the visible result. Temporarily change your own code to break that behavior, then restore it after reading the failure. A passing test is useful only if it detects the relevant mistake.


- [pytest - Get Started](https://github.com/pytest-dev/pytest/blob/main/doc/en/getting-started.rst) (Free): Official introductory guide to installing pytest, writing a first Python test and interpreting assertion failures before progressing to multiple tests.
- [Playwright - Getting Started](https://github.com/microsoft/playwright) (Free): Official Playwright introduction with installation commands and sample end-to-end web tests using browser automation, locators and assertions.

**Advance when:** Your test passes with the intended behavior, fails after the deliberate change and passes again after restoration; you can identify the expected and actual results in the report.


## Step 3: Turn the examples into a small repeatable suite

Add checks for the remaining examples from the first step. For Python, include the empty list and a simple total with more than one price. For the web page, include its initial message and the result of another interaction. Give every check a clear name and avoid depending on a previous test's side effects. Run the suite twice from the same clean starting state, investigating any inconsistent result rather than hiding it with a fixed delay.


- [pytest - Get Started](https://github.com/pytest-dev/pytest/blob/main/doc/en/getting-started.rst) (Free): Official introductory guide to installing pytest, writing a first Python test and interpreting assertion failures before progressing to multiple tests.
- [Playwright - Getting Started](https://github.com/microsoft/playwright) (Free): Official Playwright introduction with installation commands and sample end-to-end web tests using browser automation, locators and assertions.

**Advance when:** At least three checks run and produce the same expected outcomes on two consecutive runs, and changing one relevant behavior causes the appropriate check to fail.


## Step 4: Leave a useful failure report and instructions for the next run

Finish the mini project with a short README containing installation steps, the command to run tests and any application startup step. Write one sample bug report from the deliberate failure: starting state, reproduction steps, expected result and actual result. State what your suite does not cover. Keep reports local and remove passwords or personal data from screenshots and logs before sharing them.


- [pytest - Get Started](https://github.com/pytest-dev/pytest/blob/main/doc/en/getting-started.rst) (Free): Official introductory guide to installing pytest, writing a first Python test and interpreting assertion failures before progressing to multiple tests.
- [Playwright - Getting Started](https://github.com/microsoft/playwright) (Free): Official Playwright introduction with installation commands and sample end-to-end web tests using browser automation, locators and assertions.

**Advance when:** You can restart the chosen toolchain and rerun the checks using only your notes, and someone reading the sample report can understand and reproduce the problem.


## Where to go next

After the last checkpoint, improve your project or browse the related areas for a specific gap:

- [Software testing and QA](area-testing.md)

[Compare the learning paths](../README.md#choose-a-learning-path)

---
This path is an editorial starting point, not an exhaustive curriculum or certification. Tell us what worked for you: see [CONTRIBUTING](../CONTRIBUTING.md).

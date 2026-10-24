# First project: data analysis

Data analysts turn questions into calculations, check the quality of the data and explain what the results support. This route is for beginners who want to explore a small table rather than build a production data system. SQL practice needs only a browser. Before the Python step, you should be able to use variables, lists, loops and functions from Path 0. Use a small public tutorial dataset or an invented CSV, never private records. Your final result is a short report with a reproducible calculation, a chart and limitations.

[Back to the start](../README.md)

**Short first-project guide.** To study toward a profession over a longer sequence, [choose a curriculum](curricula.md).

## Before you start

A browser is enough to begin SQL; learn basic Python variables, lists, loops and functions before Step 3.

If a step assumes programming or terminal skills you have not learned, use the relevant parts of [Path 0](path-0-fundamentals.md) first. Work through one small step at a time; you do not need to finish every linked course.

## Step 1: Answer questions with SQL

Start with SELECT, filtering, sorting and aggregate lessons in the browser. Save three working queries and write the question each one answers, such as which group has the largest count. Check a small result by counting the example rows yourself. Then try one JOIN lesson and compare the input and output rows to see how repeated matches change a count.

- [SQLBolt](https://sqlbolt.com/) (Free): Short interactive SQL lessons and exercises from SELECT to JOINs, aggregates and table changes, run in the browser.

**Advance when:** You can write a filtered query and a grouped summary, explain their results and identify when a JOIN could count the same record more than once.

## Step 2: Explore your own small table

Install the desktop tool if your machine supports it, create a local SQLite database and import an invented CSV with a category and a numeric value. Include a missing value and a duplicate row so you can practise checking them. Write queries for row count, missing values and totals by category, and record how you treat the duplicate.

- [DB Browser for SQLite](https://github.com/sqlitebrowser/sqlitebrowser) (Free): Visual desktop tool for creating and editing SQLite databases, importing CSV files and running SQL queries with inspectable results.

**Advance when:** Your saved SQL reproduces the totals, you have checked them against the small source table, and you can explain how missing or duplicated values affect the answer.

## Step 3: Repeat the analysis in Python

Follow the tutorials on reading a CSV, selecting data and calculating summary statistics. Load the same invented table, reproduce one SQL result and compare the numbers. Keep the CSV and a short Python script together, with notes about the duplicate and missing value. Start with only the operations needed for your question.

- [pandas Getting Started Tutorials](https://pandas.pydata.org/docs/getting_started/index.html) (Free): Official pandas getting-started guide with short tutorials on reading and writing data, selecting, filtering, plotting, reshaping, merging and time series.

**Advance when:** Running your script from the start produces the expected summary, and you can explain any difference between the raw rows and the rows used in your calculation.

## Step 4: Explain one finding with a chart

Use the chart guide to choose a simple display for your summary, then create it using the pandas plotting tutorial from the previous step. Label the title, axes and units. Write a short report containing the question, data source, result and one limitation; do not claim that a pattern proves its cause.

- [From Data to Viz](https://www.data-to-viz.com/) (Free): Decision-tree website that guides you from your data type to an appropriate chart, with links to R and Python code and a catalog of common chart caveats.

**Advance when:** A reader can tell what was measured, reproduce the reported number and understand a limitation without asking you to explain the chart.

## Where to go next

After the last checkpoint, improve your project or browse the related areas for a specific gap:

- [Data, databases and statistics](area-data.md)

[Compare first-project guides](learning-paths.md) · [Choose a profession curriculum](curricula.md)

---
Tell us what worked for you: see [CONTRIBUTING](../CONTRIBUTING.md).

# First project: AI and machine learning

Machine-learning practitioners use data to build models, test predictions on examples the model has not seen and explain where the results can fail. This route is for beginners exploring that work, not a promise of professional readiness. You need basic Python, including functions and lists, plus comfort with tables, averages and simple algebra. Complete the relevant parts of Path 0 first if needed. Start with small public tutorial datasets and classic models; no paid API or large model is required. Never upload personal, confidential or sensitive data to a hosted notebook.

[Back to the start](../README.md)

**Short first-project guide.** To study toward a profession over a longer sequence, [choose a curriculum](curricula.md).

## Before you start

Basic Python functions and lists, plus familiarity with tables, averages and simple algebra.

If a step assumes programming or terminal skills you have not learned, use the relevant parts of [Path 0](path-0-fundamentals.md) first. Work through one small step at a time; you do not need to finish every linked course.

## Step 1: Understand a prediction task

Start with the introductory regression and classification material. Use a small tutorial example to identify the input features and the target being predicted. Write down whether the task predicts a number or a category, what information is available at prediction time and what a wrong prediction would mean. Review the recommended prerequisites when a topic is unfamiliar.

- [Machine Learning Crash Course (Google)](https://developers.google.com/machine-learning/crash-course) (Free): Google's fast-paced introduction to machine learning with animated videos, interactive visualizations and exercises, refreshed to cover embeddings, large language models and production ML.

**Advance when:** You can explain features, labels, training and evaluation in your own words and identify one feature that would leak the answer into the inputs.

## Step 2: Train a simple baseline model

Take the introductory machine-learning exercises with their supplied dataset. A free Kaggle account is needed for the hosted notebooks. Separate training and validation data before fitting, compare the model with a simple constant prediction and record the validation metric. Keep the dataset small and do not use a GPU or paid service for this exercise.

- [Kaggle Learn](https://www.kaggle.com/learn) (Free): Short, no-cost interactive micro-courses with in-browser notebooks on Python, pandas, SQL, data visualization, machine learning, deep learning, computer vision, NLP and more.

**Advance when:** You can rerun the notebook from the beginning, show predictions on held-out examples and explain whether the model improves on the constant baseline using the same metric.

## Step 3: Turn one example into a reproducible mini-project

Choose a beginner lesson matching the kind of prediction you just practised and work through its sample-data project. Record the data source, feature choices, split and evaluation metric. Compare two simple configurations while keeping the evaluation method fixed. Write a short report about the result, a mistake you inspected and a limitation. Leave any final test set untouched while choosing between configurations.

- [Machine Learning for Beginners (Microsoft)](https://github.com/microsoft/ML-For-Beginners) (Free): Microsoft's 12-week, 26-lesson curriculum on classic machine learning with Scikit-learn, with pre- and post-lesson quizzes, assignments and projects (Python and R).

**Advance when:** Your saved instructions reproduce the analysis, the report compares the models with a baseline and you can explain why a good score on tutorial data does not establish that the model is safe or useful in a real application.

## Where to go next

After the last checkpoint, improve your project or browse the related areas for a specific gap:

- [AI, machine learning and LLMs](area-ai.md)

[Compare first-project guides](learning-paths.md) · [Choose a profession curriculum](curricula.md)

---
Tell us what worked for you: see [CONTRIBUTING](../CONTRIBUTING.md).

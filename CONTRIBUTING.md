# How to contribute

Thank you! You can help even if you have never used Git.

## Easiest way: suggest a tool (no Git needed)
1. Go to **Issues > New issue** and choose **Suggest a tool**.
2. Fill in the form. If you are not sure about a field, write "not sure": that is fine.

## Fix a wrong detail
Open an issue with the tool name and what is wrong (dead link, price changed, no longer free...).

## Send a pull request (if you know Git)
1. Add or edit one file in `data/tools/<slug>.yml`. Copy an existing entry and follow `data/SCHEMA.md`.
2. Run `make install` once, then `make build`. This checks your file and regenerates the README and `docs/`.
3. Open a pull request. CI re-checks everything.

## Improve a learning path

Learning paths in `data/paths/*.yml` help people choose a direction and know what to do next. Explain the role or activity in plain language, state prerequisites, and choose a few existing resources for a small project. Each step needs a concrete action and an observable completion check. Follow `data/SCHEMA.md`, then run `make build` and `make check` to validate the references and regenerate navigation and pages. Never edit generated pages by hand.

## Improve profession profiles and source guidance

Edit the group data in `data/professions/` and the reference metadata in `data/profession-guidelines.yml`. Explain what each role does, preserve useful aliases, and link only relevant areas and existing routes. Separate academic recommendations, skill frameworks, certification objectives and educational courses. Record the issuing organisation, scope and whether you actually read each source. A related reference is not evidence of a profession-specific curriculum. See `data/SCHEMA.md`, then regenerate and validate with `make build` and `make check`.

## Improve a profession curriculum

The editorial recipes in `data/curricula/` are longer learning sequences: prerequisites, topics, practice, checkpoints and a final work sample. Tailor each sequence to its role, state experience requirements and record resource gaps honestly. A short first-project guide is a way to try an area; it does not replace the full recipe. Keep one recipe per profile and use existing resource slugs. Run `make build` and `make check`; the checks protect complete profile coverage, valid references and navigation.

## What gets in
- Free first. A cheap option is fine if the community clearly recommends it. Say honestly what it costs.
- It must work today and be maintained (or clearly marked as an archive).
- Link to the official page (not a copy, shortener or file-sharing link).
- One objective sentence, no marketing. Do not guess: if you could not confirm a detail, write `unverified` or `unknown`.
- Not a duplicate of another entry.

## Not medical or professional advice
Focus and ADHD entries are learning tools and community experience, not medical advice.

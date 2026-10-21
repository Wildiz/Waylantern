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

## What gets in
- Free first. A cheap option is fine if the community clearly recommends it. Say honestly what it costs.
- It must work today and be maintained (or clearly marked as an archive).
- Link to the official page (not a copy, shortener or file-sharing link).
- One objective sentence, no marketing. Do not guess: if you could not confirm a detail, write `unverified` or `unknown`.
- Not a duplicate of another entry.

## Not medical or professional advice
Focus and ADHD entries are learning tools and community experience, not medical advice.

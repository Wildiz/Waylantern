# Entry schema (draft v0)

One YAML file per tool in `data/tools/<slug>.yml`.

| Field | Values / notes |
|---|---|
| `name` | Name as the resource calls itself |
| `url` | Authoritative link (author/official site or repo) |
| `category` | The **format** only: `path` (full ordered curriculum), `course` (course or book), `practice` (interactive exercises), `reference` (lists, docs, articles), `roadmap`, `tool` (apps and software), `community`. The subject goes in `areas`, never in the category. |
| `price` | `free`, `freemium`, `paid-cheap`, `paid`, `unverified` |
| `level` | `beginner`, `intermediate`, `advanced`, `all` |
| `languages` | ISO codes of available languages, `en` first |
| `structure` | `guided` (has a path), `semi`, `self-directed` |
| `focus_friendly` | `high`, `medium`, `low`, `unknown` (short sessions, fast feedback, clear path) |
| `description` | One objective sentence |
| `pros` / `cons` | Short lists |
| `verified` | `{date, method, notes}`. `method`: `official-site`, `github-repo`, `search-only` |

Rule: if a field was not confirmed from a primary source, use `unverified`/`unknown`. Do not guess.


`areas` (required, one or more): the subject area(s) used by the "Browse by area" pages. Values: `cs`, `web`, `software`, `networking`, `architecture`, `testing`, `embedded`, `design-product`, `data`, `ai`, `devops`, `it-support`, `security`, `math`, `games-mobile`, `career`, `study-skills`, `focus`, `general` (platforms that cover any topic). An entry can belong to several areas.

The added areas distinguish computer networks (`networking`), software and systems architecture (`architecture`), software testing and QA (`testing`), embedded systems and firmware (`embedded`), UX/UI and product design (`design-product`), and IT support and service management (`it-support`). Keep existing area assignments when adding a relevant subject, so resources remain discoverable from their previous pages.

Areas describe subjects, not job titles, seniority or specific products. For example, Network Engineer is a role, PostgreSQL is a technology, and Senior is a career level. The entry's `level` describes the learning resource's difficulty. Add an area when there are relevant resources to browse; this catalogue does not claim to be an exhaustive or official classification of IT professions.

## Editorial learning paths

Short learning paths live in `data/paths/*.yml` and are validated against `data/path-schema.json`. Each requires a `title`, a short `summary` for the README, related `areas`, an `intro`, and ordered `steps`. The introduction explains what the learner will try, what a related role does and any prerequisites. Each step has a `title`, a `short` label, existing resource slugs in `tools`, a `why` explaining the next action, and an observable `advance_when` checkpoint. `helpers` is optional; when present it contains `why` and `tools`. A step may set `sequence: true` when resources are complementary rather than alternatives in the fundamentals summary.

Prefer a small project and a few focused steps over another long list of courses. Describe required accounts, hardware or paid infrastructure when relevant. Do not promise employment, imply that completing the path qualifies someone for a role, or present an editorial path as an official professional standard. `make check` validates the paths and their resource/area references before checking generated pages. The generator links paths from the README and related area pages; edit the YAML instead of generated documentation.

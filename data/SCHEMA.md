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


`areas` (required, one or more): the subject area(s) used by the "Browse by area" pages. Values: `cs`, `web`, `software`, `data`, `ai`, `devops`, `security`, `math`, `games-mobile`, `career`, `study-skills`, `focus`, `general` (platforms that cover any topic). An entry can belong to several areas.

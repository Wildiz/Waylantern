# Working notes for Claude

## Delegating to subagents (owner's standing instruction)
Choose the model and effort per task to save tokens. The owner has asked for this explicitly, so set `model` and `effort` on every Agent call without asking each time.

| Task | Model | Effort |
|---|---|---|
| Mechanical checks: link status, price/field re-verification on pages that load | haiku | low |
| Verification on tricky pages (bot protection, JS-rendered, conflicting sources) | sonnet | medium |
| Discovering and writing new entries (needs judgment about quality and fit) | sonnet | medium |
| Dedupe, final review, merging, anything user-facing | main session model | default |

Never use `max` effort unless the owner asks. Never guess data: unconfirmed fields stay `unverified`/`unknown`.

## Merging and publishing (owner's standing instruction)
- Never merge into `main`, push to `main`, change repo visibility or enable auto-merge/auto-approve of anything without the owner's explicit confirmation in the same conversation. Work on a branch, push the branch, then ask.
- No workflow may auto-merge, auto-approve or run with write permissions it does not need.
- Do not commit downloaded third-party files (scratch downloads go in the scratchpad, never the repo).

## Project rules
- English first; Spanish is optional and lives in `docs/other-languages.md` when a resource has no English version.
- Data lives in `data/tools/*.yml`; README and `docs/` are generated: run `make build`, never edit them by hand.
- The repo stays private until the owner says otherwise.

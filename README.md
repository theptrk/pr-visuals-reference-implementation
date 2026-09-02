# PR Visuals Reference Implementation

How to write PR descriptions that visual readers can scan — demonstrated on a
fresh Django project where **each theme is a branch** and each branch carries a
`PR.md` written exactly per the
[style guide](docs/pr-visual-review-style-guide.md). A rendered example of
every element lives in [docs/pr-visual-mock.html](docs/pr-visual-mock.html) —
open it in a browser.

## Branch map

Read each branch's `PR.md` as if it were the real PR description for that
branch's diff against its parent.

| Branch | Theme | What the PR demonstrates |
|---|---|---|
| `main` | baseline | Fresh project skeleton, style guide, PR template |
| `theme/creating-dbs` | creating DBs | `CREATE TABLE` ×4 — summary table, colored ERD, raw diff block |
| `theme/changing-dbs` | changing DBs | One PR exercising all five change types: `RENAME COLUMN` (orange), `ALTER COLUMN` (blue), `DROP COLUMN` / `DROP TABLE` (red), `ADD COLUMN` (green) |
| `theme/adding-logic` | adding logic | No schema change — the schema sections are *absent*, a sequence flow diagram appears instead |

## Rules the PRs follow (from the style guide)

1. **Never hide a change** — the description is a layer over the net migration
   diff, never a curation of it.
2. **Diff against the base branch**, not migration history — in-PR chains
   coalesce to their net result.
3. **Verbs name their object type** — `RENAME COLUMN`, never a bare `RENAME`.

Sections appear only when the PR touches what they describe — a pure-logic PR
has no schema section at all (see `theme/adding-logic`).

## Regenerating the ERDs

Each schema PR commits its Graphviz source in `PR.md` and the rendered SVG
under `docs/assets/`:

```sh
dot -Tsvg -o docs/assets/<name>.svg <(extract the dot source from PR.md)
```

## Making real PRs from the branches

Push the repo and open one PR per theme branch:

```sh
gh repo create pr-visuals-reference-implementation --public --source=.
git push -u origin main
git push origin theme/creating-dbs theme/changing-dbs theme/adding-logic
gh pr create --base main --head theme/creating-dbs --title "..." --body-file PR.md
```

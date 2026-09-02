# PR Visuals Reference Implementation

How to write PR descriptions that visual readers can scan — demonstrated on a
fresh Django project where **each theme is a branch** and each branch carries a
`PR.md` written exactly per the
[style guide](docs/pr-visual-review-style-guide.md). A rendered example of
every element lives in [docs/pr-visual-mock.html](docs/pr-visual-mock.html) —
open it in a browser.

## Branch map

Read each branch's `PR.md` as if it were the real PR description for that
branch's diff against its parent — or read the real PRs, which are the most
illustrative form:

| Branch | Theme | Real PR | What it demonstrates |
|---|---|---|---|
| `main` | baseline | — | Fresh project skeleton, style guide, PR template |
| `theme/creating-dbs` | creating DBs | [PR #1 — Add the catalog schema](https://github.com/theptrk/pr-visuals-reference-implementation/pull/1) | `CREATE TABLE` ×4 — summary table, colored ERD, raw diff block |
| `theme/changing-dbs` | changing DBs | [PR #2 — Reshape the catalog schema](https://github.com/theptrk/pr-visuals-reference-implementation/pull/2) | One PR exercising all five change types: `RENAME COLUMN` (orange), `ALTER COLUMN` (blue), `DROP COLUMN` / `DROP TABLE` (red), `ADD COLUMN` (green) |
| `theme/adding-logic` | adding logic | [PR #3 — Add tag merging and note search](https://github.com/theptrk/pr-visuals-reference-implementation/pull/3) | No schema change — the schema sections are *absent*, a sequence flow diagram appears instead |

The PRs are stacked: each is based on its parent theme branch, so each PR's
diff is exactly one theme.

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

## Opening the PRs in another repo

The three PRs above were opened with one command per stacked branch — the
same recipe for adopting this in your own project:

```sh
git push origin main theme/creating-dbs theme/changing-dbs theme/adding-logic
gh pr create --base main --head theme/creating-dbs --title "..." --body-file PR.md
# then per branch, each based on its parent:
gh pr create --base theme/creating-dbs --head theme/changing-dbs --title "..." --body-file PR.md
gh pr create --base theme/changing-dbs --head theme/adding-logic --title "..." --body-file PR.md
```

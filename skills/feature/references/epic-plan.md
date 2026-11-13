# Epic · <name>

**Level:** epic · **Status:** planned · **Issue:** #… · **Branch:** … · **PR:** #… ·
**Progress page:** <link>

Used by the `feature` skill for an epic, and by `mvp-plan` for each epic of a project
(there it sits in `docs/mvp/<name>/plans/epic-<n>-<slug>.md`).

## What a person gets
Three to five sentences: what they can do when the epic is done that they cannot now.

## Source
- Design: <boards> → inventory screens <ids>; or
- Requirements: `requirements/<AREA>.yaml`, ids BP-FAM-…; or both (say which part is which).

## Features, in order
| # | Feature | Source ids | Plan | Status |
|---|---|---|---|---|
| 1 | … | … | `<n>-<feature>.md` beside this file (in an MVP: `plans/<feature>.md`) | todo / planned / building / verifying / done |

Order: what the others depend on first (a shared model before its screens).

## End-to-end scenarios — the epic's acceptance criteria
Each crosses features and runs as one browser test (an API test when the epic has no
screen) before the pull request.

| # | A person… | …does, from start to end | …and then | Test |
|---|---|---|---|---|
| 1 | new, signed out | signs up → creates a family → invites a partner | the partner joins and sees the family | `e2e/<file>::<name>` |

## Decisions
| Date | Question | Answer |
|---|---|---|

## Impact on what exists
The epic as a whole: other apps and packages, existing data and accounts, released
builds, deploy order. Each feature's plan details its own.

## Area documents
`docs/features/<area>.md` files this epic creates or changes.

## Later or cut, by the owner
- … (date)

## Log
| Date | From → to | Why |
|---|---|---|

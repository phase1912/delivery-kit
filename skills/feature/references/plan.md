# <What, in a few words>

**Level:** feature — <why> · **Status:** analysing · **Issue:** #… · **PR:** #… ·
**Epic:** <its plan, if part of one>

## What the person can do
Two or three sentences, in the product's words.

## Source
Where this comes from, by id: inventory items (LP-CAL-07…), requirement items (BP-FAM-03…),
or the issue and the owner's words, quoted.

## Scope
- In: … (source ids)
- Out (and why, or which later work): …

## Decisions
| Date | Question | Answer (owner, or "mine — revisit") |
|---|---|---|

## Changes
- Backend: models / migrations, routes (`METHOD /path` — who may call, its refusals),
  rules, outside services (stubbed in tests at the port).
- Client: stores, screens, words in every language.
- Files: the ones this is expected to touch.

## Steps
- [ ] backend and its tests
- [ ] data and seed
- [ ] client
- [ ] a test per criterion

## Acceptance criteria
| # | Given | When | Then | Source | Proof |
|---|---|---|---|---|---|
| 1 | … | … | … | LP-CAL-07 / BP-FAM-03 | test name / screenshot, filled in stage 5 |

## Impact on what exists
- Callers (found by search): … and what each sees after the change.
- API: shapes that change; clients that still send the old one (released phone builds).
- Data: existing rows and accounts — backfill, default, move?
- Deploy: the migration works with the code still running; the order of deploys.
- Behaviour people rely on that changes — agreed by the owner?
- Suites to run besides this work's own: …

## Area documents
- `docs/features/<area>.md` — what changes in it.

## Risks
- …

## Review
Date, reviewers, findings fixed, re-check result.

## Log
| Date | From → to | Why |
|---|---|---|

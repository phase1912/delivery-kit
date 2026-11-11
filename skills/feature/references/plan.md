# <What, in a few words>

**Status:** analysing · **Size:** feature — <why> · **Issue:** #… · **PR:** #…

## What the person can do
Two or three sentences, in the product's words.

## Scope
- In: …
- Out (and why, or which later work): …
- Large only — the features, one commit each: 1. … 2. …

## Decisions
| Date | Question | Answer (owner, or "mine — revisit") |
|---|---|---|

## Changes
- Backend: models / migrations, routes (`METHOD /path` — who may call, its refusals),
  rules, outside services (stubbed in tests at the port).
- Client: stores, screens, words in every language.
- Files: the ones this is expected to touch.

## Acceptance criteria
| # | Given | When | Then | Proof |
|---|---|---|---|---|
| 1 | … | … | … | test name / screenshot, filled in stage 5 |

## Impact on what exists
- Callers (found by search): … and what each sees after the change.
- API: shapes that change; clients that still send the old one (released phone builds).
- Data: existing rows and accounts — backfill, default, move?
- Deploy: the migration works with the code still running; the order of deploys.
- Behaviour people rely on that changes — agreed by the owner?
- Suites to run besides this work's own: …

## Risks
- …

## Log
| Date | From → to | Why |
|---|---|---|

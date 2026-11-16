# Work levels: fix, feature, epic, project

**Status:** shipping · **Level:** feature — several skill files, one script rule ·
**Issue:** #2

## What the person can do
Say what they need in their own words. The kit decides whether it is a fix, a feature, an
epic or a project (asking when unsure), plans it at that size, checks every result
against written criteria and keeps documentation of how the system works now.

## Decisions (owner, 2026-11-13)
| Question | Answer |
|---|---|
| Levels | fix / feature / epic / project; one entry (`feature`) sizes and asks when unsure |
| Split a feature into subtasks? | No — a step checklist in its plan; one that outgrows becomes an epic |
| A plan | Always. Fix: in the issue. Feature, epic, project: a file |
| Source without a design | Requirements with ids, each with its source and build / later / cut |
| Design for only part of the work | Each epic its own way: inventory where drawn, requirements elsewhere |
| Living documentation | One file per area, `docs/features/<area>.md`, updated in the commit that changes behaviour |
| Review on a fix | Yes, one code-reviewer |
| Epic criteria | End-to-end scenarios, browser-tested before the epic's pull request |
| Progress page | Epic and project; each feature's criteria on click; updated at every status change |
| An MVP in progress | Adopts this at its next epic |

## Changes
- `feature`: the four levels, the question when unsure, the step checklist, docs per area,
  review at every level; templates for a fix (issue), an epic plan, an area document.
- `mvp-discover`: requirements when there is no design, per epic when mixed.
- `mvp-plan`: an epic plan file with end-to-end scenarios.
- `mvp-verify`: the area document in each feature's commit, the scenarios before an epic's
  PR, the progress page at every status with criteria per feature.
- `code-reviewer`: checks the diff against the plan's criteria and the area document.
- `check_inventory.py`: an area file with `source:` (not a design board) and `rule` items.

## Acceptance criteria
| # | Given | When | Then | Proof |
|---|---|---|---|---|
| 1 | the request "fix the typo on the sign-in screen" | `feature` starts | fix: plan in the issue, a code-reviewer, no plan file | skills/feature/SKILL.md §1 |
| 2 | "add a CSV export of receipts" | `feature` starts | feature: a plan file with criteria and impact | §1 |
| 3 | a request that could be a feature or an epic | `feature` starts | one question with a recommendation before planning | §1 |
| 4 | "build the family area" with no design | sized as epic | requirements with ids, an epic plan with scenarios | §1, epic-plan.md |
| 5 | an MVP with `docs/mvp/<name>/state.yaml` from 0.2 | the plugin is updated mid-epic | the same skill names, paths and state format; new parts start at the next epic | mvp/SKILL.md |
| 6 | a requirements file with an item verified but no test naming it | the check runs | it reports the item | scripts/tests |
| 7 | a valid 0.2 inventory | the check runs | the same result as before | scripts/tests; the planner's 62 screens, old vs new script |

## Impact on what exists
- Callers: the planner MVP in phase1912/budget-planner uses `delivery-kit:mvp*` with
  `docs/mvp/life-planner/`; nothing it reads is renamed or reshaped.
- Users get it only after `claude plugin update`; version 0.3.0.
- The consumer's own words: budget-planner's `docs/stack.md` and `CLAUDE.md` still say
  "small" and "large" (0.2 sizes) — to update there when it moves to 0.3.
- A running MVP's progress page gains criteria per feature and updates at every status.
- Suites: `pytest scripts/tests` (CI).

## Log
| Date | From → to | Why |
|---|---|---|
| 2026-11-13 | verify → build | code-reviewer: 1 blocker (strict wanted a design review on requirement areas), 9 major, 13 minor |
| 2026-11-13 | verify → build | re-check: strict on a whole area refused every feature but the last; `--items` added |

## Review
2026-11-13: code-reviewer (1 blocker, 9 major, 13 minor — fixed), a fresh re-check (18 of
24 fixed, one new major from a fix — fixed with `--items` and its tests), then 14 tests
green and the planner's 62-screen inventory giving the same output, plain and strict, on
the old and the new script.

---
name: feature
description: Run one piece of work on rails — a feature, a fix, a change to how something behaves. Size it, analyse it and ask everything unclear up front, plan it with acceptance criteria and its impact on what exists, build it, verify it (checks, your own look, reviewers who did not build it), go back and fix on any failure, and finish with a pull request. Use whenever the person asks to build, add, change or fix something ("add X", "fix Y", "make Z work like…"). For a whole app or area built from a design, use the mvp skill instead.
---

# One piece of work, on rails

The person in charge ("the owner") says what is needed. You deliver it tested, reviewed
and in a pull request, asking whenever something is not decided. Nothing moves to the
next stage until its exit holds; a failure sends the work back, never around.

| Stage | Exit |
|---|---|
| 1. Size | small, feature or large — said in one line with the reason |
| 2. Analyse and ask | every open question answered, written in the plan |
| 3. Plan | criteria and impact written; no open question left |
| 4. Build | the code, its tests, the project's checks pass locally |
| 5. Verify | checks green, own look done, reviews clean, every criterion proven |
| 6. Ship | commits and the pull request, its "what to check" list |

## Going back

- A check or test fails, or your own look finds a difference → 4, fix, then 5 from its
  first step.
- A reviewer finds something above minor → 4, fix, then a narrow re-check (5.4).
- The fix needs a decision nobody made → 2: ask, then go on.
- The plan was wrong (a missed caller, a criterion that cannot hold) → 3: change the plan
  and say what changed.
- The same failure survives two fix rounds → stop and ask the owner, with what you tried.
- Changes asked for on the pull request → 4 and 5 again, same branch, same PR.

Write each return in the plan's log (date, from → to, why). Never ship a failing check,
and never call a criterion met without its proof.

## Where things live

- **The project's rules and commands** — issues, branches, commits, pull requests, how
  to run, test and check, the widths and devices — in the stack file the project's
  `CLAUDE.md` names. If there is none, write one from the project, modelled on
  `../mvp/references/stack-example.md`, and show it to the owner.
- **The work's state** — `docs/plans/<YYYY-MM-DD>-<slug>.md` (or where the stack file
  says), from `references/plan.md`. Its status line is one of `sizing`, `analysing`,
  `planned`, `building`, `verifying`, `shipping`, `done`, `blocked: <why>`. Update it at
  every change; after a break or a compacted context, read it and go on from there.

## 1. Size

- **Small** — one or two files, no shared code, no data or API change, nothing a person
  sees beyond the fix itself. No plan file: the criteria go in the issue; stage 5 is the
  checks, the tests and your own look, without reviewers.
- **Feature** — everything else that fits in about a day. All stages.
- **Large** — more than about 12 criteria, more than two screens with their own flows, or
  a new backend domain *and* a large screen. Split it into features in the plan; each runs
  stages 3–5 and becomes its own commit; ship once. Built from a design end to end → `mvp`.

The owner may change the size; write it in the plan.

## 2. Analyse and ask

Read what the request touches: the code, its tests, the documents that describe it, the
history of its files. Find every caller by search (or the project's impact tools). Then
write down what the person will be able to do and everything that is not decided:
behaviour, errors and empty states, who may do what, limits, words, what changes for
people already using it, what it could break elsewhere.

Ask it all at once, before planning, the way `../mvp-discover/references/asking.md`
says: up to 4 questions per card, as many cards as needed, recommendation first. Ask
nothing you can find out yourself. Later, ask the moment a stage meets something
undecided — never build around the gap. Every answer goes into the plan, dated.

## 3. Plan

Fill `references/plan.md`: what the person can do, scope, decisions, the backend and
client changes, **acceptance criteria** (given / when / then, each checkable by a test or
by hand) and **impact on what exists** (every caller, API client, existing data, the
deploy order, the other suites to run — "none" only after the search that proved it).
A breaking change to something already used goes back to 2 as a question.

## 4. Build

Backend (with a test per rule and a test that another account cannot see or change what
it owns), data and seed, client, then a test per criterion. Follow the project's rules
files. When a design board is involved, port it and read
`../mvp-build/references/details.md`. Commit nothing before stage 5 passes.

## 5. Verify — cheap first

1. The project's checks, the new tests, the whole suite once, and every suite the
   plan's impact section names.
2. Your own look: run the app and walk every criterion by hand at the stack file's widths;
   the phone builds when the change touches them.
3. Reviewers (feature and large): the `code-reviewer` agent always, the
   `design-reviewer` when screens change, in parallel. Give them paths, never your
   conclusions — briefs in `../mvp-verify/references/review-loop.md`.
4. Fixes, then one narrow re-check by a fresh agent of each kind that found something.
5. Tick every criterion in the plan with its proof (a test name, a screenshot).

## 6. Ship

Commit as the stack file says (one commit per feature), push, and open the pull request:
one "what to check" line per commit, the criteria met, the impact in one or two lines,
the issue it closes. Set the plan `shipping`, and `done` once it is merged.

---
name: feature
description: The entry point for any work — a fix, a feature, an epic or a whole project. Sizes it (asking when unsure), then runs it on rails — analyse and ask everything unclear, plan it against a written source with acceptance criteria and its impact on what exists, build, verify (checks, your own look, reviewers who did not build it), go back and fix on any failure, keep the documentation of how the system works, finish with a pull request. Use whenever the person asks to build, add, change or fix something ("add X", "fix Y", "make Z work like…"). A project of many epics continues in the mvp skill.
---

# Any piece of work, on rails

The person in charge ("the owner") says what is needed. You deliver it planned, tested,
reviewed, documented and in a pull request, asking whenever something is not decided.
Nothing moves to the next stage until its exit holds; a failure sends the work back,
never around.

| Stage | Exit |
|---|---|
| 1. Size | the level, said in one line with the reason (asked when unsure) |
| 2. Analyse and ask | the source written; every open question answered |
| 3. Plan | the plan, its criteria and impact written; nothing open |
| 4. Build | the code, its tests, the project's checks pass locally |
| 5. Verify | checks green, own look done, review clean, every criterion proven |
| 6. Ship | the area documents updated, commits, the pull request |

## 1. Size — four levels

| Level | What it is | Its plan | Its parts |
|---|---|---|---|
| **Fix** | one or two files, no shared code, no data or API change | in the issue (`references/fix-plan.md`) | one commit |
| **Feature** | one thing a person recognises, about a day | a file (`references/plan.md`) | one commit; steps as a checklist |
| **Epic** | several features of one area | a file (`references/epic-plan.md`) + a plan per feature | a commit per feature, one PR |
| **Project** | several epics | → the `mvp` skill (with or without a design) | a PR per epic |

Say the level and why. When the request could be two neighbouring levels, ask once
before anything else — AskUserQuestion, your recommendation first with what it would be
cut into ("an epic of three features: A, B, C — or one feature?"). The owner's word
wins. A feature is never split into tracked subtasks: its steps are a checklist in its
plan. A feature that outgrows its plan (more than about 12 criteria, more than two screens
with their own flows, a new backend domain *and* a large screen) is an epic: say so and
re-plan.

## 2. The source, then the questions

Everything is checked against something written. Before planning, write down where the
work comes from, and cite it from the plan by id:

- **a design** → the screens' inventory (`../mvp-discover/references/inventory-format.md`);
- **no design** (epic, project) → requirements with ids
  (`../mvp-discover/references/requirements-format.md`), each with its source — the
  owner's words, a document, the code — and a decision;
- **a fix or a feature** → the issue and the owner's words, quoted in the plan.

When the source is an inventory or requirements, end this stage with the kit's
`scripts/check_inventory.py` over all of it in one run (`requirements/` and `inventory/`),
clean output; before each feature's commit, run it with `--strict --items <the feature's
item ids>` — an area's later items belong to later features.

Read what the work touches: the code, its tests, `docs/features/` for its area, the
history of its files. Find every caller by search (or the project's impact tools). Then
collect everything not decided: behaviour, errors and empty states, who may do what,
limits, words, what changes for people already using it, what it could break elsewhere.
Ask it all at once, before planning, as `../mvp-discover/references/asking.md` says. Ask
nothing you can find out yourself; later, ask the moment a stage meets something
undecided. Every answer goes into the plan's decisions, dated.

## 3. Plan

Fill the level's template. Every plan has: what the person can do, the source it cites,
decisions, the changes, **acceptance criteria** (given / when / then, each checkable by a
test or by hand, each tied to a source id), **impact on what exists** (callers, API
clients, existing data, deploy order, other suites — "none" only after the search that
proved it) and the **area documents** it will change. An epic's plan adds 3–6
**end-to-end scenarios** across its features. A breaking change to something already used
goes back to 2 as a question.

## 4. Build

Backend (a test per rule, and a test that another account cannot see or change what it
owns), data and seed, client, a test per criterion. Follow the project's rules. With a
design, port it and read `../mvp-build/references/details.md`. In an epic, build one
feature at a time, each through 3–5 and committed (with its area documents) as soon as
its stage 5 passes; the epic's pull request waits for the scenarios. Nothing is committed
before its stage 5 passes.

## 5. Verify — cheap first, at every level

1. The project's checks, the new tests, the whole suite once, every suite the impact names.
2. Your own look: run it and walk every criterion at the stack file's widths; the phone
   builds when the change touches them.
3. Review by agents that did not build it: `code-reviewer` always — a fix too — for
   quality, security and the criteria; `design-reviewer` when screens change. Give them
   paths, never your conclusions (`../mvp-verify/references/review-loop.md`).
4. Fixes, then one narrow re-check by a fresh agent of each kind that found something.
5. Tick every criterion with its proof (a test name, a screenshot). An epic, before its
   PR: its end-to-end scenarios green — browser tests, or API tests when it has no screen.

## 6. Ship

Update `docs/features/<area>.md` (`references/area-doc.md`) in the same commit that
changes the behaviour it describes, citing the source ids and the plan. Commit as the
stack file says, push, open the pull request: one "what to check" line per commit, the
criteria met, the impact in a line or two, the issue it closes. An epic keeps its progress
page (`../mvp-verify/references/progress.md`) current at every status change.

## Going back

- A check, a test or your own look fails → 4, fix, then 5 from its first step.
- A reviewer finds something above minor → 4, fix, then the narrow re-check.
- A decision nobody made → 2: ask. The plan was wrong → 3: change it, say what changed.
- The same failure survives two fix rounds → stop and ask the owner, with what you tried.
- Changes asked for on the pull request → 4 and 5 again, same branch, same PR.

Write each return in the plan's log (date, from → to, why). Never ship a failing check,
and never call a criterion met without its proof.

## Where things live

- The project's rules and commands: the stack file its `CLAUDE.md` names (none: write
  one from `../mvp/references/stack-example.md` and show the owner).
- Plans: a feature's `docs/plans/<YYYY-MM-DD>-<slug>.md` (or where the stack file says).
  An epic's folder `docs/plans/<YYYY-MM-DD>-<slug>/`: `epic.md`, `<n>-<feature>.md`, and
  its `requirements/` or `inventory/`. Status line: `sizing`, `analysing`,
  `planned`, `building`, `verifying`, `shipping`, `done`, `blocked: <why>` — update it at
  every change; after a break or a compacted context, read it and go on.
- How the system works now: `docs/features/<area>.md` — in a repository of several apps,
  the app's own docs folder (the stack file says where).

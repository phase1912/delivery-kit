---
name: mvp
description: Entry point for a project of several epics — an app, an MVP or a large area, from a design or from requirements when there is none — or for resuming one. Use when the person says to build an MVP / a prototype / "the whole app as the design", to redo screens to match a design, when the feature skill sizes work as a project, or to continue one already started (a docs/mvp/<name>/state.yaml exists). For a fix, a feature or one epic, use the feature skill. It runs the stages in order and loads mvp-discover, mvp-plan, mvp-build and mvp-verify when each stage starts.
---

# A project, one verified feature at a time

The person in charge (here: "the owner") gives a goal and its source: a design, or what
they want in words and documents. You deliver a working app that matches it — the design
screen by screen and control by control, or the requirements item by item (each epic may
use either; then "matches the design" reads "meets the requirements") — built epic by
epic, each feature tested, reviewed by agents that did not build it, and committed. You
ask the owner whenever the source does not answer a question, and never call something
done that a file does not prove.

## The stages

| Stage | Load | Ends with |
|---|---|---|
| 1. Discover | `mvp-discover` | the inventory or requirements, the owner's answers |
| 2. Cut into epics | `mvp-plan` (epics part) | `state.yaml`; each epic's plan (scenarios) when it starts |
| 3. Per feature: plan | `mvp-plan` (feature part) | `plans/<feature>.md` with acceptance criteria |
| 4. Per feature: build | `mvp-build` | code, seed data, tests, the design's details in place |
| 5. Per feature: verify | `mvp-verify` | tests green, reviews clean, criteria met, one commit |
| 6. Per epic: ship | `mvp-verify` (epic part) | a pull request; the progress table updated |

Stages 3–5 repeat for every feature of an epic; stage 6 closes the epic; then the next
epic. Load a stage's skill when the stage starts, not before: each one is short and
points to its `references/` files, which you read only when that step needs them.

## The state lives in files, not in your memory

Everything is under `docs/mvp/<name>/` in the project (create it in stage 1):

- `state.yaml` — the epics and their features with a status each (`todo`, `planned`,
  `building`, `verifying`, `done`, `blocked: <why>`), the epic's branch and PR.
- `inventory/<screen>.yaml` — one file per screen (format: `mvp-discover`); without a
  design, `requirements/<area>.yaml` (same check, `mvp-discover`'s requirements format).
- `decisions.md` — every question asked and the owner's answer, dated.
- `plans/epic-<n>-<slug>.md` — the epic's plan with its end-to-end scenarios
  (`../feature/references/epic-plan.md`); `plans/<feature>.md` — each feature's plan.
- The project's `docs/features/<area>.md` (in a repository of several apps, the app's
  own docs folder, as the stack file says) — how each area works now
  (`../feature/references/area-doc.md`), updated in each feature's commit. It replaces
  the older `rules/<epic>.md`; read those where they exist.
- `stack.md` — this project's commands and conventions (see below).

On start or after your context was compacted: read `state.yaml`, find the first
feature not `done`, read only its plan and its screens' inventory files, and go on.
Update `state.yaml` at every status change, so the next session can continue.

A project started on an older kit keeps its files as they are. At the start of its next
epic, adopt the rest: write that epic's plan with scenarios, and a
`docs/features/<area>.md` for each area already built, from its plans and decisions.

## The project's stack

The stages are written for any stack. The project's own commands (run, test, lint,
browser tests, phone builds), widths to check, folder layout and rules live in
`docs/mvp/<name>/stack.md` — or in the file the project's `CLAUDE.md` names. If neither
exists, write one in stage 1 from the project (its `CLAUDE.md`, `package.json`,
`pyproject.toml`, CI files), modelled on `references/stack-example.md`, and show it to the
owner.

## Asking the owner

Ask whenever the design or the answers so far do not decide something: in stage 1 all at
once, later as it comes up. Use AskUserQuestion — up to 4 questions per card, as many
cards in a row as needed; each question names the screen, says what is unclear, and puts
your recommendation first. Never decide a product question silently, never cut what the
design draws or fake data on your own, never leave a dead control. Write each answer into
`decisions.md` (and `docs/features/<area>.md` when it is behaviour) before acting on it.

## What the owner sees

A progress artifact — one page, updated at every status change of a feature (`mvp-verify`
says how), each feature's acceptance criteria shown on click:
epics, features, status, design / app screenshots, review results, what is cut or
later. The link goes in every progress message and in each epic's PR.

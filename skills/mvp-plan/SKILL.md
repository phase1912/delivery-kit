---
name: mvp-plan
description: Stages 2 and 3 of the mvp skill — cut the MVP into epics and order them, then, when a feature is about to start, plan just that feature with acceptance criteria and decide whether it must be split. Load it after discovery, and again at the start of every feature.
---

# Plan: epics up front, each feature just in time

Plan wide once, plan deep only what is next: a feature planned weeks ahead is planned on
guesses.

## Epics (once, after discovery)

An epic is an area a person recognises and the owner can accept as a whole: sign-in and
account, onboarding, home, calendar, papers, family. Group the inventory's screens by
epic (set `epic:` in each screen file) and order the epics the way a new user meets the
app, moving forward anything others depend on (sign-in before everything; a shared model
before its screens).

Write them into `state.yaml`: name, screens, order, the branch `feature/<name>-<epic>`
and, later, its PR. Each epic becomes one pull request; each feature inside, one commit.
Show the owner the list in one message and adjust if they reorder.

## Features (when the epic starts)

Cut the epic into features of a sensible size: one screen with its sheets, or one flow
across two screens (sign-up → confirm the address), about a day of work at most, small
enough that one review can hold it, big enough to be worth a commit. List them in
`state.yaml` with status `todo`.

## A feature's plan (when it is next)

Before building, read only the feature's screen files, its epic's `rules/` and the code
it touches; then write `plans/<feature>.md` from `references/feature-plan.md`:

- what the person can do when it is done, in two or three sentences;
- the inventory items it covers (by id), and those it leaves for a later feature;
- the backend: models, migrations, routes, rules, who may do what; outside services;
- the client: stores, screens, the design's source to port (`mvp-build` says how);
- **impact on what exists** — whenever the feature touches code, data or an API that
  something already uses: every caller found by search (other apps, shared packages, phone
  builds already released), existing rows and accounts, a migration that must work with
  the code still running, behaviour people rely on that changes, and the other suites to
  run. A breaking change to something already used is an open question for the owner;
- **acceptance criteria**, one per behaviour: *given / when / then*, each tied to item ids
  and checkable in a browser or by a test — these are what `mvp-verify` signs off;
- risks and open questions.

Then judge the size. Split the feature (and update `state.yaml`) when the plan has more
than about 12 criteria, touches more than two screens with their own flows, or needs a new
domain on the backend *and* a large screen. When an open question remains, ask the owner
now (the `mvp` skill's way of asking) — not after building.

Set the feature `planned`, then load `mvp-build`.

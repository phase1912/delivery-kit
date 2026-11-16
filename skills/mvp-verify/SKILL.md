---
name: mvp-verify
description: Stages 5 and 6 of the mvp skill — prove a built feature: tests, your own side-by-side check, then one design review and one code review by agents that did not build it, fixes, a narrow re-check, the acceptance criteria signed off, one commit, the progress table updated; and close an epic with its pull request. Load it when a feature is built.
---

# Verify one feature, then commit it

The order matters: cheap checks first, so the reviewers spend their tokens on code that
already works.

## 1. Tests and checks

The project's checks from `stack.md`, the feature's unit and backend tests, its browser
tests by item id, and the whole suite once. Then every suite the plan's "impact on what
exists" names — the other app's, the shared packages', the migration against the code
still running — so a change to something shared is proven not to break its other users.
On a phone-touching feature, the iOS and
Android builds in their simulators. Fix and repeat until green.

## 2. Your own side-by-side

For each screen of the feature: the board and the app at every width, saved as
`<SCREEN-ID>-{design,app}-<width>.png` outside git; press every item in both and compare
what happens. Mark items `verified`, or `differs` with what differs, and fix. Go through
`../mvp-build/references/details.md` once more.

For requirement items (no board): walk each item's `does` in the running app or through
its test, and mark it `verified` or `differs` the same way.

## 3. Two reviewers, once per feature

Spawn, in parallel, the `code-reviewer` and — when the feature has drawn screens — the
`design-reviewer` (this plugin's `agents/`). Give each only what it needs to look for itself — **never your conclusions**:

- design-reviewer: the feature's screen files, the design sources and saved boards, the
  running app's address and a demo account;
- code-reviewer: the feature's diff (uncommitted, or a commit range), the project's rules
  files and `stack.md`.

Fix every design difference and every finding above minor, or ask the owner when it is a
design question. Then **one** narrow re-check: a fresh agent of each kind that found
something (never the same one) gets only its list and your fixes, and confirms each is
fixed without new breakage. New findings loop on those items only. Minor findings you fix
without a re-check. Record `review: {at, differences: 0}` on each drawn screen file;
requirement areas carry no `review:` — their proof is the tests and the plan's Review.
`references/review-loop.md` has the briefs.

## 4. Sign off and commit

Go through the plan's acceptance criteria one by one and tick each with its proof (a
test, a screenshot). Run the kit's check in strict mode on the feature's own items
(`scripts/check_inventory.py --strict --items <ids> <inventory and requirements folders>`).
Update the area documents the plan names (`docs/features/<area>.md` — or the app's own
docs folder in a repository of several apps — from
`../feature/references/area-doc.md`) so they describe the behaviour as now built, with
its source ids. Then commit the feature with them — one commit, the project's message
rules, the plan's summary in the body — set it `done` in `state.yaml`, and update the
progress artifact (`references/progress.md`). Next feature: back to `mvp-plan`.

The progress artifact changes at every status change, not only here: when a feature is
planned, building, verifying or done, publish it in the same step that writes
`state.yaml`.

## 5. Closing an epic

When every feature of the epic is `done`: run the epic plan's end-to-end scenarios
against the seeded stack — browser tests, or API tests for an epic with no screen — all
green (a failure goes back to the feature it belongs to). An epic begun on an older kit,
without an epic plan, has none: say so in the PR. Then push the branch, open the pull request with one
"what to check" line per commit, the criteria met and the link to the progress table, and
put the epic's screenshots in front of the owner. Follow the project's CI and merge rules;
the next epic starts from the merged main (or stacks on the branch if the owner says so).

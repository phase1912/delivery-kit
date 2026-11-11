# delivery-kit

Skills and agents for Claude Code that put work on rails. The agent sizes the work, asks
everything unclear up front, plans with acceptance criteria and the impact on what
already exists, builds, verifies with tests and with reviewers that did not build it,
goes back to fix on any failure, and finishes with a pull request.

Two entry points share the same stages:

- **`feature`** — one piece of work: a feature, a fix, a change ("add X", "fix Y").
- **`mvp`** — a whole app or area from a design, epic by epic, each feature through the
  same plan → build → verify loop, with a progress page for the person in charge.

## The rails

```
feature: size → analyse & ask → plan → build → verify → ship (pull request)
                     ▲            ▲       ▲        │
                     │            │       └─ fix ◄─┤ a check, a test or a review fails
                     │            └─ re-plan ◄─────┤ the plan was wrong
                     └─ ask ◄──────────────────────┘ a decision nobody made
                     (the same failure twice → stop and ask the owner)

mvp: discover (whole design → inventory, questions) → epics
     └─ per feature: plan → build → verify → commit;  per epic: pull request
```

Each skill is short and loads its `references/` only at the step that needs them. All
state is in files (`docs/plans/…` for a feature, `docs/mvp/<name>/` for an MVP), so work
resumes after a break or a compacted context.

## Contents

| Path | What |
|---|---|
| `skills/feature` | one piece of work on rails; the plan template |
| `skills/mvp` | MVP entry point, the stages, the state files, how to ask |
| `skills/mvp-discover` | inventory format, asking patterns (used by `feature` too) |
| `skills/mvp-plan` | epics, features, the feature plan with criteria and impact |
| `skills/mvp-build` | build order, porting the design, the details checklist |
| `skills/mvp-verify` | checks, the review loop and briefs, the progress page |
| `agents/design-reviewer.md` | compares built screens with the design, control by control |
| `agents/code-reviewer.md` | reviews a change: rules, impact, correctness, tests, security |
| `scripts/check_inventory.py` | refuses an inventory that would let "matches the design" be said untrue |

## The project's side

The project gives the kit a **stack file** and names it in its `CLAUDE.md`: how to run,
test and check the app, the widths and devices, its layers, and its issue, branch,
commit and pull-request rules. `skills/mvp/references/stack-example.md` is one for
FastAPI + React + Capacitor.

## Install

As a plugin:

```
/plugin marketplace add phase1912/delivery-kit
/plugin install delivery-kit@delivery-kit
```

Or link `skills/*` and `agents/*` into the project's `.claude/skills/` and
`.claude/agents/`.

`check_inventory.py` needs Python 3.11+ and PyYAML; its tests: `pytest scripts/tests`.

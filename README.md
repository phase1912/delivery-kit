# delivery-kit

Skills and agents for Claude Code that put work on rails. The agent sizes the work, asks
everything unclear up front, plans with acceptance criteria and the impact on what
already exists, builds, verifies with tests and with reviewers that did not build it,
goes back to fix on any failure, and finishes with a pull request.

`feature` is the entry for any work. It sizes it into one of four levels, asking when
unsure:

| Level | Plan | Parts |
|---|---|---|
| fix | in the issue | one commit, still reviewed |
| feature | a plan file | one commit; steps as a checklist, never subtasks |
| epic | an epic plan with end-to-end scenarios + a plan per feature | a commit per feature, one PR, a progress page |
| project | → `mvp`: epics, each as above | a PR per epic, a progress page |

Every level works from a written source — a design's inventory, or requirements with ids
when there is no design — and its plan's acceptance criteria cite it. Every change is
reviewed by an agent that did not build it. `docs/features/<area>.md` describes how each
area works now and changes in the same commit as the behaviour.

## The rails

```
feature: size → analyse & ask → plan → build → verify → ship (pull request)
                     ▲            ▲       ▲        │
                     │            │       └─ fix ◄─┤ a check, a test or a review fails
                     │            └─ re-plan ◄─────┤ the plan was wrong
                     └─ ask ◄──────────────────────┘ a decision nobody made
                     (the same failure twice → stop and ask the owner)

mvp: discover (a design → inventory, or requirements; questions) → epics → epic plans
     └─ per feature: plan → build → verify → commit;  per epic: pull request
```

Each skill is short and loads its `references/` only at the step that needs them. All
state is in files (`docs/plans/…` for a feature, `docs/mvp/<name>/` for an MVP), so work
resumes after a break or a compacted context.

## Contents

| Path | What |
|---|---|
| `skills/feature` | the entry: levels, rails; plan templates (fix, feature, epic), the area document |
| `skills/mvp` | MVP entry point, the stages, the state files, how to ask |
| `skills/mvp-discover` | inventory and requirements formats, asking patterns (used by `feature` too) |
| `skills/mvp-plan` | epics, features, the feature plan with criteria and impact |
| `skills/mvp-build` | build order, porting the design, the details checklist |
| `skills/mvp-verify` | checks, the review loop and briefs, the progress page |
| `agents/design-reviewer.md` | compares built screens with the design, control by control |
| `agents/code-reviewer.md` | reviews a change: rules, impact, correctness, tests, security |
| `scripts/check_inventory.py` | refuses an inventory or requirements list that would let "done" be said untrue |

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

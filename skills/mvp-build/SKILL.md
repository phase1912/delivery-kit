---
name: mvp-build
description: Stage 4 of the mvp skill — build one planned feature down to the smallest detail of the design (sizes, colours, motion, every state, every control's behaviour), with its backend, seed data and tests. Load it when a feature's plan is written; never for a feature without one.
---

# Build one feature, to the last detail

Read the feature's plan, its screens' inventory files and the project's `stack.md`;
nothing else from the MVP. Set the feature `building` in `state.yaml`.

## Order inside a feature

1. **Backend** — models and migration, repository, service with the rules, routes, the
   refusal codes; tests for each rule and a test that another account (another family,
   another tenant) can neither see nor change it.
2. **Seed** — extend the demo data so the screen shows what the design shows (names,
   counts, dates relative to today); the seed runs twice without duplicates.
3. **Client** — store, then screen, then its sheets and states.
4. **Browser tests** — one per control, sheet and state item of the feature, named by its
   id, doing what a person does and checking what the plan's criterion says.

Commit nothing yet: `mvp-verify` commits the feature once it passes.

## Port the design, do not redraw it

The closest match comes from the design's own source. Take the board's markup, CSS, SVG
and animation and move them into the project's components, replacing raw values with the
project's tokens (add tokens where the design has values the project lacks) and fake data
with the store's. Redraw only what cannot be ported, and say so in the plan.
`references/details.md` lists what is easy to lose on the way — read it before the
screen and again before you hand the feature to `mvp-verify`.

## When the design does not decide

Stop and ask the owner (the `mvp` skill's way of asking) the moment a criterion, a
control or a state is not decided by the design, the rules or the plan. Write the answer
into `rules/<epic>.md`, then go on. Do not build around the gap. Do not cut an item,
fake its data or leave a control dead because it is hard; ask.

## Done building

Every item of the feature is `built` in its inventory file, the project's checks pass
(`stack.md`), the browser tests run green, and you looked at each screen at the widths in
`stack.md`. Set the feature `verifying` and load `mvp-verify`.

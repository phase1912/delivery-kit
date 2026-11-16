---
name: mvp-discover
description: Stage 1 of the mvp skill — read the whole design (or, without one, the owner's words, documents and code) and the existing code, list every screen, state and control in an inventory (or every behaviour as requirements with ids), find everything unclear, and ask the owner until nothing product-level is left to guess. Load it when an MVP starts (from the mvp skill), or when a new design area arrives mid-way.
---

# Discover: the whole design, everything unclear, every answer

Go wide before deep: skim everything first, then write it down precisely. Nothing is
built in this stage.

## 1. Collect the design

- Read every design source the owner names (artifacts, canvases, files, links) and ask
  once whether there are more. Save each board's source outside git (e.g.
  `~/Library/Caches/<name>-design/`) and note in `decisions.md` which source wins when two
  disagree.
- Compare sources before reading them twice: two artifacts may hold the same boards.
- Render the boards you will compare against later (a static page around the board's
  HTML is enough); a board's logic code says what its controls do.

No design, or none for some epics: collect the owner's words, the documents they name
and what the code does today instead, and write requirements for those epics
(`references/requirements-format.md`) — same ids, decisions and check as the inventory.
The rest of this stage applies to both.

## 2. The inventory, one file per screen

Write `docs/mvp/<name>/inventory/<SCREEN-ID>.yaml` for every screen — each route, sheet,
dialog, onboarding step, and the frame around them (tab bar, header). Inside, one item
per block, control, state and text. Format and rules: `references/inventory-format.md`.
For many boards, split them among helper agents by group with the same brief and the
format file, then merge and spot-check; ids stay unique.

For every item check the existing code and say honestly: `data: have | missing` (does a
route / field serve it today) and `status: todo | built` (does a screen implement it).
Nothing is `verified` in this stage.

## 3. Find what is unclear

While reading, collect into `decisions.md` (draft) everything the design does not decide:

- features whose data or service does not exist (the big product questions);
- behaviour the design does not draw: errors, empty states, permissions (who may change
  what), concurrency, notifications, limits, what a control does when undrawn;
- contradictions between boards, and promises the product cannot keep (privacy, hosting,
  security claims) — these are always asked, never quietly reworded;
- anything the design shows that the platform makes hard (camera, push, background);
- what the design changes in a system already running: other apps or packages that
  share the code, people's existing data and accounts, released phone builds — ask before
  planning anything that would break them.

## 4. Ask until nothing is guessed

Group the questions from big to small: product scope first (build now / later / cut a
whole area), then per screen. Ask with AskUserQuestion — up to 4 per card, as many cards
in a row as needed, each question naming the screen and the problem, recommendation first
with a one-line reason and a rough size (S/M/L). Patterns: `references/asking.md`.

A group answer decides its items: write the decision on every item it covers
(`decision`, `decided: owner YYYY-MM-DD`) and the behaviour into `docs/features/<area>.md`
(`../feature/references/area-doc.md`, "Rules"). Keep
asking rounds until every `data: missing` item has a decision and no note says
"unclear". If the owner says "you decide" for a group, decide, write it as yours, and list
it in the progress table so it can be revisited.

## 5. Close the stage

Run the kit's check over everything written, in one run so an id is never used twice
(`scripts/check_inventory.py docs/mvp/<name>/inventory docs/mvp/<name>/requirements`,
whichever exist): only clean output ends the stage. Then load `mvp-plan`.

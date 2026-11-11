# <Epic> · <Feature>

**Status:** planned · **Epic PR:** #… · **Inventory:** LP-XXX-01..12, LP-YYY-03

## What the person can do
Two or three sentences, in the product's words.

## Scope
- Covers: <item ids>.
- Leaves for later: <item ids> — <which feature>.

## Backend
- Models / migrations: …
- Routes: `METHOD /path` — who may call it, what it returns, its refusals (codes).
- Rules: … (link `rules/<epic>.md` entries).
- Outside services: … (stubbed in tests at the port).

## Client
- Stores: … · Screens: … · Design source to port: <board, its CSS/SVG/animation>.
- Words: new keys in every language.

## Impact on what exists
Leave a line out only when it truly does not apply; "none" needs the search that proved it.
- Callers: every module, app and package that uses what this changes (found by search,
  not memory) and what each sees after it.
- API: routes or schemas that change shape, and which clients (web, phone builds already
  in the stores, the other app) still send the old one.
- Data: existing rows and accounts — do they need a backfill, a new default, a move?
- Deploy: does the migration work with the code still running (add before remove)?
  The order of deploys when two services change.
- Behaviour a person already relies on that changes, and whether the owner agreed.
- Suites to run besides this feature's: the other app's, the packages', end-to-end.

## Acceptance criteria
| # | Given | When | Then | Items |
|---|---|---|---|---|
| 1 | a family with two adults | the second taps + | the new-event sheet opens with today | LP-CAL-07 |
| 2 | … | … | … | … |

## Risks and open questions
- …

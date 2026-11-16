# Inventory format — one file per screen

`docs/mvp/<name>/inventory/<SCREEN-ID>.yaml`. The ids are stable for the life of the
MVP: tests, plans and reviews refer to them.

```yaml
id: LP-CAL                       # <APP>-<SCREEN>, capitals and digits
board: P-Calendar                # the design board(s) it comes from
route: /calendar                 # or "sheet from LP-CAL-07", "dialog"
epic: calendar                   # filled in by mvp-plan
review: {at: 2026-11-12, differences: 0}   # filled in by mvp-verify
items:
  - id: LP-CAL-07
    kind: control                # block | control | sheet | state | text | rule
    what: "+ beside the faces"
    does: "opens the new-event sheet with today's date"
    data: have                   # have | missing
    decision: build              # build | cut | later  (empty until decided)
    decided: owner 2026-11-12    # required for missing data, cut and later
    status: todo                 # todo | built | verified | differs
    test: e2e/test_calendar.py   # a file that names the id; required once verified
    note: ""                     # ambiguity, the owner's words, what differs
```

## What is an item

- **block** — a card or section with its heading (it holds texts and controls).
- **control** — anything pressed, typed or swiped: buttons, chips, tabs, fields, toggles,
  links, list rows that open something, drag handles.
- **sheet** — a sheet, dialog or menu a control opens (its own screen file when large).
- **state** — empty, loading, error, filled, long text, offline, a role that sees less.
- **text** — words that carry meaning (a promise, a rule, a legal line, a number's label).
- **rule** — a behaviour the board does not draw (who may, a limit, an error); tested like
  a control.

Write `does` as the observable result: what opens, what changes on screen, what is saved
(it is still there after a reload), where it navigates, what the refusal says. Motion
that carries meaning (the sun crossing the sky by the hour, a progress ring filling) is
an item too.

## Rules

- `data: have` only when a route or field serves it today — name it in `note` if unsure.
- `decision: build` may be set for `have` items without asking; `missing` items wait for
  the owner. `cut` and `later` always carry `decided: owner …`.
- Variants of one board (another language, larger type, another time of day) are states
  of one screen, not screens.
- Boards that are art or rejected alternatives go in `docs/mvp/<name>/not-screens.md`
  with why.

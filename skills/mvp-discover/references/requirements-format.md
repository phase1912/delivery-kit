# Requirements format — the source when there is no design

`docs/mvp/<name>/requirements/<AREA-ID>.yaml` for a project, or
`docs/plans/<YYYY-MM-DD>-<slug>/requirements/<AREA-ID>.yaml` for an epic run by the
`feature` skill. One file per area a person
recognises. It is checked by the same script as an inventory, so the ids are stable,
every item carries a decision, and nothing is called verified without a test naming it.

```yaml
id: BP-FAM                        # <APP>-<AREA>, capitals and digits
source: "owner, chat 2026-11-13; docs/brd.md §4"   # where these come from (no design board)
epic: family                      # filled in when epics are cut
items:
  - id: BP-FAM-03
    kind: rule                    # rule | control | state | text | block
    what: "an adult changes another member's products"
    does: "the change is saved and the member sees it on next load; a child gets 403"
    source: "owner 2026-11-05"    # the item's own source when it differs from the file's
    data: missing                 # have | missing — does the code serve it today
    decision: build               # build | cut | later  (empty until decided)
    decided: owner 2026-11-13     # required for missing data, cut and later
    status: todo                  # todo | built | verified | differs
    test: backend/tests/test_family_products.py   # names the id; required once verified
    note: ""
```

## What is an item

- **rule** — a behaviour: who may do what, a limit, a calculation, what happens on error
  or at a boundary. Most requirements are rules.
- **control**, **state**, **text**, **block** — as in an inventory, when the requirement
  is about something a person sees but no design draws it.

Write `does` as the observable result, the way a test would check it. One behaviour per
item: "and" in `does` usually means two items.

## Where requirements come from

The owner's words (quote them and date them), existing documents (name the section),
the current code (name the file — then it is `data: have`), and the answers you collect.
An item you inferred and nobody confirmed waits for a decision like a missing one.

## Mixed work

When a design draws only some epics, those epics use inventory screens and the rest use
requirement areas — both in the same folder tree, both checked by the same script, and
an epic plan names which it uses.

# Area document — how one area works now

`docs/features/<area>.md`, one per area a person recognises (calendar, family, receipts,
sign-in). Plans say what will change; this says what **is**. It is updated in the same
commit that changes the behaviour, so it is never behind the code. Reviewers and later
plans read it before touching the area.

```markdown
# <Area>

What it is for, in two sentences.

## What a person can do
- <ability> — BP-FAM-03 / LP-CAL-07 · since <plan link>

## Rules
- <rule: who may do what, limits, what happens on error> — BP-FAM-03 · decided <date>

## States and refusals
- empty / error / a role that sees less — what shows, what the person can do next.

## Where it lives
- Backend: routes, services, models (paths). Client: stores, screens (paths).
- Tests: the files that prove the rules above.

## Not built (by the owner's decision)
- <what> — later / cut, <date>, <decision link>

## History
| Date | Plan | What changed |
|---|---|---|
```

Write rules as behaviour, not code. Each line cites its source id, so a question
"why does it do this?" ends at the owner's decision or the design.

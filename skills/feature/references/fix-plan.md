# A fix's plan — the body of its issue

A fix has no plan file: this is its issue, and the reviewer gets the issue's link. Keep
it to what the sections ask; a fix that needs more is a feature.

```markdown
**Level:** fix — <why> · **Status:** analysing

## What is wrong
What the person sees, and what they should see. The owner's words, quoted.

## Cause
Where and why (file:line), found by reading the code, not guessed.

## Acceptance criteria
- [ ] Given …, when …, then … — proof: <test name>
- [ ] Nothing else changes: <the neighbouring behaviour checked>

## Impact
One line: who calls what the fix changes (found by search), or "only <file>".

## Area document
`docs/features/<area>.md` — changed / unchanged (and why).

## Log
- <date>: <from → to, why> (returns to an earlier stage, if any)
```

Tick the criteria with their proof before the pull request; the review result goes in a
comment on the issue.

# Briefs for the reviewers

Each brief is complete on its own: the reviewer knows nothing of the conversation. Give
paths and addresses, not opinions. Ask for the report at a path outside git.

## design-reviewer — first pass

> Review the feature "<feature>" of the MVP "<name>" against its design. Screens:
> `docs/mvp/<name>/inventory/<A>.yaml`, `<B>.yaml` (check every item with
> `decision: build`). Design: <artifact URLs>; saved boards in <folder>. The app runs at
> <address>; sign in as <demo account from the seed script>. Widths: <from stack.md>.
> Write your report to <path>.

## code-reviewer — first pass

> Review the code of the feature "<feature>": `git diff <base>` (uncommitted) or
> `<base>..<head>`. Rules: <the project's rules files>, `docs/mvp/<name>/stack.md`, the
> plan `docs/mvp/<name>/plans/<feature>.md`. Write your report to <path>.

## For the feature skill

Same briefs, without the inventory: the design-reviewer gets the screens the plan
changes and the design they follow; both get the plan `docs/plans/<date>-<slug>.md`
instead of the MVP's files, and the code-reviewer also its "Impact on what exists".

## Re-check (a fresh agent, narrow)

> A first review of "<feature>" found the items listed in <report path>. Fixes are in
> <diff or commits>. For each item say fixed / not fixed / fixed but broke <what>; look
> nowhere else except what the fixes touched. Write to <path>.

## Cost

One first pass of each kind per feature, one narrow re-check per kind that found
something. A third round is a sign the feature was handed over too early: go back to your
own side-by-side before spawning again.

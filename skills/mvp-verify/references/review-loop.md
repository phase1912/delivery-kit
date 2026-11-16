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
> plan `docs/mvp/<name>/plans/<feature>.md`, the area documents it names. Write your
> report to <path>.

## code-reviewer — a fix

> Review the fix in `git diff <base>`. Its plan and acceptance criteria are the issue
> <URL> (read it with `gh issue view`). Rules: <the project's rules files>, the stack
> file. Area document: `docs/features/<area>.md`. Write your report to <path>.

## code-reviewer — a feature or an epic's feature (feature skill)

> Review the code of "<feature>": `git diff <base>` or `<base>..<head>`. Plan:
> `docs/plans/<date>-<slug>.md` (or `<epic folder>/<n>-<feature>.md`), its acceptance
> criteria and "Impact on what exists". Rules: <the project's rules files>, the stack
> file. Area documents: <the ones the plan names>. Write your report to <path>.

The design-reviewer brief is the same as above, with the screens the plan changes and
the design they follow instead of inventory files when there are none.

## Re-check (a fresh agent, narrow)

> A first review of "<feature>" found the items listed in <report path>. Fixes are in
> <diff or commits>. For each item say fixed / not fixed / fixed but broke <what>; look
> nowhere else except what the fixes touched. Write to <path>.

## Cost

One first pass of each kind per feature, one narrow re-check per kind that found
something. A third round is a sign the feature was handed over too early: go back to your
own side-by-side before spawning again.

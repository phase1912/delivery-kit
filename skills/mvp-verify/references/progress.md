# The progress artifact

One page the owner opens instead of asking "where are we". Publish it once (an Artifact,
if the environment has them; otherwise a page in the project's docs) and update the same
page at every status change of a feature (planned, building, verifying, done) — same
file, same address. Used for an epic run by the `feature` skill too: then the top shows
the epic, and the rest its features.

## What it shows

- **Top:** the MVP's name, the design links, epics done / total, features done / total,
  and the next feature.
- **Per epic:** its PR (link, state), its end-to-end scenarios with their state, its
  features with status, and for each feature, on click: **its acceptance criteria
  themselves** (given / when / then, ticked with their proof, open ones visible), the
  review result (differences and findings fixed), and the screens as design / app
  thumbnails at the phone width (wider ones on click). A count alone ("6 of 6") is not
  enough: the owner checks the criteria, not the number.
- **Decided by the owner:** cuts and laters with the date — and any group the owner left
  to you, marked so it can be revisited.
- **Open questions** waiting for the owner, if any.

## How

Keep the page's data in one JSON file beside it (features, statuses, image paths) and
render the table from it, so an update is a data change, not a rewrite. Small screenshots
(phone width, compressed) keep the page light; never put personal data from real accounts
in it — demo data only.

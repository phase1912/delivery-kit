# Stack file — example (FastAPI + PostgreSQL, React + MobX + Tailwind, Capacitor)

A project's `docs/mvp/<name>/stack.md` answers these headings. This one is from a
monorepo with two apps sharing packages; replace every line with the project's own.

## Run it locally
- Database: `docker compose up -d` in the app folder (Postgres on its own port).
- API: `cd backend && uv run uvicorn app.main:app --port <free port>`; never a port the
  owner's live preview uses.
- Client: `cd frontend && VITE_API_BASE_URL=http://localhost:<api> npx vite --port <free>`.
- Seed: `cd backend && uv run python -m scripts.seed_demo` (idempotent; demo accounts in
  the script).

## Checks before a commit
- Backend: `uv run ruff format && uv run ruff check . && uv run mypy . && uv run pytest -q`.
- Frontend: `npm run format:write && npm run lint && npx tsc -b && npx vitest run`.
- Repository: size limits, one copy of shared libraries, generated API types up to date.

## Browser tests
- Playwright, one test per inventory control, named by its id
  (`test_LP_CAL_07_add_event_opens_sheet`), against the seeded local stack.

## Widths and devices
- 375, 768, 1280 px; phone first (base classes are the phone).
- iOS simulator and Android emulator for every feature that touches the keyboard, the
  camera, safe areas, back gestures or permissions.

## Layers and rules
- Backend: router → service → repository → models; domain errors mapped once.
- Frontend: a store fetches and owns state, a component renders; words in all locales;
  colours and spacing from tokens.
- Shared code moves to a package when the second app needs it.

## Commits and PRs
- One PR per epic, one commit per feature; imperative subject, body says why.
- `main` is never pushed to; merged only with green CI.

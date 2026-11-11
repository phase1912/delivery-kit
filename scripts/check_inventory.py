#!/usr/bin/env python3
"""Check an MVP's inventory: what the design draws, what is built, tested and reviewed.

The mvp skills list every screen, state and control of a design in
`docs/mvp/<name>/inventory/<SCREEN-ID>.yaml` before code is written. This keeps the list
honest: no item without a decision, no cut without the owner, no control called verified
without a browser test that names it, and — with --strict, before a feature or the MVP
is said to match the design — nothing built left unverified and no screen unreviewed.

    check_inventory.py docs/mvp/planner/inventory
    check_inventory.py --strict --screens LP-CAL,LP-CALSHEET docs/mvp/planner/inventory

Test paths are read from the project root (--root, default the current directory).
Needs PyYAML.
"""

from __future__ import annotations

import argparse
import re
import sys
from collections import Counter
from pathlib import Path
from typing import Any

import yaml

KINDS = {"block", "control", "sheet", "state", "text"}
DECISIONS = {"build", "cut", "later"}
STATUSES = {"todo", "built", "verified", "differs"}
TESTED_KINDS = {"control", "sheet", "state"}
ID = re.compile(r"^[A-Z][A-Z0-9]*(-[A-Z0-9]+)+$")


def _decision_problems(iid: str, item: dict[str, Any]) -> list[str]:
    """An item needs a decision; missing data, cuts and laters need the owner's."""
    decision = item.get("decision")
    by_owner = str(item.get("decided", "")).startswith("owner")
    if not decision:
        if item.get("data") == "missing":
            return [f"{iid}: waits for the owner's decision (build, cut or later)"]
        return [f"{iid}: no decision (build, cut or later)"]
    if decision not in DECISIONS:
        return [f"{iid}: decision must be one of {sorted(DECISIONS)}"]
    if (item.get("data") == "missing" or decision != "build") and not by_owner:
        return [f"{iid}: {decision} needs the owner's decision (decided: owner <date>)"]
    return []


def _test_problems(iid: str, test: object, root: Path) -> list[str]:
    """A verified control needs a test file that names its id."""
    if not test:
        return [f"{iid}: verified without a browser test (test: <file>)"]
    path = root / str(test).split("::")[0]
    if not path.is_file():
        return [f"{iid}: its test {test} does not exist"]
    text = path.read_text(encoding="utf-8")
    if iid not in text and iid.replace("-", "_") not in text:
        return [f"{iid}: {test} never names {iid}"]
    return []


def item_problems(
    item: dict[str, Any], seen: set[str], strict: bool, root: Path
) -> list[str]:
    """What is wrong with one item; `seen` collects ids to catch duplicates."""
    iid = str(item.get("id", "?"))
    out: list[str] = []
    if not ID.match(iid):
        out.append(f"{iid}: id must look like LP-CAL-07")
    if iid in seen:
        out.append(f"{iid}: the id is used twice")
    seen.add(iid)
    if item.get("kind") not in KINDS:
        out.append(f"{iid}: kind must be one of {sorted(KINDS)}")
    if not item.get("what") or not item.get("does"):
        out.append(f"{iid}: says neither what it is nor what it does")
    out.extend(_decision_problems(iid, item))
    status = item.get("status", "todo")
    if status not in STATUSES:
        out.append(f"{iid}: status must be one of {sorted(STATUSES)}")
    if status == "verified" and item.get("kind") in TESTED_KINDS:
        out.extend(_test_problems(iid, item.get("test"), root))
    if strict and item.get("decision") == "build" and status != "verified":
        out.append(f"{iid}: to be built but {status}, not verified")
    return out


def problems(
    screens: list[dict[str, Any]], strict: bool, root: Path
) -> tuple[list[str], Counter[str]]:
    """Every problem of these screens, and how many items to build stand at each status."""
    out: list[str] = []
    counts: Counter[str] = Counter()
    seen: set[str] = set()
    for screen in screens:
        sid = str(screen.get("id", "?"))
        if not screen.get("board") or not screen.get("items"):
            out.append(f"{sid}: a screen names its design board and lists its items")
        for item in screen.get("items") or []:
            out.extend(item_problems(item, seen, strict, root))
            if item.get("decision") == "build":
                counts[item.get("status", "todo")] += 1
        review = screen.get("review") or {}
        if strict and (not review.get("at") or review.get("differences") != 0):
            out.append(f"{sid}: no review with zero differences")
    return out, counts


def load_screens(path: Path) -> list[dict[str, Any]]:
    """A folder of screen files, one screen file, or a file holding `screens:`."""
    files = sorted(path.glob("*.yaml")) if path.is_dir() else [path]
    screens: list[dict[str, Any]] = []
    for file in files:
        data = yaml.safe_load(file.read_text(encoding="utf-8")) or {}
        screens.extend(data.get("screens", [data]))
    return screens


def main() -> int:
    """Check the inventory named; print a tally and every problem."""
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("inventory", type=Path, help="the inventory folder or a file")
    parser.add_argument(
        "--strict", action="store_true", help="matches the design is said"
    )
    parser.add_argument("--screens", default="", help="only these screen ids, by comma")
    parser.add_argument(
        "--root", type=Path, default=Path.cwd(), help="the project root"
    )
    args = parser.parse_args()
    screens = load_screens(args.inventory)
    if args.screens:
        wanted = set(args.screens.split(","))
        screens = [s for s in screens if s.get("id") in wanted]
    found, counts = problems(screens, args.strict, args.root)
    tally = (
        ", ".join(f"{n} {s}" for s, n in sorted(counts.items())) or "nothing to build"
    )
    print(f"{args.inventory}: {len(screens)} screens; to build: {tally}")
    for line in found:
        print(f"  {line}")
    return 1 if found else 0


if __name__ == "__main__":
    sys.exit(main())

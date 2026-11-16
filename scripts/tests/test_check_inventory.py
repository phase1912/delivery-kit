"""The inventory check refuses what would let "matches the design" be said untrue."""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path
from typing import Any

import yaml

SCRIPT = Path(__file__).resolve().parent.parent / "check_inventory.py"
spec = importlib.util.spec_from_file_location("check_inventory", SCRIPT)
assert spec and spec.loader
check = importlib.util.module_from_spec(spec)
sys.modules["check_inventory"] = check
spec.loader.exec_module(check)

HERE = Path(__file__).resolve().parent
TEST_FILE = Path(__file__).name  # this file names LP-CAL-07 below; read from HERE


def screen(**item: Any) -> dict[str, Any]:
    """One screen with one item: a built, verified, reviewed control unless overridden."""
    base = {
        "id": "LP-CAL-07",
        "kind": "control",
        "what": "+ beside the faces",
        "does": "opens the new-event sheet",
        "data": "have",
        "decision": "build",
        "status": "verified",
        "test": TEST_FILE,
    }
    base.update(item)
    return {
        "id": "LP-CAL",
        "board": "P-Calendar",
        "review": {"at": "2026-11-12", "differences": 0},
        "items": [base],
    }


def run(strict: bool = False, **item: Any) -> list[str]:
    found, _ = check.problems([screen(**item)], strict, HERE)
    return list(found)


def test_a_verified_tested_reviewed_item_passes_strict() -> None:
    found, counts = check.problems([screen()], True, HERE)
    assert found == []
    assert counts["verified"] == 1


def test_missing_data_waits_for_the_owner_with_one_line() -> None:
    found = run(data="missing", decision=None, status="todo")
    assert found == ["LP-CAL-07: waits for the owner's decision (build, cut or later)"]


def test_a_cut_or_a_built_missing_item_needs_the_owner() -> None:
    assert any("owner" in line for line in run(decision="cut", status="todo"))
    assert any("owner" in line for line in run(data="missing"))
    assert run(decision="cut", status="todo", decided="owner 2026-11-12") == []


def test_a_verified_control_needs_a_test_that_names_it() -> None:
    assert any("without a browser test" in line for line in run(test=None))
    assert any("never names" in line for line in run(id="LP-CAL-" + "99"))
    assert any("does not exist" in line for line in run(test="nowhere.py"))


def test_strict_refuses_unverified_and_unreviewed() -> None:
    assert run(status="built") == []
    assert any("not verified" in line for line in run(strict=True, status="built"))
    unreviewed = screen()
    unreviewed["review"] = {"at": "2026-11-12", "differences": 2}
    found, _ = check.problems([unreviewed], True, HERE)
    assert any("review" in line for line in found)


def test_duplicate_ids_and_bad_kinds_are_refused() -> None:
    one = screen(kind="button")
    one["items"].append(dict(one["items"][0]))
    found, _ = check.problems([one], False, HERE)
    assert any("used twice" in line for line in found)
    assert any("kind must be" in line for line in found)


def test_a_folder_of_screen_files_and_a_single_file_load_alike(tmp_path: Path) -> None:
    (tmp_path / "LP-CAL.yaml").write_text(yaml.safe_dump(screen()), encoding="utf-8")
    (tmp_path / "LP-FAM.yaml").write_text(
        yaml.safe_dump({**screen(), "id": "LP-FAM"}), encoding="utf-8"
    )
    assert [s["id"] for s in check.load_screens(tmp_path)] == ["LP-CAL", "LP-FAM"]
    whole = tmp_path / "all.yml"
    whole.write_text(yaml.safe_dump({"screens": [screen()]}), encoding="utf-8")
    assert [s["id"] for s in check.load_screens(whole)] == ["LP-CAL"]


def requirement_area(**item: Any) -> dict[str, Any]:
    """A requirements area (no design board): one verified rule unless overridden."""
    area = screen(kind="rule", what="an adult changes a member's products", **item)
    del area["board"]
    del area["review"]  # requirements have no design review
    area["source"] = "owner, chat 2026-11-13"
    return area


def test_a_requirement_area_with_a_source_passes_like_a_screen() -> None:
    found, _ = check.problems([requirement_area()], True, HERE)
    assert found == []


def test_a_verified_rule_needs_a_test_that_names_it() -> None:
    found, _ = check.problems([requirement_area(test=None)], False, HERE)
    assert found == ["LP-CAL-07: verified without a test (test: <file>)"]


def test_an_area_without_a_board_or_a_source_is_refused() -> None:
    area = requirement_area()
    del area["source"]
    found, _ = check.problems([area], False, HERE)
    assert any("names its design board or source" in line for line in found)


def test_a_drawn_screen_still_needs_its_design_review_in_strict() -> None:
    drawn = screen()
    del drawn["review"]
    found, _ = check.problems([drawn], True, HERE)
    assert found == ["LP-CAL: no review with zero differences"]


def test_an_id_in_both_an_inventory_and_requirements_is_caught(tmp_path: Path) -> None:
    (tmp_path / "inventory").mkdir()
    (tmp_path / "requirements").mkdir()
    (tmp_path / "inventory" / "LP-CAL.yaml").write_text(yaml.safe_dump(screen()))
    (tmp_path / "requirements" / "LP-FAM.yaml").write_text(
        yaml.safe_dump({**requirement_area(), "id": "LP-FAM"})
    )
    both = [
        s
        for folder in ("inventory", "requirements")
        for s in check.load_screens(tmp_path / folder)
    ]
    found, _ = check.problems(both, False, HERE)
    assert "LP-CAL-07: the id is used twice" in found


def test_strict_on_a_feature_s_own_items_ignores_the_area_s_later_ones() -> None:
    area = requirement_area()
    area["items"].append({**area["items"][0], "id": "LP-CAL-08", "status": "todo"})
    whole, _ = check.problems([area], True, HERE)
    assert whole == ["LP-CAL-08: to be built but todo, not verified"]
    mine, _ = check.problems(check.select([area], "", "LP-CAL-07"), True, HERE)
    assert mine == []


def test_main_checks_several_folders_and_names_a_missing_one(
    tmp_path: Path, monkeypatch: Any, capsys: Any
) -> None:
    (tmp_path / "inventory").mkdir()
    (tmp_path / "inventory" / "LP-CAL.yaml").write_text(yaml.safe_dump(screen()))
    argv = ["check", str(tmp_path / "inventory"), str(tmp_path / "nope")]
    monkeypatch.setattr(sys, "argv", argv)
    assert check.main() == 2
    assert "no such folder or file" in capsys.readouterr().out
    argv = ["check", "--root", str(HERE), str(tmp_path / "inventory")]
    monkeypatch.setattr(sys, "argv", argv)
    assert check.main() == 0

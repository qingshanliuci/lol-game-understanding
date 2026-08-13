#!/usr/bin/env python3
"""Validate repository structure, links, ledger fields, and public-file hygiene."""

from __future__ import annotations

import csv
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "README.md",
    "docs/methodology.md",
    "tier-lists/current.md",
    "tier-lists/roles/2026-08-13-LCK.md",
    "tier-lists/roles/2026-08-13-LPL.md",
    "composition-tiers/current.md",
    "knowledge-ledger/claims.csv",
]
LEDGER_FIELDS = [
    "id",
    "date",
    "category",
    "scope",
    "claim",
    "status",
    "confidence",
    "evidence",
    "counterevidence",
    "next_test",
]
ALLOWED_STATUS = {"provisional", "supported", "falsified"}
ALLOWED_CONFIDENCE = {"low", "medium", "high"}
REQUIRED_ROLES = {"上路", "打野", "中路", "AD", "辅助"}
LOCAL_PATH = re.compile(r"/(?:Users|home)/[^\s)`]+")
MD_LINK = re.compile(r"\[[^]]+\]\(([^)]+)\)")


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def main() -> int:
    errors: list[str] = []
    for rel in REQUIRED:
        if not (ROOT / rel).is_file():
            fail(errors, f"missing required file: {rel}")

    for path in ROOT.rglob("*.md"):
        text = path.read_text(encoding="utf-8")
        rel = path.relative_to(ROOT)
        if LOCAL_PATH.search(text):
            fail(errors, f"local absolute path leaked: {rel}")
        for target in MD_LINK.findall(text):
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            clean = target.split("#", 1)[0]
            if clean and not (path.parent / clean).resolve().exists():
                fail(errors, f"broken markdown link: {rel} -> {target}")

    for rel in (
        "tier-lists/roles/2026-08-13-LCK.md",
        "tier-lists/roles/2026-08-13-LPL.md",
    ):
        path = ROOT / rel
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        missing_roles = [role for role in REQUIRED_ROLES if role not in text]
        if missing_roles:
            fail(errors, f"role audit incomplete: {rel} missing {missing_roles}")
        for marker in ("T0", "T0.5", "Counter", "逆风", "陷阱"):
            if marker not in text:
                fail(errors, f"role audit missing marker: {rel} -> {marker}")

    comp_tiers = ROOT / "composition-tiers/current.md"
    if comp_tiers.exists():
        text = comp_tiers.read_text(encoding="utf-8")
        for marker in ("T0", "T0.5", "T1", "陷阱", "逆风", "Counter"):
            if marker not in text:
                fail(errors, f"composition tiers missing marker: {marker}")

    ledger = ROOT / "knowledge-ledger/claims.csv"
    if ledger.exists():
        with ledger.open(encoding="utf-8", newline="") as handle:
            rows = list(csv.DictReader(handle))
        fields = list(rows[0].keys()) if rows else []
        if fields != LEDGER_FIELDS:
            fail(errors, f"ledger fields mismatch: {fields}")
        ids: set[str] = set()
        for number, row in enumerate(rows, start=2):
            if row["id"] in ids:
                fail(errors, f"duplicate claim id at row {number}: {row['id']}")
            ids.add(row["id"])
            if row["status"] not in ALLOWED_STATUS:
                fail(errors, f"invalid status at row {number}: {row['status']}")
            if row["confidence"] not in ALLOWED_CONFIDENCE:
                fail(errors, f"invalid confidence at row {number}: {row['confidence']}")
            if not all(row.get(field, "").strip() for field in LEDGER_FIELDS):
                fail(errors, f"blank ledger field at row {number}")

    if errors:
        print("VALIDATION FAILED")
        for error in errors:
            print(f"- {error}")
        return 1
    print("VALIDATION OK")
    print(f"markdown_files={sum(1 for _ in ROOT.rglob('*.md'))}")
    print(f"claims={len(rows) if ledger.exists() else 0}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

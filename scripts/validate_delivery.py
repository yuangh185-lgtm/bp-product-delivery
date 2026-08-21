#!/usr/bin/env python3
"""Validate a BP product delivery directory or traceability CSV."""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from pathlib import Path


EXPECTED_GROUPS = {
    "requirement baseline": ("01-requirement-baseline.md",),
    "PRD": ("02-prd.md", "02-prd.docx"),
    "process and rules": ("03-process-and-rules.md",),
    "prototype": ("04-prototype", "04-prototype.html"),
    "data design": ("05-data-design.md",),
    "Oracle DDL": ("06-oracle.sql",),
    "OpenAPI": ("07-openapi.yaml", "07-openapi.yml"),
    "test cases": ("08-test-cases.csv", "08-test-cases.xlsx"),
    "acceptance": ("09-acceptance.md",),
    "traceability": ("10-traceability.csv", "10-traceability.xlsx"),
    "manifest": ("delivery-manifest.json",),
}

TRACE_COLUMNS = {
    "requirement_id",
    "design_ref",
    "implementation_ref",
    "test_case_id",
    "acceptance_id",
    "status",
}

PLACEHOLDER_PATTERNS = (
    re.compile(r"\[待(?:确认|补充)\]"),
    re.compile(r"\b(?:TODO|TBD|FIXME)\b", re.IGNORECASE),
    re.compile(r"replace-with-", re.IGNORECASE),
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate full manufacturing delivery packages or traceability CSV files."
    )
    parser.add_argument("target", type=Path, help="Delivery directory or traceability CSV")
    parser.add_argument(
        "--profile",
        choices=("full", "traceability"),
        default="full",
        help="Validation profile (default: full)",
    )
    return parser.parse_args()


def validate_traceability(path: Path) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    if not path.is_file():
        return [f"Traceability file not found: {path}"], warnings
    if path.suffix.lower() != ".csv":
        return errors, [f"Skipped row validation for non-CSV traceability file: {path.name}"]

    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        headers = set(reader.fieldnames or [])
        missing = sorted(TRACE_COLUMNS - headers)
        if missing:
            errors.append(f"Traceability columns missing: {', '.join(missing)}")
            return errors, warnings

        seen: set[tuple[str, str, str]] = set()
        row_count = 0
        for number, row in enumerate(reader, start=2):
            row_count += 1
            req = (row.get("requirement_id") or "").strip()
            tc = (row.get("test_case_id") or "").strip()
            ac = (row.get("acceptance_id") or "").strip()
            if not re.fullmatch(r"REQ-\d{3,}", req):
                errors.append(f"Row {number}: invalid requirement_id '{req}'")
            if tc and not re.fullmatch(r"TC-\d{3,}", tc):
                errors.append(f"Row {number}: invalid test_case_id '{tc}'")
            if ac and not re.fullmatch(r"AC-\d{3,}", ac):
                errors.append(f"Row {number}: invalid acceptance_id '{ac}'")
            key = (req, tc, ac)
            if key in seen:
                warnings.append(f"Row {number}: duplicate traceability link {key}")
            seen.add(key)
        if row_count == 0:
            warnings.append("Traceability file contains headers but no mappings")
    return errors, warnings


def scan_placeholders(root: Path) -> list[str]:
    warnings: list[str] = []
    text_suffixes = {".md", ".txt", ".csv", ".yaml", ".yml", ".json", ".sql", ".html"}
    for path in root.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in text_suffixes:
            continue
        try:
            content = path.read_text(encoding="utf-8-sig")
        except UnicodeDecodeError:
            warnings.append(f"Could not decode as UTF-8: {path.relative_to(root)}")
            continue
        for pattern in PLACEHOLDER_PATTERNS:
            if pattern.search(content):
                warnings.append(f"Unresolved placeholder in {path.relative_to(root)}")
                break
    return warnings


def validate_full(root: Path) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    if not root.is_dir():
        return [f"Delivery directory not found: {root}"], warnings

    manifest = root / "delivery-manifest.json"
    manifest_data: dict = {}
    if manifest.is_file() and manifest.stat().st_size:
        try:
            parsed = json.loads(manifest.read_text(encoding="utf-8-sig"))
            if isinstance(parsed, dict):
                manifest_data = parsed
            else:
                errors.append("delivery-manifest.json must contain a JSON object")
        except (UnicodeDecodeError, json.JSONDecodeError) as exc:
            errors.append(f"Invalid delivery-manifest.json: {exc}")

    omitted: set[str] = set()
    for item in manifest_data.get("omittedArtifacts", []):
        if isinstance(item, str):
            omitted.add(item)
        elif isinstance(item, dict):
            for key in ("path", "name", "type"):
                value = item.get(key)
                if isinstance(value, str):
                    omitted.add(value)

    for label, alternatives in EXPECTED_GROUPS.items():
        matches = [root / name for name in alternatives if (root / name).exists()]
        if not matches:
            if label in omitted or any(name in omitted for name in alternatives):
                warnings.append(f"Artifact group intentionally omitted: {label}")
            else:
                errors.append(f"Missing artifact group: {label} ({' or '.join(alternatives)})")
            continue
        for match in matches:
            if match.is_file() and match.stat().st_size == 0:
                errors.append(f"Empty artifact: {match.name}")
            elif match.is_dir() and not any(match.iterdir()):
                warnings.append(f"Artifact directory is empty: {match.name}")

    trace_csv = root / "10-traceability.csv"
    if trace_csv.exists():
        trace_errors, trace_warnings = validate_traceability(trace_csv)
        errors.extend(trace_errors)
        warnings.extend(trace_warnings)
    elif (root / "10-traceability.xlsx").exists():
        warnings.append("Traceability XLSX exists; validate its columns in the spreadsheet workflow")

    warnings.extend(scan_placeholders(root))
    return errors, warnings


def main() -> int:
    args = parse_args()
    if args.profile == "traceability":
        errors, warnings = validate_traceability(args.target)
    else:
        errors, warnings = validate_full(args.target)

    for message in errors:
        print(f"ERROR: {message}")
    for message in warnings:
        print(f"WARNING: {message}")
    if errors:
        print(f"FAILED: {len(errors)} error(s), {len(warnings)} warning(s)")
        return 1
    print(f"PASSED: 0 errors, {len(warnings)} warning(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())

"""Validate the public workbook and create a deterministic analysis-ready CSV."""

from __future__ import annotations

import argparse
import hashlib
from pathlib import Path

import pandas as pd


REQUIRED_COLUMNS = {
    "record_id",
    "stratum",
    "owner",
    "repository_url",
    "risk_governance_observed",
    "access_control_observed",
    "source_code_protection_observed",
    "traceability_observed",
    "observed_overall",
}
DIMENSIONS = [
    "risk_governance_observed",
    "access_control_observed",
    "source_code_protection_observed",
    "traceability_observed",
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--input",
        type=Path,
        default=Path("data/raw/public_repo_security_peru_benchmark.xlsx"),
        help="Public source workbook.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("data/public_repo_security_benchmark.csv"),
        help="Derived CSV path.",
    )
    parser.add_argument("--sheet", default="Datos_repositorios", help="Workbook sheet to read.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    frame = pd.read_excel(args.input, sheet_name=args.sheet)
    missing = REQUIRED_COLUMNS.difference(frame.columns)
    if missing:
        raise ValueError(f"The source workbook is missing required columns: {sorted(missing)}")

    if len(frame) != 48:
        raise ValueError(f"Expected 48 public repositories; found {len(frame)}.")
    if set(frame["stratum"].dropna().unique()) != {"Peru", "International benchmark"}:
        raise ValueError("The source workbook must contain the Peru and International benchmark strata.")
    if frame["record_id"].duplicated().any() or frame["repository_url"].duplicated().any():
        raise ValueError("Record identifiers and repository URLs must be unique.")

    for column in DIMENSIONS + ["observed_overall"]:
        frame[column] = pd.to_numeric(frame[column], errors="raise")
        if not frame[column].between(0, 10).all():
            raise ValueError(f"{column} must remain on the documented 0-10 observed scale.")

    # Keep every original public indicator so later checks can be traced to the workbook.
    frame = frame.sort_values("record_id").reset_index(drop=True)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    frame.to_csv(args.output, index=False, float_format="%.6f")

    digest = hashlib.sha256(args.output.read_bytes()).hexdigest()
    print(f"Created {args.output} with {len(frame)} repositories.")
    print(f"SHA256: {digest}")


if __name__ == "__main__":
    main()

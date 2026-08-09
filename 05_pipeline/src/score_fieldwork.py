"""Validate and score survey exports without exposing protected fieldwork data."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path

import pandas as pd
import yaml


ROOT = Path(__file__).resolve().parents[1]
IDENTIFIER_PATTERN = re.compile(r"^[A-Za-z0-9_-]{1,32}$")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--params", type=Path, default=ROOT / "params.yaml")
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=ROOT / "fieldwork" / "private_output",
    )
    parser.add_argument(
        "--synthetic",
        action="store_true",
        help="Require an explicit synthetic-data marker and label all outputs as synthetic.",
    )
    return parser.parse_args()


def validate_identifiers(frame: pd.DataFrame, column: str) -> None:
    invalid = frame.loc[~frame[column].map(lambda value: bool(IDENTIFIER_PATTERN.fullmatch(value))), column]
    if not invalid.empty:
        raise ValueError(f"{column} contains missing or unsafe identifiers: {invalid.index.tolist()}")


def parse_items(
    frame: pd.DataFrame,
    item_names: list[str],
    missing_tokens: set[str],
) -> pd.DataFrame:
    parsed = pd.DataFrame(index=frame.index)
    for item in item_names:
        text = frame[item].astype("string").str.strip()
        missing = text.isna() | text.str.lower().isin(missing_tokens)
        numeric = pd.to_numeric(text.where(~missing), errors="coerce")
        invalid = ~missing & (numeric.isna() | ~numeric.isin([1, 2, 3, 4, 5]))
        if invalid.any():
            rows = (frame.index[invalid] + 2).tolist()
            raise ValueError(f"{item} contains a value outside 1 to 5 on CSV row(s) {rows}")
        parsed[item] = numeric.astype(float)
    return parsed


def summarize_group(
    label: str,
    organization_count: int,
    frame: pd.DataFrame,
    score_columns: list[str],
    reporting_scope: str,
    expose_scores: bool = True,
) -> dict[str, object]:
    row: dict[str, object] = {
        "organization_code": label,
        "organization_count": organization_count,
        "participant_count": len(frame),
        "reporting_scope": reporting_scope,
    }
    for score in score_columns:
        eligible = int(frame[score].notna().sum())
        row[f"{score}_eligible_n"] = eligible if expose_scores else ""
        row[f"{score}_mean"] = float(frame[score].mean()) if expose_scores and eligible else ""
    return row


def main() -> None:
    args = parse_args()
    params = yaml.safe_load(args.params.read_text(encoding="utf-8"))
    scoring = params["fieldwork_scoring"]
    dimensions = scoring["dimensions"]
    item_names = [item for definition in dimensions.values() for item in definition["items"]]
    if len(item_names) != len(set(item_names)):
        raise ValueError("An instrument item appears in more than one scoring dimension.")

    frame = pd.read_csv(args.input, dtype=str, keep_default_na=False)
    required = {"participant_code", "organization_code", *item_names}
    missing_columns = sorted(required.difference(frame.columns))
    if missing_columns:
        raise ValueError(f"Input is missing required columns: {', '.join(missing_columns)}")
    if frame.empty:
        raise ValueError("Input contains no survey records.")
    if frame["participant_code"].duplicated().any():
        raise ValueError("participant_code must be unique within the scoring file.")
    validate_identifiers(frame, "participant_code")
    validate_identifiers(frame, "organization_code")
    for column, allowed_values in scoring.get("context_fields", {}).items():
        if column not in frame:
            continue
        values = frame[column].str.strip()
        invalid = values.ne("") & ~values.isin(allowed_values)
        if invalid.any():
            rows = (frame.index[invalid] + 2).tolist()
            raise ValueError(f"{column} contains an unapproved category on CSV row(s) {rows}")
    if args.synthetic:
        if "synthetic_record" not in frame or not frame["synthetic_record"].str.lower().eq("true").all():
            raise ValueError("Synthetic runs require synthetic_record=true for every row.")

    parsed = parse_items(
        frame,
        item_names,
        {str(token).strip().lower() for token in scoring["missing_tokens"]},
    )
    identity_columns = [
        column
        for column in [
            "participant_code",
            "organization_code",
            "role_group",
            "experience_group",
            "company_size_group",
            "delivery_approach",
            "synthetic_record",
        ]
        if column in frame
    ]
    scored = frame[identity_columns].copy()
    risk_dimension_scores: list[str] = []
    outcome_scores: list[str] = []
    for name, definition in dimensions.items():
        items = definition["items"]
        answered_column = f"{name}_answered"
        score_column = f"{name}_score"
        answered = parsed[items].notna().sum(axis=1)
        scored[answered_column] = answered
        scored[score_column] = parsed[items].mean(axis=1).where(
            answered >= int(definition["minimum_answered"])
        )
        if definition["construct"] == "risk_management_maturity":
            risk_dimension_scores.append(score_column)
        else:
            outcome_scores.append(score_column)

    scored["risk_dimensions_answered"] = scored[risk_dimension_scores].notna().sum(axis=1)
    scored["risk_management_maturity"] = scored[risk_dimension_scores].mean(axis=1).where(
        scored["risk_dimensions_answered"] >= int(scoring["minimum_risk_dimensions"])
    )
    for dimension_score in outcome_scores:
        public_name = dimension_score.removesuffix("_score")
        scored[public_name] = scored[dimension_score]

    score_columns = [
        "risk_management_maturity",
        "access_control_effectiveness",
        "source_code_protection",
        "development_traceability",
    ]
    minimum_group_size = int(scoring["minimum_organization_size_for_reporting"])
    scope = "synthetic demonstration only" if args.synthetic else "restricted exploratory fieldwork"
    organization_groups = list(scored.groupby("organization_code", sort=True))
    small_groups = [group for _, group in organization_groups if len(group) < minimum_group_size]
    summary_rows = [
        summarize_group(
            "ALL_PARTICIPANTS",
            len(organization_groups),
            scored,
            score_columns,
            scope,
        )
    ]
    if small_groups:
        # Publishing the large groups beside the overall mean could reveal the
        # small group's mean by subtraction, so the whole breakdown is withheld.
        summary_rows.append(
            summarize_group(
                "ORGANIZATION_BREAKDOWN_WITHHELD",
                len(organization_groups),
                scored,
                score_columns,
                scope,
                expose_scores=False,
            )
        )
    else:
        for organization_code, group in organization_groups:
            summary_rows.append(
                summarize_group(organization_code, 1, group, score_columns, scope)
            )

    missingness = pd.DataFrame(
        {
            "item": item_names,
            "answered_count": [int(parsed[item].notna().sum()) for item in item_names],
            "missing_count": [int(parsed[item].isna().sum()) for item in item_names],
            "missing_percent": [float(parsed[item].isna().mean() * 100) for item in item_names],
        }
    )
    suffix = "_synthetic" if args.synthetic else ""
    args.output_dir.mkdir(parents=True, exist_ok=True)
    scored_path = args.output_dir / f"scored_responses{suffix}.csv"
    summary_path = args.output_dir / f"organization_summary{suffix}.csv"
    missingness_path = args.output_dir / f"item_missingness{suffix}.csv"
    metadata_path = args.output_dir / f"scoring_metadata{suffix}.json"
    scored.to_csv(scored_path, index=False, float_format="%.4f", lineterminator="\n")
    pd.DataFrame(summary_rows).to_csv(
        summary_path, index=False, float_format="%.4f", lineterminator="\n"
    )
    missingness.to_csv(
        missingness_path, index=False, float_format="%.2f", lineterminator="\n"
    )
    metadata = {
        "synthetic_data": args.synthetic,
        "input_file": args.input.name,
        "input_sha256": hashlib.sha256(args.input.read_bytes()).hexdigest(),
        "params_file": args.params.name,
        "params_sha256": hashlib.sha256(args.params.read_bytes()).hexdigest(),
        "participant_count": len(scored),
        "organization_count": int(scored["organization_code"].nunique()),
        "minimum_organization_size_for_reporting": minimum_group_size,
        "score_range": [1, 5],
        "outputs": [scored_path.name, summary_path.name, missingness_path.name],
    }
    metadata_path.write_text(
        json.dumps(metadata, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(f"Scored {len(scored)} records. Outputs written to {args.output_dir}.")


if __name__ == "__main__":
    main()

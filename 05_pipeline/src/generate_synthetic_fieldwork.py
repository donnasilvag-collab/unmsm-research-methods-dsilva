"""Generate a deterministic synthetic survey file for scoring tests.

The records do not describe real people or organizations. They exercise the
instrument schema and missing-data rules before protected fieldwork begins.
"""

from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
RISK_ITEMS = [f"RM{index:02d}" for index in range(1, 15)]
ACCESS_ITEMS = [f"AC{index:02d}" for index in range(1, 7)]
SOURCE_ITEMS = [f"SC{index:02d}" for index in range(1, 7)]
TRACE_ITEMS = [f"TR{index:02d}" for index in range(1, 7)]
ALL_ITEMS = RISK_ITEMS + ACCESS_ITEMS + SOURCE_ITEMS + TRACE_ITEMS


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output",
        type=Path,
        default=ROOT / "fieldwork" / "synthetic" / "survey_responses_synthetic.csv",
    )
    parser.add_argument("--seed", type=int, default=20260808)
    return parser.parse_args()


def bounded_score(value: float) -> int:
    return int(np.clip(np.rint(value), 1, 5))


def main() -> None:
    args = parse_args()
    rng = np.random.default_rng(args.seed)
    roles = [
        "Software development",
        "Technical leadership",
        "DevOps or platform",
        "Information security",
        "Quality or testing",
    ]
    experience = ["2 to 5 years", "6 to 10 years", "More than 10 years"]
    delivery = ["Agile", "DevOps or continuous delivery", "Hybrid"]
    organization_specs = [(2.35, 6), (2.90, 6), (3.45, 6), (4.00, 4)]

    records: list[dict[str, object]] = []
    participant_number = 1
    for organization_index, (organization_level, member_count) in enumerate(
        organization_specs, start=1
    ):
        for member_index in range(member_count):
            participant_level = organization_level + rng.normal(0, 0.30)
            record: dict[str, object] = {
                "participant_code": f"SYN_P{participant_number:03d}",
                "organization_code": f"SYN_ORG_{organization_index:02d}",
                "role_group": roles[(participant_number - 1) % len(roles)],
                "experience_group": experience[(participant_number - 1) % len(experience)],
                "company_size_group": ["1 to 49", "50 to 249", "250 or more"][organization_index % 3],
                "delivery_approach": delivery[(organization_index + member_index) % len(delivery)],
                "synthetic_record": "true",
            }
            for item in RISK_ITEMS:
                record[item] = bounded_score(participant_level + rng.normal(0, 0.55))
            for item in ACCESS_ITEMS:
                record[item] = bounded_score(participant_level - 0.10 + rng.normal(0, 0.60))
            for item in SOURCE_ITEMS:
                record[item] = bounded_score(participant_level - 0.20 + rng.normal(0, 0.65))
            for item in TRACE_ITEMS:
                record[item] = bounded_score(participant_level + rng.normal(0, 0.55))
            records.append(record)
            participant_number += 1

    frame = pd.DataFrame(records)
    # These fixed omissions test the minimum-completeness rules without random drift.
    frame.loc[0, ["AC01", "AC02", "AC03"]] = pd.NA
    frame.loc[6, ["SC01", "SC02", "SC03"]] = pd.NA
    frame.loc[12, ["TR01", "TR02", "TR03"]] = pd.NA
    frame.loc[18, ["RM01"]] = pd.NA
    for item in ALL_ITEMS:
        frame[item] = frame[item].astype("Int64")

    args.output.parent.mkdir(parents=True, exist_ok=True)
    frame.to_csv(args.output, index=False, lineterminator="\n")
    print(f"Created {args.output} with {len(frame)} synthetic records.")


if __name__ == "__main__":
    main()

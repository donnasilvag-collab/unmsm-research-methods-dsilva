"""Generate synthetic records for the association-analysis demonstration.

The output represents no person, company, repository, interview, or document.
It contains an intentionally constructed signal so the analysis code can be
tested before authorized fieldwork begins.
"""

from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
import pandas as pd
import yaml

from generate_synthetic_fieldwork import (
    ACCESS_ITEMS,
    RISK_ITEMS,
    SOURCE_ITEMS,
    TRACE_ITEMS,
    bounded_score,
)


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT_DIR = ROOT / "fieldwork" / "synthetic" / "association_demo"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--params", type=Path, default=ROOT / "params.yaml")
    return parser.parse_args()


def item_scores(
    items: list[str],
    center: float,
    rng: np.random.Generator,
    noise: float,
) -> dict[str, int]:
    return {item: bounded_score(center + rng.normal(0, noise)) for item in items}


def build_survey(seed: int, participant_count: int, organization_count: int) -> pd.DataFrame:
    if participant_count % organization_count:
        raise ValueError("Synthetic participants must divide evenly across organizations.")

    rng = np.random.default_rng(seed)
    members_per_organization = participant_count // organization_count
    organization_levels = np.linspace(2.15, 4.05, organization_count)
    roles = [
        "Software development",
        "Technical leadership",
        "DevOps or platform",
        "Quality or testing",
        "Information security",
    ]
    experience = [
        "Less than 2 years",
        "2 to 5 years",
        "6 to 10 years",
        "More than 10 years",
    ]
    delivery = ["Agile", "DevOps or continuous delivery", "Hybrid"]
    company_sizes = ["1 to 49", "50 to 249", "250 or more"]

    records: list[dict[str, object]] = []
    participant_number = 1
    for organization_index, organization_level in enumerate(organization_levels, start=1):
        for member_index in range(members_per_organization):
            individual_maturity = organization_level + rng.normal(0, 0.48)
            experience_index = (participant_number - 1) % len(experience)
            company_size_index = (organization_index - 1) % len(company_sizes)
            access_center = 0.72 + 0.72 * individual_maturity + 0.06 * experience_index
            source_center = 0.62 + 0.70 * individual_maturity + 0.05 * company_size_index
            trace_center = 0.55 + 0.76 * individual_maturity + 0.05 * (member_index % 3)

            record: dict[str, object] = {
                "participant_code": f"SYN_ANALYSIS_P{participant_number:03d}",
                "organization_code": f"SYN_ANALYSIS_ORG_{organization_index:02d}",
                "role_group": roles[(participant_number - 1) % len(roles)],
                "experience_group": experience[experience_index],
                "company_size_group": company_sizes[company_size_index],
                "delivery_approach": delivery[(organization_index + member_index) % len(delivery)],
                "synthetic_record": "true",
            }
            record.update(item_scores(RISK_ITEMS, individual_maturity, rng, 0.68))
            record.update(item_scores(ACCESS_ITEMS, access_center, rng, 0.82))
            record.update(item_scores(SOURCE_ITEMS, source_center, rng, 0.88))
            record.update(item_scores(TRACE_ITEMS, trace_center, rng, 0.78))
            records.append(record)
            participant_number += 1

    return pd.DataFrame(records)


def build_integration_evidence() -> pd.DataFrame:
    rows = [
        {
            "outcome": "access_control_effectiveness",
            "synthetic_interview_pattern": "Fictitious participants describe clearer access reviews when ownership and escalation duties are explicit.",
            "synthetic_document_pattern": "Fictitious review records show partly consistent approval and access-removal evidence.",
            "synthetic_integration_assessment": "Illustrative convergence with qualifications",
        },
        {
            "outcome": "source_code_protection",
            "synthetic_interview_pattern": "Fictitious participants describe stronger repository protection when secure-change checks are part of routine delivery.",
            "synthetic_document_pattern": "Fictitious repository procedures show uneven evidence for secret scanning and dependency review.",
            "synthetic_integration_assessment": "Illustrative partial convergence",
        },
        {
            "outcome": "development_traceability",
            "synthetic_interview_pattern": "Fictitious participants connect traceability with disciplined links among requests, reviews, tests, and deployments.",
            "synthetic_document_pattern": "Fictitious audit samples show that links are easier to retrieve when workflow responsibilities are defined.",
            "synthetic_integration_assessment": "Illustrative convergence",
        },
    ]
    evidence = pd.DataFrame(rows)
    evidence["synthetic_evidence"] = "true"
    return evidence


def main() -> None:
    args = parse_args()
    params = yaml.safe_load(args.params.read_text(encoding="utf-8"))
    demo = params["synthetic_analysis_demo"]
    if demo.get("synthetic_data") is not True:
        raise ValueError("The analysis demonstration must remain explicitly synthetic.")

    survey = build_survey(
        seed=int(demo["seed"]),
        participant_count=int(demo["participant_count"]),
        organization_count=int(demo["organization_count"]),
    )
    evidence = build_integration_evidence()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    survey_path = args.output_dir / "survey_responses_analysis_synthetic.csv"
    evidence_path = args.output_dir / "integration_evidence_synthetic.csv"
    survey.to_csv(survey_path, index=False, lineterminator="\n")
    evidence.to_csv(evidence_path, index=False, lineterminator="\n")
    print(
        f"Created {survey_path} with {len(survey)} synthetic participants and "
        f"{survey['organization_code'].nunique()} synthetic organizations."
    )
    print(f"Created {evidence_path} with {len(evidence)} synthetic integration records.")


if __name__ == "__main__":
    main()

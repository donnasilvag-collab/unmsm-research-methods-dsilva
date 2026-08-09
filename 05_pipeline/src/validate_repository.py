"""Validate research-document consistency and machine-readable review records."""

from __future__ import annotations

import csv
import re
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[2]
TITLE = (
    "Madurez de la gestión de riesgos y eficacia de los controles de "
    "desarrollo seguro en empresas peruanas"
)
REQUIRED_FILES = [
    "03_protocol/operationalization_matrix.md",
    "03_protocol/instruments/survey.md",
    "03_protocol/instruments/interview_guide.md",
    "03_protocol/instruments/document_review_form.md",
    "03_protocol/instruments/validation_procedure.md",
    "04_literature/search_log.csv",
    "04_literature/screening_log.csv",
    "04_literature/quality_appraisal.csv",
    "04_literature/prisma_flow.csv",
    "11_bias_audit/bias_audit_summary.csv",
    "11_bias_audit/owner_influence_diagnostics.csv",
    "12_integrity/ai_use_policy.md",
]
LINK_PATTERN = re.compile(r"!?(?:\[[^\]]*\])\(([^)]+)\)")
ITEM_PATTERN = re.compile(r"\| (RM\d{2}|AC\d{2}|SC\d{2}|TR\d{2}) \|")


def read_csv(relative_path: str) -> list[dict[str, str]]:
    with (ROOT / relative_path).open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def validate_required_files(errors: list[str]) -> None:
    for relative_path in REQUIRED_FILES:
        if not (ROOT / relative_path).is_file():
            errors.append(f"Required file is missing: {relative_path}")


def validate_markdown(errors: list[str]) -> None:
    title_occurrences = 0
    for markdown in ROOT.rglob("*.md"):
        if ".venv" in markdown.parts or ".dvc" in markdown.parts:
            continue
        text = markdown.read_text(encoding="utf-8")
        title_occurrences += text.count(TITLE)
        if "Influencia de la gestión de riesgos" in text:
            errors.append(f"Previous research title remains in {markdown.relative_to(ROOT)}")
        if "\u2014" in text or "\u2013" in text:
            errors.append(f"Em dash or en dash remains in {markdown.relative_to(ROOT)}")
        for target in LINK_PATTERN.findall(text):
            clean_target = target.strip().strip("<>").split("#", maxsplit=1)[0]
            if not clean_target or re.match(r"^(https?|mailto):", clean_target):
                continue
            local_target = (markdown.parent / unquote(clean_target)).resolve()
            if not local_target.exists():
                errors.append(
                    f"Broken Markdown link in {markdown.relative_to(ROOT)}: {target}"
                )
    if title_occurrences < 5:
        errors.append("The controlled research title is not used consistently.")


def validate_survey(errors: list[str]) -> None:
    survey = (ROOT / "03_protocol/instruments/survey.md").read_text(encoding="utf-8")
    items = ITEM_PATTERN.findall(survey)
    unique_items = set(items)
    expected = {
        *(f"RM{index:02d}" for index in range(1, 15)),
        *(f"AC{index:02d}" for index in range(1, 7)),
        *(f"SC{index:02d}" for index in range(1, 7)),
        *(f"TR{index:02d}" for index in range(1, 7)),
    }
    if unique_items != expected or len(items) != 32:
        errors.append(
            f"Survey item set is invalid: found {len(items)} rows and "
            f"{len(unique_items)} unique substantive items."
        )


def validate_prisma(errors: list[str]) -> None:
    rows = read_csv("04_literature/prisma_flow.csv")
    counts = {row["phase"]: int(row["count"]) for row in rows}
    required = {
        "primary_source_records",
        "additional_records",
        "total_identified",
        "duplicates_removed",
        "title_abstract_screened",
        "title_abstract_excluded",
        "full_text_assessed",
        "full_text_excluded",
        "included_qualitative_synthesis",
    }
    if set(counts) != required:
        errors.append("PRISMA flow contains missing or unexpected phases.")
        return
    checks = [
        counts["primary_source_records"] + counts["additional_records"]
        == counts["total_identified"],
        counts["total_identified"] - counts["duplicates_removed"]
        == counts["title_abstract_screened"],
        counts["title_abstract_screened"] - counts["title_abstract_excluded"]
        == counts["full_text_assessed"],
        counts["full_text_assessed"] - counts["full_text_excluded"]
        == counts["included_qualitative_synthesis"],
    ]
    if not all(checks):
        errors.append("PRISMA arithmetic is inconsistent.")


def validate_screening(errors: list[str]) -> None:
    rows = read_csv("04_literature/screening_log.csv")
    included = [row for row in rows if row["decision"] == "Include"]
    excluded = [row for row in rows if row["decision"] == "Exclude"]
    if len(included) != 10 or len(excluded) != 6 or len(rows) != 16:
        errors.append(
            "Screening log must contain 10 included and 6 excluded full texts."
        )
    for row in included:
        identifier = row["identifier"].strip().lower()
        if not identifier.startswith("10."):
            errors.append(f"Included record lacks a DOI: {row['record_id']}")
        if row["publication_status"] != "Published":
            errors.append(f"Included record is not marked Published: {row['record_id']}")
        if not row["status_checked"]:
            errors.append(f"Included record lacks a status-check date: {row['record_id']}")


def validate_quality(errors: list[str]) -> None:
    rows = read_csv("04_literature/quality_appraisal.csv")
    if len(rows) != 10:
        errors.append("Quality appraisal must contain exactly 10 included studies.")
    criteria = [
        "direct_relevance",
        "method_transparency",
        "evidence_basis",
        "reproducibility_trace",
        "transferability",
    ]
    for row in rows:
        scores = [int(row[column]) for column in criteria]
        total = int(row["total"])
        if any(score not in {0, 1, 2} for score in scores) or sum(scores) != total:
            errors.append(f"Invalid quality score for {row['record_id']}")
        expected_rating = "High" if total >= 8 else "Moderate" if total >= 5 else "Contextual only"
        if row["rating"] != expected_rating:
            errors.append(f"Invalid quality rating for {row['record_id']}")


def main() -> None:
    errors: list[str] = []
    validate_required_files(errors)
    validate_markdown(errors)
    validate_survey(errors)
    validate_prisma(errors)
    validate_screening(errors)
    validate_quality(errors)

    if errors:
        details = "\n".join(f"- {error}" for error in errors)
        raise SystemExit(f"Repository validation failed:\n{details}")
    print("Repository validation passed.")


if __name__ == "__main__":
    main()

"""Validate research-document consistency and machine-readable review records."""

from __future__ import annotations

import csv
import hashlib
import json
import re
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[2]
TITLE = (
    "Madurez de la gestión de riesgos y eficacia de los controles de "
    "desarrollo seguro en empresas peruanas"
)
EXPECTED_SECTIONS = {
    "01_paradigm",
    "02_method",
    "03_protocol",
    "04_literature",
    "05_pipeline",
    "06_repro_audit",
    "07_model_card",
    "09_ethics",
    "10_data_mgmt",
    "11_bias_audit",
    "12_integrity",
    "13_presentation",
}
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
    "04_literature/thesis_search_protocol.md",
    "04_literature/database_search_plan.csv",
    "05_pipeline/fieldwork/README.md",
    "05_pipeline/src/generate_synthetic_fieldwork.py",
    "05_pipeline/src/generate_synthetic_analysis.py",
    "05_pipeline/src/analyze_synthetic_fieldwork.py",
    "05_pipeline/src/score_fieldwork.py",
    "05_pipeline/fieldwork/synthetic/survey_responses_synthetic.csv",
    "05_pipeline/fieldwork/synthetic/scored_responses_synthetic.csv",
    "05_pipeline/fieldwork/synthetic/organization_summary_synthetic.csv",
    "05_pipeline/fieldwork/synthetic/item_missingness_synthetic.csv",
    "05_pipeline/fieldwork/synthetic/scoring_metadata_synthetic.json",
    "05_pipeline/fieldwork/synthetic/association_demo/survey_responses_analysis_synthetic.csv",
    "05_pipeline/fieldwork/synthetic/association_demo/integration_evidence_synthetic.csv",
    "05_pipeline/fieldwork/synthetic/association_demo/scored_responses_synthetic.csv",
    "05_pipeline/fieldwork/synthetic/association_demo/organization_summary_synthetic.csv",
    "05_pipeline/fieldwork/synthetic/association_demo/item_missingness_synthetic.csv",
    "05_pipeline/fieldwork/synthetic/association_demo/scoring_metadata_synthetic.json",
    "05_pipeline/fieldwork/synthetic/association_demo/spearman_correlations_synthetic.csv",
    "05_pipeline/fieldwork/synthetic/association_demo/exploratory_regressions_synthetic.csv",
    "05_pipeline/fieldwork/synthetic/association_demo/regression_diagnostics_synthetic.csv",
    "05_pipeline/fieldwork/synthetic/association_demo/integration_joint_display_synthetic.csv",
    "05_pipeline/fieldwork/synthetic/association_demo/analysis_report_synthetic.md",
    "05_pipeline/fieldwork/synthetic/association_demo/analysis_metadata_synthetic.json",
    "05_pipeline/fieldwork/synthetic/association_demo/README.md",
    "05_pipeline/docs/environment.md",
    "05_pipeline/docs/quality_checks.md",
    "05_pipeline/docs/source_manifest.csv",
    "05_pipeline/docs/data_dictionary.csv",
    "05_pipeline/docs/analysis_report.md",
    "05_pipeline/docs/presentation_evidence.md",
    "05_pipeline/docs/public_inspection_sample.md",
    "05_pipeline/docs/reproduction_record.md",
    "06_repro_audit/paper_source.md",
    "11_bias_audit/bias_audit_summary.csv",
    "11_bias_audit/owner_influence_diagnostics.csv",
    "12_integrity/ai_use_policy.md",
    "12_integrity/retraction_source.md",
    "13_presentation/README.md",
    "13_presentation/index.html",
    "13_presentation/assets/unmsm-logo.svg",
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


def validate_structure(errors: list[str]) -> None:
    actual_sections = {
        path.name
        for path in ROOT.iterdir()
        if path.is_dir() and re.fullmatch(r"\d{2}_.+", path.name)
    }
    missing = EXPECTED_SECTIONS.difference(actual_sections)
    unexpected = actual_sections.difference(EXPECTED_SECTIONS)
    if missing:
        errors.append(f"Numbered repository sections are missing: {sorted(missing)}")
    if unexpected:
        errors.append(f"Unexpected numbered repository sections exist: {sorted(unexpected)}")


def validate_pipeline_docs(errors: list[str]) -> None:
    sources = read_csv("05_pipeline/docs/source_manifest.csv")
    expected_source_ids = {f"SRC{index:02d}" for index in range(1, 8)}
    if {row.get("source_id") for row in sources} != expected_source_ids:
        errors.append("The pipeline source manifest does not contain the seven controlled sources.")

    dictionary = read_csv("05_pipeline/docs/data_dictionary.csv")
    documented_variables = {row.get("variable") for row in dictionary}
    required_variables = {
        "stratum",
        "repository_url",
        "risk_governance_observed",
        "access_control_observed",
        "source_code_protection_observed",
        "traceability_observed",
        "observed_overall",
        "git_clone_status",
    }
    if not required_variables.issubset(documented_variables):
        errors.append("The pipeline data dictionary omits a required analytical variable.")

    analysis = (ROOT / "05_pipeline/docs/analysis_report.md").read_text(encoding="utf-8")
    if "Fieldwork has not begun" not in analysis or "does not answer" not in analysis:
        errors.append("The analysis report does not state its fieldwork boundary clearly.")

    environment = (ROOT / "05_pipeline/docs/environment.md").read_text(encoding="utf-8")
    if "Docker remains unverified" not in environment:
        errors.append("The environment record does not preserve the pending Docker status.")


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


def validate_search_plan(errors: list[str]) -> None:
    rows = read_csv("04_literature/database_search_plan.csv")
    expected_sources = {
        "Scopus",
        "Web of Science Core Collection",
        "IEEE Xplore",
        "ACM Digital Library",
        "Semantic Scholar",
    }
    if {row["source"] for row in rows} != expected_sources:
        errors.append("The prospective thesis search plan has missing or unexpected sources.")
    if any(row["status"] != "Planned" for row in rows):
        errors.append("An unexecuted thesis search source is not marked Planned.")


def validate_fieldwork_scoring(errors: list[str]) -> None:
    base = "05_pipeline/fieldwork/synthetic"
    source = read_csv(f"{base}/survey_responses_synthetic.csv")
    scored = read_csv(f"{base}/scored_responses_synthetic.csv")
    summary = read_csv(f"{base}/organization_summary_synthetic.csv")
    missingness = read_csv(f"{base}/item_missingness_synthetic.csv")
    expected_items = {
        *(f"RM{index:02d}" for index in range(1, 15)),
        *(f"AC{index:02d}" for index in range(1, 7)),
        *(f"SC{index:02d}" for index in range(1, 7)),
        *(f"TR{index:02d}" for index in range(1, 7)),
    }
    if len(source) != 22 or len({row["organization_code"] for row in source}) != 4:
        errors.append("Synthetic fieldwork input must contain 22 records in four organizations.")
    if any(row.get("synthetic_record", "").lower() != "true" for row in source):
        errors.append("Every synthetic fieldwork input row must be explicitly labeled.")
    if not expected_items.issubset(source[0] if source else {}):
        errors.append("Synthetic fieldwork input does not contain all 32 survey items.")
    if len(scored) != len(source):
        errors.append("Synthetic scored output does not preserve the input row count.")

    score_columns = [
        "risk_management_maturity",
        "access_control_effectiveness",
        "source_code_protection",
        "development_traceability",
    ]
    for row in scored:
        for column in score_columns:
            value = row.get(column, "")
            if value and not 1 <= float(value) <= 5:
                errors.append(f"Synthetic score is outside 1 to 5: {column}")
    first_record = next((row for row in scored if row["participant_code"] == "SYN_P001"), None)
    if first_record is None or first_record["access_control_effectiveness"]:
        errors.append("Synthetic missing-data case does not enforce the access-control rule.")

    expected_summary_rows = {
        "ALL_PARTICIPANTS",
        "ORGANIZATION_BREAKDOWN_WITHHELD",
    }
    if {row["organization_code"] for row in summary} != expected_summary_rows:
        errors.append("Synthetic organization summary has unexpected reporting groups.")
    suppressed = next(
        (
            row
            for row in summary
            if row["organization_code"] == "ORGANIZATION_BREAKDOWN_WITHHELD"
        ),
        None,
    )
    if suppressed is None or any(suppressed[f"{column}_mean"] for column in score_columns):
        errors.append("The synthetic small-group row does not suppress its score means.")
    if len(missingness) != 32 or sum(int(row["missing_count"]) for row in missingness) != 10:
        errors.append("Synthetic item-missingness output does not match the controlled cases.")

    metadata_path = ROOT / base / "scoring_metadata_synthetic.json"
    metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
    if (
        metadata.get("synthetic_data") is not True
        or metadata.get("participant_count") != 22
        or metadata.get("organization_count") != 4
    ):
        errors.append("Synthetic scoring metadata has an invalid scope or record count.")


def validate_synthetic_analysis(errors: list[str]) -> None:
    base = "05_pipeline/fieldwork/synthetic/association_demo"
    source = read_csv(f"{base}/survey_responses_analysis_synthetic.csv")
    evidence = read_csv(f"{base}/integration_evidence_synthetic.csv")
    scored = read_csv(f"{base}/scored_responses_synthetic.csv")
    correlations = read_csv(f"{base}/spearman_correlations_synthetic.csv")
    regressions = read_csv(f"{base}/exploratory_regressions_synthetic.csv")
    diagnostics = read_csv(f"{base}/regression_diagnostics_synthetic.csv")
    integration = read_csv(f"{base}/integration_joint_display_synthetic.csv")
    outcomes = {
        "access_control_effectiveness",
        "source_code_protection",
        "development_traceability",
    }

    if len(source) != 64 or len({row["organization_code"] for row in source}) != 8:
        errors.append("Synthetic analysis input must contain 64 records in eight organizations.")
    if any(row.get("synthetic_record", "").lower() != "true" for row in source):
        errors.append("Every synthetic analysis input row must be explicitly labeled.")
    if len(scored) != 64 or any(
        row.get("synthetic_record", "").lower() != "true" for row in scored
    ):
        errors.append("Synthetic analysis scoring output has an invalid size or label.")

    if len(evidence) != 3 or {row["outcome"] for row in evidence} != outcomes:
        errors.append("Synthetic integration evidence must contain the three outcomes.")
    if any(row.get("synthetic_evidence", "").lower() != "true" for row in evidence):
        errors.append("Every synthetic integration evidence row must be explicitly labeled.")

    if len(correlations) != 3 or {row["outcome"] for row in correlations} != outcomes:
        errors.append("Synthetic Spearman output must contain the three primary associations.")
    for row in correlations:
        if row.get("synthetic_data", "").lower() != "true":
            errors.append("A synthetic Spearman result is not labeled synthetic.")
        if int(row["bootstrap_iterations"]) != 2000:
            errors.append("A synthetic Spearman result has an unexpected bootstrap count.")
        rho = float(row["spearman_rho"])
        lower = float(row["cluster_bootstrap_ci_95_lower"])
        upper = float(row["cluster_bootstrap_ci_95_upper"])
        if not -1 <= lower <= rho <= upper <= 1:
            errors.append(f"Synthetic Spearman interval is invalid for {row['outcome']}.")

    expected_terms = {
        "const",
        "risk_management_maturity",
        "experience_ordinal",
        "company_size_ordinal",
    }
    if len(regressions) != 12 or {row["outcome"] for row in regressions} != outcomes:
        errors.append("Synthetic regression output must contain three four-term models.")
    for outcome in outcomes:
        terms = {row["term"] for row in regressions if row["outcome"] == outcome}
        if terms != expected_terms:
            errors.append(f"Synthetic regression terms are invalid for {outcome}.")
    if any(row.get("synthetic_data", "").lower() != "true" for row in regressions):
        errors.append("A synthetic regression result is not labeled synthetic.")

    if len(diagnostics) != 3 or {row["outcome"] for row in diagnostics} != outcomes:
        errors.append("Synthetic regression diagnostics must contain the three outcomes.")
    if any(row.get("synthetic_data", "").lower() != "true" for row in diagnostics):
        errors.append("A synthetic regression diagnostic is not labeled synthetic.")
    if any("fieldwork requires" not in row["diagnostic_scope"] for row in diagnostics):
        errors.append("A synthetic regression diagnostic lacks its fieldwork boundary.")

    if len(integration) != 3 or {row["outcome"] for row in integration} != outcomes:
        errors.append("Synthetic joint display must contain the three outcomes.")
    if any(row.get("synthetic_data", "").lower() != "true" for row in integration):
        errors.append("A joint-display row is not labeled synthetic.")
    if any("generated for testing" not in row["interpretive_boundary"] for row in integration):
        errors.append("A joint-display row lacks its synthetic interpretive boundary.")

    metadata = json.loads((ROOT / base / "analysis_metadata_synthetic.json").read_text(encoding="utf-8"))
    expected_outputs = {
        "spearman_correlations_synthetic.csv",
        "exploratory_regressions_synthetic.csv",
        "regression_diagnostics_synthetic.csv",
        "integration_joint_display_synthetic.csv",
        "analysis_report_synthetic.md",
    }
    if (
        metadata.get("synthetic_data") is not True
        or metadata.get("participant_count") != 64
        or metadata.get("organization_count") != 8
        or len(metadata.get("methods", [])) != 4
        or set(metadata.get("outputs", [])) != expected_outputs
    ):
        errors.append("Synthetic analysis metadata has an invalid scope or count.")
    source_path = ROOT / base / "scored_responses_synthetic.csv"
    evidence_path = ROOT / base / "integration_evidence_synthetic.csv"
    if metadata.get("input_sha256") != hashlib.sha256(source_path.read_bytes()).hexdigest():
        errors.append("Synthetic analysis metadata has an invalid scored-input hash.")
    if metadata.get("integration_evidence_sha256") != hashlib.sha256(
        evidence_path.read_bytes()
    ).hexdigest():
        errors.append("Synthetic analysis metadata has an invalid integration-evidence hash.")
    report = (ROOT / base / "analysis_report_synthetic.md").read_text(encoding="utf-8")
    if "SYNTHETIC DATA ONLY. THESE VALUES ARE NOT RESEARCH FINDINGS." not in report:
        errors.append("Synthetic analysis report lacks the required warning.")


def validate_presentation(errors: list[str]) -> None:
    presentation = (ROOT / "13_presentation/index.html").read_text(encoding="utf-8")
    current_title = (
        "Risk management maturity and effectiveness of secure development "
        "controls in Peruvian companies"
    )
    previous_title = "Influence of information security risk management on the effectiveness"
    if current_title not in presentation:
        errors.append("The presentation does not use the current research title.")
    if previous_title in presentation:
        errors.append("The presentation still contains the previous research title.")
    if 'src="unmsm-logo.svg"' in presentation:
        errors.append("The presentation still uses the previous root-level logo path.")
    if 'src="assets/unmsm-logo.svg"' not in presentation:
        errors.append("The presentation does not reference its institutional asset folder.")
    if presentation.count('<section class="slide') != 16:
        errors.append("The presentation must contain 16 slides.")
    if presentation.count("unmsm-logo") != 16:
        errors.append("Each presentation slide must include the institutional logo.")
    if "The analysis tests three predefined associations" not in presentation:
        errors.append("The presentation does not explain the analytical algorithm.")
    if "The 64-record implementation is entirely synthetic" not in presentation:
        errors.append("The presentation does not state the synthetic-analysis boundary.")

    guide = (ROOT / "13_presentation/README.md").read_text(encoding="utf-8")
    if "The deck contains 16 slides" not in guide or "### Slide 16:" not in guide:
        errors.append("The presentation guide does not cover all 16 slides.")


def main() -> None:
    errors: list[str] = []
    validate_required_files(errors)
    validate_structure(errors)
    validate_markdown(errors)
    validate_pipeline_docs(errors)
    validate_survey(errors)
    validate_prisma(errors)
    validate_screening(errors)
    validate_quality(errors)
    validate_search_plan(errors)
    validate_fieldwork_scoring(errors)
    validate_synthetic_analysis(errors)
    validate_presentation(errors)

    if errors:
        details = "\n".join(f"- {error}" for error in errors)
        raise SystemExit(f"Repository validation failed:\n{details}")
    print("Repository validation passed.")


if __name__ == "__main__":
    main()

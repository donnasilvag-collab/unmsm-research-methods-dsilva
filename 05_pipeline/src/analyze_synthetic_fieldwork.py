"""Run the synthetic Spearman, regression, and mixed-evidence demonstration."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np
import pandas as pd
import statsmodels.api as sm
import yaml
from scipy.stats import spearmanr


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_ANALYSIS_DIR = ROOT / "fieldwork" / "synthetic" / "association_demo"
SCOPE_NOTE = "Synthetic methodological demonstration only; not a research finding."


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--input",
        type=Path,
        default=DEFAULT_ANALYSIS_DIR / "scored_responses_synthetic.csv",
    )
    parser.add_argument(
        "--evidence",
        type=Path,
        default=DEFAULT_ANALYSIS_DIR / "integration_evidence_synthetic.csv",
    )
    parser.add_argument("--params", type=Path, default=ROOT / "params.yaml")
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_ANALYSIS_DIR)
    parser.add_argument(
        "--synthetic",
        action="store_true",
        help="Required safeguard: reject any input not explicitly labeled synthetic.",
    )
    return parser.parse_args()


def file_hash(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def validate_and_prepare(
    frame: pd.DataFrame,
    demo: dict,
    require_synthetic: bool,
) -> pd.DataFrame:
    if not require_synthetic:
        raise ValueError("This demonstration runs only with the --synthetic safeguard.")

    explanatory = demo["explanatory_variable"]
    outcomes = list(demo["outcomes"])
    required = {
        "participant_code",
        "organization_code",
        "synthetic_record",
        "experience_group",
        "company_size_group",
        explanatory,
        *outcomes,
    }
    missing = sorted(required.difference(frame.columns))
    if missing:
        raise ValueError(f"The scored synthetic file is missing: {', '.join(missing)}")
    if not frame["synthetic_record"].astype(str).str.lower().eq("true").all():
        raise ValueError("Every analysis record must be explicitly labeled synthetic.")
    if frame["participant_code"].duplicated().any():
        raise ValueError("Synthetic participant codes must be unique.")

    expected_participants = int(demo["participant_count"])
    expected_organizations = int(demo["organization_count"])
    actual_organizations = int(frame["organization_code"].nunique())
    if len(frame) != expected_participants or actual_organizations != expected_organizations:
        raise ValueError("The synthetic analysis fixture does not match its controlled size.")
    if len(frame) < int(demo["minimum_eligible_participants"]):
        raise ValueError("The synthetic fixture does not meet the demonstration participant threshold.")
    if actual_organizations < int(demo["minimum_organizations"]):
        raise ValueError("The synthetic fixture does not meet the demonstration organization threshold.")

    prepared = frame.copy()
    mappings = demo["covariate_mappings"]
    prepared["experience_ordinal"] = prepared["experience_group"].map(
        mappings["experience_group"]
    )
    prepared["company_size_ordinal"] = prepared["company_size_group"].map(
        mappings["company_size_group"]
    )
    numeric = [explanatory, *outcomes, "experience_ordinal", "company_size_ordinal"]
    for column in numeric:
        prepared[column] = pd.to_numeric(prepared[column], errors="coerce")
    return prepared


def clustered_spearman_interval(
    frame: pd.DataFrame,
    explanatory: str,
    outcome: str,
    iterations: int,
    seed: int,
) -> tuple[float, float]:
    rng = np.random.default_rng(seed)
    groups = {
        code: group[[explanatory, outcome]].dropna()
        for code, group in frame.groupby("organization_code", sort=True)
    }
    organization_codes = np.array(sorted(groups))
    bootstrap_values: list[float] = []
    for _ in range(iterations):
        sampled_codes = rng.choice(
            organization_codes,
            size=len(organization_codes),
            replace=True,
        )
        sample = pd.concat([groups[code] for code in sampled_codes], ignore_index=True)
        estimate = float(spearmanr(sample[explanatory], sample[outcome]).statistic)
        if np.isfinite(estimate):
            bootstrap_values.append(estimate)
    if len(bootstrap_values) < int(iterations * 0.95):
        raise ValueError(f"Too few valid bootstrap correlations for {outcome}.")
    lower, upper = np.quantile(bootstrap_values, [0.025, 0.975])
    return float(lower), float(upper)


def run_correlations(frame: pd.DataFrame, demo: dict) -> pd.DataFrame:
    explanatory = demo["explanatory_variable"]
    iterations = int(demo["bootstrap_iterations"])
    seed_sequence = np.random.SeedSequence(int(demo["seed"]))
    child_seeds = seed_sequence.spawn(len(demo["outcomes"]))
    rows: list[dict[str, object]] = []
    for outcome, child_seed in zip(demo["outcomes"], child_seeds, strict=True):
        complete = frame.dropna(subset=[explanatory, outcome, "organization_code"])
        result = spearmanr(complete[explanatory], complete[outcome])
        lower, upper = clustered_spearman_interval(
            complete,
            explanatory,
            outcome,
            iterations,
            int(child_seed.generate_state(1)[0]),
        )
        rows.append(
            {
                "synthetic_data": True,
                "outcome": outcome,
                "eligible_participants": len(complete),
                "organization_count": int(complete["organization_code"].nunique()),
                "spearman_rho": float(result.statistic),
                "spearman_p_value_unadjusted": float(result.pvalue),
                "cluster_bootstrap_ci_95_lower": lower,
                "cluster_bootstrap_ci_95_upper": upper,
                "bootstrap_iterations": iterations,
                "scope_note": SCOPE_NOTE,
            }
        )
    return pd.DataFrame(rows)


def run_regressions(frame: pd.DataFrame, demo: dict) -> tuple[pd.DataFrame, pd.DataFrame]:
    explanatory = demo["explanatory_variable"]
    predictors = [explanatory, "experience_ordinal", "company_size_ordinal"]
    rows: list[dict[str, object]] = []
    diagnostic_rows: list[dict[str, object]] = []
    for outcome in demo["outcomes"]:
        complete = frame.dropna(subset=[outcome, "organization_code", *predictors]).copy()
        design = sm.add_constant(complete[predictors], has_constant="add")
        model = sm.OLS(complete[outcome], design).fit(
            cov_type="cluster",
            cov_kwds={
                "groups": complete["organization_code"],
                "use_correction": True,
            },
            use_t=True,
        )
        influence = model.get_influence()
        cooks_distance = influence.cooks_distance[0]
        studentized_residuals = influence.resid_studentized_external
        diagnostic_rows.append(
            {
                "synthetic_data": True,
                "outcome": outcome,
                "eligible_participants": int(model.nobs),
                "organization_count": int(complete["organization_code"].nunique()),
                "r_squared": float(model.rsquared),
                "adjusted_r_squared": float(model.rsquared_adj),
                "condition_number": float(model.condition_number),
                "maximum_cooks_distance": float(np.nanmax(cooks_distance)),
                "maximum_absolute_studentized_residual": float(
                    np.nanmax(np.abs(studentized_residuals))
                ),
                "diagnostic_scope": (
                    "Synthetic software check only; fieldwork requires a fresh diagnostic review."
                ),
            }
        )
        intervals = model.conf_int(alpha=0.05)
        for term in design.columns:
            rows.append(
                {
                    "synthetic_data": True,
                    "outcome": outcome,
                    "term": term,
                    "coefficient": float(model.params[term]),
                    "cluster_robust_standard_error": float(model.bse[term]),
                    "ci_95_lower": float(intervals.loc[term, 0]),
                    "ci_95_upper": float(intervals.loc[term, 1]),
                    "p_value": float(model.pvalues[term]),
                    "eligible_participants": int(model.nobs),
                    "organization_count": int(complete["organization_code"].nunique()),
                    "r_squared": float(model.rsquared),
                    "scope_note": SCOPE_NOTE,
                }
            )
    return pd.DataFrame(rows), pd.DataFrame(diagnostic_rows)


def build_joint_display(
    correlations: pd.DataFrame,
    regressions: pd.DataFrame,
    evidence: pd.DataFrame,
    explanatory: str,
) -> pd.DataFrame:
    required = {
        "outcome",
        "synthetic_interview_pattern",
        "synthetic_document_pattern",
        "synthetic_integration_assessment",
        "synthetic_evidence",
    }
    if not required.issubset(evidence.columns):
        raise ValueError("The synthetic integration evidence has an invalid schema.")
    if not evidence["synthetic_evidence"].astype(str).str.lower().eq("true").all():
        raise ValueError("Every integration record must be explicitly labeled synthetic.")

    maturity_terms = regressions.loc[regressions["term"] == explanatory].copy()
    merged = correlations.merge(maturity_terms, on="outcome", validate="one_to_one")
    merged = merged.merge(evidence, on="outcome", validate="one_to_one")
    rows: list[dict[str, object]] = []
    for row in merged.itertuples(index=False):
        rows.append(
            {
                "synthetic_data": True,
                "outcome": row.outcome,
                "quantitative_pattern": (
                    f"Synthetic rho={row.spearman_rho:.3f} "
                    f"(organization-bootstrap 95% CI {row.cluster_bootstrap_ci_95_lower:.3f} "
                    f"to {row.cluster_bootstrap_ci_95_upper:.3f}); adjusted synthetic "
                    f"beta={row.coefficient:.3f} (95% CI {row.ci_95_lower:.3f} "
                    f"to {row.ci_95_upper:.3f})."
                ),
                "synthetic_interview_pattern": row.synthetic_interview_pattern,
                "synthetic_document_pattern": row.synthetic_document_pattern,
                "integration_assessment": row.synthetic_integration_assessment,
                "interpretive_boundary": (
                    "Illustrates joint-display logic only; all quantitative and qualitative "
                    "content was generated for testing."
                ),
            }
        )
    return pd.DataFrame(rows)


def markdown_table(frame: pd.DataFrame, columns: list[str]) -> str:
    def format_value(value: object) -> str:
        if isinstance(value, (float, np.floating)):
            return f"{float(value):.4f}"
        return str(value).replace("|", "\\|")

    header = "| " + " | ".join(columns) + " |"
    separator = "| " + " | ".join("---" for _ in columns) + " |"
    rows = [
        "| " + " | ".join(format_value(row[column]) for column in columns) + " |"
        for _, row in frame[columns].iterrows()
    ]
    return "\n".join([header, separator, *rows])


def write_report(
    destination: Path,
    correlations: pd.DataFrame,
    regressions: pd.DataFrame,
    diagnostics: pd.DataFrame,
    joint_display: pd.DataFrame,
) -> None:
    correlation_report = correlations.rename(
        columns={
            "outcome": "Outcome",
            "eligible_participants": "Eligible n",
            "organization_count": "Organizations",
            "spearman_rho": "Spearman rho",
            "cluster_bootstrap_ci_95_lower": "CI lower",
            "cluster_bootstrap_ci_95_upper": "CI upper",
        }
    )
    maturity = regressions.loc[regressions["term"] == "risk_management_maturity"].copy()
    maturity["p value"] = maturity["p_value"].map(
        lambda value: "<0.0001" if value < 0.0001 else f"{value:.4f}"
    )
    maturity_report = maturity.rename(
        columns={
            "outcome": "Outcome",
            "coefficient": "Maturity coefficient",
            "cluster_robust_standard_error": "Clustered SE",
            "ci_95_lower": "CI lower",
            "ci_95_upper": "CI upper",
            "r_squared": "R squared",
        }
    )
    joint_report = joint_display.rename(
        columns={
            "outcome": "Outcome",
            "quantitative_pattern": "Synthetic quantitative pattern",
            "synthetic_interview_pattern": "Fictitious interview pattern",
            "synthetic_document_pattern": "Fictitious document pattern",
            "integration_assessment": "Illustrative integration",
        }
    )
    diagnostic_report = diagnostics.rename(
        columns={
            "outcome": "Outcome",
            "r_squared": "R squared",
            "adjusted_r_squared": "Adjusted R squared",
            "condition_number": "Condition number",
            "maximum_cooks_distance": "Maximum Cook distance",
            "maximum_absolute_studentized_residual": "Maximum absolute studentized residual",
        }
    )
    lines = [
        "# Synthetic association and integration demonstration",
        "",
        "**SYNTHETIC DATA ONLY. THESE VALUES ARE NOT RESEARCH FINDINGS.**",
        "",
        "This report tests the analytical sequence planned for Donna Silva's study. The 64 participant records, eight organizations, interview patterns, and documentary patterns were generated by code. They do not describe Peruvian companies or real security practices.",
        "",
        "## Spearman correlations",
        "",
        "The point estimates use participant-level scores. The 95% intervals resample whole synthetic organizations so participants from the same organization are not treated as fully independent. The unadjusted Spearman p-values are retained for software inspection only and have no substantive evidentiary meaning in designed data.",
        "",
        markdown_table(
            correlation_report,
            [
                "Outcome",
                "Eligible n",
                "Organizations",
                "Spearman rho",
                "CI lower",
                "CI upper",
            ],
        ),
        "",
        "## Exploratory regressions",
        "",
        "Three separate linear models estimate the association between the synthetic maturity score and each synthetic outcome. Experience and company size are included only to exercise the two-covariate protocol limit. Standard errors are grouped by synthetic organization. These covariates are not frozen choices for real fieldwork.",
        "",
        markdown_table(
            maturity_report,
            [
                "Outcome",
                "Maturity coefficient",
                "Clustered SE",
                "CI lower",
                "CI upper",
                "p value",
                "R squared",
            ],
        ),
        "",
        "### Model diagnostics",
        "",
        "The diagnostic table is retained to test the review path. Its thresholds are not acceptance criteria for future fieldwork; model form, influential observations, residual behavior, and organization count must be reassessed with authorized data.",
        "",
        markdown_table(
            diagnostic_report,
            [
                "Outcome",
                "R squared",
                "Adjusted R squared",
                "Condition number",
                "Maximum Cook distance",
                "Maximum absolute studentized residual",
            ],
        ),
        "",
        "## Mixed methods joint display",
        "",
        markdown_table(
            joint_report,
            [
                "Outcome",
                "Synthetic quantitative pattern",
                "Fictitious interview pattern",
                "Fictitious document pattern",
                "Illustrative integration",
            ],
        ),
        "",
        "## Interpretation boundary",
        "",
        "The generator deliberately links maturity and control scores, so positive associations are expected by construction. The demonstration shows that the code can validate thresholds, preserve organization dependence, fit the three bounded models, and assemble a joint display. It does not validate the instrument, estimate an effect, test a hypothesis about Peru, or replace authorized fieldwork.",
        "",
        "Real analysis remains conditional on expert review, cognitive testing, pilot testing, ethics or institutional approval, recruitment, and a dated freeze of the analytical choices.",
    ]
    destination.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    args = parse_args()
    params = yaml.safe_load(args.params.read_text(encoding="utf-8"))
    demo = params["synthetic_analysis_demo"]
    if demo.get("synthetic_data") is not True:
        raise ValueError("The configured analysis demonstration must remain synthetic.")

    frame = pd.read_csv(args.input)
    evidence = pd.read_csv(args.evidence)
    prepared = validate_and_prepare(frame, demo, args.synthetic)
    correlations = run_correlations(prepared, demo)
    regressions, diagnostics = run_regressions(prepared, demo)
    joint_display = build_joint_display(
        correlations,
        regressions,
        evidence,
        demo["explanatory_variable"],
    )

    args.output_dir.mkdir(parents=True, exist_ok=True)
    correlations_path = args.output_dir / "spearman_correlations_synthetic.csv"
    regressions_path = args.output_dir / "exploratory_regressions_synthetic.csv"
    diagnostics_path = args.output_dir / "regression_diagnostics_synthetic.csv"
    joint_display_path = args.output_dir / "integration_joint_display_synthetic.csv"
    report_path = args.output_dir / "analysis_report_synthetic.md"
    metadata_path = args.output_dir / "analysis_metadata_synthetic.json"
    correlations.to_csv(correlations_path, index=False, float_format="%.10g", lineterminator="\n")
    regressions.to_csv(regressions_path, index=False, float_format="%.10g", lineterminator="\n")
    diagnostics.to_csv(diagnostics_path, index=False, float_format="%.10g", lineterminator="\n")
    joint_display.to_csv(joint_display_path, index=False, lineterminator="\n")
    write_report(report_path, correlations, regressions, diagnostics, joint_display)

    metadata = {
        "synthetic_data": True,
        "scope_note": SCOPE_NOTE,
        "input_file": args.input.name,
        "input_sha256": file_hash(args.input),
        "integration_evidence_file": args.evidence.name,
        "integration_evidence_sha256": file_hash(args.evidence),
        "params_file": args.params.name,
        "params_sha256": file_hash(args.params),
        "participant_count": len(prepared),
        "organization_count": int(prepared["organization_code"].nunique()),
        "methods": [
            "Spearman correlation",
            "organization-clustered bootstrap interval",
            "linear regression with organization-clustered standard errors",
            "mixed methods joint display",
        ],
        "outputs": [
            correlations_path.name,
            regressions_path.name,
            diagnostics_path.name,
            joint_display_path.name,
            report_path.name,
        ],
    }
    metadata_path.write_text(
        json.dumps(metadata, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(
        "Completed the synthetic-only Spearman, regression, and integration "
        f"demonstration for {len(prepared)} records."
    )


if __name__ == "__main__":
    main()

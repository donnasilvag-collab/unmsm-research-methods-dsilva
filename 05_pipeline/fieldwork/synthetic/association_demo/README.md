# Synthetic association demonstration

**Every record and result in this directory is synthetic. Nothing here is a finding about a person, organization, repository, or Peruvian company.**

## Purpose

This fixture tests the analytical sequence planned in the protocol without using protected fieldwork data. The generator creates 64 fictitious participants in eight fictitious organizations and deliberately links risk-management maturity with three control outcomes. It also creates three fictional interview and document patterns so the mixed methods joint display can be assembled.

## Reproduce

Run from `05_pipeline/`:

```powershell
python src/generate_synthetic_analysis.py
python src/score_fieldwork.py --input fieldwork/synthetic/association_demo/survey_responses_analysis_synthetic.csv --output-dir fieldwork/synthetic/association_demo --synthetic
python src/analyze_synthetic_fieldwork.py --synthetic
```

The analysis calculates three participant-level Spearman correlations, 2,000-iteration bootstrap intervals that resample whole organizations, and three exploratory linear regressions. Each regression includes the maturity score and two context covariates used only to exercise the protocol limit. Standard errors are grouped by fictitious organization.

## Files

| File | Role |
| --- | --- |
| `survey_responses_analysis_synthetic.csv` | Generated 32-item survey responses |
| `integration_evidence_synthetic.csv` | Fictitious interview and document patterns |
| `scored_responses_synthetic.csv` | Participant-level scores produced by the standard scoring script |
| `organization_summary_synthetic.csv` | Synthetic organization summaries |
| `item_missingness_synthetic.csv` | Item-level completeness check |
| `scoring_metadata_synthetic.json` | Scoring input hash and scope |
| `spearman_correlations_synthetic.csv` | Correlations and organization-bootstrap intervals |
| `exploratory_regressions_synthetic.csv` | Coefficients and organization-clustered uncertainty |
| `regression_diagnostics_synthetic.csv` | Model fit and influence checks for the software demonstration |
| `integration_joint_display_synthetic.csv` | Quantitative, interview, and document integration |
| `analysis_report_synthetic.md` | Readable methodological demonstration |
| `analysis_metadata_synthetic.json` | Analysis input hashes, methods, and output list |

## Boundary before fieldwork

The generated signal makes positive associations likely by construction. The p-values, confidence intervals, coefficients, and integration assessments show that the code runs; they do not validate the survey or support an empirical claim. Real analysis requires instrument validation, ethics or institutional approval, authorized recruitment, protected storage, and a dated analytical freeze.

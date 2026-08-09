# Data and pipeline quality checks

## Public source workbook

The preparation stage rejects the workbook instead of silently repairing it when a structural condition fails. The validated workbook met these conditions:

| Check | Verified result |
| --- | --- |
| Repository records | 48 |
| Strata | 24 Peru and 24 International benchmark |
| Distinct Peru organization owners | 9 |
| Duplicate record identifiers | 0 |
| Duplicate repository URLs | 0 |
| GitHub REST responses | 48 with HTTP 200 |
| Local Git inspection | 48 with status `ok` |
| OpenSSF overall scores available | 19 of 48 |
| OpenSSF check records retained | 303 |
| Observed composite scores outside 0 to 10 | 0 |

OpenSSF returned HTTP 406 for 26 repositories and HTTP 404 for 3. These responses remain unavailable observations. They are not converted to zero because absence of a public score is not evidence of a failed control.

The source snapshot was collected on 31 July 2026 at 19:28:08 Lima time. The Git history inspection was recorded on the same date at 19:40:45 Lima time. Row-level endpoints, timestamps, status codes, and provenance remain in the workbook.

## Deterministic transformation

`dvc repro` runs [`../data/create_dataset.py`](../data/create_dataset.py). The script checks required columns, row count, strata, uniqueness, numeric conversion, and the 0 to 10 range before writing the analysis-ready CSV. The current verified hashes are:

| File | SHA-256 |
| --- | --- |
| Source workbook | `f52fcde575114a0e1d2a758df40859977b1f1aec109eb3c77794cbe123bb9e91` |
| Analysis-ready CSV | `37b0ea8db091671216cd7c0c67af68fbe62513f99e67a6f8cb69e938895300e3` |
| Preparation script | `fcdef8f384b6cb694981e61f7a39b72cf2a29bcdd2877ee5afa0128d2a65a5af` |

The derived CSV has 48 rows and 55 columns. Missing values are retained where a source could not provide a valid observation. The quality check does not impute unavailable public signals.

## Synthetic fieldwork fixture

The survey-scoring fixture is separate from the public repository benchmark. It contains 22 synthetic participants across four synthetic organizations with sizes 6, 6, 6, and 4. Ten item values are deliberately missing to test the documented completeness rules. The smallest group triggers suppression of the full organization breakdown.

The fixture verifies schema and scoring behavior only. It does not validate the survey, estimate reliability, or provide evidence about Peruvian companies.

## Synthetic association fixture

A second fixture contains 64 generated participants in eight generated organizations. It meets the protocol's numerical thresholds only so that the planned analysis branches can run during software testing. The following checks apply:

| Check | Verified design |
| --- | --- |
| Synthetic participant records | 64 |
| Synthetic organizations | 8, with 8 records each |
| Substantive survey items | 32 |
| Primary Spearman associations | 3 |
| Clustered bootstrap iterations | 2,000 per association |
| Exploratory linear models | 3 |
| Predictors per model | Maturity plus two synthetic context covariates |
| Model diagnostic records | 3 |
| Joint-display rows | 3 |

The generator intentionally links maturity and outcome values. The evidence file contains fictitious interview and document patterns. The analysis script requires `--synthetic`, rejects unlabeled rows, records source hashes, and writes a scope warning into every output. These controls prevent a successful code test from being presented as empirical evidence.

## Commands

```powershell
dvc repro
python src/run_experiments.py
python src/generate_synthetic_fieldwork.py
python src/score_fieldwork.py --input fieldwork/synthetic/survey_responses_synthetic.csv --output-dir fieldwork/synthetic --synthetic
python src/generate_synthetic_analysis.py
python src/score_fieldwork.py --input fieldwork/synthetic/association_demo/survey_responses_analysis_synthetic.csv --output-dir fieldwork/synthetic/association_demo --synthetic
python src/analyze_synthetic_fieldwork.py --synthetic
cd ..
.\05_pipeline\.venv\Scripts\python.exe 11_bias_audit\bias_audit.py
.\05_pipeline\.venv\Scripts\python.exe 05_pipeline\src\validate_repository.py
```

# UNMSM Research Methods - Donna Silva

**Author:** Donna Silva
**Research topic:** *Madurez de la gestión de riesgos y eficacia de los controles de desarrollo seguro en empresas peruanas.*

## Purpose

This folder implements the reproducibility component of the study. It follows the Git + DVC + MLflow + Docker architecture required for the course, while respecting the study's current stage: no internal company data, personal data, interview material, or confidential code is stored here.

The executable component analyzes a complementary, public benchmark of software repositories. It makes the data preparation and descriptive comparison reproducible; it does **not** test the relationships proposed for the fieldwork, estimate company-level risk-management maturity, or replace the planned mixed-methods study.

A separate fieldwork module implements the scoring rules for the draft survey. Its committed input is synthetic and exists only to test the code before protected collection begins. The public benchmark and the synthetic survey test remain separate analytical paths.

## What Is Reproduced

The source workbook contains 48 public GitHub repositories: 24 linked to organization profiles that publicly declare Peru and 24 international benchmark repositories. The analytical unit is one repository. The preparation script retains the publicly observable indicators and four documented proxy dimensions:

| Dimension | Interpretation in this benchmark |
| --- | --- |
| `risk_governance_observed` | Public signals related to security policy, dependency updates, repository activity, and licensing. |
| `access_control_observed` | Public signals related to CODEOWNERS, workflow permissions, and signed commits. |
| `source_code_protection_observed` | Public signals related to automated scanning, dependency updates, signing, and action pinning. |
| `traceability_observed` | Public signals related to activity, commit conventions, issue references, merge history, tests, and releases. |

These are observability proxies, not direct measures of internal controls. A missing public signal means **not observed**, not that the control does not exist. Results are descriptive and are reported at the repository level. For the Peru stratum, uncertainty intervals use organization-clustered bootstrap resampling because several repositories may belong to the same organization.

## Folder Structure

```text
05_pipeline/
+-- .dvc/                         # DVC configuration for this subproject
+-- data/
|   +-- raw/                      # Small public source workbook, tracked by Git
|   +-- create_dataset.py          # Validates and derives the analysis-ready CSV
|   `-- public_repo_security_benchmark.csv  # DVC output after `dvc repro`
+-- fieldwork/
|   +-- README.md                 # Protected-data boundary and scoring instructions
|   `-- synthetic/               # Scoring fixture and synthetic association demonstration
+-- docs/                         # Environment, provenance, quality, results, and run evidence
+-- results/                      # Summary tables produced by the experiments
+-- src/
|   +-- generate_synthetic_fieldwork.py  # Creates deterministic test records
|   +-- generate_synthetic_analysis.py   # Creates the 64-record analysis demonstration
|   +-- analyze_synthetic_fieldwork.py   # Runs Spearman, regression, and joint integration
|   +-- score_fieldwork.py        # Validates and scores the 32 survey items
|   +-- train.py                  # Repository-level benchmark analysis
|   `-- run_experiments.py        # Four seeded MLflow runs and summary artifacts
+-- dvc.yaml                      # Data-preparation stage
+-- params.yaml                   # Explicit, versioned analytical parameters
+-- requirements.txt              # Pinned runtime dependencies
`-- Dockerfile                    # Isolated execution environment
```

`train.py` retains the conventional filename used in the course template, but it does not train a predictive model. It performs the parameterized benchmark analysis described above.

## Reproducible Execution

Run the following commands from `05_pipeline/`.

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
dvc repro
python src/run_experiments.py
```

On Windows, clone the repository to a short path, such as `C:\research\dsilva`, before creating `.venv`. A deeply nested parent path can prevent compiled SciPy or statsmodels extensions from loading and produce a `file name or extension is too long` error. If that occurs, use a shorter clone path and recreate the virtual environment.

This produces:

- `data/public_repo_security_benchmark.csv`, the validated analysis-ready dataset;
- `results/benchmark_summary_seed_*.csv`, one clustered-bootstrap summary per seed;
- `results/seed_stability.csv`, the cross-seed comparison;
- `docs/mlflow_runs.png`, a visual summary of the latest run;
- `mlruns/`, local MLflow metadata with parameters, metrics, and result artifacts.

From the repository root, reproduce the complementary bias audit after the pipeline has prepared the data:

```powershell
.\05_pipeline\.venv\Scripts\python.exe 11_bias_audit\bias_audit.py
```

The audit compares row-level and owner-clustered bootstrap intervals and performs a leave-one-owner-out sensitivity analysis. It writes three numerical CSV files and one chart in `11_bias_audit/`. The algorithm uses organization aliases in its influence outputs and does not rank repositories or companies.

To inspect the local experiment ledger, run:

```powershell
mlflow ui --backend-store-uri .\mlruns
```

## Synthetic fieldwork scoring test

Run the following commands from `05_pipeline/`:

```powershell
python src/generate_synthetic_fieldwork.py
python src/score_fieldwork.py --input fieldwork/synthetic/survey_responses_synthetic.csv --output-dir fieldwork/synthetic --synthetic
```

The scoring script applies the rules in `03_protocol/operationalization_matrix.md`. It requires both items for each risk-management dimension, at least five of seven risk dimensions for the overall maturity score, and at least four of six items for each control outcome. Missing answers remain missing. If any organization falls below the threshold in `params.yaml`, the script withholds the full organization breakdown to prevent reconstruction by subtraction.

See [`fieldwork/README.md`](fieldwork/README.md) before using the script with authorized data. Real exports and scored files must stay in protected storage outside Git. The 22-record scoring fixture does not run correlations, regression, or psychometric validation. The separate demonstration below exercises analysis code with a larger generated dataset but does not authorize or stand in for real fieldwork.

## Synthetic association and integration demonstration

The repository also exercises the planned analytical sequence with a second, clearly separated synthetic fixture:

```powershell
python src/generate_synthetic_analysis.py
python src/score_fieldwork.py --input fieldwork/synthetic/association_demo/survey_responses_analysis_synthetic.csv --output-dir fieldwork/synthetic/association_demo --synthetic
python src/analyze_synthetic_fieldwork.py --synthetic
```

This fixture contains 64 generated participants in eight generated organizations. It runs the three prespecified Spearman associations, 2,000-iteration organization-clustered bootstrap intervals, three exploratory linear regressions, and a mixed methods joint display based on fictitious interview and documentary patterns. The signal is deliberately constructed to test the code. Its estimates and p-values are not fieldwork findings and cannot be used to characterize Peruvian companies.

## Docker Execution

```powershell
docker build -t unmsm-security-benchmark .
docker run --rm unmsm-security-benchmark
```

The container is configured to run `dvc repro`, the four seeded public-benchmark analyses, both synthetic generators, both scoring paths, and the synthetic association demonstration. It does not require credentials or network access because the small public workbook and all generated fixtures are self-contained. Docker remains unverified until these commands complete in an environment with a Docker engine.

## Reproducibility Controls

- **Git:** versions scripts, parameters, documentation, and the small public source workbook.
- **DVC:** declares the derived CSV as a reproducible output of `dvc.yaml`; a fresh clone can rebuild it with `dvc repro` rather than relying on a private remote.
- **MLflow:** records the seed, bootstrap iterations, analysis scope, summary metrics, and output artifacts for each run.
- **Docker:** fixes the execution environment defined in `requirements.txt`.
- **Four-seed rule:** the pipeline runs seeds `13`, `21`, `42`, and `87` to check that the bootstrap intervals are not an artifact of one random draw.
- **Continuous integration:** `.github/workflows/repository-quality.yml` checks Python compilation, Markdown links, PRISMA arithmetic, DOI coverage, public-pipeline regeneration, synthetic survey scoring, and bias-audit CSV outputs on pushes and pull requests.

## Limits and Responsible Use

The workbook is a deliberately bounded public benchmark, not a probability sample of Peruvian companies. The location field is self-declared by public GitHub organization profiles; public repositories cannot reveal private governance processes; and repositories from the same organization are not independent observations. The synthetic survey file is also not evidence. The workflow therefore avoids causal language, avoids imputing unavailable OpenSSF values as zero, and keeps the planned survey and interview evidence outside this public demonstration.

See [artifact_manifest.md](artifact_manifest.md) and [reproducibility_checklist.md](reproducibility_checklist.md) for the expected artifacts and the recorded verification steps. Docker remains pending until the image can be built and executed in an environment with a Docker engine.

The supporting records in [`docs/`](docs/) provide an English data dictionary, source manifest, environment record, quality checks, concise analysis report, public inspection guidance, presentation evidence map, and reproduction record. The workbook remains the authoritative row-level provenance source.

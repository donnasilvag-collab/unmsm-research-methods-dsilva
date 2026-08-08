# UNMSM Research Methods - Donna Silva

**Author:** Donna Silva
**Research topic:** *Madurez de la gestión de riesgos y eficacia de los controles de desarrollo seguro en empresas peruanas.*

## Purpose

This folder implements the reproducibility component of the study. It follows the Git + DVC + MLflow + Docker architecture required for the course, while respecting the study's current stage: no internal company data, personal data, interview material, or confidential code is stored here.

The executable component analyzes a complementary, public benchmark of software repositories. It makes the data preparation and descriptive comparison reproducible; it does **not** test the relationships proposed for the fieldwork, estimate company-level risk-management maturity, or replace the planned mixed-methods study.

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
+-- docs/                         # Reproducible run visualization
+-- results/                      # Summary tables produced by the experiments
+-- src/
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

This produces:

- `data/public_repo_security_benchmark.csv`, the validated analysis-ready dataset;
- `results/benchmark_summary_seed_*.csv`, one clustered-bootstrap summary per seed;
- `results/seed_stability.csv`, the cross-seed comparison;
- `docs/mlflow_runs.png`, a visual summary of the latest run;
- `mlruns/`, local MLflow metadata with parameters, metrics, and result artifacts.

To inspect the local experiment ledger, run:

```powershell
mlflow ui --backend-store-uri .\mlruns
```

## Docker Execution

```powershell
docker build -t unmsm-security-benchmark .
docker run --rm unmsm-security-benchmark
```

The container runs `dvc repro` and then executes the four seeded analyses. It does not require credentials or network access because the small, public workbook is included in the repository.

## Reproducibility Controls

- **Git:** versions scripts, parameters, documentation, and the small public source workbook.
- **DVC:** declares the derived CSV as a reproducible output of `dvc.yaml`; a fresh clone can rebuild it with `dvc repro` rather than relying on a private remote.
- **MLflow:** records the seed, bootstrap iterations, analysis scope, summary metrics, and output artifacts for each run.
- **Docker:** fixes the execution environment defined in `requirements.txt`.
- **Four-seed rule:** the pipeline runs seeds `13`, `21`, `42`, and `87` to check that the bootstrap intervals are not an artifact of one random draw.

## Limits and Responsible Use

The workbook is a deliberately bounded public benchmark, not a probability sample of Peruvian companies. The location field is self-declared by public GitHub organization profiles; public repositories cannot reveal private governance processes; and repositories from the same organization are not independent observations. The workflow therefore avoids causal language, avoids imputing unavailable OpenSSF values as zero, and keeps the planned survey and interview evidence outside this public demonstration.

See [artifact_manifest.md](artifact_manifest.md) and [reproducibility_checklist.md](reproducibility_checklist.md) for the expected artifacts and the final verification steps.

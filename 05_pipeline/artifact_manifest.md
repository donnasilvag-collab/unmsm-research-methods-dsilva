# Pipeline Artifact Manifest

| Artifact | Purpose | Versioning method | Expected state |
| --- | --- | --- | --- |
| `data/raw/public_repo_security_peru_benchmark.xlsx` | Public source workbook with the repository-level benchmark and documentation sheets | Git | Included; small, public, and non-sensitive |
| `data/create_dataset.py` | Validates the workbook and creates the analysis-ready CSV | Git | Executable |
| `data/public_repo_security_benchmark.csv` | Derived public benchmark used by the analysis | DVC stage output | Rebuilt with `dvc repro` |
| `params.yaml` | Defines seeds, bootstrap iterations, groups, dimensions, and clustering unit | Git | Included |
| `src/train.py` | Produces one clustered-bootstrap descriptive comparison | Git | Executable |
| `src/run_experiments.py` | Executes four seeded analyses and logs them in MLflow | Git + MLflow | Executable |
| `results/benchmark_summary_seed_*.csv` | Per-seed descriptive summaries and confidence intervals | Git artifact | Generated |
| `results/seed_stability.csv` | Compares estimates across the four seeded runs | Git artifact | Generated |
| `docs/mlflow_runs.png` | Visual record of the latest seeded comparison | Git artifact | Generated |
| `mlruns/` | Local MLflow run metadata, metrics, parameters, and artifacts | Local MLflow store (ignored by Git) | Generated locally and inspectable; not committed |
| `Dockerfile` and `requirements.txt` | Rebuild the execution environment | Git | Included |

## Data Boundary

This pipeline must never contain names of participants, institutional documents, interview transcripts, private source code, access tokens, or company-internal control evidence. Those materials belong to the protected fieldwork workflow described in the protocol and require authorization before any analysis is performed.

The present benchmark is public and repository-based. It is retained only as a transparent complement to the future mixed-methods evidence.

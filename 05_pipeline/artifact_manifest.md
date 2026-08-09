# Pipeline Artifact Manifest

| Artifact | Purpose | Versioning method | Expected state |
| --- | --- | --- | --- |
| `data/raw/public_repo_security_peru_benchmark.xlsx` | Public source workbook with the repository-level benchmark and documentation sheets | Git | Included; small, public, and non-sensitive |
| `data/create_dataset.py` | Validates the workbook and creates the analysis-ready CSV | Git | Executable |
| `data/public_repo_security_benchmark.csv` | Derived public benchmark used by the analysis | DVC stage output | Rebuilt with `dvc repro` |
| `params.yaml` | Defines seeds, bootstrap iterations, groups, dimensions, and clustering unit | Git | Included |
| `src/train.py` | Produces one clustered-bootstrap descriptive comparison | Git | Executable |
| `src/run_experiments.py` | Executes four seeded analyses and logs them in MLflow | Git + MLflow | Executable |
| `src/generate_synthetic_fieldwork.py` | Creates deterministic, non-empirical records for scoring tests | Git | Executable; seed fixed by default |
| `src/score_fieldwork.py` | Validates and scores the 32 survey items under the operationalization rules | Git | Executable in public synthetic or protected fieldwork environments |
| `src/generate_synthetic_analysis.py` | Creates 64 synthetic participants, eight synthetic organizations, and fictitious integration evidence | Git | Executable; synthetic seed fixed in `params.yaml` |
| `src/analyze_synthetic_fieldwork.py` | Runs Spearman correlations, clustered intervals, three exploratory regressions, and a joint display | Git | Executable only with the `--synthetic` safeguard |
| `fieldwork/synthetic/survey_responses_synthetic.csv` | Tests the survey schema and controlled missing-data cases | Git artifact | Generated; synthetic only |
| `fieldwork/synthetic/scored_responses_synthetic.csv` | Expected participant-level scoring output for synthetic records | Git artifact | Generated; not a research result |
| `fieldwork/synthetic/organization_summary_synthetic.csv` | Tests aggregation and the minimum reporting threshold | Git artifact | Generated; synthetic only |
| `fieldwork/synthetic/item_missingness_synthetic.csv` | Tests item-level missingness reporting | Git artifact | Generated; synthetic only |
| `fieldwork/synthetic/scoring_metadata_synthetic.json` | Records the source hash, scope, counts, and output set | Git artifact | Generated deterministically |
| `fieldwork/synthetic/association_demo/` | Contains the separate synthetic analytical input, scored data, evidence, numerical outputs, joint display, report, and metadata | Git artifact | Generated deterministically; not a research result |
| `results/benchmark_summary_seed_*.csv` | Per-seed descriptive summaries and confidence intervals | Git artifact | Generated |
| `results/seed_stability.csv` | Compares estimates across the four seeded runs | Git artifact | Generated |
| `docs/mlflow_runs.png` | Visual record of the latest seeded comparison | Git artifact | Generated |
| `docs/source_manifest.csv` and `docs/data_dictionary.csv` | Record source scope, provenance, variables, and interpretive limits | Git | Included and reviewed |
| `docs/environment.md` and `docs/quality_checks.md` | Record the validated runtime and data checks | Git | Included and reviewed |
| `docs/analysis_report.md` | Summarizes the bounded descriptive results and their limits | Git | Included and tied to generated CSV files |
| `docs/presentation_evidence.md` | Maps presentation statements to repository evidence | Git | Included and reviewed |
| `docs/public_inspection_sample.md` and `docs/reproduction_record.md` | Explain public inspection and separate confirmed from pending work | Git | Included and reviewed |
| `mlruns/` | Local MLflow run metadata, metrics, parameters, and artifacts | Local MLflow store (ignored by Git) | Generated locally and inspectable; not committed |
| `Dockerfile` and `requirements.txt` | Rebuild the execution environment | Git | Included |
| `../11_bias_audit/bias_audit.py` | Compares row and owner-clustered uncertainty and runs leave-one-owner-out sensitivity analysis | Git | Executable after `dvc repro` |
| `../11_bias_audit/bias_audit_splits.csv` | Seed-by-dimension before-and-after interval comparison | Git artifact | Generated |
| `../11_bias_audit/owner_influence_diagnostics.csv` | Anonymized leave-one-owner-out diagnostics | Git artifact | Generated |
| `../11_bias_audit/bias_audit_summary.csv` | Dimension-level sensitivity decisions | Git artifact | Generated |
| `../13_presentation/index.html` | Institutional research presentation | Git | Opens locally in a modern browser |
| `../.github/workflows/repository-quality.yml` | Automated repository and reproducibility checks | GitHub Actions | Runs on pushes and pull requests |

## Data Boundary

This pipeline must never contain names of participants, institutional documents, interview transcripts, private source code, access tokens, or company-internal control evidence. Those materials belong to the protected fieldwork workflow described in the protocol and require authorization before any analysis is performed.

The present benchmark is public and repository-based. It is retained only as a transparent complement to the future mixed-methods evidence. The synthetic scoring files are code fixtures, not observations, and must remain labeled as synthetic in every output.

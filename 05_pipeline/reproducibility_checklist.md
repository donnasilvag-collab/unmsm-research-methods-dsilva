# Reproducibility checklist

**Verification date:** 8 August 2026

**Environment:** Windows PowerShell, Python 3.12 virtual environment, dependencies pinned in `requirements.txt`

- [x] The source workbook matches the documented public benchmark and contains no participant, confidential, credential, or proprietary-code fields.
- [x] `dvc repro` completes and creates or verifies `data/public_repo_security_benchmark.csv`.
- [x] The prepared dataset contains 48 rows and the two documented strata: `Peru` and `International benchmark`.
- [x] `params.yaml` identifies repository as the unit of analysis and organization owner as the Peru bootstrap cluster.
- [x] `python src/run_experiments.py` completes seeds 13, 21, 42, and 87.
- [x] Each MLflow run logs the seed, bootstrap iterations, scope note, summary metrics, and output artifacts.
- [x] `results/seed_stability.csv`, the four seed summaries, and `docs/mlflow_runs.png` were regenerated.
- [x] The synthetic fieldwork generator creates 22 labeled records with four controlled missing-data cases.
- [x] The fieldwork scorer applies the 32-item rules and withholds the full organization breakdown when one synthetic group has fewer than five participants.
- [x] The scoring metadata records the synthetic scope, source hash, participant count, organization count, and output set.
- [x] The README states that the benchmark is descriptive and does not establish causal effects or internal company practices.
- [x] Missing OpenSSF scores remain missing and are not converted to zero.
- [x] `python 11_bias_audit/bias_audit.py` regenerates 16 interval records, 36 anonymized owner-influence records, four summary decisions, and the audit chart.
- [x] The operationalization matrix, four instrument files, screening log, quality appraisal, and PRISMA counts pass `src/validate_repository.py`.
- [x] The prospective thesis search plan and institutional HTML presentation pass the repository consistency checks.
- [x] All project Python files compile, Markdown links resolve, and `git diff --check` reports no whitespace errors.
- [x] No private fieldwork data, credentials, `.env` file, virtual environment, MLflow store, or DVC cache is staged for commit.
- [x] GitHub Actions run `31286606880` passed for commit `ad0e455`, repeating Python, Markdown, PRISMA, pipeline, and bias-audit checks on Linux.
- [x] GitHub Actions run `31294241279` passed for commit `2d5d905`, including the synthetic fieldwork and presentation checks.
- [ ] The Docker image builds and completes the same preparation and experiment commands.

## Pending Docker verification

The Docker item remains open because the `docker` command is not installed in the verification environment. The `Dockerfile` has not been presented as tested. Complete this item only after both commands finish successfully in an environment with a Docker engine:

```powershell
docker build -t unmsm-security-benchmark .
docker run --rm unmsm-security-benchmark
```

## Commands executed

```powershell
.\.venv\Scripts\dvc.exe repro
.\.venv\Scripts\python.exe src\run_experiments.py
.\.venv\Scripts\python.exe src\generate_synthetic_fieldwork.py
.\.venv\Scripts\python.exe src\score_fieldwork.py --input fieldwork\synthetic\survey_responses_synthetic.csv --output-dir fieldwork\synthetic --synthetic
cd ..
.\05_pipeline\.venv\Scripts\python.exe 11_bias_audit\bias_audit.py
.\05_pipeline\.venv\Scripts\python.exe 05_pipeline\src\validate_repository.py
git diff --check
```

The CI result should be checked after each push to `main`. A passing workflow verifies the Linux execution path in addition to this local Windows run.

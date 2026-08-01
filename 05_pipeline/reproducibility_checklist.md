# Reproducibility Checklist

Use this checklist before sharing results or submitting the repository.

- [ ] The source workbook matches the documented public benchmark and contains no confidential or personal data.
- [ ] `dvc repro` completes from a fresh clone and creates `data/public_repo_security_benchmark.csv`.
- [ ] The row count is 48 and the two strata are `Peru` and `International benchmark`.
- [ ] `params.yaml` identifies repository as the unit of analysis and organization as the Peru bootstrap cluster.
- [ ] `python src/run_experiments.py` completes all four seeds: 13, 21, 42, and 87.
- [ ] Each MLflow run logs the seed, bootstrap iterations, scope note, and summary metrics.
- [ ] `results/seed_stability.csv` and `docs/mlflow_runs.png` are regenerated after any change to the data, parameters, or scripts.
- [ ] The README states that the benchmark is descriptive and does not establish causal effects or internal company practices.
- [ ] No OpenSSF score is converted from missing to zero.
- [ ] No private fieldwork data, credentials, `.env` file, or DVC cache is staged for commit.
- [ ] The Docker image builds and completes the same preparation and experiment commands.

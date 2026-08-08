# Analytical artifact card

This document follows the reporting intent of Model Cards (Mitchell et al., 2019). The filename is retained for consistency with the course structure. The artifact described here is a repository-level descriptive benchmark, not a trained or deployed predictive model.

## Artifact details

- **Developed by:** Donna Silva, UNMSM Doctoral Program in Deep Technologies.
- **Date:** July 2026.
- **Artifact type:** Parameterized descriptive analysis of publicly observable software-security signals.
- **Research context:** *Madurez de la gestión de riesgos y eficacia de los controles de desarrollo seguro en empresas peruanas.*
- **Implementation:** `05_pipeline/data/create_dataset.py` validates the public workbook. `05_pipeline/src/train.py` performs the seeded clustered-bootstrap comparison. `05_pipeline/src/run_experiments.py` records four runs in MLflow when the complete environment is installed.
- **Versioned inputs:** `05_pipeline/data/raw/public_repo_security_peru_benchmark.xlsx`, `params.yaml`, `dvc.yaml`, and `dvc.lock`.
- **Citation:** this repository, `05_pipeline/` and `07_model_card/`.

No classifier, risk score, or decision threshold is produced. The filename `train.py` is a course-template convention; the script calculates descriptive group comparisons and confidence intervals.

## Intended use

The benchmark has two purposes. First, it provides a transparent public example for testing the Git, DVC, MLflow, and Docker workflow before any confidential fieldwork begins. Second, it describes how selected public repository signals differ between the Peru stratum and an international comparison stratum at the extraction date.

Intended users are the author, course instructor, and reviewers who want to inspect the reproducibility of the public benchmark. Appropriate uses include checking the data dictionary, rerunning the preparation stage, reviewing the bootstrap design, and examining the limits of public observability.

The artifact must not be used to rank companies, certify repository security, infer internal access-control practices, estimate causal effects, or support operational decisions. It cannot replace the surveys, interviews, and authorized institutional evidence planned in the mixed-methods protocol.

## Factors and analytical design

The analytical unit is one public GitHub repository. The dataset has 48 repositories: 24 linked to organization profiles that publicly declare Peru and 24 international benchmark repositories. The Peru stratum contains repositories from 9 organizations, so its bootstrap resampling is clustered by `owner` rather than treating all repository rows as independent.

The four observed dimensions use 0 to 10 composites already defined in the source workbook:

| Dimension | Public signals summarized |
| --- | --- |
| `risk_governance_observed` | Security policy, dependency updates, recent activity, and licensing. |
| `access_control_observed` | CODEOWNERS, explicit workflow permissions, and detected signed commits. |
| `source_code_protection_observed` | SAST, secret scanning, dependency updates, pinned actions, and detected signing. |
| `traceability_observed` | Activity, commit conventions, issue references, merge history, tests, and releases. |

The analysis runs seeds 13, 21, 42, and 87. Each run uses 2,000 bootstrap iterations and reports the difference as Peru minus International benchmark. The four seeds affect the bootstrap intervals, while the repository-level means remain fixed for the versioned dataset.

## Metrics and current results

The main outputs are stratum means, their difference, and a 95% clustered-bootstrap interval. They are descriptive statistics, not estimates of a population parameter or a causal effect.

| Observed dimension | Peru mean | International benchmark mean | Peru minus benchmark |
| --- | ---: | ---: | ---: |
| Risk governance | 3.541667 | 7.239583 | -3.697917 |
| Access control | 0.902778 | 2.638889 | -1.736111 |
| Source-code protection | 1.000000 | 2.856342 | -1.856342 |
| Traceability | 3.196829 | 6.077083 | -2.880254 |

The per-seed summaries and intervals are stored in `05_pipeline/results/benchmark_summary_seed_*.csv`. `seed_stability.csv` preserves all four executions. A negative difference means that the public signals received lower observed scores in the Peru stratum. It does not show that an organization lacks an internal control.

## Evaluation and source data

The source workbook was extracted on 31 July 2026 from public GitHub repository and organization information, Git history, public workflow files, and available OpenSSF Scorecard responses. All 48 repository clones completed successfully. An OpenSSF overall score was available for 19 repositories only, and missing scores remain missing rather than being converted to zero.

The present benchmark has no training or holdout set because it does not fit a predictive model. Its reproducibility depends on preserving the input workbook, the transformation code, the parameters, and the clustering rule. `dvc repro` rebuilds the analysis-ready CSV from the small public workbook; the four seeded scripts then reproduce the result tables.

## Ethical considerations

The dataset contains public repository and organization URLs. It does not contain participant responses, interview transcripts, private source code, credentials, or internal security documents. Public availability does not justify claims about an organization's security maturity. Repository records should be discussed in aggregate and with the documented observability limits.

The location assigned to the Peru stratum is based on self-declared public organization profiles. Several repositories can belong to the same organization, and private controls can be absent from the public record. These features limit both fairness and generalizability. The dataset is unsuitable for automated classification, sanctions, procurement, or reputational scoring.

## Caveats and maintenance

- The sample is intentional and non-probabilistic. It does not represent all Peruvian software companies or all their repositories.
- A public signal is an observation, not a verified control. The absence of `SECURITY.md`, CODEOWNERS, a workflow, or a scorecard result has no direct implication for private practices.
- The repository snapshot is time-bound. Updates require a new extraction date, a revised workbook, a regenerated DVC output, and a clear comparison with the earlier version.
- Any future predictive or inferential model developed from authorized fieldwork requires a new model card and a separate fairness, privacy, and validation assessment.

## Preregistration note

The public benchmark already fixes its unit of analysis, strata, dimensions, cluster rule, seeds, bootstrap iterations, and direction of comparison in `params.yaml`. These choices should remain fixed for the current snapshot. A later thesis analysis should distinguish confirmatory questions from exploratory checks before protected fieldwork data are examined.

## References

- Mitchell, M., Wu, S., Zaldivar, A., Barnes, P., Vasserman, L., Hutchinson, B., Spitzer, E., Raji, I. D., and Gebru, T. (2019). Model Cards for Model Reporting. *Proceedings of the Conference on Fairness, Accountability, and Transparency*, 220-229.
- Gebru, T., Morgenstern, J., Vecchione, B., Vaughan, J. W., Wallach, H., Daume, H., and Crawford, K. (2021). Datasheets for Datasets. *Communications of the ACM, 64*(12), 86-92.

AI tools were used to improve wording and organize this card. The technical description and limits were derived from the versioned workbook, scripts, parameters, and results in this repository.

# Datasheet for the public repository security benchmark

This datasheet follows the documentation approach proposed by Gebru et al. (2021). It describes the public workbook used by `05_pipeline`. The dataset is a bounded repository-level benchmark, not a sample of companies or a substitute for the protected mixed-methods fieldwork.

## Motivation

### Purpose

The dataset was assembled to create a reproducible public benchmark for the study on information security risk management, access control, source-code protection, and software-development traceability in Peruvian companies. It allows the project to test data preparation, versioning, and descriptive analysis without collecting confidential organizational evidence.

### Creator and support

Donna Silva maintains the version included in this repository for the UNMSM course *Research Methods and Scientific Integrity in AI and Advanced Technologies*. The workbook compiles public information from GitHub and available OpenSSF Scorecard responses. Funding information is not recorded in the workbook.

## Composition

### Instances and scope

Each row represents one public GitHub repository. The workbook contains 48 repositories: 24 in the Peru stratum and 24 in the International benchmark stratum. The Peru records are connected to 9 organization profiles that publicly declare Peru. The benchmark is an intentional, non-probabilistic sample. It does not cover private repositories, internal development systems, or all software companies in Peru.

### Information recorded

The workbook retains repository identity and provenance fields, public workflow and policy signals, Git-history aggregates, OpenSSF response metadata, and four observed composite dimensions. The full field-level description is in the `Diccionario` sheet.

| Field group | Examples | Notes |
| --- | --- | --- |
| Provenance | `repository_url`, `organization_url`, `github_api_url`, extraction dates | Supports review of each public observation. |
| Repository context | Language, license, activity, stars, forks, issue count, file count | Descriptive context only. |
| Governance and access signals | `security_policy_present`, `codeowners_present`, workflow permissions, signed-commit ratio | Public proxies with limited coverage. |
| Code-protection signals | Dependency updates, SAST, secret scanning, pinned actions | Based on visible workflow or tree evidence. |
| Traceability signals | Commit conventions, issue references, merges, tests, releases | Heuristic repository-history indicators. |
| External assessment | OpenSSF Scorecard status and overall score when available | Missing availability is not scored as zero. |
| Composite outputs | Four observed dimensions and `observed_overall` | Exploratory 0 to 10 public-observability proxies. |

### Missing values, relationships, and quality

The records are complete enough for the four composite dimensions, but external OpenSSF scores are available for 19 of 48 repositories. Missing external scores remain blank. They must not be imputed as zero. Several repositories may belong to the same owner, which creates a dependency among observations. The pipeline accounts for this in the Peru stratum through organization-clustered bootstrap resampling.

All 48 Git clone attempts recorded an `ok` status. This confirms that the public tree and limited Git history could be inspected at extraction time. It does not verify that every internal process or historical security decision is observable from the repository.

## Collection process

The workbook records a public snapshot extracted on 31 July 2026. Repository and organization metadata came from GitHub public endpoints and visible repository files. Workflow indicators were derived from files in the default branch. Commit-based indicators were calculated from the most recent 100 commits, with recent activity defined within that observed history. OpenSSF data were queried through the public Scorecard API when a response was available.

The Peru location label is based on a public organization-profile declaration. The International benchmark stratum provides a comparison group; it is not a control group and was not drawn through probability sampling. The workbook includes source URLs, API endpoints, HTTP statuses, and clone status to make this process inspectable.

## Preprocessing, labeling, and analysis-ready data

`05_pipeline/data/create_dataset.py` reads the `Datos_repositorios` sheet, checks the required fields, verifies the 48-row composition and unique identifiers, validates the 0 to 10 composite scales, sorts by `record_id`, and writes `public_repo_security_benchmark.csv`. The script preserves the original public indicators so a reported composite can be traced back to the workbook.

The source workbook defines the composite dimensions. They summarize public signals and should be described as observed proxies. They are not labels for whether a company is secure, compliant, mature, or vulnerable.

## Uses

### Appropriate uses

- Reproducing the public descriptive comparison in `05_pipeline`.
- Inspecting the provenance and operational definitions of public repository signals.
- Demonstrating DVC-based data preparation and seeded bootstrap analysis for the course.

### Inappropriate uses

- Measuring the information-security maturity of a company or its private systems.
- Ranking organizations, vendors, people, or repositories for reputational or procurement decisions.
- Claiming that observed differences establish causation, prevalence, or national representativeness.
- Training a production model or combining these records with confidential fieldwork data without an approved protocol.

## Distribution and access

The small public source workbook is versioned in Git at `05_pipeline/data/raw/public_repo_security_peru_benchmark.xlsx`. The analysis-ready CSV is a DVC stage output and can be regenerated with `dvc repro`. The repository also contains parameters, scripts, result tables, and a Docker definition.

No separate dataset license is declared in this repository. GitHub and OpenSSF remain the sources of the underlying public metadata, and their respective terms apply. Anyone reusing the benchmark should retain the provenance fields and the stated limitations.

## Maintenance

Donna Silva maintains this course version. The dataset is a dated snapshot. A future update should preserve the prior workbook, record a new extraction date, document changes to the sampling frame or indicator rules, regenerate the DVC output, and avoid comparing scores across versions without noting the changed observation date.

The final thesis dataset will require a separate datasheet because it may include authorized survey, interview, or institutional evidence that cannot be stored in this public repository.

## References

- Gebru, T., Morgenstern, J., Vecchione, B., Vaughan, J. W., Wallach, H., Daume, H., and Crawford, K. (2021). Datasheets for Datasets. *Communications of the ACM, 64*(12), 86-92.

AI tools were used to improve wording and organize this datasheet. The dataset description was derived from the versioned workbook, data dictionary, preparation script, and pipeline documentation in this repository.

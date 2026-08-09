# Reproduction record

The detailed checklist is maintained in [`../reproducibility_checklist.md`](../reproducibility_checklist.md). This shorter record separates confirmed execution from pending work.

## Confirmed through 9 August 2026

- DVC reported that the data stage was up to date.
- Four MLflow-backed seeded analyses completed.
- The synthetic survey fixture and scoring outputs regenerated deterministically.
- The 64-record synthetic analysis fixture regenerated with eight synthetic organizations.
- Spearman intervals, three exploratory regressions, and the joint display regenerated from labeled synthetic inputs.
- The owner-clustered bias audit regenerated its numerical outputs and chart.
- Repository validation, Python compilation, Markdown-link checks, and whitespace checks passed.
- GitHub Actions completed the expanded workflow successfully on Windows-independent Linux infrastructure.

## Not yet confirmed

- The Docker image has not been built or run in an environment with a Docker engine.
- The fieldwork instruments have not completed expert validation, pilot testing, or institutional approval.
- No participant or confidential company data have been collected.

These pending items are not software failures. They mark the boundary between a reproducible methodological demonstration and the later empirical study.

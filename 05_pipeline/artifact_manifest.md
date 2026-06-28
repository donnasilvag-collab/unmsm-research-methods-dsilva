# Minimum Pipeline Artifact Inventory

## Purpose

This document defines the minimum artifacts that the reproducible pipeline should contain once the study moves from the planning stage to the analysis stage.

## Planned Artifacts

| Artifact | Purpose | Main tool | Status in this delivery |
| --- | --- | --- | --- |
| Anonymized quantitative dataset | To gather structured responses for quantitative analysis | DVC | Defined |
| Variable dictionary | To specify the name, type, scale, and meaning of each variable | Git | Defined |
| Transformation record | To preserve the trail of cleaning, coding, and changes applied to the data | Git + DVC | Defined |
| Analytical runs | To record parameters, assumptions, and outputs of quantitative analysis | MLflow | Defined |
| Integration evidence | To connect quantitative results with qualitative findings and interpretive decisions | Git | Defined |

## Minimum Conventions

- Identifiable data will not be stored in the repository.
- Every analytical artifact should include a date, version, and brief description.
- Relevant transformations should be traceable from the input to the reported result.

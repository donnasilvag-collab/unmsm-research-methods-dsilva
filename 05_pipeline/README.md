# UNMSM Research Methods - Donna Silva

**Author:** Donna Silva

**Research topic:** Influence of information security risk management on the effectiveness of access control, source code protection, and software development traceability in Peruvian companies: protocol for a mixed methods study.

## Purpose of This Folder

This folder presents the technical-documentary deliverable for step 5 of the course. Its role is not yet to host real data or final scripts, but to specify clearly how the reproducible workflow of the study will be organized once authorized and anonymized inputs become available.

## Scope of This Delivery

At this stage, the reproducible component is resolved at the level of design and traceability. For that reason, the folder includes:

- an explicit description of the reproducible workflow;
- a minimum inventory of expected artifacts;
- a checklist to ensure consistency among data, analysis, and results;
- basic criteria for using Git, DVC, and MLflow in a way that is coherent with the sensitive nature of the study.

## Reproducibility Approach

- **Git** will be used to version documents, instruments, scripts, and methodological decisions.
- **DVC** will be reserved for versioning anonymized datasets, variable matrices, questionnaire versions, and tabular derivatives that should not be stored directly in Git.
- **MLflow** will be used as a log of analytical executions, especially to record alternative quantitative processing configurations, analytical assumptions, and comparable results.

## Reproducible Workflow

1. Collection or consolidation of anonymized data from surveys, interviews, and authorized institutional documents.
2. Versioning of the tabular input and its transformations through DVC.
3. Cleaning, coding, and generation of analytical variables.
4. Execution of the quantitative analysis and registration of parameters, outputs, and metrics in MLflow.
5. Integration with qualitative findings and preservation of traceable evidence within the repository.

## Minimum Pipeline Artifacts

- `README.md`: explains the purpose of the folder and the overall workflow.
- `artifact_manifest.md`: defines which files or products should exist when the pipeline is executed with real inputs.
- `reproducibility_checklist.md`: summarizes the minimum controls required to maintain traceability and consistency.

## Expected Outputs

- An anonymized quantitative dataset.
- A variable dictionary and coding criteria.
- A record of reproducible analytical runs.
- Traceability evidence linking input, transformation, analysis, and result.

## Current Status

The pipeline is documented as a preliminary reproducible design, sufficient for this phase of the course. Real data, executable scripts, and `.dvc` files are not yet incorporated because the study has not entered fieldwork or empirical processing; however, the structure, versioning criteria, and traceability logic are already defined.

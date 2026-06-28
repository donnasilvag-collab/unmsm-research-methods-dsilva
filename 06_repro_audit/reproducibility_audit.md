# Reproducibility Audit

## Scope

This preliminary audit evaluates whether the repository currently provides the minimum conditions required to support a reproducible research workflow for the study on the influence of information security risk management on access control, source code protection, and software development traceability in Peruvian companies.

## Overall Assessment

The repository is well structured and clearly organized by course progression. The main documents from the root through `05_pipeline` define the research problem, methodological stance, protocol logic, literature base, and the intended reproducibility workflow. At the same time, the project remains at a documentary stage rather than an execution stage, which means reproducibility is currently defined by design and traceability rules rather than by runnable analytical artifacts.

## Strengths Identified

- The repository structure is easy to follow and reflects the sequence of course deliverables.
- The research problem is consistently formulated across the main sections.
- The selected method is justified in relation to the nature of the problem.
- The literature review and gap analysis provide a defensible foundation for the protocol.
- The pipeline folder now includes a documented workflow, a minimum artifact inventory, and a reproducibility checklist.

## Current Limitations

- The repository does not yet include real data, executable scripts, `.dvc` files, or MLflow outputs.
- Reproducibility is presently documented at a conceptual level, not yet demonstrated through a full analytical run.
- Some later folders outside the scope of this review remain intentionally empty, which is acceptable for the present stage but should be addressed in future iterations if the project expands.

## Audit Table

| Component reviewed | Current status | Observation |
| --- | --- | --- |
| Repository structure | Adequate | The numbering and folder logic make the project easy to navigate. |
| Problem consistency | Adequate | The same research framing is preserved across the core documents. |
| Methodological documentation | Adequate | Paradigm, method, and protocol are documented with sufficient clarity for a course delivery. |
| Literature traceability | Adequate | The review question, screening logic, prioritized studies, and gap analysis are explicit. |
| Reproducibility design | Partial but sufficient | The workflow is clearly documented, but not yet operationalized with code or tracked data. |
| Technical execution evidence | Not yet available | No scripts, tracked datasets, or analytical runs are included at this stage. |

## Recommendations

1. Keep the current documentary structure as the official basis for the course submission.
2. If the project later advances beyond the course stage, incorporate executable scripts, DVC-tracked artifacts, and MLflow records.
3. Maintain the current traceability logic when data collection begins, especially regarding anonymization, file versioning, and transformation logs.

## Conclusion

For the current academic stage, the repository meets the expectations of a well-documented methodological project and provides a credible reproducibility design. It should not yet be described as a fully operational reproducible pipeline, but it can be defended as a structured and traceable preparatory implementation.

# Prospective search protocol for the thesis review

## Status

This protocol has not yet been executed. It defines how the course-stage review will be expanded without changing the recorded PRISMA counts or reconstructing files that were not preserved in June 2026. The new search will receive its own date, exports, deduplication log, screening decisions, quality assessment, and PRISMA flow.

## Review question

What empirical and methodological evidence explains the association between information security risk-management maturity and the effectiveness of access control, source-code protection, and software-development traceability in organizational software development?

## Planned sources

The search will cover Scopus, Web of Science Core Collection, IEEE Xplore, ACM Digital Library, and Semantic Scholar. Each source has a defined role in [`database_search_plan.csv`](database_search_plan.csv). Access restrictions, platform limits, and any departure from this plan will be recorded on the execution date.

## Concept blocks

The query will combine three concept blocks. Syntax will be adapted to each database without changing the concepts.

```text
("information security risk management" OR "security risk management" OR "risk management maturity")
AND
("secure software development" OR "secure SDLC" OR SSDLC OR DevSecOps OR "software security")
AND
("access control" OR authorization OR "source code protection" OR repository OR traceability OR auditability)
```

The search will cover English and Spanish records. The publication interval will retain the current lower boundary of 2006 and extend through the date of the thesis search. Any additional geographic query for Peru or Latin America will be run separately so that it does not remove relevant international evidence from the main search.

## Records to preserve

For every source, the researcher will retain the exact query, search date, platform, filters, result count, and unedited RIS or BibTeX export. A combined record file will retain the source identifier of each item. Deduplication decisions will preserve the retained record, removed record, matching fields, and reason.

Title and abstract screening will record one decision and one predefined reason for every record. Full-text screening will retain the citation, DOI or stable identifier, publication-status check, decision, reason, reviewer, and date. A second reviewer will independently assess a documented sample. Disagreements and their resolution will remain in the audit trail.

## Quality and synthesis

The final review will select an appraisal tool appropriate to each study design before quality scoring begins. The current project-specific rubric may support comparison, but it will not replace a recognized design-specific tool when one is available. The synthesis will distinguish direct organizational evidence from framework proposals, technical experiments, reviews, and contextual sources.

## Version control

The course-stage review remains unchanged as a historical record. The thesis search will use a dated subdirectory or release tag. Any amendment to databases, criteria, dates, language limits, or screening procedure will state what changed, why it changed, and whether the change occurred before or after results were examined.

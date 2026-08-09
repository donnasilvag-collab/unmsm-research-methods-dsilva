# Public benchmark analysis report

## Analytical question

The executable benchmark asks whether four public repository signals differ between a bounded Peru stratum and an international reference stratum. It tests the analysis workflow without using participant or confidential company data. It does not answer the doctoral fieldwork question.

## Method

The dataset contains 48 public repositories, split evenly between the two strata. The Peru stratum includes 24 repositories associated with 9 public organization profiles. The point estimate is the difference in repository means, calculated as Peru minus International benchmark. A 2,000-iteration bootstrap resamples the Peru stratum by organization owner and the reference stratum by repository. Seeds 13, 21, 42, and 87 test interval stability.

## Reproduced descriptive results

The point estimates do not change across seeds because the bootstrap affects uncertainty, not the observed means. The table reports the widest range reached by the four lower and upper interval limits.

| Observed public proxy | Difference | Range of 95% interval limits across seeds |
| --- | ---: | ---: |
| Risk governance | -3.698 | -6.330 to -1.223 |
| Access control | -1.736 | -2.986 to -0.476 |
| Source code protection | -1.856 | -3.214 to -0.443 |
| Development traceability | -2.880 | -4.707 to -1.337 |

Negative values indicate that the observed public signals were lower in the Peru stratum within this selected benchmark. They do not establish weaker internal controls, a country effect, a causal relationship, or population prevalence.

## Sensitivity to organization dependence

The bias audit found that owner-clustered intervals were 1.34 to 1.52 times as wide as row-level intervals. No leave-one-owner-out analysis reversed the direction of a point estimate. Risk governance, access control, and source code protection still triggered the prespecified owner-sensitivity review rule; traceability remained stable for bounded descriptive use.

These results justify organization-aware uncertainty and cautious aggregate reporting. They do not justify removing an organization or ranking individual repositories.

## Missingness and measurement limits

Only 19 of 48 repositories had an available OpenSSF overall score. The remaining observations stay missing. Public repository files and histories cannot reveal private identity management, internal risk registers, approval decisions, incident records, or undocumented controls. The international stratum is a reference set, not a matched or probability-sampled control group.

## Status of the doctoral evidence

Fieldwork has not begun. The survey, interviews, and authorized document review remain the evidence needed to assess the relationship stated in the research question. The benchmark demonstrates transparent preparation, parameter control, repeated seeded analysis, dependence-aware uncertainty, and auditable reporting.

# Operationalization matrix

## Purpose and measurement period

This matrix translates the study constructs into observable measures for the quantitative phase. Survey respondents will assess practices they have directly observed during the previous 12 months. Documentary evidence and interviews will help interpret the scores, but they will not replace or silently alter a participant's answers.

The survey is a draft instrument. It must pass expert review, cognitive testing, pilot testing, and ethics approval before fieldwork. The sources below guide item content; they do not imply that the resulting scale has already been validated.

## Matrix

| Variable | Dimension | Indicator | Source | Item | Scale | Scoring rule |
| --- | --- | --- | --- | --- | --- | --- |
| Information security risk-management maturity (explanatory) | Governance and accountability | Assigned responsibility, management review, and risk-informed priorities | NIST CSF 2.0, Govern; OWASP SAMM, Governance | RM01-RM02 | Frequency from 1 to 5; `N/A` or insufficient knowledge is missing | Mean of both items. Both answers are required. |
| Information security risk-management maturity (explanatory) | Risk identification | Periodic identification of software assets, threats, vulnerabilities, and dependencies | NIST CSF 2.0, Identify; NIST SP 800-53 Rev. 5, RA-3 | RM03-RM04 | Frequency from 1 to 5; `N/A` or insufficient knowledge is missing | Mean of both items. Both answers are required. |
| Information security risk-management maturity (explanatory) | Assessment and prioritization | Consistent assessment criteria and priority based on likelihood, impact, and exposure | NIST CSF 2.0, GV.RM and ID.RA; NIST SP 800-53 Rev. 5, RA-3 and RA-7 | RM05-RM06 | Frequency from 1 to 5; `N/A` or insufficient knowledge is missing | Mean of both items. Both answers are required. |
| Information security risk-management maturity (explanatory) | Risk treatment | Defined owners, deadlines, acceptance criteria, and follow-up for selected responses | NIST CSF 2.0, Govern and Respond; NIST SSDF 1.1, PO and RV | RM07-RM08 | Frequency from 1 to 5; `N/A` or insufficient knowledge is missing | Mean of both items. Both answers are required. |
| Information security risk-management maturity (explanatory) | Monitoring and review | Reassessment after relevant changes and management review of overdue or residual risk | NIST CSF 2.0, Identify and Govern; OWASP SAMM, Strategy and Metrics | RM09-RM10 | Frequency from 1 to 5; `N/A` or insufficient knowledge is missing | Mean of both items. Both answers are required. |
| Information security risk-management maturity (explanatory) | Training and risk culture | Role-based guidance and safe escalation of security concerns | NIST CSF 2.0, Protect; OWASP SAMM, Education and Guidance | RM11-RM12 | Frequency from 1 to 5; `N/A` or insufficient knowledge is missing | Mean of both items. Both answers are required. |
| Information security risk-management maturity (explanatory) | Learning and continuous improvement | Use of incidents, exceptions, audit findings, and metrics to revise practices | NIST CSF 2.0, Govern and Identify; NIST SSDF 1.1, RV | RM13-RM14 | Frequency from 1 to 5; `N/A` or insufficient knowledge is missing | Mean of both items. Both answers are required. |
| Effectiveness of secure-development controls (outcome) | Access-control effectiveness | Unique identities, least privilege, protected privileged changes, periodic review, timely removal, and exception monitoring | NIST SP 800-53 Rev. 5, AC-2, AC-3, AC-5, and AC-6; NIST SSDF 1.1, PO.5 | AC01-AC06 | Frequency from 1 to 5; `N/A` or insufficient knowledge is missing | Mean when at least 4 of 6 items are answered. |
| Effectiveness of secure-development controls (outcome) | Source-code protection | Repository protection, approved changes, secret prevention, automated checks, dependency control, and protected release artifacts | NIST SSDF 1.1, PS and PW; OWASP SAMM, Implementation and Verification | SC01-SC06 | Frequency from 1 to 5; `N/A` or insufficient knowledge is missing | Mean when at least 4 of 6 items are answered. |
| Effectiveness of secure-development controls (outcome) | Development traceability | Linkage among request, change, review, test, approval, deployment, and retrievable audit evidence | NIST SP 800-53 Rev. 5, AU-2, AU-3, AU-6, AU-12, CM-3, and SA-10; NIST SSDF 1.1, PO and PW | TR01-TR06 | Frequency from 1 to 5; `N/A` or insufficient knowledge is missing | Mean when at least 4 of 6 items are answered. |

## Scale anchors

All substantive survey items use one frequency scale:

| Value | Anchor |
| ---: | --- |
| 1 | Never |
| 2 | Rarely |
| 3 | Sometimes |
| 4 | Usually |
| 5 | Consistently |
| Missing | Not applicable or insufficient knowledge |

## Composite scores

Each score remains continuous in the primary analysis.

1. Calculate the seven risk-management dimension means only when both items in a dimension are present.
2. Calculate the overall risk-management maturity score when at least five of the seven dimension means are available. The overall score is their unweighted mean.
3. Calculate each control-effectiveness score when at least four of its six items are available.
4. Retain the original 1 to 5 metric for analysis. A 0 to 100 presentation score may be calculated as `(mean - 1) * 25`, but it will not replace the original score.
5. Do not create low, medium, or high categories for the primary analysis. Any later category must have an empirical or normative basis and must be documented before outcome analysis.
6. Do not impute `N/A`, insufficient-knowledge, or unanswered items as zero. Report item and scale missingness.

## Evidence alignment

The document-review form records whether authorized evidence supports, partly supports, does not support, or cannot assess a reported practice. This is a triangulation result, not a second numerical scale. Material disagreement between survey and documentary evidence will guide the interview phase and will be reported as a finding rather than resolved through an undocumented score change.

## Source framework references

- Joint Task Force. (2020). *Security and privacy controls for information systems and organizations* (NIST Special Publication 800-53, Revision 5). National Institute of Standards and Technology. https://doi.org/10.6028/NIST.SP.800-53r5
- OWASP Foundation. (2020). *OWASP Software Assurance Maturity Model, version 2.0*. https://owaspsamm.org/model/
- Pascoe, C., Quinn, S., and Scarfone, K. (2024). *The NIST Cybersecurity Framework (CSF) 2.0* (NIST CSWP 29). National Institute of Standards and Technology. https://doi.org/10.6028/NIST.CSWP.29
- Souppaya, M., Scarfone, K., and Dodson, D. (2022). *Secure Software Development Framework (SSDF) version 1.1* (NIST Special Publication 800-218). National Institute of Standards and Technology. https://doi.org/10.6028/NIST.SP.800-218

---

**AI support statement:** AI tools assisted with table formatting, wording review, and consistency checks. Donna Silva selected the constructs, approved the scoring rules, and remains responsible for validation and use of the instrument.

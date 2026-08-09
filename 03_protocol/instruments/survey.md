# Structured survey draft

## Study information

**Study:** *Madurez de la gestión de riesgos y eficacia de los controles de desarrollo seguro en empresas peruanas*

**Researcher:** Donna Silva

This survey asks about software-development and information-security practices that you have personally observed during the previous 12 months. It does not request names, credentials, source code, repository addresses, vulnerability details, customer information, or incident records. Participation is voluntary. A participant may skip a question or stop before submission without penalty.

Estimated completion time will be established during cognitive testing and the pilot. The instrument will not be deployed until the study receives the required ethics or institutional approval.

## Eligibility and consent

| Code | Question | Response |
| --- | --- | --- |
| EL01 | Are you at least 18 years old? | Yes / No |
| EL02 | During the previous 12 months, have you worked in a company with formal operations in Peru and an identifiable software-development function? | Yes / No |
| EL03 | Does your role give you direct knowledge of at least one practice covered by this survey? | Yes / No |
| CO01 | Have you read the study information and do you freely consent to participate? | Yes / No |

If any eligibility answer or consent is `No`, the survey ends without collecting substantive responses.

## Non-identifying context

These fields support interpretation and coverage checks. Categories may be combined or suppressed when reporting to prevent identification.

| Code | Question | Response |
| --- | --- | --- |
| CT01 | Broad role | Software development / Technical leadership / DevOps or platform / Quality or testing / Information security / Other relevant role |
| CT02 | Experience in software-related work | Less than 2 years / 2 to 5 years / 6 to 10 years / More than 10 years |
| CT03 | Approximate company workforce | 1 to 49 / 50 to 249 / 250 or more / Prefer not to answer |
| CT04 | Main delivery approach observed | Agile / DevOps or continuous delivery / Hybrid / Other / Insufficient knowledge |
| CT05 | Anonymous organization code supplied by the researcher | Controlled code; no company name |

## Response scale

For items `RM01` to `TR06`, select the answer that best describes the practice during the previous 12 months:

`1 Never` | `2 Rarely` | `3 Sometimes` | `4 Usually` | `5 Consistently` | `N/A or insufficient knowledge`

## Information security risk-management maturity

### Governance and accountability

| Code | Item |
| --- | --- |
| RM01 | Responsibility for information-security risks affecting software development was assigned to identifiable roles. |
| RM02 | Management reviewed software-security risks when setting priorities, resources, or delivery decisions. |

### Risk identification

| Code | Item |
| --- | --- |
| RM03 | The company maintained a current view of software assets, repositories, dependencies, and services relevant to risk assessment. |
| RM04 | Teams identified threats, vulnerabilities, and operational weaknesses throughout software development rather than only before release. |

### Assessment and prioritization

| Code | Item |
| --- | --- |
| RM05 | Identified risks were assessed using consistent criteria for likelihood, impact, and exposure. |
| RM06 | Security work was prioritized according to documented risk rather than only urgency or individual preference. |

### Risk treatment

| Code | Item |
| --- | --- |
| RM07 | Accepted, mitigated, transferred, or avoided risks had an assigned owner and a documented decision. |
| RM08 | Risk-treatment actions had deadlines or review conditions and were followed until closure or formal acceptance. |

### Monitoring and review

| Code | Item |
| --- | --- |
| RM09 | Risks were reassessed after material changes to architecture, dependencies, access, or deployment processes. |
| RM10 | Overdue actions, exceptions, and residual risks were reviewed at an appropriate management level. |

### Training and risk culture

| Code | Item |
| --- | --- |
| RM11 | People involved in software delivery received security guidance suited to their responsibilities. |
| RM12 | Team members could report a security concern or challenge an unsafe delivery decision without retaliation. |

### Learning and continuous improvement

| Code | Item |
| --- | --- |
| RM13 | Incidents, near misses, audit findings, or control failures led to documented changes in development practices. |
| RM14 | The company reviewed risk and control measures over time to determine whether practices were improving. |

## Effectiveness of secure-development controls

### Access control

| Code | Item |
| --- | --- |
| AC01 | Access to code repositories and delivery tools used unique, attributable user identities. |
| AC02 | Permissions reflected job responsibilities and the principle of least privilege. |
| AC03 | Privileged changes required independent approval or another documented compensating control. |
| AC04 | Access rights were reviewed periodically and after relevant role changes. |
| AC05 | Access was removed or adjusted promptly when employment, assignment, or contractual need ended. |
| AC06 | Exceptional or privileged access was logged and reviewed for inappropriate use. |

### Source-code protection

| Code | Item |
| --- | --- |
| SC01 | Protected branches or equivalent controls prevented unreviewed changes to important code. |
| SC02 | Changes to important code required review and recorded approval before integration. |
| SC03 | The development process prevented or detected credentials and secrets in source code. |
| SC04 | Automated checks examined code or dependencies for security weaknesses before release. |
| SC05 | Third-party components were identified and updated through a documented vulnerability-response process. |
| SC06 | Build and release artifacts were protected against unauthorized alteration. |

### Development traceability

| Code | Item |
| --- | --- |
| TR01 | A software change could be linked to its business request, requirement, defect, or approved maintenance need. |
| TR02 | The repository history identified who made and reviewed each material change. |
| TR03 | Test evidence could be linked to the change or release it supported. |
| TR04 | Release approval and deployment records could be linked to the relevant version or build. |
| TR05 | Logs and records needed for an authorized review were retained for a defined period. |
| TR06 | The company could reconstruct the path of a material change from request to production without relying on one person's memory. |

## Optional closing comment

`CM01`: Without naming a person, company, system, or vulnerability, is there a practice that would help explain your answers?

The free-text response is optional. The researcher will remove identifying or security-sensitive detail before analysis. If a response contains information that should not have been collected, it will be quarantined and handled under the data-management and incident procedures.

## Scoring note

The researcher will score this instrument according to [operationalization_matrix.md](../operationalization_matrix.md). `N/A`, insufficient knowledge, and unanswered items remain missing. The primary analysis uses continuous scores and reports missingness; it does not turn a missing answer into a failed control.

---

**AI support statement:** AI tools assisted with drafting and language review. Donna Silva approved the item content and remains responsible for expert review, participant testing, ethics approval, and final administration.

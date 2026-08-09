# Targeted document-review form

## Review boundary

This form records only evidence that an organization has explicitly authorized for the study. The researcher will ask for the least sensitive artifact needed to assess a practice. A redacted extract, screenshot, template, or demonstration may be sufficient. No proprietary source code, credentials, vulnerability details, private repository address, customer information, raw security log, or unrestricted copy of a confidential document belongs in the research repository.

## Administrative record

| Field | Entry |
| --- | --- |
| Organization code |  |
| Evidence code |  |
| Review date |  |
| Reviewer | Donna Silva |
| Evidence owner or authorizing role | Record role only |
| Artifact type | Policy / Procedure / Redacted record / Demonstration / Other |
| Date or version of artifact |  |
| Access mode | Controlled view / Redacted copy / Authorized extract |
| Retention decision | No copy / Protected extract / Protected redacted copy |
| Destruction or return date, if applicable |  |

## Evidence assessment

Use one result for each applicable row: `Supported`, `Partly supported`, `Not supported`, or `Cannot assess`. `Not supported` means the authorized evidence was sufficient to test the indicator and did not substantiate it. `Cannot assess` means access or content was insufficient. It is not a failed control.

| Code | Indicator examined | Acceptable evidence examples | Result | Evidence note and locator |
| --- | --- | --- | --- | --- |
| DR01 | Risk roles and accountability are assigned. | Approved role matrix, policy section, committee terms |  |  |
| DR02 | Software-security risks are recorded and prioritized using defined criteria. | Redacted risk-register fields, approved assessment procedure, workflow demonstration |  |  |
| DR03 | Risk-treatment decisions have owners and review conditions. | Redacted treatment record, approval workflow, exception template |  |  |
| DR04 | Risk and control performance is reviewed over time. | Redacted dashboard, meeting template, review schedule |  |  |
| DR05 | Repository and delivery-tool access follows an approval process. | Access procedure, redacted access request, controlled demonstration |  |  |
| DR06 | Access is reviewed and removed after role or status changes. | Review schedule, redacted removal record, offboarding procedure |  |  |
| DR07 | Privileged or exceptional access is logged and reviewed. | Redacted exception procedure, logging configuration description, review record |  |  |
| DR08 | Important branches or equivalent assets are protected from unreviewed change. | Redacted repository rule, controlled settings demonstration, approved procedure |  |  |
| DR09 | Secrets and vulnerable dependencies are prevented or detected. | Approved scanning procedure, redacted pipeline result, remediation workflow |  |  |
| DR10 | Build and release artifacts are protected against unauthorized alteration. | Release procedure, signing or integrity-control description, controlled demonstration |  |  |
| DR11 | Changes link to requests, reviews, and test evidence. | Redacted work-item example, traceability report, controlled demonstration |  |  |
| DR12 | Release approval and deployment records link to a defined version or build. | Redacted release record, deployment approval, version register |  |  |
| DR13 | Relevant audit evidence has a defined retention period. | Retention schedule, logging standard, approved procedure |  |  |
| DR14 | Incidents or findings lead to tracked process improvements. | Redacted corrective-action record, lessons-learned template, revision history |  |  |

## Triangulation note

| Field | Entry |
| --- | --- |
| Survey dimension or interview theme examined |  |
| Relationship to other evidence | Convergent / Complementary / Contradictory / Not comparable |
| Plausible explanation to test in interview |  |
| Additional authorized evidence needed |  |
| Reporting restriction |  |

## Handling decision

Before ending the review, confirm that the retained material contains no unnecessary identifier or security-sensitive detail. If an artifact cannot be safely retained, record only the evidence code, the assessment, and a non-sensitive note. Store protected extracts according to `10_data_mgmt/data_management_plan.md`; never commit them to Git.

---

**AI support statement:** AI tools assisted with form structure and language review. Donna Silva remains responsible for authorization, evidence minimization, assessment, and secure handling.

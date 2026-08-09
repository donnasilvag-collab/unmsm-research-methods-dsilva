# Instrument validation procedure

## Status and purpose

The survey, interview guide, and document-review form are draft instruments. Validation will determine whether they are understandable, relevant to the constructs, feasible to administer, and sufficiently consistent for an exploratory mixed methods study. No document in this folder should be described as validated until the steps below are completed and recorded.

## Step 1: construct and source review

Create an item-to-construct map using `operationalization_matrix.md`. Confirm that each item measures one defined practice, uses a 12-month reference period, and does not request confidential technical detail. Check the mapping against NIST CSF 2.0, NIST SSDF 1.1, NIST SP 800-53 Rev. 5, and OWASP SAMM 2.0.

Remove duplicate items and wording that combines two practices in a way that prevents a clear answer. Record every addition, deletion, and wording change in an instrument changelog.

## Step 2: expert content review

Recruit three to five reviewers with complementary experience in information-security risk management, secure software development, research methods, or psychometrics. Reviewers must disclose relevant conflicts and must not receive identifiable fieldwork data.

Each reviewer will rate every substantive item for relevance, clarity, and alignment with its assigned dimension on a four-point scale. The review record will include comments and a decision for each item: retain, revise, move, or remove. Item-level and scale-level content-validity indices may be reported as descriptive evidence, but the decision will also consider written comments and construct coverage. The researcher will not retain an unclear item merely to achieve a numerical threshold.

## Step 3: cognitive interviews

Conduct cognitive interviews with approximately five to eight practitioners who resemble the target participants but are not part of the final analytic sample where feasible. Ask them to explain how they interpreted selected items, chose an answer, used the 12-month period, and distinguished `Never` from `N/A or insufficient knowledge`.

Record comprehension problems, missing response options, sensitive wording, and terms that vary by role or company. Revise the instruments before the pilot and keep a versioned decision log.

## Step 4: pilot administration

Pilot the revised survey with approximately 15 to 25 eligible practitioners outside the final sample where access permits. The pilot tests administration, missingness, completion time, response distribution, and scoring code. It is not a substitute for the main study and will not be pooled with fieldwork unless the protocol and consent process explicitly allow pooling before collection.

Review:

- item and scale missingness, including use of `N/A or insufficient knowledge`;
- floor and ceiling concentration;
- corrected item-to-total relationships within each proposed scale;
- internal consistency using McDonald's omega when estimable, with Cronbach's alpha reported only as a familiar supplementary statistic;
- comments suggesting ambiguity, discomfort, or an unrepresented practice;
- whether the planned minimum-item scoring rules retain enough complete cases.

Small pilot estimates will be treated as unstable. They inform revision rather than prove reliability or validity.

## Step 5: interview and document-form trial

Run at least two trial interviews and two simulated or authorized document reviews before fieldwork. Check whether the guide produces explanations rather than yes-or-no confirmations, whether prompts expose unnecessary sensitive detail, and whether the document form can distinguish `Not supported` from `Cannot assess`.

Revise interviewer instructions and evidence examples when a trial produces leading questions, duplicate prompts, or an unsafe request. Trial records that contain identifiable or confidential material will remain outside Git and follow the data-management plan.

## Step 6: scoring and analysis verification

Write a scoring script before outcome analysis. Test it with synthetic records that cover complete responses, permitted partial responses, all missing-response types, and invalid values. Verify that:

- both items are required for each risk-management dimension;
- at least five dimension scores are required for overall maturity;
- at least four of six items are required for each outcome;
- missing values never become zero;
- the optional 0 to 100 transformation preserves ordering and does not create categories.

The final codebook, scoring script, and synthetic tests will be versioned in the repository. Protected pilot and fieldwork data will not be committed.

## Step 7: freeze and approval

Freeze the field version only after methodological review and the required ethics or institutional approval. Assign a version number and date to every instrument. Later changes require a documented reason, impact assessment, and decision about comparability with responses already collected.

## Validation record template

| Stage | Planned sample or reviewers | Completion evidence | Main finding | Decision | Version produced |
| --- | --- | --- | --- | --- | --- |
| Construct and source review | Researcher and methodological adviser | Item-source map and changelog | Pending | Pending | Draft |
| Expert content review | 3 to 5 reviewers | Rating sheet and decision log | Pending | Pending | Pending |
| Cognitive interviews | 5 to 8 practitioners | Protected notes and issue summary | Pending | Pending | Pending |
| Survey pilot | 15 to 25 practitioners | Protected pilot data and aggregate diagnostics | Pending | Pending | Pending |
| Interview and document-form trial | At least 2 of each | Protected trial notes and revision log | Pending | Pending | Pending |
| Scoring verification | Synthetic test cases | Versioned code and test output | Pending | Pending | Pending |
| Ethics or institutional review | Required reviewing body | Approval or formal determination | Pending | Pending | Field version |

## Methodological reference

Boateng, G. O., Neilands, T. B., Frongillo, E. A., Melgar-Quiñonez, H. R., and Young, S. L. (2018). Best practices for developing and validating scales for health, social, and behavioral research: A primer. *Frontiers in Public Health, 6*, 149. https://doi.org/10.3389/fpubh.2018.00149

---

**AI support statement:** AI tools assisted with drafting, organization, and consistency checks. Donna Silva selected the validation sequence and remains responsible for reviewer selection, ethics compliance, decisions, and final instrument approval.

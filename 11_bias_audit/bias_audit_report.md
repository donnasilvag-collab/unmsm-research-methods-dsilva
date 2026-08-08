# Bias audit report

## 11.1. Audit purpose and boundary

This report examines possible sources of bias in the public repository benchmark and in the planned mixed methods fieldwork for the study, *Madurez de la gestión de riesgos y eficacia de los controles de desarrollo seguro en empresas peruanas*.

Conventional model bias audits use classifiers, protected attributes, favorable outcomes, and before-and-after fairness metrics. Those elements do not exist in the current project. `05_pipeline/` contains a descriptive comparison of public repository signals, not a predictive model, risk score, automated decision, or person-level classification. The appropriate audit therefore focuses on representation, selection, measurement, aggregation, and interpretation rather than applying demographic-parity or equalized-odds metrics without a valid denominator.

This document has two parts. The first audits the data and claims that already exist in the public benchmark. The second sets review rules for the survey and interview components before fieldwork begins. It does not claim that the future fieldwork has already been collected or audited.

## 11.2. Audit object and available evidence

| Item | Current state |
| --- | --- |
| Analytical artifact | A parameterized descriptive benchmark of public software-security signals. No classifier is trained or deployed. |
| Unit of analysis | One public GitHub repository. |
| Dataset composition | 48 repositories: 24 in the Peru stratum and 24 in the International benchmark stratum. The Peru repositories belong to 9 public organization profiles that declare Peru. |
| Observation date | 31 July 2026. The dataset is a dated snapshot, not a longitudinal record. |
| Outcome variables | Four 0 to 10 observability proxies: `risk_governance_observed`, `access_control_observed`, `source_code_protection_observed`, and `traceability_observed`. |
| Source coverage | Public GitHub repository and organization information, visible files and history, and available OpenSSF Scorecard responses. OpenSSF overall scores are available for 19 of 48 records. |
| Existing uncertainty control | The Peru stratum uses owner-clustered bootstrap resampling because multiple repositories can belong to the same organization. Each seed uses 2,000 iterations. |

The Peru and International benchmark strata are analytical groups, not protected groups. The location label is based on self-declared public organization-profile information. It should not be read as nationality, residence, ethnicity, or an exhaustive representation of Peruvian software development.

## 11.3. What fairness metrics do and do not apply

Disparate impact, statistical parity difference, equal opportunity difference, average odds difference, and calibration measure the behavior of a decision system across defined groups. They require a prediction or selection outcome, a valid reference label, and a defensible group definition. The current benchmark has none of these elements.

The four-fifths rule therefore does not apply to the public benchmark. Calculating a pass or fail result would create false precision because there is no hiring, lending, admission, sentencing, or other allocation decision in the analysis. The observed scores are not favorable or unfavorable outcomes assigned to people.

This limitation does not remove the need for scrutiny. A non-predictive dataset can still be biased through who is visible, which signals are recorded, how groups are formed, and how findings are communicated. The audit treats those mechanisms as the relevant risks for this artifact.

## 11.4. Measured descriptive differences

The point differences below are Peru minus International benchmark. They describe the bounded public snapshot and remain fixed across bootstrap runs.

| Observed dimension | Peru mean | International benchmark mean | Difference |
| --- | ---: | ---: | ---: |
| Risk governance | 3.541667 | 7.239583 | -3.697917 |
| Access control | 0.902778 | 2.638889 | -1.736111 |
| Source-code protection | 1.000000 | 2.856342 | -1.856342 |
| Traceability | 3.196829 | 6.077083 | -2.880254 |

All four public means are lower in the Peru stratum for this snapshot. This does not show that a Peruvian organization lacks an internal control. Repositories differ in purpose, visibility, maintenance, open-source orientation, and the signals exposed on a default branch. The benchmark records public observability, not an organization's complete security posture.

The before-and-after audit tests one specific analytical risk: treating repositories owned by the same organization as independent observations. The before estimate resamples individual Peru repository rows. The after estimate resamples Peru owners and retains all repositories associated with each selected owner. The International benchmark uses repository-level resampling in both cases so that the comparison isolates the treatment of dependence within the Peru stratum.

| Observed dimension | Mean naive 95% interval width | Mean owner-clustered 95% interval width | Change |
| --- | ---: | ---: | ---: |
| Risk governance | 3.365039 | 5.049860 | +1.684821 |
| Access control | 1.858073 | 2.490878 | +0.632805 |
| Source-code protection | 1.979381 | 2.737715 | +0.758334 |
| Traceability | 2.224056 | 3.372842 | +1.148785 |

The clustered intervals are wider in all four dimensions when averaged across seeds 13, 21, 42, and 87. The point estimates do not change. Wider intervals are not a worse result; they make the limited amount of independent organizational evidence more visible. This correction does not address selection bias, measurement bias, or the non-probabilistic comparison frame.

`bias_audit.py` regenerates the 16 seed-by-dimension records in `bias_audit_splits.csv` and the comparison in `before_after_chart.png`. The chart is a before-and-after dependency correction, not a protected-group fairness intervention.

## 11.5. Bias-risk register for the public benchmark

| Risk mechanism | Evidence or reason for concern | Consequence if ignored | Existing control | Remaining action |
| --- | --- | --- | --- | --- |
| Selection and coverage bias | The sample is intentional and non-probabilistic. It contains public repositories only. Private repositories and companies without a visible GitHub organization are outside the frame. | Results could be misread as representative of all Peruvian software companies. | Documentation states the sample is bounded and non-representative. | Retain this limitation in every result table, presentation, or derivative analysis. |
| Location misclassification | Peru membership relies on a public organization profile that declares Peru. | The stratum could be interpreted as a legal, national, or workforce classification that it is not. | The data card states the origin of the location field. | Refer to a "Peru stratum" rather than to all Peruvian companies or developers. |
| Measurement and observability bias | The proxies use visible policies, workflow files, Git history, and public repository settings. Internal controls may exist without public evidence. | An absent public signal could be mistaken for an absent internal control. | Documentation defines the variables as observed proxies and treats missing OpenSSF scores as missing, not zero. | Preserve the phrase "not observed" in codebooks, tables, and narrative results. |
| Owner clustering | Several Peru repositories belong to the same organization. Repository rows are not fully independent. | Unclustered uncertainty estimates would exaggerate the amount of independent evidence. | Peru bootstrap resampling clusters by `owner`. | Keep the cluster rule fixed for the current snapshot and state the 9-organization count. |
| Comparison-frame bias | The International benchmark is not a probability-sampled control group. Repository purpose, ecosystem, maintenance capacity, and public exposure may differ. | A descriptive difference could be interpreted as a country effect. | The pipeline labels the comparison descriptive and non-causal. | Do not use causal language or present the international group as a baseline of expected maturity. |
| Missing external assessment | OpenSSF overall scores are present for 19 of 48 records. | Replacing missing values with zero would penalize repositories without an available response. | The workbook and pipeline leave missing values blank. | Keep missingness visible in any extended analysis and avoid completeness claims for this field. |
| Snapshot and history bias | The workbook records one extraction date and limited observed history. | A temporary change or older public history could be treated as a durable organizational practice. | Extraction date and collection method are documented. | Version any refresh separately and compare snapshots only with an explicit date and method note. |
| Reputational harm | Named public repositories can invite unsupported conclusions about organizations. | Descriptive research could become an informal ranking or procurement signal. | The model card and ethics protocol prohibit ranking and operational use. | Report aggregate results and do not publish a league table of organizations or repositories. |

## 11.6. Assessment of current controls

The current public artifact does not need a model-level mitigation such as reweighing, threshold adjustment, or post-processing because it does not make a prediction. It does require design and analysis controls that reduce avoidable misinterpretation:

- the repository is explicit that the measures are public observability proxies;
- the data preparation script keeps the original public indicators so a composite can be traced to its inputs;
- the before-and-after audit shows how row-level resampling understates uncertainty when one owner contributes several repositories;
- the main analysis uses organization-clustered bootstrap resampling for the Peru stratum;
- unavailable OpenSSF values remain missing rather than being converted to zero;
- the model card, datasheet, ethics protocol, and data management plan prohibit causal, company-level, and reputational conclusions.

These controls reduce specific risks, but they do not turn the dataset into a representative sample or a direct measure of internal security practice. The numerical after table concerns dependence correction only. It is not evidence of improved demographic fairness, and it does not assess a decision model.

## 11.7. Audit plan for the future fieldwork

The protocol anticipates purposive recruitment of approximately 50 to 80 practitioners from 6 to 10 organizations, followed by interviews with 10 to 15 key informants. This approach can produce useful explanatory evidence, but access through professional networks, organization permissions, job role, seniority, company size, and geographic concentration can shape whose experience enters the study.

Before recruitment, the researcher will record the intended organization and participant coverage in a protected study log. The log will document recruitment channel, organization code, broad role, participation stage, and reason for non-inclusion when known. It will not be published with identifiers. If organization size, region, sector, or other contextual categories are needed to evaluate coverage, they will be collected in broad categories and only after the ethics and instrument review confirm that they are necessary.

The study does not currently require demographic attributes such as race, ethnicity, gender identity, disability, or age. They will not be added merely to produce a fairness statistic. If a future research question requires such information, the protocol, consent process, collection rationale, access controls, disclosure risk, and analysis plan must be revised before collection.

| Fieldwork risk | Review before analysis | Response if the risk is present |
| --- | --- | --- |
| Recruitment depends on a narrow professional network or a small number of organizations. | Compare the protected coverage log with the stated target population and recruitment plan. | Describe the access limitation, seek authorized additional channels where feasible, and avoid claims beyond the observed participants. |
| One role, seniority level, or organizational profile dominates the responses. | Produce internal counts by approved broad categories and inspect whether some relevant perspectives are absent. | Interpret results as role-specific or organization-specific when necessary; do not treat one group as the general experience. |
| Participants may feel pressure because access is facilitated by an employer. | Review consent records and recruitment messages for voluntary participation safeguards. | Separate recruitment from managerial decisions and prevent organizations from seeing individual participation or responses. |
| A quotation can identify a person or organization through combined details. | Perform disclosure review before reporting qualitative material. | Generalize, redact, aggregate, or withhold the quotation, as specified in `09_ethics/` and `10_data_mgmt/`. |
| Missing responses differ by recruitment path or question topic. | Document item nonresponse and withdrawals without attempting to infer private reasons. | Report the missingness, avoid filling it with assumptions, and qualify any comparison affected by it. |

## 11.8. Decision rules for interpretation and dissemination

| Situation | Required decision |
| --- | --- |
| A public result could be read as a ranking of an organization. | Remove the organization-level comparison and report the result in aggregate with its observability limit. |
| A public proxy is missing. | Record it as "not observed" or missing. Do not convert it to an absence of the internal control. |
| A fieldwork subgroup has few participants or could reveal an organization. | Suppress or generalize the subgroup result and avoid identifiable quotation. |
| A recruitment pathway excludes a relevant perspective. | Record the limitation and do not generalize the result to that excluded perspective. |
| A future analysis introduces a predictive model or an automated recommendation. | Pause the analysis and prepare a separate model, privacy, validation, and fairness assessment before deployment or dissemination. |

## 11.9. Limits of this audit

This audit does not measure discrimination against protected groups because the current artifact contains no person-level outcome, protected attribute, or model decision. It also does not establish that a public repository signal is biased in any specific direction. It identifies the conditions under which the signal can be misunderstood or unevenly available.

The future fieldwork review cannot be completed until recruitment, consent, and collection occur. Its purpose is to make the checks and decision points visible before access patterns harden into an unexamined sample. The audit must be updated when the fieldwork instruments, recruitment route, and approved data environment are finalized.

## References

Chouldechova, A. (2017). Fair prediction with disparate impact: A study of bias in recidivism prediction instruments. *Proceedings of Machine Learning Research, 81*, 153-163.

Kleinberg, J., Mullainathan, S., & Raghavan, M. (2017). Inherent trade-offs in the fair determination of risk scores. *Proceedings of Innovations in Theoretical Computer Science*.

Mitchell, M., Wu, S., Zaldivar, A., Barnes, P., Vasserman, L., Hutchinson, B., Spitzer, E., Raji, I. D., & Gebru, T. (2019). Model cards for model reporting. *Proceedings of the Conference on Fairness, Accountability, and Transparency*, 220-229.

Raji, I. D., Smart, A., White, R. N., Mitchell, M., Gebru, T., Hutchinson, B., Smith-Loud, J., & Theron, D. (2020). Closing the AI accountability gap: Defining an end-to-end framework for internal algorithmic auditing. *Proceedings of the Conference on Fairness, Accountability, and Transparency*, 33-44.

Suresh, H., & Guttag, J. V. (2021). A framework for understanding sources of harm throughout the machine learning life cycle. *Proceedings of the 2021 ACM Conference on Equity and Access in Algorithms, Mechanisms, and Optimization*, 1-9.

---

**AI support statement:** AI tools were used to organize the report, improve clarity, and check editorial consistency. The audit scope, interpretation limits, and methodological decisions remain the author's responsibility.

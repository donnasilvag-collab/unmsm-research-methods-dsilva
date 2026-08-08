# Draft Ethics Protocol for Doctoral Research

## 9.1. Purpose and Scope

This ethics protocol supports the planned study, **Madurez de la gestión de riesgos y eficacia de los controles de desarrollo seguro en empresas peruanas**. It translates the methodological commitments in `03_protocol/protocol_v0.1.md` into practical safeguards for fieldwork, data handling, reporting, and the use of public evidence.

The research has two clearly separated components:

- **Planned mixed methods fieldwork:** a survey of approximately 50 to 80 software-development practitioners from 6 to 10 Peruvian organizations, followed by semistructured interviews with 10 to 15 voluntary key informants selected to explain relevant quantitative patterns.
- **Public repository benchmark:** a bounded descriptive dataset of 48 public GitHub repositories. It uses repository-level metadata and observable security proxies only. It is not a substitute for fieldwork, does not include confidential organizational information, and does not support causal conclusions about companies or individuals.

The study may involve developers, technical leaders, DevOps practitioners, quality practitioners, and security practitioners. It also concerns the organizations in which they work because accounts of security practices can reveal operational details. For that reason, protecting people and organizations is part of the research design, not a final editing step.

No recruitment, survey, interview, or collection of non-public organizational material will begin until the applicable institutional ethics or review requirements have been confirmed.

## 9.2. Data Sources and Collection Boundaries

| Source | Planned information | Ethical boundary |
| --- | --- | --- |
| Public repository benchmark | Public repository metadata, public organization information, visible workflow and history signals, and OpenSSF Scorecard results when available. | The benchmark uses only information already made public by repository owners. Results are descriptive, do not rank organizations, and are not combined with confidential fieldwork records. |
| Structured survey | Voluntary responses on risk identification, evaluation, treatment, monitoring, access control, source code protection, and traceability practices. | The instrument will collect the minimum information needed for analysis. It will not request passwords, access tokens, source code, private URLs, incident evidence, or client information. |
| Semistructured interviews | Participants' interpretations of controls, routines, adoption barriers, and differences between documented procedures and daily practice. | Interviews will not seek proprietary code, credentials, system configurations, vulnerabilities, incident details, or trade secrets. The researcher will redirect the conversation if such information is offered. |
| Organizational documents | Voluntarily provided, non-confidential or redacted policies, guidelines, procedures, or other evidence relevant to the research questions. | Documents will be used only with explicit authorization and within the agreed scope. Sensitive material will not be uploaded to the public repository or used as an example that identifies an organization. |

If contact information is required to arrange an interview, it will be collected separately from survey responses and used only for that purpose. A recording will not be made without explicit consent. Any transcript used for analysis will replace direct identifiers with participant and organization codes.

## 9.3. Informed Consent and Voluntary Participation

Participation in the survey and interviews will be voluntary and limited to adults who can make an informed decision about participation. Before taking part, each participant will receive a clear explanation of the study purpose, the expected activities, the types of data collected, the intended uses of the findings, and the available contact channel for questions.

The consent process will state that participants may skip questions, stop participation at any time, and decline to discuss information they consider sensitive. Participation or non-participation will not be reported to a supervisor or employer. Individual responses will not be shared with organizations.

The consent information will also explain the practical limit to withdrawal: a participant may request removal of identifiable material before the data have been irreversibly anonymized, aggregated, or integrated into the analysis. Once an anonymized result cannot reasonably be linked back to a person, removing it may no longer be possible.

Recruitment messages and interview arrangements will avoid creating pressure through reporting lines. When an organization facilitates access, it will not receive a list of participants, individual responses, or identifiable interview extracts.

## 9.4. Risk Assessment and Mitigation

| Potential risk | Why it matters in this study | Planned safeguard |
| --- | --- | --- |
| Employment or reputational harm | A participant's account of weak controls or informal practices could be linked to a person, team, or organization. | Minimize identifiers, separate contact details from research data, report results in aggregate, and generalize or suppress quotations that could reveal a small organization or a distinctive role. |
| Accidental disclosure of security-sensitive information | Discussions about access control, repositories, and traceability may reveal credentials, configurations, vulnerabilities, or incident details. | Exclude these topics from the instrument, remind participants of the boundary, redirect the discussion, and redact material that exceeds the approved scope. |
| Undue influence in the workplace | Employees may feel expected to participate when access is facilitated by their organization. | Make participation independent from employment decisions, provide a direct consent process, and prevent managers from accessing participation records or individual data. |
| Re-identification through combinations of details | A role, company size, technology stack, and quoted event can identify a participant even if names are removed. | Use broad descriptions, aggregate across organizations where possible, review quotations before publication, and omit unnecessary contextual detail. |
| Reputational inference from public repository data | Public signals can be misread as a complete assessment of an organization's security posture. | Treat benchmark variables as observable proxies, describe their limits, avoid rankings, and make no claims about internal controls, maturity, or causality from public data alone. |
| Unauthorized access to fieldwork data | Survey exports, recordings, or documents could contain personal or organizationally sensitive information. | Store fieldwork material in access-controlled, protected storage separate from the public repository. Apply least-privilege access and do not publish raw fieldwork data. |

The study offers no security audit, certification, or remediation service. This boundary prevents participants and organizations from interpreting the research interaction as an assurance activity.

## 9.5. Expected Benefits

Participants should not expect a direct personal benefit from taking part. The expected contribution is collective: the study may clarify how information security risk management relates to access control, source code protection, and traceability in Peruvian software-development settings.

At an organizational level, the aggregated findings may support reflection on secure development practices. They will not be presented as an individual performance evaluation or as evidence that a particular organization meets or fails a security standard.

## 9.6. Confidentiality and Reporting

Confidentiality will be protected through data minimization, pseudonymization where contact is necessary, and careful reporting. Participant identifiers and organization identifiers will be kept separate from analytical records. Any linkage file needed during data collection will be stored apart from the main study data and will not be placed in the public repository.

Public outputs will use aggregated results and de-identified quotations. Names of people, teams, and organizations will not be published unless an explicit authorization is obtained and the disclosure remains consistent with the approved ethics process. The public repository will document instruments, procedures, code, and non-sensitive derived outputs, not raw survey responses, audio files, unredacted transcripts, private documents, or security-sensitive evidence.

The public benchmark is different because its repository-level sources are already public. Even so, its results will be reported as bounded observations rather than as a reputational score for a company. Public repository URLs will not be used to connect benchmark records with confidential fieldwork records.

## 9.7. Storage, Access, Retention, and Sharing

The public benchmark and its reproducibility materials are maintained in this repository because they contain public, bounded, repository-level information. Any fieldwork data will be stored separately in protected, access-controlled storage appropriate to the institutional requirements confirmed before recruitment.

Only the researcher and authorized academic supervisors or reviewers, when required, will have access to identifiable fieldwork material. Access permissions will follow the principle of least privilege. The project repository will not be used to store identifiable data, proprietary source code, credentials, security configurations, recordings, incident material, or documents that were not cleared for public release.

The final retention period for fieldwork data will be set before recruitment in accordance with the applicable institutional ethics decision and personal-data obligations. At the end of that period, identifiable material and the linkage file will be securely deleted or irreversibly de-identified. Only anonymized, approved outputs may be shared as part of the academic record.

## 9.8. Conflicts of Interest and Researcher Responsibilities

The current research protocol does not document a funding, employment, consulting, or organizational relationship that would determine recruitment or interpretation. Before fieldwork begins, any relationship that could affect access to participants, participant freedom, analysis, or reporting will be declared and managed through the applicable institutional process.

The researcher is responsible for maintaining the study boundaries, protecting confidential information, documenting methodological decisions, and reporting limitations that could affect interpretation. Access to an organization will not be treated as permission to disclose its practices, tools, or internal security conditions.

## 9.9. AI-Specific Considerations

The public benchmark is not a predictive model and does not make automated decisions about people. Its repository-level measures are observable proxies, so they must not be interpreted as a definitive security classification of an organization or a person.

No external generative AI service may receive raw interview text, unredacted survey exports, internal documents, source code, credentials, or direct identifiers unless a separate data-processing assessment, explicit participant information, and the required institutional authorization have been completed. If a digital tool is used for transcription, coding, or language support, its role, data-access conditions, and effect on the analysis will be documented.

The study will also avoid creating a misleading fairness claim. Publicly observable repository signals are uneven across organizations, and organizations that agree to participate in fieldwork may not represent all Peruvian software-development companies. These limitations will be reported rather than hidden through broad generalizations.

## 9.10. Decision Rules Before and During Fieldwork

| Situation | Required action |
| --- | --- |
| Ethics or institutional requirements have not been confirmed. | Do not recruit participants or collect non-public data. |
| A participant offers credentials, proprietary code, vulnerability details, or incident evidence. | Stop or redirect that part of the conversation and exclude the material from the study record. |
| A quotation or table could identify a person or organization. | Aggregate, generalize, redact, or omit it before dissemination. |
| A new digital or AI-enabled service would process fieldwork data. | Assess the data flow and obtain the required participant information and authorization before use. |
| A public benchmark result could be read as a rating of a named organization. | Report the methodological limitation and avoid individual ranking or claims about internal security maturity. |

## 9.11. Ethical and Academic Framework

The protocol is guided by the principles of respect for persons, beneficence, and justice described in the *Belmont Report*. In the Peruvian context, it also follows the commitments already established in the research protocol: protection of personal data under Peruvian Law No. 29733 and scientific-integrity expectations under the National Code of Scientific Integrity approved by CONCYTEC through Presidential Resolution No. 028-2024-CONCYTEC-P.

These references do not replace the review requirements of the relevant university or institutional body. Their purpose here is to make the planned safeguards visible before data collection and to provide a record that can be reviewed and refined when the fieldwork instruments are finalized.

## 9.12. Reflection on Fairness and the COMPAS Case

The COMPAS case illustrates how a score can appear neutral while producing consequences that differ across groups. This study does not deploy a classifier or risk score for people. However, a comparable ethical risk would arise if public repository indicators were used to label a Peruvian organization as secure or insecure without access to its internal context.

For that reason, the benchmark will remain descriptive, its sampling and observability limits will be explicit, and its results will not be used to rank organizations, make employment decisions, or infer internal security maturity. The mixed methods design adds context, but it does not remove the obligation to report selection limits and uneven visibility in public data.

## References

The National Commission for the Protection of Human Subjects of Biomedical and Behavioral Research. (1979). *The Belmont Report: Ethical principles and guidelines for the protection of human subjects of research*.

Consejo Nacional de Ciencia, Tecnologia e Innovacion Tecnologica. (2024). *National Code of Scientific Integrity*. Presidential Resolution No. 028-2024-CONCYTEC-P.

Peru. (2011). *Law No. 29733: Personal Data Protection Law*.

Angwin, J., Larson, J., Mattu, S., & Kirchner, L. (2016). Machine bias. *ProPublica*.

---

**AI support statement:** AI tools were used to help organize the document, improve the clarity of the language, and check editorial consistency. The research topic, methodological decisions, ethical boundaries, and final academic responsibility remain with the author.

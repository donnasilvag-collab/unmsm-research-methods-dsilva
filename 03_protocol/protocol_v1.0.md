# Research protocol (v1.0)

## 3.1. Title

**Madurez de la gestión de riesgos y eficacia de los controles de desarrollo seguro en empresas peruanas**

## 3.2. Abstract

Software development companies depend on code repositories, privileged access, integration and deployment pipelines, and activity logs. These assets create a broad risk surface in which unauthorized access, source code leakage, and incomplete traceability can affect both operational continuity and trust. Although companies may have risk policies and security tools, there is limited empirical evidence on whether risk-management maturity translates into effective controls during everyday software development in Peru.

This protocol proposes an explanatory sequential mixed methods study in Peruvian software development companies. The quantitative phase will examine the relationship between information security risk-management maturity and three outcomes: access-control effectiveness, source code protection, and development traceability. The qualitative phase will use semistructured interviews and authorized document review to explain patterns that need organizational context. The study is intended to identify technical, organizational, and human factors associated with stronger controls and to formulate practical recommendations for secure software development. A separate public-repository benchmark supports methodological testing but does not replace fieldwork or measure internal company security.

## 3.3. Introduction and problem statement

### Problem statement

Digital transformation has increased organizational dependence on software and exposure to risks associated with unauthorized access, source code leakage, weak change governance, and incomplete activity records. In agile, DevOps, and continuous-integration environments, delivery pressure can also create a gap between formally documented controls and the way those controls operate in routine technical work.

Recent literature reports uneven integration of security throughout the software development life cycle. Policies and tools alone do not show whether access is governed consistently, repositories are protected, or changes can be traced from request to deployment. Control effectiveness also depends on leadership, training, role clarity, monitoring, and operational discipline.

The central problem is therefore empirical: it remains unclear how and to what extent information security risk-management maturity is associated with the effectiveness of access control, source code protection, and development traceability in Peruvian software development companies. It is also necessary to explain why companies with apparently similar formal controls may obtain different operational results.

### Relevance of the study

The study addresses a fragmented area of software-security research by examining risk management and three connected control dimensions within one design. Its practical value lies in producing evidence that can inform access governance, repository protection, auditing, compliance, and capability development without exposing proprietary code or security-sensitive information.

## 3.4. Brief literature review

The preliminary literature points to four recurring findings. Security is not always integrated across the full development life cycle; operational speed can increase exposure when DevOps governance is weak; effective controls depend on organizational behavior as well as technology; and measurement alone may not explain why formal practices succeed or fail in a specific setting.

Khan et al. (2022) describe persistent weaknesses in the consistent integration of security practices across software development. Kolisnichenko et al. (2022) argue that risk management should extend across DevOps activities rather than appear as a late control. Valdes-Rodriguez et al. (2023) identify continuing challenges in the adoption of security practices in agile environments. Tsai et al. (2025), in turn, propose performance baselines that connect proactive and reactive security management with secure software-development outcomes. These studies support a design that combines measurement with contextual explanation.

## 3.5. Research questions and objectives

### General research question

**How and to what extent is information security risk-management maturity associated with the effectiveness of access control, source code protection, and software development traceability in Peruvian companies, and how do organizational, human, and operational factors help explain the observed relationships?**

### Specific research questions

- Which dimensions of information security risk management have the strongest relationship with access-control effectiveness, source code protection, and software development traceability?
- What differences are observed among participating companies with different levels of risk-management maturity?
- How do developers, technical leaders, and security practitioners explain gaps between formal controls and actual development practices?
- Which organizational and operational factors help explain the quantitative results?

### General objective

To analyze the association between information security risk-management maturity and the effectiveness of access control, source code protection, and software development traceability in Peruvian companies, and to examine the organizational, human, and operational factors that help explain the observed relationships.

### Specific objectives

- Characterize information security risk-management maturity in participating Peruvian software development companies.
- Evaluate the relationship between that maturity and access-control effectiveness, source code protection, and software development traceability.
- Identify organizational, human, and operational factors that explain differences observed in the quantitative phase.
- Integrate quantitative and qualitative evidence to formulate recommendations for secure software development.

## 3.6. Methodology

### Paradigm and design

The study adopts a pragmatic paradigm and an explanatory sequential mixed methods design. The quantitative phase will identify relationships between the study variables. The qualitative phase will then examine selected results in greater depth, including cases where formal controls and reported practice appear inconsistent. Integration will occur when quantitative findings guide qualitative sampling and again when both forms of evidence are interpreted together.

### Scope

The study has an explanatory and applied scope. It does not seek to build a new technological artifact. Its purpose is to produce evidence about the relationship between risk management and critical controls within software development, while accounting for the organizational setting in which those controls operate.

### Context, population, and sample

The population of interest comprises Peruvian companies whose regular operations include software development and the management of code repositories, access mechanisms, and traceability processes. The study will prioritize companies located in Metropolitan Lima or with formal operations in Peru that use agile, DevOps, or continuous-integration practices. Teams that develop software only as an informal internal activity and organizations without an identifiable software development function are outside the study population.

The quantitative phase will use purposive, non-probability sampling. It is expected to include approximately 50 to 80 participants from 6 to 10 organizations. Relevant roles include software developers, technical leaders, DevOps practitioners, quality practitioners, and security practitioners. The qualitative phase will select 10 to 15 voluntary key informants based on the quantitative results, with attention to contrasting maturity profiles and results that appear especially consistent or contradictory.

### Data-collection techniques and instruments

- **Structured survey:** measures practices related to risk identification, assessment, treatment, monitoring, access control, source code protection, and traceability.
- **Semistructured interviews:** examine decisions, adoption barriers, operational tensions, and differences between written procedures and everyday practice.
- **Targeted document review:** examines authorized policies, procedures, guidelines, logs, or other institutional evidence needed to interpret the findings.

### Variables and dimensions

The explanatory variable is information security risk-management maturity. Its preliminary dimensions are governance, risk identification, assessment, treatment, monitoring, training, and follow-up. The outcome variables are access-control effectiveness, source code protection, and software development traceability. Operational definitions and instrument items will be reviewed before fieldwork and documented with their source and scoring rule.

### Analysis strategy

The quantitative phase will include descriptive analysis, assessment of instrument consistency, and association analysis. Correlations, group comparisons, and regression models may be used if their assumptions are supported by the collected data. Organization-level dependence and the limited purposive sample will be considered when selecting inferential procedures and interpreting uncertainty.

The qualitative phase will use thematic analysis. A documented coding process will identify recurring explanations, divergent cases, and contextual conditions. Integration will use joint interpretation and meta-inferences so that qualitative evidence can explain, qualify, or challenge the quantitative findings. No causal conclusion will be made solely from cross-sectional associations.

### Public benchmark boundary

The public repository analysis in `05_pipeline/` is a descriptive methodological benchmark based on visible GitHub signals. It is not part of the protected participant dataset, does not measure internal company security maturity, and cannot support national, causal, or organization-level conclusions. An absent public signal means only that the control was not observed in the bounded public source.

## 3.7. Ethical considerations

The study may involve sensitive descriptions of internal security practices. Participation will be voluntary and based on informed consent. Recruitment will avoid managerial pressure, and withdrawal will be possible without penalty. The study will not request proprietary source code, credentials, private repository addresses, security configurations, vulnerability details, trade secrets, or incident evidence.

Data will be coded at collection and stored in access-controlled locations. Public reports will not identify people, teams, or organizations unless specific authorization permits it. Quotations and small subgroups will undergo disclosure review before publication. Raw survey responses, recordings, unredacted transcripts, contact information, and confidential organizational documents will remain outside the public repository.

The protocol will be aligned with Peruvian Law No. 29733 on Personal Data Protection and the National Code of Scientific Integrity approved through CONCYTEC Presidential Resolution No. 028-2024-CONCYTEC-P. The required institutional or ethics review will be completed before participant recruitment begins.

## 3.8. Expected results

- A documented characterization of information security risk-management maturity in the participating companies.
- Evidence on the association between that maturity and the three control dimensions.
- An explanation of organizational and operational factors linked to gaps between formal and sustained controls.
- Recommendations for strengthening secure development in agile, DevOps, and continuous-integration settings.
- A reproducible public repository containing approved documentation, instruments, code, and non-sensitive derived results.

## 3.9. Timeline and feasibility

### Preliminary timeline

| Period | Planned work |
| --- | --- |
| Months 1-4 | Refine the protocol, update the literature review, design instruments, and prepare the ethics submission. |
| Months 5-8 | Conduct preliminary instrument validation, contact organizations, and manage fieldwork access. |
| Months 9-14 | Collect and analyze quantitative data. |
| Months 15-20 | Select explanatory cases, conduct interviews, and complete qualitative analysis. |
| Months 21-24 | Integrate results, discuss findings, and formulate recommendations. |
| Months 25-30 | Draft articles or thesis chapters and consolidate the reproducible repository. |
| Months 31-36 | Complete the thesis, conduct internal review, and prepare for the defense. |

### Feasibility and provisions

The design is feasible if enough organizations authorize access and participants can discuss security practices without exposing sensitive material. The schedule therefore allows time for institutional coordination, ethics review, instrument validation, and complementary collection when the first recruitment route provides insufficient coverage.

### Preliminary resource estimate

| Resource | Estimated cost |
| --- | ---: |
| Interview transcription and systematization support | PEN 1,500 |
| Travel, meetings, and fieldwork coordination | PEN 1,200 |
| Digital tools, secure storage, and backups | PEN 800 |
| Operational contingencies | PEN 1,000 |

## 3.10. Preliminary bibliography

Cleland-Huang, J., Gotel, O. C. Z., Hayes, J. H., Mader, P., & Zisman, A. (2014). Software traceability: Trends and future directions. In *Proceedings of the Future of Software Engineering* (pp. 55-69).

CONCYTEC. (2024). *National Code of Scientific Integrity*. Presidential Resolution No. 028-2024-CONCYTEC-P.

Joint Task Force. (2020). *Security and privacy controls for information systems and organizations* (NIST Special Publication 800-53, Revision 5). National Institute of Standards and Technology.

Khan, R. A., Khan, S. U., Khan, H. U., & Ilyas, M. (2022). Systematic literature review on security risks and its practices in secure software development. *IEEE Access, 10*, 5456-5481.

Kolisnichenko, O., Kolomytsev, M., & Nosok, S. (2022). Software security risk management in DevOps methodology. *Theoretical and Applied Cybersecurity, 3*(1).

OWASP Foundation. (2020). *OWASP SAMM version 2*.

Peruvian Law No. 29733. *Personal Data Protection Law*.

Pillitteri, V. (2022). *Assessing security and privacy controls in information systems and organizations* (NIST Special Publication 800-53A, Revision 5). National Institute of Standards and Technology.

Sanchez-Gordon, M.-L., & Colomo-Palacios, R. (2020). Security as culture: A systematic literature review of DevSecOps. In *Proceedings of the IEEE/ACM 42nd International Conference on Software Engineering Workshops* (pp. 266-269).

Souppaya, M., Scarfone, K., & Dodson, D. (2022). *Secure Software Development Framework (SSDF) version 1.1: Recommendations for mitigating the risk of software vulnerabilities* (NIST Special Publication 800-218). National Institute of Standards and Technology.

Tsai, Y.-T., Wang, C.-H., Chang, Y.-C., & Tong, L.-I. (2025). Establishing performance baselines for secure software development. *IET Information Security, 2025*, Article 6139424.

Valdes-Rodriguez, Y., Hochstetter-Diez, J., Diaz-Arancibia, J., & Cadena-Martinez, R. (2023). Towards the integration of security practices in agile software development: A systematic mapping review. *Applied Sciences, 13*, Article 4578.

## Version record

| Version | Status | Record |
| --- | --- | --- |
| v0.1 | Earlier draft | Preserved as the initial protocol and preliminary bibliography. |
| v1.0 | Current controlled release | Consolidates the full protocol, narrows the population to companies with an identifiable software development function, and separates the public benchmark from protected fieldwork. |

---

**AI support statement:** AI tools supported language editing, document organization, and consistency checks. Donna Silva reviewed the evidence, determined the methodological choices, and remains responsible for the protocol.

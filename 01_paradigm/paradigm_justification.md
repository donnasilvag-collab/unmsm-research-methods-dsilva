# Paradigm Justification

## Research Paradigms for Software Security: Positivism, Interpretivism, and Mixed Methods

### 1.1. Research Topic and Context

Digital transformation has turned software into a critical infrastructure for organizations. In Peruvian software development companies, teams no longer manage applications alone: they also manage source code repositories, privileged credentials, continuous integration and deployment pipelines, cloud environments, third-party dependencies, activity logs, and other sensitive assets. In this context, information security is no longer an accessory requirement. It becomes a necessary condition for operational continuity, intellectual property protection, regulatory compliance, and user trust.

Even so, recent literature continues to show a substantial gap between that ideal and everyday practice. Khan et al. (2022), in their systematic review of risks and practices in secure software development, argue that many organizations still treat security as a late-stage concern rather than as an activity integrated throughout the software development life cycle. Kolisnichenko et al. (2022) similarly maintain that risk management must be applied across all stages of DevOps, since accelerating development without embedding security directly increases exposure to attack. In the same vein, Valdes-Rodriguez et al. (2023) show that integrating security practices into agile environments remains a relevant challenge, especially in organizations facing time, resource, or institutional maturity constraints.

The problem is not exclusively technical. Course materials and the reviewed studies converge on the idea that the effective adoption of secure development practices also depends on organizational variables such as security culture, leadership, governance, training, metrics, and maturity level. Tsai et al. (2025), for example, propose performance baselines for secure software development that combine proactive security awareness with reactive risk management. That dual perspective is especially useful for this study because it suggests that the effectiveness of access control, source code protection, and software development traceability depends not only on the existence of formal controls, but also on how those controls are understood, applied, and sustained in practice.

On that basis, the research problem is formulated as follows: **the influence of information security risk management on the effectiveness of access control, source code protection, and software development traceability in Peruvian companies**, with particular interest in agile, DevOps, and continuous integration contexts.

### 1.2. Preliminary Research Question

How does information security risk management influence the effectiveness of access control, source code protection, and software development traceability in Peruvian companies?

**Three formulations of the same research question:**

**Version A - Explanatory-quantitative orientation:** To what extent does the maturity level of information security risk management predict the effectiveness of access control, source code protection, and software development traceability in Peruvian companies?

**Version B - Organizational-interpretive orientation:** How do developers, technical leaders, and security practitioners in Peruvian companies experience the relationship between risk management and the actual implementation of access controls, code protection, and traceability practices within the development process?

**Version C - Integrative mixed methods orientation:** Which measurable dimensions of risk management are associated with stronger outcomes in access control, source code protection, and software development traceability in Peruvian companies, and how do human and organizational factors explain those associations?

### 1.3. Selected Paradigm and Rationale

This research adopts a **mixed methods paradigm** with a **pragmatic orientation**, implemented through an **explanatory sequential design**. The overall logic is to first identify and measure relationships between variables and then interpret more deeply why those relationships take shape in particular ways across organizational settings.

This decision follows a central methodological principle of the course: paradigm choice should be derived from the nature of the problem rather than from personal preference or disciplinary habit. Within that perspective, mixed methods are justified only when a single approach is insufficient to understand the phenomenon under study. In this case, that insufficiency is evident.

A purely **positivist paradigm** is not adopted as the primary stance, although the quantitative component of the study is indispensable. A positivist approach would allow the researcher to measure variables, construct indicators, estimate associations, and assess whether a higher degree of risk management maturity is related to better outcomes in access control, source code protection, and traceability. That view is necessary because the problem includes observable dimensions such as policies, control mechanisms, formal practices, incident frequency, logging, activity auditing, and procedure compliance. However, an exclusively positivist reading would leave a key question unanswered: why organizations with apparently similar controls still produce different outcomes. The reviewed literature suggests that such variation is shaped by factors such as organizational maturity, training, resistance to change, leadership, and security culture. These elements are not exhausted by numerical scales alone.

Nor is a purely **interpretivist paradigm** adopted. A qualitative approach would allow a deeper understanding of how actors interpret security, how they negotiate priorities between speed and control, why certain mechanisms are seen as useful or bureaucratic, and how failures in traceability or relaxed controls emerge in daily practice. That understanding is valuable, but on its own it does not provide a strong enough basis for estimating the magnitude of influence between variables or for sustaining comparisons across organizations. If the research question includes the verb *influence*, then describing perceptions is not sufficient; observable relationships must also be examined.

Likewise, **design science** is not selected as the primary paradigm. Although this study may later support the development of an assessment model, an improvement guide, or a recommendation framework for secure development, its central purpose is not to design and validate a new technological artifact under criteria of utility, novelty, and rigor. Its main purpose is to explain a relationship between risk management practices and technical and organizational security outcomes. For that reason, the core of the study is explanatory rather than artifact-oriented.

Consequently, a mixed methods paradigm provides the best fit because the phenomenon includes both a measurable dimension and a clearly interpretive one. The quantitative phase may show, for example, that certain dimensions of risk management are associated with stronger traceability or more robust access controls. The qualitative phase may then explain why that association appears, weakens, or even becomes contradictory in particular settings, such as those shaped by limited training, low adoption, delivery pressure, diffuse governance, or weak security culture. The value of the mixed design does not lie in combining techniques for breadth alone, but in producing a more robust interpretation of a problem that cannot be understood well through a single type of evidence.

For that reason, the qualitative phase is not conceived as a merely narrative complement to the quantitative data. The intended integration is substantive: qualitative findings should help reinterpret the quantitative results and explain why risk management works better in some organizations than in others, even when their formal controls appear comparable. That is precisely what turns a mixed methods study into a coherent research design rather than into two parallel studies presented under the same cover.

### 1.4. Implications of the Paradigm Choice

**Type of data:** The study requires both quantitative and qualitative data. The quantitative side may include risk management maturity scales, evidence on access policies and practices, repository control mechanisms, traceability processes, audit records, security training, and procedure compliance. The qualitative side may include semistructured interviews with developers, project leaders, security professionals, or DevOps-oriented roles, together with the analysis of organizational documents, workflows, and routine practices.

**Methods:** The paradigm points toward an explanatory sequential design. First, a quantitative phase is needed to identify patterns of association or influence between risk management and the three dependent dimensions of the study. Then, a qualitative phase is needed to explain those patterns, especially where gaps exist between formal control and actual practice. The strength of the study will depend not only on the rigor of each phase separately, but also on the quality of integration between them.

**Validity criteria:** The quantitative phase requires clear variable operationalization, instrument consistency, and appropriate analytical techniques. The qualitative phase requires interpretive transparency, analytic traceability, and coherence between evidence and conclusions. At the integrative level, the key criterion is the quality of the meta-inferences: whether the final explanation convincingly articulates what the data show with what the actors do, interpret, and experience.

**Expected contribution:** The study is expected to contribute on two levels. Academically, it may provide evidence on how information security risk management influences critical processes in secure software development. Practically, it may generate useful findings to strengthen organizational policies, practices, and capabilities related to access control, source code protection, and traceability in Peruvian software development companies, especially in agile or DevOps-oriented environments.

### 1.5. A Methodological Tension

The main methodological tension lies in access to high-quality evidence. Software organizations usually consider information about access controls, incidents, actual repository practices, traceability failures, and security weaknesses to be sensitive. This may limit the availability of direct data and push the researcher to rely too heavily on self-reported responses, which often overestimate the actual level of maturity. The main concern, therefore, is not whether a mixed methods paradigm fits, but how to ensure that the quantitative phase captures effective practices rather than merely declared compliance, and that the qualitative phase obtains enough openness from participants to explain tensions that many organizations prefer not to make explicit.

## References Cited

Khan, R. A., Khan, S. U., Khan, H. U., and Ilyas, M. (2022). *Systematic Literature Review on Security Risks and Its Practices in Secure Software Development*. IEEE Access, 10, 5456-5481.

Kolisnichenko, O., Kolomytsev, M., and Nosok, S. (2022). *Software Security Risk Management in DEVOPS Methodology*. Theoretical and Applied Cybersecurity, 3(1).

Tsai, Y.-T., Wang, C.-H., Chang, Y.-C., and Tong, L.-I. (2025). *Establishing Performance Baselines for Secure Software Development*. IET Information Security, 2025, 6139424.

Valdes-Rodriguez, Y., Hochstetter-Diez, J., Diaz-Arancibia, J., and Cadena-Martinez, R. (2023). *Towards the Integration of Security Practices in Agile Software Development: A Systematic Mapping Review*. Applied Sciences, 13, 4578.

Souppaya, M., Scarfone, K., and Dodson, D. (2022). *Secure Software Development Framework (SSDF) Version 1.1: Recommendations for Mitigating the Risk of Software Vulnerabilities* (NIST SP 800-218). National Institute of Standards and Technology.

OWASP Foundation. (2020). *OWASP SAMM v2*.

Cleland-Huang, J., Gotel, O. C. Z., Hayes, J. H., Mader, P., and Zisman, A. (2014). *Software Traceability: Trends and Future Directions*. In *Future of Software Engineering, FOSE 2014 Proceedings* (pp. 55-69).

# Research Gap Analysis

## 4.1. Purpose

This gap analysis synthesizes which aspects remain insufficiently resolved in the reviewed literature on secure software development, risk management, access control, and traceability. Its purpose is to show clearly why the proposed research problem does not merely repeat what is already known, but instead addresses an area that remains insufficiently articulated across technical frameworks, organizational practices, and applied evidence.

## 4.2. Gap Matrix

| Type of gap | Identified gap | Main evidence | Relevance for the study |
| --- | --- | --- | --- |
| **Knowledge gap** | The literature describes risks, practices, and secure SDLC frameworks, but still offers limited integrated evidence on how **risk management maturity** concretely influences **access control**, **source code protection**, and **software development traceability** within Peruvian software development companies. | Khan et al. (2022); Tsai et al. (2025); Valdes-Rodriguez et al. (2023) | Justifies the need to study the relationship between a broad organizational variable such as risk management and specific operational outcomes within the development process. |
| **Methodological gap** | Reviews, comparative frameworks, and best-practice proposals predominate, but there are fewer studies that combine **quantitative measurement** and **qualitative explanation** to understand why similar controls produce different results across organizations. | Khan et al. (2022); Sanchez-Gordon and Colomo-Palacios (2020); De Win et al. (2009) | Supports the choice of a mixed methods design, since a purely descriptive or exclusively technical approach would leave out the organizational dimension of the problem. |
| **Contextual gap** | Most of the reviewed studies are situated in general international settings, broad industrial frameworks, or academic environments. There is still little evidence centered on **Peruvian companies** or, more broadly, on Latin American software development organizations. | Valdes-Rodriguez et al. (2023); Basin et al. (2023); Humayun et al. (2022) | Reinforces the applied relevance of the study, because it enables the production of situated evidence in a context where institutional, resource, and maturity constraints may differ. |
| **Theoretical-practical gap** | Strong standards and frameworks such as NIST SSDF, NIST SP 800-53, and OWASP SAMM exist, but these guidelines do not by themselves explain how they translate into sustained practices or how they interact with factors such as culture, leadership, operational discipline, or delivery pressure. | Souppaya et al. (2022); OWASP Foundation (2020); Tsai et al. (2025); Sanchez-Gordon and Colomo-Palacios (2020) | Opens space for research that does not stop at formal compliance, but instead examines the gap between prescribed control and actually executed control. |
| **Access control gap** | Studies on access modeling and access vulnerabilities do exist, but they are often concentrated on architecture, web applications, or highly specialized approaches. There is less development of studies that integrate access control into a broader view of risk management across the SDLC. | Basin et al. (2023); Basin, Doser, and Lodderstedt (2006) | Supports one of the three dependent dimensions of the study and avoids treating access control as an isolated design or configuration problem. |
| **Traceability gap** | Traceability is well recognized as a key capability for assurance, governance, and maintaining links among artifacts, but it does not always appear connected to organizational security assessments or to the risk management of everyday development work. | Cleland-Huang et al. (2014) | Justifies approaching traceability not only as a documentation practice, but as a component of control and auditability within secure development. |
| **Code and artifact protection gap** | The reviewed literature offers greater density on secure SDLC, threats, and access control than on the relationship between risk management and the **protection of repositories, source code, and development artifacts** as a central object of analysis. | Khan et al. (2022); Kolisnichenko et al. (2022); Tsai et al. (2025) | Reinforces the originality of the study by incorporating a dimension that is often dispersed across supply chain security, repository practices, and change control. |

## 4.3. Integrated Reading of the Gaps

The review does not show a total absence of literature. What it reveals instead is a **fragmentation** of the available knowledge. Some studies focus on risks and practices across the SDLC; others focus on process frameworks; others on access control; others on traceability; and still others on DevSecOps culture. The problem is that these contributions do not always converge into an integrated question about how risk management affects concrete controls within software development.

That point matters because the study does not seek to demonstrate that security is important; the literature has already established that clearly. What it seeks is a more specific contribution: to understand whether a higher maturity in risk management is effectively related to stronger outcomes in access control, source code protection, and software development traceability, and to explain why that relationship may strengthen or weaken depending on the organizational context.

## 4.4. How This Research Responds to Those Gaps

The proposed research responds to the identified gaps in four ways:

- **It integrates dimensions that are usually studied separately:** risk management, access control, source code protection, and software development traceability.
- **It combines measurement and interpretation:** it does not stop at describing frameworks or practices, but instead seeks to connect quantitative indicators with qualitative explanations.
- **It contributes applied context:** it directs the analysis toward Peruvian software development companies, an area that remains underrepresented in the reviewed literature.
- **It examines the gap between formal structures and real practice:** it does not assume that the existence of policies or tools automatically implies effective controls.

## 4.5. Implication for Problem Formulation

Based on this analysis, the research problem is strengthened at a central point: it is not enough to ask whether organizations have security practices, nor to list the available frameworks. The more relevant question is whether risk management actually translates into stronger control capabilities within software development and which conditions explain that translation. That is precisely the space in which this study can make a more defensible academic and applied contribution.

## 4.6. Base References Used for the Analysis

- Basin, D., Guarnizo, J., Krstić, S., Nguyen, H., and Ochoa, M. (2023). *Is Modeling Access Control Worth It?* In *Proceedings of the 2023 ACM SIGSAC Conference on Computer and Communications Security (CCS '23)*.
- Basin, D. A., Doser, J., and Lodderstedt, T. (2006). *Model Driven Security: From UML Models to Access Control Infrastructures*. ACM Transactions on Software Engineering and Methodology, 15(1), 39-91.
- Cleland-Huang, J., Gotel, O. C. Z., Hayes, J. H., Mader, P., and Zisman, A. (2014). *Software Traceability: Trends and Future Directions*. In *Future of Software Engineering, FOSE 2014 Proceedings* (pp. 55-69).
- De Win, B., Scandariato, R., Buyens, K., Gregoire, J., and Joosen, W. (2009). *On the Secure Software Development Process: CLASP, SDL and Touchpoints Compared*. Information and Software Technology, 51(7), 1152-1171.
- Humayun, M., Jhanjhi, N., Almufareh, M. F., and Khalil, M. I. (2022). *Security Threat and Vulnerability Assessment and Measurement in Secure Software Development*. Computers, Materials & Continua, 71(3), 5039-5059.
- Khan, R. A., Khan, S. U., Khan, H. U., and Ilyas, M. (2022). *Systematic Literature Review on Security Risks and Its Practices in Secure Software Development*. IEEE Access, 10, 5456-5481.
- Kolisnichenko, O., Kolomytsev, M., and Nosok, S. (2022). *Software Security Risk Management in DEVOPS Methodology*. Theoretical and Applied Cybersecurity, 3(1).
- OWASP Foundation. (2020). *OWASP SAMM v2*.
- Sanchez-Gordon, M.-L., and Colomo-Palacios, R. (2020). *Security as Culture: A Systematic Literature Review of DevSecOps*. In *Proceedings of the IEEE/ACM 42nd International Conference on Software Engineering Workshops* (pp. 266-269).
- Souppaya, M., Scarfone, K., and Dodson, D. (2022). *Secure Software Development Framework (SSDF) Version 1.1: Recommendations for Mitigating the Risk of Software Vulnerabilities* (NIST SP 800-218). National Institute of Standards and Technology.
- Tsai, Y.-T., Wang, C.-H., Chang, Y.-C., and Tong, L.-I. (2025). *Establishing Performance Baselines for Secure Software Development*. IET Information Security, 2025, 6139424.
- Valdes-Rodriguez, Y., Hochstetter-Diez, J., Diaz-Arancibia, J., and Cadena-Martinez, R. (2023). *Towards the Integration of Security Practices in Agile Software Development: A Systematic Mapping Review*. Applied Sciences, 13, 4578.

---

**AI support statement:** AI assistance was used to support draft organization, review wording, and improve expository clarity. The identification of gaps, the articulation of the problem, and the academic interpretation correspond to the author.

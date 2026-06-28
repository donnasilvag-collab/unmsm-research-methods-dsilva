# Preliminary Systematic Literature Review

## 4.1. Review Question

The question guiding this preliminary systematic review is the following:

**What recent and relevant evidence helps explain the influence of information security risk management on the effectiveness of access control, source code protection, and software development traceability, with particular interest in Peruvian companies?**

This formulation makes it possible to focus the review on four dimensions directly linked to the research problem: **risk management**, **access control**, **protection of code and development artifacts**, and **software development traceability**.

## 4.2. Search Strategy

| Field | Value |
| --- | --- |
| **Primary source** | Semantic Scholar |
| **Complementary support** | Manual review of cited references and previously assembled local corpus |
| **Seed search date** | June 25, 2026 |
| **Coverage period** | 2006-2025 |
| **Languages** | English and Spanish |
| **Prioritized document type** | Peer-reviewed journal articles, conference papers, and systematic or mapping reviews |

**Boolean query used in the seed search:**

```text
("software security" OR "secure software development" OR "secure SDLC" OR SSDLC OR DevSecOps OR DevOps)
AND ("risk management" OR "security risks" OR "threat modeling" OR "vulnerability assessment")
AND ("access control" OR authorization OR traceability OR "source code" OR repository)
```

The search was designed as a **seed mini-review**, following the logic developed in the course literature review unit. For that reason, in addition to the primary source, backward reference tracking was used in order not to miss foundational studies that remain relevant to the problem.

## 4.3. Inclusion and Exclusion Criteria

**Inclusion criteria:**

- Publications between **2006 and 2025**.
- Studies in English or Spanish with full text available.
- Peer-reviewed journal articles and conference papers directly related to at least one dimension of the study: risk management, secure development, access control, traceability, or protection of development artifacts.
- Systematic reviews, mapping reviews, empirical studies, comparative frameworks, and methodological works with a clear contribution to the secure software development life cycle.
- Studies whose contribution is transferable to the context of Peruvian software development companies, even when they are not situated in Peru.

**Exclusion criteria:**

- Studies focused only on network security, cryptography, or perimeter security without a clear connection to the software development life cycle.
- Preprints, technical notes, or gray literature without academic peer review.
- Studies that are overly specific to a domain with low transferability to the central problem.
- Duplicate texts, preliminary versions, or works with insufficient methodological clarity.

## 4.4. PRISMA 2020 Structure

### Preliminary Flow of the Seed Search

| Phase | n |
| --- | ---: |
| Records identified in the primary search | 31 |
| Additional records from reference tracking and local corpus | 12 |
| **Total identified** | **43** |
| Duplicates or redundant versions removed | 7 |
| Records screened by title and abstract | 36 |
| Excluded at title and abstract stage | 20 |
| Full texts assessed for eligibility | 16 |
| Excluded after full-text reading | 6 |
| **Studies included in the qualitative synthesis** | **10** |

### Main Reasons for Exclusion

- Outside the focus of the study: general security without a sufficient link to SDLC, access control, traceability, or risk management.
- Excessively restricted focus with low transferability.
- Lack of academic peer review or insufficient methodological detail.

**Note:** this flow corresponds to a **preliminary PRISMA draft** prepared for the present course delivery. The counts should be revalidated when the final search is carried out using a closed and unique database for the final version of the review.

The diagram corresponding to this flow is presented in **`prisma_diagram.png`** within the same folder.

## 4.5. The 10 Prioritized Studies

| No. | Prioritized study | Main focus | Reason for prioritization |
| --- | --- | --- | --- |
| 1 | **Khan, R. A., Khan, S. U., Khan, H. U., and Ilyas, M. (2022). _Systematic Literature Review on Security Risks and Its Practices in Secure Software Development_. IEEE Access, 10, 5456-5481.** | Risks and secure development practices | This is the most valuable synthetic reference for the problem because it organizes risks and practices across the SDLC and provides a broad basis for justifying the variables and dimensions of the study. |
| 2 | **Valdes-Rodriguez, Y., Hochstetter-Diez, J., Diaz-Arancibia, J., and Cadena-Martinez, R. (2023). _Towards the Integration of Security Practices in Agile Software Development: A Systematic Mapping Review_. Applied Sciences, 13, 4578.** | Security integration in agile contexts | This study is central because it connects secure development with agile environments, where tensions often appear between speed, control discipline, and security maturity. |
| 3 | **Tsai, Y.-T., Wang, C.-H., Chang, Y.-C., and Tong, L.-I. (2025). _Establishing Performance Baselines for Secure Software Development_. IET Information Security, 2025, 6139424.** | Metrics and performance baselines | It offers a recent perspective on how to measure secure development capabilities, which is useful for translating risk management into observable indicators. |
| 4 | **Humayun, M., Jhanjhi, N., Almufareh, M. F., and Khalil, M. I. (2022). _Security Threat and Vulnerability Assessment and Measurement in Secure Software Development_. Computers, Materials & Continua, 71(3), 5039-5059.** | Threat and vulnerability assessment | It strengthens the dimension of threat assessment and measurement within the SDLC and supports the quantifiable part of the study. |
| 5 | **Basin, D., Guarnizo, J., Krstić, S., Nguyen, H., and Ochoa, M. (2023). _Is Modeling Access Control Worth It?_ In _Proceedings of the 2023 ACM SIGSAC Conference on Computer and Communications Security (CCS '23)_.** | Access control | This is one of the studies most directly aligned with the access control dimension and it compares implementation approaches using empirical evidence. |
| 6 | **Cleland-Huang, J., Gotel, O. C. Z., Hayes, J. H., Mader, P., and Zisman, A. (2014). _Software Traceability: Trends and Future Directions_. In _Future of Software Engineering, FOSE 2014 Proceedings_ (pp. 55-69).** | Traceability | It functions as an anchor reference for the traceability dimension and helps justify traceability as a strategic capability, not merely as a documentation practice. |
| 7 | **Othmane, L. B., Angin, P., Weffers, H., and Bhargava, B. (2014). _Extending the Agile Development Process to Develop Acceptably Secure Software_. IEEE Transactions on Dependable and Secure Computing, 11(6), 497-509.** | Secure development in agile processes | It is useful for explaining how security can be integrated without breaking the iterative logic of agile or continuous delivery teams. |
| 8 | **Sanchez-Gordon, M.-L., and Colomo-Palacios, R. (2020). _Security as Culture: A Systematic Literature Review of DevSecOps_. In _Proceedings of the IEEE/ACM 42nd International Conference on Software Engineering Workshops_ (pp. 266-269).** | DevSecOps culture | It complements the technical view with an organizational and cultural dimension, which is especially relevant for explaining why equivalent controls may produce different outcomes. |
| 9 | **De Win, B., Scandariato, R., Buyens, K., Gregoire, J., and Joosen, W. (2009). _On the Secure Software Development Process: CLASP, SDL and Touchpoints Compared_. Information and Software Technology, 51(7), 1152-1171.** | Processes and secure development frameworks | It provides an early but still valuable comparison among secure development frameworks and supports the process and governance dimension. |
| 10 | **Basin, D. A., Doser, J., and Lodderstedt, T. (2006). _Model Driven Security: From UML Models to Access Control Infrastructures_. ACM Transactions on Software Engineering and Methodology, 15(1), 39-91.** | Access design and formalization | Although more foundational, it remains highly useful for the access dimension because it shows how control policies can be translated systematically into technical infrastructure. |

## 4.6. Initial Synthesis of Findings

The preliminary review reveals five broad patterns. First, the literature agrees that security is still incorporated too frequently at a late stage, even though there is already enough evidence about the cost of that decision. Second, risk management appears as a central organizing axis of secure development, yet many publications focus more on frameworks and practices than on empirical evidence of their actual effectiveness. Third, the **access control** dimension does have specific studies, although most of them are oriented toward modeling, vulnerability detection, or particular environments rather than toward its integrated relationship with organizational risk management.

Fourth, **traceability** is well supported as an assurance and governance capability, but in the reviewed literature it is less connected to security metrics applied to Peruvian software development companies or to comparable organizational contexts. Fifth, the most recent work on DevSecOps and secure SDLC insists that human and cultural factors remain a persistent barrier to consolidating secure practices, even when tools or frameworks are already available.

## 4.7. Gaps that Justify the Study

- The literature offers extensive discussion of secure SDLC, but less evidence directly connecting the **maturity of risk management** with concrete outcomes in **access control**, **code protection**, and **traceability**.
- There are more studies on frameworks, models, or best practices than on how those practices actually work within Peruvian software development companies or in comparable organizational contexts with real operational constraints.
- The dimension of **source code and development artifact protection** appears less developed than access control or general secure SDLC practices.
- Contextual gaps remain for Latin American organizations and, more specifically, for Peruvian software development companies.

## 4.8. Methodological Support References

The following references are not part of the ten prioritized studies, but they support the methodological construction of the review:

- Page, M. J., McKenzie, J. E., Bossuyt, P. M., Boutron, I., Hoffmann, T. C., Mulrow, C. D., and others. (2021). *The PRISMA 2020 Statement: An Updated Guideline for Reporting Systematic Reviews*. BMJ, 372, n71.
- Kitchenham, B., and Brereton, P. (2013). *A Systematic Review of Systematic Review Process Research in Software Engineering*. Information and Software Technology, 55, 2049-2075.

---

**AI support statement:** AI assistance was used to organize the draft, review wording, and help structure the synthesis. The study selection, the interpretation of the gaps, and the methodological organization of the mini-review correspond to the author.

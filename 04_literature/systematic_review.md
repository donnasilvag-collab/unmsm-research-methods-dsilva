# Preliminary systematic literature review

## 4.1. Review question

**What evidence helps explain the relationship between information security risk-management maturity and the effectiveness of access control, source-code protection, and software-development traceability?**

The review supports construct definition and instrument design for the study *Madurez de la gestión de riesgos y eficacia de los controles de desarrollo seguro en empresas peruanas*. It is a course-stage systematic review, not the final thesis review.

## 4.2. Search strategy

The seed search was conducted on 25 June 2026. Semantic Scholar was the primary discovery source. Backward reference tracking and the local article corpus supplied complementary records. The date, source, count, and evidence retained for each search action appear in [`search_log.csv`](search_log.csv).

```text
("software security" OR "secure software development" OR "secure SDLC" OR SSDLC OR DevSecOps OR DevOps)
AND ("risk management" OR "security risks" OR "threat modeling" OR "vulnerability assessment")
AND ("access control" OR authorization OR traceability OR "source code" OR repository)
```

| Field | Decision |
| --- | --- |
| Publication period | 2006 to 2025 |
| Languages | English or Spanish |
| Eligible formats | Peer-reviewed journal articles, conference papers, systematic reviews, and mapping reviews |
| Main concepts | Risk management, secure SDLC, access control, source-code or development-artifact protection, and traceability |
| Context requirement | Direct software-development relevance and reasonable transferability to company practice |

The broad query was intentionally retained because no single term consistently covers governance maturity and all three control outcomes. Search refinement for the thesis should add Scopus, Web of Science, IEEE Xplore, ACM Digital Library, and a preserved RIS or BibTeX export from every source.

## 4.3. Eligibility criteria

### Inclusion

- Full text was available in English or Spanish.
- The work was published from 2006 through 2025 in an eligible peer-reviewed format.
- The study addressed at least one predefined construct and maintained a clear connection to software-development practice.
- The method and contribution could be assessed from the available text.
- The findings offered empirical, methodological, or theoretical support transferable to the proposed field study.

### Exclusion

- Duplicate or superseded record.
- Preprint or gray literature without confirmed peer review.
- Network, cryptographic, or domain-specific security work without sufficient connection to the study constructs.
- Review or article with insufficient method detail to determine how evidence was located, selected, or analyzed.
- Narrow technical comparison that did not inform risk-management maturity or the effectiveness of the selected controls.

## 4.4. Screening and PRISMA validation

| Phase | n | Arithmetic check |
| --- | ---: | --- |
| Primary-source records | 31 |  |
| Records from reference tracking and local corpus | 12 |  |
| Total identified | 43 | 31 + 12 = 43 |
| Duplicates or redundant versions removed | 7 | 43 - 7 = 36 |
| Title and abstract records screened | 36 |  |
| Excluded at title and abstract | 20 | 36 - 20 = 16 |
| Full texts assessed | 16 |  |
| Excluded after full-text assessment | 6 | 16 - 6 = 10 |
| Studies included in qualitative synthesis | 10 | Validated |

The machine-readable counts are in [`prisma_flow.csv`](prisma_flow.csv), and the record-level full-text decisions are in [`screening_log.csv`](screening_log.csv). The updated diagram is available as [`prisma_diagram.png`](prisma_diagram.png) and [`prisma_diagram.svg`](prisma_diagram.svg).

Regenerate the PNG from the recorded counts with `python 04_literature/render_prisma.py` after installing the pipeline requirements.

The validation completed on 8 August 2026 confirmed the arithmetic, full-text decisions, DOI values, and publication status of the ten included studies. The original export containing every one of the 43 identification records was not preserved. For that reason, the present evidence trail is reproducible from full-text assessment onward, while the initial identification counts remain a documented legacy of the June search. The final thesis search must preserve complete database exports and deduplication decisions.

### Full-text exclusions

| Record | Decision reason |
| --- | --- |
| Zhong (2023), *A Survey of Prevent and Detect Access Control Vulnerabilities* | arXiv preprint without confirmed peer review at screening. |
| Chen et al. (2025), *TRACE: Securing Smart Contract Repository Against Access Control Vulnerability* | arXiv preprint and smart-contract-specific intervention with limited transferability to the organizational question. |
| Odera, Otieno, and Ounza (2023), *Security Risks in the Software Development Lifecycle: A Review* | Review method did not provide enough reproducible search and selection detail for this synthesis. |
| Otieno, Odera, and Ounza (2023), *Theory and Practice in Secure Software Development Lifecycle: A Comprehensive Survey* | Broad narrative coverage overlapped with included reviews and did not document a reproducible selection method. |
| Kolisnichenko, Kolomytsev, and Nosok (2021), *Software Security Risk Management in DevOps Methodology* | Three-page comparison of five risk methods on one illustrative web application did not examine organizational maturity or the selected outcomes. |
| Mahomedov (2025), *Information Security Challenges in an Enterprise-Grade Software Development Lifecycle* | Narrative review with insufficient search and selection detail for reproducible inclusion. |

## 4.5. Included studies

| ID | Study | DOI | Contribution to this study |
| --- | --- | --- | --- |
| S01 | Khan, R. A., Khan, S. U., Khan, H. U., and Ilyas, M. (2022). Systematic literature review on security risks and its practices in secure software development. *IEEE Access, 10*, 5456-5481. | [10.1109/ACCESS.2022.3140181](https://doi.org/10.1109/ACCESS.2022.3140181) | Organizes security risks and practices across the SDLC and supports the broad construct map. |
| S02 | Valdes-Rodriguez, Y., Hochstetter-Diez, J., Diaz-Arancibia, J., and Cadena-Martinez, R. (2023). Towards the integration of security practices in agile software development: A systematic mapping review. *Applied Sciences, 13*, 4578. | [10.3390/app13074578](https://doi.org/10.3390/app13074578) | Documents integration barriers and practices in agile settings. |
| S03 | Tsai, Y.-T., Wang, C.-H., Chang, Y.-C., and Tong, L.-I. (2025). Establishing performance baselines for secure software development. *IET Information Security, 2025*, 6139424. | [10.1049/ise2/6139424](https://doi.org/10.1049/ise2/6139424) | Connects proactive awareness and reactive risk management with measurable secure-development performance. |
| S04 | Humayun, M., Jhanjhi, N., Almufareh, M. F., and Khalil, M. I. (2022). Security threat and vulnerability assessment and measurement in secure software development. *Computers, Materials & Continua, 71*(3), 5039-5059. | [10.32604/cmc.2022.019289](https://doi.org/10.32604/cmc.2022.019289) | Supports threat assessment and measurement within the SDLC. |
| S05 | Basin, D., Guarnizo, J., Krstic, S., Nguyen, H., and Ochoa, M. (2023). Is modeling access control worth it? In *Proceedings of the 2023 ACM SIGSAC Conference on Computer and Communications Security*. | [10.1145/3576915.3623196](https://doi.org/10.1145/3576915.3623196) | Provides empirical evidence for the access-control dimension and implementation choices. |
| S06 | Cleland-Huang, J., Gotel, O. C. Z., Hayes, J. H., Mader, P., and Zisman, A. (2014). Software traceability: Trends and future directions. In *Proceedings of the Future of Software Engineering* (pp. 55-69). | [10.1145/2593882.2593891](https://doi.org/10.1145/2593882.2593891) | Establishes traceability as an assurance and governance capability. |
| S07 | Othmane, L. B., Angin, P., Weffers, H., and Bhargava, B. (2014). Extending the agile development process to develop acceptably secure software. *IEEE Transactions on Dependable and Secure Computing, 11*(6), 497-509. | [10.1109/TDSC.2014.2298011](https://doi.org/10.1109/TDSC.2014.2298011) | Shows how security activities can be integrated into iterative development. |
| S08 | Sanchez-Gordon, M.-L., and Colomo-Palacios, R. (2020). Security as culture: A systematic literature review of DevSecOps. In *Proceedings of the IEEE/ACM 42nd International Conference on Software Engineering Workshops* (pp. 266-269). | [10.1145/3387940.3392233](https://doi.org/10.1145/3387940.3392233) | Supports the organizational and cultural explanation required in the qualitative phase. |
| S09 | De Win, B., Scandariato, R., Buyens, K., Gregoire, J., and Joosen, W. (2009). On the secure software development process: CLASP, SDL and Touchpoints compared. *Information and Software Technology, 51*(7), 1152-1171. | [10.1016/j.infsof.2008.01.010](https://doi.org/10.1016/j.infsof.2008.01.010) | Compares secure-development processes and their governance implications. |
| S10 | Basin, D. A., Doser, J., and Lodderstedt, T. (2006). Model driven security: From UML models to access control infrastructures. *ACM Transactions on Software Engineering and Methodology, 15*(1), 39-91. | [10.1145/1125808.1125810](https://doi.org/10.1145/1125808.1125810) | Provides foundational support for systematic translation of access policy into technical controls. |

## 4.6. Quality appraisal

Each included study was assessed on five criteria scored from 0 to 2: direct relevance, method transparency, evidence basis, reproducibility or evidence trace, and transferability to the proposed study. Totals from 8 to 10 are classified as high, 5 to 7 as moderate, and 0 to 4 as contextual only. This project-specific appraisal supports transparent weighting of a mixed evidence base; it is not presented as a validated risk-of-bias instrument.

| ID | Relevance | Method | Evidence | Trace | Transferability | Total | Rating |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| S01 | 2 | 2 | 2 | 1 | 2 | 9 | High |
| S02 | 2 | 2 | 2 | 1 | 2 | 9 | High |
| S03 | 2 | 2 | 2 | 1 | 2 | 9 | High |
| S04 | 2 | 2 | 1 | 1 | 2 | 8 | High |
| S05 | 2 | 2 | 2 | 1 | 1 | 8 | High |
| S06 | 2 | 1 | 1 | 1 | 2 | 7 | Moderate |
| S07 | 2 | 2 | 1 | 1 | 2 | 8 | High |
| S08 | 2 | 1 | 1 | 0 | 2 | 6 | Moderate |
| S09 | 2 | 2 | 1 | 1 | 2 | 8 | High |
| S10 | 2 | 2 | 1 | 1 | 1 | 7 | Moderate |

Detailed scores and short rationales are in [`quality_appraisal.csv`](quality_appraisal.csv). No included study provides direct evidence from Peruvian companies, and no single study measures the full relationship proposed in the protocol.

## 4.7. Synthesis

The evidence supports four conclusions relevant to the protocol. Security practices are often unevenly integrated across the SDLC, especially where delivery pressure and role separation place security late in the process. Risk management offers a way to prioritize secure-development work, but the reviewed studies usually examine frameworks, individual practices, or technical outcomes rather than the association between organizational maturity and sustained control effectiveness.

Access control and traceability have established technical and process foundations. Source-code protection appears across secure build, review, dependency, and artifact practices, but it is rarely analyzed as one organizational outcome. The literature also shows that tools cannot explain consistent adoption on their own. Governance, role clarity, training, and working culture affect whether a documented control becomes routine practice.

These findings support an explanatory sequential mixed methods design. The survey can estimate exploratory associations among the predefined constructs, while interviews and authorized document review can examine why formal and observed practices differ.

## 4.8. Research gap and limits

The review found no included study that jointly measures risk-management maturity, access-control effectiveness, source-code protection, and development traceability in Peruvian companies. Evidence from Latin American software organizations is also limited in the selected set. This is a contextual and integration gap, not proof that no relevant study exists outside the current search.

The present review has four limits. It began with one primary discovery source, lacks a preserved export for all initial records, includes only ten studies for the course exercise, and uses a project-specific quality appraisal. The thesis review must broaden database coverage, register the protocol before screening, preserve every record and exclusion decision, use duplicate screening on a documented sample, and rerun publication-status checks immediately before submission.

## 4.9. Methodological references

- Kitchenham, B., and Brereton, P. (2013). A systematic review of systematic review process research in software engineering. *Information and Software Technology, 55*(12), 2049-2075. https://doi.org/10.1016/j.infsof.2013.07.010
- Page, M. J., McKenzie, J. E., Bossuyt, P. M., Boutron, I., Hoffmann, T. C., Mulrow, C. D., and others. (2021). The PRISMA 2020 statement: An updated guideline for reporting systematic reviews. *BMJ, 372*, n71. https://doi.org/10.1136/bmj.n71

---

**AI support statement:** AI tools assisted with record organization, DOI cross-checking, formatting, and language review. Donna Silva reviewed the full-text decisions, approved the appraisal judgments, and remains responsible for the synthesis and its limits.

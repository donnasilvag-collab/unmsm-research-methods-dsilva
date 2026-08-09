# Analysis of a retracted security study

## 12.1. Purpose of the case analysis

This exercise examines how a retraction should change literature screening, citation use, and dependent research decisions. It does not investigate the author or repeat the publisher's inquiry. The analysis is limited to the public article record, the publisher's retraction notice, the retained notice PDF, and a search of this repository.

The authoritative DOI records, local evidence file, status-check date, and repository decision are summarized in [`retraction_source.md`](retraction_source.md).

## 12.2. Bibliographic record and timeline

### Retracted article

Chen, S. (2023). The design of network security protection trust management system based on an improved hidden Markov model. *EURASIP Journal on Information Security, 2023*, Article 10. https://doi.org/10.1186/s13635-023-00146-z

### Retraction notice

Chen, S. (2024). Retraction note: The design of network security protection trust management system based on an improved hidden Markov model. *EURASIP Journal on Information Security, 2024*, Article 18. https://doi.org/10.1186/s13635-024-00167-2

| Date | Event | Evidence |
| --- | --- | --- |
| 23 November 2023 | Original article published | Publisher record linked from the retraction notice |
| 13 May 2024 | Retraction notice published | Springer Nature version of record |
| 8 August 2026 | DOI status and repository dependencies checked | Publisher page, retained notice PDF, and repository-wide search |

A publisher-issued copy of the notice is preserved in [`retraction_note_network_security_trust_management.pdf`](retraction_note_network_security_trust_management.pdf). The DOI links are the authoritative status records; the local PDF is supporting evidence for the course repository.

## 12.3. What the publisher established

The Editor-in-Chief and publisher retracted the article after investigating a guest-edited issue. The notice reports concerns that included compromised editorial handling and peer review, inappropriate or irrelevant references, and content that may not have been within the scope of the journal or the guest-edited issue. The Editor-in-Chief stated that confidence in the article's results and conclusions could no longer be maintained. The notice also states that the author did not respond to the publisher's correspondence about the retraction.

These statements come from the publisher. The notice does not provide a technical replication, itemized data audit, or finding of author intent. This analysis therefore does not label the case as fabrication, falsification, plagiarism, or deliberate misconduct. Retraction status is enough to exclude the article as supporting evidence, but it is not permission to make accusations beyond the record.

## 12.4. Evidence hierarchy used for the decision

| Evidence | Weight in this analysis | Reason |
| --- | --- | --- |
| Publisher's retraction notice and DOI record | Decisive | It states the current publication status and the editor's basis for withdrawing confidence. |
| Original publisher record | Contextual | It confirms article metadata and links to the notice, but its results cannot support this study after retraction. |
| Local notice PDF | Corroborating | It preserves the notice used in the course exercise. |
| Citation indexes or search-engine snippets | Discovery only | They may lag behind the publisher or omit the reason for retraction. |
| AI-generated summary | No independent evidentiary weight | It may help locate a notice but must be checked against the publisher record. |

The Committee on Publication Ethics advises that retraction notices should identify the article, state who is retracting it and why, remain accessible, and use factual language. Those principles support the narrow response used here: preserve the notice, remove the article from evidentiary use, trace dependent claims, and avoid unsupported allegations.

## 12.5. Relevance to the current research

The retracted article concerns network-security protection, trust management, alarm data, and an improved hidden Markov model. Its language is adjacent to information security risk management and control effectiveness, so a title or abstract search could initially retrieve it. Its actual focus, however, does not directly operationalize risk-management maturity, secure-development access control, source-code protection, or development traceability in companies.

The article therefore presents two independent reasons for exclusion:

1. The publisher has retracted it and no longer has confidence in its results and conclusions.
2. Its technical and network-oriented scope has weak fit with the organizational software-development question.

The first reason is sufficient. The second records the topic decision that would still matter if publication status were not known.

## 12.6. Dependency analysis

The repository was searched on 8 August 2026 for the article title, author, original DOI, and retraction DOI. The local integrity file and retained notice were excluded from the dependency count because they document the case rather than use the article as evidence.

| Research component | Dependent claim found | Required correction |
| --- | --- | --- |
| Paradigm justification | No | None |
| Method comparison | No | None |
| Protocol and bibliography | No | None |
| Systematic-review synthesis | No | Keep excluded; do not add to the ten studies |
| Operationalization matrix and instruments | No | None |
| Reproducible pipeline | No | None |
| Reproducibility audit and model documentation | No | None |
| Ethics and data-management documents | No | None |
| Bias audit | No | None |

No research question, objective, variable, item, algorithm, result, or recommendation depends on the retracted article. The retraction therefore does not require recalculation or withdrawal of a study result. It requires a recorded exclusion and continued status checks.

## 12.7. Counterfactual correction procedure

If a retracted article had supported a claim, the following procedure would apply:

1. Freeze the affected document version and identify every direct and indirect citation dependency.
2. Classify each dependency as background, method, data, numerical result, interpretation, or recommendation.
3. Remove the retracted work as supporting evidence. Do not merely replace its citation with an unrelated source.
4. Search for independent, non-retracted evidence that supports the same claim and assess it under the review criteria.
5. Revise or withdraw any claim that lacks adequate support after removal.
6. Rerun code or synthesis when the retracted work supplied data, parameters, labels, or an analytical method.
7. Record the change, reason, date, affected outputs, and reviewer in a correction log.
8. Notify the relevant academic reviewer, coauthor, repository user, or publisher when the correction affects submitted or published work.

This sequence prevents citation replacement from hiding a substantive dependency.

## 12.8. Potential harms if the status were ignored

Ignoring the retraction could mislead several groups. A reader could assume that the article provides reliable empirical support. A practitioner could adopt a technical approach whose reported results no longer have editorial confidence. The researcher could build an instrument or interpretation on evidence that should have been removed. Repeated citation could also allow the article to continue shaping later reviews even though the publisher has marked it as unreliable.

There is also a fairness concern toward the article's author. Retraction must be reported accurately without treating it as automatic proof of misconduct. The repository should neither rehabilitate the findings nor enlarge the allegations.

## 12.9. Preventive controls for this repository

### Before inclusion

- Verify the DOI and title against the publisher or another authoritative bibliographic record.
- Check the current status for retraction, expression of concern, or material correction.
- Record the status-check date in the screening log.
- Distinguish a publisher version from a preprint, accepted manuscript, or duplicate record.
- Review scope and method rather than relying on title similarity.

### During synthesis

- Link every material claim to the study that supports it.
- Keep exclusion reasons and quality judgments at record level.
- Do not use a retracted article to support a result, method, or theoretical claim.
- If a retracted work is discussed as an integrity case, label it clearly and separate it from the evidence base.

### Before submission or publication

- Recheck the status of all included DOI records.
- Search the repository for newly retracted identifiers and titles.
- Review dependent claims when a status change appears.
- Preserve the correction decision and rerun affected outputs.

The systematic-review files now implement these controls through `04_literature/screening_log.csv`, which records identifier, publication status, status-check date, decision, and reason.

## 12.10. Decision and screening record

| Field | Record |
| --- | --- |
| Original DOI | 10.1186/s13635-023-00146-z |
| Retraction DOI | 10.1186/s13635-024-00167-2 |
| Status checked | 8 August 2026 |
| Authoritative evidence | Springer Nature retraction notice |
| Literature decision | Exclude from the evidence base |
| Permitted use | Research-integrity case only |
| Dependent claims found | None |
| Current repository action | Preserve the notice, document the check, and maintain exclusion |

## 12.11. Limits of this analysis

The publisher notice gives a publication-level decision, not a complete technical or institutional investigation. The analysis did not inspect confidential editorial records, reproduce the hidden Markov model, or assess the author's intent. It also cannot guarantee that every external database displays the status consistently.

The repository check is dated. A clean result on 8 August 2026 does not replace later status checks before thesis submission or publication. The correct response to new information is to update the dependency record and the affected research outputs.

## References

Chen, S. (2023). The design of network security protection trust management system based on an improved hidden Markov model. *EURASIP Journal on Information Security, 2023*, Article 10. https://doi.org/10.1186/s13635-023-00146-z (Retracted)

Chen, S. (2024). Retraction note: The design of network security protection trust management system based on an improved hidden Markov model. *EURASIP Journal on Information Security, 2024*, Article 18. https://doi.org/10.1186/s13635-024-00167-2

COPE Council. (2019). *COPE retraction guidelines*. https://doi.org/10.24318/cope.2019.1.4

---

**AI support statement:** AI tools assisted with source discovery, document organization, dependency-search planning, and language review. Donna Silva verified the publisher notice, approved the distinction between documented facts and inference, and remains responsible for the exclusion decision.

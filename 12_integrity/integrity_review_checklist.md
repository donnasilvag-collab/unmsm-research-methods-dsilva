# Research-integrity review checklist

## Purpose

This checklist records the minimum integrity review for material added to the repository. It applies to research writing, code, public benchmark updates, and any future fieldwork output.

| Review area | Check before publication or submission |
| --- | --- |
| Authorship and contribution | The author can explain the research question, methods, analytical decisions, and conclusions. Contributors and support tools are acknowledged accurately. |
| Sources and citations | Each factual claim has an appropriate source where one is needed. References are checked against the cited work and are not copied from an unverified bibliography. |
| Data provenance | Public data retain their source and extraction information. Restricted data remain outside the public repository. |
| Reproducibility | Scripts, parameters, input paths, and expected outputs are documented. Results are not presented as rerun if the command was not executed. |
| Privacy and confidentiality | The material contains no participant identifiers, credentials, private source code, confidential documents, or disclosure-prone quotations. |
| Interpretation | Claims match the design and evidence. Public observability proxies are not described as verified internal controls or causal effects. |
| AI assistance | The use of AI is disclosed when it affected drafting, coding, editing, or analysis support. The author verifies all substantive content before release. |
| Corrections | Errors, changed sources, or revised methods are documented in a commit and, when material, in the affected file. |

## Review outcome

Before a release, the author records one of the following outcomes in the relevant document or commit message:

- approved for public release;
- approved only as a restricted academic record;
- needs revision before release.

This checklist supports the ethics protocol in `09_ethics/` and the data management plan in `10_data_mgmt/`. It does not replace institutional review or legal advice.

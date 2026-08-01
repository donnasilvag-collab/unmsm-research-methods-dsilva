# Reproducibility audit report

## 6.1. Article audited

Chen, C., Bao, L., Lo, D., Wang, Y., Shan, Z., Chen, T., Yin, G., Yu, J., Zheng, Z., & Chen, J. (2026). TRACE: Securing smart contract repository against access control vulnerability. *IEEE Transactions on Software Engineering, 52*(4), 1301-1314. https://doi.org/10.1109/TSE.2026.3660900

This audit was conducted on the first arXiv version, submitted on 22 October 2025 as arXiv:2510.19254v1. That exact snapshot is preserved in [trace_2510.19254v1.pdf](trace_2510.19254v1.pdf). A peer-reviewed version was subsequently published in *IEEE Transactions on Software Engineering* in 2026. The scores below remain tied to the audited v1 preprint and should not be transferred automatically to the journal version. A separate audit would be required to determine whether the final article or its artifacts resolved any of the issues recorded here.

The public source code, datasets, and installation instructions are available at [BugmakerCC/Trace](https://github.com/BugmakerCC/Trace). TRACE was selected because it evaluates an LLM-supported method for detecting access-control vulnerabilities in source-code repositories. This connects directly with the technical side of the present study: access control, source-code protection, repository artifacts, and traceability.

TRACE is not part of the frozen ten-paper corpus in `04_literature/`. That preliminary corpus was assembled before the journal publication was verified. The final literature review should reassess TRACE against the stated date range, eligibility criteria, and search protocol rather than adding it retrospectively without rerunning the screening record.

## 6.2. Reproducibility scorecard

The course scorecard is applied to the stochastic parts of TRACE. The paper is not a conventional supervised-training study, so a train, validation, and test split is not expected in the usual sense. The comparable requirement is a complete and repeatable account of dataset selection, sampling, LLM configuration, and evaluation.

| No. | Item | Score | Evidence and assessment |
| ---: | --- | --- | --- |
| 1 | Random seeds reported | No | The audited version states that the models were accessed through API calls with default parameter settings. It does not report a seed, temperature, sampling configuration, model snapshot, or another means of controlling stochastic LLM behavior. |
| 2 | Data splits or equivalent sampling described | Partial | The paper identifies 15 CVE-tagged contracts, 5,000 recent on-chain contracts, and 83 repositories sampled from DAppSCAN. It also states that 91 contracts were selected for manual labeling. It does not report the sampling seed, a frozen repository manifest, or checksums that would reconstruct the exact sample without the linked artifact. |
| 3 | Multiple runs and variability reported | No | One set of precision, recall, compilation, and failure values is reported for each setting. Repeated API-based LLM calls and run-to-run variation are not documented. |
| 4 | Statistical significance test used | No | The baseline comparisons are descriptive. The audited version does not report a paired test, bootstrap comparison, or other procedure for assessing experimental variation. |
| 5 | Effect size or confidence interval shown | No | The paper gives point estimates, including 89.2% precision on the on-chain dataset and 87.0% precision on repositories, without confidence intervals or another variance measure. |
| 6 | Compute environment documented | Partial | The evaluation reports Ubuntu 22.04.5 LTS, 10 CPU cores, 20 GB of RAM, and a 30-minute limit per tool and contract. It does not specify the LLM API model revision, API cost, total execution time, or call count for each experiment. |
| 7 | Code and data accessible | Yes | The public repository contains source code, datasets, evaluation outputs, a dependency file, and basic execution instructions. Reproduction still depends on an external LLM API and on provider behavior at the time of execution. |

## 6.3. Overall assessment

**One of seven items is fully met, two are partially met, and four are not met.**

The audited snapshot has a useful artifact record: its public repository contains implementation code, data folders, evaluation outputs, and a requirements file. The weaker part is the experimental record. A reader can inspect the inputs and code but cannot determine how much the results depend on API nondeterminism, provider defaults, the sampled repositories, or the model version available at the time of execution.

The reported scores should therefore be treated as results from the stated execution, not as stable estimates with known uncertainty. This judgment does not reject the technical contribution or the later peer-reviewed publication. It limits the reproducibility claims that can be made from the archived v1 materials reviewed here.

## 6.4. Relevance to the present study

TRACE treats repositories as development artifacts and addresses access-control vulnerabilities through source-code analysis and LLM assistance. It also distinguishes a reported risk from a confirmed vulnerability. That distinction matters for the public benchmark in `05_pipeline/`, where an absent public signal means "not observed," not proof that an internal control is absent.

TRACE should not be used as a numerical benchmark for this research. Its unit of analysis is a Solidity smart-contract repository, its outcome is vulnerability detection, and its datasets are unrelated to Peruvian companies. Its estimates in the audited snapshot also lack uncertainty intervals. It may inform the technical framing of repository-level access-control research, but it cannot serve as a target score for the public benchmark or future fieldwork.

The current project addresses several audit gaps in its own bounded benchmark. `05_pipeline/` includes a source workbook, a DVC preparation stage, explicit parameters, four recorded seeds, a 2,000-iteration organization-clustered bootstrap, and per-seed result tables. These controls apply only to the descriptive public-repository analysis. They do not replace the protected survey and interview workflow.

## 6.5. Priority improvements for a stranger test

1. Record the complete LLM execution configuration: provider, exact model revision, prompt version, temperature, sampling parameters, supported seed, run date, and call count.
2. Publish a versioned manifest of sampled contracts and repositories with source URLs, selection rules, timestamps, and file hashes.
3. Repeat stochastic LLM evaluations and report dispersion or bootstrap confidence intervals. Compare TRACE and each baseline with a paired procedure suited to shared evaluation units.

## Sources reviewed

- Chen et al. (2025), arXiv:2510.19254v1, preserved in this folder.
- Chen et al. (2026), the institutional bibliographic record for the *IEEE Transactions on Software Engineering* article: https://ink.library.smu.edu.sg/sis_research/11023/
- TRACE public code and datasets: https://github.com/BugmakerCC/Trace
- Course guidance on splits, repeated runs, uncertainty, statistical comparison, compute documentation, and the stranger test.

---

**AI support statement:** AI tools supported language editing and scorecard formatting. Donna Silva reviewed the audited preprint, the linked repository, and the updated publication record and remains responsible for the assessment.

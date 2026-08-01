# Reproducibility audit report

## 6.1. Article audited

Chen, C., Chen, J., Bao, L., Lo, D., Wang, Y., Shan, Z., Chen, T., Yin, G., Yu, J., and Zheng, Z. (2025). *TRACE: Securing Smart Contract Repository Against Access Control Vulnerability*. arXiv:2510.19254v1. https://doi.org/10.48550/arXiv.2510.19254

The preprint was submitted to arXiv on 22 October 2025. Its public source code, datasets, and installation instructions are available at [BugmakerCC/Trace](https://github.com/BugmakerCC/Trace). A copy of the audited preprint is included as [trace_2510.19254v1.pdf](trace_2510.19254v1.pdf).

This paper was selected because it evaluates an LLM-supported method for detecting access-control vulnerabilities in source-code repositories. It is close to the technical side of this study, particularly the relationship between access control, source-code protection, repository artifacts, and traceability. It is not one of the ten studies in the systematic review because it is a preprint rather than a peer-reviewed publication. Its role here is methodological: to examine whether a relevant AI and software-security experiment can be independently rerun.

## 6.2. Reproducibility scorecard

The course scorecard is applied to the stochastic parts of TRACE. The paper is not a conventional supervised-training study, so a train, validation, and test split is not expected in the usual sense. The comparable requirement is a complete and repeatable account of dataset selection, sampling, LLM configuration, and evaluation protocol.

| No. | Item | Score | Evidence and assessment |
| ---: | --- | --- | --- |
| 1 | Random seeds reported | No | TRACE states that the models were accessed through API calls with "default parameter settings." It does not report a seed, temperature, sampling configuration, model snapshot, or a way to control the stochastic behavior of the LLM calls. |
| 2 | Data splits or equivalent sampling described | Partial | The paper identifies three evaluation sources: 15 CVE-tagged contracts, 5,000 recent on-chain contracts, and 83 repositories sampled from DAppSCAN. It also states that 91 contracts were randomly selected for manual labeling. However, it does not provide the sampling seed, a frozen repository manifest, or checksums that would let another researcher reconstruct the exact sample without relying on the linked artifact. |
| 3 | Multiple runs and variability reported | No | The article reports one set of precision, recall, compilation, and failure values for each setting. It does not repeat API-based LLM calls or report variation across runs, although the default API calls may be nondeterministic. |
| 4 | Statistical significance test used | No | The comparisons with baseline tools are descriptive. The article reports differences in precision and recall but does not use a paired test, bootstrap comparison, or other formal procedure to assess whether the observed differences exceed experimental variation. |
| 5 | Effect size or confidence interval shown | No | The paper gives point estimates such as 89.2% precision on the on-chain dataset and 87.0% precision on repositories. It provides neither confidence intervals nor a variance measure for those estimates. |
| 6 | Compute environment documented | Partial | The evaluation reports Ubuntu 22.04.5 LTS, 10 CPU cores, 20 GB of RAM, and a 30-minute limit per tool and contract. It does not specify the LLM API model revision, GPU use, API cost, total execution time, or the number of calls made for each experiment. |
| 7 | Code and data accessible | Yes | The public repository contains source code, datasets, evaluation outputs, a dependency file, and basic execution instructions. Reproduction still depends on an external LLM API key and on the provider behavior available at the time of rerunning. |

## 6.3. Overall assessment

**1 of 7 items is fully met, 2 are partially met, and 4 are not met.**

TRACE has a stronger artifact record than many papers that only describe their method: a public repository contains the implementation, data folders, evaluation outputs, and a requirements file. That is a meaningful strength. The gap is in the experimental record. A reader can inspect the code and inputs, but cannot determine whether a second set of API calls would produce the same outputs or how much the reported performance depends on the sampled repositories, the model version, or the provider defaults.

The reported scores should therefore be read as results from the stated execution, not as stable estimates with known uncertainty. This does not invalidate the contribution. It limits the strength of claims that TRACE is more precise than its baselines across repeated runs or other repository samples.

## 6.4. Relevance to the present study

The paper is useful because it treats repositories as software-development artifacts and addresses access-control vulnerabilities through a combination of source-code analysis and LLM assistance. It also makes a careful distinction between a reported risk and a confirmed vulnerability. That distinction is relevant to the public benchmark in `05_pipeline`, where an absent public signal means "not observed" rather than evidence that an internal control is absent.

TRACE should not be used as a numerical benchmark for the present research. Its unit of analysis is a Solidity smart-contract repository, its outcome is vulnerability detection, and its datasets are unrelated to Peruvian companies. In addition, its headline estimates lack uncertainty intervals. The study can cite the paper for its technical framing of access-control and repository-level security, but not as a target score for the public benchmark or future fieldwork.

The current project addresses several of the gaps noted in this audit for its own public benchmark. The `05_pipeline` folder includes the source workbook, a DVC preparation stage, explicit parameters, four recorded seeds, a 2,000-iteration organization-clustered bootstrap, and per-seed result tables. These controls apply only to the repository-level descriptive benchmark. They do not substitute for the protected survey and interview workflow planned for the mixed-methods study.

## 6.5. Priority improvements for a stranger test

1. Record the complete LLM execution configuration: provider, exact model revision, prompt version, temperature, other sampling parameters, seed when the API supports it, date of each run, and the number of calls.
2. Publish a versioned manifest of the sampled contracts and repositories, including source URLs, selection rule, timestamp, and file hashes. A public repository link is helpful, but it does not by itself preserve the exact sample.
3. Repeat the stochastic LLM evaluation across several runs and report mean performance with dispersion or bootstrap confidence intervals. Compare TRACE and each baseline with a paired statistical procedure that matches the shared evaluation units.

## Sources reviewed

- Chen et al. (2025), the preprint included in this folder.
- [TRACE public code and datasets](https://github.com/BugmakerCC/Trace).
- Session 6 course guidance on splits, repeated runs, uncertainty, statistical comparison, compute documentation, and the stranger test.

AI tools were used to improve wording and format the scorecard. The assessment is based on the public preprint, its linked repository, and the criteria from the course material.

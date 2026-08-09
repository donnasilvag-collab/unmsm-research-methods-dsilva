# Research presentation

This folder contains the institutional HTML presentation for Donna Silva's research project, *Madurez de la gestión de riesgos y eficacia de los controles de desarrollo seguro en empresas peruanas*.

Open [`index.html`](index.html) in a modern browser. Use the left and right arrow keys to move between slides, `Home` or `End` to jump to the first or last slide, and `F` to enter full-screen mode. Touch gestures and the on-screen controls are available on smaller devices.

The deck contains 16 slides that summarize the research problem, question, method, analytical algorithm, instruments, ethics, reproducibility plan, public benchmark, limitations, feasibility, and next steps. Public benchmark values are labeled as descriptive evidence. The presentation does not report fieldwork findings because participant recruitment and data collection have not begun.

`assets/unmsm-logo.svg` is the institutional visual used by the HTML file. Keep the `assets/` folder beside `index.html` when presenting without an internet connection.

## Speaker guide

The deck is designed for an 18 to 22 minute presentation. The notes below are prompts rather than a script. They preserve the distinction between the planned field study, the completed public benchmark, and the synthetic software tests.

### Slide 1: Cover

Introduce yourself, the university, and the research title. Explain that the project is a doctoral protocol about whether mature information security risk management is associated with more effective controls during software development in Peruvian companies. Name the three control outcomes so the audience knows the scope from the beginning: access control, source code protection, and development traceability.

Transition: The next slide gives the complete study in one view before examining each decision.

### Slide 2: Research overview

Summarize the project in three sentences. The quantitative phase will identify patterns through a structured survey. Interviews and authorized document review will then explain why those patterns appear or differ across settings. Clarify that the current repository contains a finished protocol, a preliminary review, executable code, and a public benchmark, but no company fieldwork findings.

Transition: That distinction matters because the study begins with a gap between written security policy and everyday practice.

### Slide 3: Research problem

Explain that agile and DevOps teams work with repositories, privileged access, automated pipelines, and change records under delivery pressure. A company may own security tools and policies without applying them consistently. The research therefore examines operational effectiveness rather than counting whether a formal control exists. Briefly connect unauthorized access, code exposure, and incomplete traceability to operational, intellectual-property, and audit risks.

Transition: Once the problem is clear, the variables and research question can be stated precisely.

### Slide 4: Question and objective

Present risk-management maturity as the explanatory variable. Its dimensions cover governance, identification, assessment, treatment, monitoring, training, and continuous improvement. The three outcomes are access-control effectiveness, source-code protection, and development traceability. State that the objective is to analyze associations and then use qualitative evidence to explain them. Avoid the word "impact" because the cross-sectional design cannot establish causality.

Transition: The literature supports these constructs, but it also shows why evidence from Peru is needed.

### Slide 5: Literature review

Walk through the PRISMA counts: 43 records were identified, 36 remained after duplicate removal, 16 full texts were assessed, and 10 studies were retained. The preliminary synthesis shows uneven security integration, weak DevOps governance in some settings, and the importance of leadership, culture, and training. Acknowledge that the original export of all 43 identification records was not preserved. The final thesis review must rerun the search and retain complete exports and exclusion decisions.

Transition: Because the problem requires both measurement and explanation, the method cannot be selected on convenience alone.

### Slide 6: Method selection

Explain that three plausible methods were compared. The explanatory sequential mixed methods design obtained 23 points, compared with 19 for the correlational option and 18 for the multiple case study. The selected design can estimate patterns and then examine the organizational conditions behind them. A survey alone would rely heavily on self-report, while case studies alone would provide less comparative evidence.

Transition: The selected method is useful only if the two phases are connected rather than conducted as separate exercises.

### Slide 7: Mixed methods design

Describe the sequence from left to right. The survey produces quantitative patterns. Those results guide the selection of contrasting cases and questions for the qualitative phase. Interviews and authorized documents then help explain, qualify, or challenge the numerical patterns. Integration takes place during qualitative sampling and again in the joint interpretation. A disagreement between sources is a result to analyze, not a problem to hide.

Transition: The next slide shows the analytical algorithm used inside the quantitative phase.

### Slide 8: Analytical algorithm

Explain the five steps clearly. First, 32 survey items are converted into an overall maturity score and three control outcomes under minimum-completeness rules. Second, three Spearman correlations estimate the predefined associations. Third, a 2,000-iteration bootstrap resamples whole organizations to produce 95% intervals without treating colleagues as fully independent. Fourth, up to three exploratory regressions may adjust for no more than two prespecified contextual variables. Fifth, leave-one-organization-out checks and the joint display test the stability and interpretation of the results. Regression requires at least 50 eligible participants across six organizations. The current 64-record execution is synthetic and verifies code only.

Transition: Those thresholds connect the algorithm to a feasible recruitment and evidence plan.

### Slide 9: Participants and instruments

State the intended coverage: 50 to 80 survey participants from 6 to 10 organizations, followed by 10 to 15 qualitative informants. Participants may include developers, technical leaders, DevOps practitioners, quality staff, and security practitioners. The evidence comes from a structured survey, semistructured interviews, and targeted document review. Because the organization count is small, comparisons between companies remain descriptive and the quantitative inference is exploratory.

Transition: Access to this evidence depends on safeguards that protect both participants and organizations.

### Slide 10: Ethics and data management

Discuss harm before procedure. Participants could face employment or reputational harm if a weak practice were identifiable. Interviews could also reveal security-sensitive information. Explain the safeguards: voluntary consent, withdrawal rules, pseudonymization, aggregate reporting, separation of identifiers, and disclosure review. The study will not request credentials, proprietary code, private repository addresses, vulnerability details, security configurations, or incident evidence. Recruitment begins only after the applicable review is confirmed.

Transition: Ethical protection applies to fieldwork, while reproducibility applies to every public analytical step.

### Slide 11: Reproducible architecture

Explain the role of each component. Git versions the protocol, code, and approved outputs. DVC declares how the public workbook becomes an analytical dataset. Python validates and analyzes the records. MLflow stores parameters, seeds, metrics, and artifacts. GitHub Actions repeats the checks on Linux. Docker defines the planned isolated environment, but its build remains unverified and should not be presented as completed.

Transition: This architecture is exercised with a bounded public benchmark that contains no confidential company data.

### Slide 12: Public benchmark

Describe the benchmark as a methodological demonstration: 48 public repositories, split evenly between the Peru stratum and an international reference, with nine public organization owners in the Peru stratum. The four dimensions use visible repository signals. They are public-observability proxies, not measurements of internal company maturity. An absent signal means only that it was not observed in the selected public source.

Transition: With that boundary established, the descriptive differences can be interpreted without turning them into company ratings.

### Slide 13: Descriptive results

Report that the Peru stratum has lower mean public-observability scores in all four dimensions shown on the slide. Give one or two examples rather than reading every number. Emphasize that the result applies only to the selected public repositories and observation date. It does not represent all Peruvian companies, identify a causal mechanism, or answer the doctoral research question.

Transition: The result also changes when dependence among repositories from the same owner is handled correctly.

### Slide 14: Bias, limitations, and integrity

Explain why 24 repositories do not equal 24 independent organizations. The Peru stratum contains nine owners, so the audit resamples by owner and obtains wider intervals in every dimension. A leave-one-owner-out analysis checks whether one organization dominates the difference. The audit does not calculate demographic fairness because the artifact is not a predictive model and contains no person-level protected attributes. Its purpose is to identify selection, coverage, clustering, missingness, and reputational risks.

Transition: These limits inform what one researcher can complete within the proposed schedule.

### Slide 15: Feasibility and challenges

Present the 36-month schedule, target sample, and preliminary PEN 4,500 resource estimate as planning assumptions. The main practical risk is access to organizations willing to discuss security practices. Self-report, sensitive subject matter, and limited generalizability are also expected constraints. The design addresses them through focused eligibility, complementary evidence, protected collection, and conclusions limited to the observed participants and organizations.

Transition: The closing slide separates what the project has established from what still requires field evidence.

### Slide 16: Conclusions and next steps

Conclude that the protocol is methodologically coherent, ethically bounded, and reproducible at the software-demonstration level. Do not claim that mature risk management already improves controls in Peruvian companies. That proposition still requires validated instruments, ethical approval, recruitment, survey data, interviews, and authorized documentary evidence. End with the expected contribution: an explanation of the organizational conditions associated with more consistent secure-development controls.

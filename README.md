# UNMSM Research Methods and Scientific Integrity in AI

[![Repository quality](https://github.com/donnasilvag-collab/unmsm-research-methods-dsilva/actions/workflows/repository-quality.yml/badge.svg)](https://github.com/donnasilvag-collab/unmsm-research-methods-dsilva/actions/workflows/repository-quality.yml)

**Author:** Donna Silva

**Professor:** Dr. Loveleen Gaur

## Project Focus

This repository organizes the course deliverables around the following research topic:

**Madurez de la gestión de riesgos y eficacia de los controles de desarrollo seguro en empresas peruanas**

## Academic Purpose

This repository brings together the main deliverables for the course *Research Methods and Scientific Integrity in AI and Advanced Technologies*. It follows the sequence of the course from paradigm selection and protocol design through systematic review, reproducibility, ethics, bias auditing, and research integrity.

## Repository Structure

- `01_paradigm/`: research paradigm justification.
- `02_method/`: method comparison and methodological fit matrix.
- `03_protocol/`: core research protocol, operationalization matrix, survey, interview guide, document-review form, and validation procedure.
- `04_literature/`: preliminary systematic review, search and screening records, quality appraisal, gap analysis, validated PRISMA diagram, and prospective search protocol for the thesis review.
- `05_pipeline/`: executable Git + DVC + MLflow + Docker pipeline based on a bounded public repository benchmark, plus a synthetic test of the future survey-scoring rules.
- `06_repro_audit/`: reproducibility audit of a relevant public AI and software-security experiment.
- `07_model_card/`: analytical artifact card and datasheet for the public repository security benchmark.
- `09_ethics/`: ethics protocol for the planned mixed methods fieldwork and the bounded public benchmark.
- `10_data_mgmt/`: data management plan for public benchmark materials and planned fieldwork data.
- `11_bias_audit/`: bias audit of the public benchmark and safeguards for the planned fieldwork.
- `12_integrity/`: research-integrity records, AI-use policy, and literature-screening controls.
- `13_presentation/`: institutional HTML presentation summarizing the research design, current evidence, limitations, and next steps.

The numbering follows the course delivery sequence. Checkpoint `08` is an integration point rather than a separate deliverable, so the repository does not create an empty placeholder folder. The twelve numbered folders therefore follow the same main structure as the reference repository while retaining the instruments and audit records required by this research design.

`03_protocol/protocol_v1.0.md` is the current protocol. Version `v0.1` is retained as history. A later version will be created only after genuine methodological feedback, instrument testing, or an approved protocol amendment.

## Study Focus

The study is designed to understand how the maturity of information security risk management relates to three critical capabilities in software development:

- access control effectiveness;
- source code protection;
- software development traceability.

The applied scope of the study is situated in **Peruvian software development companies**, with particular interest in agile, DevOps, or continuous-integration environments. The planned field study uses an explanatory sequential mixed methods design. Its quantitative component is exploratory because the feasible sample covers 50 to 80 participants grouped in only 6 to 10 companies.

## Reproduce the public pipeline

The executable benchmark uses public repository data and remains separate from protected fieldwork. From the repository root on Windows PowerShell:

```powershell
cd 05_pipeline
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
dvc repro
python src/run_experiments.py
cd ..
.\05_pipeline\.venv\Scripts\python.exe 11_bias_audit\bias_audit.py
```

The final command compares naive and organization-aware uncertainty and performs a leave-one-owner-out sensitivity audit. Numerical outputs are written to `11_bias_audit/*.csv`; no company or repository ranking is produced.

The scoring rules for the future survey can be tested without protected data:

```powershell
cd 05_pipeline
python src/generate_synthetic_fieldwork.py
python src/score_fieldwork.py --input fieldwork/synthetic/survey_responses_synthetic.csv --output-dir fieldwork/synthetic --synthetic
```

These commands use 22 synthetic records. They verify the item schema, completeness rules, missing-value treatment, and suppression threshold. They do not validate the instrument or produce findings about Peruvian companies.

Docker instructions are available in [`05_pipeline/README.md`](05_pipeline/README.md). Docker remains an unverified option until the image can be built and run in an available Docker environment.

## Research boundary

The committed workbook is a bounded public-repository benchmark. It does not measure the internal risk-management maturity of a company and cannot answer the fieldwork question. The synthetic survey records test code only. Survey responses, interviews, consent records, organizational evidence, credentials, proprietary code, and security-sensitive information must remain outside Git and follow the ethics and data-management controls in this repository.

# Fieldwork scoring bridge

## Purpose and boundary

This module implements the scoring rules defined in the operationalization matrix before protected fieldwork begins. It validates the 32 substantive survey items, calculates the seven risk-management dimensions, derives the overall maturity score, and calculates the three control-effectiveness outcomes.

The committed records are synthetic. They do not describe a person, company, repository, or observed security practice. Their only purpose is to test the schema, minimum-completeness rules, missing-value handling, and small-group reporting rule. They cannot establish reliability, validity, an association between variables, or a research finding.

## Input schema

The scoring script requires two coded identifiers and the 32 items from the survey. Context fields are optional.

| Field | Rule |
| --- | --- |
| `participant_code` | Unique study code. Do not use a name, email address, or employee identifier. |
| `organization_code` | Controlled organization code. Do not use the company name. |
| `role_group`, `experience_group`, `company_size_group`, `delivery_approach` | Optional controlled categories defined in `params.yaml`. Free text is rejected. |
| `RM01` to `RM14` | Values from 1 to 5 or an approved missing token. |
| `AC01` to `AC06` | Values from 1 to 5 or an approved missing token. |
| `SC01` to `SC06` | Values from 1 to 5 or an approved missing token. |
| `TR01` to `TR06` | Values from 1 to 5 or an approved missing token. |

The script does not accept free-text comments, consent records, contact details, company names, repository addresses, or security evidence. Eligibility and consent must be resolved before a protected export enters the scoring environment.

## Reproduce the synthetic test

Run these commands from `05_pipeline/`:

```powershell
python src/generate_synthetic_fieldwork.py
python src/score_fieldwork.py --input fieldwork/synthetic/survey_responses_synthetic.csv --output-dir fieldwork/synthetic --synthetic
```

The first command always produces the same 22 synthetic records with four controlled missing-data cases. Three synthetic organizations meet the reporting threshold and one does not. The second command writes participant scores, an overall summary, item missingness, and deterministic metadata. When any organization is below the threshold in `params.yaml`, the script withholds the full organization breakdown. This prevents readers from reconstructing the small group's mean by subtracting the reported organizations from the overall result.

## Use with authorized fieldwork data

Real survey exports must remain in protected storage outside this repository. Run the script in that environment and direct the output to a protected location:

```powershell
python src/score_fieldwork.py --input D:\protected\survey_export.csv --output-dir D:\protected\scored
```

Before using those scores for correlations or regression, complete expert review, cognitive testing, pilot testing, ethics or institutional review, and the version freeze described in `03_protocol/instruments/validation_procedure.md`. The analytical thresholds in the protocol still apply. This scoring module does not authorize fieldwork and does not replace psychometric assessment.

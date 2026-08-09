# Semistructured interview guide

## Purpose

The interviews explain quantitative patterns, especially differences among control dimensions and cases in which reported maturity does not match control effectiveness. They are not compliance inspections. The interviewer must not ask for credentials, proprietary source code, private repository addresses, exploitable vulnerability details, client information, or identifiable incident records.

Participants will be selected after the survey analysis using predefined contrast criteria. Selection may consider high or low scores, disagreement among dimensions, missing perspectives by role, and cases where authorized documentary evidence does not match survey patterns. Participation remains voluntary and does not affect employment.

## Opening script

Thank you for considering this interview. The study examines how information-security risk-management practices relate to access control, source-code protection, and traceability in software development. I am interested in the way work is organized, not in confidential technical details or individual performance.

With your permission, the interview will be recorded for transcription. You may decline recording, skip a question, ask to pause, or withdraw. Please do not name customers, systems, repositories, colleagues, vulnerabilities, or incidents. If sensitive detail arises, I will stop that part of the discussion and redirect the question.

Confirm before proceeding:

- informed consent remains valid;
- recording permission is granted or declined;
- the participant understands the confidentiality boundary;
- the participant has no question about withdrawal or use of quotations.

## Core questions and probes

| Code | Core question | Optional probes | Link to quantitative phase |
| --- | --- | --- | --- |
| IN01 | How are software-security risks identified and discussed in your normal development work? | Who starts the discussion? At what point in delivery? What makes a risk visible? | RM03-RM04 |
| IN02 | How does the company decide which security risks need action first? | What criteria are used? Who can accept residual risk? How is urgency balanced with delivery pressure? | RM05-RM08 |
| IN03 | What happens after a risk-treatment action is assigned? | How are deadlines, exceptions, and closure reviewed? What causes follow-up to fail? | RM07-RM10 |
| IN04 | In practice, how is access to repositories and delivery tools granted, changed, reviewed, and removed? | Where do formal rules and daily practice differ? How are privileged or emergency changes handled? | AC01-AC06 |
| IN05 | Which practices protect source code and build or release artifacts from unauthorized change or exposure? | How are reviews, secrets, dependencies, automated checks, and release artifacts handled? | SC01-SC06 |
| IN06 | If an authorized reviewer needed to reconstruct a change from request to deployment, what evidence would be available? | Which links are automatic? Which depend on manual work? Where does the chain usually break? | TR01-TR06 |
| IN07 | What organizational conditions make these controls work consistently? | Consider leadership, staffing, training, role clarity, tooling, incentives, and time pressure. | RM01-RM14 and all outcomes |
| IN08 | The survey showed a pattern that requires explanation: `[insert only an approved aggregate or participant-specific prompt]`. How do you interpret it? | Does the pattern fit your experience? What alternative explanation should be considered? | Selected quantitative result |
| IN09 | Can you describe a case in which a formal control existed but did not work as intended, without revealing sensitive details? | What blocked it? How was the problem detected? What changed afterward? | Divergent case |
| IN10 | Which feasible change would most improve secure-development controls in this setting? | Who would need to act? What resource or dependency could prevent the change? | Recommendations and feasibility |

## Adaptive follow-up rules

The interviewer may change question order and use neutral probes such as "What happened next?" or "What evidence informed that decision?" A follow-up must not assume that a control is absent or ineffective. It must not ask the participant to confirm a preferred explanation.

Questions about a survey result will use only information approved for that interview. Cross-company rankings, named comparisons, and another participant's answers are prohibited. The interview guide will record any skipped core question and the reason when known.

## Closing script

Ask whether the participant wishes to clarify or withdraw any statement. Explain that quotations may be edited to remove identifying or security-sensitive detail without changing their meaning. Confirm whether the participant agrees to the use of anonymized quotations. Record the answer separately from the transcript.

## Interviewer field note

Complete immediately after the interview:

| Field | Record |
| --- | --- |
| Study interview code |  |
| Date and mode |  |
| Broad participant role |  |
| Recording status |  |
| Core questions not asked |  |
| Sensitive-detail interruption required | Yes / No; describe handling without repeating the detail |
| Initial explanatory points |  |
| Possible contradiction or negative case |  |
| Follow-up evidence needed |  |
| Disclosure risk noted |  |

---

**AI support statement:** AI tools assisted with organization and language review. Donna Silva determined the interview logic and remains responsible for ethical administration, probing decisions, and interpretation.

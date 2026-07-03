# Scoring and Classification Rules

Use this reference after applying `references/evaluation-rubric.md`.

## Purpose

Convert the Job A and Job B evaluation scores into final candidate classifications and recruiter outreach priorities.

Scores support structured comparison, but they must not replace evidence review or human judgment.

## Role Fit Score

Each valid candidate receives:

- Job A score: 0 to 100.
- Job B score: 0 to 100.

Use the weighted rubric in `references/evaluation-rubric.md` to calculate each role score.

## Score Bands

Interpret each role score using these bands:

| Score Range | Interpretation |
|---:|---|
| 85-100 | Strong fit |
| 70-84 | Good potential fit |
| 55-69 | Possible fit with concerns |
| 40-54 | Weak or uncertain fit |
| 0-39 | Not currently supported |

## Minimum Evidence Rule

A candidate should not be treated as a strong fit when the score is based mainly on unknown or vague evidence.

Before assigning a high recommendation, confirm that the candidate has meaningful evidence for the most important mandatory requirements.

## Final Classification Thresholds

Assign exactly one final classification to every evaluated candidate.

### Job A

Assign `Job A` when:

- Job A score is at least 70.
- Job A score is at least 10 points higher than Job B.
- Job A mandatory requirements are sufficiently supported.
- No confirmed blocking constraint prevents Job A placement.

### Job B

Assign `Job B` when:

- Job B score is at least 70.
- Job B score is at least 10 points higher than Job A.
- Job B mandatory requirements are sufficiently supported.
- No confirmed blocking constraint prevents Job B placement.

### Both

Assign `Both` when:

- Job A score is at least 70.
- Job B score is at least 70.
- Both roles have sufficient evidence for their mandatory requirements.
- No confirmed blocking constraint prevents placement in either role.

When assigning `Both`, choose a preferred primary role using:

1. Higher role score.
2. Stronger mandatory-requirement evidence.
3. Stronger role-specific experience.
4. Fewer unresolved constraints.
5. Clearer recruiter follow-up path.

If the preferred role cannot be determined reliably, preserve the tie and add a human-review note.

### Neither

Assign `Neither` when:

- Both Job A and Job B scores are below 55, or
- Neither role has sufficient evidence for mandatory requirements, or
- Confirmed blocking constraints prevent placement in both roles.

Do not assign `Neither` only because optional or preferred information is missing.

## Borderline Classification Rules

Use human-review notes when:

- One role score is between 65 and 74.
- The score difference between Job A and Job B is less than 10 points.
- A mandatory requirement is partially supported but not fully confirmed.
- A constraint could be blocking but is not verified.
- The profile contains strong evidence but lacks dates, duration, scope, or seniority clarity.

Borderline candidates should usually be placed in `Review Next` unless the evidence strongly supports immediate outreach.

## Outreach Priority Thresholds

After final classification, assign one outreach priority.

### Contact Now

Use `Contact Now` when:

- The candidate is classified as Job A, Job B, or Both.
- The preferred role score is at least 80.
- Mandatory requirements are strongly supported.
- Evidence is clear enough for recruiter action.
- No confirmed blocking constraint exists.
- Follow-up questions are useful but not essential to determine basic fit.

### Review Next

Use `Review Next` when:

- The preferred role score is between 65 and 79, or
- Important evidence is partial or unknown, or
- A follow-up question could materially change the recommendation, or
- The candidate has promising experience but unclear seniority, scope, availability, language, compensation, or placement feasibility.

### Keep in Reserve

Use `Keep in Reserve` when:

- The preferred role score is between 55 and 64, or
- The candidate has relevant background but is less competitive than stronger candidates, or
- The candidate may be useful if higher-priority candidates are unavailable.

### Do Not Prioritize

Use `Do Not Prioritize` when:

- The candidate is classified as Neither, or
- The preferred role score is below 55, or
- The profile does not provide enough job-related evidence for outreach, or
- A confirmed blocking constraint prevents placement.

Do not use `Do Not Prioritize` as a final rejection. It only means the candidate should not be contacted first for the current roles.

## Constraint Handling

Confirmed blocking constraints can lower outreach priority even when the technical score is strong.

Examples:

- Required on-site work and candidate is only available remotely.
- Required language level is not demonstrated.
- Required work authorization is contradicted.
- Compensation expectations clearly exceed the available range, when both values are known.
- Availability does not match the role need.

If a constraint is unknown, do not treat it as confirmed. Add a follow-up question.

## Tie Handling

When candidates have similar evidence and scores:

- Do not create artificial precision.
- Preserve ties when justified.
- Use priority tiers instead of forcing exact ordering.
- Explain what information would break the tie.

## Score Adjustment Rules

Only adjust a score when the evidence supports the adjustment.

Do not add points for:

- Vague claims without supporting detail.
- Job titles alone.
- Technologies mentioned only once without context.
- Assumptions about seniority.
- Non-job-related personal characteristics.

Do not subtract points for:

- Missing optional information.
- Unknown information that was not requested by the job.
- Lack of irrelevant technologies.
- Protected or sensitive personal characteristics.

## Required Output

For every candidate, record:

- Job A score.
- Job B score.
- Final classification.
- Preferred primary role.
- Outreach priority.
- Main score drivers.
- Main score limitations.
- Follow-up question.
- Human-review note when applicable.

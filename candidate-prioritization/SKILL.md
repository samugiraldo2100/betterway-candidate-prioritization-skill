---
name: candidate-prioritization
description: Evaluates, classifies, and prioritizes candidate profiles against two job descriptions using job-related evidence and transparent reasoning. Use when the user provides resumes, CVs, candidate profiles, or folders together with two roles and asks to compare fit, rank candidates, identify who to contact first, or classify candidates for Job A, Job B, both, or neither.
license: MIT
compatibility: Requires readable job descriptions and candidate files. Publishing to Notion requires an authenticated Notion MCP connection.
metadata:
  author: Samuel Giraldo
  version: 0.1.0
  category: recruiting-workflow
  mcp-server: notion
---

# Candidate Prioritization

## Purpose

Evaluate a collection of candidate profiles against two job descriptions and produce a transparent, evidence-based recruiter contact priority.

The skill analyzes every candidate against both roles, classifies each candidate as Job A, Job B, Both, or Neither, and prepares clear recommendations for human review.

## Critical Rules

- Evaluate candidates only against job-related requirements found in the two job descriptions.
- Review every candidate against both jobs before assigning a final classification.
- Classify every candidate into exactly one overall category: Job A, Job B, Both, or Neither.
- Do not classify or rank candidates using keyword matches alone.
- Support every important recommendation with evidence found in the supplied candidate profile.
- Distinguish missing information from information confirmed to be absent.
- Do not invent experience, skills, education, certifications, location, salary expectations, language proficiency, availability, or employment history.
- Do not use protected or sensitive personal characteristics as evaluation criteria.
- Treat scores and rankings as decision-support indicators, not final hiring decisions.
- Add human-review notes whenever evidence is incomplete, ambiguous, outdated, or contradictory.
- Ensure every candidate appears exactly once in the final overall classification.
- Do not publish a final report to Notion until the evaluation and report have passed validation.

## Required Inputs

Before starting the evaluation, confirm that the available inputs include:

1. Exactly two identifiable job descriptions.
2. At least one candidate profile.
3. Readable content for every file being evaluated.
4. A clear distinction between Job A and Job B.
5. A reliable way to identify each candidate across the evaluation and final report.

If the two roles cannot be identified reliably, stop and ask the user for clarification instead of guessing.

If one or more candidate files are unreadable, incomplete, duplicated, or unsupported, record the issue and exclude those files from scoring until they can be reviewed.

## Expected Outcome

A completed execution must produce:

- A structured interpretation of Job A.
- A structured interpretation of Job B.
- An evaluation of every valid candidate against both jobs.
- One final overall classification for every evaluated candidate: Job A, Job B, Both, or Neither.
- A prioritized recruiter contact queue.
- Evidence-based reasons supporting every contact recommendation.
- Candidate strengths, relevant gaps, risks, and uncertainties.
- Follow-up questions for important information that could not be verified.
- A clear separation between confirmed deficiencies and missing information.
- Validation notes describing excluded, duplicated, unreadable, or incomplete files.
- A recruiter-friendly report containing the complete evaluated candidate population.
- A human-review disclaimer explaining that scores and rankings are decision-support indicators.
- A Notion page only when publishing is requested, validation has passed, and an authenticated Notion MCP connection is available.

## Workflow

### Phase 1: Inventory and Validate Inputs

Before interpreting either role or evaluating any candidate:

1. Create an inventory of every supplied file.
2. Record each file's name, type, readable status, and probable purpose.
3. Identify exactly two files as job descriptions.
4. Label the two roles consistently as Job A and Job B.
5. Identify the remaining valid files as candidate profiles.
6. Detect unreadable, unsupported, empty, incomplete, or duplicated files.
7. Assign a stable candidate identifier using the candidate's name when available and the source filename as a fallback.
8. Record all excluded files and the reason for exclusion.
9. Confirm that the number of valid candidate profiles matches the number that will be evaluated.

Do not begin scoring or classification during this phase.

Stop and ask the user for clarification when:

- Fewer or more than two job descriptions are present and their intended roles cannot be determined reliably.
- No readable candidate profiles are available.
- Job A and Job B cannot be distinguished clearly.
- Multiple files appear to represent the same candidate and the duplication cannot be resolved safely.

The phase is complete only when there is a validated input manifest containing:

- Job A source file.
- Job B source file.
- Every valid candidate profile.
- Every excluded file.
- The exclusion reason for each excluded file.
- The final number of candidates approved for evaluation.

### Phase 2: Interpret and Structure Both Jobs

Read Job A and Job B completely before evaluating any candidate.

For each job, create a structured role profile containing:

1. Job title and role purpose.
2. Core responsibilities.
3. Mandatory skills and experience.
4. Preferred skills and experience.
5. Required seniority or minimum years of experience, when explicitly stated.
6. Relevant technologies, platforms, tools, modules, and methodologies.
7. Required functional, business, or industry knowledge.
8. Education or certification requirements.
9. Language requirements.
10. Location, time-zone, travel, remote-work, or work-authorization constraints.
11. Compensation information, when provided.
12. Any additional conditions that could affect candidate suitability.

Classify each extracted criterion as one of the following:

- Mandatory: explicitly required or essential for performing the role.
- Preferred: valuable but not required.
- Constraint: a condition that may prevent or limit placement, such as location, availability, language, or work authorization.
- Context: information that helps explain the role but should not independently determine candidate fit.

Preserve the meaning of the original job description and do not convert preferred qualifications into mandatory requirements.

When a requirement is unclear:

- Record it as ambiguous.
- Preserve the relevant wording from the job description.
- Do not invent a threshold, technology, seniority level, or business condition.
- Add a clarification note for human review when the ambiguity could materially affect candidate ranking.

After both role profiles are complete:

1. Compare Job A and Job B.
2. Identify shared requirements.
3. Identify requirements unique to each role.
4. Identify possible trade-offs between technical fit, functional fit, seniority, and logistical constraints.
5. Keep the two role profiles separate throughout the candidate evaluation.

This phase is complete only when Job A and Job B each have a structured and reviewable role profile.

### Phase 3: Evaluate Every Candidate Against Both Jobs

Evaluate each valid candidate separately against Job A and Job B.

Complete the full evaluation for one candidate before assigning that candidate's final classification.

For each candidate and each job:

1. Review the complete candidate profile.
2. Compare the candidate with every mandatory requirement.
3. Compare the candidate with every preferred requirement.
4. Review relevant logistical and employment constraints.
5. Identify transferable experience when the profile provides sufficient evidence.
6. Record strengths that directly support suitability for the role.
7. Record relevant gaps or mismatches.
8. Record important information that is missing or cannot be verified.
9. Record contradictions, outdated information, or unclear statements.
10. Prepare follow-up questions for information that could materially change the recommendation.

For every evaluated criterion, use one of these evidence states:

- Confirmed: the candidate profile provides clear supporting evidence.
- Partial: the profile provides related evidence, but does not fully satisfy or confirm the criterion.
- Not demonstrated: the profile was reviewed, but the required evidence was not found.
- Contradicted: the profile contains information that conflicts with the criterion.
- Unknown: the available profile does not contain enough information to assess the criterion reliably.

Do not treat `Not demonstrated` or `Unknown` as proof that the candidate lacks a skill or qualification.

For every important finding, retain:

- The evaluated job.
- The relevant requirement.
- The evidence state.
- A concise evidence summary.
- The source filename.
- A page, section, or location reference when available.
- Any required human-review note.

Apply the same evaluation method consistently to every candidate.

Do not:

- Skip evaluation against one job because the candidate appears better suited to the other.
- Infer expertise from a job title alone.
- Infer years of experience without sufficient dates or explicit statements.
- Treat exposure to a technology as equivalent to demonstrated proficiency.
- Penalize a candidate because optional information is absent.
- Use sensitive personal information as positive or negative evidence.

This phase is complete only when every valid candidate has a separate, evidence-based evaluation for Job A and Job B.

### Phase 4: Assign the Final Candidate Classification

After completing the candidate's separate evaluations for Job A and Job B, assign exactly one final overall classification.

Use the following categories:

- Job A: the candidate demonstrates a materially stronger and sufficiently supported fit for Job A than for Job B.
- Job B: the candidate demonstrates a materially stronger and sufficiently supported fit for Job B than for Job A.
- Both: the candidate demonstrates sufficiently supported suitability for both jobs.
- Neither: the available evidence does not support prioritizing the candidate for either job.

Apply these classification rules:

1. Review the complete Job A and Job B evaluations together.
2. Consider mandatory requirements before preferred requirements.
3. Consider confirmed constraints that may prevent placement.
4. Distinguish missing information from confirmed mismatches.
5. Do not assign `Neither` only because optional information is absent.
6. Do not assign `Both` only because the candidate mentions technologies shared by both jobs.
7. Do not force a candidate into Job A or Job B when neither evaluation contains sufficient evidence.
8. Record the primary reason for the selected classification.
9. Record the strongest evidence supporting the classification.
10. Record any uncertainty that could change the classification after human review.

When the candidate appears suitable for both jobs:

- Assign `Both` as the overall category.
- Identify the preferred primary role.
- Explain why that role is the stronger first-contact option.
- Preserve the second role as a supported alternative.

When the evidence is too incomplete to make a reliable distinction:

- Use the most cautious classification supported by the available evidence.
- Add a human-review note.
- Add follow-up questions that could resolve the uncertainty.
- Do not invent a tie-breaker.

Every candidate must appear in exactly one overall category, even when the classification includes a preferred primary role and an alternative role.

This phase is complete only when every evaluated candidate has:

- One final overall classification.
- A concise classification rationale.
- Supporting evidence.
- Relevant uncertainty or human-review notes.
- A preferred primary role when classified as `Both`.

### Phase 5: Prioritize Recruiter Contact

After every candidate has a final classification, create a recruiter contact priority across the complete evaluated population.

Assign each candidate to exactly one outreach priority:

- Contact Now: strong, well-supported fit for at least one job with no confirmed blocking constraint.
- Review Next: potentially suitable candidate whose recommendation depends on important missing, partial, or ambiguous information.
- Keep in Reserve: relevant candidate who is currently less competitive than the higher-priority group but may be useful as an alternative.
- Do Not Prioritize: candidate whose available evidence does not support recruiter outreach for either job at this time.

Determine priority using:

1. Evidence supporting mandatory requirements.
2. Relevant preferred qualifications.
3. Role-specific experience.
4. Confirmed logistical or employment constraints.
5. Strength and clarity of the available evidence.
6. Material gaps or contradictions.
7. The amount of uncertainty that remains.
8. Whether a focused follow-up question could materially improve confidence.
9. The candidate's relative fit compared with other candidates for the same role.

Apply these rules:

- Prioritize job-related evidence over keyword frequency.
- Do not place a candidate in `Contact Now` when a confirmed blocking constraint prevents placement.
- Do not automatically place a candidate in `Do Not Prioritize` because important information is missing.
- Use `Review Next` when missing information could reasonably change the recommendation.
- Use `Keep in Reserve` for supported candidates who are less competitive than the current contact group.
- Compare candidates only after each individual evaluation and classification has been completed.
- Do not create false precision when candidates have similar evidence.
- Preserve ties when the available evidence does not support a reliable distinction.
- Explain every `Contact Now` recommendation with concise, profile-based evidence.
- Record the main reason for every lower-priority placement.

For candidates classified as `Both`:

- Use the preferred primary role when ordering the first-contact queue.
- Preserve the alternative role in the report.
- Explain whether the second role increases the candidate's overall outreach value.

The recruiter contact queue must include:

- Priority position or tier.
- Candidate identifier.
- Final classification.
- Preferred role.
- Concise contact rationale.
- Strongest supporting evidence.
- Relevant gaps or uncertainties.
- Confirmed constraints.
- Recommended follow-up question.
- Human-review note when needed.

This phase is complete only when every evaluated candidate appears exactly once in the recruiter contact priority.
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

Create a validated manifest containing exactly two identifiable job descriptions, every valid candidate profile, and all excluded files with their exclusion reasons.

Before executing this phase, read and follow `references/input-validation.md`.

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

### Phase 6: Validate the Complete Evaluation

Validate the complete evaluation before generating or publishing the final report.

Perform the following checks:

1. Confirm that every valid candidate from the input manifest was evaluated against Job A.
2. Confirm that every valid candidate from the input manifest was evaluated against Job B.
3. Confirm that every evaluated candidate has exactly one final overall classification.
4. Confirm that every evaluated candidate appears exactly once in the recruiter contact priority.
5. Confirm that all excluded files are documented with a clear exclusion reason.
6. Confirm that no duplicated candidate record has been counted more than once.
7. Confirm that every `Contact Now` recommendation contains supporting evidence.
8. Confirm that every classification rationale is consistent with the underlying Job A and Job B evaluations.
9. Confirm that missing information is not presented as a confirmed deficiency.
10. Confirm that no unsupported candidate fact, skill, experience, qualification, constraint, or preference has been invented.
11. Confirm that no sensitive or protected personal characteristic influenced scoring, classification, or prioritization.
12. Confirm that confirmed blocking constraints are visible in the candidate recommendation.
13. Confirm that candidates classified as `Both` include a preferred primary role.
14. Confirm that every important uncertainty includes a human-review note or follow-up question.
15. Confirm that the final totals reconcile with the validated input manifest.

Check the following totals:

- Number of valid candidate profiles.
- Number of excluded files.
- Number classified as Job A.
- Number classified as Job B.
- Number classified as Both.
- Number classified as Neither.
- Number assigned to Contact Now.
- Number assigned to Review Next.
- Number assigned to Keep in Reserve.
- Number assigned to Do Not Prioritize.

The classification totals must equal the number of valid evaluated candidates.

The outreach-priority totals must also equal the number of valid evaluated candidates.

If validation fails:

1. Record every failed check.
2. Return to the relevant workflow phase.
3. Correct the affected evaluation, classification, or priority.
4. Run the complete validation again.
5. Do not generate or publish the final report until all critical checks pass.

Validation is complete only when:

- Every candidate is fully accounted for.
- All totals reconcile.
- All critical checks pass.
- Remaining limitations are explicitly documented for human review.

### Phase 7: Generate the Recruiter Report

Generate the final recruiter report only after the complete evaluation has passed validation.

Organize the report in the following order:

#### 1. Report Context

Include:

- Report title.
- Generation date.
- Job A title.
- Job B title.
- Number of valid candidates evaluated.
- Number of excluded files.
- A statement that the report supports human review and does not make final hiring decisions.

#### 2. Executive Summary

Summarize:

- The most important findings.
- The number of candidates classified as Job A.
- The number classified as Job B.
- The number classified as Both.
- The number classified as Neither.
- The number assigned to each outreach-priority tier.
- The main strengths observed across the candidate population.
- The most common gaps, uncertainties, or constraints.
- The recommended immediate recruiter action.

#### 3. Priority Contact Queue

Present the candidates in recruiter-contact order.

For each candidate include:

- Priority position or tier.
- Candidate identifier.
- Final classification.
- Preferred primary role.
- Alternative role when applicable.
- Concise contact recommendation.
- Strongest supporting evidence.
- Relevant gaps or uncertainties.
- Confirmed constraints.
- Recommended follow-up question.
- Human-review note when required.

Place `Contact Now` candidates first, followed by:

1. Review Next.
2. Keep in Reserve.
3. Do Not Prioritize.

Preserve ties when the available evidence does not support a reliable ordering.

#### 4. Recommended Candidates for Job A

Include candidates classified as `Job A` and candidates classified as `Both` whose preferred primary role is Job A.

For each candidate explain:

- Why the candidate fits Job A.
- The strongest supporting evidence.
- Important gaps or uncertainties.
- Confirmed constraints.
- The recommended recruiter action.

#### 5. Recommended Candidates for Job B

Include candidates classified as `Job B` and candidates classified as `Both` whose preferred primary role is Job B.

Use the same evidence and review structure applied to Job A.

#### 6. Candidates Suitable for Both Jobs

For every candidate classified as `Both`, include:

- Preferred primary role.
- Supported alternative role.
- Reason the candidate is suitable for both.
- Reason one role should be considered first.
- Relevant trade-offs.
- Follow-up questions that may influence final placement.

#### 7. Candidates Requiring Additional Review

Highlight candidates whose recommendation depends on:

- Missing information.
- Partial evidence.
- Ambiguous experience.
- Contradictory statements.
- Unclear seniority.
- Unverified language proficiency.
- Location, work-authorization, availability, or compensation questions.
- Other material uncertainties.

Do not present uncertain information as confirmed.

#### 8. Complete Candidate Matrix

Include every valid evaluated candidate exactly once.

The matrix must contain:

- Candidate identifier.
- Job A evaluation result.
- Job B evaluation result.
- Final classification.
- Preferred role.
- Outreach priority.
- Key supporting evidence.
- Main gap or uncertainty.
- Confirmed constraint.
- Follow-up question.

#### 9. Excluded Files

List every excluded file with:

- Source filename.
- Probable file purpose.
- Exclusion reason.
- Recommended corrective action when applicable.

Do not silently omit unreadable, unsupported, empty, incomplete, or duplicated files.

#### 10. Methodology and Limitations

Explain:

- How the two jobs were interpreted.
- How candidates were evaluated against both roles.
- How evidence states were used.
- How classifications were assigned.
- How outreach priority was determined.
- How missing information was handled.
- Which limitations remain.
- Why human review is required before recruiter action.

Apply these report-quality rules:

- Use concise and recruiter-friendly language.
- Lead with actionable recommendations.
- Keep evidence separate from interpretation.
- Do not expose unnecessary sensitive personal information.
- Do not include unsupported statements.
- Do not hide important gaps, constraints, or uncertainties.
- Keep terminology consistent throughout the report.
- Ensure all report totals match the validated evaluation totals.

This phase is complete only when the report is complete, internally consistent, evidence-based, and ready for human review.

### Phase 8: Publish the Validated Report to Notion

Publish the recruiter report to Notion only when:

- The user explicitly requests publication.
- The complete evaluation has passed validation.
- The recruiter report has passed human review or the user has approved publication.
- An authenticated Notion MCP connection is available.
- The destination page or workspace location can be identified safely.

Before publishing:

1. Confirm that the report totals match the validated evaluation totals.
2. Confirm that every evaluated candidate appears exactly once in the complete candidate matrix.
3. Confirm that excluded files and remaining limitations are documented.
4. Confirm that no unsupported or unnecessary sensitive personal information is included.
5. Confirm the intended Notion destination with the user when it is not already clear.
6. Check whether a report for the same evaluation already exists to avoid accidental duplication.

Create or update a Notion page containing:

1. Report context.
2. Executive summary.
3. Priority contact queue.
4. Recommended candidates for Job A.
5. Recommended candidates for Job B.
6. Candidates suitable for both jobs.
7. Candidates requiring additional review.
8. Complete candidate matrix.
9. Excluded files.
10. Methodology and limitations.
11. Human-review disclaimer.

Apply the following publishing rules:

- Preserve the validated report structure and terminology.
- Use headings, lists, tables, and callouts when supported by the available Notion MCP tools.
- Keep the priority contact queue near the beginning of the page.
- Make blocking constraints and important uncertainties visible.
- Do not publish local file paths, credentials, access tokens, or private configuration values.
- Do not expose information that is unnecessary for recruiter decision support.
- Do not silently omit content because of page-size or tool limitations.
- If the report is too large for one operation, publish it in ordered sections and verify each section.
- Prefer updating the intended report page over creating unintended duplicate pages.
- Do not claim successful publication until the Notion operation has been confirmed.

After publishing:

1. Verify that the page exists and is accessible through the authenticated Notion connection.
2. Confirm that all required report sections were published.
3. Confirm that tables and structured content remain readable.
4. Record the page title.
5. Record the page URL or returned Notion reference.
6. Report any formatting differences, omitted content, or tool limitations to the user.

If the Notion MCP connection is unavailable or authentication fails:

1. Do not discard or regenerate the validated report unnecessarily.
2. Preserve the report in its completed local or conversational form.
3. Explain the connection problem clearly.
4. Provide the exact next action required to reconnect or authenticate Notion.
5. Retry publication only after the connection is available.
6. Do not report the task as published until Notion confirms success.

If publication partially succeeds:

1. Identify which sections were created successfully.
2. Identify which sections failed.
3. Avoid duplicating completed sections during the retry.
4. Complete the missing sections.
5. Recheck the entire published page before confirming success.

This phase is complete only when:

- The validated report has been published completely.
- The Notion page has been verified.
- The page title and reference have been recorded.
- Any publishing limitations have been disclosed.
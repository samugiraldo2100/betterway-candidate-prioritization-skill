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

## Activation Scope

Use this skill when the user:

- Provides exactly two job descriptions and one or more candidate profiles.
- Asks to evaluate candidates against both roles.
- Wants candidates classified as Job A, Job B, Both, or Neither.
- Requests a prioritized recruiter contact queue.
- Wants evidence-based candidate strengths, gaps, uncertainties, and follow-up questions.
- Requests a complete candidate-prioritization report.
- Requests publication of an approved report through Notion MCP.

Do not use this skill when the user:

- Wants general resume writing, editing, or formatting.
- Provides only one job description.
- Requests evaluation of a single candidate without comparing the candidate against two roles.
- Requests a final hiring decision without human review.
- Wants candidates ranked using protected or sensitive personal characteristics.
- Requests general Notion page creation unrelated to candidate prioritization.

If the request is potentially relevant but the required inputs are incomplete, explain what is missing and wait for clarification instead of starting an unsupported evaluation.

## Activation Examples

Examples that should activate this skill:

- "Compare these candidate profiles against Job A and Job B and tell me who to contact first."
- "Classify every candidate as Job A, Job B, Both, or Neither."
- "Review these resumes against both Oracle roles and create a prioritized recruiter queue."
- "Evaluate all candidates, explain their strengths and gaps, and prepare a recruiting report."
- "Use the completed candidate evaluation to publish the approved report in Notion."

Examples that should not activate this skill:

- "Improve the wording of my resume."
- "Create a general Notion project page."
- "Evaluate this candidate for one position only."
- "Write a job description for a software developer."
- "Choose who should be hired based on age, gender, nationality, or another protected characteristic."

## General Error Handling

When any workflow phase fails:

1. Stop before advancing to the next phase.
2. Preserve all previously completed and validated work.
3. Record the phase, failed operation, affected files or candidates, and available error details.
4. Determine whether the failure is caused by missing inputs, unreadable files, unsupported formats, inconsistent data, failed validation, or an unavailable external tool.
5. Follow the recovery instructions in the relevant reference file.
6. Ask the user for clarification only when the missing information cannot be resolved safely from the supplied files.
7. Retry only the failed phase when possible instead of restarting the complete workflow.
8. Re-run every validation check affected by the correction.
9. Do not report the workflow as complete until the failed operation has succeeded or the limitation has been disclosed clearly.

Never:

- Hide or silently ignore an error.
- Discard valid completed work unnecessarily.
- Duplicate candidate evaluations or published report sections during a retry.
- Weaken validation rules to force successful completion.
- Expose credentials, access tokens, private configuration values, or unnecessary sensitive information in an error message.

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

For local file handling and privacy-safe input preparation, follow `references/local-input-processing.md`.

For local text extraction from input files, follow `references/local-text-extraction.md`.

## Evaluation Framework

Use the evaluation framework references when scoring and classifying candidates.

Before assigning role-fit scores, read and follow `references/evaluation-rubric.md`.

Before assigning final classifications or outreach priorities, read and follow `references/scoring-rules.md`.

The rubric and scoring rules support structured comparison, but they do not replace evidence review or human judgment.

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

Convert Job A and Job B into separate role profiles containing mandatory requirements, preferred qualifications, constraints, contextual information, and documented ambiguities.

Before executing this phase, read and follow `references/job-interpretation.md`.

### Phase 3: Evaluate Every Candidate Against Both Jobs

Evaluate every valid candidate separately against Job A and Job B using consistent evidence states, source references, gaps, uncertainties, and follow-up questions.

Before executing this phase, read and follow `references/candidate-evaluation.md`.

### Phase 4: Assign the Final Candidate Classification

Assign every evaluated candidate exactly one final category: Job A, Job B, Both, or Neither, supported by the completed evaluations for both roles.

Before executing this phase, read and follow `references/final-classification.md`.

### Phase 5: Prioritize Recruiter Contact

Place every evaluated candidate into exactly one evidence-based outreach tier and create the recruiter contact queue.

Before executing this phase, read and follow `references/contact-prioritization.md`.

### Phase 6: Validate the Complete Evaluation

Validate candidate coverage, classifications, priorities, evidence, exclusions, responsible-screening safeguards, and reconciled totals before report generation.

Before executing this phase, read and follow `references/evaluation-validation.md`.

### Phase 7: Generate the Recruiter Report

Generate a complete, recruiter-friendly report containing actionable recommendations, evidence, uncertainties, the complete candidate matrix, exclusions, methodology, and limitations.

Before executing this phase, read and follow `references/report-specification.md`.

### Phase 8: Publish the Validated Report to Notion

Publish the approved and validated recruiter report only through an authenticated Notion MCP connection, then verify the completed page and record its reference.

Before executing this phase, read and follow `references/notion-publishing.md`.

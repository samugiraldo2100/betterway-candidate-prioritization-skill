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
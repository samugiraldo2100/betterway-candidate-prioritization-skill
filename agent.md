# Candidate Prioritization Agent

## Purpose

This file is the reviewer-facing agent entrypoint for the BetterWay Candidate Prioritization Skill.

The main skill implementation is located at:

candidate-prioritization/SKILL.md

Use this agent to evaluate candidate profiles against two job descriptions and produce a structured recruiter-facing prioritization report.

## Main Skill

Read and follow:

candidate-prioritization/SKILL.md

The skill uses progressive-disclosure references from:

candidate-prioritization/references/

## Required Local Inputs

Private local input files should be placed in:

data/input/jobs/
data/input/candidates/

Expected structure:

data/input/
  jobs/
    job-a.pdf
    job-b.pdf
  candidates/
    candidate-001.pdf
    candidate-002.pdf
    candidate-003.pdf

Private candidate files and job files must remain local and must not be committed to Git.

## Local Processing Workflow

Run the workflow from the repository root.

### 1. Inventory local files

Command:

py candidate-prioritization/scripts/inventory_input_files.py

Expected purpose:

- Detect job files.
- Detect candidate files.
- Report unsupported files.
- Write inventory output to the ignored outputs/ folder.

### 2. Extract readable text

Command:

py candidate-prioritization/scripts/extract_input_text.py

Optional PDF support:

py -m pip install pypdf

Optional DOCX support:

py -m pip install python-docx

### 3. Build evaluation workspace

Command:

py candidate-prioritization/scripts/build_evaluation_workspace.py

Expected workspace:

outputs/evaluation-workspace/
  jobs/
  candidates/
  evaluation-matrix.json

## Evaluation Instructions

Evaluate every candidate against both Job A and Job B.

Use these references:

candidate-prioritization/references/evaluation-rubric.md
candidate-prioritization/references/scoring-rules.md
candidate-prioritization/references/evaluation-execution.md
candidate-prioritization/references/report-specification.md

For each candidate, produce:

- Job A score.
- Job B score.
- Final classification: Job A, Job B, Both, or Neither.
- Outreach priority: Contact Now, Review Next, Keep in Reserve, or Do Not Prioritize.
- Evidence-based reasoning.
- Main gaps or uncertainties.
- Follow-up questions.
- Human-review notes when needed.

## Report Output

Use this template:

reports/templates/candidate-prioritization-report.md

Generated reports should be saved locally in:

reports/generated/

Generated reports must not be committed to Git unless explicitly requested and privacy-reviewed.

## Responsible Screening Rules

Use only job-related evidence.

Do not rank, classify, prioritize, or reject candidates using protected or sensitive personal characteristics.

Do not invent missing information.

If information is missing, mark it as unknown and add a follow-up question.

## Validation

Before final submission, run:

py candidate-prioritization/scripts/validate_project.py

Expected result:

Project validation passed.

Also verify:

git status --short

Private files and generated outputs should not appear.

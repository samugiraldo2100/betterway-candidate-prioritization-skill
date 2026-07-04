# BetterWay Candidate Prioritization Skill

## Overview

This repository contains a Claude Skill designed to support candidate prioritization for two job openings.

The skill helps evaluate candidate profiles against two job descriptions, classify candidates by role fit, prioritize recruiter outreach, and produce a structured recruiter-facing report.

The project follows a privacy-safe workflow: candidate files, job description PDFs, extracted text, generated inventories, and generated reports are kept local and ignored by Git.

## Purpose

The main goal of this project is to help recruiters answer:

- Which candidates fit Job A?
- Which candidates fit Job B?
- Which candidates could fit both roles?
- Which candidates should not be prioritized for the current openings?
- Who should be contacted first?
- What evidence supports each recommendation?
- What information is missing and should be confirmed by a human reviewer?

## Skill Location

The main skill folder is:

```text
candidate-prioritization/
```

The main skill instruction file is:

```text
candidate-prioritization/SKILL.md
```

## What the Skill Does

The skill provides a structured workflow to:

1. Validate input files.
2. Interpret Job A and Job B requirements.
3. Evaluate each candidate against both jobs.
4. Apply a weighted evaluation rubric.
5. Assign Job A, Job B, Both, or Neither classification.
6. Assign recruiter outreach priority.
7. Generate a recruiter-facing report.
8. Optionally publish results to Notion when a Notion MCP connection is available.
9. Validate the project structure before submission.

## What the Skill Does Not Do

The skill does not:

- Make hiring decisions automatically.
- Replace recruiter or human review.
- Use protected or sensitive personal characteristics for ranking.
- Commit private candidate files to Git.
- Commit generated outputs to Git.
- Guarantee perfect PDF extraction for every file.
- Publish to Notion unless the user has a valid authenticated Notion MCP connection.

## Repository Structure

```text
candidate-prioritization/
  SKILL.md
  references/
  scripts/

data/
  input/

outputs/

reports/
  generated/
  templates/

tests/
```

## Important Files

| File | Purpose |
|---|---|
| `candidate-prioritization/SKILL.md` | Main Claude Skill instruction file. |
| `candidate-prioritization/references/evaluation-rubric.md` | Weighted candidate evaluation rubric. |
| `candidate-prioritization/references/scoring-rules.md` | Score bands, classification rules, and outreach priority rules. |
| `candidate-prioritization/references/report-specification.md` | Recruiter report requirements. |
| `reports/templates/candidate-prioritization-report.md` | Markdown template for the final recruiter report. |
| `candidate-prioritization/scripts/validate_project.py` | Final repository-level validation script. |

## Local Data Safety

Private and generated files should stay local.

Do not commit:

- Candidate resumes.
- Candidate profiles.
- Job description PDFs.
- ZIP packages.
- Extracted text.
- Generated inventories.
- Generated reports.
- `.env` files.
- IDE metadata.

The `.gitignore` protects local and generated folders such as:

```text
data/input/
outputs/
reports/generated/
```

## Local Workflow

### 1. Place local files

Place private local input files in:

```text
data/input/
```

Recommended structure:

```text
data/input/
  jobs/
    job-a.pdf
    job-b.pdf
  candidates/
    candidate-001.pdf
    candidate-002.pdf
```

### 2. Inventory input files

```bash
py candidate-prioritization/scripts/inventory_input_files.py
```

Generated output:

```text
outputs/input-inventory.json
```

### 3. Extract readable text

```bash
py candidate-prioritization/scripts/extract_input_text.py
```

Generated outputs:

```text
outputs/extracted-text/
outputs/extracted-text-manifest.json
```

Optional dependencies:

```bash
py -m pip install pypdf
py -m pip install python-docx
```

### 4. Build evaluation workspace

```bash
py candidate-prioritization/scripts/build_evaluation_workspace.py
```

Generated outputs:

```text
outputs/evaluation-workspace/
outputs/evaluation-workspace-manifest.json
```

### 5. Evaluate candidates

Use these references:

```text
candidate-prioritization/references/evaluation-rubric.md
candidate-prioritization/references/scoring-rules.md
candidate-prioritization/references/evaluation-execution.md
```

### 6. Prepare recruiter report

Use the report template:

```text
reports/templates/candidate-prioritization-report.md
```

Generated reports should be saved in:

```text
reports/generated/
```

## Validation Commands

Run these commands before creating a final Pull Request or submitting the project.

### Validate skill references

```bash
py candidate-prioritization/scripts/validate_skill_references.py
```

Expected result:

```text
Skill reference validation passed.
```

### Validate evaluation framework

```bash
py candidate-prioritization/scripts/validate_evaluation_framework.py
```

Expected result:

```text
Evaluation framework validation passed.
```

### Validate entire project

```bash
py candidate-prioritization/scripts/validate_project.py
```

Expected result:

```text
Project validation passed.
```

## Final Git Safety Check

Before every commit, run:

```bash
git status --short
```

Only safe repository files should appear.

Private files and generated outputs should not appear.

## Branching and Traceability

This project follows a GitHub Flow style:

- `main` remains stable.
- Each major phase is developed in a separate branch.
- Each branch is merged through a Pull Request.
- Merge commits are preserved for traceability.
- Historical branches are kept instead of deleted.

Implemented phases include:

- Repository foundation.
- Skill core.
- Evaluation framework.
- Local input processing.
- Local text extraction.
- Evaluation execution workspace.
- Recruiter report template.
- Final project validation.
- Final submission documentation.

## Responsible Screening

Candidate evaluation must use only job-related evidence.

Do not score, rank, classify, reject, or prioritize candidates based on protected or sensitive personal characteristics.

Missing information should be marked as unknown and handled with follow-up questions, not assumptions.

## License

This project uses the MIT License.

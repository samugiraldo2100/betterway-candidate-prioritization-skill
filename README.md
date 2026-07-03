# BetterWay Candidate Prioritization Skill

A reusable agent skill for evaluating, classifying, and prioritizing candidate profiles against two job descriptions.

The project is being developed as part of the BetterWay Devs agentic candidate prioritization challenge. Its goal is to help recruiters identify which candidates should be contacted first while preserving transparent reasoning, evidence-based recommendations, and human review.

## Project Status

This repository is currently under active development.

The initial repository structure and version-control workflow have been established. Candidate evaluation, report generation, validation, and Notion MCP publishing will be implemented in subsequent stages.

## Objectives

The skill will:

- Receive two job descriptions and a collection of candidate profiles.
- Extract and organize the relevant requirements for each position.
- Evaluate every candidate using explicit and reusable criteria.
- Classify each candidate for Job A, Job B, both jobs, or neither job.
- Produce a prioritized recruiter contact queue.
- Explain strengths, gaps, risks, and follow-up questions using profile evidence.
- Generate a structured recruitment report.
- Publish the final report to Notion through the official Notion MCP integration.
- Remain reusable with candidate files and job descriptions beyond the provided sample package.

## Planned Workflow

1. Validate the supplied files and identify job descriptions and candidate profiles.
2. Convert each job description into structured evaluation criteria.
3. Review every candidate against both positions.
4. Assign classifications, scores, evidence, gaps, and follow-up questions.
5. Prioritize the candidates the recruiter should contact first.
6. Validate completeness, consistency, and responsible-screening rules.
7. Generate a recruiter-friendly report.
8. Publish the approved report to Notion through MCP.

## Repository Structure

```text
betterway-candidate-prioritization-skill/
├── candidate-prioritization/
│   ├── assets/
│   ├── references/
│   └── scripts/
├── data/
│   └── input/
├── examples/
├── outputs/
├── reports/
│   └── generated/
├── tests/
├── .gitignore
├── LICENSE
└── README.md
```

## Main Directories

- `candidate-prioritization/`: contains the reusable agent skill and its supporting resources.
- `candidate-prioritization/scripts/`: contains deterministic validation and processing utilities.
- `candidate-prioritization/references/`: contains evaluation rules, report specifications, and supporting guidance.
- `candidate-prioritization/assets/`: contains reusable templates used by the skill.
- `data/input/`: local working directory for job descriptions and candidate profiles.
- `examples/`: contains example inputs or outputs that are safe to share.
- `outputs/`: contains locally generated intermediate results.
- `reports/generated/`: contains locally generated recruitment reports.
- `tests/`: contains trigger, functional, and acceptance validation cases.

## Data Handling

The provided candidate sample package is used only as local test data and is not committed to the public repository.

Generated outputs and local candidate files are excluded from version control to reduce the risk of unintentionally publishing personal or test-profile information.

## Responsible Screening

The skill is intended to support recruiter review, not replace human judgment.

Candidate recommendations must:

- Be based on job-related evidence.
- Distinguish missing information from confirmed deficiencies.
- Avoid using protected or sensitive personal characteristics as evaluation criteria.
- Present scores as decision-support indicators rather than final hiring decisions.
- Include follow-up questions when important information cannot be verified.

## Version-Control Workflow

This project follows GitHub Flow:

1. Keep `main` stable.
2. Create a descriptive branch for each logical phase or feature.
3. Record each meaningful change in a focused commit.
4. Review the completed branch through a Pull Request.
5. Merge the approved work into `main`.
6. Remove the completed temporary branch.

## License

This project is distributed under the MIT License. See `LICENSE` for details.
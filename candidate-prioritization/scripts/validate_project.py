"""Validate the overall candidate prioritization project structure.

This script performs safe repository-level checks.

It verifies:
- Required project files exist.
- Required skill references exist.
- Required scripts exist.
- The recruiter report template exists.
- Git ignore rules protect private and generated files.
- Existing validation scripts pass.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


REQUIRED_FILES = [
    "README.md",
    ".gitignore",
    "candidate-prioritization/SKILL.md",
    "reports/templates/candidate-prioritization-report.md",
]

REQUIRED_REFERENCES = [
    "candidate-prioritization/references/input-validation.md",
    "candidate-prioritization/references/job-interpretation.md",
    "candidate-prioritization/references/candidate-evaluation.md",
    "candidate-prioritization/references/final-classification.md",
    "candidate-prioritization/references/contact-prioritization.md",
    "candidate-prioritization/references/evaluation-validation.md",
    "candidate-prioritization/references/report-specification.md",
    "candidate-prioritization/references/notion-publishing.md",
    "candidate-prioritization/references/evaluation-rubric.md",
    "candidate-prioritization/references/scoring-rules.md",
    "candidate-prioritization/references/local-input-processing.md",
    "candidate-prioritization/references/local-text-extraction.md",
    "candidate-prioritization/references/evaluation-execution.md",
]

REQUIRED_SCRIPTS = [
    "candidate-prioritization/scripts/validate_skill_references.py",
    "candidate-prioritization/scripts/validate_evaluation_framework.py",
    "candidate-prioritization/scripts/inventory_input_files.py",
    "candidate-prioritization/scripts/extract_input_text.py",
    "candidate-prioritization/scripts/build_evaluation_workspace.py",
]

REQUIRED_GITIGNORE_PATTERNS = [
    "data/input/*",
    "outputs/*",
    "reports/generated/*",
    "sample-pack*.zip",
    ".env",
    ".idea/",
]

VALIDATION_SCRIPTS = [
    "candidate-prioritization/scripts/validate_skill_references.py",
    "candidate-prioritization/scripts/validate_evaluation_framework.py",
]


def require_existing_paths(
    repo_root: Path,
    paths: list[str],
    label: str,
    errors: list[str],
) -> None:
    """Validate that required paths exist."""
    for relative_path in paths:
        path = repo_root / relative_path

        if not path.exists():
            errors.append(f"Missing {label}: {relative_path}")


def validate_gitignore(repo_root: Path, errors: list[str]) -> None:
    """Validate important privacy and generated-output ignore rules."""
    gitignore_path = repo_root / ".gitignore"

    if not gitignore_path.exists():
        errors.append("Missing .gitignore file.")
        return

    gitignore_content = gitignore_path.read_text(encoding="utf-8")

    for pattern in REQUIRED_GITIGNORE_PATTERNS:
        if pattern not in gitignore_content:
            errors.append(f".gitignore is missing required pattern: {pattern}")


def run_validation_script(
    repo_root: Path,
    script_path: str,
    errors: list[str],
) -> None:
    """Run one validation script using the current Python interpreter."""
    result = subprocess.run(
        [sys.executable, script_path],
        cwd=repo_root,
        text=True,
        capture_output=True,
        check=False,
    )

    if result.returncode != 0:
        errors.append(
            f"Validation script failed: {script_path}\n"
            f"STDOUT:\n{result.stdout}\n"
            f"STDERR:\n{result.stderr}"
        )
        return

    print(result.stdout.strip())


def validate_report_template(repo_root: Path, errors: list[str]) -> None:
    """Validate that the report template contains key sections."""
    template_path = repo_root / "reports/templates/candidate-prioritization-report.md"

    if not template_path.exists():
        errors.append("Missing recruiter report template.")
        return

    template_content = template_path.read_text(encoding="utf-8")

    required_sections = [
        "## Report Context",
        "## Executive Summary",
        "## Priority Contact Queue",
        "## Job A Recommendations",
        "## Job B Recommendations",
        "## Complete Candidate Matrix",
        "## Final Recommendation",
    ]

    for section in required_sections:
        if section not in template_content:
            errors.append(f"Report template is missing section: {section}")


def main() -> int:
    """Run project validation checks."""
    repo_root = Path(__file__).resolve().parents[2]
    errors: list[str] = []

    require_existing_paths(repo_root, REQUIRED_FILES, "required file", errors)
    require_existing_paths(repo_root, REQUIRED_REFERENCES, "reference file", errors)
    require_existing_paths(repo_root, REQUIRED_SCRIPTS, "script file", errors)

    validate_gitignore(repo_root, errors)
    validate_report_template(repo_root, errors)

    for script_path in VALIDATION_SCRIPTS:
        run_validation_script(repo_root, script_path, errors)

    if errors:
        print("Project validation failed:\n")

        for error in errors:
            print(f"- {error}")

        print(f"\nTotal errors: {len(errors)}")
        return 1

    print("Project validation passed.")
    print(f"Required files: {len(REQUIRED_FILES)}")
    print(f"Reference files: {len(REQUIRED_REFERENCES)}")
    print(f"Script files: {len(REQUIRED_SCRIPTS)}")
    print("Privacy and generated-output ignore rules verified.")
    print("Recruiter report template verified.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

"""Validate the candidate evaluation framework references.

This script uses only the Python standard library. It verifies that:
- evaluation-rubric.md exists.
- scoring-rules.md exists.
- The rubric contains the expected weighted criteria.
- The rubric weights sum to 100.
- The scoring rules define all final classifications.
- The scoring rules define all outreach priorities.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path


EXPECTED_CRITERIA = {
    "Mandatory role requirements": 35,
    "Role-specific technical or functional fit": 20,
    "Relevant professional experience and seniority": 15,
    "Preferred qualifications": 10,
    "Evidence quality and clarity": 10,
    "Constraints and placement feasibility": 10,
}

EXPECTED_CLASSIFICATIONS = ["Job A", "Job B", "Both", "Neither"]

EXPECTED_OUTREACH_PRIORITIES = [
    "Contact Now",
    "Review Next",
    "Keep in Reserve",
    "Do Not Prioritize",
]


def extract_weighted_criteria(markdown: str) -> dict[str, int]:
    criteria: dict[str, int] = {}

    for line in markdown.splitlines():
        match = re.match(r"^\|\s*(.+?)\s*\|\s*(\d+)\s*\|", line)

        if not match:
            continue

        criterion = match.group(1).strip()
        weight = int(match.group(2))

        if criterion in EXPECTED_CRITERIA:
            criteria[criterion] = weight

    return criteria


def require_text(content: str, expected_text: str, errors: list[str], source: str) -> None:
    if expected_text not in content:
        errors.append(f"{source} is missing required text: {expected_text}")


def main() -> int:
    skill_root = Path(__file__).resolve().parents[1]
    references_dir = skill_root / "references"
    rubric_path = references_dir / "evaluation-rubric.md"
    scoring_path = references_dir / "scoring-rules.md"

    errors: list[str] = []

    if not rubric_path.is_file():
        errors.append(f"Missing required file: {rubric_path.relative_to(skill_root)}")

    if not scoring_path.is_file():
        errors.append(f"Missing required file: {scoring_path.relative_to(skill_root)}")

    if errors:
        print("Evaluation framework validation failed:\n")
        for error in errors:
            print(f"- {error}")
        return 1

    rubric = rubric_path.read_text(encoding="utf-8")
    scoring = scoring_path.read_text(encoding="utf-8")

    weighted_criteria = extract_weighted_criteria(rubric)

    for criterion, expected_weight in EXPECTED_CRITERIA.items():
        actual_weight = weighted_criteria.get(criterion)

        if actual_weight is None:
            errors.append(f"Rubric is missing criterion: {criterion}")
        elif actual_weight != expected_weight:
            errors.append(
                f"Rubric criterion '{criterion}' has weight {actual_weight}, "
                f"expected {expected_weight}."
            )

    total_weight = sum(weighted_criteria.values())

    if total_weight != 100:
        errors.append(f"Rubric weights sum to {total_weight}, expected 100.")

    for evidence_state in [
        "Confirmed",
        "Partial",
        "Not demonstrated",
        "Contradicted",
        "Unknown",
    ]:
        require_text(rubric, evidence_state, errors, "evaluation-rubric.md")

    for classification in EXPECTED_CLASSIFICATIONS:
        require_text(scoring, f"### {classification}", errors, "scoring-rules.md")

    for priority in EXPECTED_OUTREACH_PRIORITIES:
        require_text(scoring, f"### {priority}", errors, "scoring-rules.md")

    require_text(scoring, "85-100", errors, "scoring-rules.md")
    require_text(scoring, "70-84", errors, "scoring-rules.md")
    require_text(scoring, "55-69", errors, "scoring-rules.md")
    require_text(scoring, "40-54", errors, "scoring-rules.md")
    require_text(scoring, "0-39", errors, "scoring-rules.md")

    if errors:
        print("Evaluation framework validation failed:\n")

        for error in errors:
            print(f"- {error}")

        print(f"\nTotal errors: {len(errors)}")
        return 1

    print("Evaluation framework validation passed.")
    print(f"Weighted criteria: {len(weighted_criteria)}")
    print(f"Total rubric weight: {total_weight}")
    print(f"Classifications: {len(EXPECTED_CLASSIFICATIONS)}")
    print(f"Outreach priorities: {len(EXPECTED_OUTREACH_PRIORITIES)}")

    return 0


if __name__ == "__main__":
    sys.exit(main())

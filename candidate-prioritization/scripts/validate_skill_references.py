"""Validate Markdown references declared inside SKILL.md.

This script uses only the Python standard library. It verifies that:
- SKILL.md exists.
- At least one references/*.md path is declared.
- Every declared reference exists.
- No reference is declared more than once.
- Every Markdown file in references/ is linked from SKILL.md.
"""

from __future__ import annotations

import re
import sys
from collections import Counter
from pathlib import Path


REFERENCE_PATTERN = re.compile(r"`(references/[^`]+\.md)`")


def main() -> int:
    skill_root = Path(__file__).resolve().parents[1]
    skill_file = skill_root / "SKILL.md"
    references_directory = skill_root / "references"

    errors: list[str] = []

    if not skill_file.is_file():
        print(f"ERROR: Required file not found: {skill_file}")
        return 1

    if not references_directory.is_dir():
        print(f"ERROR: References directory not found: {references_directory}")
        return 1

    content = skill_file.read_text(encoding="utf-8")
    declared_references = REFERENCE_PATTERN.findall(content)

    if not declared_references:
        errors.append("SKILL.md does not declare any references/*.md files.")

    reference_counts = Counter(declared_references)

    duplicated_references = sorted(
        reference
        for reference, count in reference_counts.items()
        if count > 1
    )

    for reference in duplicated_references:
        errors.append(
            f"Reference is declared more than once: "
            f"{reference} ({reference_counts[reference]} occurrences)"
        )

    unique_declared_references = sorted(reference_counts)

    for relative_reference in unique_declared_references:
        reference_file = skill_root / Path(relative_reference)

        if not reference_file.is_file():
            errors.append(f"Referenced file does not exist: {relative_reference}")

    existing_reference_files = sorted(
        path.relative_to(skill_root).as_posix()
        for path in references_directory.rglob("*.md")
        if path.is_file()
    )

    unlinked_reference_files = sorted(
        set(existing_reference_files) - set(unique_declared_references)
    )

    for reference in unlinked_reference_files:
        errors.append(f"Reference file is not linked from SKILL.md: {reference}")

    if errors:
        print("Skill reference validation failed:\n")

        for error in errors:
            print(f"- {error}")

        print(f"\nTotal errors: {len(errors)}")
        return 1

    print("Skill reference validation passed.")
    print(f"Declared references: {len(unique_declared_references)}")
    print(f"Existing reference files: {len(existing_reference_files)}")

    for reference in unique_declared_references:
        print(f"- OK: {reference}")

    return 0


if __name__ == "__main__":
    sys.exit(main())

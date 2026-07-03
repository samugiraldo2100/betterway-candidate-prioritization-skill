"""Inventory local input files for the candidate prioritization skill.

This script does not evaluate candidates.
It only scans a local input directory and produces a structured inventory.

Default input directory:
    data/input

Example:
    py candidate-prioritization/scripts/inventory_input_files.py

Optional:
    py candidate-prioritization/scripts/inventory_input_files.py --input-dir data/input
"""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path


SUPPORTED_EXTENSIONS = {
    ".pdf",
    ".docx",
    ".txt",
    ".md",
    ".zip",
}


def classify_input_file(file_path: Path) -> str:
    """Classify a local input file by name and extension."""
    file_name = file_path.name.lower()
    file_extension = file_path.suffix.lower()

    if file_extension == ".zip":
        return "archive"

    if (
            "job" in file_name
            or "description" in file_name
            or "role" in file_name
    ):
        return "possible_job_description"

    if file_extension in {".pdf", ".docx", ".txt", ".md"}:
        return "possible_candidate_profile"

    return "unsupported"


def build_inventory(input_directory: Path) -> dict:
    """Build a structured inventory for all valid files in the input directory."""
    inventory_files = []

    if not input_directory.exists():
        return {
            "input_dir": str(input_directory),
            "exists": False,
            "total_files": 0,
            "summary": {},
            "warnings": [
                f"Input directory does not exist: {input_directory}"
            ],
            "files": [],
        }

    for file_path in sorted(input_directory.rglob("*")):
        if not file_path.is_file():
            continue

        if file_path.name == ".gitkeep":
            continue

        file_extension = file_path.suffix.lower()
        classification = classify_input_file(file_path)

        inventory_files.append(
            {
                "relative_path": str(
                    file_path.relative_to(input_directory)
                ).replace("\\", "/"),
                "name": file_path.name,
                "extension": file_extension,
                "size_bytes": file_path.stat().st_size,
                "classification": classification,
                "supported_extension": file_extension in SUPPORTED_EXTENSIONS,
            }
        )

    classification_counts = Counter(
        file_item["classification"] for file_item in inventory_files
    )
    extension_counts = Counter(
        file_item["extension"] or "[no extension]"
        for file_item in inventory_files
    )

    warnings = []

    possible_job_count = classification_counts.get(
        "possible_job_description",
        0,
    )
    possible_candidate_count = classification_counts.get(
        "possible_candidate_profile",
        0,
    )
    unsupported_count = classification_counts.get("unsupported", 0)

    if possible_job_count != 2:
        warnings.append(
            f"Expected exactly 2 possible job descriptions, "
            f"found {possible_job_count}."
        )

    if possible_candidate_count == 0:
        warnings.append("No possible candidate profiles were found.")

    if unsupported_count:
        warnings.append(f"Found {unsupported_count} unsupported file(s).")

    return {
        "input_dir": str(input_directory),
        "exists": True,
        "total_files": len(inventory_files),
        "summary": {
            "by_classification": dict(sorted(classification_counts.items())),
            "by_extension": dict(sorted(extension_counts.items())),
        },
        "warnings": warnings,
        "files": inventory_files,
    }


def parse_arguments() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Inventory local input files for candidate prioritization."
    )

    parser.add_argument(
        "--input-dir",
        default="data/input",
        help="Local input directory to scan. Default: data/input",
    )

    parser.add_argument(
        "--output",
        default="outputs/input-inventory.json",
        help="JSON output path. Default: outputs/input-inventory.json",
    )

    return parser.parse_args()


def write_inventory_output(inventory: dict, output_path: Path) -> None:
    """Write the inventory result to a JSON file."""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(
        json.dumps(inventory, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
        )


def print_inventory_summary(inventory: dict, output_path: Path) -> None:
    """Print a readable inventory summary in the terminal."""
    print("Input inventory completed.")
    print(f"Input directory: {inventory['input_dir']}")
    print(f"Total files: {inventory['total_files']}")
    print(f"Output: {output_path}")

    if inventory["warnings"]:
        print("\nWarnings:")
        for warning in inventory["warnings"]:
            print(f"- {warning}")


def main() -> int:
    """Run the input inventory workflow."""
    args = parse_arguments()

    input_directory = Path(args.input_dir)
    output_path = Path(args.output)

    inventory = build_inventory(input_directory)

    write_inventory_output(inventory, output_path)
    print_inventory_summary(inventory, output_path)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
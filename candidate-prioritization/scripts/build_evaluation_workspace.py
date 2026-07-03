"""Build a local evaluation workspace from extracted text files.

This script prepares local evaluation artifacts for the candidate prioritization
workflow. It does not score candidates automatically.

Default input:
    outputs/extracted-text

Default output:
    outputs/evaluation-workspace

The output folder is ignored by Git.
"""

from __future__ import annotations

import argparse
import json
import shutil
from pathlib import Path


JOB_KEYWORDS = ("job", "role", "description")
CANDIDATE_KEYWORDS = ("candidate", "resume", "cv", "profile")


def classify_extracted_text(file_path: Path) -> str:
    """Classify extracted text as a possible job or candidate file."""
    file_name = file_path.name.lower()

    if any(keyword in file_name for keyword in JOB_KEYWORDS):
        return "job"

    if any(keyword in file_name for keyword in CANDIDATE_KEYWORDS):
        return "candidate"

    return "candidate"


def prepare_clean_directory(directory_path: Path) -> None:
    """Create an empty output directory."""
    if directory_path.exists():
        shutil.rmtree(directory_path)

    directory_path.mkdir(parents=True, exist_ok=True)


def copy_text_file(source_path: Path, target_directory: Path) -> Path:
    """Copy one extracted text file into the target directory."""
    target_directory.mkdir(parents=True, exist_ok=True)
    target_path = target_directory / source_path.name
    shutil.copy2(source_path, target_path)
    return target_path


def build_workspace(input_directory: Path, output_directory: Path) -> dict:
    """Build a local evaluation workspace from extracted text files."""
    jobs_directory = output_directory / "jobs"
    candidates_directory = output_directory / "candidates"

    prepare_clean_directory(output_directory)
    jobs_directory.mkdir(parents=True, exist_ok=True)
    candidates_directory.mkdir(parents=True, exist_ok=True)

    manifest = {
        "input_dir": str(input_directory),
        "output_dir": str(output_directory),
        "job_files": [],
        "candidate_files": [],
        "warnings": [],
    }

    if not input_directory.exists():
        manifest["warnings"].append(
            f"Extracted text directory does not exist: {input_directory}"
        )
        return manifest

    text_files = sorted(input_directory.rglob("*.txt"))

    if not text_files:
        manifest["warnings"].append(
            f"No extracted text files were found in: {input_directory}"
        )

    for text_file in text_files:
        classification = classify_extracted_text(text_file)

        if classification == "job":
            target_path = copy_text_file(text_file, jobs_directory)
            manifest["job_files"].append(str(target_path).replace("\\", "/"))
        else:
            target_path = copy_text_file(text_file, candidates_directory)
            manifest["candidate_files"].append(str(target_path).replace("\\", "/"))

    if len(manifest["job_files"]) != 2:
        manifest["warnings"].append(
            f"Expected exactly 2 job text files, found {len(manifest['job_files'])}."
        )

    if not manifest["candidate_files"]:
        manifest["warnings"].append("No candidate text files were prepared.")

    evaluation_matrix_path = output_directory / "evaluation-matrix.json"
    evaluation_matrix = {
        "jobs": manifest["job_files"],
        "candidates": [
            {
                "candidate_file": candidate_file,
                "job_a_score": None,
                "job_b_score": None,
                "final_classification": None,
                "outreach_priority": None,
                "main_evidence": [],
                "main_gaps_or_uncertainties": [],
                "follow_up_questions": [],
                "human_review_notes": [],
            }
            for candidate_file in manifest["candidate_files"]
        ],
    }

    evaluation_matrix_path.write_text(
        json.dumps(evaluation_matrix, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
        )

    manifest["evaluation_matrix"] = str(evaluation_matrix_path).replace("\\", "/")

    return manifest


def parse_arguments() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Build a local evaluation workspace from extracted text files."
    )

    parser.add_argument(
        "--input-dir",
        default="outputs/extracted-text",
        help="Directory containing extracted text files. Default: outputs/extracted-text",
    )

    parser.add_argument(
        "--output-dir",
        default="outputs/evaluation-workspace",
        help="Directory for local evaluation workspace. Default: outputs/evaluation-workspace",
    )

    parser.add_argument(
        "--manifest",
        default="outputs/evaluation-workspace-manifest.json",
        help="Workspace manifest path. Default: outputs/evaluation-workspace-manifest.json",
    )

    return parser.parse_args()


def write_manifest(manifest: dict, manifest_path: Path) -> None:
    """Write workspace manifest to JSON."""
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    manifest_path.write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
        )


def print_summary(manifest: dict, manifest_path: Path) -> None:
    """Print workspace summary."""
    print("Evaluation workspace completed.")
    print(f"Input directory: {manifest['input_dir']}")
    print(f"Output directory: {manifest['output_dir']}")
    print(f"Job files: {len(manifest['job_files'])}")
    print(f"Candidate files: {len(manifest['candidate_files'])}")
    print(f"Manifest: {manifest_path}")

    if manifest["warnings"]:
        print("\nWarnings:")
        for warning in manifest["warnings"]:
            print(f"- {warning}")


def main() -> int:
    """Run the evaluation workspace workflow."""
    args = parse_arguments()

    input_directory = Path(args.input_dir)
    output_directory = Path(args.output_dir)
    manifest_path = Path(args.manifest)

    manifest = build_workspace(input_directory, output_directory)

    write_manifest(manifest, manifest_path)
    print_summary(manifest, manifest_path)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
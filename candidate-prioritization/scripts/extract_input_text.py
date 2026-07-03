"""Extract readable text from local input files.

This script prepares local text outputs for the candidate prioritization workflow.

Default input directory:
    data/input

Default output directory:
    outputs/extracted-text

Supported without extra packages:
    .txt
    .md

Optional support:
    .pdf  requires pypdf
    .docx requires python-docx

The script never commits private input files. Outputs are written to the ignored
outputs/ directory.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


TEXT_EXTENSIONS = {".txt", ".md"}
OPTIONAL_EXTENSIONS = {".pdf", ".docx"}
SKIPPED_EXTENSIONS = {".zip"}


def slugify(value: str) -> str:
    """Convert a file name into a safe output name."""
    value = value.lower().strip()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    value = value.strip("-")
    return value or "file"


def read_plain_text(file_path: Path) -> str:
    """Read plain text files with UTF-8 fallback handling."""
    return file_path.read_text(encoding="utf-8", errors="replace")


def read_pdf_text(file_path: Path) -> tuple[str, str | None]:
    """Read PDF text when pypdf is installed."""
    try:
        from pypdf import PdfReader
    except ImportError:
        return "", "PDF extraction requires optional package: pypdf"

    try:
        reader = PdfReader(str(file_path))
        page_text = []

        for page in reader.pages:
            page_text.append(page.extract_text() or "")

        return "\n\n".join(page_text).strip(), None
    except Exception as error:
        return "", f"PDF extraction failed: {error}"


def read_docx_text(file_path: Path) -> tuple[str, str | None]:
    """Read DOCX text when python-docx is installed."""
    try:
        import docx
    except ImportError:
        return "", "DOCX extraction requires optional package: python-docx"

    try:
        document = docx.Document(str(file_path))
        paragraphs = [paragraph.text for paragraph in document.paragraphs]
        return "\n".join(paragraphs).strip(), None
    except Exception as error:
        return "", f"DOCX extraction failed: {error}"


def extract_text(file_path: Path) -> tuple[str, str]:
    """Extract text from one supported input file."""
    extension = file_path.suffix.lower()

    if extension in TEXT_EXTENSIONS:
        return read_plain_text(file_path), "extracted"

    if extension == ".pdf":
        text, warning = read_pdf_text(file_path)
        if warning:
            return "", warning
        return text, "extracted"

    if extension == ".docx":
        text, warning = read_docx_text(file_path)
        if warning:
            return "", warning
        return text, "extracted"

    if extension in SKIPPED_EXTENSIONS:
        return "", "skipped archive"

    return "", "unsupported extension"


def build_output_path(file_path: Path, input_directory: Path, output_directory: Path) -> Path:
    """Build a stable output text path for an input file."""
    relative_path = file_path.relative_to(input_directory)
    relative_without_suffix = relative_path.with_suffix("")
    safe_parts = [slugify(part) for part in relative_without_suffix.parts]
    safe_name = "__".join(safe_parts) + ".txt"
    return output_directory / safe_name


def extract_input_directory(input_directory: Path, output_directory: Path) -> dict:
    """Extract text from local input files and return a manifest."""
    output_directory.mkdir(parents=True, exist_ok=True)

    manifest_items = []
    warnings = []

    if not input_directory.exists():
        return {
            "input_dir": str(input_directory),
            "output_dir": str(output_directory),
            "exists": False,
            "total_files_seen": 0,
            "extracted_files": 0,
            "warnings": [f"Input directory does not exist: {input_directory}"],
            "files": [],
        }

    files_seen = 0
    extracted_count = 0

    for file_path in sorted(input_directory.rglob("*")):
        if not file_path.is_file():
            continue

        if file_path.name == ".gitkeep":
            continue

        files_seen += 1

        output_path = build_output_path(file_path, input_directory, output_directory)
        text, status = extract_text(file_path)

        extracted = bool(text.strip()) and status == "extracted"

        if extracted:
            output_path.write_text(text.strip() + "\n", encoding="utf-8")
            extracted_count += 1
        else:
            warnings.append(f"{file_path.name}: {status}")

        manifest_items.append(
            {
                "source_path": str(file_path.relative_to(input_directory)).replace("\\", "/"),
                "source_extension": file_path.suffix.lower(),
                "output_path": str(output_path).replace("\\", "/") if extracted else None,
                "status": status,
                "extracted": extracted,
                "character_count": len(text),
            }
        )

    return {
        "input_dir": str(input_directory),
        "output_dir": str(output_directory),
        "exists": True,
        "total_files_seen": files_seen,
        "extracted_files": extracted_count,
        "warnings": warnings,
        "files": manifest_items,
    }


def parse_arguments() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Extract readable text from local input files."
    )

    parser.add_argument(
        "--input-dir",
        default="data/input",
        help="Local input directory. Default: data/input",
    )

    parser.add_argument(
        "--output-dir",
        default="outputs/extracted-text",
        help="Output directory for extracted text. Default: outputs/extracted-text",
    )

    parser.add_argument(
        "--manifest",
        default="outputs/extracted-text-manifest.json",
        help="Manifest output path. Default: outputs/extracted-text-manifest.json",
    )

    return parser.parse_args()


def write_manifest(manifest: dict, manifest_path: Path) -> None:
    """Write extraction manifest to JSON."""
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    manifest_path.write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
        )


def print_summary(manifest: dict, manifest_path: Path) -> None:
    """Print extraction summary."""
    print("Input text extraction completed.")
    print(f"Input directory: {manifest['input_dir']}")
    print(f"Output directory: {manifest['output_dir']}")
    print(f"Total files seen: {manifest['total_files_seen']}")
    print(f"Extracted files: {manifest['extracted_files']}")
    print(f"Manifest: {manifest_path}")

    if manifest["warnings"]:
        print("\nWarnings:")
        for warning in manifest["warnings"]:
            print(f"- {warning}")


def main() -> int:
    """Run text extraction workflow."""
    args = parse_arguments()

    input_directory = Path(args.input_dir)
    output_directory = Path(args.output_dir)
    manifest_path = Path(args.manifest)

    manifest = extract_input_directory(input_directory, output_directory)

    write_manifest(manifest, manifest_path)
    print_summary(manifest, manifest_path)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
from __future__ import annotations

import sys
from pathlib import Path, PurePosixPath
from zipfile import ZIP_DEFLATED, ZipFile


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
SKILL_DIRECTORY = REPOSITORY_ROOT / "candidate-prioritization"
DISTRIBUTION_DIRECTORY = REPOSITORY_ROOT / "dist"
OUTPUT_ZIP = DISTRIBUTION_DIRECTORY / "candidate-prioritization-skill.zip"

EXCLUDED_DIRECTORY_NAMES = {
    "__pycache__",
}

EXCLUDED_FILE_NAMES = {
    ".DS_Store",
    ".gitkeep",
    "Thumbs.db",
}

EXCLUDED_FILE_SUFFIXES = {
    ".pyc",
}


def validate_skill_source() -> None:
    """Validate the minimum structure required by Claude."""

    if not SKILL_DIRECTORY.is_dir():
        raise FileNotFoundError(
            f"Skill directory not found: {SKILL_DIRECTORY}"
        )

    skill_file = SKILL_DIRECTORY / "SKILL.md"

    if not skill_file.is_file():
        raise FileNotFoundError(
            f"Required SKILL.md file not found: {skill_file}"
        )

    content = skill_file.read_text(encoding="utf-8").lstrip("\ufeff")

    if not content.startswith("---"):
        raise ValueError(
            "SKILL.md must begin with YAML front matter."
        )

    front_matter_parts = content.split("---", maxsplit=2)

    if len(front_matter_parts) < 3:
        raise ValueError(
            "SKILL.md contains incomplete YAML front matter."
        )

    front_matter = front_matter_parts[1]

    if "name:" not in front_matter:
        raise ValueError(
            "SKILL.md YAML front matter must include 'name:'."
        )

    if "description:" not in front_matter:
        raise ValueError(
            "SKILL.md YAML front matter must include 'description:'."
        )


def should_include(file_path: Path) -> bool:
    """Return True when the file should be included in the package."""

    relative_path = file_path.relative_to(SKILL_DIRECTORY)

    if any(
        part in EXCLUDED_DIRECTORY_NAMES
        for part in relative_path.parts
    ):
        return False

    if file_path.name in EXCLUDED_FILE_NAMES:
        return False

    if file_path.suffix.lower() in EXCLUDED_FILE_SUFFIXES:
        return False

    return file_path.is_file()


def collect_skill_files() -> list[Path]:
    """Collect skill files in a deterministic order."""

    files = sorted(
        file_path
        for file_path in SKILL_DIRECTORY.rglob("*")
        if should_include(file_path)
    )

    if not files:
        raise ValueError("No files were found to package.")

    return files


def create_package(files: list[Path]) -> None:
    """Create a Claude-compatible ZIP archive."""

    DISTRIBUTION_DIRECTORY.mkdir(parents=True, exist_ok=True)

    if OUTPUT_ZIP.exists():
        OUTPUT_ZIP.unlink()

    with ZipFile(
        OUTPUT_ZIP,
        mode="w",
        compression=ZIP_DEFLATED,
    ) as archive:
        for file_path in files:
            archive_path = (
                file_path
                .relative_to(SKILL_DIRECTORY)
                .as_posix()
            )

            archive.write(
                filename=file_path,
                arcname=archive_path,
            )


def validate_package() -> list[str]:
    """Validate paths and required files inside the generated ZIP."""

    with ZipFile(OUTPUT_ZIP, mode="r") as archive:
        names = archive.namelist()

        if not names:
            raise ValueError("The generated ZIP is empty.")

        if "SKILL.md" not in names:
            raise ValueError(
                "SKILL.md is not located at the root of the ZIP."
            )

        if len(names) != len(set(names)):
            raise ValueError(
                "The generated ZIP contains duplicate paths."
            )

        for name in names:
            if "\\" in name:
                raise ValueError(
                    f"Invalid Windows separator found in ZIP path: {name}"
                )

            if name.startswith("/"):
                raise ValueError(
                    f"Absolute path found in ZIP: {name}"
                )

            path = PurePosixPath(name)

            if ".." in path.parts:
                raise ValueError(
                    f"Unsafe parent path found in ZIP: {name}"
                )

            if path.parts[0] == SKILL_DIRECTORY.name:
                raise ValueError(
                    "The ZIP contains an unnecessary outer "
                    "'candidate-prioritization' directory."
                )

        corrupted_file = archive.testzip()

        if corrupted_file is not None:
            raise ValueError(
                f"Corrupted file detected in ZIP: {corrupted_file}"
            )

        return names


def main() -> int:
    try:
        validate_skill_source()

        files = collect_skill_files()

        create_package(files)

        packaged_paths = validate_package()

        size_kb = OUTPUT_ZIP.stat().st_size / 1024

        print("Claude-compatible skill package created successfully.")
        print(f"Source: {SKILL_DIRECTORY}")
        print(f"Output: {OUTPUT_ZIP}")
        print(f"Packaged files: {len(packaged_paths)}")
        print(f"Package size: {size_kb:.2f} KB")
        print("SKILL.md location: ZIP root")
        print("Path format: POSIX-compatible forward slashes")
        print("Archive integrity: passed")

        return 0

    except Exception as error:
        print(
            f"Package creation failed: {error}",
            file=sys.stderr,
        )
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
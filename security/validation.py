from pathlib import Path

ALLOWED_IMAGE_EXTENSIONS = [".jpg", ".jpeg", ".png"]
ALLOWED_DATA_EXTENSIONS = [".csv"]

MAX_FILE_SIZE_MB = 20


def validate_file(file_path: str) -> bool:
    path = Path(file_path)

    if not path.exists():
        raise ValueError("File does not exist.")

    if path.suffix.lower() not in (
        ALLOWED_IMAGE_EXTENSIONS + ALLOWED_DATA_EXTENSIONS
    ):
        raise ValueError("Unsupported file type.")

    size_mb = path.stat().st_size / (1024 * 1024)

    if size_mb > MAX_FILE_SIZE_MB:
        raise ValueError(
            f"File exceeds {MAX_FILE_SIZE_MB} MB limit."
        )

    return True
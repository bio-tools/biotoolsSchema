"""Shared helpers for the artifact build scripts."""

import json
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[1]
ENUMS_DIR = REPO_ROOT / "enums"
DIST_DIR = REPO_ROOT.parent / "dist"


def load_vocab(vocab: str) -> Any:
    path = ENUMS_DIR / f"{vocab}.json"
    if not path.is_file():
        raise FileNotFoundError(f"vocab file not found: {path}")
    return json.loads(path.read_text(encoding="utf-8"))


def load_vocab_values(vocab: str, include_deprecated: bool = False) -> list[str]:
    payload = load_vocab(vocab)

    if isinstance(payload, list):
        return payload
    ids = [v["id"] for v in payload.get("values", [])]
    ids += [v["id"] for v in payload.get("curated_extra", [])]
    if include_deprecated:
        ids += [
            v["id"] for v in payload.get("deprecated", [])
        ]  # Keep deprecated values for bio.tools entries that still use them
    return ids


def resolve_output_path(
    output_path: Path | None, filename: str, default_dir: Path = DIST_DIR
) -> Path:

    dir = output_path or default_dir
    dir.mkdir(parents=True, exist_ok=True)

    return dir / filename

import json
from dataclasses import dataclass
from pathlib import Path

import pytest

from btschema.build import build_jsonschema, build_xsd, generate_vocab

REPO_ROOT = Path(__file__).resolve().parents[1]
ENUMS_DIR = REPO_ROOT / "src" / "enums"
VOCABS = [
    p.stem
    for p in sorted(ENUMS_DIR.glob("*.json"))
    if p.stem != "license_curated_extra"
]


@dataclass(frozen=True)
class BuiltArtifacts:
    dir: Path
    vocab: Path
    xsd: Path
    jsonschema: Path


def pytest_addoption(parser):
    parser.addoption(
        "--schema-dir",
        action="store",
        dest="schema_dir",
        default=None,
        metavar="DIR",
        help=(
            "Use pre-built schema artifacts from this directory instead of building them."
        ),
    )


@pytest.fixture(scope="session")
def built_artifacts(request, tmp_path_factory) -> BuiltArtifacts:
    """
    Build the schema artifacts for testing, or use pre-built artifacts if --schema-dir is specified.
    """
    schema_dir = request.config.getoption("--schema-dir")

    if schema_dir:
        output_dir = Path(schema_dir).resolve()

        if not output_dir.is_dir():
            pytest.fail(f"--schema-dir {output_dir} is not a directory")

        xsd_candidates = sorted(output_dir.glob("biotools-*.xsd"))
        jsonschema_candidates = sorted(output_dir.glob("biotools-*.schema.json"))
        vocab_candidates = sorted(output_dir.glob("biotools_vocab.py"))

        if len(xsd_candidates) != 1:
            pytest.fail(
                f"--schema-dir {output_dir} must contain exactly one biotools-*.xsd file"
            )

        if len(jsonschema_candidates) != 1:
            pytest.fail(
                f"--schema-dir {output_dir} must contain exactly one biotools-*.schema.json file"
            )

        if len(vocab_candidates) != 1:
            pytest.fail(
                f"--schema-dir {output_dir} must contain exactly one biotools_vocab.py file"
            )

        return BuiltArtifacts(
            dir=output_dir,
            vocab=vocab_candidates[0],
            xsd=xsd_candidates[0],
            jsonschema=jsonschema_candidates[0],
        )

    output_dir = tmp_path_factory.mktemp("schema-build")

    vocab_path = generate_vocab(output_dir)
    xsd_path = build_xsd("test", output_dir)
    jsonschema_path = build_jsonschema("test", output_dir)

    return BuiltArtifacts(
        dir=output_dir,
        vocab=vocab_path,
        xsd=xsd_path,
        jsonschema=jsonschema_path,
    )


def vocab_ids(vocab: str, deprecated: bool = False) -> set[str]:
    payload = json.loads((ENUMS_DIR / f"{vocab}.json").read_text(encoding="utf-8"))
    if isinstance(payload, list):
        return set(payload)
    ids = {v["id"] for v in payload.get("values", [])}
    ids |= {v["id"] for v in payload.get("curated_extra", [])}
    if deprecated:
        ids |= {v["id"] for v in payload.get("deprecated", [])}
    return ids

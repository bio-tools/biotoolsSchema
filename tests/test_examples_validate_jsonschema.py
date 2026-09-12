"""Validate representative tool records against the freshly built JSON Schema."""

import json
from pathlib import Path

import jsonschema
import pytest
import xmltodict
from conftest import REPO_ROOT, BuiltArtifacts

EXAMPLE_DIR = REPO_ROOT / "examples"


def _load_schema(built_artifacts: BuiltArtifacts):
    return json.loads(built_artifacts.jsonschema.read_text(encoding="utf-8"))


def test_built_jsonschema_is_valid_json_schema(built_artifacts: BuiltArtifacts):
    schema = _load_schema(built_artifacts)
    jsonschema.Draft7Validator.check_schema(schema)


def _xml_tool_to_json_minimal(xml_path: str | Path) -> dict:
    """Pull just the handful of mandatory/simple fields out of an official XML
    example - enough to prove the built schema accepts a realistic minimal
    record without needing a full XML->JSON structural mapper."""
    with open(xml_path, "rb") as fh:
        doc = xmltodict.parse(fh, process_namespaces=False)
    root_key = next(iter(doc))
    tool = doc[root_key].get("tool", doc[root_key])
    if isinstance(tool, list):
        tool = tool[0]
    minimal = {
        "name": tool["name"],
        "description": tool["description"],
        "homepage": tool["homepage"],
    }
    return minimal


def test_minimal_record_from_official_example_validates(
    built_artifacts: BuiltArtifacts,
):
    schema = _load_schema(built_artifacts)
    for example in sorted(EXAMPLE_DIR.glob("*.xml")):
        minimal = _xml_tool_to_json_minimal(example)
        jsonschema.validate(instance=[minimal], schema=schema)


def test_invalid_enum_value_is_rejected(built_artifacts: BuiltArtifacts):
    schema = _load_schema(built_artifacts)
    bad = [
        {
            "name": "x",
            "description": "x" * 20,
            "homepage": "http://example.org",
            "license": "Definitely-Not-A-Real-License",
        }
    ]

    with pytest.raises(jsonschema.ValidationError):
        jsonschema.validate(instance=bad, schema=schema)

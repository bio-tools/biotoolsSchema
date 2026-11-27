"""Shared paths and JSON helpers for the artifact tools."""

import json
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
SCHEMA_PATH = Path("jsonschema/biotoolsj.json")
LICENSE_PATH = Path("src/enums/license.json")
CURATED_LICENSE_PATH = LICENSE_PATH.with_name("license_curated_extra.json")


def repository_root():
    for start in (REPO_ROOT, Path.cwd()):
        for directory in (start, *start.parents):
            if (directory / SCHEMA_PATH).is_file():
                return directory
    raise FileNotFoundError("Run this command from the biotoolsSchema checkout.")


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def license_ids(snapshot, *groups):
    return [entry["id"] for group in groups for entry in snapshot[group]]


def schema_license_ids(snapshot):
    return sorted(
        set(license_ids(snapshot, "values", "curated_extra")) | set(snapshot["legacy_accepted"]),
        key=lambda value: (value.casefold(), value),
    )


def license_enum(schema):
    return schema["$defs"]["tool"]["properties"]["license"]["enum"]

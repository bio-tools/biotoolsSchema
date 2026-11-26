"""Validate bio.tools JSON files against the development schema."""

import argparse
import json
import sys
from pathlib import Path

from jsonschema import Draft202012Validator
from jsonschema.exceptions import SchemaError


SCHEMA_PATH = Path(__file__).with_name("biotoolsj.json")


def read_json(path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as error:
        raise ValueError(f"line {error.lineno}, column {error.colno}: {error.msg}") from error


def make_validators(schema):
    Draft202012Validator.check_schema(schema)
    batch = Draft202012Validator(schema)
    return batch, batch.evolve(schema={"$ref": "#/$defs/tool"})


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("files", nargs="*", type=Path, help="JSON files with a tool or an array of tools")
    parser.add_argument("--check-schema", action="store_true", help="check the schema without requiring record files")
    args = parser.parse_args()
    if not args.files and not args.check_schema:
        parser.error("provide at least one JSON file or use --check-schema")

    try:
        batch, tool = make_validators(read_json(SCHEMA_PATH))
    except SchemaError as error:
        print(f"{SCHEMA_PATH}: {error.json_path}: {error.message}", file=sys.stderr)
        return 1
    except (OSError, ValueError) as error:
        print(f"{SCHEMA_PATH}: {error}", file=sys.stderr)
        return 1

    invalid = False
    for path in args.files:
        try:
            data = read_json(path)
        except (OSError, ValueError) as error:
            print(f"{path}: {error}", file=sys.stderr)
            invalid = True
            continue

        if not isinstance(data, (dict, list)):
            print(f"{path}: $: expected a tool object or an array of tools", file=sys.stderr)
            invalid = True
            continue

        validator = tool if isinstance(data, dict) else batch
        for error in validator.iter_errors(data):
            print(f"{path}: {error.json_path}: {error.message}", file=sys.stderr)
            invalid = True

    return int(invalid)


if __name__ == "__main__":
    sys.exit(main())

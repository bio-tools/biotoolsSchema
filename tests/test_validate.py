import json
import subprocess
import sys
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from jsonschema import Draft202012Validator
from referencing import Registry
from referencing.jsonschema import DRAFT202012


ROOT = Path(__file__).resolve().parents[1]
SCHEMA_DIR = ROOT / "jsonschema"
EXAMPLES = SCHEMA_DIR / "examples"
MINIMAL = EXAMPLES / "minimal.json"
COLLECTION = EXAMPLES / "collection.json"


class ValidateTests(unittest.TestCase):
    def setUp(self):
        self.directory = Path(self.enterContext(TemporaryDirectory()))
        self.tool = json.loads(MINIMAL.read_text(encoding="utf-8"))

    def run_cli(self, *files):
        return subprocess.run(
            [sys.executable, str(SCHEMA_DIR / "validate.py"), *files],
            cwd=self.directory,
            capture_output=True,
            text=True,
        )

    def write_json(self, name, data):
        path = self.directory / name
        path.write_text(json.dumps(data), encoding="utf-8")
        return path

    def test_examples_validate(self):
        result = self.run_cli(MINIMAL, COLLECTION)
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_single_tool_entry_point_used_by_editors(self):
        path = SCHEMA_DIR / "biotools-tool.json"
        schema = json.loads(path.read_text(encoding="utf-8"))
        canonical = path.with_name("biotoolsj.json")
        registry = Registry().with_resources(
            (file.as_uri(), DRAFT202012.create_resource(json.loads(file.read_text(encoding="utf-8"))))
            for file in (path, canonical)
        )
        Draft202012Validator.check_schema(schema)
        validator = Draft202012Validator({"$ref": path.as_uri()}, registry=registry)
        validator.validate(self.tool)
        self.assertFalse(validator.is_valid([self.tool]))
        self.assertFalse(validator.is_valid({**self.tool, "homepage": "example.org"}))

    def test_schema_errors_include_file_and_field(self):
        invalid = {
            **self.tool,
            "elixirCommunity": ["Invalid community"],
            "publication": [{"type": ["Primary"]}],
        }
        path = self.write_json("invalid.tools.json", [self.tool, invalid])
        result = self.run_cli(path)
        self.assertEqual(result.returncode, 1)
        self.assertIn(f"{path}: $[1].elixirCommunity[0]:", result.stderr)
        self.assertIn(f"{path}: $[1].publication[0]:", result.stderr)

    def test_malformed_json_does_not_stop_other_files(self):
        broken = self.directory / "broken.json"
        broken.write_text("{", encoding="utf-8")
        scalar = self.write_json("scalar.json", 42)
        result = self.run_cli(broken, scalar)
        self.assertEqual(result.returncode, 1)
        self.assertIn(f"{broken}: line 1, column 2:", result.stderr)
        self.assertIn(f"{scalar}: $: expected a tool object or an array of tools", result.stderr)


if __name__ == "__main__":
    unittest.main()

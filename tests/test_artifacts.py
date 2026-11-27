import io
import json
import runpy
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import patch
from urllib.error import URLError

from jsonschema import Draft202012Validator

from btschema.build import VOCABS, build_jsonschema, generate_vocab
from btschema.build_utils import (
    CURATED_LICENSE_PATH,
    LICENSE_PATH,
    SCHEMA_PATH,
    license_enum,
    license_ids,
    read_json,
    repository_root,
    schema_license_ids,
)
from btschema.fetch_spdx_licenses import refresh


ROOT = repository_root()


class ArtifactTests(unittest.TestCase):
    def test_builds_are_reproducible(self):
        with TemporaryDirectory() as first, TemporaryDirectory() as second:
            schema = build_jsonschema("4.0.0", Path(first))
            vocab = generate_vocab(Path(first))
            self.assertEqual(schema.read_bytes(), (ROOT / SCHEMA_PATH).read_bytes())
            self.assertEqual(schema.read_bytes(), build_jsonschema("4.0.0", Path(second)).read_bytes())
            self.assertEqual(vocab.read_bytes(), generate_vocab(Path(second)).read_bytes())

            output = runpy.run_path(str(vocab))
            properties = read_json(schema)["$defs"]["tool"]["properties"]
            self.assertEqual({key for key in output if key.isupper()}, set(VOCABS))
            for variable, path in VOCABS.items():
                values = properties
                for key in path.split("."):
                    values = values[key]
                if variable == "LICENSE":
                    deprecated = license_ids(read_json(ROOT / LICENSE_PATH), "deprecated")
                    values = list(dict.fromkeys([*values, *deprecated]))
                self.assertEqual(output[variable], [(value, value) for value in values])

    def test_vocabulary_compatibility(self):
        schema = read_json(ROOT / SCHEMA_PATH)
        snapshot = read_json(ROOT / LICENSE_PATH)
        self.assertEqual(license_enum(schema), schema_license_ids(snapshot))
        self.assertEqual(len(license_enum(schema)), len(set(license_enum(schema))))
        batch = Draft202012Validator(schema)
        tool = read_json(ROOT / "jsonschema/examples/minimal.json")
        batch.validate([{**tool, "license": identifier} for identifier in snapshot["legacy_accepted"]])
        batch.validate([{
            **tool,
            "toolType": ["Bioinformatics portal"],
            "language": ["JSP", "MLXTRAN", "NMTRAN", "PyMOL"],
            "publication": [{"pmid": "123", "type": ["Preprint"]}],
            "documentation": [{"url": "https://example.org", "type": ["Command-line options"]}],
            "credit": [{"name": "Example team", "typeRole": ["Documentor"]}],
        }])
        deprecated_only = set(license_ids(snapshot, "deprecated")) - set(snapshot["legacy_accepted"])
        self.assertTrue(deprecated_only)
        for identifier in deprecated_only:
            self.assertFalse(batch.is_valid([{**tool, "license": identifier}]))


class SpdxRefreshTests(unittest.TestCase):
    def setUp(self):
        self.root = Path(self.enterContext(TemporaryDirectory()))
        schema = read_json(ROOT / SCHEMA_PATH)
        license_enum(schema)[:] = ["GPL-2.0", "MIT", "Other"]
        self.write(SCHEMA_PATH, schema)
        self.write(LICENSE_PATH, {"legacy_accepted": []})
        self.write(CURATED_LICENSE_PATH, [{"id": "Other"}])
        self.feed = {
            "licenseListVersion": "test-1",
            "licenses": [
                {"licenseId": "MIT", "name": "MIT"},
                {"licenseId": "Apache-2.0", "name": "Apache 2.0"},
                {"licenseId": "GPL-2.0", "name": "GPL 2.0", "isDeprecatedLicenseId": True},
                {"licenseId": "Old", "name": "Old license", "isDeprecatedLicenseId": True},
            ],
        }

    def write(self, path, value):
        target = self.root / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(json.dumps(value), encoding="utf-8")

    def files(self):
        return [(self.root / path).read_bytes() for path in (LICENSE_PATH, SCHEMA_PATH)]

    def refresh(self, check=False):
        with patch("btschema.fetch_spdx_licenses.urlopen", return_value=io.BytesIO(json.dumps(self.feed).encode())):
            with redirect_stdout(io.StringIO()):
                return refresh(self.root, "test-1", check)

    def test_check_refresh_and_repeat(self):
        original = self.files()
        self.assertEqual(self.refresh(check=True), 1)
        self.assertEqual(self.files(), original)

        self.assertEqual(self.refresh(), 0)
        snapshot = read_json(self.root / LICENSE_PATH)
        self.assertEqual(snapshot["legacy_accepted"], ["GPL-2.0"])
        self.assertEqual(
            license_enum(read_json(self.root / SCHEMA_PATH)),
            ["Apache-2.0", "GPL-2.0", "MIT", "Other"],
        )
        refreshed = self.files()
        self.assertEqual(self.refresh(check=True), 0)
        self.assertEqual(self.refresh(), 0)
        self.assertEqual(self.files(), refreshed)

    def test_feed_errors_leave_files_intact(self):
        original = self.files()
        with patch("btschema.fetch_spdx_licenses.urlopen", side_effect=URLError("offline")):
            with self.assertRaises(URLError):
                refresh(self.root, "test-1")
        self.assertEqual(self.files(), original)

        self.feed["licenses"] = []
        with self.assertRaises(ValueError):
            self.refresh()
        self.assertEqual(self.files(), original)

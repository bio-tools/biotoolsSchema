"""
Validate the official bio.tools example XML files against the freshly
built XSD, to catch structural regressions (missing elements, bad
cardinality, mis-typed enums, malformed template placeholders, etc.).
"""

import xmlschema
from conftest import REPO_ROOT, BuiltArtifacts
from lxml import etree

EXAMPLE_DIR = REPO_ROOT / "examples"


def test_built_xsd_is_well_formed_xml(built_artifacts: BuiltArtifacts):
    etree.parse(str(built_artifacts.xsd))


def test_built_xsd_is_structurally_valid(built_artifacts: BuiltArtifacts):
    xmlschema.XMLSchema(str(built_artifacts.xsd))


def _example_files():
    return sorted(EXAMPLE_DIR.glob("*.xml"))


def test_example_files_present():
    examples = _example_files()
    assert examples, f"no example XML files found in {EXAMPLE_DIR}"


def test_official_examples_validate_against_built_xsd(built_artifacts: BuiltArtifacts):
    schema = xmlschema.XMLSchema(str(built_artifacts.xsd))
    for example in _example_files():
        schema.validate(str(example))

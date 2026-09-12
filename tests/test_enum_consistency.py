"""
Verify that the generated XSD, JSON Schema, and biotools_vocab.py are consistent with the source-of-truth JSON vocab files in src/enums.
build_xsd() -> excludes deprecated values
build_jsonschema() -> excludes deprecated values
generate_vocab() -> INCLUDES deprecated values so existing bio.tools records remain representable
"""

import importlib.util
import json
from typing import Any

from conftest import VOCABS, BuiltArtifacts, vocab_ids
from lxml import etree

XSD_NS = {"xs": "http://www.w3.org/2001/XMLSchema"}
# vocab -> (element name, enclosing parent element name or None if unambiguous).
# XSD uses anonymous inline simpleType/restriction blocks
# nested inside the xs:element they constrain - there are no named
# top-level simpleTypes to look up by name, so we locate by element (and, for the "type" element reused across several parents, by parent too).
XSD_ELEMENT_LOOKUP = {
    "language": ("language", None),
    "license": ("license", None),
    "operating_system": ("operatingSystem", None),
    "tool_type": ("toolType", None),
    "maturity": ("maturity", None),
    "cost": ("cost", None),
    "accessibility": ("accessibility", None),
    "elixir_platform": ("elixirPlatform", None),
    "elixir_community": ("elixirCommunity", None),
    "elixir_node": ("elixirNode", None),
    "credit_type_entity": ("typeEntity", None),
    "credit_type_role": ("typeRole", None),
    "other_id_type": ("type", "otherID"),
    "link_type": ("type", "link"),
    "download_type": ("type", "download"),
    "documentation_type": ("type", "documentation"),
    "relation_type": ("type", "relation"),
    "publication_type": ("type", "publication"),
}
# Backwards-compatible alias so the rest of this module can keep iterating
# "the 18 vocabs with an XSD element" without a rename everywhere below.
XSD_SIMPLETYPE_NAMES = XSD_ELEMENT_LOOKUP

# Source vocabulary name -> generated biotools_vocab.py variable name
VOCAB_VAR_NAMES = {
    "language": "LANGUAGE",
    "license": "LICENSE",
    "operating_system": "OPERATING_SYSTEM",
    "tool_type": "TOOL_TYPE",
    "maturity": "MATURITY",
    "cost": "COST",
    "accessibility": "ACCESSIBILITY",
    "elixir_platform": "ELIXIR_PLATFORM",
    "elixir_community": "ELIXIR_COMMUNITY",
    "elixir_node": "ELIXIR_NODE",
    "other_id_type": "OTHER_ID_TYPE",
    "link_type": "LINK_TYPE",
    "download_type": "DOWNLOAD_TYPE",
    "documentation_type": "DOCUMENTATION_TYPE",
    "relation_type": "RELATION_TYPE",
    "publication_type": "PUBLICATION_TYPE",
    "credit_type_entity": "CREDIT_TYPE_ENTITY",
    "credit_type_role": "CREDIT_TYPE_ROLE",
}


def xsd_values_for(built_artifacts: BuiltArtifacts, vocab: str) -> set[str]:
    elem_name, parent_name = XSD_ELEMENT_LOOKUP[vocab]
    tree = etree.parse(str(built_artifacts.xsd))
    root = tree.getroot()
    candidates = root.findall(f".//xs:element[@name='{elem_name}']", XSD_NS)
    assert candidates, f"xs:element[@name='{elem_name}'] not found in built XSD"

    if parent_name is None:
        assert len(candidates) == 1, (
            f"expected exactly one xs:element[@name='{elem_name}'], found {len(candidates)} "
            "- update XSD_ELEMENT_LOOKUP with a disambiguating parent"
        )
        target = candidates[0]
    else:
        # Disambiguate by nearest enclosing xs:element with @name == parent_name.
        parent_elem = root.find(f".//xs:element[@name='{parent_name}']", XSD_NS)
        assert (
            parent_elem is not None
        ), f"parent xs:element[@name='{parent_name}'] not found"
        matches = parent_elem.findall(f".//xs:element[@name='{elem_name}']", XSD_NS)
        assert len(matches) == 1, (
            f"expected exactly one xs:element[@name='{elem_name}'] under parent '{parent_name}', "
            f"found {len(matches)}"
        )
        target = matches[0]

    enums = target.findall(".//xs:enumeration", XSD_NS)
    assert (
        enums
    ), f"no xs:enumeration values found under element '{elem_name}' (parent={parent_name})"
    return {e.get("value") for e in enums}


def jsonschema_values_for(
    built_artifacts: BuiltArtifacts, vocab: str, path_map: dict
) -> set[str]:
    schema = json.loads(built_artifacts.jsonschema.read_text(encoding="utf-8"))
    node = schema
    for key in path_map[vocab].split("."):
        node = node[key]
    return set(node["enum"])


JSONSCHEMA_PATHS = {
    "tool_type": "definitions.tool.properties.toolType.items",
    "operating_system": "definitions.tool.properties.operatingSystem.items",
    "language": "definitions.tool.properties.language.items",
    "license": "definitions.tool.properties.license",
    "maturity": "definitions.tool.properties.maturity",
    "cost": "definitions.tool.properties.cost",
    "accessibility": "definitions.tool.properties.accessibility",
    "elixir_platform": "definitions.tool.properties.elixirPlatform.items",
    "elixir_community": "definitions.tool.properties.elixirCommunity.items",
    "elixir_node": "definitions.tool.properties.elixirNode.items",
    "other_id_type": "definitions.tool.properties.otherID.items.properties.type",
    "link_type": "definitions.tool.properties.link.items.properties.type.items",
    "download_type": "definitions.tool.properties.download.items.properties.type",
    "documentation_type": "definitions.tool.properties.documentation.items.properties.type.items",
    "relation_type": "definitions.tool.properties.relation.items.properties.type",
    "publication_type": "definitions.tool.properties.publication.items.properties.type.items",
    "credit_type_entity": "definitions.tool.properties.credit.items.properties.typeEntity",
    "credit_type_role": "definitions.tool.properties.credit.items.properties.typeRole.items",
}


def _load_vocab_module(built_artifacts: BuiltArtifacts) -> Any:
    spec = importlib.util.spec_from_file_location("vocab", built_artifacts.vocab)

    assert spec is not None
    assert spec.loader is not None

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def vocab_values_for(built_artifacts: BuiltArtifacts, vocab: str) -> set[str]:
    module = _load_vocab_module(built_artifacts)
    var_name = VOCAB_VAR_NAMES[vocab]
    choices = getattr(module, var_name)
    return {value for value, _label in choices}


def test_every_vocab_has_source_file():
    for vocab in VOCAB_VAR_NAMES:
        assert vocab in VOCABS, f"missing src/enums/{vocab}.json"


def test_xsd_matches_source_of_truth(built_artifacts: BuiltArtifacts):
    for vocab in XSD_SIMPLETYPE_NAMES:
        expected = vocab_ids(vocab)
        actual = xsd_values_for(built_artifacts, vocab)
        assert actual == expected, (
            f"XSD/{vocab} drifted from src/enums/{vocab}.json: "
            f"only-in-xsd={actual - expected} "
            f"only-in-source={expected - actual}"
        )


def test_jsonschema_matches_source_of_truth(built_artifacts: BuiltArtifacts):
    for vocab in JSONSCHEMA_PATHS:
        expected = vocab_ids(vocab)
        actual = jsonschema_values_for(built_artifacts, vocab, JSONSCHEMA_PATHS)
        assert actual == expected, (
            f"JSON Schema/{vocab} drifted from src/enums/{vocab}.json: "
            f"only-in-schema={actual - expected} "
            f"only-in-source={expected - actual}"
        )


def test_vocab_matches_source_of_truth(built_artifacts: BuiltArtifacts):
    for vocab in VOCAB_VAR_NAMES:
        expected = vocab_ids(vocab, deprecated=True)
        actual = vocab_values_for(built_artifacts, vocab)
        assert actual == expected, (
            f"biotools_vocab.py/{vocab} drifted from src/enums/{vocab}.json: "
            f"only-in-vocab={actual - expected} "
            f"only-in-source={expected - actual}"
        )

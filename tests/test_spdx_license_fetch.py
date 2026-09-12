"""
Tests for the commited SPDX-derived license vocabulary.
"""

import json

from conftest import ENUMS_DIR


def test_license_json_has_expected_shape():
    payload = json.loads((ENUMS_DIR / "license.json").read_text(encoding="utf-8"))
    assert isinstance(payload, dict)
    assert isinstance(payload["values"], list)
    assert isinstance(payload["deprecated"], list)
    assert isinstance(payload["curated_extra"], list)

    active_ids = {license_["id"] for license_ in payload["values"]}

    assert len(active_ids) > 500, "expected the full active SPDX license list"
    assert "MIT" in active_ids
    assert "Apache-2.0" in active_ids

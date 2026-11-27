"""Refresh the SPDX snapshot and the canonical schema's license enum."""

import argparse
import json
from pathlib import Path
from tempfile import NamedTemporaryFile
from urllib.parse import quote
from urllib.request import urlopen

from .build_utils import (
    CURATED_LICENSE_PATH,
    LICENSE_PATH,
    SCHEMA_PATH,
    license_enum,
    license_ids,
    read_json,
    repository_root,
    schema_license_ids,
)


SPDX_URL = "https://raw.githubusercontent.com/spdx/license-list-data/{ref}/json/licenses.json"


def write_json(path, payload, indent):
    content = json.dumps(payload, ensure_ascii=False, indent=indent) + "\n"
    with NamedTemporaryFile(mode="w", encoding="utf-8", dir=path.parent, delete=False) as handle:
        temporary = Path(handle.name)
        try:
            handle.write(content)
            handle.close()
            temporary.chmod(path.stat().st_mode & 0o777)
            temporary.replace(path)
        finally:
            temporary.unlink(missing_ok=True)


def build_payload(feed, curated, previous_accepted, source):
    values = []
    deprecated = []
    seen = set()
    for item in feed["licenses"]:
        identifier = item["licenseId"]
        if not isinstance(identifier, str) or not identifier or identifier in seen:
            raise ValueError(f"Invalid or duplicate SPDX license ID: {identifier!r}")
        seen.add(identifier)
        entry = {
            "id": identifier,
            "name": item["name"],
            "osi_approved": bool(item.get("isOsiApproved", False)),
        }
        group = deprecated if item.get("isDeprecatedLicenseId", False) else values
        group.append(entry)
    if not values or not feed["licenseListVersion"]:
        raise ValueError("An SPDX feed must contain a version and active licenses.")

    active = {entry["id"] for entry in [*values, *curated]}
    return {
        "source": source,
        "spdx_license_list_version": feed["licenseListVersion"],
        "generator": "src/btschema/fetch_spdx_licenses.py",
        "values": sorted(values, key=lambda entry: entry["id"].casefold()),
        "deprecated": sorted(deprecated, key=lambda entry: entry["id"].casefold()),
        "curated_extra": curated,
        "legacy_accepted": sorted(set(previous_accepted) - active, key=lambda value: (value.casefold(), value)),
    }


def refresh(root, ref, check=False):
    snapshot_path = root / LICENSE_PATH
    schema_path = root / SCHEMA_PATH
    previous = read_json(snapshot_path)
    schema = read_json(schema_path)
    curated = read_json(root / CURATED_LICENSE_PATH)
    source = SPDX_URL.format(ref=quote(ref, safe="/"))
    with urlopen(source, timeout=30) as response:
        feed = json.load(response)

    current = license_enum(schema)
    accepted = [*current, *previous.get("legacy_accepted", [])]
    snapshot = build_payload(feed, curated, accepted, source)
    expected = schema_license_ids(snapshot)
    snapshot_changed = snapshot != previous
    schema_changed = expected != current
    if not (snapshot_changed or schema_changed):
        print("SPDX snapshot and schema are up to date.")
        return 0
    if check:
        print("SPDX snapshot or schema has changed. Run fetch-spdx to update.")
        return 1

    if snapshot_changed:
        write_json(snapshot_path, snapshot, indent=2)
    if schema_changed:
        current[:] = expected
        write_json(schema_path, schema, indent="\t")
    print(f"SPDX {snapshot['spdx_license_list_version']}: {len(license_ids(snapshot, 'values'))} active SPDX licenses.")
    return 0


def fetch_spdx_licenses():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--ref", default="main", help="SPDX license-list-data Git ref (default: main)")
    parser.add_argument("--check", action="store_true", help="report changes without writing files")
    args = parser.parse_args()
    try:
        return refresh(repository_root(), args.ref, args.check)
    except (OSError, ValueError, KeyError, TypeError) as error:
        parser.exit(2, f"SPDX refresh failed: {error}\n")


if __name__ == "__main__":
    raise SystemExit(fetch_spdx_licenses())

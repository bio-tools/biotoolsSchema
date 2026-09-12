#!/usr/bin/env python3
"""
Refresh src/enums/license.json from the live SPDX License List.

Source: https://github.com/spdx/license-list-data
    https://raw.githubusercontent.com/spdx/license-list-data/main/json/licenses.json

Non-SPDX values (Proprietary, Freeware, Not licensed, Other)
are NOT licenses in SPDX's sense and are merged in from
src/enums/license_curated_extra.json, which is hand-maintained.
"""

import argparse
import json
import sys
import urllib.request
from datetime import UTC, datetime
from pathlib import Path

PKG_ROOT = Path(__file__).resolve().parents[1]
ENUMS_DIR = PKG_ROOT / "enums"
LICENSE_PATH = ENUMS_DIR / "license.json"
CURATED_EXTRA_PATH = ENUMS_DIR / "license_curated_extra.json"

SPDX_URL_TMPL = (
    "https://raw.githubusercontent.com/spdx/license-list-data/{ref}/json/licenses.json"
)


def ensure_curated_extra():
    if not CURATED_EXTRA_PATH.exists():
        raise RuntimeError(f"Missing curated extra file: {CURATED_EXTRA_PATH}")
    return json.loads(CURATED_EXTRA_PATH.read_text(encoding="utf-8"))


def fetch_spdx(ref: str):
    url = SPDX_URL_TMPL.format(ref=ref)
    try:
        with urllib.request.urlopen(url, timeout=30) as resp:
            data = json.load(resp)
    except urllib.error.HTTPError as e:
        if e.code == 404:
            raise RuntimeError(
                f"Failed to fetch SPDX license list: {e}. "
                f"Check that the ref/tag exists in the SPDX repository."
            )
        raise RuntimeError(f"Failed to fetch SPDX license list from {url}: {e}")
    return data


def build_payload(spdx_data, curated_extra, ref: str):
    values = []
    deprecated = []
    for lic in spdx_data.get("licenses", []):
        entry = {
            "id": lic["licenseId"],
            "name": lic.get("name"),
            "osi_approved": bool(lic.get("isOsiApproved", False)),
        }
        if lic.get("isDeprecatedLicenseId"):
            deprecated.append(entry)
        else:
            values.append(entry)

    values.sort(key=lambda v: v["id"].lower())
    deprecated.sort(key=lambda v: v["id"].lower())

    return {
        "source": SPDX_URL_TMPL.format(ref=ref),
        "spdx_license_list_version": spdx_data.get("licenseListVersion"),
        "generated_at": datetime.now(UTC).isoformat(),
        "generator": "scripts/fetch_spdx_licenses.py",
        "values": values,
        "deprecated": deprecated,
        "curated_extra": curated_extra,
    }


def output(new, old):
    old_values = {x["id"]: x for x in old["values"] if x["id"] not in new["values"]}
    new_values = {x["id"]: x for x in new["values"]}

    added = sorted(set(new_values) - set(old_values))
    removed = sorted(set(old_values) - set(new_values))
    modified = sorted(
        x for x in set(new_values) & set(old_values) if new_values[x] != old_values[x]
    )

    print(f"Added licenses: {len(added)}")
    for license_id in added:
        print(f"  + {license_id}")
    print(f"Removed licenses: {len(removed)}")
    for license_id in removed:
        print(f"  - {license_id}")
    print(f"Modified licenses: {len(modified)}")
    for license_id in modified:
        print(f"  * {license_id}")
        print(f"    old: {old_values[license_id]}")
        print(f"    new: {new_values[license_id]}")


def fetch_spdx_licenses():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--ref", default="main", help="SPDX license-list-data git ref/tag to fetch"
    )
    parser.add_argument(
        "--check", action="store_true", help="don't write, exit 1 if changed"
    )
    args = parser.parse_args()

    curated_extra = ensure_curated_extra()
    spdx_data = fetch_spdx(args.ref)
    new_payload = build_payload(spdx_data, curated_extra, args.ref)

    if LICENSE_PATH.exists():
        old_payload = json.loads(LICENSE_PATH.read_text(encoding="utf-8"))
    else:
        old_payload = None

    def comparable(p):
        if p is None:
            return None
        return {
            "values": p.get("values"),
            "deprecated": p.get("deprecated"),
            "curated_extra": p.get("curated_extra"),
        }

    changed = comparable(old_payload) != comparable(new_payload)

    if args.check:
        if changed:
            print(
                f"license.json is stale: SPDX list has {len(new_payload['values'])} active licenses "
                f"(SPDX list version {new_payload['spdx_license_list_version']})"
            )
            output(new_payload, old_payload)
            sys.exit(1)
        print("license.json is up to date")
        sys.exit(0)

    LICENSE_PATH.write_text(json.dumps(new_payload, indent=2) + "\n", encoding="utf-8")
    print(
        f"wrote {LICENSE_PATH}: {len(new_payload['values'])} active licenses, "
        f"{len(new_payload['deprecated'])} deprecated, {len(curated_extra)} curated extras "
        f"(SPDX list version {new_payload['spdx_license_list_version']})"
    )


if __name__ == "__main__":
    fetch_spdx_licenses()

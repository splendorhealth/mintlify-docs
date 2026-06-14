#!/usr/bin/env python3
"""Sync the Splendor OpenAPI spec into the docs site.

Copies a freshly generated spec into ``api-reference/openapi.json`` and reorders
its ``paths`` so they appear grouped by product domain, in the order the spec's
own top-level ``tags`` array declares. Mintlify auto-generates the API reference
navigation from path order, so this makes the sidebar lead with Identity,
Datasets, Search, etc. — the same order the product repo defines in
``ALLOWED_TAGS`` (no duplicated ordering here).

Usage:
    python scripts/sync-openapi.py /path/to/withsplendor/openapi.json

Regenerate the source spec first in the product repo with ``make openapi``.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

OUTPUT = Path(__file__).resolve().parent.parent / "api-reference" / "openapi.json"


def _first_tag(path_item: dict[str, object]) -> str:
    for operation in path_item.values():
        if isinstance(operation, dict):
            tags = operation.get("tags")
            if isinstance(tags, list) and tags:
                return str(tags[0])
    return "~"  # untagged sorts last


def main() -> None:
    if len(sys.argv) != 2:
        sys.exit("usage: sync-openapi.py <path-to-generated-openapi.json>")
    spec = json.loads(Path(sys.argv[1]).read_text())

    tag_order = {t["name"]: i for i, t in enumerate(spec.get("tags", []))}
    paths: dict[str, dict[str, object]] = spec["paths"]
    spec["paths"] = dict(
        sorted(paths.items(), key=lambda kv: (tag_order.get(_first_tag(kv[1]), 999), kv[0]))
    )

    OUTPUT.write_text(json.dumps(spec, indent=2) + "\n")
    sys.stdout.write(f"Wrote {OUTPUT} ({len(spec['paths'])} paths)\n")


if __name__ == "__main__":
    main()

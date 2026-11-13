"""Ordered JSONL requests shared by Compass's read-only batch commands."""

from __future__ import annotations

import json
from typing import Callable, TextIO


def run_batch(stream: TextIO, fields: set[str], required: str, operation: Callable[[dict], dict]) -> int:
    count = 0
    invalid = False
    hit = False
    for count, line in enumerate(stream, 1):
        record = None
        try:
            record = json.loads(line)
            if not isinstance(record, dict):
                raise ValueError("request must be a JSON object")
            unknown = set(record) - fields - {"id"}
            if unknown:
                raise ValueError("unknown fields: " + ", ".join(sorted(unknown)))
            if not isinstance(record.get(required), str) or not record[required].strip():
                raise ValueError(f"{required} must be a non-empty string")
            result = operation(record)
        except (ValueError, TypeError) as error:
            result = {"status": "error", "error": str(error)}
            invalid = True
        result["line"] = count
        if isinstance(record, dict) and "id" in record:
            result["id"] = record["id"]
        hit = hit or result["status"] in ("hit", "ambiguous")
        print(json.dumps(result, ensure_ascii=False))
    if not count:
        print(json.dumps({"status": "error", "error": "empty batch", "line": 0}))
        return 2
    return 2 if invalid else 0 if hit else 1

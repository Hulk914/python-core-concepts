"""Translate validated JSON records to and from Task instances."""

from dataclasses import asdict
import json
from pathlib import Path

from projects.task_tracker.model import Task


def load_tasks(path):
    """A missing file starts empty; malformed data raises rather than being lost."""
    path = Path(path)
    try:
        text = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        return []
    try:
        records = json.loads(text)
    except json.JSONDecodeError as error:
        raise ValueError(f"Invalid JSON in {path}") from error
    if not isinstance(records, list):
        raise ValueError("Task file must contain a JSON list")

    tasks = []
    seen_ids = set()
    for record in records:
        if not isinstance(record, dict) or set(record) != {"id", "title", "done"}:
            raise ValueError("Each task must have exactly id, title, and done fields")
        # bool is a subclass of int; True must not accidentally become ID 1.
        if type(record["id"]) is not int or record["id"] < 1:
            raise ValueError("Task IDs must be positive integers")
        if record["id"] in seen_ids:
            raise ValueError("Task IDs must be unique")
        if not isinstance(record["title"], str) or not record["title"].strip():
            raise ValueError("Task titles must be non-empty strings")
        if type(record["done"]) is not bool:
            raise ValueError("Task done fields must be booleans")
        seen_ids.add(record["id"])
        tasks.append(Task(**record))
    return tasks


def save_tasks(path, tasks):
    """Write beside the destination, then replace it to avoid partial JSON files.

    This simple learning project supports one process at a time. A fixed staging
    path and a read/modify/write flow do not provide concurrent-update safety.
    """
    path = Path(path)
    content = json.dumps([asdict(task) for task in tasks], indent=2, ensure_ascii=False)
    path.parent.mkdir(parents=True, exist_ok=True)
    staging = path.with_name(path.name + ".tmp")
    try:
        staging.write_text(content + "\n", encoding="utf-8")
        staging.replace(path)
    finally:
        staging.unlink(missing_ok=True)

"""Argument parsing and presentation; domain behavior lives in model.py."""

import argparse
from pathlib import Path
import sys

from projects.task_tracker.model import add_task, complete_task, summarize
from projects.task_tracker.storage import load_tasks, save_tasks

# Predictable even when the command is invoked from another working directory.
DEFAULT_FILE = Path(__file__).resolve().parents[2] / ".practice" / "tasks.json"


def main(argv=None):
    parser = argparse.ArgumentParser(description="A small core-Python task tracker")
    parser.add_argument("--file", type=Path, default=DEFAULT_FILE, help="JSON storage path")
    commands = parser.add_subparsers(dest="command", required=True)
    add = commands.add_parser("add", help="Add a task")
    add.add_argument("title")
    commands.add_parser("list", help="List tasks")
    done = commands.add_parser("done", help="Mark a task complete")
    done.add_argument("id", type=int)
    commands.add_parser("summary", help="Show total, completed, and pending counts")
    args = parser.parse_args(argv)

    try:
        tasks = load_tasks(args.file)
        if args.command == "add":
            task = add_task(tasks, args.title)
            save_tasks(args.file, tasks)
            print(f"Added #{task.id}: {task.title}")
        elif args.command == "done":
            task = complete_task(tasks, args.id)
            save_tasks(args.file, tasks)
            print(f"Completed #{task.id}: {task.title}")
        elif args.command == "list":
            if not tasks:
                print("No tasks yet. Add one with: add \"Revise Python\"")
            for task in tasks:
                marker = "x" if task.done else " "
                print(f"[{marker}] {task.id}: {task.title}")
        else:
            counts = summarize(tasks)
            print(f"Total: {counts['total']} | Done: {counts['done']} | Pending: {counts['pending']}")
    except (ValueError, OSError) as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

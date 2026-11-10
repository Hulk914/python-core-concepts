"""A task data model and operations independent of the CLI and filesystem."""

from dataclasses import dataclass


@dataclass
class Task:
    id: int
    title: str
    done: bool = False


def add_task(tasks, title):
    """Add a task in place, assigning an ID above every existing ID."""
    title = title.strip()
    if not title:
        raise ValueError("Task title cannot be empty")
    next_id = max((task.id for task in tasks), default=0) + 1
    task = Task(next_id, title)
    tasks.append(task)
    return task


def complete_task(tasks, task_id):
    """Complete the matching task; repeating this operation is harmless."""
    for task in tasks:
        if task.id == task_id:
            task.done = True
            return task
    raise ValueError(f"No task with ID {task_id}")


def summarize(tasks):
    """Return counts without changing any tasks."""
    completed = sum(task.done for task in tasks)
    return {"total": len(tasks), "done": completed, "pending": len(tasks) - completed}

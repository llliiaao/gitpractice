"""一个使用标准库实现的简单命令行 Todo 工具。"""

import argparse
import json
from pathlib import Path


TASKS_FILE = Path(__file__).with_name("tasks.json")


def load_tasks():
    """从 JSON 文件读取任务；文件不存在时返回空列表。"""
    if not TASKS_FILE.exists():
        return []

    try:
        with TASKS_FILE.open("r", encoding="utf-8") as file:
            tasks = json.load(file)
    except json.JSONDecodeError:
        print("任务文件格式无效，将使用空任务列表。")
        return []

    return tasks if isinstance(tasks, list) else []


def save_tasks(tasks):
    """将任务列表写入 JSON 文件。"""
    with TASKS_FILE.open("w", encoding="utf-8") as file:
        json.dump(tasks, file, ensure_ascii=False, indent=2)


def add_task(title):
    tasks = load_tasks()
    tasks.append({"title": title, "done": False})
    save_tasks(tasks)
    print(f"已添加任务：{title}")


def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("暂无任务。")
        return

    for index, task in enumerate(tasks, start=1):
        status = "x" if task.get("done") else " "
        print(f"{index}. [{status}] {task.get('title', '未命名任务')}")


def build_parser():
    parser = argparse.ArgumentParser(description="简单的命令行 Todo 工具")
    subparsers = parser.add_subparsers(dest="command", required=True)

    add_parser = subparsers.add_parser("add", help="添加一条任务")
    add_parser.add_argument("title", help="任务内容")
    subparsers.add_parser("list", help="查看全部任务")
    return parser


def main():
    args = build_parser().parse_args()
    if args.command == "add":
        add_task(args.title)
    elif args.command == "list":
        list_tasks()


if __name__ == "__main__":
    main()

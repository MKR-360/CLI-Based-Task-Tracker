#!/usr/bin/python3

from rich.console import Console
import argparse

import os
import sys
import json
home_path = os.getenv("HOME")
folder_name = ".task_tracker"
file_name = "tasks.json"
dest = os.path.join(home_path, folder_name)
file_path = os.path.join(dest, file_name)

sys.path.append(f"{dest}")

from modules.manage import tasks # type:ignore

# curr_path = os.getcwd()


console = Console()

parser = argparse.ArgumentParser(description = "Check the validity of the parsed arguments.")
parser.add_argument("-l", action = "store_true", help = "List all the tasks.")
parser.add_argument("-u", action = "store_true", help = "List all uncompleted tasks.")
parser.add_argument("-c", action = "store_true", help = "List all completed tasks.")
parser.add_argument("--remove", type = str, help = "Remove the task with specified id.")
parser.add_argument("--add", type = str, help = "Add new task with name '--add [name]'")
parser.add_argument("--adds", nargs = "+", help = "Add a list of new task with name '--add name1 name2 name3 .....'")
parser.add_argument("--update", type = str, help = "Update status of a particular task")


args = parser.parse_args()

curr_tasks = dict() # Stores current tasks or initial tasks


if os.path.exists(f"{dest}"):
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            curr_tasks = json.load(file)
    else:
        with open(file_path, "w") as file:
            file.write("{}")
        with open(file_path, "r") as file:
            curr_tasks = json.load(file)
else:
    os.makedirs(dest)
    with open(file_path, "w") as file:
        file.write("{}")
    with open(file_path, "r") as file:
        curr_tasks = json.load(file)

task = tasks(curr_tasks)

if args.l:
    task.listAll()
elif args.u:
    task.listToDo()
elif args.c:
    task.listDone()
elif args.add:
    curr_tasks.update(task.add(args.add))

    with open(file_path, "w") as file:
        json.dump(curr_tasks, file, indent=True)
    console.print("[green]Successfully added[/green]")
elif args.adds:
    items = args.adds
    temp = dict()
    for i in items:
        temp.update(task.add(i))
    
    curr_tasks.update(temp)
    
    with open(file_path, "w") as file:
        json.dump(curr_tasks, file, indent=True)
    console.print(f"[green]Successfully added {len(items)} tasks.[/green]")
elif args.remove:
    curr_tasks = task.remove(args.remove)
    
    with open(file_path, "w") as file:
        json.dump(curr_tasks, file, indent=True)
elif args.update:
    temp = task.taskUpdate(args.update)
    curr_tasks.update(temp)

    with open(file_path, "w") as file:
        json.dump(curr_tasks, file, indent=True)
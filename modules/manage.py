#!/usr/bin/python3

import datetime as dt
import json
import os
from rich.console import Console
from rich.table import Table
import rich.box

home_path = os.getenv("HOME")
folder_name = ".task_tracker"
theme_path = "settings/theme.json"
theme_path = os.path.join(home_path, folder_name, theme_path)

console = Console()

class tasks():
    
    def __init__(self, data: dict):
        self.data = data

        self.theme = dict()
        with open(theme_path, "r") as file:
            self.theme = json.load(file)
    
    def add(self, name: str, id = 0) -> dict:
        if len(self.data) == 0:
            id = "1"
        else:
            id = str(int(list(self.data.keys())[-1]) + 1)
        
        curr_time = dt.datetime.now()
        self.data[id] = {"task": name, "createdAt": f'{curr_time}', "updatedAt": f'{curr_time}', "status": "To Do"}

        return self.data

    
    def listAll(self):
        table = Table(title="All Tasks", box = getattr(rich.box, self.theme["table"]["box"]))
        table.add_column(header="ID", justify="center", style="white")
        table.add_column(header="Task", justify="left", style="white")
        table.add_column(header="Created At", justify="center", style="white")
        table.add_column(header="Updated At", justify="center", style="white")
        table.add_column(header="Status", justify="center")

    
        if len(self.data) == 0:
            console.print("[bold red]No tasks are scheduled yet.[/bold red]")
        else:
            status_theme = self.theme["table"]["status"]
            for key, value in self.data.items():
                    status_colour = status_theme[value["status"]]
                    table.add_row(str(key), value["task"], value["createdAt"], value["updatedAt"], f'[{status_colour}]{value["status"]}[/{status_colour}]')
            console.print(table)
    
    def listToDo(self):
        table = Table(title = "To Do Tasks", box = getattr(rich.box, self.theme["table"]["box"]))
        table.add_column("ID", justify="center", style="white")
        table.add_column("Task", justify="left", style="white")
        table.add_column("Created At", justify="center", style="white")
        table.add_column("Updated At", justify="center", style="white")

        if len(self.data)<=0:
            console.print("[bold red]Either no tasks were scheduled or all tasks are done.[/bold red]")
        else:
            for key, value in self.data.items():
                if value["status"] == "To Do":
                    table.add_row(key, value["task"], value["updatedAt"], value["createdAt"])
            console.print(table)
    
    def listDone(self):
        table = Table(title = "Completed Tasks", box = getattr(rich.box, self.theme["table"]["box"]))
        table.add_column("ID", justify = "center", style="white")
        table.add_column("Task", justify = "left", style="white")
        table.add_column("Updated At", justify = "center", style="white")
        table.add_column("Created At", justify = "center", style="white")

        if len(self.data) <=0:
            console.print("[bold red]Either no tasks were scheduled or all tasks are done.[/bold red]")
        else:
            for key, value in self.data.items():
                if value["status"] == "Done":
                    table.add_row(key, value["task"], value["createdAt"], value["updatedAt"])
            console.print(table)

    
    def taskUpdate(self, id: str) -> dict:
        if self.data[id]["status"] == "To Do":
            self.data[id]["status"] = "Done"
            self.data[id]["updatedAt"] = str(dt.datetime.now())
            console.print(f"Task with id [bold green]'{id}'[/bold green] is set to [bold green]'Done'[/bold green].")
        else:
            self.data[id]["status"] = "To Do"
            self.data[id]["updatedAt"] = str(dt.datetime.now())
            console.print(f"Task with id [bold red]'{id}'[/bold red] is set to [bold red]'To Do'[/bold red].")
        
        return self.data
    
    def remove(self, id: str) -> dict:
        if id == "*":
            self.data.clear()
            return self.data
        else:
            try:
                del self.data[id]
                console.print("[yellow]Successfully deleted.[/yellow]")
            except:
                console.print("[bold red]Wrong task id.[/bold red]")

        return self.data
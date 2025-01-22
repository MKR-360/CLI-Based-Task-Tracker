# CLI Based Task Tracker
---

A **CLI (command line interface)** based task tracker through which a user can manage his/her day to day tasks efficiently and effectively just needing a CLI.  
(*Best for programmers using LINUX for their daily work.*)  

**Note:** Currently this is developed and tested only on Ubuntu 22 and lower versions.

---

## Introduction
This project is designed to substitute the need of a GUI based task management tool. It is for those who loves cli a lot and use it frequently for their things/tasks/stuff to get done. No distraction, no fancy GUI just a cli and your tasks.  

---

## Features
Below are some features it provides:
- Add tasks no matter single or multiple
- List all tasks
- List tasks based on the status
- Update the task status (To Do or Done)
- Remove a task which is done
- Unique ID for each task
- Have created and updated dates along with the time
- Tables and color coding for easy readability and organization
- Single command to use any where with simple flags and attributes
- Help page wherever you get stuck
- Local and efficient storage in JSON file format
- install and uninstall scripts for easiness

---

## Installation

**Avoid Installation for now still in development stage.**
1. Clone this repository
```
git clone https://github.com/mkr-360/CLI-Based-Task-Tracker.git
cd CLI-Based-Task-Tracker

pip install -r requirements.txt
```
2. Make install.sh executable and run
```
chmod +x ./install.sh
./install.sh
```
3. Task tracker is now successfully installed. Now you can delete the cloned repository

---

## Usage
```
# To add a single task
task-tracker --add "task1"

# To add multiple tasks in one go
task-tracker --adds "task1" "task2" "task3" ....... "nth task"

# List all tasks with their status
task-tracker -l

# List all uncompleted 'To Do' tasks
task-tracker -u

# List all completed tasks
task-tracker -c

# Update a single task with its id
task-tracker --update ID1

# Remove a single task with its id
task-tracker --remove ID1

# To remove all tasks in one go
task-tracker --remove "*"
```

---

## Uninstallation
```
~/.task-tracker/uninstall.sh
```

---
#### Contact
- [Email me](mailto:manoj210205@gmial.com?subject=[CLI-Based-Tracker])
- [GitHub](https://github.com/mkr-360)

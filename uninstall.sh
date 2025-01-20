#!/usr/bin/bash

cd $HOME
rm -rf $HOME/.task_tracker

cd ../..
sudo rm -rf bin/task-tracker
echo "Task Tracker is successfully uninstalled"

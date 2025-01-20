#!/usr/bin/bash

curr_dir=$(pwd)
folder_name=.task_tracker

mkdir $HOME/$folder_name

dest_path=$HOME/$folder_name

cp -r modules $dest_path
cp -r settings $dest_path
cp main.py $dest_path
cp uninstall.sh $dest_path

mv $dest_path/main.py $dest_path/main
chmod +x $dest_path/main
chmod +x $dest_path/modules/
mv $dest_path/uninstall.sh $dest_path/uninstall
chmod +x $dest_path/uninstall

cd $HOME
cd ../..
main_path=$(pwd)

sudo mv $dest_path/main $main_path/bin/task-tracker

echo "Task Tracker installed successfully!"
echo "Use task-tracker [flags] to use."
echo "Note: For help [task-tracker -h]"

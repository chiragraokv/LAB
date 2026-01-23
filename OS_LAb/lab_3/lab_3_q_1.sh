#!/bin/bash

echo "enter the path to the file"
read file_path

if [ -f "$file_path" ]; then
    echo "$file_path is a normal file"
else
    echo "not a normal file"
fi

echo "end"

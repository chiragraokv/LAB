#!/bin/bash
echo "enter the folder name"
read folder
cd $folder 
find -type f -name "*.txt" | while read file
    do 
        echo "$file is being renamed"
        new_file_name="${file%.txt}.text"
        mv "$file" "$new_file_name"
    done
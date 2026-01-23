#!/bin/bash
echo "enter extension"
read ext
 
echo "enter destination folder name"
read dest

mkdir -p "$dest"

find -type f -name "*.$ext" | while read file
do 
    echo "current file $file"
    cp "$file" "$dest/"
done
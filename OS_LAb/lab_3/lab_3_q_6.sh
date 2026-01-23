#!/bin/bash
echo "Enter the filename:"
read file

if [ ! -f "$file" ]; then
    echo "File not found!"
    exit 1
fi
sed '2~2d' "$file" > temp.txt
mv temp.txt "$file"
echo "Even-numbered lines deleted from $file"

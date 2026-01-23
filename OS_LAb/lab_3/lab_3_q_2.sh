!#/bin/sh
echo "enter the folder path"
read folder
echo "enter the string to  search for "
read search
for file in "$folder"/*;do
	if [ -f "$file" ]; then
		if grep -q "$word" "$file"; then
            echo "Found in: $file"
        fi
	else
		echo "$file not a normal file"
	fi
done 












































































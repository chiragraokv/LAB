#!/bin/bash
echo "base salary ans ta"
read base ta
salary=$(echo "$base+$ta+(0.1*$base)" | bc)
echo "final salary $salary"


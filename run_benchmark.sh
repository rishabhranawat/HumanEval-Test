#!/bin/bash

# Check if at least one argument is provided
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <filename>"
    exit 1
fi

# Assign the argument to a variable
input_file1=$1

# Define the second file statically (you can also parameterize this if needed)
input_file2="evaluate_base.py"

# Output file
output_file="evaluate.py"

# Merge the files
cat "$input_file1" "$input_file2" > "$output_file"

# Execute the merged Python script
python "$output_file"

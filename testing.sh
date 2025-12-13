#!/bin/bash

# Check results from `make-sub-scripts.py`

# Usage: ./testing.sh /path/to/comp/directory
#  --> for class proj tests, /path/to = test-dir

compdir="$1"
ex_dir="example"
numsame=0

# directory exist? 
if [ ! -d "$compdir" ]; then
	echo "Directory does not exist: $compdir"
	exit 1
fi 

echo "Checking .fits.gz files ..."

for file in "$ex_dir"/*.fits.gz; do
	fname=$(basename "$file")
	filecomp="$compdir/$fname"

	if [ ! -f "$filecomp" ]; then
		echo "No file named $fname in comparison directory"
		continue
	fi 

	for file2 in "$compdir"/*.fits.gz; do
		if cmp -s "$file" "$file2"; then
			echo "Identical files: $file in $ex_dir and $file2 in $compdir"
			((numsame++))
		fi
	done
done 

echo "Total identical .fits.gz files: $numsame"

echo "Checking .root files ..."

for file in "$ex_dir"/*.root; do
        fname=$(basename "$file")
        filecomp="$compdir/$fname"

        if [ ! -f "$filecomp" ]; then
                echo "No file named $fname in comparison directory"
                continue
        fi

        for file2 in "$compdir"/*.root; do
                if cmp -s "$file" "$file2"; then
                        echo "Identical files: $file in $ex_dir and $file2 in $compdir"
                        ((numsame++))
                fi
        done
done

echo "Total identical .root files: $numsame"

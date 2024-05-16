#!/bin/bash

export PATH=$PATH:/usr/local/bin:/usr/bin:/bin  # Adjust as needed

YEAR=$1
DAY=$2
FILE_PATH="$HOME/AOC/${YEAR}/data/${DAY}.txt"

if test -f "${FILE_PATH}"; then
    echo "File exists"
else
    echo "File does not exist"
    mkdir -p "$(dirname "${FILE_PATH}")"  # Ensure the directory exists
    touch "${FILE_PATH}"  # Create the file
    python3 request_input.py $YEAR $DAY > $FILE_PATH
fi


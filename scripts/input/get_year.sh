#!/bin/bash

export PATH=$PATH:/usr/local/bin:/usr/bin:/bin

YEAR=$1

for i in {1..25}
do
    ./get_day.sh $YEAR $i
    echo "AOC $YEAR DAY $i WRITTEN TO FOLDER"
done

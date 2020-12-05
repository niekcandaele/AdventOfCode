#!/bin/bash

# yes, I'm seriously too lazy to create 3 files by hand

if [ $# -eq 0 ]; then
    echo "No arguments supplied"
    exit 1
fi

if ! [[ "$1" =~ ^[0-9]+$ ]]; then
    echo "Sorry integers only"
    exit 1
fi


DAY="$1"


mkdir challenges/$DAY
touch challenges/$DAY/challenge.md
touch challenges/$DAY/index.py
touch challenges/$DAY/input.txt
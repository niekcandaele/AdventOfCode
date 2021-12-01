#!/bin/bash

# yes, I'm seriously too lazy to create these files by hand

DAY="$1"
YEAR=`date +%Y`

get_input() {
    # Credit: https://github.com/Bruception/advent-of-code-2020/blob/master/get_input.sh
    cookies=`cat .cookies`
    printf '%s' "`curl -H "cookie: $cookies" https://adventofcode.com/$YEAR/day/$DAY/input`" > challenges/$YEAR/$DAY/input.txt
}

if [ $# -eq 0 ]; then
    echo "No arguments supplied"
    exit 1
fi

if ! [[ "$1" =~ ^[0-9]+$ ]]; then
    echo "Sorry integers only"
    exit 1
fi


printf "Creating files for day $DAY\n"
mkdir challenges/$YEAR/$DAY
cp -r challenges/template/* challenges/$YEAR/$DAY

printf "Getting input for day $DAY...\n"
get_input

printf "Happy hacking!"


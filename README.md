
# Advent of Code 2020

https://adventofcode.com/2020

I use this repo to learn some Python by practicing. I started off with Javascript but by day 4 I realized I was not learning anything new, so I switched to a language I hadn't worked with too much, Python. I make it a point to not go back to past days and refactor so I can see the progress I made throughout the month. eg, on day 8 I added template files with support for tests. From this day on, I switched from just running the files to TDD.


## My usage

When starting a new challenge, run the `createDay.sh` script to copy the challenge template to a new folder.

For the script to fetch your input automatically, make sure you have a file called `.cookies` that contains your AoC session cookie (Should look something like `session=123456789`). otherwise, from the AoC site, get the real input and add it to input.txt

Every challenge has had a smaller input with expected outcomes, use these for smallinput.txt and in the tests.

To run the tests:

```sh
python3 -m unittest challenges/0/test.py

# Or, the poor mans watch mode for TDD:
watch python3 -m unittest challenges/0/test.py
```


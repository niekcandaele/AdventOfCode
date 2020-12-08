https://adventofcode.com/2020

Practicing stuff...


## My usage

When starting a new challenge, run the `createDay.sh` script to copy the challenge templates to a new folder.

From the AoC site, get the real input and add it to input.txt
Every challenge has had a smaller input with expected outcomes, use these for smallinput.txt and in the tests.

To run the tests:

```sh
python3 -m unittest challenges/0/test.py

# Or, the poor mans watch mode for TDD:
watch python3 -m unittest challenges/0/test.py
```
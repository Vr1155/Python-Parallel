#!/usr/bin/python3

from sys import stdout, stderr

# we can also specify where 
# we want to the output of print statement to go to:
print(f"1. Whatever you say...", file=stdout)
print(f"2. Nothing to say... ", file=stderr)

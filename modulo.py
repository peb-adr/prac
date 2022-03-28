#!/bin/python3

import core

args = core.read_args(2)
for i in range(len(args)):
    if not args[i].isdigit():
        print(f"{args[i]} must be a whole number")
        exit(1)
    args[i] = int(args[i])

rem, div = args

while rem >= div:
    rem -= div

print(rem)

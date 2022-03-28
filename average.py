#!/bin/python3

import core

l = core.read_file_to_list()
numbers = []

for n in l:
    if n.isnumeric():
        numbers.append(float(n))

if len(numbers) == 0:
    print("no numbers read")
    exit (1)

average = sum(numbers) / len(numbers)
print(average)

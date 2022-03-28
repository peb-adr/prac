#!/bin/python3

import core

l = core.read_file_to_list()

vowels = ['a', 'e', 'i', 'o', 'u']
count = 0

for line in l:
    for char in line:
        if char in vowels:
            count += 1

print(f"counted {count} vowels.")

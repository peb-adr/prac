#!/bin/python3

import os.path
import sys

DEFAULT_INPUT_FILE = "input.txt"
DEFAULT_OUTPUT_FILE = "output.txt"

def read_args(c):
    if len(sys.argv) != c+1:
        print(f"expected {c} arguments")
        exit(1)

    return sys.argv[1:c+1]

def read_file_to_list():
    ifile = DEFAULT_INPUT_FILE
    if len(sys.argv) > 1:
        ifile = sys.argv[1]
    if not os.path.exists(ifile):
        print(f"file {ifile} does not exist")
        exit(1)

    l = []
    with open(ifile, 'r') as f:
        for line in f:
            l.append(line.strip())

    return l

def write_list_to_file(l):
    ofile = DEFAULT_OUTPUT_FILE

    with open(ofile, 'w') as f:
        for line in l:
            f.write(f"{line}\n")

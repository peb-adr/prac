#!/bin/python3

import core

secret="secret"
hide_str="XXX"

l = core.read_file_to_list()

for i in range(len(l)):
    l[i] = l[i].replace(secret, hide_str)

core.write_list_to_file(l)

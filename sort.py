#!/bin/python3

import core

l = core.read_file_to_list()

l.sort()

core.write_list_to_file(l)

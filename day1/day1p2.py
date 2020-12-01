#!/usr/bin/env python
from itertools import combinations


input_file = open("input.txt", "r")
if input_file.mode == 'r':
    lines = input_file.readlines()
    for x,y,z in combinations(lines, 3):
        if int(x) + int(y) + int(z) == 2020:
            print (int(x) * int(y) * int(z))
exit()
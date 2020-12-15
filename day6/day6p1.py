#!/usr/bin/env python

boardingList = set()

total = 0

input_file = open("input.txt", "r")
if input_file.mode == 'r':
    lines = input_file.read().split("\n\n")
    for line in lines:    
        foo = "".join(set(line.replace("\n", "")))
        total += len(foo)
    print(total)

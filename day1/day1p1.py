#!/usr/bin/env python

map = {}

input_file = open("input.txt", "r")
if input_file.mode == 'r':
    lines = input_file.readlines()
    for x in lines:
        x = int(x)
        if map.get(x) is not None: 
            print(map[x])
        y = 2020 - x
        map[y] = x*y

exit()
#!/usr/bin/env python

count = 0
x = 0

input_file = open("input.txt", "r")
if input_file.mode == 'r':
    lines = input_file.readlines()
    for line in lines:
        if x >= len(line)-1:
            x -=len(line)-1
        if line[x] == '#':    
            count += 1
        x +=3
    print(count)

exit()
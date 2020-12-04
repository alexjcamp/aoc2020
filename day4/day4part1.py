#!/usr/bin/env python
import re


count = 0

input_file = open("input.txt", "r")
if input_file.mode == 'r':
    lines = input_file.read().split("\n\n")

    for line in lines:
        x = len(line.split())
        z = line.find("cid")
        if(x == 8):
            count += 1
        if(x==7 and z==-1):
            count += 1
    print(count)
    
exit()
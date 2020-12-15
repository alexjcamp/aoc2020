#!/usr/bin/env python

boardingList = set()

i = 256 * 8

input_file = open("input.txt", "r")
if input_file.mode == 'r':
    lines = input_file.read().split()
    for line in lines:
        line = line.replace('F', '0')
        line = line.replace('B', '1')
        line = line.replace('L', '0')
        line = line.replace('R', '1')
        num = int(line, 2)
        boardingList.add(num)    
    while i != 0:
        if i not in boardingList and i+1 in boardingList and i-1 in boardingList:
            print(i)
            exit()
        i -= 1  

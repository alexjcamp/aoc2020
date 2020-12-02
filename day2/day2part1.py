#!/usr/bin/env python

count = 0

input_file = open("input.text", "r")
if input_file.mode == 'r':
    lines = input_file.readlines()
    
    for x in lines:
        line = x.split()
        rang = line[0].split('-')
        minimum = int(rang[0])
        maximum = int(rang[1])
        total = line[2].count(line[1][0])
        if(minimum <= total and total <= maximum):
            count = count + 1
        
    print(count)

exit()
#!/usr/bin/env python

count = 0

input_file = open("input.text", "r")
if input_file.mode == 'r':
    lines = input_file.readlines()
    
    for x in lines:
        line = x.split()
        rang = line[0].split('-')
        locala = int(rang[0])-1
        localb = int(rang[1])-1
        testa = line[2][locala] == line[1][0]
        testb = line[2][localb] == line[1][0]  
        if(testa != testb):
            count = count + 1
        total = line[2].count(line[1][0])
    print(count)

exit()
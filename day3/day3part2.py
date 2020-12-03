#!/usr/bin/env python



def slope(down, right, hill):
    count = 0
    x = right
    y = down
    bottom = len(hill)
    width = len(hill[0])
    while y < bottom:    
        if lines[y][x%width] == '#':    
            count += 1
        x += right
        y += down
    return count
         

input_file = open("input.txt", "r")
if input_file.mode == 'r':
    lines = input_file.read().split()
    a = slope(1,1,lines)
    print(a)
    b = slope(1,3,lines)
    print(b)
    c = slope(1,5,lines)
    print(c)
    d = slope(1,7,lines)
    print(d)
    e = slope(2,1,lines)
    print(e)
    print(a*b*c*d*e)

exit()
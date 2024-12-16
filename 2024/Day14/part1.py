#!/usr/bin/env python3

from sys import argv
file = open(argv[1], 'r').readlines()
import re
def mid(n):
    return (n -  (n % 2) )/2

max_x = 101 # numbers from the question
max_y = 103
mid_x = mid(max_x)
mid_y = mid(max_y)

top_left, bottom_left, top_right, bottom_right = 0,0,0,0
for line in file:
    result = re.search('p=([-\\d]+),([-\\d]+) v=([-\\d]+),([-\\d]+)' , line)
    if result:
        p = [ int(result.group(1)), int(result.group(2)) ]
        v = [ int(result.group(3)), int(result.group(4)) ]
        final = [ p[0] + 100*v[0] , p[1] + 100*v[1] ]

        final[0] = final[0] % max_x 
        final[1] = final[1] % max_y 

        if 0 <= final[0] < mid_x:
            if 0 <= final[1] < mid_y:
                top_left += 1
            if mid_y < final[1] <= max_y:
                bottom_left += 1

        elif mid_x < final[0] <= max_x: 
            if mid_y < final[1] <= max_y:
                top_right += 1
            if 0 <= final[1] < mid_y:
                bottom_right += 1

print(top_left* bottom_left* top_right* bottom_right)
        


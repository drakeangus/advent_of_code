#!/bin/python3

import sys
from collections import defaultdict
import re
import math


lines = (sys.stdin).read().split("\n\n")

direction = lines[0]
theMap = lines[1].split("\n")[:-1]

#currentLoc = ['AAA', 'MGA']
currentLoc=[]

mapDict=defaultdict(list)
for step in theMap:
    result = re.search(r"([A-Z0-9]*) = \(([A-Z0-9]*), ([A-Z0-9]*)\)", step)
    key, leftVal, rightVal = result.group(1, 2, 3)
#    print(f"{key} -> {leftVal}, {rightVal}")
    mapDict[key] = (leftVal, rightVal)

    # Grab all the keys ending with A
    if key[2] == "A":
        print(f"Valid key : {key}")
        currentLoc.append(key)
    

print(f"currentLoc = {currentLoc}")

def LeftOrRight(char):
    if char == "L":
        return 0
    return 1

def isAllAtEnd(currentLoc):
    global totalSteps
    for l in currentLoc:
        if l[2] != "Z":
            return False
    return True


# Here we're looking to find the number of steps it takes to go from a key ending in Z back to the same position
# ie A -> B -> Z -> C
#         ^         v
#         F <- E <- D
# takes 6 steps to loop
# However we also have the requirement that we are in the same position in the direction map (RRLLRRLLL...) which we check with the count variable
# Hense why we count the (key, count) pairs

# then we find the lowest common multiple of each loop


loop_lengths=list()  
for key in currentLoc:
    keyCount=defaultdict(int)
    bLoop = True
    count = 0
    total_steps = 0
    first=True
    while bLoop:
        if count == len(direction):
            count = 0
        key = mapDict[key][LeftOrRight(direction[count])]
        if key[2] == 'Z':
            if first:
                total_steps = 0
                first=False
            if keyCount[(key, count)] == 0:
                keyCount[(key, count)] += 1
            else:
                print((key, count), f" Total steps {total_steps}")
                bLoop = False
        total_steps += 1
        count += 1
    loop_lengths.append(total_steps-1)

print(math.lcm(*loop_lengths))


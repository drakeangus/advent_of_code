#!/bin/python3

import sys
from collections import defaultdict
import re


lines = (sys.stdin).read().split("\n\n")

direction = lines[0]
theMap = lines[1].split("\n")[:-1]

#currentLoc = theMap[0].split(" = ")[0]
currentLoc = ['AAA', 'MGA']
print(currentLoc)

mapDict=defaultdict(list)
for step in theMap:
    result = re.search(r"([A-Z0-9]*) = \(([A-Z0-9]*), ([A-Z0-9]*)\)", step)
    key, leftVal, rightVal = result.group(1, 2, 3)
#    print(f"{key} -> {leftVal}, {rightVal}")
    mapDict[key] = (leftVal, rightVal)

    # Grab all the keys ending with A
    '''if key[2] == "A":
        print(f"Valid key : {key}")
        currentLoc.append(key)
    '''

print(f"currentLoc = {currentLoc}")

def LeftOrRight(char):
    if char == "L":
        return 0
    return 1

def isAllAtEnd(currentLoc):
    for l in currentLoc:
        if l[2] != "Z":
            return False
    return True

#countKeysDict=defaultdict(int)

count=0
totalSteps=0
while (not isAllAtEnd(currentLoc)):
    if count == len(direction):
        count = 0
    for l in range(0,len(currentLoc)):
#        print(f"Current: {currentLoc[l]}, Going {direction[count]}")
        currentLoc[l] = mapDict[currentLoc[l]][LeftOrRight(direction[count])]
#    print("---")
    '''
    countKeysDict[currentLoc[l]]+=1
    max_key=""
    max_key_count=0
    for n,m in countKeysDict.items():
        if m>max_key_count:
            max_key_count = m
            max_key = n
    '''
    count+=1
    totalSteps+=1
    #print(f"Key: {max_key}, Count {max_key_count}")
print(f"Total steps: {totalSteps}")

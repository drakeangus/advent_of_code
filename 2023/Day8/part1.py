#!/bin/python3

import sys
from collections import defaultdict
import re


lines = (sys.stdin).read().split("\n\n")

direction = lines[0]
theMap = lines[1].split("\n")[:-1]
#currentLoc = theMap[0].split(" = ")[0]
currentLoc = "AAA"

mapDict=defaultdict(list)
for step in theMap:
    result = re.search(r"([A-Z]*) = \(([A-Z]*), ([A-Z]*)\)", step)
    key, leftVal, rightVal = result.group(1, 2, 3)
    print(f"{key} -> {leftVal}, {rightVal}")
    mapDict[key] = (leftVal, rightVal)

def LeftOrRight(char):
    if char == "L":
        return 0
    return 1

count=0
totalSteps=0
while True:
    if count == len(direction):
        count = 0
    #print(f"Current: {currentLoc}, Going {direction[count]}")
    currentLoc = mapDict[currentLoc][LeftOrRight(direction[count])]  
    count+=1
    totalSteps+=1
    if currentLoc == "ZZZ":
        #print("At ZZZ")
        break;
print(f"Total steps: {totalSteps}")

#!/bin/python3.10
import sys    
from collections import defaultdict
    
lines = (sys.stdin).read().strip().split('\n')    
matrix = [[char for char in line] for line in lines]
R = len(lines)
C = len(matrix[0])

gearDict=defaultdict(list)

nRow=-1
for row in matrix:
    gearCurrent=set()
    nRow+=1
    nCol=-1
    num_found = False
    num=0
    for char in row:
        nCol+=1
        if char.isdigit():
            num_found = True
            num = 10*num + int(char)
            for i in [-1,0,1]:
                for j in [-1,0,1]:
                    if (R > nRow+i >= 0) and (C > nCol+j >= 0):
                        if matrix[nRow+i][nCol+j] == "*":
                            if (nRow+i, nCol+j) not in gearCurrent:
                                gearCurrent.add((nRow+i, nCol+j))
        if not char.isdigit() or nCol == C-1:
            if num_found:
                print(num)
                for gear in gearCurrent:
                    print(gear)
                    gearDict[gear].append(num)
                gearCurrent=set()
            num_found = False
            num=0

print(gearDict)

# So our gearDict is a map of set() -> list
# the set is a pair of numbers ie the location of a gear in the matrix (3,5)
# the list contains the numbers next to each gear

sum=0
for n,m in gearDict.items():
    product = 0
    if len(m) == 2:
        print(f"Gear {n} has two nums: {m}")
        product = m[0] * m[1]
        sum += product
print(sum)

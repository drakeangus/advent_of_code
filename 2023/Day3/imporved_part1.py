#!/bin/python3.10


import sys

lines = (sys.stdin).read().strip().split('\n')
matrix = [[char for char in line] for line in lines]


def AddToSum(num):
    global answer
    answer += num


def IsAdjacent(nRow, nCol):
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            try:
                cell = matrix[nRow+i][nCol+j]
                if not cell.isdigit() and cell != '.':
                    return True
            except IndexError:
                continue
    return False

answer=0
nRow=-1
for row in matrix:
    nRow+=1
    num = 0
    num_found = False
    nCol=-1
    shouldCount = False
    for char in row:
        nCol+=1
        if char.isdigit():
            if IsAdjacent(nRow, nCol):
                shouldCount = True
            num_found = True
            num = 10*num + int(char)
        elif num_found:
            if shouldCount:
                AddToSum(num)
            shouldCount = False
            num_found = False
            print(num)
            num = 0
        
    if num_found and shouldCount: #for the numbers ending on the row end
        AddToSum(num)

print(matrix)
print(answer)

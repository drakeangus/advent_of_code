#!/bin/python3.10
import sys    
    
lines = (sys.stdin).read().strip().split('\n')    
#matrix = [[char for char in line] for line in lines]
R = len(lines[0])

class Cell:
    def __init__(self, letter, leader):
        self.letter = letter
        self.leader = leader

def GetNumberFromLeader(leader):
    global matrix
    row=leader[0]
    col=leader[1]
    char = matrix[row][col].letter
    number = int(char)
    while col < R:
        print(number)
        col+=1
        if col >= len(matrix[0]):
            return number
        char = matrix[row][col].letter
        if not char.isdigit():
            return number
        number = number*10 +int(char)


matrix=[]
nRow=-1
for row in lines:
    nRow+=1
    nCol=-1
    column=[]
    isLeader = True
    leader=[]
    for char in row:
        nCol+=1
        if char.isdigit() and isLeader:
            leader = [nRow, nCol]
            isLeader = False
        elif not char.isdigit():
            isLeader = True
            leader=[]

        column.append(Cell(char, leader))
    matrix.append(column)

nRow=-1
answer=0
for row in matrix:
    nRow+=1
    nCol=-1
    leader_list=[]
    for cell in row:
        nCol+=1
        if cell.letter == "*":
            for i in [-1,0,1]:
                if (nRow+i < 0) or (nRow+i >= len(matrix)):
                    continue
                for j in [-1,0,1]:
                    if (nCol+j < 0) or (nCol+j >= R):
                        continue
                    if  matrix[nRow+i][nCol+j].leader not in leader_list and matrix[nRow+i][nCol+j].leader != []:
                        leader_list.append(matrix[nRow+i][nCol+j].leader)
            if len(leader_list) == 2:
                print(leader_list)
                product=1
                for leader in leader_list:
                    print(leader)
                    #print(GetNumberFromLeader(leader))
                    product *= GetNumberFromLeader(leader)
                #print(product)
                answer+=product


print(answer)            




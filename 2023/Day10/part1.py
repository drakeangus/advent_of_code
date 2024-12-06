#!/bin/python3.10
import sys

if len(sys.argv) == 2:
    file_name = sys.argv[1]
else:
    file_name = 'example.txt'

file = (open(file_name, 'r')).read().strip().split('\n')

#matrix = [[char for char in line] for line in file]

matrix=[]
for i, line in enumerate(file):
    L=[]
    for j, char in enumerate(line):
        L.append(char)
        if char == 'S':
            start_loc = (i,j)
    matrix.append(L)

print(matrix)
print(f"Start : {start_loc}")

sp = 'S' # Start Position
g = '.'  # Ground (no direction)
ne = 'L' # North <> East
ns = '|' # North <> South   
nw = 'J' # North <> West
se = 'F' # South <> East
sw = '7' # South <> West
we = '-' # West <> East
class Node:
    def SetConnections(self, type, loc):    
        self.north = None
        self.south = None 
        self.east = None
        self.west = None
        
        if type == ne:
            self.north = (loc[0] - 1, loc[1])
            self.east = (loc[0], loc[1] + 1)
        elif type == ns:
            self.north = (loc[0] - 1, loc[1])
            self.south = (loc[0] + 1, loc[1])
        elif type == nw:
            self.north = (loc[0] - 1, loc[1])
            self.west = (loc[0], loc[1]-1)
        elif type == se:
            self.south = (loc[0] + 1, loc[1])
            self.east = (loc[0], loc[1] + 1)
        elif type == sw:
            self.south = (loc[0] + 1, loc[1])
            self.west = (loc[0], loc[1]-1)
        elif type == we:
            self.west = (loc[0], loc[1]-1)
            self.east = (loc[0], loc[1] + 1)
        elif type == sp:
            self.north = (loc[0] - 1, loc[1])
            self.east = (loc[0], loc[1] + 1)
            self.south = (loc[0] + 1, loc[1])
            self.west = (loc[0], loc[1]-1)
    
    def __init__(self, loc, type, step):
        self.loc = loc
        self.type = type
        self.step = step
        self.SetConnections(type, loc)
        if matrix[self.north[0]][self.north[1]] in [ns, se, sw]:
            print("North valid")
        else:
            self.north = None
        
        if matrix[self.east[0]][self.east[1]] in [nw, sw, we]:
            print("East Valid")
        else:
            self.east = None

        if matrix[self.south[0]][self.south[1]] in [nw, ne, ns]:
            print("South Valid")
        else:
            self.east = None

        if matrix[self.west[0]][self.west[1]] in [ne, se, we]:
            print("West Valid")
        else:
            self.east = None

        for conn in [self.north, self.east, self.south, self.west]:
            if conn != None:
                print(f"{conn} Valid move")
                Node(conn, matrix[conn[0]][conn[1]], 0)

Node(start_loc, matrix[start_loc[0]][start_loc[1]], 0)

        

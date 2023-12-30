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
print(start_loc)

class Node:
    def SetConnections(self, type, loc):    
        sp = 'S' # Start Position
        g = '.'  # Ground (no direction)
        ne = 'L' # North <> East
        ns = '|' # North <> South   
        nw = 'J' # North <> West
        se = 'F' # South <> East
        sw = '7' # South <> West
        we = '-' # West <> East
        self.north = None
        self.south = None 
        self.east = None
        self.west = None
        
        if type == ne:
            self.north = (loc[0] - 1, loc[1])
            self.east = (loc[0], loc[1] + 1)
        elif type == ns:
            self.north = loc[0] - 1
            self.south = loc[0] + 1
        elif type == nw:
            self.north = loc[0] - 1
            self.west = loc[1] - 1
        elif type == se:
            self.south = loc[0] + 1
            self.east = loc[1] + 1
        elif type == sw:
            self.south = loc[0] + 1
            self.west = loc[1] - 1
        elif type == we:
            self.west = loc[1] - 1
            self.east = loc[1] + 1
        elif type == sp:
            self.north = loc[0] - 1
            self.east = loc[1] + 1
            self.south = loc[0] + 1
            self.west = loc[1] - 1
    
    def __init__(self, loc, type, step):
        self.loc = loc
        self.type = type
        self.step = step
        self.SetConnections(type, loc)
        for conn in [self.north, self.east, self.south, self.west]:
            print(conn)

Node(start_loc, 'L', 0)

        

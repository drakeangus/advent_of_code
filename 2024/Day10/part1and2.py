#!/usr/bin/env python3
from sys import argv
file = open(argv[1], 'r').readlines()


class Node:
    global map
    global max_x
    global max_y

    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)
        self.number = int(map[y][x])

    def connect(self) -> set:
        global PART_2_COUNT
        connected_ends = set()
        #print(f"{self.x,self.y} -> {self.number} connects to:")
        if self.number == 9:
            PART_2_COUNT += 1
            connected_ends.add(tuple((self.x, self.y)))
            return connected_ends

        self.connections = list() # [ north, east, south, west ]
        if self.y > 0:
            north = Node(self.x, self.y-1)
            if north.number == self.number + 1:
                self.connections.append(north)
        
        if self.x < max_x - 1:
            east = Node(self.x+1, self.y)
            if east.number == self.number + 1:
                self.connections.append(east)
        
        if self.y < max_y - 1 :
            south = Node(self.x, self.y+1)
            if south.number == self.number + 1:
                self.connections.append(south)

        if self.x > 0:
            west = Node(self.x-1, self.y)
            if west.number == self.number + 1:
                self.connections.append(west)

        for connection in self.connections:
            connected_ends.update(connection.connect())
        return connected_ends

start_points = set()
map = list()
for y,line in enumerate(file):
    row = list()
    for x,number in enumerate(line.strip()):
        row.append(number)
        if int(number) == 0:
            start_points.add(tuple((x,y)))
    map.append(row)

max_x, max_y= len(map[0]), len(map)

PART_1_COUNT=0
PART_2_COUNT = 0
for x,y in start_points:
    connected_ends = set()
    start_node = Node(x,y)
    connected_ends.update(start_node.connect())
    PART_1_COUNT += len(connected_ends)
print(f"{PART_1_COUNT = }")
print(f"{PART_2_COUNT = }")


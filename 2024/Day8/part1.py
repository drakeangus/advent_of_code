#!/usr/bin/env python3 
from sys import argv
file = open(argv[1], 'r').readlines()
map = list()
from collections import defaultdict
letter_locations = defaultdict(list)
for y,line in enumerate(file):
    current_line = list()
    for x,character in enumerate(line.strip()):
        current_line.append(character)
        if character != ".":
            letter_locations[character].append((x,y))
    map.append(current_line)

max_y, max_x = len(map)-1, len(map[0])-1

import numpy as np
def GetNodes(coord_a, coords) -> list:
    nodes = list()
    A = np.array(coord_a)
    for coord_b in coords:
        if coord_a == coord_b:
            continue
        B = np.array(coord_b)
        C = (2 * B - A)
        nodes.append(tuple(C))
    return nodes

def IsNodeInBounds(node):
    global map
    if 0 > node[0] or node[0] > max_x:
        return False
    if 0 > node[1] or node[1] > max_y:
        return False
    if map[node[1]][node[0]] == "#":
        return False
    
    map[node[1]][node[0]] = "#"
    return True

count = 0
for letter,coords in letter_locations.items():
    for coord in coords:
        #print(f"{letter} : {coord}")
        for node in GetNodes(coord, coords):
            if IsNodeInBounds(node):
                count += 1

for line in map:
    for cell in line:
        print(cell, end="")
    print()

print(f"Count : {count}")

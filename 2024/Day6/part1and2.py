#!/usr/bin/env python3 
import numpy as np
from collections import defaultdict
from sys import argv
file = open(argv[1], 'r').readlines()


class Position:
    def __init__(self, x, y):

        self.current_x = x
        self.current_y = y
        self.start_pos = (self.current_x, self.current_y)
        self.direction = [0,-1]
        self.path = defaultdict(list)
        self.path[self.start_pos].append(self.direction)
        #print(f"Start: {(self.current_x, self.current_y)}")

    def step_forward(self):
        self.current_x += self.direction[0]
        self.current_y += self.direction[1]
        for direc in self.path[(self.current_x, self.current_y)]:
            if self.direction[0] == direc[0] and self.direction[1] == direc[1]:
                return False # i.e same place same direction
        self.path[(self.current_x, self.current_y)].append(self.direction)
        #print(f"New location: {(self.current_x, self.current_y)}")
        return True

    def turn_right(self):
        self.direction = np.dot(self.direction, ((0, 1), (-1,0)))
        #print(f"Turn Right: {self.direction}")


def PrintMap(map):
    for row in map:
        for cell in row:
            print(cell, end="")
        print()

map=list()   # this map is backwards, its map[y][x] 
for j,line in enumerate(file):                     # j : rows
    line_list=list()
    for i,letter in enumerate(line.strip()):       # i : columns
        line_list.append(letter)
        if letter == "^":
            position = Position(i,j)
    map.append(line_list)

loop_count=0
def NextStep(position, current_map):
    global loop_count
    forward_step = (
            position.current_x + position.direction[0], 
            position.current_y + position.direction[1]
            )
    if forward_step[0] < 0 or forward_step[0] >= len(current_map[0]):
        return False
    if forward_step[1] < 0 or forward_step[1] >= len(current_map):
        return False
    
    if current_map[forward_step[1]][forward_step[0]] == "#":
        position.turn_right()
    else:
        if not position.step_forward(): # False means we've been here going in this direction before
            loop_count+=1
            return False
    return True


### PART 1 ###
# generate list of all distinct positions
# for part two I re-run the program with an obsicle in each of the distinct positions and count if it leads to an infinite loop

while NextStep(position, map):
    continue

distinct_positions = len(position.path)
print(f"Distinct positions (part 1): {distinct_positions}")


### PART 2 ###

possible_obs = [ key for key in position.path.keys() ] 

from copy import deepcopy
for n,obj_test in enumerate(possible_obs):
    #print(f"{obj_test} : {n}/{distinct_positions}")
    test_position = Position(position.start_pos[0], position.start_pos[1])
    if obj_test == position.start_pos:
        continue
    map_copy = deepcopy(map)
    map_copy[obj_test[1]][obj_test[0]] = "#"
    
    
    while NextStep(test_position, map_copy):
        continue


print(f"Loop Count: {loop_count}")

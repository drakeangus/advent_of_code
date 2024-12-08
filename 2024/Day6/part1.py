#!/usr/bin/env python3 
import numpy as np
from collections import defaultdict
from sys import argv
file = open(argv[1], 'r').readlines()


class Position:
    path = defaultdict(int)
    def __init__(self, x, y):
        self.current_x = x
        self.current_y = y
        self.path[(self.current_x, self.current_y)] = 1
        self.direction = [0,-1]
        #print(f"Start: {(self.current_x, self.current_y)}")

    def step_forward(self):
        self.current_x += self.direction[0]
        self.current_y += self.direction[1]
        self.path[(self.current_x, self.current_y)] += 1
        #print(f"New location: {(self.current_x, self.current_y)}")

    def turn_right(self):
        self.direction = np.dot(self.direction, ((0, 1), (-1,0)))
        #print(f"Turn Right: {self.direction}")




map=list()   # this map is backwards, its map[y][x] 
for j,line in enumerate(file):                     # j : rows
    line_list=list()
    for i,letter in enumerate(line.strip()):       # i : columns
        line_list.append(letter)
        if letter == "^":
            position = Position(i,j)
    map.append(line_list)



def NextStep(position):
    forward_step = (
            position.current_x + position.direction[0], 
            position.current_y + position.direction[1]
            )
    if forward_step[0] < 0 or forward_step[0] >= len(map[0]):
        return False
    if forward_step[1] < 0 or forward_step[1] >= len(map):
        return False

    if map[forward_step[1]][forward_step[0]] == "#":
        position.turn_right()
    else:
        position.step_forward()
    return True


while NextStep(position):
    continue

print(f"Distinct positions: {len(position.path)}")


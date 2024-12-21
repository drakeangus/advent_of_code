#!/usr/bin/env python3
from sys import argv
import numpy as np
file = open(argv[1], 'r').readlines()

map=list()
class Robot:
    x = int()
    y = int()
    
robot=Robot()

bReadMap = True
for x,line in enumerate(file):
    line = line.strip()
    if line == "":
        bReadMap = False
        continue

    if bReadMap:
        row = list()
        for y,char in enumerate(line):
            row.append(char)
            if char == "@":
                robot.x = x
                robot.y = y
        if len(row) > 0:
            map.append(row)
    else:
        move_instructions += line




def UpdateRobotCoords():
    global robot
    for y,row in enumerate(map):
        for x,char in enumerate(row):
            if char == "@":
                robot.x = x
                robot.y = y

def MoveRobot():
    global robot
    global map
    line = np.array(map[robot.y][:])
    for index in range(robot.x, len(line)):
        if line[index] == "#":
            return False
        if line[index] == ".":
            line = np.delete(line, index)
            line = np.insert(line, robot.x, ".")
            map[robot.y] = line
            return True
    return False

map = np.array(map)
for n,instruction in enumerate(move_instructions):
    if instruction == "<":
        # 180 degree rotation
        map = np.rot90(map, k=2, axes=(0,1))
        UpdateRobotCoords()
        MoveRobot()
        # 180 degree rotation
        map = np.rot90(map, k=2, axes=(0,1)) 
    elif instruction == "^":
        # clockwise 90 degree rotation
        map = np.rot90(map, k=1, axes=(1,0)) 
        UpdateRobotCoords()
        MoveRobot()
        # anti-clockwise 90 degree rotation
        map = np.rot90(map, k=1, axes=(0,1)) 
    elif instruction == ">": # no rotation
        UpdateRobotCoords()
        MoveRobot()
    elif instruction == "v":
        # anti-clockwise 90 degree rotation
        map = np.rot90(map, k=1, axes=(0,1))
        UpdateRobotCoords()
        MoveRobot()
        # clockwise 90 degree rotation
        map = np.rot90(map, k=1, axes=(1,0)) 
    else:
        print("borked")
   
GPS = 0
for n,row in enumerate(map):
    #print(''.join(row))
    for m,char in enumerate(row):
        if char == "O":
            GPS += (100 * n) + m
print(f"{GPS = }")

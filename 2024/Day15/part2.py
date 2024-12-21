#!/usr/bin/env python3
from sys import argv
file = open(argv[1], 'r').readlines()

map=list()
class Robot:
    x = int()
    y = int()

    def VerticledateRobotCoords(self):
        global map
        for y,row in enumerate(map):
            for x,char in enumerate(row):
                if char == "@":
                    self.x = x
                    self.y = y
    
robot=Robot()

move_instructions=str()
bReadMap = True
for line in file:
    line = line.strip()
    if line == "":
        bReadMap = False
        continue

    if bReadMap:
        row = list()
        for char in line:
            if char == "O":
                row.append("[")
                row.append("]")
            elif char == "#":
                row.append("#")
                row.append("#")
            else:
                row.append(char)
                row.append(".")
        if len(row) > 0:
            map.append(row)
    else:
        move_instructions += line

robot.VerticledateRobotCoords()

#for n,row in enumerate(map):
#    print(''.join(row))



def Right():
    global robot
    global map
    line = map[robot.y]
    bFirst = True
    for index in range(robot.x, len(line)):
        if line[index] == "#":
            return False
        
        if line[index] == ".":
            line.pop(index)
            line.insert(robot.x, ".")      
            map[robot.y] = line
            robot.x += 1
            return True
    return False

def Left():
    global robot
    global map
    line = map[robot.y][::-1]
    flipped_robot_x = len(line) -1 -robot.x
    for index in range(flipped_robot_x, len(line)):
        if line[index] == "#":
            return False
        if line[index] == ".":
            line.pop(index)
            line.insert(flipped_robot_x, ".")      
            map[robot.y] = line[::-1]
            robot.x -= 1
            return True
    return False


def GetMoveableObjects(robot, y) -> list:

    objects = list()
    objects.append(tuple((robot.x, robot.y)))

    for obj in objects:
        if map[obj[1] + y][obj[0]] == "#":
            return list()

        if map[obj[1]][obj[0]] == "@":
            if map[obj[1] + y][obj[0]] == ".":
                return objects

        if map[obj[1] + y][obj[0]] == "[":
            objects.append(tuple((obj[0], obj[1] + y)))
            objects.append(tuple((obj[0] +1, obj[1] + y)))
        
        if map[obj[1] + y][obj[0]] == "]":
            objects.append(tuple((obj[0], obj[1] + y)))
            objects.append(tuple((obj[0] -1, obj[1] + y)))
    
    object_set = set()
    for obj in objects:
        object_set.add(obj)
    return [item for item in object_set ]

def Verticle(direction):
    if direction == "up":
        y = -1
        from_bottom = False
    else:
        y = 1
        from_bottom = True

    global robot
    global map
    
    move_objects = GetMoveableObjects(robot, y)
    for obj in sorted(move_objects, reverse=from_bottom):
        map[obj[1] + y][obj[0]], map[obj[1]][obj[0]] = map[obj[1]][obj[0]], map[obj[1] +y][obj[0]] 
    
    if len(move_objects) > 0:
        robot.y += y



for n,instruction in enumerate(move_instructions):
    if instruction == "a" or instruction == "<":
        Left()
    elif instruction == "w" or instruction ==  "^" :
        Verticle("up")
    elif instruction ==  "d" or instruction == ">":
        Right()
    elif instruction == "s" or instruction == "v":
        Verticle("down")
    else:
        print("borked")
        continue


GPS = 0
for n,row in enumerate(map):
    #print(''.join(row))
    for m,char in enumerate(row):
        if char == "[":
            GPS += (100 * n) + m
print(f"{GPS = }")

#!/usr/bin/env python3

from sys import argv
file = open(argv[1],'r').readlines()

garden = [ [ character for character in line if character != '\n' ] for line in file ]
#print(garden)

max_x,max_y = len(garden[0]), len(garden)
class Node:
    global garden
    global visited_plots 

    # part 1
    def GetCostOfPlot(self):
        plots = 1
        perimiters = self.perimiter_sides
        for node in self.connections:
            perimiters += node.perimiter_sides 
            plots += 1
        
        return plots * perimiters


    def __init__(self, x, y):
        self.x = x
        self.y = y 
        visited_plots.add(tuple((self.x, self.y)))
        self.letter = garden[y][x]
        self.perimiter_sides = 4 
        self.corners = 4
        self.connections = self.GetConnections()


    def GetConnections(self)->set:
        connections=set()
        connected_sides = set()
        if self.y > 0:
            if garden[self.y - 1][self.x] == self.letter:
                self.perimiter_sides -= 1
                if (self.x, self.y-1) not in visited_plots:            
                    north = Node(self.x, self.y - 1) 
                    connections.add(north)
                    connections.update(north.connections)     

        if self.x < max_x-1:
            if garden[self.y][self.x + 1] == self.letter:
                self.perimiter_sides -= 1
                if (self.x+1, self.y) not in visited_plots:            
                    east = Node(self.x + 1, self.y) 
                    connections.add(east)
                    connections.update(east.connections)

        if self.y < max_y-1: 
            if garden[self.y + 1][self.x] == self.letter:
                self.perimiter_sides -= 1
                if (self.x, self.y+1) not in visited_plots:            
                    south = Node(self.x, self.y + 1) 
                    connections.add(south)
                    connections.update(south.connections)

        if self.x > 0: 
            if garden[self.y][self.x - 1] == self.letter:
                self.perimiter_sides -= 1
                if (self.x-1, self.y) not in visited_plots:            
                    west = Node(self.x - 1, self.y) 
                    connections.add(west)
                    connections.update(west.connections)

        return connections

def CountUnconnectedSides(sides, sort_axis):
    if sort_axis == "x":
        prim_axis,sec_axis = 0,1
    else:
        prim_axis,sec_axis = 1,0
    
    # for up/down sides the y axis is the primary sort axis
    # for left/right sides the x axis is the primary sort axis
    sorted_sides = sorted(sides, key=lambda k: [k[prim_axis], k[sec_axis]])
    count = len(sorted_sides)
    for i in range(1, len(sorted_sides)):
        # then we can check if two points are on the same line
        if sorted_sides[i][prim_axis] == sorted_sides[i-1][prim_axis]:
            # then if they are next to each other
            if sorted_sides[i-1][sec_axis] + 1 == sorted_sides[i][sec_axis]:
                count -= 1
    return count


def CalcNumberOfSides(plot):
    coordinate_set = set()
    coordinate_set.add(tuple((plot.x,plot.y)))
    for connection in plot.connections:
        x,y = connection.x, connection.y
        coordinate_set.add((x,y))

    left_sides = set()
    right_sides = set()
    up_sides = set()
    down_sides = set()

    for (x,y) in coordinate_set:
        if (x-1,y) not in coordinate_set:
            left_sides.add((x-1,y))

        if (x+1,y) not in coordinate_set:
            right_sides.add((x+1,y))

        if (x,y-1) not in coordinate_set:
            up_sides.add((x,y-1))

        if (x,y+1) not in coordinate_set:
            down_sides.add((x,y+1))
           
    sides = 0
    sides += CountUnconnectedSides(left_sides,'x')
    sides += CountUnconnectedSides(right_sides,'x')
    sides += CountUnconnectedSides(up_sides,'y')
    sides += CountUnconnectedSides(down_sides,'y')

    return sides

visited_plots=set()
cost = 0
for x,y in [(x,y) for y in range(max_y) for x in range(max_x)]:
    if (x,y) in visited_plots:
        continue
    plot = Node(x,y)
    #print(f"{plot.letter = }")

    units = len(plot.connections) + 1
    side_count = CalcNumberOfSides(plot)

    cost += units * side_count
print(f"{cost = }") 

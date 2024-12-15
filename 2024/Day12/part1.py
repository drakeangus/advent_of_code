#!/usr/bin/env python3

from sys import argv
file = open(argv[1],'r').readlines()

garden = [ [ character for character in line if character != '\n' ] for line in file ]

max_x,max_y = len(garden[0]), len(garden)
class Node:
    global garden
    global visited_plots 

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
        self.connections = self.GetConnections()


    def GetConnections(self)->set:
        connections=set()
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



visited_plots=set()
cost = 0
for x,y in [(x,y) for y in range(max_y) for x in range(max_x)]:
    if (x,y) in visited_plots:
        continue
    plot = Node(x,y)
    cost += plot.GetCostOfPlot()
print(f"{cost = }") 

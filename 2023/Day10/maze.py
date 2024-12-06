#!/bin/python3
import sys


start_coords=(0,0)
historic_coords=[start_coords]


class Node:
    def GetNorth(self, coords):
        return (coords[0]-1, coords[1])
    def GetEast(self, coords):
        return (coords[0], coords[1]+1)
    def GetSouth(self, coords):    
        return (coords[0]+1, coords[1])
    def GetWest(self, coords):
        return (coords[0], coords[1]-1)

    def IsConnectionValid(self, current_coords, connection_coords):
        # Connection must be to a node inside the boundary 0 -> max_boundary
        if connection_coords[0] < 0 or connection_coords[0] > max_boundary_verticle:
            return False
        if connection_coords[1] < 0 or connection_coords[1] > max_boundary_horizontal:
            return False
        
        if int(simple_maze[connection_coords[0]][connection_coords[1]]) == 0: 
            return False
       
        if connection_coords in historic_coords:
            return False
        else:
            historic_coords.append(connection_coords)

        print(f"Valid conn: {connection_coords}")

        return True

    def __init__(self, coords, distance):
        #print(f"Coordinates: {coords}, Distance: {distance}")
        self.coords = coords
        self.distance = distance
        north = self.GetNorth(coords)
        east  = self.GetEast(coords)      
        south = self.GetSouth(coords)
        west  = self.GetWest(coords) 
            
        self.connections = [north, east, south, west]

        if distance < 50:
            for conn in self.connections:
                if self.IsConnectionValid(coords, conn):
                    Node(conn, self.distance+1)



lines = (open(sys.argv[1], 'r')).read().split("\n")[:-1]
simple_maze = [[char for char in line ] for line in lines]

print(len(lines))
print(len(lines[0]))
max_boundary_verticle = len(lines)-1
max_boundary_horizontal = len(lines[0])-1

for line in simple_maze:
    print(line)



Node((0,0),0)


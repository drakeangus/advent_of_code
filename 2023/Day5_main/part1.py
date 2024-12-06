#!/bin/python3

import sys
from collections import defaultdict

file = open(sys.argv[1]).read().strip()

parts = file.split("\n\n")
lines = file.split("\n")


seed_array = parts[0].split(": ")[1].split(" ")
for seed in seed_array:
    print(seed)

p_SeedToSoil = parts[1].split("\n")[1:]
p_SoilToFert = parts[2].split("\n")[1:]
p_FertToWater= parts[3].split("\n")[1:]
p_WaterToLight = parts[4].split("\n")[1:]
p_LightToTemp = parts[5].split("\n")[1:]
p_TempToHum = parts[6].split("\n")[1:]
p_HumToLoc = parts[7].split("\n")[1:]

class Map:
    def __init__(self, part):
        self.map = defaultdict()
        for line in part:
            dest = int(line.split(" ")[0])
            start = int(line.split(" ")[1])
            map_range = int(line.split(" ")[2])
            
            n = 0
            while (n <= map_range):
                print(f"while loop : n = {n} out of {map_range}")
                self.map[start + n] = dest + n
                n += 1
    
    def GetValue(self, input):
        if input in self.map:
            return self.map[input]
        else:
            return input



SeedToSoil = Map(p_SeedToSoil)
SoilToFert = Map(p_SoilToFert)
FertToWater = Map(p_FertToWater)
WaterToLight = Map(p_WaterToLight)
LightToTemp = Map(p_LightToTemp)
TempToHum = Map(p_TempToHum) 
HumToLoc = Map(p_HumToLoc)

print(seed_array)

for seed in seed_array:
    
    seed = int(seed) 
    print(seed, " -> ", end=" ")
    
    soil = SeedToSoil.GetValue(seed)
    print(soil , " -> ", end=" ")

    fert = SoilToFert.GetValue(soil)
    print(fert, " -> ", end=" ")

    water = FertToWater.GetValue(fert)
    print(water, " -> ", end=" ")

    light = WaterToLight.GetValue(water)
    print(light, " -> ", end=" ")

    temp = LightToTemp.GetValue(light)
    print(temp, " -> ", end=" ")

    hum = TempToHum.GetValue(temp)
    print(temp, " -> ", end=" ")

    loc = HumToLoc.GetValue(hum)
    print(loc)

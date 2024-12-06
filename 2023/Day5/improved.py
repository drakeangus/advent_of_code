#!/bin/python3

import sys
from collections import defaultdict

file = open(sys.argv[1]).read().strip()

parts = file.split("\n\n")
lines = file.split("\n")


seed_array = parts[0].split(": ")[1].split(" ")


seed, *others = parts

# 50 (dest) 98 (start) 2 (range)

def find(seed, O):
    for line in O:
        dest, start, range = [int(x) for x in line.split(" ")]
        if start <= seed < start+range:
            seed =seed+(dest-start)
        else:
            seed = seed
    return seed

for seed in seed_array:
    seed = int(seed)
    print(seed)


    for o in others:
        O = o.split("\n")
        loc = find(seed, O[1:])
        print(loc)

#!/usr/bin/env python3 
from collections import defaultdict

#file_name="example.txt"
file_name="input.txt"
left=defaultdict(lambda: 0)
right=defaultdict(lambda: 0)


with open(file_name, 'r') as file:
    for line in file.readlines():
        line = line.strip()
        a,b = line.split("   ")
        #print(f"a: {a}, b: {b}")
        right[int(b)] += 1
        left[int(a)] += 1
sum=0
for number,count in right.items():
     #print(f"Right: {number}, count: {count}")
     #print(f"Left count: {left[number]}")
     sum += (number * left[number] * count)
print("Sum ", sum)

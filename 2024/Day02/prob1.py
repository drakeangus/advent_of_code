#!/usr/bin/env python3
import sys
file_name=sys.argv[1]
file = open(file_name, 'r')

def IsSafe(values):
    multiplier = 0
    for i,value in enumerate(values):
        if i == 0:
            last = int(value)
            continue
        
        if int(value) > last:
            # increasing
            if multiplier == -1:
                return 0
            multiplier = 1
        else:
            if multiplier == 1:
                return 0
            multiplier = -1

        diff = multiplier * (int(value) - last)
        if 0 < diff <= 3:
            last = int(value)
            continue
        else:
            return 0
        
    return 1

def IsSafeDampened(values):
    print(values)
    isSafe = True
    i=0
    j=1
    if int(values[i]) < int(values[j]):
        direction = 1
    else:
        direction = -1

    while (j < len(values)):
        print(f"i: {values[i]}, j: {values[j]}")
        if direction * int(values[i]) > int(values[j]):
           print("broke increase/decrease rule")
           isSafe = False
           break

        diff = direction * (int(values[j]) - int(values[i]))
        if not (0 < diff <= 3):
           print(diff)
           print("broke distance rule")
           isSafe = False
           break
       
        i += 1
        j += 1
    print(isSafe)
    return isSafe

sum = 0
for line in file.readlines():
    values = line.strip().split(" ")
    if IsSafeDampened(values):
        sum += 1

print(f"Sum: {sum}")

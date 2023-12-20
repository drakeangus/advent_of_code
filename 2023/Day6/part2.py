#!/bin/python3.10
import sys    
import math


def AppendElements(array):
    result = str()
    for num in array:
        result += str(num)
    return int(result)

file = open(sys.argv[1], "r")

time = (file.readline()).split(":")[1].strip().split()
distance = (file.readline()).split(":")[1].strip().split()

file.close()


T = AppendElements(time)
D = AppendElements(distance) 


Upper = 0.5 * ( T + ( (T**2) - 4*(D) )**0.5 )
Lower = 0.5 * ( T - ( (T**2) - 4*(D) )**0.5 )

if Upper % 1 == 0:    
    Upper -= 1        
if Lower % 1 == 0:    
    Lower += 1

count = math.floor(Upper) - math.ceil(Lower) +1
print(f"Number of solutions: {count}")

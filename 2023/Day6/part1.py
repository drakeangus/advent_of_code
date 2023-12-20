#!/bin/python3.10
import sys    
import math

file = open(sys.argv[1], "r")

time = (file.readline()).split(":")[1].strip().split()
distance = (file.readline()).split(":")[1].strip().split()

file.close()

answer=1
for i in range(0, len(time)):
    T=int(time[i]) 
    D=int(distance[i])
    print(f"Time: {T} Distance: {D}")
    
    Upper = 0.5 * ( T + ( (T**2) - 4*(D) )**0.5 )    
    Lower = 0.5 * ( T - ( (T**2) - 4*(D) )**0.5 )
    
    if Upper % 1 == 0:
        Upper -= 1
    if Lower % 1 == 0:
        Lower += 1

    count =  math.floor(Upper) - math.ceil(Lower) +1
   
    answer *= count
    

print("")
print(f"Product = {answer}")

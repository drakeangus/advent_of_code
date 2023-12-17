#!/bin/python3
import sys    
   
def FindFirstChar(line):
    for char in line:
        if char.isnumeric():
            return char
sum=0
for line in sys.stdin:    
    print(f"Input : {line.strip()}")    
    number = FindFirstChar(line) + FindFirstChar(line[::-1])
    print(f"Number : {number}\n")
    sum += int(number)

    
print(f"Sum is {sum}")

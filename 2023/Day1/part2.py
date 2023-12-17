#!/bin/python3.10
import sys    
    
def ReturnNum(sub_str):
    match sub_str:
        case "one":
            return 1
        case "two":
            return 2
        case "three":
            return 3
        case "four":
            return 4
        case "five":
            return 5
        case "six":
            return 6
        case "seven":
            return 7
        case "eight":
            return 8
        case "nine":
            return 9
        case other:
            return False

def IsAnyCharNumeric(string):   #remember to do this backwards for the reverse case
    for char in string:
        if char.isnumeric():
            return char
    return False

def FindFirst(line):
    while (len(line) > 0):
        for n in 3, 4, 5:
            
            sub_str = line[:n]
            #print(sub_str)
            if sub_str[0].isnumeric():
                print(f"number Match: {sub_str[0]}")
                return str(sub_str[0])
        
            num_match = ReturnNum(sub_str)
            if num_match:
                print(f"word Match: {num_match}")
                return str(num_match)

        line = line[1:]    # remove fist character from the string


def FindLast(line):
    while (len(line) > 0):
        for n in 3, 4, 5:
            
            sub_str = line[-n:]
            #print(sub_str)
            if sub_str[-1].isnumeric():
                print(f"number Match: {sub_str[-1]}")
                return str(sub_str[-1])
        
            num_match = ReturnNum(sub_str)
            if num_match:
                print(f"word Match: {num_match}")
                return str(num_match)

        line = line[:-1]    # remove fist character from the string

sum=0
for line in sys.stdin:    
    print(f"Input : {line.strip()}")    
    sum += int( FindFirst(line.strip()) + FindLast(line.strip()) )
    

    
print("Done!")
print(f"Sum = {sum}")

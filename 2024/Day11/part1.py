#!/usr/bin/env python3 

long_example="125 17"
example = "0 1 10 99 999"
input = "3935565 31753 437818 7697 5 38 0 123"

def split(number) -> list:    
    number = str(number)
    mid = int(len(number)/2)    
    return [int(number[:mid]), int(number[mid:])]

def Rules(stones, blinks=25):
    if blinks == 0:
        return stones
    new_stones = list()
    for stone in stones:
        if stone == 0:
            stone = [ 1 ]
            new_stones += stone
        elif len(str(stone)) % 2 == 0:
            stone = split(int(stone))
            new_stones += stone
            
        else:
            stone = [ stone * 2024 ]
            new_stones += stone
    return Rules(new_stones, blinks -1)

count = 0
for stone in input.split():
    count += len(Rules( [ int(stone) ], 25 ))

print(f"{count = }")

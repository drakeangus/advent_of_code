#!/usr/bin/env python3 


# This one was fucking tough. Had to see how other people went about it. 
# Got told the best way was with a recursive function taking the stone number and the number of blinks left, then returning the number of stones was the best way to go

# The array of stones gets WAY to large so you can't track them

long_example="125 17"
example = "0 1 10 99 999"
input = "3935565 31753 437818 7697 5 38 0 123"

def split(number) -> list:    
    number = str(number)
    mid = int(len(number)/2)    
    return [int(number[:mid]), int(number[mid:])]

from functools import cache

@cache
def Count(stone, blinks_left):
    if blinks_left == 0:
        return 1
    
    if stone == 0:
        return Count(1, blinks_left -1)

    if len(str(stone)) % 2 == 0:
        return sum([Count(half_stone, blinks_left -1) for half_stone in split(stone)])

    new_stone = int(stone) * 2024
    return Count(new_stone, blinks_left -1)



#stones = [ int(stone) for stone in long_example.split(" ")]
stones = [ int(stone) for stone in input.split(" ")]

total_blinks = 75
count = sum([Count(stone, total_blinks) for stone in stones])

print(f"{count = }")

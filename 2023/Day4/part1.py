#!/bin/python3.10
import sys    
import re
import math

lines = (sys.stdin).read().strip().split('\n')    

total=0
for line in lines:
    parts = re.split(":|\|", line)
    card_id = parts[0]
    winners = parts[1].split()
    nums = parts[2].split()
    print(card_id)
    print(winners)
    print(nums)
    count=0
    for num in nums:
        if num in winners:
            print(num)
            count += 1
    print(f"Count : {count}")
    score = math.floor(2**(count-1))
    total += score
    print(f"Score : {score}")



print(f"Total Score : {total}")

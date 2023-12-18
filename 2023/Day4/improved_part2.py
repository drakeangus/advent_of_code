#!/bin/python3.10
import sys    
import re
import math
from collections import defaultdict


def CountWins(parts):
    winners = parts[1].split()
    nums = parts[2].split()
#    print(card_id)
#    print(winners)
#    print(nums)
    win_count=0
    for num in nums:
        if num in winners:
            win_count += 1
    return win_count

lines = (sys.stdin).read().strip().split('\n')    


cardCount={}

line_count=-1
for line in lines:
    print(line)
    line_count+=1
    parts = re.split(":|\|", line)
    card_id = int(parts[0].split()[1])
    win_count = CountWins(parts)
    cardCount[card_id] = cardCount.get(card_id, 0) + win_count



cardDict=defaultdict(list)
for card_id, win_count in cardCount.items():
    print(f"{card_id} : {win_count}")
    if win_count == 0:
        cardDict[card_id].append(str())
    for n in range(int(card_id)+1, int(card_id)+win_count+1):
        #cardDict[card_id].append("C"+str(n))
        cardDict[card_id].append(str(n))


print()
card_count=0
cardScore = defaultdict(int)
for cardID, copys in reversed(cardDict.items()):
    print(f"{cardID} : {copys}")
    
    card_count += 1

    current_score=1
    if len(copys) == 1 and copys[0] == "":
        cardScore[int(cardID)] = 1
    else:
        for copy in copys:
            current_score += cardScore.get(int(copy))

    cardScore[cardID] = current_score

print()
sum=0
for n,m in cardScore.items():
    print(f"ID : {n} | score {m}")
    sum+=m

print(sum)

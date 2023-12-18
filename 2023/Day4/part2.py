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
    line_count+=1
    parts = re.split(":|\|", line)
    card_id = parts[0].split(" ")[1]
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


for cardID, copys in cardDict.items():
    print(f"{cardID} : {copys}")

print()

new_cardDict=defaultdict(list)
for cardID, copys in reversed(cardDict.items()):
    print(copys)
    for card in copys:
        print(f"{card}")
        #print(cardDict[card])
        #new_cardDict[cardID].append(r)

for cardID, copys in new_cardDict.items():
    print(f"{cardID} : {copys}")

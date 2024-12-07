#!/usr/bin/env python3
from collections import defaultdict
import sys


file = open(sys.argv[1], 'r').readlines()
instructions=list()
updates=list()
bFoundBreak = False
for line in file:
    line = line.strip()
    if line == "":
        bFoundBreak = True
        continue
    if bFoundBreak:
        updates.append(line)
    else:
        instructions.append(line) 



def GetMiddlePage(pages):
    page_list = pages.split(",")
    return page_list[int(((len(page_list) + 1)/2 ) - 1)]

def GetMiddlePageOfFixed(pages):
    page_list = pages.split(",")
    def FixBadPage():
        illegal_pages=list()
        for index in range(len(page_list)-1,-1,-1):
            page = page_list[index]
            if page in illegal_pages:
                page_list[index], page_list[index+1] = page_list[index+1], page_list[index]
                return False
            illegal_pages += instructions_dict[page]
        return True

    bGoodOrder=False
    while not bGoodOrder:
        bGoodOrder = FixBadPage()
    
    return GetMiddlePage(",".join(page_list))



instructions_dict=defaultdict(list)
for inst in instructions:
    key,value = inst.split("|")
    instructions_dict[key].append(value)


sum = 0
part_2_sum = 0
for update in updates:
    bGoodUpdate = True
    illegal_pages=list()
    for page in update.split(",")[::-1]:
        if page in illegal_pages:
            bGoodUpdate=False
            break
        illegal_pages += instructions_dict[page]
    if bGoodUpdate:
        sum += int(GetMiddlePage(update))

    if not bGoodUpdate:
        part_2_sum += int(GetMiddlePageOfFixed(update))

print(f"Sum: {sum}")
print(f"Sum part 2: {part_2_sum}")

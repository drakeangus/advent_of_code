#!/usr/bin/env python3 

import re
import sys
input = open(sys.argv[1], 'r').readlines()

word_search=[]
for line in input:
    word_search.append([char for char in str(line).strip()])

def GetSection(i,j):
    section = ""
    for x,y in [(x,y) for y in (j-1, j, j+1) for x in (i-1, i, i+1)]:
        section += word_search[x][y]
    return section

count=0
valid_patterns = r'M.M.A.S.S|M.S.A.M.S|S.S.A.M.M|S.M.A.S.M'
for i in range(1,len(word_search)-1):        # i : rows
    for j in range(1,len(word_search[0])-1): # j : columns
        if word_search[i][j] == "A":
            section = GetSection(i,j)
            if re.search(valid_patterns, section):
                count += 1

print(f"Count: {count}")

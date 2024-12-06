#!/usr/bin/env python3

import re
import sys
file_name=sys.argv[1]

file = open(file_name, 'r').readlines()

def GetMatches(pattern, line):
    return  [ (match.start(0),match.end(0)) for match in re.finditer(pattern, line) ]

sum=0
loc_dict=dict()
for line in file:
    calc_next = True
    mul_pattern='mul\\(\d+,\d+\\)'
    for loc in GetMatches(mul_pattern, line):
        loc_dict[loc[0]] = line[loc[0]:loc[1]]
    
    do_pattern='do\\(\\)'
    for loc in GetMatches(do_pattern, line):
        loc_dict[loc[0]] = line[loc[0]:loc[1]]

    dont_pattern='don\'t\\(\\)'
    for loc in GetMatches(dont_pattern, line):
        loc_dict[loc[0]] = line[loc[0]:loc[1]]
   
    for key,value in sorted(loc_dict.items()):
        if value == 'do()':
            calc_next=True
            continue
        if value == 'don\'t()':
            calc_next=False
            continue
        
        if calc_next:
            result = re.search(r'.*mul\((\d+),(\d+)\).*', str(value))
            if result:
                sum += int(result.group(1)) * int(result.group(2))
print(sum)

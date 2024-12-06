#!/usr/bin/env python3 

import re
import sys
input = open(sys.argv[1], 'r').readlines()
word_search=[]
for line in input:
    word_search.append(str(line).strip())

def GetDiagRight(word_search):
    string=str()
    max_y = len(word_search)
    max_x = len(word_search[0])
    for y in range(0,max_y + max_x):
        x=0
        while y >= 0:
            try:
                string += word_search[y][x]
            except:
                y-=1
                x+=1
                continue
            y-=1
            x+=1
        string += "_"
    return string

def GetDiagLeft(word_search):
    rev_word_seach=[]
    for line in word_search:
        rev_word_seach.append(line[::-1])
    return GetDiagRight(rev_word_seach)

def GetVertical(word_search):
    string=""
    for index in range(0,len(word_search[0])):
        for line in word_search:
            string += line[index]
        string += "_"
    return string

def GetHorizontal(word_search):
    string=""
    for line in word_search:
        string += line
        string += "_"
    return string


def CountMatches(string):
    pattern=r'XMAS'
    matches=list(re.findall(pattern, string))
    pattern=r'SAMX'
    matches += list(re.findall(pattern, string))
    return len(matches)

#print(GetHorizontal(word_search))
#print(GetVertical(word_search))
#print(GetDiagRight(word_search))
#print(GetDiagLeft(word_search))


search_string = GetHorizontal(word_search) + "_" + GetVertical(word_search) + "_" + GetDiagRight(word_search) + "_" + GetDiagLeft(word_search)

print(f"Matches: {CountMatches(search_string)}")


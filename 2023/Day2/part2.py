#!/bin/python3
import sys    
import re

def GameScore(line):
    red = 12
    green = 13
    blue = 14

    maxRed = 0
    maxGreen = 0
    maxBlue = 0

    gameRegex = re.search(r"^Game (\d*):(.*)$", line)
    gameID = int(gameRegex.group(1))
    game = gameRegex.group(2)
    print(f"Game ID : {gameID}")
    for round in game.split(";"):

        redRegex = re.search(r"^.* (\d*) red.*$", round)
        if redRegex:
            if int(redRegex.group(1)) > maxRed:
                maxRed = int(redRegex.group(1))

        greenRegex = re.search(r"^.* (\d*) green.*$", round)
        if greenRegex: 
            if int(greenRegex.group(1)) > maxGreen:
                maxGreen = int(greenRegex.group(1))

        blueRegex = re.search(r"^.* (\d*) blue.*$", round)
        if blueRegex: 
            if int(blueRegex.group(1)) > maxBlue:
                maxBlue = int(blueRegex.group(1))

        print( "red ",maxRed)
        print( "green ",maxGreen)
        print( "blue ",maxBlue)
    return maxRed * maxGreen * maxBlue

sum=0
for line in sys.stdin:    
    line=line.strip()
    print(f"Input : {line}")    


    sum = sum + GameScore(line)
    print(sum)
    
print("Done!")

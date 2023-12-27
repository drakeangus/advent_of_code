#!/bin/python3.10

# Run with file name as argument eg: ./part1and2.py example.txt

# Playing around with the yield/next keywords here:

# For part 1
def GetLines(filename):
    for line in open(filename, 'r'):
        yield line.strip()

# For part 2
def GetLinesReversed(filename):
    from functools import reduce
    for line in open(filename, 'r'):
        yield reduce(lambda a, b: a + " " + b, line.split()[::-1])

def PrintSequence(sequence):
    global bPrintSequences
    count=0
    bLoop = True
    while bLoop:
        bLoop=False
        for s in sequence:
            try: 
                val = str(s[count])
                bLoop=True
            except:
                val  = ""
            print(val, " ", end="")
        print("")
        count+=1

def GenerateSequence(line):
    global sequence
    sequence = [ [int(num)] for num in line.split() ]
    sequence_length = len(sequence)
    bLoop = True
    while bLoop:
        bLoop = False
        for i in range(1, sequence_length):
            step = sequence[i][-1] - sequence[i-1][-1]
            sequence[i-1].append(step)
            if step != 0:
                bLoop = True
        sequence_length-=1    

    if bPrintSequences:
        print("Original:")
        PrintSequence(sequence)

def GetPrediction(sequence):
    depth=int()
    for s in reversed(sequence):
        if depth == len(s):
            break;
        depth=len(s)

    bLoop = True
    bFirst = True
    while bLoop:
        bLoop = False
        if bFirst:
            bFirst = False
            dif = sequence[0-depth][-1]
            num = sequence[0-depth-1][-1]

        depth-=1

        if depth != 0:
            sequence[0-depth].append(num + dif)
            dif = sequence[0-depth][-1]
            num = sequence[0-depth][-2] 
            bLoop = True
        else:
            sequence.append([num+dif])
    
    if bPrintSequences:
        print("Predicted:")
        PrintSequence(sequence)
    
    return sequence[-1][0]

from sys import argv
file=argv[1]

# ------------- Part 1: -------------

bPrintSequences = True
line = GetLines(file)
part1_answer = 0
while True:
    try:    
        GenerateSequence(next(line))
        part1_answer += GetPrediction(sequence)
        bPrintSequences = False
    except:
        break

# ------------- Part 2: -------------

bPrintSequences = True
line = GetLinesReversed(file)
part2_answer = 0
while True:
    try:    
        GenerateSequence(next(line))
        part2_answer += GetPrediction(sequence)
        bPrintSequences = False
    except:
        break

# # -----------------------------------
print(f"Part1: \nSum of predictions: {part1_answer}")
print(f"Part2: \nSum of predictions: {part2_answer}")

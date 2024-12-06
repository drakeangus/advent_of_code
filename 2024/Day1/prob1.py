#!/usr/bin/env python3 

file_name="input.txt"
left=list()
right=list()

def AddToList(list,num):
    for i,entry in enumerate(list):
        if entry >= num:
            list.insert(i,num)
            return
    list.append(num)

with open(file_name, 'r') as file:
    for line in file.readlines():
        line = line.strip()
        a,b = line.split("   ")
        #print(f"a: {a}, b: {b}")
        AddToList(left, int(a))
        AddToList(right, int(b))

sum=0
for i in range(0,len(left)):
    sum += abs(left[i] - right[i])

print(sum)

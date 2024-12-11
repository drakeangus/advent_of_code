#!/usr/bin/env python3
from sys import argv
with open(argv[1], 'r') as file:
    line = ''.join(file.readlines()).strip()
    count=0
    id_dict=dict()
    filesystem=list()
    for index in range(0, len(line), 2):
        id_number = int(index/2)
        if index  < len(line):
            files = int(line[index])
            if index + 1 < len(line):
                free_space = int(line[index+1])
            else:
                free_space = 0
        else:
            files = 0

        new_entry = [ id_number for _ in range(0, files) ] 
        new_entry += [ "." for _ in range(free_space) ]
        filesystem += new_entry


from collections import deque
dq_filesystem = deque(filesystem)

def GetLast():
    global dq_filesystem
    global max_count
    reverse_count = -1
    try:
        while True:
            number = dq_filesystem[-1]
            if str(number) == ".":
                dq_filesystem.pop()
                max_count -= 1
            else:
                dq_filesystem[-1] = "."
                return int(number)
    except:
        return 0



count = -1
checksum = 0
max_count = len(dq_filesystem) -1
while count < max_count:
    count += 1
    number = dq_filesystem.popleft()
    if number == ".":
        number = GetLast()
    checksum += count * number

print(f"{checksum = }")

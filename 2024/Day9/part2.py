#!/usr/bin/env python3
from sys import argv
with open(argv[1], 'r') as file:
    line = ''.join(file.readlines()).strip()
    count=0
    id_dict=dict()
    filesystem=list()
    for index in range(0, len(line), 2):
        id_number = int(index/2)
        free_space = 0
        files = 0
        if index  < len(line):
            files = int(line[index])
            if index + 1 < len(line):
                free_space = int(line[index+1])

        filesystem.append((id_number, files))
        if free_space > 0:
            filesystem.append((".", free_space))

checksum = 0
moved=set()
reversed_index = 0
while abs(reversed_index) < len(filesystem):
    reversed_index -= 1
    block = filesystem[reversed_index]
    char,count = block
    if char == ".":
        continue
    if block in moved:
        continue
    for i,front_block in enumerate(filesystem):
        if len(filesystem) + reversed_index <= i:
            break
        if front_block[0] == ".":
            size_diff = front_block[1] - count
            if size_diff >= 0:
                filesystem.pop(reversed_index)
                if reversed_index != -1:
                    filesystem.insert(reversed_index+1, (".", count))
                else:
                    filesystem.append((".", count))
                filesystem.pop(i)
                filesystem.insert(i, block)

                if size_diff > 0: 
                    filesystem.insert(i+1, (".", size_diff))
                    reversed_index += 1
                moved.add(block)
                break

num_string = list()
count = 0
checksum = 0
for block in filesystem:
    id, copys = block[0], block[1]
    if id == ".":
        id = 0
    
    block_val = int(id) * (sum( range(count, count + int(copys) )))
    count += int(copys)
    checksum += block_val

print(f"{checksum = }")



#!/usr/bin/env python3

from sys import argv
file = open(argv[1], 'r').readlines()

results=list()
numbers=list()
for line in file:
    result_string, num_string = line.split(":")
    results.append(int(result_string))
    numbers.append([ int(number) for number in num_string.strip().split(" ") ])

from collections import deque # deque is good for popleft()
def CalcResult(dq_combination, dq_numbers):
    result = dq_numbers.popleft()
    while len(dq_numbers) > 0:
        current_num = dq_numbers.popleft()
        if dq_combination.popleft() == "+":
            result += current_num
        else:
            result *= current_num
    return result

import itertools # to get the combinations of + or *
def IsPossible(index):
    result = results[index]
    number_array = numbers[index]
    
    n_operations = len(number_array) - 1
    combinations = list(itertools.product("*+", repeat=n_operations))

    for combination in combinations:
        if CalcResult(deque(combination), deque(number_array)) == result:
            return True

    return False


count = 0
for index in range(len(results)):
    if IsPossible(index):
        count += results[index]

print(count)

 
import re
sum=0
state=1
with open('input.txt') as f:
    for line in f:
        pattern = r"mul\(\d+,\d+\)|do\(\)|don\'t\(\)"
        match = re.search(pattern, line)
        while match is not None:
            if match:
                line = line[match.end():]
                #print(match.group(0))
                result = match.group(0)
                if result == "do()":
                    state = 1
                if result == "don't()":
                    state = 0
                if result[0:3] == "mul" and state == 1:
                    numbers = re.findall(r'\d+', result)
                    numbers = list(map(int, numbers))
                    sum+=(numbers[0] * numbers[1])
                match = re.search(pattern, line)
print(f"Sum: {sum}")
 

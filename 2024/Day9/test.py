string="00992111777.44.333....5555.6666.....8888.."
count =0
for n,num in enumerate(string):
    if num == ".":
        continue
    count += n * int(num)

print(f"{count = }")

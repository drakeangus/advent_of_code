def is_safe_report(levels):
    direction = 0
    for i in range(len(levels) - 1):
        if levels[i] < levels[i + 1]:
            if direction == -1:
                return False
            direction = 1
        elif levels[i] > levels[i + 1]:
            if direction == 1:
                return False
            direction = -1
        else:
            return False

        spacing = abs(levels[i] - levels[i + 1])
        if spacing < 1 or spacing > 3:
            return False
    return True


safenum = 0
with open('input.txt') as f:
    for report in f:
        safe = False
        levels = list(map(int, report.split()))
        if is_safe_report(levels):
            safe=True
        if not safe:
            for i in range(len(levels)):
                temp_levels = levels.copy()
                temp_levels.pop(i)
                if is_safe_report(temp_levels):
                    safe = True
                    break
        if safe:
            safenum +=1

print(safenum)
 

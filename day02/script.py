import numpy as np
from datetime import datetime

init_time = datetime.now()

# We use python built-in file reading has we can process computations per lines
data = []
part1_count, part2_count = 0, 0

# Read the file line by line
with open("input.txt", "r") as file:
    for line in file:
        values = line.split()
        values_diff = [int(x) - int(y) for x, y in zip(values[1:], values [:-1])] 

        max = np.array(values_diff).max()
        min = np.array(values_diff).min()
        if max * min > 0 and np.max(np.array([abs(min),abs(max)])) < 4:
            part1_count += 1

        incr = []
        decr = []

        for index, value in enumerate(values_diff):
            if value > 0:
                incr.append(index)
            elif value < 0:
                decr.append(index)
        
        if len(incr) < len(decr):
            values_diff = [-x for x in values_diff]

        errors = []
        for index, value in enumerate(values_diff):
            if value < 1 or value > 3:
                errors.append(index) 

        if len(errors) == 0:
            part2_count += 1
        elif len(errors) < 2:
            if errors[0] == len(values_diff)-1 or errors[0] == 0:
                part2_count += 1
            elif values_diff[errors[0]] + values_diff[errors[0] + 1] < 4 and values_diff[errors[0]] + values_diff[errors[0] + 1] > 0:
                part2_count += 1
            elif values_diff[errors[0]] + values_diff[errors[0] - 1] < 4 and values_diff[errors[0]] + values_diff[errors[0] - 1] > 0:
                part2_count += 1
        elif len(errors) == 2:
            if errors[0] + 1 == errors[1]:
                if values_diff[errors[0]] + values_diff[errors[1]] < 4 and values_diff[errors[0]] + values_diff[errors[1]] > 0:
                    part2_count += 1

print("Time elapsed:", datetime.now() - init_time)
print("Part 1 safe reports count:", part1_count)
print("Part 2 safe reports count:", part2_count)
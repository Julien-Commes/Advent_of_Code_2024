import numpy as np
import re
from datetime import datetime

init_time = datetime.now()

with open('input.txt', 'r') as file:
    data = file.read()

filter = re.findall(r"(?:do)\(\)(.*?)(?:don't)\(\)", data)
filtered_data = "".join(filter)

result_part1 = re.findall(r"(?:mul)\(([0-9]{1,3})(?:,)([0-9]{1,3})\)", data)
result_part2 = re.findall(r"(?:mul)\(([0-9]{1,3})(?:,)([0-9]{1,3})\)", filtered_data)

mul_part1 = np.array([int(t[0]) * int(t[1]) for t in result_part1])
mul_part2 = np.array([int(t[0]) * int(t[1]) for t in result_part2])

print("Time elapsed:", datetime.now() - init_time)
print("Result of multiplications:", np.sum(mul_part1))
print("Result of enabled multiplications:", np.sum(mul_part2))
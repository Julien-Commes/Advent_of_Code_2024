import re
import numpy as np
from datetime import datetime

init_time = datetime.now()

disk = ""

with open("input.txt") as file:
    for line in file:
        disk = line

disk_digits_str = re.findall(r"([0-9])", disk)
disk_digits_full = [int(t) for t in disk_digits_str[::-2]]
disk_digits_full_original = [int(t) for t in disk_digits_str[::2]]
disk_digits_empty = [int(t) for t in disk_digits_str[1::2]]
disk_digits_empty_original = disk_digits_empty.copy()

offset_reverse = int(np.sum(disk_digits_full) + np.sum(disk_digits_empty) - 1)
class_id_reverse = len(disk_digits_full) - 1

sum = 0

for file in disk_digits_full:
    class_empty = 0
    while class_empty < len(disk_digits_empty) and class_empty < class_id_reverse + 1:
        empty_space = disk_digits_empty[class_empty]
    
        if file <= empty_space:
            offset = int(np.sum(disk_digits_full_original[:class_empty + 1]) + np.sum(disk_digits_empty[:class_empty])) - 1
            sum += class_id_reverse * (file * offset + ((file + 1) * file)//2)
            
            disk_digits_full_original[class_empty] += file
            class_id_reverse -= 1
            disk_digits_empty[class_empty] -= file
            offset_reverse -= (file + disk_digits_empty_original[class_id_reverse])
            break
        
        elif class_empty < len(disk_digits_empty) - 1 and class_empty < class_id_reverse:
            class_empty += 1

        else:
            class_empty += 1
            sum += class_id_reverse * (file * offset_reverse - ((file - 1) * file)//2)

            class_id_reverse -= 1
            offset_reverse -= (file + disk_digits_empty_original[class_id_reverse])

print("Time elapsed:", datetime.now() - init_time)
print("Resulting filesystem checksum:", sum)

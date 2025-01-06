import re
from datetime import datetime

init_time = datetime.now()

disk = ""

with open("input.txt") as file:
    for line in file:
        disk = line

disk_digits_str = re.findall(r"([0-9])", disk)
disk_digits_full = [int(t) for t in disk_digits_str[::2]]
disk_digits_empty = [int(t) for t in disk_digits_str[1::2]]

class_id_reverse = len(disk_digits_full) - 1
global_id = 0
class_id = 0

sum = 0

while len(disk_digits_full) > 0:
    while disk_digits_full[0] > 0:
        sum += global_id * class_id
        global_id += 1 
        disk_digits_full[0] -= 1
    disk_digits_full.pop(0)
    class_id += 1

    if len(disk_digits_full) < 1:
        break

    empty_space = disk_digits_empty[0]
    while empty_space > 0:
        while disk_digits_full[-1] > 0:
            sum += global_id * class_id_reverse
            global_id += 1
            disk_digits_full[-1] -= 1
            empty_space -= 1
            if empty_space < 1:
                break

        if disk_digits_full[-1] == 0:
            disk_digits_full.pop() 
            if len(disk_digits_full) < 1:
                break
            class_id_reverse -= 1

    disk_digits_empty.pop(0)

print("Time elapsed:", datetime.now() - init_time)
print("Resulting filesystem checksum:", sum)
import re
import numpy as np

disk = ""

with open("example.txt") as file:
    for line in file:
        disk = line

disk_digits_str = re.findall(r"([0-9])", disk)
disk_digits = [int(t) for t in disk_digits_str]
#print(disk_digits)

disk_dict={}
key = 0
offset = 0
for index, element in enumerate(disk_digits):
    if index % 2 == 0:
        loc = [k + offset for k in range(element)]
        disk_dict[key] = loc
        key += 1   
    offset += element

#print(disk_dict)

first_index = 0
first_key = 0
last_key = key - 1
last_index = max(disk_dict[last_key])

def find_empty_space(space_dict, current_key) -> list:
    max_bound = space_dict[current_key + 1][0]
    min_bound = max(space_dict[current_key]) 
    return [k for k in range(max_bound - 1, min_bound, -1)]

def apply_empty_space(space_dict, filling_space, current_filling_key, key_breaker):
    
    while len(filling_space) > 0:
        start = np.argmax(space_dict[current_filling_key])
        for k in range(start, -1, -1):
            #print(k)
            if len(filling_space) == 0:
                break
            if space_dict[current_filling_key][k] > filling_space[-1]:
                space_dict[current_filling_key][k] = filling_space[-1]
                filling_space.pop()
                if k == 0:
                    current_filling_key -= 1
            else:
                current_filling_key = key_breaker + 1
                filling_space = []


    return space_dict, current_filling_key

while last_index != first_index:
    empty_space = find_empty_space(disk_dict, first_key)
    #print(empty_space)
    disk_dict, last_key = apply_empty_space(disk_dict, empty_space, last_key, first_key)
    first_key += 1
    first_index = max(disk_dict[first_key]) 
    last_index = max(disk_dict[last_key])
    print(first_index, last_index)

sum = 0
true_last_key = key
for key in range(true_last_key):
    sum += key * np.sum(np.array(disk_dict[key]))

#print(sum, disk_dict)
print(sum)


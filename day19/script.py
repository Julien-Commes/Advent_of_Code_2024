import numpy as np
from datetime import datetime

init_time = datetime.now()

towels = np.loadtxt('input_towels.txt', delimiter=',', dtype='str') # Load the "towels" that are registered in the first line of the input given by AoC and store in the file 'input_towels.txt'
towels = np.char.strip(towels)
patterns = np.loadtxt('input_patterns.txt', dtype='str') # Load the "designs" that are registered in each line following the second of the input given by AoC and store in the file 'input_patterns.txt'

def find_pattern(pointer, max_len, pattern, towels_list):
    max_pointer = min(pointer + max_len - 1, len(pattern) - 1)
    
    potential_towels = np.array([pattern[pointer:k+1] for k in range(pointer,max_pointer+1)])

    in_towels = np.isin(potential_towels, towels_list)

    return potential_towels[in_towels]

total_valid_lines = 0
total_valid_comb = 0
max_len = np.max([len(towel) for towel in towels])

for pattern in patterns:

    pending_constructions = []
    pending_totals = []
    pointer = 0
    can_be_constructed = False
    in_towels = find_pattern(pointer, max_len, pattern, towels)
    for towel in in_towels:
        pending_constructions.append(towel)
        pending_totals.append(1)

    while len(pending_constructions) > 0:

        min_length_index = np.argmin([len(construction) for construction in pending_constructions])
        construction = pending_constructions.pop(min_length_index)
        temp_total = pending_totals.pop(min_length_index)
        pointer = len(construction)

        if pointer == len(pattern):
            total_valid_comb += temp_total
            can_be_constructed = True

        else:
            in_towels = find_pattern(pointer, max_len, pattern, towels)
            for towel in in_towels:
                new_construction = construction
                new_construction += towel

                if new_construction not in pending_constructions:
                    pending_constructions.append(new_construction)
                    pending_totals.append(temp_total)
                else:
                    index = pending_constructions.index(new_construction)
                    pending_totals[index] += temp_total
    
    total_valid_lines += can_be_constructed 
    
print(datetime.now() - init_time)
print("Total number of valid lines:", total_valid_lines)
print("Total number of valid combination:", total_valid_comb)

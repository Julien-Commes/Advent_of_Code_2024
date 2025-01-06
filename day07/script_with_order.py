'''
This code is an attempt I made before realizing we do not apply operations order rules
'''

import re
from datetime import datetime

init_time = datetime.now()

def generate_binaries(n, prefix=""):
    if n == 0:
        return [prefix]
    return generate_binaries(n - 1, prefix + "0") + generate_binaries(n - 1, prefix + "1")

def find_first_0(seq: list) -> int:
    n = 0
    not_find = True

    while n < len(seq) and not_find:
        if seq[n] == "0":
            not_find = False
        n += 1
    
    if not_find:
        print('No 0 in sequence')
        return -1
    
    return n-1


def apply_combination(comb, numb):
    if len(comb) == 0:
        return numb[0]
    
    nb_mul = 0
    for operation in comb:
        if operation == "1":
            nb_mul += 1
    if nb_mul == len(comb):
        total = 1
        for num in numb:
            total *= num
        return  total
    
    first_0_id = find_first_0(comb)
    return apply_combination(comb[:first_0_id], numb[:first_0_id+1]) + apply_combination(comb[first_0_id+1:], numb[first_0_id+1:])


with open('input.txt', 'r') as file:
    total = 0
    for line in file:
        numbers = re.findall(r"([0-9]+)", line)
        test_value = int(numbers[0])
        remaining_numbers = [int(num) for num in numbers[1:]]
        combinations = generate_binaries(len(remaining_numbers) - 1)

        has_valid_comb = False
        for combination in combinations:
            operation_candidate = apply_combination(combination, remaining_numbers)
            if operation_candidate == test_value:
                has_valid_comb = True
        
        total += has_valid_comb * test_value

print("Time elapsed:", datetime.now() - init_time)
print(total)



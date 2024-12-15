'''
This code is an attempt I made before realizing we do not apply operations order rules
'''

import re

def generate_binaries(n, prefix="", part_2 = False):
    if n == 0:
        return [prefix]
    
    if part_2:
        return generate_binaries(n - 1, prefix + "0" , part_2) + generate_binaries(n - 1, prefix + "1", part_2) + generate_binaries(n - 1, prefix + "2", part_2)
    
    return generate_binaries(n - 1, prefix + "0") + generate_binaries(n - 1, prefix + "1")

def apply_combination(comb, numb):
    sum = numb[0]
    for index, operator in enumerate(comb):
        if operator == "0":
            sum += numb[index + 1]
        elif operator == "1":
            sum *= numb[index +1]
        else:
            sum = int(str(sum) + str(numb[index +1]))
    
    return sum


with open('input.txt', 'r') as file:
    total = 0
    for line in file:
        numbers = re.findall(r"([0-9]+)", line)
        test_value = int(numbers[0])
        remaining_numbers = [int(num) for num in numbers[1:]]
        combinations = generate_binaries(len(remaining_numbers) - 1, part_2= True)

        has_valid_comb = False
        for combination in combinations:
            operation_candidate = apply_combination(combination, remaining_numbers)
            if operation_candidate == test_value:
                has_valid_comb = True
        
        total += has_valid_comb * test_value

print(total)



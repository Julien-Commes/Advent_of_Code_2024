import re
from datetime import datetime

init_time = datetime.now()

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
    total_part1 = 0
    total_part2 = 0
    
    for line in file:
        numbers = re.findall(r"([0-9]+)", line)
        test_value = int(numbers[0])
        remaining_numbers = [int(num) for num in numbers[1:]]
        combinations_part1 = generate_binaries(len(remaining_numbers) - 1, part_2= False)
        combinations_part2 = generate_binaries(len(remaining_numbers) - 1, part_2= True)

        has_valid_comb_part1 = False
        for combination in combinations_part1:
            operation_candidate = apply_combination(combination, remaining_numbers)
            if operation_candidate == test_value:
                has_valid_comb_part1 = True
                break
        
        total_part1 += has_valid_comb_part1 * test_value

        has_valid_comb_part2 = False
        for combination in combinations_part2:
            operation_candidate = apply_combination(combination, remaining_numbers)
            if operation_candidate == test_value:
                has_valid_comb_part2 = True
                break
        
        total_part2 += has_valid_comb_part2 * test_value

print("Time elapsed:", datetime.now() - init_time)
print("Total calibration result part 1:", total_part1)
print("Total calibration result part 2:", total_part2)
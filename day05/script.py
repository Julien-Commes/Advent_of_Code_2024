import re
from datetime import datetime

init_time = datetime.now()

rules = []
updates = []

rules_dict = {}
sum_middle_page = 0

with open('input_rules.txt', 'r') as file:
    for line in file:
        higher = int(line[:2])
        lower = int(line[3:5])

        if higher in rules_dict:
            rules_dict[higher].append(lower)
        else:
            rules_dict[higher] = [lower]

with open('input_updates.txt', 'r') as file:
    for line in file:
        update_candidate = re.findall(r"([0-9]{1,2})", line)
        not_candidate = False
        for index, element in enumerate(update_candidate):
            if int(element) in rules_dict:
                rules = rules_dict[int(element)]
                before = update_candidate[:index]
                for before_element in before:
                    if int(before_element) in rules:
                        not_candidate = True
                        break
                else:
                    continue
                break

        sum_middle_page += (1 - not_candidate) * int(update_candidate[len(update_candidate)//2])

print("Time elapsed:", datetime.now() - init_time)
print("Sum of middle pages:", sum_middle_page)
import re
from datetime import datetime

init_time = datetime.now()

rules = []
updates = []

rules_dict = {}
sum_corrected_middle_pages = 0

def find_kth_zero_reverse(lst, k):
    indices = [i for i, val in enumerate(lst) if val == 0]
    return indices[-k - 1]

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

        if not_candidate:
            new_line = [0 for _ in range(len(update_candidate))]
            for index, element in enumerate(update_candidate):
                if int(element) in rules_dict:
                    rules = rules_dict[int(element)]
                    after = update_candidate[index+1:]
                    if len(after) == 0:
                        new_line[find_kth_zero_reverse(new_line,0)] = int(element)
                    else:
                        loc = 0
                        for after_element in after:
                            if int(after_element) in rules:
                                loc += 1
                        index = find_kth_zero_reverse(new_line, loc)
                        new_line[index] = int(element)
                else:
                    new_line[find_kth_zero_reverse(new_line,0)] = int(element)

            sum_corrected_middle_pages += new_line[len(new_line)//2]

print("Time elapsed:", datetime.now() - init_time)
print("Sum of corrected middle pages:", sum_corrected_middle_pages)
import re
import numpy as np
import string

def segmenter_chaine(chaine):
    segments = re.findall(r'(([a-zA-Z])\2*)(\d*)', chaine)
    resultat = []
    before = '0'
    for segment, segment_type, chiffres in segments:
        is_same_as_before = (before.lower() == segment_type.lower())
        if is_same_as_before:
            if chiffres:
                resultat[-1] += segment + chiffres
            else:
                resultat[-1] += segment    
        elif chiffres:
            resultat.append(segment + chiffres)
        else:
            resultat.append(segment)
        before = segment_type
    
    return resultat

def get_regions_of_line(line, letters_id_dict, duplicate_regions_dict):
    new_line = []
    for region in line:
        is_lower = len(re.findall(r'[a-z]+', region)) > 0
        category = re.findall(r'[a-zA-Z]+', region)[0][0]
        if is_lower:
            category_ids = list(np.unique(re.findall(r'([0-9]+)', region)))
            category_id, position = str(np.min([int(t) for t in category_ids])), np.argmin([int(t) for t in category_ids])
            
            if len(category_ids) > 1:
                regions = [category.lower() + id for id in category_ids]
                
                if regions[position] in duplicate_regions_dict:
                    regions.pop(position)
                    duplicate_regions_dict[category.lower() + category_id] += regions
                else:
                    regions.pop(position)
                    duplicate_regions_dict[category.lower() + category_id] = regions

            new_sequence = add_sequence_id(region, category_id)
            new_line += new_sequence
        else:
            category_id = max(letters_id_dict[category])+1
            letters_id_dict[category].append(category_id)
            new_sequence = add_sequence_id(region, str(category_id))
            new_line += new_sequence
    return new_line, letters_id_dict

def add_sequence_id(sequence, category_id):
    letters = re.findall(r'[a-zA-Z]', sequence)
    result = [letter + category_id for letter in letters]
    return result

def transform_overlaping_regions(overlaping_map, duplicate_regions_dict):
    new_map = []
    for nb, line in enumerate(overlaping_map):
        for index, element in enumerate(line):
            if element.lower() not in duplicate_regions_dict:
                for key in duplicate_regions_dict:
                    if key[:1] == element[:1].lower():
                        if element.lower() in duplicate_regions_dict[key]:
                            line[index] = element[:1] + key[1:]
        new_map.append(line)
    return new_map
    
def update_line_with_shape(curr_line, next_line):
    next_line_updated=''

    for index, element in enumerate(curr_line):
        next_line_neighbour = next_line[index]
        if element[:1].upper() == next_line_neighbour:
            next_line_neighbour = element.lower()
        
        next_line_updated += next_line_neighbour

    return next_line_updated


def count_area_perim(curr_line, next_line, prev_line, counting_dict):
    #print(curr_line)
    for index in range(len(curr_line) + 1):
        if index == 0:
            prev_line_first = 'X'
            curr_line_first = 'X'
            next_line_first = 'X'
        else:
            prev_line_first = prev_line[index - 1]
            curr_line_first = curr_line[index - 1]
            next_line_first = next_line[index - 1]
        if index == len(curr_line):
            prev_line_sec = 'X'
            curr_line_sec = 'X'
            next_line_sec = 'X'
        else:
            prev_line_sec = prev_line[index]
            curr_line_sec = curr_line[index]
            next_line_sec = next_line[index]

        first_perim = 0
        second_perim = 0
        
        if curr_line_first != "X":
            if curr_line_first.lower() == curr_line_first:
                if curr_line_first.upper() == curr_line_sec:
                    first_perim += 1
                elif curr_line_first != curr_line_sec.lower() and curr_line_first == prev_line_sec.lower():
                    first_perim += 1
            elif curr_line_first.lower() == curr_line_sec:
                first_perim += 1
            elif curr_line_first != curr_line_sec.upper():
                first_perim += 1
            if curr_line_first.upper() != curr_line_sec.upper() and curr_line_first.upper() != next_line_first.upper():
                first_perim += 1

            if curr_line_first.upper() in counting_dict:
                counting_dict[curr_line_first.upper()][0] += first_perim
                counting_dict[curr_line_first.upper()][1] += 1
            else:
                counting_dict[curr_line_first.upper()] = [first_perim, 1]
        
        if curr_line_sec != "X":
            if curr_line_sec.upper() == curr_line_sec:
                if curr_line_first.upper() != curr_line_sec:
                    second_perim += 1
            elif curr_line_first.lower() != curr_line_sec and prev_line_first.lower() == curr_line_sec:
                second_perim += 1
            if curr_line_sec.upper() != curr_line_first.upper() and curr_line_sec.upper() != next_line_sec.upper():
                second_perim += 1

            if curr_line_sec.upper() in counting_dict:
                counting_dict[curr_line_sec.upper()][0] += second_perim
            else:
                counting_dict[curr_line_sec.upper()] = [second_perim, 0]

    return counting_dict

garden_map = np.loadtxt('example.txt', dtype=str)
max_bound_x = len(garden_map[0])
max_bound_y = garden_map.shape[0]

regions_dict = {}
category_id_dict = {letter: [0] for letter in string.ascii_uppercase}
same_regions_dict = {}

garden_map_with_regions = []
garden_map_with_regions.append(['X' for k in range(max_bound_x)])

curr_line = segmenter_chaine(garden_map[0])

for y in range(1, max_bound_y):
    first_line, category_id_dict = get_regions_of_line(curr_line, category_id_dict, same_regions_dict)
    garden_map_with_regions.append(first_line)

    next_line = garden_map[y]
    curr_line = segmenter_chaine(update_line_with_shape(first_line, next_line))
    if y == max_bound_y - 1:
        garden_map_with_regions.append(['X' for k in range(max_bound_x)])

regions_dict = {}
keys_to_del = []
for key in same_regions_dict:
    for key_alt in same_regions_dict:
        if key in same_regions_dict[key_alt]:
            same_regions_dict[key_alt] += same_regions_dict[key]
            keys_to_del.append(key)

for key in keys_to_del:
    same_regions_dict.pop(key)

garden_map_with_regions = transform_overlaping_regions(garden_map_with_regions, same_regions_dict)

for y in range(0, max_bound_y - 1):
    prev_line = garden_map_with_regions[y]
    curr_line = garden_map_with_regions[y+1]
    next_line = garden_map_with_regions[y+2]

    regions_dict = count_area_perim(curr_line, next_line, prev_line, regions_dict)

sum = 0
for key in regions_dict:
    sum += regions_dict[key][0] * regions_dict[key][1]

print(sum) #, regions_dict)
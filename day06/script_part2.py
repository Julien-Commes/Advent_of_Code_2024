import copy
from datetime import datetime

init_time = datetime.now()

map = {"^": [],
       "#": [],}

with open('input.txt', 'r') as file:
    i = 0
    for line in file:
        for j, element in enumerate(line):
            if element in map:
                map[element].append((i, j))
        i += 1

max_index_i, max_index_j = i, j + 1

def move_dir(row, col, dir):
    match dir:
        case 0:
            row, col = row - 1, col
        case 1 :
            row, col = row, col + 1
        case 2:
            row, col = row + 1, col
        case 3:
            row, col = row, col - 1
        case _:
            print("Not a valid direction: ", dir)
    return row, col

def emulate_guard_route(border_i, border_j, tested_map, starting_i, starting_j, starting_direction, is_init=False):
    i, j, direction = starting_i, starting_j, starting_direction
    is_looping = False

    if is_init:
        futur_candidates = []

    while i < border_i and i >= 0 and j < border_j and j >= 0:
        pot_i, pot_j = move_dir(i, j, direction)
        if (pot_i, pot_j) in tested_map['#']:
            direction = (direction + 1) % 4
        else:
            i, j = pot_i, pot_j
            if (pot_i, pot_j, direction) not in tested_map['X']:
                if is_init:
                    if (pot_i, pot_j) not in futur_candidates:
                        tested_map['X'].append((pot_i, pot_j, direction))
                        futur_candidates.append((pot_i, pot_j))
                else:
                    tested_map['X'].append((pot_i, pot_j, direction))

            else:
                is_looping = True
                i = -1
    
    return tested_map, is_looping

def test_build_candidates(original_map, nb_candidates: int, candidates: list, max_index_i: int, max_index_j: int):
    nb_looping = 0

    for index, candidate in enumerate(candidates[1:]):
        print(index + 1, " out of ", nb_candidates, end='\r')
        tested_map = copy.deepcopy(original_map)
        tested_map['#'].append((candidate[0], candidate[1]))
        tested_map['X'] = candidates[:index + 1]
        i, j, direction = tested_map['X'][-1]

        _, is_looping = emulate_guard_route(max_index_i, max_index_j, tested_map, i, j, direction)
        
        nb_looping += is_looping

    return nb_looping

i, j = map["^"][0]
direction = 0
map['X'] = [(i, j, direction)]

map, _= emulate_guard_route(max_index_i, max_index_j, map, i, j, direction, is_init=True)

candidates = map['X']
nb_distinct_positions = len(map['X']) - 1

map['X'] = []

nb_builds = test_build_candidates(map, nb_distinct_positions, candidates, max_index_i, max_index_j)

print("Time elapsed:", datetime.now() - init_time)
print("Number of distinct positions:", nb_distinct_positions)
print("Number of positions creating loops:", nb_builds)
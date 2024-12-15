import copy

map = {"X": [],
       "^": [],
       "#": [],}

candidates = []

with open('input.txt', 'r') as file:
    i = 0
    for line in file:
        for j, element in enumerate(line):
            if element in map:
                map[element].append((i, j))
            elif element == ".":
                candidates.append((i, j))
        i += 1

max_index_i, max_index_j = i, j + 1

#print(max_index_i, max_index_j)

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


def test_build_candidates(original_map, candidates: list, max_index_i: int, max_index_j: int):
    nb_looping = 0
    for index, candidate in enumerate(candidates):
        print(index, " out of ", len(candidates), end='\r')
        is_looping = False
        tested_map = copy.deepcopy(original_map)
        tested_map["#"].append(candidate)
        i, j = tested_map["^"][0]
        direction = 0

       #print("candidate:", candidate)

        while i < max_index_i and i >= 0 and j < max_index_j and j >= 0:
            pot_i, pot_j = move_dir(i, j, direction)
            if (pot_i, pot_j) in tested_map["#"]:
                direction = (direction + 1) % 4
            else:
                i, j = pot_i, pot_j
                if (pot_i, pot_j, direction) not in tested_map['X']:
                    tested_map['X'].append((pot_i, pot_j, direction))
                    #print((pot_i, pot_j, direction))
                else:
                    #print("looped at: ", (pot_i, pot_j, direction))
                    is_looping = True
                    i = -1
        
        nb_looping += is_looping

    return nb_looping

#candidates = [(0,1),(0,2),(6,3)]

nb_builds = test_build_candidates(map, candidates, max_index_i, max_index_j)
print("\n", nb_builds)
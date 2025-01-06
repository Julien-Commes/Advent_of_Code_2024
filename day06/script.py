from datetime import datetime

init_time = datetime.now()

map = {"X": [],
       "^": [],
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
            print("Not a valid direction:", dir)
    return row, col

i, j = map["^"][0]
direction = 0

while i < max_index_i and i >= 0 and j < max_index_j and j >= 0:
    pot_i, pot_j = move_dir(i, j, direction)
    if (pot_i, pot_j) in map["#"]:
        direction = (direction + 1) % 4
    else:
        i, j = pot_i, pot_j
        if (pot_i, pot_j) not in map['X']:
            map['X'].append((pot_i, pot_j))

if map["^"][0] not in map['X']:
    map['X'].append(map["^"][0])

print("Time elapsed:", datetime.now() - init_time)
print("Number of distinct positions:", len(map['X']) - 1)
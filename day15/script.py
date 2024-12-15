import numpy as np

'''
########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

max_i, max_j = 7, 7

moves = '<^^>>>vv<v>>v<<'

boxes = [(1, 3), (1, 5), (2, 4), (3, 4), (4, 4), (5, 4)]

walls = [(2, 1), (4, 2)]

pos = (2, 2)
'''

boxes = []
walls = []

with open('input_map.txt') as file:
    for index_i, line in enumerate(file):
        for index_j, element in enumerate(line):
            match element:
                case 'O':
                    boxes.append((index_i, index_j))
                case '#':
                    walls.append((index_i, index_j))
                case '@':
                    pos = (index_i, index_j)

max_i, max_j = index_i, index_j

moves = ''
with open('input_moves.txt') as file:
    for line in file:
        moves += line[:-1]

def move_dir(str_direction):
    match str_direction:
        case '<':
            return((0, -1))
        case '^':
            return((-1, 0))
        case '>':
            return((0, 1))
        case 'v' : 
            return((1, 0))
        case _:
            print("Not a valid direction")
            return 0
        
def determine_move(positions, indexes, walls: list, boxes: list, direction: tuple):
    #print(positions, direction, boxes)
    position_candidate = positions[-1][0] + direction[0], positions[-1][1]  + direction[1]
    out_of_bound = position_candidate[0] == 0 or position_candidate[0] == max_i or position_candidate[1] == 0 or position_candidate[1] == max_j

    if position_candidate in walls or out_of_bound:
        return positions, indexes
    elif position_candidate in boxes:
        index = boxes.index(position_candidate)
        positions = np.concatenate((positions, [position_candidate]))
        indexes = indexes + [index]
        return(determine_move(positions, indexes, walls, boxes, direction))
    else:
        return(positions + direction, indexes)

for move in moves:
    #print(boxes, pos, move)
    direction = move_dir(move)
    new_posistions, indexes = determine_move(np.array([pos], dtype=object), [], walls, boxes, direction)
    pos, new_boxes = new_posistions[0], new_posistions[1:]
    if len(new_boxes) > 0:
        for loc, index in enumerate(indexes):
            boxes[index] = (new_boxes[loc][0], new_boxes[loc][1])

#print(boxes, pos)

total = 0
for box in boxes:
    total += 100 * box[0] + box[1]

print(total)
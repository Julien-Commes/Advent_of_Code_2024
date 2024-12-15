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

boxes = [[],[]]
walls = []

with open('input_map.txt') as file:
    for index_i, line in enumerate(file):
        for index_j, element in enumerate(line):
            match element:
                case 'O':
                    boxes[0].append((index_i, 2 * index_j))
                    boxes[1].append((index_i, 2 * index_j + 1))
                case '#':
                    walls.append((index_i, 2 * index_j))
                    walls.append((index_i, 2 * index_j + 1))
                case '@':
                    pos = (index_i, 2 * index_j)

max_i, max_j = index_i, 2 * index_j + 1

moves = ''
with open('input_moves.txt') as file:
    for line in file:
        moves += line[:-1]

def move_dir(str_direction):
    match str_direction:
        case '<':
            return((0, -1), False)
        case '^':
            return((-1, 0), True)
        case '>':
            return((0, 1), False)
        case 'v' : 
            return((1, 0), True)
        case _:
            print("Not a valid direction")
            return 0
        
def check_positions_vert(positions, walls: list, boxes: list, direction: tuple):
    #print('vert', positions, direction) #, boxes)
    positions_candidates = [(t[0] + direction[0], t[1] + direction[1]) for t in positions[-1]] # --> Check how we get positions to check
    
    #print(positions_candidates)
    checking_status = []
    #out_of_bound = positions_candidates[0] == 0 or positions_candidates[0] == max_i or positions_candidates[1] == 0 or positions_candidates[1] == max_j

    for index, position in enumerate(positions_candidates):
        if position in walls:
            return positions, (0, 0)
        elif position in boxes[0]:  # i.e. '['
            checking_status.append((index, 0))
        elif position in boxes[1]:  # i.e. ']'
            checking_status.append((index, 1))
        
    if len(checking_status) == 0:
        return positions, direction

    else:
        #print(len(checking_status))
        positions_to_check = []
        for element in checking_status:
            #assert(0 == 1)
            match element[1]:
                case 0: # i.e. '['
                    position_candidate_coupled = (positions_candidates[element[0]][0], positions_candidates[element[0]][1] + 1)
                case 1: # i.e. ']'
                    position_candidate_coupled = (positions_candidates[element[0]][0], positions_candidates[element[0]][1] - 1)
                        
            #print("oui vert plusieurs", position_candidate_coupled, positions_candidates[element[0]])
            positions_to_check.append(positions_candidates[element[0]])
            positions_to_check.append(position_candidate_coupled)
        positions.append(positions_to_check)
        return check_positions_vert(positions, walls, boxes, direction)

def check_positions_horiz(positions, walls: list, boxes: list, direction: tuple):
    #print(positions, direction, boxes)
    position_candidate = positions[-1][0] + direction[0], positions[-1][1]  + direction[1]
    
    #out_of_bound = position_candidate[0] == 0 or position_candidate[0] == max_i or position_candidate[1] == 0 or position_candidate[1] == max_j
    checking_status = -1

    if position_candidate in walls:
        return positions, (0, 0)
    elif position_candidate in boxes[0]:  # i.e. '['
        checking_status = 0
    elif position_candidate in boxes[1]:  # i.e. ']'
        checking_status = 1
        
    if checking_status == -1:
        return positions, direction

    elif checking_status == 0: # i.e. '['
        position_candidate_coupled = position_candidate[0], position_candidate[1] + 1
    elif checking_status == 1: # i.e. ']'
        position_candidate_coupled = position_candidate[0], position_candidate[1] - 1
    
    positions.append(position_candidate)
    positions.append(position_candidate_coupled)
            
    return check_positions_horiz(positions, walls, boxes, direction)
    

for move in moves:
    #print(boxes, pos, move)
    direction, is_vert = move_dir(move)

    if is_vert:
        positions_involved, real_move = check_positions_vert([[pos]], walls, boxes, direction)
        positions_involved = [item for sublist in positions_involved for item in sublist] # flatten positions_involved
        #print(boxes, pos, move)
    else:
        positions_involved, real_move = check_positions_horiz([pos], walls, boxes, direction)

    pos, new_boxes = positions_involved[0], positions_involved[1:]
    #print("move computed: ", pos, real_move, new_boxes)
    if len(new_boxes) > 0:
        boxes_moved_0 = [tuple(map(sum, zip(box, real_move))) if box in new_boxes else box for box in boxes[0]]
        boxes_moved_1 = [tuple(map(sum, zip(box, real_move))) if box in new_boxes else box for box in boxes[1]]

        boxes[0], boxes[1] = boxes_moved_0, boxes_moved_1
    pos = (pos[0] + real_move[0], pos[1] + real_move[1])

#print(boxes, pos)

total = 0
for box in boxes[0]:
    total += 100 * box[0] + box[1]

print(total)
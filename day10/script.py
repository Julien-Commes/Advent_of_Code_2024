import numpy as np 

trail_map = np.loadtxt('input.txt', dtype=str)

"""
    Directions map:
             3    
             |
        2 <--X--> 0
             |
             1    
"""

def check_dirs(pos_x, pos_y, checked_map):
    level = int(checked_map[pos_y][pos_x]) + 1
    #print(level)
    dirs = []
    min_dir = 5
    if pos_x < len(checked_map[0]) - 1 and int(checked_map[pos_y][pos_x + 1]) == level:
        dirs.append(0)
        min_dir = 0
    if pos_y < len(checked_map) - 1 and int(checked_map[pos_y + 1][pos_x]) == level:
        dirs.append(1)
        min_dir = min(min_dir, 1)
    if pos_x > 0 and int(checked_map[pos_y][pos_x - 1]) == level:
        dirs.append(2)
        min_dir = min(min_dir, 2)
    if pos_y > 0 and int(checked_map[pos_y - 1][pos_x]) == level:
        dirs.append(3)
        min_dir = min(min_dir, 3)
    
    return min_dir, dirs

def move_position(pos_x, pos_y, dir):
    match dir:
        case 0:
            pos_x += 1
        case 1:
            pos_y += 1
        case 2:
            pos_x -= 1
        case 3:
            pos_y -= 1
        case _:
            print('No valid direction')
    return pos_x, pos_y

end_trail = 9
trails=[[] for k in range(end_trail + 1)]
total = 0
part2 = False

for y, line in enumerate(trail_map):
    for x, element in enumerate(line):
        if element == '0':
            reachables = []
            futur_dir, trails[0] = check_dirs(x, y, trail_map)
            
            if futur_dir != 5:
                movs = [futur_dir]
            index = 0

            while len(movs) > 0:
                x, y = move_position(x, y, movs[-1])
                index += 1
                #print(x, y)

                futur_dir, trails[index] = check_dirs(x, y, trail_map)
                #print(futur_dir, trails)

                if futur_dir != 5:
                    movs.append(futur_dir)
                else:
                    if index == end_trail:
                        if part2 or (x, y) not in reachables:
                            reachables.append((x, y))

                    descend = True
                    while descend:
                        index -= 1
                        trails[index].pop(0)
                        last_mov = movs.pop()
                        x, y = move_position(x, y, (last_mov+2)%4)
                        descend = len(trails[index]) == 0 and index > 0
                    
                    if index >= 0 and len(trails[index]) > 0:
                        movs.append(trails[index][0])
            
            total += len(reachables)
            #print(reachables)

print(total)
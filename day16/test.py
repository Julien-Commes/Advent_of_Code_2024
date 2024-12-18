max_cost = 107512

ROW = 141
COL = 141

src = [139, 1]
dest = [1, 139]

dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]

grid = [['' for _ in range(COL)] for _ in range(ROW)]

with open('input.txt') as file:
    for index_i, line in enumerate(file):
        for index_j, element in enumerate(line):
            if element != '\n':
                grid[index_i][index_j] = element

def is_valid(row, col):
    return (row >= 0) and (row < ROW) and (col >= 0) and (col < COL)

# Check if a cell is unblocked
def is_unblocked(grid, row, col):
    return grid[row][col] == '.' or grid[row][col] == 'S' or grid[row][col] == 'E'

def is_destination(row, col, dest):
    return row == dest[0] and col == dest[1]

def check_neighbours(i, j, grid):
    possible_neighbours = []

    for dir in dirs:
        candidate_i, candidate_j = i + dir[0], j + dir[1]
        if is_valid(candidate_i, candidate_j) and is_unblocked(grid, candidate_i, candidate_j):
            possible_neighbours.append((candidate_i, candidate_j))
    
    return possible_neighbours

def compute_cost(prev_loc, next_loc, dir):
    cost = 1
    move = next_loc[0] - prev_loc[0], next_loc[1] - prev_loc[1]
    match move:
        case (1,0):
            new_dir = 1
        case (0,1):
            new_dir = 0
        case (-1,0):
            new_dir = 3
        case (0,-1):
            new_dir = 2
    
    diff_dir = abs(dir - new_dir)
    if diff_dir == 3:
        diff_dir = 1

    cost += diff_dir * 1000  
    return cost, new_dir 

pending_nodes = [[src, 0, 0, check_neighbours(src[0], src[1], grid)]]
print(pending_nodes)
current_path = []
all_paths = []
dir = 0

while len(pending_nodes) > 0:
    current_node = pending_nodes[-1]

    #print(current_node)

    tot_cost = current_node[1]
    dir = current_node[2]
    next_node_candidate = current_node[3][-1]
    
    move_cost, new_dir = compute_cost(current_node[0], next_node_candidate, dir)
    tot_cost += move_cost

    if tot_cost >= max_cost:
        if is_destination(next_node_candidate[0], next_node_candidate[1], dest):
            all_paths.append(current_path)
            print('found a new path', len(pending_nodes))

        pending_nodes[-1][3].pop()
        if len(pending_nodes[-1][3]) == 0:
            pending_nodes.pop()
        if len(pending_nodes) > 0:
            next_node_coord = (pending_nodes[-1][0][0], pending_nodes[-1][0][1])
            node_index_in_path = current_path.index(next_node_coord)
            current_path = current_path[:node_index_in_path+1]

    else:
        current_path.append((next_node_candidate[0], next_node_candidate[1]))
        available_neighbours = check_neighbours(next_node_candidate[0], next_node_candidate[1], grid)
        new_neighbours = []
        for element in available_neighbours:
            if element not in current_path:
                new_neighbours.append(element)
        
        if len(new_neighbours) == 0:
            pending_nodes[-1][3].pop()
            if len(pending_nodes[-1][3]) == 0:
                pending_nodes.pop()
        
            if len(pending_nodes) > 0:
                next_node_coord = (pending_nodes[-1][0][0], pending_nodes[-1][0][1])
                node_index_in_path = current_path.index(next_node_coord)
                current_path = current_path[:node_index_in_path+1]
        else:
            pending_nodes[-1][3].pop()
            if len(pending_nodes[-1][3]) == 0:
                pending_nodes.pop()

            pending_nodes.append([next_node_candidate, tot_cost, new_dir, new_neighbours])
            current_path.append(next_node_candidate)

tiles_in_all_paths = [element for sublist in all_paths for element in sublist]
#print(tiles_in_all_paths)

set_tiles = set(tiles_in_all_paths) 
list_unique_tiles = (list(set_tiles))
 
print(len(list_unique_tiles)+2) #, list_unique_tiles)
# Python program for A* Search Algorithm
import heapq
from datetime import datetime

init_time = datetime.now()

# Define the size of the grid
ROW = 141
COL = 141

max_cost = 107512

# Define the Cell class
class Cell:
    def __init__(self):
      # Parent cell's row index
        self.parent_i = []
    # Parent cell's column index
        self.parent_j = []
    # Parent cell's orientation
        self.parent_orientation = []
    # Total cost of the cell (g + h)
        self.cost = float('inf')

# Check if a cell is valid (within the grid)
def is_valid(row, col):
    return (row >= 0) and (row < ROW) and (col >= 0) and (col < COL)

# Check if a cell is unblocked
def is_unblocked(grid, row, col):
    return grid[row][col] == '.' or grid[row][col] == 'S' or grid[row][col] == 'E'

# Check if a cell is the destination
def is_destination(row, col, dest):
    return row == dest[0] and col == dest[1]

# Trace the path from source to destination
def trace_path(cell_details, dest, grid):
    path = []
    row = dest[0]
    col = dest[1]
    orient = 0
    paths_to_add = [(row, col, orient)]

    while len(paths_to_add) > 0:
        p = paths_to_add.pop()
        row, col, orient = p

        # Trace the path from destination to source using parent cells
        while not (cell_details[row][col][orient].parent_i[-1] == row and cell_details[row][col][orient].parent_j[-1] == col and cell_details[row][col][orient].parent_orientation[-1] == orient):
            path.append((row, col))

            if len(cell_details[row][col][orient].parent_i) > 1:
                new_paths = []
                for k in range(len(cell_details[row][col][orient].parent_i)):
                    new_paths.append((cell_details[row][col][orient].parent_i[k], cell_details[row][col][orient].parent_j[k], cell_details[row][col][orient].parent_orientation[k]))
                set_new_paths = set(new_paths) 
                new_paths_unique = (list(set_new_paths))
                for element in  new_paths_unique[:-1]:
                    paths_to_add.append(element)
                temp_row = new_paths_unique[-1][0]
                temp_col = new_paths_unique[-1][1]
                temp_orient = new_paths_unique[-1][2]

            else:
                temp_row = cell_details[row][col][orient].parent_i[-1]
                temp_col = cell_details[row][col][orient].parent_j[-1]
                temp_orient = cell_details[row][col][orient].parent_orientation[-1]

            row = temp_row
            col = temp_col
            orient = temp_orient

        # Add the source cell to the path
        path.append((row, col))
    
    set_tiles_on_paths = set(path) 
    tiles_on_paths = (list(set_tiles_on_paths))
    print("Number of tiles on shortest paths:", len(tiles_on_paths))

# Implement the A* search algorithm
def a_star_search(grid, src, dest):
    # Check if the source and destination are valid
    if not is_valid(src[0], src[1]) or not is_valid(dest[0], dest[1]):
        print("Source or destination is invalid")
        return

    #print(grid[src[0]][src[1]], grid[dest[0]][dest[1]])
    # Check if the source and destination are unblocked
    if not is_unblocked(grid, src[0], src[1]) or not is_unblocked(grid, dest[0], dest[1]):
        print("Source or the destination is blocked")
        return

    # Check if we are already at the destination
    if is_destination(src[0], src[1], dest):
        print("We are already at the destination")
        return

    # Initialize the closed list (visited cells)
    closed_list = [[[False for _ in range(4)] for _ in range(COL)] for _ in range(ROW)]
    # Initialize the details of each cell
    cell_details = [[[Cell() for _ in range(4)] for _ in range(COL)] for _ in range(ROW)]

    # Initialize the start cell details
    i = src[0]
    j = src[1]
    orientation  = 0
    cell_details[i][j][orientation].cost = 0.
    cell_details[i][j][orientation].parent_i.append(i)
    cell_details[i][j][orientation].parent_j.append(j)
    cell_details[i][j][orientation].parent_orientation.append(orientation)

    # Initialize the open list (cells to be visited) with the start cell
    open_list = []
    heapq.heappush(open_list, (0.0, i, j, orientation))

    # Initialize the flag for whether destination is found
    found_dest = False

    # Main loop of A* search algorithm
    while len(open_list) > 0:
        # Pop the cell with the smallest f value from the open list
        p = heapq.heappop(open_list)

        # Mark the cell as visited
        i = p[1]
        j = p[2]
        orientation = p[3]
        closed_list[i][j][orientation] = True
        #print(i, j, orientation)

        match orientation:
            case 0:
                directions = [(0, 1, 0), (0, 0, 1), (0, 0, 3)]
            case 1:
                directions = [(1, 0, 0), (0, 0, 1), (0, 0, 3)]
            case 2:
                directions = [(0, -1, 0), (0, 0, 1), (0, 0, 3)]
            case 3:
                directions = [(-1, 0, 0), (0, 0, 1), (0, 0, 3)]
        # For each direction, check the successors
        for dir in directions:
            new_i = i + dir[0]
            new_j = j + dir[1]
            new_orient = (orientation + dir[2]) % 4

            # If the successor is valid, unblocked, and not visited
            if is_valid(new_i, new_j) and is_unblocked(grid, new_i, new_j) and not closed_list[new_i][new_j][new_orient]:
                # If the successor is the destination
                if is_destination(new_i, new_j, dest):
                    # Set the parent of the destination cell
                    cell_details[new_i][new_j][0].parent_i.append(i)
                    cell_details[new_i][new_j][0].parent_j.append(j)
                    cell_details[new_i][new_j][0].parent_orientation.append(orientation)

                    #print("The destination cell is found")
                    # Trace and print the path from source to destination
                    trace_path(cell_details, dest, grid)
                    return 
                else:
                    # Calculate the new f, g, and h values
                    added_cost = 1.0
                    if orientation != new_orient:
                        added_cost = 1000.0
                    new_cost = cell_details[i][j][orientation].cost + added_cost
                    
                    # If the cell is not in the open list or the new f value is smaller
                    if (cell_details[new_i][new_j][new_orient].cost == float('inf') or cell_details[new_i][new_j][new_orient].cost == new_cost) and new_cost <= max_cost:
                        # Add the cell to the open list
                        heapq.heappush(open_list, (new_cost, new_i, new_j, new_orient))
                        # Update the cell details
                        cell_details[new_i][new_j][new_orient].cost = new_cost
                        cell_details[new_i][new_j][new_orient].parent_i.append(i)
                        cell_details[new_i][new_j][new_orient].parent_j.append(j)
                        cell_details[new_i][new_j][new_orient].parent_orientation.append(orientation)
                    
                    elif (cell_details[new_i][new_j][new_orient].cost == float('inf') or cell_details[new_i][new_j][new_orient].cost > new_cost) and new_cost <= max_cost:
                        # Add the cell to the open list
                        heapq.heappush(open_list, (new_cost, new_i, new_j, new_orient))
                        # Update the cell details
                        cell_details[new_i][new_j][new_orient].cost = new_cost
                        cell_details[new_i][new_j][new_orient].parent_i = [i]
                        cell_details[new_i][new_j][new_orient].parent_j = [j]
                        cell_details[new_i][new_j][new_orient].parent_orientation = [orientation]

    # If the destination is not found after visiting all cells
    if not found_dest:
        print("Failed to find the destination cell")

def main():
    grid=[['' for _ in range(COL)] for _ in range(ROW)]

    with open('input.txt') as file:
        for index_i, line in enumerate(file):
            for index_j, element in enumerate(line):
                if element != '\n':
                    grid[index_i][index_j] = element

    # Define the source and destination
    src = [139, 1]
    dest = [1, 139]

    # Run the A* search algorithm
    a_star_search(grid, src, dest)
    print("Time elapsed:", datetime.now() - init_time)

if __name__ == "__main__":
    main()
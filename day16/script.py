# Python program for A* Search Algorithm
import heapq
from datetime import datetime

init_time = datetime.now()

# Define the size of the grid
ROW = 140
COL = 140

# Define the Cell class
class Cell:
    def __init__(self):
      # Parent cell's row index
        self.parent_i = 0
    # Parent cell's column index
        self.parent_j = 0
    # Parent cell's orientation
        self.parent_orientation = 0
    # Total cost of the cell (g + h)
        self.f = float('inf')
    # Cost from start to this cell
        self.g = float('inf')
    # Heuristic cost from this cell to destination
        self.h = 0

# Check if a cell is valid (within the grid)
def is_valid(row, col):
    return (row >= 0) and (row < ROW) and (col >= 0) and (col < COL)

# Check if a cell is unblocked
def is_unblocked(grid, row, col):
    return grid[row][col] == '.' or grid[row][col] == 'S' or grid[row][col] == 'E'

# Check if a cell is the destination
def is_destination(row, col, dest):
    return row == dest[0] and col == dest[1]

# Calculate the heuristic value of a cell (Euclidean distance to destination)
def calculate_h_value(row, col, dest, orient):
    match orient:
        case 0:
            h = abs(row - dest[0])+ abs(col - dest[1]) + 1000 * (row - dest[0] == 0)
        case 1:
            h = abs(row - dest[0]) + abs(col - dest[1]) + 1000 * (col - dest[1] == 0) + 1000 * (row - dest[0] == 0)
        case 2:
            h = abs(row - dest[0]) + abs(col - dest[1]) + 1000 * (row - dest[0] == 0) + 1000 * (col - dest[1] == 0) 
        case 3:
            h = abs(row - dest[0]) + abs(col - dest[1]) + 1000 * (col - dest[1] == 0)
    return h

# Trace the path from source to destination
def trace_path(cell_details, dest):
    total = 0

    #print("The Path is ")
    path = []
    row = dest[0]
    col = dest[1]
    orient = 0

    # Trace the path from destination to source using parent cells
    while not (cell_details[row][col][orient].parent_i == row and cell_details[row][col][orient].parent_j == col and cell_details[row][col][orient].parent_orientation == orient):
        path.append((row, col, orient))
        temp_row = cell_details[row][col][orient].parent_i
        temp_col = cell_details[row][col][orient].parent_j
        temp_orient = cell_details[row][col][orient].parent_orientation
        if row == dest[0] and col == dest[1]:
            total += 1
        elif temp_orient != orient:
            total += 1000
        else:
            total += 1
        row = temp_row
        col = temp_col
        orient = temp_orient

    '''
    # Add the source cell to the path
    path.append((row, col, orient))
    # Reverse the path to get the path from source to destination
    path.reverse()
    # Print the path
    for i in path:
        print("->", i, end=" ")
    '''
    print("Lowest score a Reindeer could get:", total)

# Implement the A* search algorithm
def a_star_search(grid, src, dest):
    # Check if the source and destination are valid
    if not is_valid(src[0], src[1]) or not is_valid(dest[0], dest[1]):
        print("Source or destination is invalid")
        return

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
    cell_details[i][j][orientation].f = 0
    cell_details[i][j][orientation].g = 0
    cell_details[i][j][orientation].h = 0
    cell_details[i][j][orientation].parent_i = i
    cell_details[i][j][orientation].parent_j = j
    cell_details[i][j][orientation].parent_orientation = orientation

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
                    cell_details[new_i][new_j][0].parent_i = i
                    cell_details[new_i][new_j][0].parent_j = j
                    cell_details[new_i][new_j][0].parent_orientation = orientation

                    #print("The destination cell is found")
                    # Trace and print the path from source to destination
                    trace_path(cell_details, dest)
                    found_dest = True
                    return
                else:
                    # Calculate the new f, g, and h values
                    added_g = 1.0
                    if orientation != new_orient:
                        added_g = 1000.0
                    g_new = cell_details[i][j][orientation].g + added_g
                    h_new = calculate_h_value(new_i, new_j, dest, new_orient)
                    f_new = g_new + h_new

                    # If the cell is not in the open list or the new f value is smaller
                    if cell_details[new_i][new_j][new_orient].f == float('inf') or cell_details[new_i][new_j][new_orient].f > f_new:
                        # Add the cell to the open list
                        heapq.heappush(open_list, (f_new, new_i, new_j, new_orient))
                        # Update the cell details
                        cell_details[new_i][new_j][new_orient].f = f_new
                        cell_details[new_i][new_j][new_orient].g = g_new
                        cell_details[new_i][new_j][new_orient].h = h_new
                        cell_details[new_i][new_j][new_orient].parent_i = i
                        cell_details[new_i][new_j][new_orient].parent_j = j
                        cell_details[new_i][new_j][new_orient].parent_orientation = orientation

    # If the destination is not found after visiting all cells
    if not found_dest:
        print("Failed to find the destination cell")


def main():
    grid=[]

    with open('input.txt') as file:
        for line in file:
            grid.append(line)

    # Define the source and destination
    src = [139, 1]
    dest = [1, 139]

    # Run the A* search algorithm
    a_star_search(grid, src, dest)
    print("Time elapsed:", datetime.now() - init_time)

if __name__ == "__main__":
    main()
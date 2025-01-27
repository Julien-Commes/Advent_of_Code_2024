# Python program for A* Search Algorithm
import heapq
import numpy as np
from datetime import datetime

init_time = datetime.now()

# Define the size of the grid
ROW = 71
COL = 71

# Define the Cell class
class Cell:
    def __init__(self):
    # Parent cell's row index
        self.parent_i = 0
    # Parent cell's column index
        self.parent_j = 0
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
    return grid[row][col] == '.'

# Check if a cell is the destination
def is_destination(row, col, dest):
    return row == dest[0] and col == dest[1]

# Calculate the heuristic value of a cell (Euclidean distance to destination)
def calculate_h_value(row, col, dest):
    return (((row - dest[0]) ** 2 + (col - dest[1]) ** 2) ** 0.5)

# Trace the path from source to destination
def trace_path(cell_details, dest, is_part_1 = False):
    path = []
    row = dest[0]
    col = dest[1]

    # Trace the path from destination to source using parent cells
    while not (cell_details[row][col].parent_i == row and cell_details[row][col].parent_j == col):
        path.append((row, col))
        temp_row = cell_details[row][col].parent_i
        temp_col = cell_details[row][col].parent_j
        row = temp_row
        col = temp_col

    # Add the source cell to the path
    path.append((row, col))
    
    if is_part_1:
        print("Minimum number of steps needed to reach the exit:", len(path)-1)
    return path

# Implement the A* search algorithm
def a_star_search(grid, src, dest, is_part_1 = False):
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
    closed_list = [[False for _ in range(COL)] for _ in range(ROW)]
    # Initialize the details of each cell
    cell_details = [[Cell() for _ in range(COL)] for _ in range(ROW)]

    # Initialize the start cell details
    i = src[0]
    j = src[1]
    cell_details[i][j].f = 0
    cell_details[i][j].g = 0
    cell_details[i][j].h = 0
    cell_details[i][j].parent_i = i
    cell_details[i][j].parent_j = j

    # Initialize the open list (cells to be visited) with the start cell
    open_list = []
    heapq.heappush(open_list, (0.0, i, j))

    # Initialize the flag for whether destination is found
    found_dest = False

    # Main loop of A* search algorithm
    while len(open_list) > 0:
        # Pop the cell with the smallest f value from the open list
        p = heapq.heappop(open_list)

        # Mark the cell as visited
        i = p[1]
        j = p[2]
        closed_list[i][j] = True

        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        # For each direction, check the successors
        for dir in directions:
            new_i = i + dir[0]
            new_j = j + dir[1]

            # If the successor is valid, unblocked, and not visited
            if is_valid(new_i, new_j) and is_unblocked(grid, new_i, new_j) and not closed_list[new_i][new_j]:
                # If the successor is the destination
                if is_destination(new_i, new_j, dest):
                    # Set the parent of the destination cell
                    cell_details[new_i][new_j].parent_i = i
                    cell_details[new_i][new_j].parent_j = j

                    #print("The destination cell is found")
                    # Trace and print the path from source to destination
                    new_path = trace_path(cell_details, dest, is_part_1)
                    found_dest = True
                    return found_dest, new_path
                else:
                    # Calculate the new f, g, and h values
                    g_new = cell_details[i][j].g + 1.0
                    h_new = calculate_h_value(new_i, new_j, dest)
                    f_new = g_new + h_new

                    # If the cell is not in the open list or the new f value is smaller
                    if cell_details[new_i][new_j].f == float('inf') or cell_details[new_i][new_j].f > f_new:
                        # Add the cell to the open list
                        heapq.heappush(open_list, (f_new, new_i, new_j))
                        # Update the cell details
                        cell_details[new_i][new_j].f = f_new
                        cell_details[new_i][new_j].g = g_new
                        cell_details[new_i][new_j].h = h_new
                        cell_details[new_i][new_j].parent_i = i
                        cell_details[new_i][new_j].parent_j = j

    # If the destination is not found after visiting all cells
    if not found_dest:
        #print("Failed to find the destination cell")
        return False, []

def main():
    grid=[['.' for _ in range(COL)] for _ in range(ROW)]

    falling_bytes = np.loadtxt('input.txt', dtype=int, delimiter=',')
    for element in falling_bytes[:1024]:
        grid[element[0]][element[1]] = '#'
    
    # Define the source and destination
    src = [0, 0]
    dest = [70, 70]

    # Run the A* search algorithm
    path_exist, path = a_star_search(grid, src, dest, is_part_1 = True)

    for element in falling_bytes[1024:]:
        grid[element[0]][element[1]] = '#'

        if (element[0], element[1]) in path:
            # Run the A* search algorithm
            path_exist, path = a_star_search(grid, src, dest)
            if not path_exist:
                print("Coordinates of the first byte preventing the exit from being reachable:", str(element[0]) + "," + str(element[1]))
                break
    
    print("Time elapsed:", datetime.now() - init_time)

if __name__ == "__main__":
    main()
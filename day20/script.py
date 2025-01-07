# Python program for A* Search Algorithm
import heapq
from datetime import datetime

init_time = datetime.now()

# Define the size of the grid
ROW = 141
COL = 141

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
    return grid[row][col] == '.' or grid[row][col] == 'S' or grid[row][col] == 'E'

# Check if a cell is the destination
def is_destination(row, col, dest):
    return row == dest[0] and col == dest[1]

# Calculate the heuristic value of a cell (Euclidean distance to destination)
def calculate_h_value(row, col, dest):
    return (((row - dest[0]) ** 2 + (col - dest[1]) ** 2) ** 0.5)

# Trace the path from source to destination
def trace_path(cell_details, dest):
    total = 0

    #print("The Path is ")
    path = []
    row = dest[0]
    col = dest[1]
    #print(row, col, orient)

    # Trace the path from destination to source using parent cells
    while not (cell_details[row][col].parent_i == row and cell_details[row][col].parent_j == col):
        path.append((row, col))
        temp_row = cell_details[row][col].parent_i
        temp_col = cell_details[row][col].parent_j
        row = temp_row
        col = temp_col
        #print(temp_row, temp_col)

    # Add the source cell to the path
    path.append((row, col))
    # Reverse the path to get the path from source to destination
    path.reverse()

    # Print the path
    '''
    for i in path:
        print("->", i, end=" ")
    '''
    return len(path), path

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
        #print(i, j, orientation)

        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        # For each direction, check the successors
        for dir in directions:
            new_i = i + dir[0]
            new_j = j + dir[1]

            # If the successor is valid, unblocked, and not visited
            if is_valid(new_i, new_j) and not closed_list[new_i][new_j]:
                # If the successor is the destination
                if is_destination(new_i, new_j, dest):
                    # Set the parent of the destination cell
                    cell_details[new_i][new_j].parent_i = i
                    cell_details[new_i][new_j].parent_j = j

                    #print("The destination cell is found")
                    # Trace and print the path from source to destination
                    cost, path = trace_path(cell_details, dest)
                    found_dest = True
                    return cost, path
                elif is_unblocked(grid, new_i, new_j):
                    # Calculate the new f, g, and h values
                    g_new = cell_details[i][j].g + 1.0
                    h_new = calculate_h_value(new_i, new_j, dest)
                    f_new = g_new + h_new

                    #print(f_new, new_i, new_j, new_orient)
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
        print("Failed to find the destination cell")
        return -1, []

# Driver Code


def main():
    grid=[['.' for _ in range(COL)] for _ in range(ROW)]

    with open('input.txt') as file:
        for index_i, line  in enumerate(file):
            for index_j, element in enumerate(line):
                if element != '\n':
                    grid[index_i][index_j] = element
                if element == 'S':
                    src = [index_i, index_j]
                if element == 'E':
                    dest = [index_i, index_j]

    # Run the A* search algorithm
    init_cost, init_path = a_star_search(grid, src, dest)

    min_time_gained = 100
    max_len_cheat_part1 = 2
    max_len_cheat_part2 = 20

    two_pico_cheats = []
    twenty_or_less_pico_cheats = []
    for index_start, start in enumerate(init_path):
        #print(index_start, 'out of', len(init_path)) #Uncomment this line to check the progress
        for index_end, end in enumerate(init_path[index_start+min_time_gained:]):
            if start != end:
                distance = abs(start[0] - end[0]) + abs(start[1] - end[1])
                if distance <= max_len_cheat_part1 and index_end - distance >= 0: 
                    two_pico_cheats.append((start, end))
                if distance <= max_len_cheat_part2 and index_end - distance >= 0: 
                    twenty_or_less_pico_cheats.append((start, end))

    print("Time elapsed:", datetime.now() - init_time)
    print("Total number of cheats of maximum length:", max_len_cheat_part1, "saving at least 100 picoseconds:", len(two_pico_cheats))
    print("Total number of cheats of maximum length:", max_len_cheat_part2, "saving at least 100 picoseconds:", len(twenty_or_less_pico_cheats))


if __name__ == "__main__":
    main()
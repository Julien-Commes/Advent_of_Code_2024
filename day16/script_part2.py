# Python program for A* Search Algorithm
import math
import heapq

# Define the size of the grid
ROW = 14
COL = 14

max_cost = 100000

# Define the Cell class
class Cell:
    def __init__(self):
      # Parent cell's row index
        self.parent_i = [0]
    # Parent cell's column index
        self.parent_j = [0]
    # Parent cell's orientation
        self.parent_orientation = [0]
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
    #print(h, ((row - dest[0]) ** 2 + (col - dest[1]) ** 2) ** 0.5)
    return h # --> To modify

# Trace the path from source to destination


def trace_path(cell_details, dest):
    total = 0

    print("The Path is ")
    path = []
    row = dest[0]
    col = dest[1]
    orient = 0
    #print(row, col, orient)

    # Trace the path from destination to source using parent cells
    while not (cell_details[row][col][orient].parent_i[-1] == row and cell_details[row][col][orient].parent_j[-1] == col and cell_details[row][col][orient].parent_orientation[-1] == orient):
        path.append((row, col, orient))

        print(cell_details[row][col][orient].parent_i, cell_details[row][col][orient].parent_j, cell_details[row][col][orient].parent_orientation)
        temp_row = cell_details[row][col][orient].parent_i[-1]
        temp_col = cell_details[row][col][orient].parent_j[-1]
        temp_orient = cell_details[row][col][orient].parent_orientation[-1]
        if row == dest[0] and col == dest[1]:
            total += 1
        elif temp_orient != orient:
            total += 1000
        else:
            total += 1
        row = temp_row
        col = temp_col
        orient = temp_orient
        #print(temp_row, temp_col, temp_orient)

    # Add the source cell to the path
    path.append((row, col, orient))
    # Reverse the path to get the path from source to destination
    path.reverse()

    # Print the path
    for i in path:
        print("->", i, end=" ")
    print(total)

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

                    #print(open_list)
                    print("The destination cell is found")
                    # Trace and print the path from source to destination
                    trace_path(cell_details, dest)
                    return
                else:
                    # Calculate the new f, g, and h values
                    added_cost = 1.0
                    if orientation != new_orient:
                        added_cost = 1000.0
                    new_cost = cell_details[i][j][orientation].cost + added_cost
                    
                    #print(f_new, new_i, new_j, new_orient)
                    # If the cell is not in the open list or the new f value is smaller
                    if (cell_details[new_i][new_j][new_orient].cost == float('inf') or cell_details[new_i][new_j][new_orient].cost >= new_cost) and new_cost <= max_cost:
                        # Add the cell to the open list
                        heapq.heappush(open_list, (new_cost, new_i, new_j, new_orient))
                        # Update the cell details
                        cell_details[new_i][new_j][new_orient].cost = new_cost
                        cell_details[new_i][new_j][new_orient].parent_i.append(i)
                        cell_details[new_i][new_j][new_orient].parent_j.append(j)
                        cell_details[new_i][new_j][new_orient].parent_orientation.append(orientation)

    # If the destination is not found after visiting all cells
    if not found_dest:
        print("Failed to find the destination cell")

# Driver Code


def main():
    grid=[]

    with open('input.txt') as file:
        for line in file:
            grid.append(line)

    # Define the source and destination
    src = [13, 1]
    dest = [1, 13]

    # Run the A* search algorithm
    a_star_search(grid, src, dest)


if __name__ == "__main__":
    main()
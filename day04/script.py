import numpy as np

data = np.loadtxt("input.txt", dtype=str)

def check_direction(mat, dir, id_row, id_col):

    """
    Directions map:
        5    6    7
             |
        4 <--X--> 0
             |
        3    2    1
    """

    match dir:
        case 0:
            contains_xmas = (mat[id_row][id_col + 1] == "M") * (mat[id_row][id_col + 2] == "A") * (mat[id_row][id_col + 3] == "S") 
        case 1:
            contains_xmas = (mat[id_row + 1][id_col + 1] == "M") * (mat[id_row + 2][id_col + 2] == "A") * (mat[id_row + 3][id_col + 3] == "S") 
        case 2:
            contains_xmas = (mat[id_row + 1][id_col] == "M") * (mat[id_row + 2][id_col] == "A") * (mat[id_row + 3][id_col] == "S")
        case 3:
            contains_xmas = (mat[id_row + 1][id_col - 1] == "M") * (mat[id_row + 2][id_col - 2] == "A") * (mat[id_row + 3][id_col - 3] == "S")
        case 4:
            contains_xmas = (mat[id_row][id_col - 1] == "M") * (mat[id_row][id_col - 2] == "A") * (mat[id_row][id_col - 3] == "S")
        case 5:
            contains_xmas = (mat[id_row - 1][id_col - 1] == "M") * (mat[id_row - 2][id_col - 2] == "A") * (mat[id_row - 3][id_col - 3] == "S")
        case 6:
            contains_xmas = (mat[id_row - 1][id_col] == "M") * (mat[id_row - 2][id_col] == "A") * (mat[id_row - 3][id_col] == "S")
        case 7:
            contains_xmas = (mat[id_row - 1][id_col + 1] == "M") * (mat[id_row - 2][id_col + 2] == "A") * (mat[id_row - 3][id_col + 3] == "S")

    return contains_xmas

sum = 0
for i in range(len(data)):
    for j in range(len(data[0])):

        if data[i][j] == "X":
            directions = []
            if i > 2 :
                directions.append(6)
                if j > 2:
                    directions.append(5)
                    directions.append(4)
                if j < len(data[0]) - 3: 
                    directions.append(7)
                    directions.append(0)
            if i < len(data) - 3: 
                directions.append(2)
                if j > 2:
                    directions.append(3)
                    directions.append(4)
                if j < len(data[0]) - 3:
                    directions.append(1)
                    directions.append(0)
        
            directions = list(dict.fromkeys(directions))

            #print(i, j, directions)

            for direction in directions:
                sum += check_direction(data, direction, i, j)

print(sum)
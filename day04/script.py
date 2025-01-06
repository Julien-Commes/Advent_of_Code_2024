import numpy as np
from datetime import datetime

init_time = datetime.now()

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

sum_xmas = 0
sum_crossed_mas = 0

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
                sum_xmas += check_direction(data, direction, i, j)
            
            contains_crossed_mas = False
        
        elif i < len(data) - 2 and j < len(data[0]) - 2 and data[i][j] == "M":
            contains_as = check_direction(data, 1, i-1, j-1)
            other_cross_mas = check_direction(data, 3, i-1, j+3)
            other_cross_sam = check_direction(data, 7, i+3, j-1)

            contains_crossed_mas = contains_as * (other_cross_mas + other_cross_sam)
        
        elif i < len(data) - 2 and j < len(data[0]) - 2 and data[i][j] == "S":
            contains_am = check_direction(data, 5, i+3, j+3)
            other_cross_mas = check_direction(data, 3, i-1, j+3)
            other_cross_sam = check_direction(data, 7, i+3, j-1)

            contains_crossed_mas = contains_am * (other_cross_mas + other_cross_sam)
        
        else: 
            contains_crossed_mas = False
        
        sum_crossed_mas += contains_crossed_mas
        

print("Time elapsed:", datetime.now() - init_time)
print("Number of XMAS occurences:", sum_xmas)
print("Number of X-MAS occurences:", sum_crossed_mas)
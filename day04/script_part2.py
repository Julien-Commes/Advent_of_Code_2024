import numpy as np

data = np.loadtxt("input.txt", dtype=str)

sum = 0
for i in range(len(data) - 2):
    for j in range(len(data[0]) - 2):

        if data[i][j] == "M":
            contains_as = (data[i + 1][j + 1] == "A") * (data[i + 2][j + 2] == "S")
            other_cross_mas = (data[i][j + 2] == "M") * (data[i + 2][j] == "S")
            other_cross_sam = (data[i][j + 2] == "S") * (data[i + 2][j] == "M")
            
            contains_xmas = contains_as * (other_cross_mas + other_cross_sam)

            #print(i, j, contains_xmas)

        elif data[i][j] == "S":
            contains_am = (data[i + 1][j + 1] == "A") * (data[i + 2][j + 2] == "M")
            other_cross_mas = (data[i][j + 2] == "M") * (data[i + 2][j] == "S")
            other_cross_sam = (data[i][j + 2] == "S") * (data[i + 2][j] == "M")
            
            contains_xmas = contains_am * (other_cross_mas + other_cross_sam)

            #print(i, j, contains_xmas)
        
        else:
            contains_xmas = False

        sum += contains_xmas
        
print(sum)
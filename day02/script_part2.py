import numpy as np

#  Initialiser les listes pour chaque colonne
data = []
count = 0
line_ind = 0

# Lire le fichier ligne par ligne
with open("input.txt", "r") as file:
    for line in file:
        values = line.split()  # Diviser la ligne en éléments
        values_diff = [int(x) - int(y) for x, y in zip(values[1:], values [:-1])] 

        incr = []
        decr = []
        zeros = []
        
        for index, value in enumerate(values_diff):
            if value > 0:
                incr.append(index)
            elif value < 0:
                decr.append(index)
        
        if len(incr) < len(decr):
            values_diff = [-x for x in values_diff]

        errors = []
        for index, value in enumerate(values_diff):
            if value < 1 or value > 3:
                errors.append(index) 

        if len(errors) == 0:
            count += 1
        elif len(errors) < 2:
            print(values_diff, values)
            if errors[0] == len(values_diff)-1 or errors[0] == 0:
                count += 1
            elif values_diff[errors[0]] + values_diff[errors[0] + 1] < 4 and values_diff[errors[0]] + values_diff[errors[0] + 1] > 0:
                count += 1
            elif values_diff[errors[0]] + values_diff[errors[0] - 1] < 4 and values_diff[errors[0]] + values_diff[errors[0] - 1] > 0:
                count += 1
        elif len(errors) == 2:
            if errors[0] + 1 == errors[1]:
                if values_diff[errors[0]] + values_diff[errors[1]] < 4 and values_diff[errors[0]] + values_diff[errors[1]] > 0:
                    count += 1

        line_ind += 1

print("count: ", count)
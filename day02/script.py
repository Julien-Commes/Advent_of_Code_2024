import numpy as np

#  Initialiser les listes pour chaque colonne
data = []
count = 0

# Lire le fichier ligne par ligne
with open("input.txt", "r") as file:
    for line in file:
        values = line.split()  # Diviser la ligne en éléments
        values_diff = [int(x) - int(y) for x, y in zip(values[1:], values [:-1])] 
        max = np.array(values_diff).max()
        min = np.array(values_diff).min()
        print(max, min)
        if max * min > 0 and np.max(np.array([abs(min),abs(max)])) < 4:
            count += 1

print("count: ", count)
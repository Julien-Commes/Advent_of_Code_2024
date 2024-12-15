import numpy as np

# Charger les données depuis le fichier txt
data = np.loadtxt("input.txt")

# Extraire les deux colonnes sous forme de listes
col1 = np.array(data[:, 0])
col2 = np.array(data[:, 1])

print("Colonne 1 :", col1[0])
print("Colonne 2 :", col2[0])

col1_sorted = np.sort(col1)
col2_sorted = np.sort(col2)


print(col2.sum() - col1.sum(), np.sum(np.abs(col2_sorted-col1_sorted)))

keys_dict = {}

for k in col2_sorted:
    if k in keys_dict:
        keys_dict[k] += 1
    else:
        keys_dict[k] = 1


sum = 0
for k in col1_sorted:
    sum += k * keys_dict[k] if k in keys_dict else 0

print(sum)
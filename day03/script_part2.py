import numpy as np
import re

data = []

# Lire le fichier ligne par ligne
with open('input.txt', 'r') as file:
    data = file.read()

filter = re.findall(r"(?:do)\(\)(.*?)(?:don't)\(\)", data)

new_data = "".join(filter)

result = re.findall(r"(?:mul)\(([0-9]{1,3})(?:,)([0-9]{1,3})\)", new_data)

mul = np.array([int(t[0]) * int(t[1]) for t in result])

print(np.sum(mul))
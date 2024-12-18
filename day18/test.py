import numpy as np

result = np.loadtxt('input.txt', dtype=int, delimiter=',')

print(result[0:1024, 0])
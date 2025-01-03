import numpy as np
from datetime import datetime

init_time = datetime.now()

data = np.loadtxt("input.txt", dtype=int)

col1 = np.array(data[:, 0])
col2 = np.array(data[:, 1])

col1_sorted = np.sort(col1)
col2_sorted = np.sort(col2)

unique_keys, counts = np.unique(col2_sorted, return_counts=True)
keys_dict = dict(zip(unique_keys, counts))

sum = np.sum([k * keys_dict.get(k, 0) for k in col1_sorted])

print("Time elapsed:", datetime.now() - init_time)
print("Total distance:", np.sum(np.abs(col1_sorted - col2_sorted)))
print("Similarity score:", sum)
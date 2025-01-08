import numpy as np
from datetime import datetime

init_time = datetime.now()

secret_numbers = np.loadtxt('input.txt', dtype=np.int64)
nb_buyer = secret_numbers.shape[0]
current_seq = np.zeros((nb_buyer, 4), dtype=np.int64)
prev_price = secret_numbers % 10
bananas_price_record = {}

for k in range(2000):
    #print(k+1, end='\r')
    secret_numbers = secret_numbers ^ (secret_numbers * 64) % 16777216
    secret_numbers = secret_numbers ^ (secret_numbers // 32) % 16777216 
    secret_numbers = secret_numbers ^ (secret_numbers * 2048) % 16777216

    new_price = secret_numbers % 10
    new_change = new_price - prev_price
    current_seq[:, :-1] = current_seq[:, 1:]
    current_seq[:, -1] = new_change

    if k >= 3:
        for i in range(nb_buyer):
            idx = tuple(current_seq[i])
            if idx not in bananas_price_record:
                bananas_price_record[idx] = np.zeros(nb_buyer, dtype=np.int64)
            if bananas_price_record[idx][i] == 0:
                bananas_price_record[idx][i] = new_price[i]

    prev_price = new_price

max_sum = max(np.sum(arr) for arr in bananas_price_record.values())

print("Time elapsed:", datetime.now() - init_time)
print("Sum of the 2000th secret numbers:", np.sum(secret_numbers))
print("Maximum number of bananas:", max_sum)
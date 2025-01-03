import numpy as np
from datetime import datetime

init_time = datetime.now()

def bitwise_XOR(A, B):
    binary_A = bin(A)[2:]
    binary_B = bin(B)[2:]

    new_bin_len = max(len(binary_A), len(binary_B))
    binary_A = format(A, '0' + str(new_bin_len) + 'b')
    binary_B = format(B, '0' + str(new_bin_len) + 'b')

    new_bin = ''
    for k in range(new_bin_len):
        digit_A = binary_A[k]
        digit_B = binary_B[k]

        if digit_A == digit_B:
            new_bin += '0'
        else:
            new_bin += '1'
    
    return int(new_bin, 2)

secret_numbers = np.loadtxt('input.txt', dtype=np.int64)
nb_buyer = secret_numbers.shape[0]
current_seq = np.zeros((nb_buyer, 4), dtype=np.int64)
prev_price = secret_numbers % 10
bananas_price_record = {}

for k in range(2000):
    print(k, end='\r')
    b = secret_numbers * 64
    secret_numbers = np.array([bitwise_XOR(a, b) for a, b in zip(secret_numbers, b)], dtype=np.int64)
    secret_numbers = secret_numbers % 16777216
    b = secret_numbers // 32
    secret_numbers = np.array([bitwise_XOR(a, b) for a, b in zip(secret_numbers, b)], dtype=np.int64)
    secret_numbers = secret_numbers % 16777216 
    b = secret_numbers * 2048
    secret_numbers = np.array([bitwise_XOR(a, b) for a, b in zip(secret_numbers, b)], dtype=np.int64)
    secret_numbers = secret_numbers % 16777216

    new_price = secret_numbers % 10
    new_change = new_price - prev_price 
    current_seq = current_seq[:, 1:]
    current_seq = np.column_stack((current_seq, new_change))

    if k >= 3:
        for i in range(len(current_seq)):
            idx = str(current_seq[i])
            if idx in bananas_price_record:
                if bananas_price_record[idx][i] == 0:
                    bananas_price_record[idx][i] = new_price[i]
            else:
                bananas_price_record[idx] = np.zeros(nb_buyer, dtype=np.int64)
                bananas_price_record[idx][i] = new_price[i]
    
    prev_price = new_price

max_sum = max(np.sum(arr) for arr in bananas_price_record.values())

print()
print(datetime.now() - init_time)
print("Sum of the 2000th secret numbers:", np.sum(secret_numbers))
print("Maximum number of bananas:", max_sum)
import numpy as np
from datetime import datetime

init_time = datetime.now()

data = np.loadtxt('input.txt', dtype=np.int64)

stones = {element: 1 for element in data}
epochs = 75
total_25_epochs = 0

for k in range(epochs):
    
    if k == 25:
        total_25_epochs = total

    new_stones = {}
    total = 0

    for stone_number in stones:

        if stone_number == 0:
            new_stones[1] = new_stones.get(1, 0) + stones[0]

            total += stones[0]

        elif len(str(stone_number))%2 == 0:
            first_half = int(str(stone_number)[:len(str(stone_number))//2])
            second_half = int(str(stone_number)[len(str(stone_number))//2:])
            new_stones[first_half] = new_stones.get(first_half, 0) + stones[stone_number]
            new_stones[second_half] = new_stones.get(second_half, 0) + stones[stone_number]
            
            total += 2 * stones[stone_number]
        
        else:
            new_number = stone_number * 2024
            new_stones[new_number] = new_stones.get(new_number, 0) + stones[stone_number]

            total += stones[stone_number]
    
    stones = new_stones

print("Time elapsed:", datetime.now() - init_time)
print("Number of stones after blinking 25 times:", total_25_epochs)
print("Number of stones after blinking 75 times:", total)
#stones = {17: 1, 125: 1}

stones = {41078: 1,
          18: 1,
          7: 1, 
          0: 1,
          4785508: 1,
          535256: 1,
          8154: 1,
          447: 1}

epochs = 75

for k in range(epochs):
    new_stones = {}
    total = 0
    for stone_number in stones:

        if stone_number == 0:
            if 1 in new_stones:
                new_stones[1] += stones[0]
            else:
                new_stones[1] = stones[0]

            total += stones[0]

        elif len(str(stone_number))%2 == 0:
            first_half = int(str(stone_number)[:len(str(stone_number))//2])
            second_half = int(str(stone_number)[len(str(stone_number))//2:])

            if first_half in new_stones:
                new_stones[first_half] += stones[stone_number]
            else:
                new_stones[first_half] = stones[stone_number]

            if second_half in new_stones:
                new_stones[second_half] += stones[stone_number]
            else:
                new_stones[second_half] = stones[stone_number]
            
            total += 2 * stones[stone_number]
        
        else:
            new_number = stone_number * 2024
            if new_number in new_stones:
                new_stones[new_number] += stones[stone_number]
            else:
                new_stones[new_number] = stones[stone_number]

            total += stones[stone_number]
    
    stones = new_stones

print(total)
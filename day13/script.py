import re
from datetime import datetime

init_time = datetime.now()

tot_part1 = 0
tot_part2 = 0

with open('input.txt') as file:
    for index, line in enumerate(file):
        match index % 4:
            case 0:
                move_A = re.findall(r'[0-9]+', line)
                move_A[0], move_A[1] = int(move_A[0]), int(move_A[1])
            case 1:
                move_B = re.findall(r'[0-9]+', line)
                move_B[0], move_B[1] = int(move_B[0]), int(move_B[1])
            case 2:
                target = re.findall(r'[0-9]+', line)
                target[0], target[1] = int(target[0]), int(target[1])
                target_part2 = target[0] + 10000000000000, target[1] + 10000000000000

                i, j = 0, 0
                det_moves = move_A[0] * move_B[1] - move_A[1] * move_B[0]
                if det_moves != 0:
                    i = (target[0] * move_B[1] - move_B[0] * target[1])//det_moves * ((target[0] * move_B[1] - move_B[0] * target[1])%det_moves == 0) * ((target[1] * move_A[0] - move_A[1] * target[0])%det_moves == 0)
                    j = (target[1] * move_A[0] - move_A[1] * target[0])//det_moves * ((target[1] * move_A[0] - move_A[1] * target[0])%det_moves == 0) * ((target[0] * move_B[1] - move_B[0] * target[1])%det_moves == 0)
                    i_part2 = (target_part2[0] * move_B[1] - move_B[0] * target_part2[1])//det_moves * ((target_part2[0] * move_B[1] - move_B[0] * target_part2[1])%det_moves == 0) * ((target_part2[1] * move_A[0] - move_A[1] * target_part2[0])%det_moves == 0)
                    j_part2 = (target_part2[1] * move_A[0] - move_A[1] * target_part2[0])//det_moves * ((target_part2[1] * move_A[0] - move_A[1] * target_part2[0])%det_moves == 0) * ((target_part2[0] * move_B[1] - move_B[0] * target_part2[1])%det_moves == 0)
                tot_part1 += 3 * i + j
                tot_part2 += 3 * i_part2 + j_part2 

print("Time elapsed:", datetime.now() - init_time)
print("Fewest tokens to win all possible prizes:", tot_part1)
print("Fewest tokens to win all possible prizes with correction on target:", tot_part2)
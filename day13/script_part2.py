import re
from datetime import datetime, timedelta

tot = 0

with open('input.txt') as file:
    for index, line in enumerate(file):
        match index % 4:
            case 0:
                move_A = re.findall(r'[0-9]+', line)
                move_A[0], move_A[1] = int(move_A[0]), int(move_A[1])
                #print(move_A)
            case 1:
                move_B = re.findall(r'[0-9]+', line)
                move_B[0], move_B[1] = int(move_B[0]), int(move_B[1])
                #print(move_B)
            case 2:
                target = re.findall(r'[0-9]+', line)
                target[0], target[1] = int(target[0]) + 10000000000000, int(target[1]) + 10000000000000

                #print(target)

                #init_time = datetime.now()
                i, j = 0, 0
                det_moves = move_A[0] * move_B[1] - move_A[1] * move_B[0]
                if det_moves != 0:
                    i = (target[0] * move_B[1] - move_B[0] * target[1])//det_moves * ((target[0] * move_B[1] - move_B[0] * target[1])%det_moves == 0) * ((target[1] * move_A[0] - move_A[1] * target[0])%det_moves == 0)
                    j = (target[1] * move_A[0] - move_A[1] * target[0])//det_moves * ((target[1] * move_A[0] - move_A[1] * target[0])%det_moves == 0) * ((target[0] * move_B[1] - move_B[0] * target[1])%det_moves == 0)
                #print(i, j)
                tot += 3 * i + j

                #end_time = datetime.now()
                #print(end_time - init_time)

print(tot)
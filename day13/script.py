import re

claw_machines = []
tot = 0

with open('example.txt') as file:
    for index, line in enumerate(file):
        match index % 4:
            case 0:
                move_A = re.findall(r'[0-9]+', line)
                #print(move_A)
            case 1:
                move_B = re.findall(r'[0-9]+', line)
                #print(move_B)
            case 2:
                target = re.findall(r'[0-9]+', line)
                #print(target)

                min = 401
                for i in range(100):
                    for j in range(100):
                        pos_X, pos_Y = i * int(move_A[0]) + j * int(move_B[0]), i * int(move_A[1]) + j * int(move_B[1])
                        if pos_X == int(target[0]) and pos_Y == int(target[1]):
                            if i * 3 + j < min:
                                min = i * 3 + j

                if min < 401:
                    tot += min

print(tot)


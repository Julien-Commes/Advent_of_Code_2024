from copy import copy

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

possible_A_curr_loop = [1, 2, 3, 4, 5, 6, 7]
test_program = [2,4,1,5,7,5,1,6,0,3,4,6,5,5,3,0]
test_program.reverse()

for k in range(len(test_program)):
    possible_A_next_loop = []

    for element in possible_A_curr_loop:
        output = test_program[k]

        candidate_A = element

        candidate_B = bitwise_XOR(candidate_A%8, 5)
        candidate_C = candidate_A//(2**candidate_B)

        candidate_B = bitwise_XOR(candidate_C, bitwise_XOR(candidate_B, 6))

        if candidate_B%8 == output:
            if k == len(test_program) - 1:
                print(candidate_A) 
            if candidate_A * 8 not in possible_A_next_loop:
                possible_A_next_loop.append(candidate_A * 8)
                possible_A_next_loop.append(candidate_A * 8 + 1)
                possible_A_next_loop.append(candidate_A * 8 + 2)
                possible_A_next_loop.append(candidate_A * 8 + 3)
                possible_A_next_loop.append(candidate_A * 8 + 4)
                possible_A_next_loop.append(candidate_A * 8 + 5)
                possible_A_next_loop.append(candidate_A * 8 + 6)
                possible_A_next_loop.append(candidate_A * 8 + 7)   

    
    possible_A_curr_loop = copy(possible_A_next_loop)
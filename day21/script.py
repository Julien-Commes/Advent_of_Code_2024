from datetime import datetime

init_time = datetime.now()

class instruction_pair:
    def __init__(self, pair, children_map):
        self.children = children_map[pair]
    
    def emulate_nth_robot_instruction(self, n, children_map, step_len_memo):
        instruction_sequence_len = 0
        if n == 1:
            return len(self.children)
        else:
            for child in self.children:
                if step_len_memo[child][n-1] == 0:
                    child_instruction_class = instruction_pair(child, children_map)
                    step_len_memo[child][n-1] = child_instruction_class.emulate_nth_robot_instruction(n-1, children_map, step_len_memo)
                instruction_sequence_len += step_len_memo[child][n-1]
            return instruction_sequence_len

step_len_memo = {key: [0]*25 for key in ['A_down', 'down_left', 'left_A', 'A_left', 'A_right', 'right_A', 'A_up', 'up_A', 'down_A', 'up_right', 'right_up', 'up_left', 'left_up', 'down_right', 'right_down', 'left_down', 'right_right', 'left_left', 'up_up', 'down_down', 'A_A']}

pairs_mapping = {'left_A': ['A_right', 'right_right', 'right_up', 'up_A'], 
                 'A_left': ['A_down', 'down_left', 'left_left', 'left_A'],
                 'A_right': ['A_down', 'down_A'],
                 'right_A': ['A_up', 'up_A'],
                 'A_up': ['A_left', 'left_A'],
                 'up_A': ['A_right', 'right_A'],
                 'A_down': ['A_left', 'left_down', 'down_A'],
                 'down_A': ['A_up', 'up_right', 'right_A'],
                 'up_right': ['A_down', 'down_right', 'right_A'],
                 'right_up': ['A_left', 'left_up', 'up_A'],
                 'up_left': ['A_down', 'down_left', 'left_A'],
                 'left_up': ['A_right', 'right_up', 'up_A'],
                 'down_right': ['A_right', 'right_A'],
                 'right_down': ['A_left', 'left_A'],
                 'left_down': ['A_right', 'right_A'],
                 'down_left': ['A_left', 'left_A'],
                 'right_right': ['A_A'],
                 'left_left': ['A_A'], 
                 'up_up': ['A_A'],
                 'down_down': ['A_A'],
                 'A_A': ['A_A'],
                 }

original_sequence_0 = ['A_left', 'left_up', 'up_up', 'up_up', 'up_A', 'A_left', 'left_A', 'A_right', 'right_right', 'right_A', 'A_down', 'down_down', 'down_down', 'down_A'] #['A_up', 'up_up', 'up_up', 'up_left', 'left_A', 'A_left', 'left_A', 'A_right', 'right_right', 'right_A', 'A_down', 'down_down', 'down_down', 'down_A'] 
original_sequence_1 = ['A_left', 'left_up', 'up_up', 'up_A', 'A_down', 'down_down', 'down_A', 'A_up', 'up_up', 'up_up', 'up_A', 'A_down', 'down_down', 'down_down', 'down_right', 'right_A'] #['A_up', 'up_up', 'up_left', 'left_A', 'A_down', 'down_down', 'down_A', 'A_up', 'up_up', 'up_up', 'up_A', 'A_down', 'down_down', 'down_down', 'down_right', 'right_A'] #['A_left', 'left_up', 'up_up', 'up_A', 'A_down', 'down_down', 'down_A', 'A_up', 'up_up', 'up_up', 'up_A', 'A_right', 'right_down', 'down_down', 'down_down', 'down_A']
original_sequence_2 = ['A_up', 'up_up', 'up_left', 'left_left', 'left_A', 'A_right', 'right_right', 'right_A', 'A_down', 'down_A', 'A_down', 'down_A'] #['A_left', 'left_up', 'up_up', 'up_A', 'A_down', 'down_down', 'down_A', 'A_up', 'up_up', 'up_up', 'up_A', 'A_right', 'right_down', 'down_down', 'down_down', 'down_A']
original_sequence_3 = ['A_left', 'left_up', 'up_up', 'up_A', 'A_up', 'up_right', 'right_A', 'A_down', 'down_down', 'down_A', 'A_down', 'down_A']
original_sequence_4 = ['A_up', 'up_left', 'left_left', 'left_A', 'A_up', 'up_up', 'up_right', 'right_A', 'A_right', 'right_A', 'A_down', 'down_down', 'down_down', 'down_A']

original_sequences = [[879, original_sequence_0], [508, original_sequence_1], [463, original_sequence_2], [593, original_sequence_3], [189, original_sequence_4]]
final_sequence_len_2 = 0
final_sequence_len_25 = 0

for original_sequence in original_sequences:
    for instruction in original_sequence[1]:
        instruction_class = instruction_pair(instruction, pairs_mapping)
        final_sequence_len_2 += original_sequence[0] * instruction_class.emulate_nth_robot_instruction(2, pairs_mapping, step_len_memo)
        final_sequence_len_25 += original_sequence[0] * instruction_class.emulate_nth_robot_instruction(25, pairs_mapping, step_len_memo)

print(datetime.now() - init_time)
print("Length of the shortest sequence with 2 keypads:", final_sequence_len_2)
print("Length of the shortest sequence with 25 keypads:", final_sequence_len_25)

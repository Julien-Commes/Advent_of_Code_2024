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

class Register:

    def __init__(self, A_value, B_value, C_value):
        self.A = A_value
        self.B = B_value
        self.C = C_value
    
    def get_combo_operand(self, operand):
        if operand < 4:
            return operand
        elif operand == 4:
            return self.A
        elif operand == 5:
            return self.B
        elif operand == 6:
            return self.C
        else:
            print("Not a valid operand")
            return 0
        
    def adv(self, operand):
        numerator = self.A
        denominator =  2 ** self.get_combo_operand(operand)
        self.A  = numerator//denominator

    def bxl(self, operand):
        self.B = bitwise_XOR(self.B, operand)

    def bst(self, operand):
        combo = self.get_combo_operand(operand)
        self.B = combo%8

    def jnz(self, operand, pointer):
        condition = (self.A == 0)
        if condition:
            return pointer + 2
        return 2 * operand

    def bxc(self):
        self.B = bitwise_XOR(self.B, self.C)

    def out(self, operand):
        combo = self.get_combo_operand(operand)
        return combo%8

    def bdv(self, operand):
        numerator = self.A
        denominator = 2 ** self.get_combo_operand(operand)
        self.B  = numerator//denominator

    def cdv(self, operand):
        numerator = self.A
        denominator = 2 ** self.get_combo_operand(operand)
        self.C = numerator//denominator

test_register = Register(51064159, 0, 0)
test_program = [2,4,1,5,7,5,1,6,0,3,4,6,5,5,3,0]
instruction_pointer = 0
max_pointer = len(test_program)

outputs=[]

while instruction_pointer < max_pointer:
    instruction = test_program[instruction_pointer]
    operand = test_program[instruction_pointer + 1]

    match instruction:
        case 0:
            test_register.adv(operand)
            instruction_pointer += 2
        case 1:
            test_register.bxl(operand)
            instruction_pointer += 2
        case 2:
            test_register.bst(operand)
            instruction_pointer += 2
        case 3:
            instruction_pointer = test_register.jnz(operand, instruction_pointer)
        case 4:
            test_register.bxc()
            instruction_pointer += 2
        case 5:
            output = test_register.out(operand)
            outputs.append(output)
            instruction_pointer += 2
        case 6:
            test_register.bdv(operand)
            instruction_pointer += 2
        case 7:
            test_register.cdv(operand)
            instruction_pointer += 2

print("Time elapsed:", datetime.now() - init_time)
print("Output values:", outputs)

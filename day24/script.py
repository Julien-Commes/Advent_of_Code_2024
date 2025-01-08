import re
from datetime import datetime

init_time = datetime.now()

registered_wires = {}
gates_dict = {}

with open("input_wires.txt") as file:
    for line in file:
        key, value = re.findall(r'\w+', line)
        registered_wires[key] = int(value)

fully_registered_gates = []
incomplete_gates = []
nb_missing_wires = []

with open("input_gates.txt") as file:
    for line in file:
        wire_1, operation, wire_2, resulted_wire = re.findall(r'\w+', line)
        gates_dict[resulted_wire] = [wire_1, wire_2, operation]
        wire_1_in_registered = wire_1 in registered_wires
        wire_2_in_registered = wire_2 in registered_wires
        if wire_1_in_registered and wire_2_in_registered:
            fully_registered_gates.append([wire_1, operation, wire_2, resulted_wire])
        else:
            incomplete_gates.append([wire_1, operation, wire_2, resulted_wire])
            nb_missing_wires.append(2 - wire_1_in_registered - wire_2_in_registered)

while(len(fully_registered_gates)) > 0:
    wire_1, operation, wire_2, resulted_wire = fully_registered_gates.pop(0)
    match operation:
        case "AND":
            value = int(registered_wires[wire_1] == 1 and registered_wires[wire_2] == 1)
        case "OR":
            value = int(registered_wires[wire_1] == 1 or registered_wires[wire_2] == 1)
        case "XOR":
            value = int(registered_wires[wire_1] != registered_wires[wire_2])
    
    registered_wires[resulted_wire] = value

    for index, gate in enumerate(incomplete_gates):
        if gate[0] == resulted_wire or gate[2] == resulted_wire:
            nb_missing_wires[index] -= 1
            if nb_missing_wires[index] == 0:
                fully_registered_gates.append(gate)

decimal_number_z = 0
z_range = 0

for key, value in registered_wires.items():
    if key[0] == 'z':
        decimal_number_z += value * 2**(int(key[1:]))
        if int(key[1:]) > z_range:
            z_range = int(key[1:])

errors = []
curr_z = 'z' + str(z_range)
curr_operation = gates_dict[curr_z]
if curr_operation[2] != 'OR':
    errors.append(curr_z)

for k in range(z_range-1, 0, -1):
    if k < 10:
        curr_z, curr_x, curr_y = 'z0' + str(k), 'x0' + str(k), 'y0' + str(k) 
    else:
        curr_z, curr_x, curr_y = 'z' + str(k), 'x' + str(k), 'y' + str(k) 
        
    curr_operation = gates_dict[curr_z]
    if curr_operation[2] != 'XOR' or curr_operation[0][0] == 'x' or curr_operation[1][0] == 'y':
        errors.append(curr_z)
    
    else:
        childs = curr_operation[:2]
        for child in childs:
            child_operation = gates_dict[child]
            if child_operation[2] == 'OR':
                grand_childs = child_operation[:2]
                for grand_child in grand_childs:
                    grand_child_operation = gates_dict[grand_child]
                    if grand_child_operation[2] != 'AND':
                        errors.append(grand_child)
            else:
                set_child = set(child_operation)
                expected_set = {'XOR', curr_x, curr_y}
                if set_child != expected_set:
                    if k == 1:
                        if set_child != {'AND', 'x00', 'y00'}:
                            errors.append(child)
                    else:
                        errors.append(child)

if set(gates_dict['z00']) != {'XOR', 'y00', 'x00'}:
    errors.append('z00')

sorted_answer = ''
for x in sorted(errors):
    sorted_answer += x + ','

print("Time elapsed:", datetime.now() - init_time)
print("Decimal number output on the wires starting with z:", decimal_number_z)
print("Eight wires involved in a swap:", sorted_answer[:-1])
import re

registered_wires = {}

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
        wire_1_in_registered = wire_1 in registered_wires
        wire_2_in_registered = wire_2 in registered_wires
        if wire_1_in_registered and wire_2_in_registered:
            fully_registered_gates.append([wire_1, operation, wire_2, resulted_wire])
        else:
            incomplete_gates.append([wire_1, operation, wire_2, resulted_wire])
            nb_missing_wires.append(2 - wire_1_in_registered - wire_2_in_registered)

#print(fully_registered_gates)

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
    #to_move_indexes = []

    for index, gate in enumerate(incomplete_gates):
        if gate[0] == resulted_wire or gate[2] == resulted_wire:
            nb_missing_wires[index] -= 1
            if nb_missing_wires[index] == 0:
                #to_move_indexes.append(index)
                fully_registered_gates.append(gate)

    """
    for index in to_move_indexes:
        del incomplete_gates[index]
        del nb_missing_wires[index]
    """

decimal_number_z = 0
decimal_number_x = 0
decimal_number_y = 0

for key, value in registered_wires.items():
    if key[0] == 'z':
        decimal_number_z += value * 2**(int(key[1:]))
    if key[0] == 'x':
        decimal_number_x += value * 2**(int(key[1:]))
    if key[0] == 'y':
        decimal_number_y += value * 2**(int(key[1:]))

print(decimal_number_z, decimal_number_x + decimal_number_y)

binary_number_z = bin(decimal_number_z)[2:]
binary_number_expected = bin(decimal_number_x + decimal_number_y)[2:]
indexes_of_different_bit = []

for i in range(len(binary_number_expected)):
    if binary_number_expected[i] != binary_number_z[i]:
        indexes_of_different_bit.append(len(binary_number_expected) - i - 1)

print(indexes_of_different_bit)




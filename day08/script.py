map = {"#": [],}

with open('input.txt', 'r') as file:
    i = 0
    for line in file:
        for j, element in enumerate(line):
            if element in map:
                map[element].append((i, j))
            elif element != "." and element != "\n":
                map[element] = [(i,j)]
        i += 1

max_index_i, max_index_j = i, j + 1

def compute_dist(point_A: tuple, point_B: tuple) -> tuple:
    x_dist, y_dist = point_A[1] - point_B[1], point_A[0] - point_B[0]
    return (x_dist, y_dist)

for antena_type in map:
    if antena_type != "#":
        antenas = map[antena_type]
        for index, antena in enumerate(antenas):     
            if index == len(antenas) - 1:
                other_antenas = antenas[:index]
            else:    
                other_antenas = antenas[:index] + antenas[index+1:]
            for other_antena in other_antenas:
                x_dist, y_dist = compute_dist(antena, other_antena)
                pot_i, pot_j =  antena[0] + y_dist, antena[1] + x_dist
                
                if pot_i < max_index_i and pot_i >= 0 and pot_j < max_index_j and pot_j >= 0:
                    if (pot_i, pot_j) not in map['#']:
                        map['#'].append((pot_i, pot_j))
                
print(len(map['#']))
import copy
from datetime import datetime

init_time = datetime.now()
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
map_part1 = copy.deepcopy(map)

def compute_dist(point_A: tuple, point_B: tuple) -> tuple:
    x_dist, y_dist = point_A[1] - point_B[1], point_A[0] - point_B[0]
    return (x_dist, y_dist)

def generate_potential_antinodes(max_i, max_j, origin_point, y_dist, x_dist) -> list:
    antenas = []
    k = 0
    candidate =  origin_point[0] + k * y_dist, origin_point[1] + k * x_dist
    while candidate[0] < max_i and candidate[0] >= 0 and candidate[1] < max_j and candidate[1] >= 0:
        antenas.append(candidate)
        k += 1
        candidate = origin_point[0] + k * y_dist, origin_point[1] + k * x_dist
    return antenas

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
                    if (pot_i, pot_j) not in map_part1['#']:
                        map_part1['#'].append((pot_i, pot_j))

                new_antinodes = generate_potential_antinodes(max_index_i, max_index_j, antena, y_dist, x_dist)
                for antinode in new_antinodes:              
                    if antinode not in map['#']:
                        map['#'].append(antinode)


print("Time elapsed:", datetime.now() - init_time)   
print("Number of antinodes:", len(map_part1['#']))             
print("Number of antinodes with harmonics:", len(map['#']))
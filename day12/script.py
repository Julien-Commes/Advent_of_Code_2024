import numpy as np
from datetime import datetime

init_time = datetime.now()

image = np.loadtxt('input.txt', dtype=str)

class UnionFind:
    def __init__(self):
        self.parent = {}

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x]) 
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.parent[root_y] = root_x 

    def add(self, x):
        if x not in self.parent:
            self.parent[x] = x


def connected_components_labeling(image):
    rows, cols = len(image), len(image[0])
    labels = [[0 for _ in range(cols)] for _ in range(rows)]
    uf = UnionFind()
    current_label = 1

    for i in range(rows):
        for j in range(cols):
            neighbors = []

            if i > 0 and image[i][j] == image[i-1][j]:
                neighbors.append(labels[i-1][j])
                
            if j > 0 and image[i][j] == image[i][j-1]:
                neighbors.append(labels[i][j-1])

            if not neighbors:
                labels[i][j] = current_label
                uf.add(current_label)
                current_label += 1
            else:
                min_label = min(neighbors)
                labels[i][j] = min_label

                for neighbor in neighbors:
                    uf.union(min_label, neighbor)

    for i in range(rows):
        for j in range(cols):
            labels[i][j] = uf.find(labels[i][j])
    return labels

labels = connected_components_labeling(image) #Find distinct regions in the input 

def is_not_label(element, label):
    return element != label

def count_edges_vertices(map, i, j, label): #Count added perimeter and perimeter w/ discount per pixel in region (i.e., number of edges and vertices)
    nb_vertices = 0
    nb_edges = 0
    border_left, border_right, border_up, border_down = i > 0, i < len(map)-1, j > 0, j < len(map[0])-1

    corner_1 = is_not_label(map[i-1][j-1], label) if border_left and border_up else 1
    neighbours_1 = (is_not_label(map[i-1][j], label) if border_left else 1) + (is_not_label(map[i][j-1], label) if border_up else 1)

    corner_2 = is_not_label(map[i-1][j+1], label) if border_left and border_down else 1
    neighbours_2 = (is_not_label(map[i-1][j], label) if border_left else 1) + (is_not_label(map[i][j+1], label) if border_down else 1) 

    corner_3 = is_not_label(map[i+1][j-1], label) if border_right and border_up else 1
    neighbours_3 = (is_not_label(map[i+1][j], label) if border_right else 1) + (is_not_label(map[i][j-1], label) if border_up else 1)

    corner_4 = is_not_label(map[i+1][j+1], label) if border_right and border_down else 1
    neighbours_4 = (is_not_label(map[i+1][j], label) if border_right else 1) + (is_not_label(map[i][j+1], label) if border_down else 1)

    corners, neighbours = [corner_1, corner_2, corner_3, corner_4], [neighbours_1, neighbours_2, neighbours_3, neighbours_4]

    for corner, neighbour in zip(corners, neighbours):
        nb_vertices += 2 * ((neighbour + corner) == 3) + (neighbour == 1) * (corner == 0) +  2 * (neighbour == 2) * (corner == 0) # 2 times the number of vertices added by the pixel as it shares vertices with other pixels
    nb_edges = neighbours_1 + neighbours_4

    return nb_edges, nb_vertices

regions = {}

for i in range(len(labels)):
    for j in range(len(labels[0])):
        label = labels[i][j]
        nb_edges, nb_vertices = count_edges_vertices(labels, i, j, label) 

        if label in regions:
            regions[label][0] += 1
            regions[label][1] += nb_edges
            regions[label][2] += nb_vertices

        else:
            regions[label] = [1, nb_edges, nb_vertices]

sum_part1 = sum(value[0] * value[1] for value in regions.values())
sum_part2 = sum(value[0] * (value[2]//2) for value in regions.values()) # Divided by 2 because we counted 2 time each vertices (as some vertices are shared between 2 pixels)

print("Time elapsed:", datetime.now() - init_time)
print("Total price of fences:", sum_part1)
print("Total price of fences with discount:", sum_part2)
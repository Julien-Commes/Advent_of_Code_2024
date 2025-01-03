import networkx as nx
import numpy as np
from datetime import datetime

init_time = datetime.now()

connected_laptops = np.loadtxt('input.txt', dtype=str, delimiter ='-', usecols=(0,1))

# Map laptops ids with row/columns of the adjacency matrix
curr_index = 0
laptops_indexes = {}
laptops_indexes_reversed = {}
for connection in connected_laptops:
    if connection[0] not in laptops_indexes:
        laptops_indexes[connection[0]] = curr_index
        laptops_indexes_reversed[curr_index] = connection[0]
        curr_index += 1
    if connection[1] not in laptops_indexes:
        laptops_indexes[connection[1]] = curr_index
        laptops_indexes_reversed[curr_index] = connection[1]
        curr_index += 1

adjacency_matrix = np.zeros((curr_index + 1, curr_index + 1))

# Establish edges in the adjacency matrix (0 -> No edge, 1 -> edge)
for edges in connected_laptops:
    adjacency_matrix[laptops_indexes[edges[0]]][laptops_indexes[edges[1]]] = 1
    adjacency_matrix[laptops_indexes[edges[1]]][laptops_indexes[edges[0]]] = 1

# Create graph from adjacency matrix
G = nx.from_numpy_array(adjacency_matrix)

# Find all cliques (Subset of vertices of an undirected graph such that every two distinct vertices in the clique are adjacent.)
all_cliques = list(nx.enumerate_all_cliques(G))

# Isolate cliques with exactly three nodes and at least one starts with "t"
three_or_more = [[laptops_indexes_reversed[clique[0]], laptops_indexes_reversed[clique[1]], laptops_indexes_reversed[clique[2]]] for clique in all_cliques if len(clique) == 3]
three_or_more_with_t = [clique for clique in three_or_more if (clique[0][0] == 't' or clique[1][0] == 't' or clique[2][0] == 't')]

# Get the clique of maximal length
max_clique = max(all_cliques, key=len)

# Transform the clique into the corresponding password
max_clique_id = []
for element in max_clique:
    max_clique_id.append(laptops_indexes_reversed[element]) 
sorted_answer = ''
for x in sorted(max_clique_id):
    sorted_answer += x + ','

print("Time elapsed:", datetime.now() - init_time)
print("Number of sets of three inter-connected computers:", len(three_or_more_with_t))
print("Password is:", sorted_answer[:-1])
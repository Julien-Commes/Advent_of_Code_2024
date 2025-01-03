import numpy as np

connected_laptops = np.loadtxt('input.txt', dtype=str, delimiter ='-', usecols=(0,1))
set_mutual_connections = []

count = 0
i = 0

for connection in connected_laptops:
    print(i, end='\r')

    temp_set_mutual_connections = set_mutual_connections.copy()
    for index, set_connection in enumerate(set_mutual_connections):
        if connection[0] in set_connection:
            if connection[1] not in set_connection and len(set_connection) < 3:
                temp_set_mutual_connections.append(set_connection)
                temp_set_mutual_connections[index] = np.append(set_mutual_connections[index], connection[1])

            elif connection[1] in set_connection and len(set_connection) == 3:
                has_t = False
                for element in set_connection:
                    if element[0] == 't':
                        has_t = True
                
                count += has_t
                
        elif connection[1] in set_connection:
            if len(set_connection) < 3:
                temp_set_mutual_connections.append(set_connection)
                temp_set_mutual_connections[index] = np.append(set_mutual_connections[index], connection[0])
        
    temp_set_mutual_connections.append(connection)
    set_mutual_connections = temp_set_mutual_connections.copy()
    i += 1

print()
print(count)
def trouver_tous_les_chemins(labyrinthe, depart, arrivee):
    rows, cols = len(labyrinthe), len(labyrinthe[0])
    chemins = []
    chemin_actuel = []
    
    def dfs(x, y):
        # Si on sort des limites ou si la case est un mur (0), on arrête
        if not (0 <= x < rows and 0 <= y < cols) or labyrinthe[x][y] == '#':
            return
        
        # Ajouter le point actuel au chemin
        chemin_actuel.append((x, y))
        
        # Si on atteint l'arrivée, ajouter une copie du chemin actuel
        if (x, y) == arrivee:
            chemins.append(list(chemin_actuel))
        else:
            # Marquer le point comme visité en le changeant temporairement en 0
            labyrinthe[x][y] = '#'
            
            # Explorer les quatre directions : haut, bas, gauche, droite
            dfs(x + 1, y)
            dfs(x - 1, y)
            dfs(x, y + 1)
            dfs(x, y - 1)
            
            # Restaurer le point pour permettre d'autres explorations
            labyrinthe[x][y] = '.'
        
        # Retirer le point actuel du chemin avant de revenir en arrière
        chemin_actuel.pop()
    
    dfs(*depart)
    return chemins

def compute_cost_path(path):
    cost = 0
    dir = 0
    for k in range(len(path) - 1):
        cost += 1
        move = path[k+1][0] - path[k][0], path[k+1][1] - path[k][1]

        new_dir = 0
        match move:
            case (0, 1):
                new_dir = 0
            case (-1, 0):
                new_dir = 1
            case (0, -1):
                new_dir = 2
            case (1, 0):
                new_dir = 3
        
        diff_dir = abs(dir - new_dir)
        if diff_dir == 3:
            diff_dir = 1
        cost += 1000 * diff_dir

        dir = new_dir

    return cost

COL = 141
ROW = 141

labyrinthe = [['' for _ in range(COL)] for _ in range(ROW)]
with open('input.txt') as file:
    for index_i, line in enumerate(file):
        for index_j, element in enumerate(line):
            if element != '\n':
                labyrinthe[index_i][index_j] = element

depart = (139, 1)  # Point de départ
arrivee = (1, 139)  # Point d'arrivée

chemins = trouver_tous_les_chemins(labyrinthe, depart, arrivee)

max_cost = 107512
tiles_on_best_path = []

for i, chemin in enumerate(chemins):
    print(f"Chemin {i + 1}")
    cost = compute_cost_path(chemin)

    if cost == max_cost:
        for element in chemin:
            if element not in tiles_on_best_path:
                tiles_on_best_path.append(element)

print(len(tiles_on_best_path), tiles_on_best_path)


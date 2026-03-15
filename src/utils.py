import math
import numpy as np

def load_tsp_instance(filepath):
    coords = []
    with open(filepath, 'r') as f:
        lines = f.readlines()
    start_reading = False
    for line in lines:
        if line.startswith("NODE_COORD_SECTION"):
            start_reading = True
            continue
        if line.startswith("EOF") or line.strip() == "1": break
        if start_reading:
            parts = line.strip().split()
            if len(parts) >= 3:
                coords.append((float(parts[1]), float(parts[2])))
    return coords

def calculate_distance_matrix(coords):
    n = len(coords)
    dist_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if i != j:
                dx = coords[i][0] - coords[j][0]
                dy = coords[i][1] - coords[j][1]
                # Arrondi standard TSPLIB EUC_2D pour la précision
                dist_matrix[i][j] = int(math.sqrt(dx**2 + dy**2) + 0.5)
    return dist_matrix

def calculate_tour_cost(tour, dist_matrix):
    cost = sum(dist_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))
    cost += dist_matrix[tour[-1]][tour[0]]
    return cost
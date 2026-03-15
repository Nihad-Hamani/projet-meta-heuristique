import random
import math
import time
from .utils import calculate_tour_cost

def two_opt_swap(tour, i, j):
    """Inverse le segment entre les indices i et j."""
    return tour[:i] + tour[i:j+1][::-1] + tour[j+1:]

def simulated_annealing(dist_matrix, initial_tour, initial_temp=10000, cooling_rate=0.99999, temps_max=10):
    start_time = time.time()
    n = len(initial_tour)
    
    current_tour = list(initial_tour)
    current_cost = 0 # On va utiliser le delta, mais on initialise le coût
    for i in range(n):
        current_cost += dist_matrix[current_tour[i]][current_tour[(i+1)%n]]
        
    best_tour = current_tour[:]
    best_cost = current_cost
    temp = initial_temp

    # On boucle tant qu'on a du temps ou que la température est correcte
    while temp > 0.001 and (time.time() - start_time) < temps_max:
        # 2-opt selection
        i, j = sorted(random.sample(range(n), 2))
        if i == 0 and j == n - 1: continue 

        # --- CALCUL DELTA O(1) ---
        prev_i = current_tour[i-1]
        v_i = current_tour[i]
        v_j = current_tour[j]
        next_j = current_tour[(j+1)%n]

        # Coût avant : (prev_i->v_i) + (v_j->next_j)
        # Coût après : (prev_i->v_j) + (v_i->next_j)
        delta = (dist_matrix[prev_i][v_j] + dist_matrix[v_i][next_j]) - \
                (dist_matrix[prev_i][v_i] + dist_matrix[v_j][next_j])

        # Metropolis
        if delta < 0 or random.random() < math.exp(-delta / temp):
            # Application de l'inversion 2-opt
            current_tour[i:j+1] = current_tour[i:j+1][::-1]
            current_cost += delta
            
            if current_cost < best_cost:
                best_cost = current_cost
                best_tour = current_tour[:]
        
        temp *= cooling_rate
            
    return best_tour, best_cost, time.time() - start_time
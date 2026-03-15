import time
from .utils import calculate_tour_cost

def nearest_neighbor(dist_matrix, start_node=0):
    start_time = time.time()
    n = len(dist_matrix)
    unvisited = set(range(n))
    unvisited.remove(start_node)
    tour = [start_node]
    current = start_node
    while unvisited:
        nxt = min(unvisited, key=lambda city: dist_matrix[current][city])
        tour.append(nxt)
        unvisited.remove(nxt)
        current = nxt
    return tour, calculate_tour_cost(tour, dist_matrix), time.time() - start_time
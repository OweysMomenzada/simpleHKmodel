import numpy as np

def squared_euclidean_distance(u, v):
    """
    Calculates the squared Euclidean distance between two vectors u and v.
    """
    distance = np.sum((u - v) ** 2)
    return distance


def energy_function(x_t):
    """
    Calculates the energy of the whole configuration
    """
    energies = []
    
    for j in x_t:
        for i in x_t:
            sed = squared_euclidean_distance(i, j)
            if sed >= 1:
                energies.append(1)
            else:
                energies.append(sed)
                
    return np.sum(energies)
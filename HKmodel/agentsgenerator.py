import random
import numpy as np

class RandomAgents:
    def __init__(self, n, dim, min_val, max_val):
        self.n = n
        self.dim = dim
        self.min_val = min_val
        self.max_val = max_val
        
    
    def generate_configuration(self):
        """
        Generates a list of n random numpy arrays of dimension dim, with each element of the arrays
        being a random number within the range [min_val, max_val].

        Args:
            n: The number of random vectors to generate.
            dim: The dimension of each vector.
            min_val: The minimum value for the elements of the vectors.
            max_val: The maximum value for the elements of the vectors.

        Returns:
            A list of n random numpy arrays.
        """
        return [np.random.uniform(self.min_val, self.max_val, size=self.dim) for i in range(self.n)]
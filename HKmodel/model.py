import math
import numpy as np
from IPython.display import clear_output


class HKmodel:
    def __init__(self, N_t, epsilon):
        self.N_t = N_t
        self.epsilon = epsilon
    
    def euclidean_distance(self, v1, v2):
        """
        Calculates the Euclidean distance between two vectors represented as lists.

        Args:
            v1: A list representing the first vector.
            v2: A list representing the second vector.

        Returns:
            The Euclidean distance between the two vectors.
        """
        assert len(v1) == len(v2), "Vectors must have the same dimension."

        squared_sum = sum((v1[i] - v2[i]) ** 2 for i in range(len(v1)))
        return math.sqrt(squared_sum)


    def freeze(self, conf1, conf2):
        """
        Returns a boolean if two configurations are equal

        Args:
            conf1: first configuration.
            conf2: second configuration.

        Returns:
            True or false
        """

        return all(np.array_equal(x, y) for x, y in zip(conf1, conf2))


    def updaterule_xt(self, x_t, N_t, epsilon):
        """
        Update rule for a single agent based on their neighborhood and an upperbound epsilon.

        Args:
            epsilon: upperbound.
            x_t: The agent which is going to be updated.
            N_t: A list of agents.

        Returns:
            updated value of x_t.
        """

        # list of the neighbor hood of x_t
        neighborhood = []

        # remove bias
        try:
            N_t = self.N_t.copy()
            N_t.remove(x_t)
        except:
            pass

        for agent in N_t:
            # only consider if its in neighborhood
            if self.euclidean_distance(x_t, agent) < self.epsilon:
                neighborhood.append(agent)

        try:
            normalizer = (1/len(neighborhood))
        except:
            normalizer = 1

        return normalizer*np.sum(neighborhood, axis=0)


    def update_configuration(self, N_t):
        """
        Update rule for whole configuration.

        Args:
            epsilon: upperbound.
            N_t: A list of agents.

        Returns:
            updated configuration for some step t.
        """
        new_N_t = []

        # apply update rule on whole configuration
        for x_t in N_t:
            res = self.updaterule_xt(x_t, N_t, self.epsilon)
            new_N_t.append(res)

        return new_N_t


    def update_untilfreeze(self):
        timestep = 0
        is_freezed = False

        # starts with initial configuration
        configurations = []
        configurations.append(self.N_t)

        while not is_freezed:
            print("Timestep:", timestep)
            res = self.update_configuration(configurations[-1])
            configurations.append(res)

            timestep += 1

            # stop if configuration did not change 
            is_freezed = self.freeze(configurations[-1], configurations[-2])
            clear_output(wait=True)

        return configurations
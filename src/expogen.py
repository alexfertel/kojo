import numpy as np

class Exp:
    def __init__(self, mean, lamb=False):
        self.mean = mean if not lamb else 1 / mean

    def inverse(self, u):
        return -self.mean * np.log(u)

    def generate(self):
        return self.generate_n(1)[0]

    def generate_n(self, n=1):
        result = []

        while len(result) < n:
            u = np.random.random()
            result.append(self.inverse(u))

        assert len(result) == n 
               
        return result

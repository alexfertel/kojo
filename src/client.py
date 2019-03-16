from numpy.random import randint, random

SANDWICH    = (3 * 60, 5 * 60)  # Food 0
SUSHI       = (5 * 60, 8 * 60)  # Food 1

class Client:
    def __init__(self, index, food):
        self.index = index
        self.food = food
        # self.served_by = -1  # Who served this client?

        self.at = 0  # Arrival time
        self.dt = 0  # Departure time
        self.delta = 0

    def __repr__(self):
        return f"{self.index}: {'Sushi' if self.food else 'Sandwich'}"
    
    def __str__(self):
        return repr(self)

    def generate_wait_time(self):
        if self.food:  # This client's food is sushi
            return randint(*SUSHI)
        else:
            return randint(*SANDWICH)

    def update_delta(self):
        self.delta = self.dt - self.at
        return self.delta

    @staticmethod
    def generate(index):
        return Client(f"client_{index}", 0 if random() < .5 else 1)

    
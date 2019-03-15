from heapq import *
from .client import Client
from .event import Event
from .expogen import Exp

import os

BIG_T           = 11 * 3600  # Closing time of the kitchen
EMPLOYEES_COUNT = 2          # I think this is self-explanatory
LAMBDA          = 1          # Exponential Random Variable Mean

class Kitchen:
    def __init__(self):
        self.t      = 0

        self.state  = {
            "client_count": 0,
            "arrivals": [],  # A
            "departures": [],  # D
            "queue": []
        }

        # Init heapq
        self.events = []

        # Generate first arrival
        self.arrival()

    def arrival(self):
        delta = Exp(LAMBDA).generate()
        arrival = Event(self.t + delta)
        client = Client.generate(self.state["client_count"])
        client.log(arrival)
        heappush(self.events, arrival)


    def run(self):
        while True:
            pass

    def log(self, *events):
        pass
    


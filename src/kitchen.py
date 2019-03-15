from heapq import *
from datetime import datetime, timedelta
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
        self.na     = 0
        self.nd     = 0

        self.state  = {
            "client_count": 0,
            "queue": []
        }
        self.servers    = [(False, None)] * EMPLOYEES_COUNT  # Is server `i` busy?
        self.C          = [0] * EMPLOYEES_COUNT  # How many clients each employee has served
        self.arrivals   = []  # A
        self.departures = []  # D

        # Init heapq
        self.events = []

        # Generate first arrival
        self.arrival()

        # Simulation
        self.history = []

    def __repr__(self):
        result = ''
        result += f'time: {}'
        sec = timedelta(seconds=)
        d = datetime(1, 1, 1) + sec

        print("DAYS:HOURS:MIN:SEC")
        print("%d:%d:%d:%d" % (d.day-1, d.hour, d.minute, d.second))


    def arrival(self):
        delta = Exp(LAMBDA).generate()
        arrival = Event(self.t + delta, 0)
        
        client = Client.generate(self.state["client_count"])
        arrival.pair(client)
        
        heappush(self.events, arrival)

    def departure(self, client):
        delta = client.generate_wait_time()
        departure = Event(self.t + delta, 1)

        departure.pair(client)
        
        heappush(self.events, departure)

    def run(self):
        while True:
            curevent = heappop(self.events)

            if curevent.time > BIG_T:  # We're closing the kitchen
                pass


            if curevent.nature == 0:  # Arrival
                self.t = curevent.time
                self.na += 1
                self.state["client_count"] += 1
                if self.state["client_count"] == 1:  # System was empty
                    self.servers[0] = True  # Put client in the first server
                    
                    self.departure(curevent.client)  # Generate departure event of this client
                elif (False, None) in self.servers:  # There's at least one free employee
                    for index, (isBusy, client) in enumerate(self.servers):
                        if not isBusy:
                            self.servers[index] = True, curevent.client
                            break

                    self.departure(curevent.client)  # Generate departure event of this client
                else:  # There's no free employee
                    self.state["queue"].append(curevent.client)  # Enqueue cient
                
                self.arrival()  # Generate next arrival
                self.arrivals[self.na] = self.t  # Arrival time of client `na` is `t`
                continue
            else:  # Departure
                self.t = curevent.time
                self.nd += 1
                self.state["client_count"] -= 1
                
                server = -1
                for index, (isBusy, client) in enumerate(self.servers):
                    if client == curevent.client:
                        server = index
                        self.servers[index] = (False, None)
                        break

                assert server >= 0

                self.C[server] += 1  # Employee `server` served one more client
                self.departures[self.nd] = self.t  # Departure time of client `nd` is `t`

                if self.state["client_count"] == 0:  # There was one client left
                    pass
                elif self.state["client_count"] <= EMPLOYEES_COUNT:  # There is no enqueued client. TODO: Check if it's `<`
                    pass
                else:  # There are clients enqueued
                    head = self.state["queue"].pop(0)  # Next client
                    self.servers[server] = True, head

                    self.departure(head)                    

                self.departures[curevent.client.index] = self.t
                continue



    def log(self, *events):

        log_file = 'kitchen_simulation'
        with open(f'logs/{log_file}.txt') as fd:

    


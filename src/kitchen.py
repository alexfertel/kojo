from heapq import heappush, heappop
from datetime import datetime, timedelta
from .client import Client
from .event import Event
from .expogen import Exp

import os

BIG_T           = 11 * 3600  # Closing time of the kitchen
EMPLOYEES_COUNT = 2          # I think this is self-explanatory
LAMBDA          = 1 * 120    # Exponential Random Variable Mean, five minutes

def timefsec(t):
    seconds = timedelta(seconds=t + 10 * 3600)
    stopwatch = datetime(1, 1, 1) + seconds

    return f"{stopwatch.hour}:{stopwatch.minute}:{stopwatch.second}"

class Kitchen:
    def __init__(self, upgraded=0):
        self.up     = upgraded

        self.t      = 0
        self.na     = 0
        self.nd     = 0

        self.state  = {
            "client_count": 0,
            "queue": []
        }

        self.servers    = [(False, None)] * EMPLOYEES_COUNT  # Is server `i` busy?
        self.C          = [0] * EMPLOYEES_COUNT              # How many clients each employee has served
        self.arrivals   = []                                 # A
        self.departures = []                                 # D

        # Handle third employee
        self.three = 0

        # Init heapq
        self.events = []

        # All clients
        self.clients = []

        # Generate first arrival
        self.arrival()

    def __repr__(self):
        result =  f"time: {timefsec(self.t)}\t" 
        result += f"clients: {self.state['client_count']}\n"
        return result

    def __str__(self):
        return repr(self)


    def arrival(self):
        lamb = LAMBDA
        if self.is_peak_hours:
            lamb = LAMBDA / 2  # As the mean decreases, the exponential parameter increases

        delta = Exp(lamb).generate()
        arrival = Event(self.t + delta, 0)
        
        client = Client.generate(self.state["client_count"])
        arrival.pair(client)
        
        heappush(self.events, arrival)
        self.clients.append(client)

    def departure(self, client):
        delta = client.generate_wait_time()
        departure = Event(self.t + delta, 1)

        departure.pair(client)
        
        heappush(self.events, departure)

    def run(self):
        while True:
            print(self.t, self.state['client_count'])
            self.log(str(self))

            if self.up:
                self.preprocess()

            curevent = heappop(self.events)
            if curevent.time > BIG_T:  # We're closing the kitchen
                break

            self.t = curevent.time
            if curevent.nature == 0:  # Arrival
                self.na += 1
                self.state["client_count"] += 1
                if self.state["client_count"] == 1:  # System was empty
                    self.servers[0] = True, curevent.client  # Put client in the first server
                    
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
                self.arrivals.append(self.t)  # Arrival time of client `na` is `t`
                curevent.client.at = self.t
                continue
            else:  # Departure
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
                self.departures.append(self.t)  # Departure time of client `nd` is `t`
                curevent.client.dt = self.t

                if server == EMPLOYEES_COUNT and not self.is_peak_hours:  # Last client employee `n + 1` will serve
                    self.remove_upgrade()
                    
                    assert len(self.servers) == EMPLOYEES_COUNT
                    assert len(self.C) == EMPLOYEES_COUNT
                    continue

                if self.state["client_count"] == 0:  # There was one client left
                    pass
                elif self.state["client_count"] <= EMPLOYEES_COUNT:  # There is no enqueued client. TODO: Check if it's `<`
                    pass
                else:  # There are clients enqueued
                    head = self.state["queue"].pop(0)  # Next client
                    self.servers[server] = True, head

                    self.departure(head)                    

                continue
        
        result = self.postprocess()
        self.log(result)

    def log(self, *args):
        log_file = 'kitchen_simulation'
        with open(f'logs/{log_file}.txt', '+a') as fd:
            for arg in args:
                fd.write(arg)
    
    def preprocess(self):
        if not self.three:
            if self.is_first_peak:
                self.three = 1            
                self.C.append(0)
                self.servers.append((False, None))
            if self.is_second_peak:
                self.three = 1            
                self.C.append(self.nd - sum(self.C))
                self.servers.append((False, None))

    def remove_upgrade(self):
        self.three = 0
        self.C = self.C[:-1]
        self.servers = self.servers[:-1]

    @property
    def is_first_peak(self):
        return (1.5 * 3600 <= self.t < 3.5 * 3600)

    @property
    def is_second_peak(self):
        return (7 * 3600 <= self.t < 9 * 3600)

    @property
    def is_peak_hours(self):
        return self.is_first_peak or self.is_second_peak

    def postprocess(self):
        # Compute spent time on the kitchen of every client
        self.deltas = [c.update_delta() for c in self.clients]
        
        # Prune negative deltas (They mean the client didn't get served)
        self.deltas = self.deltas[:len(self.departures)]

        # Assume that clients being served when closing were served before closing
        self.deltas = list(map(lambda delta: BIG_T - delta if delta < 0 else delta, self.deltas))

        func = lambda t: timefsec(t)

        # Convert to readable times
        readableA = [func(t) for t in self.arrivals]
        readableD = [func(t) for t in self.departures]

        # If we were testing a third employee, show it
        if self.up:
            self.C.append(self.nd - sum(self.C))

        assert sum(self.C) == self.nd

        result = f"\tNa = {self.na}\n"
        result += f"\tArrivals = {readableA}\n"
        result += f"\tNd = {self.nd}\n"
        result += f"\tDepartures = {readableD}\n"
        result += f"\tServed = {self.C}\n"
        result += f"\tDeltas = {self.deltas}\n"

        return result



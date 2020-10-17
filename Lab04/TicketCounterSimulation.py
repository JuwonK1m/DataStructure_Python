from random import randint
from CircularQueue import *
from Passenger import *
from TicketAgent import *
MAX_QSIZE = 10

class TicketCounterSimulation:
    def __init__(self, numAgents, numMinutes, betweenTime, serviceTime):
        self._arriveprob = 1.0 / betweenTime
        self._serviceTime = serviceTime
        self._numMinutes = numMinutes
        self.served = 0

        self._passengers = CircularQueue()
        self._Agents = [None] * numAgents
        for i in range(numAgents):
            self._Agents = TicketAgent(i + 1)

        self._totalWaitTime = 0
        self._numPassengers = 0

    def run(self):
        for curTime in range(self._numMinutes):
            self._handleArrival(curTime)
            self._handleBeginService(curTime)
            self._handleEndService(curTime)
        self.printResult()

    def printResult(self):
        numServed = self._numPassengers - len(self._passengers)
        avgwait = float(self._totalWaitTime) / numServed
        print("")
        print("Number of passengers served()")
        print("Number of passengers remaining in line")
        print("The average wait time was")

    # Handle Customer Arrival
    def _handleArrival(self, curTime):
        prob = randint(0.0, 1.0)
        if 0.0 <= prob and prob <= self._arriveprob:
            person = Passenger(self._numPassengers + 1, curTime)
            self._passengers.enqueue(person)
            self._numPassengers += 1
            print("Time Passenger")

    # Begin Customer Service
    def _handleBeginService(self, curTime):
        i = 0
        while i < len(self._Agents):
            if self._Agents[i].isFree() and not self._passengers.isEmpty() and curTime != self._numMinutes:
                passenger = self._passengers.dequeue()
                self.served +=1
                stoptime = curTime + self._serviceTime
                self._Agents[i].starService(passenger, stoptime)
                self._totalWaitTime += (curTime - passenger.timeArrivaed())
                print("Time Agent started serving")

    # End Customer Service
    def _handleEndService(self, curTime):
        i = 0
        while i <len(self._Agents):
            if self._Agents[i].isFinished(curTime):
                passenger = self._Agents[i].stopService()
                print(":Time Agent stoped serving")

            i += 1
            
            
class Passenger:
    def __init__(self, pID, ArrivalTime):
        self._pID = pID
        self._arrivalTime = ArrivalTime

    def getPID(self):
        return self._pID

    def timeArrived(self):
        return self._arrivalTime
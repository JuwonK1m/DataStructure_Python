class TicketAgent:
    def __init__(self, aID):
        self._aID = aID
        self._passenger = None
        self._stopTime = -1

    def getAID(self):
        return self._aID

    def isFree(self):
        return self._passenger is None

    def isFinished(self, CurTime):
        return self._passenger is not None and CurTime == self._stopTime

    def startService(self, passenger, stopTime):
        self._passenger = passenger
        self._stopTime = stopTime

    def stopService(self):
        thepassenger = self._passenger
        self._passenger = None
        return thepassenger
    
    
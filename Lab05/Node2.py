class Node2:
    def __init__(self, prev = None, data = None, nxt = None):
        self.prev = prev
        self.data = data
        self.next = nxt
    
    def __str__(self):
        return "(" + str(self.data) + ")"
    
    def setData(self, data):
        self.data = data
        
    def getData(self):
        return self.data
    
    def setPrev(self, prev):
        self.prev = prev
        
    def getPrev(self):
        return self.prev
    
    def setNext(self, nxt):
        self.next = nxt

    def getNext(self):
        return self.next
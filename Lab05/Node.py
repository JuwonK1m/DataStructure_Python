class Node:
    def __init__(self, data = None, nxt = None):
        self.data = data
        self.next = nxt
    
    def __str__(self):
        return "(" + str(self.data) + ")"
    
    def setData(self, data):
        self.data = data
        
    def getData(self):
        return self.data
    
    def setNext(self, nxt):
        self.next = nxt

    def getNext(self):
        return self.next
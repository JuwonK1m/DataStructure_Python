from CircularQueue import *
MAX_QSIZE = 10

class CircularDeque(CircularQueue):
    def __init__(self):
        super().__init__()
        
    def addFront(self, item):
        if not self.isFull():
            self.items[self.front] = item
            self.front = (self.front - 1 + MAX_QSIZE) % MAX_QSIZE
            
    def addRear(self, item):
        self.enqueue(item)
        
    def deleteFront(self):
        return self.dequeue()
        
    def deleteRear(self):
        if not self.isEmpty():
            item = self.items[self.rear]
            self.rear = (self.rear - 1 + MAX_QSIZE) % MAX_QSIZE
            return item
    
    def getFront(self, item):
        return self.peek()
        
    def getRear(self):
        return self.items[self.rear]
    
    
    
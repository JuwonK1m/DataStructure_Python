class Stack:
    def __init__(self):
        self.top = []
    
    def __contains__(self, item):
        return item in self.top
    
    def __iter__(self):
        return StackIterator(self.top)
    
    def __str__(self):
        return str(self.top)
    
    def push(self, item):
        self.top.append(item)
        
    def pop(self):
        if not self.isEmpty():
            return self.top.pop(-1)
            
    def peek(self):
        if not self.isEmpty():
            return self.top[-1]
    
    def isEmpty(self):
        return len(self.top) == 0
    
    def size(self):
        return len(self.top)

    def clear(self):
        self.top = []
        
    def display(self):
        print(str(self.top))
        
    def find(self, item):
        return item in self.top
        
class StackIterator:
    def __init__(self, theList = None):
        self.stackItems = theList
        self.curItem = 0
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.curItem < len(self.stackItems):
            item = self.stackItems[self.curItem]
            self.curItem += 1
            return item
        else:
            raise StopIteration
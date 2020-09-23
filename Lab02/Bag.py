class Bag:
    def __init__(self):
        self.bag = []
        
    def __contains__(self, item):
        return item in self.bag
    
    def __iter__(self):
        return BagIterator(self.bag)
    
    def __str__(self):
        s = "["
        cnt = 1   
        for it in self.bag:
            # No comma in first element
            if cnt == 1:
                s += str(it)
            else:
                s += (", " + str(it))
            cnt = cnt + 1
        s += "]"
        return s

    def __eq__(self, bag2):
        if len(self.bag) != len(bag2.bag):
            return False
        
        bag1_it = iter(self)
        bag2_it = iter(bag2)
        for i in range(0, len(self.bag)):
            if next(bag1_it) != next(bag2_it):
                return False
        return True
    
    def add(self, item):
        self.bag.append(item)
        
    def remove(self, item):
        assert item in self.bag, "The item is not in the bag."
        index = self.bag.index(item)
        return self.bag.pop(index)
        
class BagIterator:
    def __init__(self, theList = None):
        self.bagItems = theList
        self.curItem = 0
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.curItem < len(self.bagItems):
            item = self.bagItems[self.curItem]
            self.curItem += 1
            return item
        else:
            raise StopIteration
        
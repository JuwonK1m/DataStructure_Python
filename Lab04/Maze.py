from Stack import *
from CircularDeque import *
from Cell import *

class Maze:
    MAZE_SIZE = 6
    
    def getMap(self):
        map = [['1', '1', '1', '1', '1', '1'],
               ['e', '0', '1', '0', '0', '1'],
               ['1', '0', '0', '0', '1', '1'],
               ['1', '0', '1', '0', '1', '1'],
               ['1', '0', '1', '0', '0', 'x'],
               ['1', '1', '1', '1', '1', '1']]
        return map
    
    def isValidPos(self, x, y, map):
        if (x < 0 or y < 0 or x >= self.MAZE_SIZE or y >= self.MAZE_SIZE):
            return False
        else:
            return map[x][y] == '0' or map[x][y] == 'x'
        
    def DFS1(self):
        # Get map
        map = self.getMap()
        # Push(addFront) start data into circular deque
        deq = CircularDeque()
        entry = Cell(0, 1)
        deq.addFront(entry)
        print('\n DFS1: using Deque Data Structure: ')
        
        while not deq.isEmpty():
            here = deq.deleteFront()
            print(here, end = '->')
            x = here.row
            y = here.col
            if map[x][y] == 'x': # target point
                return True
            else:
                map[x][y] = '.' # Mark visited
                # Inspect to see if it can be moved to an adjacent location
                if self.isValidPos(x - 1, y, map):
                    deq.addFront(Cell(x - 1, y))
                if self.isValidPos(x + 1, y, map):
                    deq.addFront(Cell(x + 1, y))
                if self.isValidPos(x, y - 1, map):
                    deq.addFront(Cell(x, y - 1))
                if self.isValidPos(x, y + 1, map):
                    deq.addFront(Cell(x, y + 1))   
                    
        return False
    
    def DFS2(self):
        # Get map
        map = self.getMap()
        # Push start data into stack
        stack = Stack()
        entry = Cell(0, 1)
        stack.push(entry)
        print('\n DFS2: using Stack Data Structure: ')
        
        while not stack.isEmpty():
            here = stack.pop()
            print(here, end = '->')
            x = here.row
            y = here.col
            if map[x][y] == 'x': # target point
                return True
            else:
                map[x][y] = '.' # Mark visited
                # Inspect to see if it can be moved to an adjacent location
                if self.isValidPos(x - 1, y, map):
                    stack.push(Cell(x - 1, y))
                if self.isValidPos(x + 1, y, map):
                    stack.push(Cell(x + 1, y))
                if self.isValidPos(x, y - 1, map):
                    stack.push(Cell(x, y - 1))
                if self.isValidPos(x, y + 1, map):
                    stack.push(Cell(x, y + 1))
                
        return False
    
    def DFS3(self):
        # Get map
        map = self.getMap()
        # Push(addRear) start data into circular deque
        deq = CircularDeque()
        entry = Cell(0, 1)
        deq.addRear(entry)
        print('\n DFS3: using Deque Data Structure: ')
        
        while not deq.isEmpty():
            here = deq.deleteRear()
            print(here, end = '->')
            x = here.row
            y = here.col
            if map[x][y] == 'x': # target point
                return True
            else:
                map[x][y] = '.' # Mark visited
                # Inspect to see if it can be moved to an adjacent location
                if self.isValidPos(x - 1, y, map):
                    deq.addRear(Cell(x - 1, y))
                if self.isValidPos(x + 1, y, map):
                    deq.addRear(Cell(x + 1, y))
                if self.isValidPos(x, y - 1, map):
                    deq.addRear(Cell(x, y - 1))
                if self.isValidPos(x, y + 1, map):
                    deq.addRear(Cell(x, y + 1))     
                    
        return False
    
    def BFS1(self):
        # Get map
        map = self.getMap()
        # Push(addRear) start data into circular deque
        deq = CircularDeque()
        entry = Cell(0, 1)
        deq.addRear(entry)
        print('\n BFS1: using Deque Data Structure: ')
        
        while not deq.isEmpty():
            here = deq.deleteFront()   
            print(here, end = '->')
            x = here.row
            y = here.col
            if map[x][y] == 'x': # target point
                return True
            else:
                map[x][y] = '.' # Mark visited
                # Inspect to see if it can be moved to an adjacent location
                if self.isValidPos(x - 1, y, map):
                    deq.addRear(Cell(x - 1, y))
                if self.isValidPos(x + 1, y, map):
                    deq.addRear(Cell(x + 1, y))
                if self.isValidPos(x, y - 1, map):
                    deq.addRear(Cell(x, y - 1))
                if self.isValidPos(x, y + 1, map):
                    deq.addRear(Cell(x, y + 1))
                    
        return False
    
    def BFS2(self):
        # Get map
        map = self.getMap()
        # Push(enqueue) start data into queue.
        que = CircularQueue()
        entry = Cell(0, 1)
        que.enqueue(entry)
        print('\n BFS2: using Queue Data Structure: ')
        
        while not que.isEmpty():
            here = que.dequeue()   
            print(here, end = '->')
            x = here.row
            y = here.col
            if map[x][y] == 'x': # target point
                return True
            else:
                map[x][y] = '.' # Mark visited
                # Inspect to see if it can be moved to an adjacent location
                if self.isValidPos(x - 1, y, map):
                    que.enqueue(Cell(x - 1, y))
                if self.isValidPos(x + 1, y, map):
                    que.enqueue(Cell(x + 1, y))
                if self.isValidPos(x, y - 1, map):
                    que.enqueue(Cell(x, y - 1))
                if self.isValidPos(x, y + 1, map):
                    que.enqueue(Cell(x, y + 1))
                    
        return False
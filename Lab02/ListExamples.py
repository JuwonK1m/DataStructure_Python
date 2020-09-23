import random

class ListExamples:
    def dot_product(self, u, v):
        assert len(u) == len(v), "Both lists must be the same length."
            
        sum = 0
        for i in range(0, len(u)):
            sum += (u[i] * v[i])
        return sum
    
    def cross_product(self, u, v):
        assert len(u) == len(v) == 3, "Each list must be 3 in length."
        c = [u[1] * v[2] - u[2] * v[1], u[2] * v[0] - u[0] * v[2], u[0] * v[1] - u[1] * v[0]]
        return c
    
    def eightQueens(self):
        rng = random.Random()
        bd = list(range(8))
        num_found = 0
        tries = 0
        while num_found < 12 :
            rng.shuffle(bd)
            tries += 1
            if not self.has_clashes(bd):
                num_found += 1
                print("solution {} : {} in {} tries".format(num_found, bd, tries))
                tries = 0
    
    def has_clashes(self, board):
        for col in range (1, len(board)):
            if self.col_clashes(board, col):
                return True
        return False
    
    def col_clashes(self, bs, c):
        for i in range(c):
            if self.diagonal_clashes(i, bs[i], c, bs[c]):
                return True
        return False
    
    def diagonal_clashes(self, x0, y0, x1, y1):
        dy = abs(y1-y0)
        dx = abs(x1-x0)
        return dx==dy

import math

class Functions:
    def is_prime(self, n):
        if n == 1:
            return False
        # Eratosthenes approach
        i = 2
        while i <= math.sqrt(n):
            if n % i == 0:
                return False
            i = i + 1          
        return True
    
    def factorial(self, n):
        # Base case
        if n == 1:
            return 1
        # Recursive call
        return n * self.factorial(n - 1)
    
    def fibonacci(self, n):
        # Base case
        if n == 1 or n == 2:
            return 1
        # Recursive call        
        return self.fibonacci(n - 1) + self.fibonacci(n - 2)
    
    def getPTriples(self, n):
        # Triple loop
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                for k in range(1, n + 1):
                    if math.pow(i, 2) + math.pow(j, 2) == math.pow(k, 2):
                        print(str(i) + "^2 + " + str(j) + "^2 = " + str(k) + "^2") 
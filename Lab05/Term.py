class Term:
    def __init__(self, sgn=None, coeff=None, expon=None):
        self.sgn = sgn
        self.coeff = coeff
        self.expon = expon

    def __str__(self):
        return str(self.sgn) + str(self.coeff) + "x^" + str(self.expon) + " "

    def getCoeff(self):
        return self.coeff

    def getExpon(self):
        return self.expon

    def getSyn(self):
        return self.sgn
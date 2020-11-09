from DoublyLinkedList import *
from Term import *

class SparsePoly(DoublyLinkedList):
    def __init__(self):
        super().__init__()

    def display(self, msg=""):
        print("\t", msg, end='')

        node = self.head
        while node is not None:
            print(node, end='')
            node = node.getNext()
        print()

    def read(self):
        self.clear()
        while (True):
            token = input("input term (syn coef expon) :").split(" ")
            if token[0] == '-1':
                self.display("The Polynomial: ")
                return
            self.addAt(self.getSize(), Term(token[0], float(token[1]), int(token[2])))

    def getDegree(self):
        maxDegree = 0
        node = self.head

        while node is not None:
            temp = node.getData().getExpon()
            if temp > maxDegree:
                maxDegree = temp
            node = node.getNext()
        return maxDegree

    def add(self, B):
        C = SparsePoly()
        a = self.head
        b = B.head
        while a!=None or b!=None:
            if a==None or (b!=None and a.data.expon > b.data.expon):
                C.addAt(C.getSize(), Term(b.data.sgn,b.data.coeff,b.data.expon))
                b=b.getNext()
            elif b==None or (a!= None and b.data.expon > a.data.expon):
                C.addAt(C.getSize(), Term(a.data.sgn,a.data.coeff,a.data.expon))
                a=a.getNext()
            elif a.data.expon == b.data.expon:
                if(a.data.sgn == b.data.sgn):
                    C.addAt(C.getSize(),Term(a.data.sgn,a.data.coeff + b.data.coeff,a.data.expon))
                elif a.data.sgn == "-":
                    num = b.data.coeff - a.data.coeff
                    if(num < 0):
                        C.addAt(C.getSize(), Term(a.data.sgn, num, a.data.expon))
                    else:
                        C.addAt(C.getSize(), Term(b.data.sgn, num, a.data.expon))
                elif b.data.sgn == "-":
                    num = b.data.coeff - a.data.coeff
                    if (num < 0):
                        C.addAt(C.getSize(), Term(b.data.sgn, num, a.data.expon))
                    else:
                        C.addAt(C.getSize(), Term(a.data.sgn, num, a.data.expon))
                a = a.getNext()
                b = b.getNext()
        return C

    def sub(self, B):
        C = SparsePoly()
        a = self.head
        b = B.head
        while a != None or b != None:
            if a == None or (b != None and a.data.expon > b.data.expon):
                C.addAt(C.getSize(), Term(b.data.sgn, b.data.coeff, b.data.expon))
                b = b.getNext()
            elif b == None or (a != None and b.data.expon > a.data.expon):
                C.addAt(C.getSize(), Term(a.data.sgn, a.data.coeff, a.data.expon))
                a = a.getNext()
            elif a.data.expon == b.data.expon:
                if (a.data.sgn == b.data.sgn):
                    num = a.data.coeff - b.data.coeff
                    temp = ""
                    if(num < 0):
                        if a.data.sgn == "+":
                            temp = "-"
                        else:
                            temp = "+"
                    else:
                       temp = a.data.sgn
                    C.addAt(C.getSize(), Term(temp, -num, a.data.expon))
                else:
                    C.addAt(C.getSize(), Term(a.data.sgn, a.data.coeff + b.data.coeff, a.data.expon))
                a = a.getNext()
                b = b.getNext()
        return C
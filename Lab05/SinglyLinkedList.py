from Node import *

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        
    def __str__(self):
        temp = self.head
        string_repr = ""
        while temp:
            string_repr += str(temp) + "->"
            temp = temp.next
            
        return string_repr + "END"
        
    def addFront(self, data):
        newNode = Node(data) 
        if self.head == None:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode
        
    def addRear(self, data):
        if self.head == None:
            self.addFront(data)
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = Node(data)
        
    def addAt(self, pos, elem):
        before = self.getNodeAt(pos - 1)
        if before == None:
            self.head = Node(elem, self.head)
        else:
            node = Node(elem, before.next)
            before.next = node
        
    def deleteFront(self):
        temp = self.head
        if self.head:
            self.head = self.head.next
            temp.next = None
        return temp
        
    def deleteRear(self):
        tmp = self.head
        if self.head:
            if self.head.next is None:
                self.head = None
            else:
                while tmp.next.next:
                    tmp = tmp.next
                    
                second_last = tmp
                tmp = tmp.next
                second_last.next = None
        return tmp
        
    def deleteAt(self, pos):
        tmp = Node()
        if (self.isEmpty() or pos > self.getSize()):
            tmp = None
        elif pos == 0:
            tmp = self.deleteFront()
        elif pos == self.getSize():
            tmp = self.deleteRear()
        else:
            prev = self.getNodeAt(pos - 1)
            tmp = prev.next
            prev.next = tmp.next
            tmp.next = None
        return tmp
        
    def getNodeAt(self, pos):
        if pos < 0:
            return None
        node = self.head
        while pos > 0 and pos != None:
            node = node.next
            pos -= 1
        return node
        
    def printList(self, msg = 'Singly Linked List: '):
        print(msg, end = '')
        tmp = self.head
        while tmp:
            print(tmp.data, end = '->')
            tmp = tmp.next    
        print('END')
        
    def getDataAt(self, pos):
        node = self.getNodeAt(pos)
        if node == None:
            return None
        else:
            return node.data
        
    def replaceDataAt(self, pos, data):
        node = self.getNodeAt(pos)
        if node != None:
            node.data = data
        
    def isEmpty(self):
        return self.head == None
        
    def clear(self):
        self.head = None
        
    def getSize(self):
        node = self.head
        cnt = 0
        while node is not None:
            node = node.getNext()
            cnt += 1
        return cnt
        
    def reverseList(self):
        prev = None
        temp = self.head
        
        while temp:
            next_node = temp.next
            temp.next = prev
            prev = temp
            temp = next_node
        
        self.head = prev
        
    def findData(self, val):
        node = self.head
        while node is not None:
            if node.data == val: 
                return node
            node = node.next
        return node
        
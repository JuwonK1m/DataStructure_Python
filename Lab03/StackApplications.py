from Stack import Stack

class StackApplications:
    def checkBrackets(self, statement):
        s = Stack()
        for ch in statement:
            if ch == '{' or ch == '[' or ch == '(':
                s.push(ch)
            elif ch == '}' or ch == ']' or ch == ')':
                if s.isEmpty():
                    return False
                else:
                    left = s.pop()
                    if (ch == '}' and left != '{') or \
                       (ch == ']' and left != '[') or \
                       (ch == ')' and left != '(') :
                           return False                   
        return s.isEmpty()
    
    def evalPostfix(self, expr):
        s = Stack()
        for i in expr:
            if i == '+' or i == '-' or i == '*' or i == '/':
                val2 = s.pop()
                val1 = s.pop()
                if i == '+':
                    s.push(val1 + val2)
                elif i == '-':
                    s.push(val1 - val2)
                elif i == '*':
                    s.push(val1 * val2)
                elif i == '/':
                    s.push(val1 / val2)
            else:
                s.push(i)
        return s.pop()
    
    def precedence(self, op):
        if op == '(' or op == ')':
            return 0
        elif op == '+' or op == '-':
            return 1
        elif op == '*' or op == '/':
            return 2
        else:
            return -1

    def Infix2Postfix(self, expr):
        s = Stack()
        output = []
        for i in expr:
            if i == '(':
                s.push(i)
            elif i == ')':
                while not s.isEmpty():
                   op = s.pop()
                   if op == '(':
                       break
                   else:
                       output.append(op)
            elif i == '+' or i == '-' or i == '*' or i == '/':
                while not s.isEmpty():
                    op = s.peek()
                    if self.precedence(i) <= self.precedence(op):
                        output.append(op)
                        s.pop()
                    else:
                        break
                s.push(i)
            else:
                output.append(i)
           
        while not s.isEmpty():
            output.append(s.pop)
            
        return output
from LinkedLists import *

class StackLL():
    def __init__(self):
        self.LL=LL()

    def __str__(self):
        return str(self.LL)

    def Push(self, node):
        self.LL.AddHead(node)
        return

    def Peek(self):
        return self.LL.head

    def Pop(self):
        ret=self.LL.head
        self.LL.RemoveHead()
        return ret

class StackArray():
    def __init__(self):
        self.stack=[]

    def __str__(self):
        ret=""
        for i in range(len(self.stack)):
            ret+=str(self.stack[i]) + " "
        return ret

    def Push(self, node):
        self.stack.append(node)
        return

    def Pop(self):
        return self.stack.pop()

    def Peek(self):
        return self.stack[len(self.stack)]

#Test Code

"""
test=StackArray()
NodeD=LLNode("D")
NodeC=LLNode("C")
NodeB=LLNode("B")
NodeA=LLNode("A")
test.Push(NodeA)
test.Push(NodeB)
test.Push(NodeC)
test.Push(NodeD)
print(test)
print(test.Pop())
print(test)
"""

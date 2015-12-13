#Init of a Queue
#Enqueue
#Dequeing

from LinkedLists import *

class QueueLL():
    def __init__(self):
        self.LL=LL()

    def __str__(self):
        return str(self.LL)
       
    def Enqueue(self, node):
        LL.AddTail(self.LL, node)
        return

    def Dequeue(self):
        ret=self.LL.head
        self.LL.RemoveHead()
        return ret

class QueueArray():
    def __init__(self):
        self.q=[]

    def __str__(self):
        ret=""
        for i in range(len(self.q)):
            ret+=str(self.q[i])+" "
        return ret
    
    def Enqueue(self, node):
        self.q.append(node)
        return

    def Dequeue(self):
        return self.q.pop(0)


NodeD=LLNode("D")
NodeC=LLNode("C")
NodeB=LLNode("B")
NodeA=LLNode("A")
test=QueueArray()
test.Enqueue(NodeA)
test.Enqueue(NodeB)
test.Enqueue(NodeC)
test.Enqueue(NodeD)
print(test.Dequeue())
print(test)
  

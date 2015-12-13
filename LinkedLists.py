#Creating the node
#Updating the after node
#Updating the data in the node

#Creating the LL with head and tail values
#Removing the nth node from the LL
#Remove a specific node from the LL
#Remove head
#Remove tail
#Adding nth node to the LL
#Adding node to end of the LL
#Adding node to head the LL



class LLNode:
    def __init__(self, data=None, after=None):
        self.data=data
        self.after=after

    def __str__(self):
        return self.data
    
class LL():
    def __init__(self, head=None, tail=None):
        self.head=head
        self.tail=tail

    def __str__(self):
        current=self.head
        ret=""
        while (current != None):
            ret+=current.data+" "
            current=current.after
        return ret

    def RemoveNode(self, data):
        if self.head.data == data:
            self.head=self.head.after
            return

        current=self.head.after
        previous=self.head

        while current != None and current.data != data:
            current=current.after
            previous=previous.after
        if current.data != data:
            return False
        else:
            previous.after=current.after
            if current.after == None:
                self.tail=previous
                previous.after=None
                return

    def RemoveNodeN(self, n):
        if n==0:
            self.head=self.head.after
            return

        current=self.head.after
        previous = self.head
        n-=1
        
        while (n > 0 and current != None):
            n -= 1
            current=current.after
            previous=previous.after

        if n > 0:
            return False
        else:
            previous.after=current.after
            if current.after==None:
                self.tail=previous
                previous.after=None
            return

    def AddHead(self, node):
        prevHead=self.head
        if prevHead==None:
            self.tail=prevHead
        node.after=prevHead
        self.head=node
        return

    def AddTail(self, node):
        node.after=None
        if self.tail==None:
            self.tail=node
            self.head=node
        else:
            self.tail.after=node
            self.tail=node
        return

    def RemoveHead(self):
        self.RemoveNodeN(0)
        return

    def RemoveTail(self):
        if self.head==None:
            return False
        previous=self.head
        current=self.head.after

        while current.after != None:
            current=current.after
            previous=previous.after

        previous.after=None
        self.tail=previous

    
    def AddNodeToN(self, node, n):
        if n == 0:
            self.AddHead(node)

        n-=1
        current=self.head.after
        previous=self.head
    
        while (n > 0 and current != None):
            n-=1
            current=current.after
            previous=previous.after

        if n > 0:
            return False

        else:
            previous.after=node
            node.after=current
            if current.after==None:
                self.tail=node
            return


#Testing the Code

"""
NodeD=LLNode("D", None)
NodeC=LLNode("C", NodeD)
NodeB=LLNode("B", NodeC)
NodeA=LLNode("A", NodeB)
test=LL(NodeA, NodeD)
test.RemoveNode("B")
test.RemoveNodeN(1)
NodeE=LLNode("E")
NodeF=LLNode("F")
test.AddHead(NodeE)
test.AddTail(NodeF)
NodeG=LLNode("G")
test.AddNodeToN(NodeG, 3)
test.RemoveTail()
test.RemoveHead()
print(test)
"""
                
    

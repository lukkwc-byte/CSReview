from Trees import *

#init tree
#add node
#remove node

class BTree():
    def __init__(self, root=None):
        self.root=root

    def Find(self, node, data):
        if node.data==data:
            return True
        elif node.data > data and node.right:
            return BTree.Find(self, node.right, data)
        elif node.data < data and node.left:
            return BTree.Find(self, node.left, data)
        else:
            return False

    def Add(self, root, new):
        if root.data > new.data and root.left:
            BTree.Add(self, root.left, new)
        elif root.data < new.data and root.right:
            BTree.Add(self, root.right, new)
        elif root.data < new.data and not root.right:
            root.right = new
        else:
            root.left = new

    def Remove(self, r):
        current=self.root
        while current != r:
            if current.data < r.data and current.right:
                current=current.right
            elif current.data > r.data and current.left:
                current=current.left
            else:
                return False

        if not current.left and not current.right:
            if current.parent.right==current: current.parent.right=None
            else: current.parent.left=None

        elif current.left and not current.right:
            if current.parent.right==current: current.parent.right=current.left
            else: current.parent.left=current.left

        elif current.right and not current.left:
            if current.parent.right==current: current.parent.right=current.right
            else: current.parent.left=current.right

        else:
            rep=current
            while rep.right:
                rep=rep.right
            while rep.left:
                rep=rep.left
            temp=TreeNode(rep.data, current.left, current.right)

            if current.parent.right==rep: current.parent.right=None
            else: current.parent.left=None

            if current.parent.right==current: current.parent.right=temp
            else: current.parent.left=temp

#Test Code
"""
d=TreeNode(2)
e=TreeNode(5, None, None)
f=TreeNode(7)
g=TreeNode(9)
b=TreeNode(4, d, e)
c=TreeNode(9, f, g)
e.parent=b
a=TreeNode(6, b, c, None)
b.parent=a
c.parent=a
test=BTree(a)
h=TreeNode(3)
test.Remove(b)
print(a.left)

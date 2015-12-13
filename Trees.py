class TreeNode():
    def __init__(self, data=None, left=None, right=None):
        self.data=data
        self.left=left
        self.right=right

    def __str__(self):
        return str(self.data)


class Tree():
    def __init__(self, root=None):
        self.root=root

    def preorder(self, node):
        print(node)
        if node.left:
            Tree.preorder(self, node.left)
        if node.right:
            Tree.preorder(self, node.right)

    def inorder(self, node):
        if node.left: Tree.inorder(self, node.left)
        print(node)
        if node.right: Tree.inorder(self, node.right)

    def postorder(self, node):
        if node.left: Tree.postorder(self, node.left)
        if node.right: Tree.postorder(self, node.right)
        print(node)


d=TreeNode("D")
e=TreeNode("E")
f=TreeNode("F")
g=TreeNode("G")
b=TreeNode("B", d, e)
c=TreeNode("C", f, g)
a=TreeNode("A", b, c)
test=Tree(a)
test.inorder(test.root)

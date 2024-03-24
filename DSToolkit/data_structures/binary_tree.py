'''
A binary tree is a hierarchical data structure in which each node has at most two children,
referred to as the left child and the right child.
It is a specific type of tree where every node or vertex contains a key (value) and pointers to its left
and right children. The topmost node is known as the root node. Binary trees are used in various applications,
including implementing binary search trees and binary heaps, supporting operations like search, insert,
and delete with efficient time complexity.
'''


class BinaryTree:

    def __init__(self, data):

        self.data  = data
        self.right = None
        self.left  = None

    def Insert(self, data):

        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = BinaryTree(data)
                else:
                    self.left.Insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = BinaryTree(data)
                else:
                    self.right.Insert(data)
        else:
            self.data = data

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data)
        if self.right:
            self.right.PrintTree()

    # Left -> Root -> Right
    def InOrderTraversal(self, root):
        res = []
        if root:
            res = self.InOrderTraversal(root.left)
            res.append(root.data)
            res = res + self.InOrderTraversal(root.right)
        return res

    # Root -> Left -> Right
    def PreOrderTraversal(self, root):
        res = []
        if root:
            res.append( root.data )
            res = res + self.PreOrderTraversal(root.left)
            res = res + self.PreOrderTraversal(root.right)
        return res

    # Postorder traversal
    # Left -> Right -> Root
    def PostOrderTraversal(self, root):
        res = []
        if root:
            res = self.PostOrderTraversal(root.left)
            res = res + self.PostOrderTraversal(root.right)
            res.append(root.data)
        return res

    def InvertTree(self, root):

        self.__solveInvert(root)
        return root

    def __solveInvert(self, root):

        if not root:
            return

        root.left, root.right = root.right, root.left
        self.__solveInvert(root.left)
        self.__solveInvert(root.right)


bt = BinaryTree(10)
bt.Insert(8)
bt.Insert(7)
bt.Insert(11)
bt.Insert(15)
bt.Insert(3)
bt.PrintTree()


#print(bt.InOrderTraversal(bt))
#print(bt.PreOrderTraversal(bt))
#print(bt.PostOrderTraversal(bt))


new_bt = bt.InvertTree(bt)
#new_bt.PrintTree()


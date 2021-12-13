# Binary Tree . . .


class BinaryTree:

    def __init__(self, data):

        self.data = data
        self.right = None
        self.left = None

    def insert(self, data):

        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = BinaryTree(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = BinaryTree(data)
                else:
                    self.right.insert(data)
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
bt.insert(5)
bt.insert(7)
bt.insert(11)
bt.insert(15)
bt.PrintTree()


print(bt.InOrderTraversal(bt))
print(bt.PreOrderTraversal(bt))
print(bt.PostOrderTraversal(bt))


new_bt = bt.InvertTree(bt)
new_bt.PrintTree()


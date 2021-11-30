class TreeNode:

    def __init__(self, data=None):
        self.left = None
        self.data = data
        self.right = None

    def add(self, data):
        if data < self.data:
            if self.left:
                self.left.add(data)
            else:
                self.left = TreeNode(data)
        elif data > self.data:
            if self.right:
                self.right.add(data)
            else:
                self.right = TreeNode(data)

class BinaryTree:

    def __init__(self):
        self.root = None

    def add(self, data):
        if self.root is None:
            self.root = TreeNode(data)
        else:
            self.root.add(data)

    def contains(self, data):
        node = self.root
        while node:
            if data < node.data:
                node = node.left
            elif data > node.data:
                node = node.right
            else:
                return True
        return False

    def find(self, data):
        node = self.root
        while node:
            if data < node.data:
                node = node.left
            elif data > node.data:
                node = node.right
            else:
                return node
        return None

    def find_closest(self, data):
        pass

    def delete(self, data):
        pass
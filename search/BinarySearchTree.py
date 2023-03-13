import sys

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def dump(self):
        def printTree(node):
            if node is not None:
                print("Value: {}".format(node.value))
                printTree(node.left)
                printTree(node.right)
        printTree(self.root)

    def _insert(self, curNode, value):
        if curNode is None:
            curNode = Node(value)
            print(f"New Node Value: {value}")
            return curNode
        else:
            if curNode.value > value:
                curNode.left = self._insert(curNode.left, value)
            elif curNode.value < value:
                curNode.right = self._insert(curNode.right, value)
        return curNode
    def insert(self, value):
        self.root = self._insert(self.root, value)

ls = [2, 1, 5, 7, 3]
print(ls)

bt = BST()
for i in range(len(ls)):
    bt.insert(ls[i])
    bt.dump()
    print("-------")

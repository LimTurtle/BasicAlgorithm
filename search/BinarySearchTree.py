import sys

class Node:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def dump(self):
        def printTree(node):
            if node is not None:
                print("Value: {}".format(node.val))
                printTree(node.left)
                printTree(node.right)
        printTree(self.root)

    def insert(self, val):
        self.root = self._insert(self.root, val)
        return self.root is not None

    def _insert(self, node, val):
        if node is None:
            return Node(val)

        if val < node.val:
            node.left = self._insert(node.left, val)
        else:
            node.right = self._insert(node.right, val)

        return node

    # def insert(self, value):
    #     def _insert(curNode, value):
    #         if curNode is None:
    #             curNode = Node(value)
    #             #print(f"New Node Value: {value}")
    #             return
    #         else:
    #             if curNode.value > value:
    #                 _insert(curNode.left, value)
    #             elif curNode.value < value:
    #                 _insert(curNode.right, value)
    #
    #     if self.root is None:
    #         self.root = Node(value)
    #         return
    #
    #     _insert(self.root, value)

ls = [2, 1, 5, 7, 3]
print(ls)

bt = BST()
for i in range(len(ls)):
    bt.insert(ls[i])
    bt.dump()
    print("-------")

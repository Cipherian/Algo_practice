"""
Write a function that takes in a binary tree and a node contained in that tree and returns the node's successor.
"""

class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent
      
    def __str__(self):
        return str(self.value)


def findSuccessor(tree, node):
    if node.right is not None: # if the node has a right child
        current = node.right
        while current.left is not None:
            current = current.left
        return current
    else: # if the node has no right child
        current = node
        while current.parent is not None and current.parent.right == current: # go up until finding a node that is the left child of its parent
            current = current.parent
        return current.parent
    
"""
The function first checks if the given node has a right child. If it does, the function goes right once and then goes left until reaching the leftmost node. That leftmost node is the successor of the original node.

If the given node does not have a right child, the function goes up the tree until finding a node that is the left child of its parent. The parent of that node is the successor of the original node.
"""

if __name__ == "__main__":
    bt = BinaryTree(1)
    bt.left = BinaryTree(2)
    bt.right = BinaryTree(3)
    bt.left.left = BinaryTree(4)
    bt.left.right = BinaryTree(5)
    bt.right.left = BinaryTree(6)
    bt.right.right = BinaryTree(7)
    bt.left.right.left = BinaryTree(8)
    bt.left.right.right = BinaryTree(9)

    print(findSuccessor(bt, bt.left.right)) # input: 4 -> output: 9
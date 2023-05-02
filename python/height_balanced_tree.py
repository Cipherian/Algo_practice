"""
Write a function that takes in a binary tree and returns the number of nodes in the tree and returns True if the tree is balanced and False if it is not.
A binary tree is balanced if the heights of the two subtrees of every node never differ by more than 1.
"""

import unittest

class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def heightBalancedBinaryTree(tree):
    if tree is None:
        return True
    
    # recursive case: a tree is balanced if both of its subtrees are balanced and the height difference between them is at most 1
    leftHeight = get_height(tree.left)
    rightHeight = get_height(tree.right)
    if abs(leftHeight - rightHeight) > 1:
        return False
    else:
        return heightBalancedBinaryTree(tree.left) and heightBalancedBinaryTree(tree.right)

def get_height(node):
    # base case: the height of an empty node is 0
    if node is None:
        return 0
    
    # recursive case: the height of a non-empty node is 1 + the maximum height of its subtrees
    leftHeight = get_height(node.left)
    rightHeight = get_height(node.right)
    return 1 + max(leftHeight, rightHeight)

class TestHeightBalancedBinaryTree(unittest.TestCase):
    def test_heightBalancedBinaryTree(self):
        bt = BinaryTree(1)
        bt.left = BinaryTree(2)
        bt.right = BinaryTree(3)
        bt.left.left = BinaryTree(4)
        bt.left.right = BinaryTree(5)
        bt.right.left = BinaryTree(6)
        self.assertTrue(heightBalancedBinaryTree(bt))
        bt2 = BinaryTree(1)
        bt2.left = BinaryTree(2)
        bt2.right = BinaryTree(3)
        bt2.left.left = BinaryTree(4)
        bt2.left.right = BinaryTree(5)
        bt2.right.left = BinaryTree(6)
        bt2.left.left.left = BinaryTree(7)
        bt2.left.left.left.left = BinaryTree(8)
        bt2.left.left.left.left.left = BinaryTree(9)
        self.assertFalse(heightBalancedBinaryTree(bt2))


if __name__ == "__main__":
    unittest.main()
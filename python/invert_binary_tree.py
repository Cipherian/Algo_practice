"""
Write a function that takes in a binary tree and inverts it.
"""
import unittest
# This is the class of the input binary tree.


class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    def __str__(self):
        return f"({str(self.left)} <- {str(self.value)} -> {str(self.right)})"


def invertBinaryTree(tree):
    if tree is None:
        return
    
    # Swap the left and right subtrees
    tree.left, tree.right = tree.right, tree.left
    
    # Recursively invert the left and right subtrees
    invertBinaryTree(tree.left)
    invertBinaryTree(tree.right)

class TestBinaryTree(unittest.TestCase):
    def test_invert_binary_tree(self):
        tree = BinaryTree(1)
        tree.left = BinaryTree(2)
        tree.right = BinaryTree(3)
        tree.left.left = BinaryTree(4)
        tree.left.right = BinaryTree(5)
        tree.right.left = BinaryTree(6)
        tree.right.right = BinaryTree(7)
        invertBinaryTree(tree)
        self.assertEqual(4, tree.right.right.value)
        self.assertEqual(7, tree.left.left.value)



if __name__ == '__main__':
    unittest.main()



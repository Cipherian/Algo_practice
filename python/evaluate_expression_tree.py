"""
You're given a binary expression tree, write a function which takes in a binary tree and returns a single resulting integer.
 All leaf nodes in the tree represent operands, which will always be positive integers, all other nodes represent operators. -1 is addition adding the left and right subtrees. 
-2 is subtraction subtracting the right tree from the left tree, -3 is division dividing the left tree by the right subtree, 04 is multiplication multiplying the left and right subtree.
"""
import math
import unittest

class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def evaluateExpressionTree(tree):
    operators = {
        -1: lambda x, y: x + y,
        -2: lambda x, y: x - y,
        -3: lambda x, y: math.floor(x / y),
        -4: lambda x, y: x * y
    }
    
    if tree.value >= 0:
        return tree.value
    
    left_val = evaluateExpressionTree(tree.left)
    right_val = evaluateExpressionTree(tree.right)
    
    return operators[tree.value](left_val, right_val)


class TestBinaryTree(unittest.TestCase):

    def setUp(self):
        self.tree1 = BinaryTree(1)
        self.tree2 = BinaryTree(-1, BinaryTree(2), BinaryTree(3))

    def test_evaluateExpressionTree(self):
        self.assertEqual(evaluateExpressionTree(self.tree1), 1)

        self.assertEqual(evaluateExpressionTree(self.tree2), 5)
      
        


if __name__ == "__main__":
    unittest.main()

